#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETAIL = ROOT / "detail"
OUT = ROOT / "data" / "summary" / "protein_full_names.tsv"
ENGINEERING = ROOT / "audit_work" / "engineering"
OUT.parent.mkdir(parents=True, exist_ok=True)
ENGINEERING.mkdir(parents=True, exist_ok=True)

FIELDS = ["gene", "uniprot_id", "protein_full_name", "source", "confidence", "updated_at"]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_gene(path: Path, text: str) -> str:
    m = re.search(r"^gene:\s*[\"']?([^\"'\n]+)", text, re.I | re.M)
    return (m.group(1).strip() if m else path.name.removesuffix("-evaluation.md"))


def clean_name(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip().strip("*")
    value = re.sub(r"\s+\{[^}]+\}$", "", value).strip()
    return value


def parse_name(text: str) -> str:
    patterns = [
        r"\|\s*\*{0,2}蛋白全(?:名|称)\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"\|\s*\*{0,2}Protein Name\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"\|\s*\*{0,2}Protein full name\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"\*\*Protein Name:\*\*\s*([^\n]+)",
        r"\*\*Protein full name:\*\*\s*([^\n]+)",
        r"Protein Name:\s*([^\n]+)",
        r"^#\s+[A-Za-z0-9._-]+\s+\(([^)]+)\)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I | re.M)
        if not m:
            continue
        name = clean_name(m.group(1))
        if name and len(name) <= 220:
            return name
    return ""


def parse_uniprot_id(text: str) -> str:
    patterns = [
        r"\|\s*\*{0,2}UniProt ID\*{0,2}\s*\|\s*([A-Z0-9]+)",
        r"\bUniProt(?:KB)?(?:\s+ID)?\s*[:|]\s*([A-Z0-9]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            return m.group(1).strip()
    return ""


def load_existing() -> dict[str, dict[str, str]]:
    if not OUT.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    with OUT.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            gene = (row.get("gene") or "").strip()
            if gene:
                rows[gene.casefold()] = {k: row.get(k, "") for k in FIELDS}
    return rows


def collect_local_rows() -> dict[str, dict[str, str]]:
    rows = load_existing()
    today = dt.date.today().isoformat()
    for path in sorted(DETAIL.glob("*/*/*-evaluation.md")):
        text = read_text(path)
        gene = parse_gene(path, text)
        key = gene.casefold()
        current = rows.get(key, {k: "" for k in FIELDS})
        name = parse_name(text)
        uniprot_id = parse_uniprot_id(text)
        if not current.get("gene"):
            current["gene"] = gene
        if uniprot_id and not current.get("uniprot_id"):
            current["uniprot_id"] = uniprot_id
        if name and (not current.get("protein_full_name") or current.get("confidence") in {"", "LOW"}):
            current["protein_full_name"] = name
            current["source"] = "detail_report"
            current["confidence"] = "HIGH"
            current["updated_at"] = today
        rows[key] = current
    return rows


def fetch_uniprot_table(organism_id: str) -> list[dict[str, str]]:
    fields = "accession,reviewed,protein_name,gene_primary,gene_synonym,organism_id"
    query = f"(organism_id:{organism_id})"
    params = urllib.parse.urlencode({"compressed": "false", "format": "tsv", "fields": fields, "query": query})
    url = "https://rest.uniprot.org/uniprotkb/stream?" + params
    with urllib.request.urlopen(url, timeout=120) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    reader = csv.DictReader(lines, delimiter="\t")
    return list(reader)


def add_uniprot_names(rows: dict[str, dict[str, str]]) -> int:
    today = dt.date.today().isoformat()
    wanted = {row["gene"].casefold() for row in rows.values() if row.get("gene")}
    best: dict[str, tuple[int, dict[str, str]]] = {}
    rank_reviewed = {"reviewed": 0, "unreviewed": 1}
    for organism_rank, organism_id in enumerate(["9606", "10090"]):
        for item in fetch_uniprot_table(organism_id):
            primary = (item.get("Gene Names (primary)") or item.get("Gene Names") or "").strip()
            synonyms = (item.get("Gene Names (synonym)") or "").split()
            names = [primary] + synonyms
            protein_name = clean_name(item.get("Protein names") or "")
            accession = (item.get("Entry") or "").strip()
            reviewed = (item.get("Reviewed") or "").strip().lower()
            if not protein_name:
                continue
            for gene_name in names:
                key = gene_name.casefold()
                if key not in wanted:
                    continue
                score = organism_rank * 10 + rank_reviewed.get(reviewed, 5)
                if key not in best or score < best[key][0]:
                    best[key] = (score, {
                        "uniprot_id": accession,
                        "protein_full_name": protein_name,
                        "source": f"UniProt:{organism_id}",
                        "confidence": "MEDIUM" if organism_id == "9606" else "LOW",
                    })
        time.sleep(0.5)
    filled = 0
    for key, (_, item) in best.items():
        row = rows[key]
        if row.get("protein_full_name"):
            continue
        row["uniprot_id"] = row.get("uniprot_id") or item["uniprot_id"]
        row["protein_full_name"] = item["protein_full_name"]
        row["source"] = item["source"]
        row["confidence"] = item["confidence"]
        row["updated_at"] = today
        filled += 1
    return filled


def write_rows(rows: dict[str, dict[str, str]]) -> None:
    ordered = sorted(rows.values(), key=lambda r: r.get("gene", "").casefold())
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        for row in ordered:
            writer.writerow({k: row.get(k, "") for k in FIELDS})
    missing = [r for r in ordered if not r.get("protein_full_name")]
    summary = ENGINEERING / f"protein_full_names_summary_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    summary.write_text(
        "\n".join([
            "# Protein Full Names Summary",
            "",
            f"- Rows: {len(ordered)}",
            f"- With protein_full_name: {len(ordered) - len(missing)}",
            f"- Missing protein_full_name: {len(missing)}",
            f"- Output: {OUT.relative_to(ROOT)}",
            "",
            "## Missing genes",
            "",
            "\n".join(f"- {r.get('gene')}" for r in missing[:500]),
        ]),
        encoding="utf-8",
    )
    print(f"rows={len(ordered)} with_names={len(ordered)-len(missing)} missing={len(missing)} output={OUT}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build protein full-name lookup table from reports and optional UniProt data.")
    parser.add_argument("--fetch-uniprot", action="store_true", help="Download human and mouse UniProt TSV data to fill missing names.")
    args = parser.parse_args()
    rows = collect_local_rows()
    if args.fetch_uniprot:
        filled = add_uniprot_names(rows)
        print(f"uniprot_filled={filled}")
    write_rows(rows)


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()
