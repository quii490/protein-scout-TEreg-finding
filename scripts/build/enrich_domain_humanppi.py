#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETAIL = ROOT / "detail"
DOCS_INDEX = ROOT / "docs" / "data" / "protein_report_index.json"
ENGINEERING = ROOT / "audit_work" / "engineering"
ENGINEERING.mkdir(parents=True, exist_ok=True)

TS = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = "protein-scout-TEreg-finding/1.0 (+domain-humanppi audit)"
BLOCK_START = "<!-- DOMAIN_HUMANPPI_REPAIR_START -->"
BLOCK_END = "<!-- DOMAIN_HUMANPPI_REPAIR_END -->"


def request_text(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def split_tsv(text: str) -> list[dict[str, str]]:
    rows = list(csv.DictReader(text.splitlines(), delimiter="\t"))
    return rows


def get_uniprot_domain(gene: str) -> dict[str, str]:
    fields = "accession,gene_primary,protein_name,xref_smart,ft_domain,xref_interpro,xref_pfam"
    base = "https://rest.uniprot.org/uniprotkb/search"
    queries = [
        f"gene_exact:{gene} AND organism_id:9606 AND reviewed:true",
        f"gene_exact:{gene} AND organism_id:9606",
    ]
    last_error = ""
    for query in queries:
        url = base + "?" + urllib.parse.urlencode({"query": query, "format": "tsv", "fields": fields})
        try:
            rows = split_tsv(request_text(url))
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            continue
        if not rows:
            continue
        row = rows[0]
        return {
            "uniprot": row.get("Entry", ""),
            "protein_name": row.get("Protein names", ""),
            "smart": row.get("SMART", ""),
            "domain_ft": row.get("Domain [FT]", ""),
            "interpro": row.get("InterPro", ""),
            "pfam": row.get("Pfam", ""),
            "uniprot_error": "",
        }
    return {"uniprot": "", "protein_name": "", "smart": "", "domain_ft": "", "interpro": "", "pfam": "", "uniprot_error": last_error or "uniprot_entry_not_found"}


def extract_hpa_base(gene: str, report_text: str) -> str:
    m = re.search(r"https://www\.proteinatlas\.org/(ENSG\d+-[A-Za-z0-9_.-]+)(?:[/\s)]|$)", report_text)
    if m:
        return f"https://www.proteinatlas.org/{m.group(1)}"
    url = f"https://www.proteinatlas.org/search/{urllib.parse.quote(gene)}"
    page = request_text(url)
    escaped_gene = re.escape(gene)
    for pat in [rf"/(ENSG\d+-{escaped_gene})(?:[/?\"'#<])", r"/(ENSG\d+-[A-Za-z0-9_.-]+)(?:[/?\"'#<])"]:
        m = re.search(pat, page, re.I)
        if m:
            return f"https://www.proteinatlas.org/{m.group(1)}"
    return ""


def parse_hpa_interactions(page: str, center_gene: str, top_n: int) -> list[dict[str, str]]:
    page = html.unescape(page).replace("\\/", "/")
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    sep = r"(?:\s|<br\s*/?>|<[^>]+>)+"
    title_re = re.compile(
        rf'"title"\s*:\s*"({re.escape(center_gene)}\s*-\s*([A-Za-z0-9_.-]+)|([A-Za-z0-9_.-]+)\s*-\s*{re.escape(center_gene)})'
        rf'{sep}Interaction found in datasets:\s*([^"]+)"',
        re.I,
    )
    structure_re = re.compile(r'"haveStructure"\s*:\s*(true|false)', re.I)
    for m in title_re.finditer(page):
        partner = m.group(2) or m.group(3) or ""
        datasets = re.sub(r"<[^>]+>", " ", m.group(4))
        datasets = re.sub(r"\s+", " ", datasets).strip()
        if not partner or partner.upper() == center_gene.upper():
            continue
        key = (partner.upper(), datasets.lower())
        if key in seen:
            continue
        seen.add(key)
        window = page[m.end():m.end() + 350]
        sm = structure_re.search(window)
        rows.append({
            "partner": partner,
            "datasets": datasets,
            "has_structure": sm.group(1).lower() if sm else "",
        })
    rows.sort(key=lambda r: (0 if r["has_structure"] == "true" else 1, r["partner"]))
    return rows[:top_n]


def get_hpa_interaction(gene: str, report_text: str, top_n: int) -> dict[str, object]:
    try:
        base = extract_hpa_base(gene, report_text)
        if not base:
            return {"hpa_interaction_url": "", "interactions": [], "humanppi_error": "hpa_entry_not_found"}
        url = base.rstrip("/") + "/interaction"
        page = request_text(url)
        interactions = parse_hpa_interactions(page, gene, top_n)
        return {"hpa_interaction_url": url, "interactions": interactions, "humanppi_error": ""}
    except Exception as exc:
        return {"hpa_interaction_url": "", "interactions": [], "humanppi_error": f"{type(exc).__name__}: {exc}"}


def replace_block(text: str, block: str) -> str:
    rx = re.compile(re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END), re.S)
    if rx.search(text):
        return rx.sub(block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def esc(value: object) -> str:
    return str(value or "").replace("|", "\\|").strip()


def build_block(gene: str, domain: dict[str, str], ppi: dict[str, object]) -> str:
    lines = [
        BLOCK_START,
        f"## Domain/SMART 与 humanPPI 补充（{dt.date.today().isoformat()}）",
        "",
        "### SMART / UniProt domain",
        "| Source | Data |",
        "|---|---|",
        f"| UniProt | {esc(domain.get('uniprot'))} |",
        f"| SMART | {esc(domain.get('smart') or '未在 UniProt xref 中检出 SMART 条目')} |",
        f"| UniProt Domain [FT] | {esc(domain.get('domain_ft') or '未检出显式 UniProt Domain feature')} |",
        f"| InterPro | {esc(domain.get('interpro') or '未检出')} |",
        f"| Pfam | {esc(domain.get('pfam') or '未检出')} |",
        "",
        "### humanPPI / HPA Interaction",
        f"Source: {ppi.get('hpa_interaction_url') or '未找到 HPA interaction 页面'}",
        "",
    ]
    interactions = list(ppi.get("interactions") or [])
    if interactions:
        lines += ["| Partner | Datasets | AF3/HPA structure |", "|---|---|:--:|"]
        for row in interactions:
            lines.append(f"| {esc(row.get('partner'))} | {esc(row.get('datasets'))} | {esc(row.get('has_structure'))} |")
    else:
        lines.append("未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。")
    lines.append(BLOCK_END)
    return "\n".join(lines)


def load_records() -> list[dict]:
    data = json.loads(DOCS_INDEX.read_text(encoding="utf-8"))
    return data.get("records", [])


def process(rec: dict, apply: bool, top_n: int, write_empty_block: bool) -> dict[str, str]:
    gene = rec["gene"]
    path = ROOT / rec["report_path"]
    text = path.read_text(encoding="utf-8", errors="replace")
    domain = get_uniprot_domain(gene)
    ppi = get_hpa_interaction(gene, text, top_n)
    changed = False
    has_evidence = bool(domain.get("smart") or domain.get("domain_ft") or domain.get("interpro") or domain.get("pfam") or ppi.get("interactions"))
    if has_evidence or write_empty_block:
        block = build_block(gene, domain, ppi)
        new_text = replace_block(text, block)
        changed = new_text != text
        if apply and changed:
            path.write_text(new_text, encoding="utf-8")
    return {
        "gene": gene,
        "report_path": rec["report_path"],
        "uniprot": domain.get("uniprot", ""),
        "smart": domain.get("smart", ""),
        "domain_ft": domain.get("domain_ft", ""),
        "interpro": domain.get("interpro", ""),
        "pfam": domain.get("pfam", ""),
        "domain_error": domain.get("uniprot_error", ""),
        "hpa_interaction_url": str(ppi.get("hpa_interaction_url", "")),
        "humanppi_count": str(len(ppi.get("interactions") or [])),
        "humanppi_partners": ";".join(row["partner"] for row in (ppi.get("interactions") or [])),
        "humanppi_error": str(ppi.get("humanppi_error", "")),
        "changed": str(changed),
        "applied": str(bool(apply and changed)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich detail reports with UniProt SMART/domain and HPA humanPPI evidence blocks.")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--genes", default="", help="Comma-separated gene symbols.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--top-n", type=int, default=10)
    parser.add_argument("--status", default="", help="Optional status filter, e.g. scored or rejected.")
    parser.add_argument("--min-score", type=float, default=None, help="Optional minimum total score filter.")
    parser.add_argument("--only-missing-block", action="store_true", default=True)
    parser.add_argument("--refresh-existing", action="store_true", help="Replace existing enrichment blocks instead of skipping them.")
    parser.add_argument("--write-empty-block", action="store_true", help="Write a reviewed no-data block when no domain or HPA interaction evidence is found.")
    args = parser.parse_args()

    selected = {g.strip().casefold() for g in args.genes.split(",") if g.strip()}
    records = load_records()
    todo = []
    for rec in records:
        if selected and rec["gene"].casefold() not in selected:
            continue
        if args.status and str(rec.get("status", "")).casefold() != args.status.casefold():
            continue
        if args.min_score is not None:
            try:
                if float(rec.get("score") or -1) < args.min_score:
                    continue
            except (TypeError, ValueError):
                continue
        path = ROOT / rec["report_path"]
        if args.only_missing_block and not args.refresh_existing and BLOCK_START in path.read_text(encoding="utf-8", errors="replace"):
            continue
        todo.append(rec)
    if args.limit:
        todo = todo[: args.limit]

    rows: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(process, rec, args.apply, args.top_n, args.write_empty_block) for rec in todo]
        for i, fut in enumerate(as_completed(futures), start=1):
            rows.append(fut.result())
            if i == 1 or i % 10 == 0 or i == len(futures):
                print(f"progress={i}/{len(futures)}", flush=True)
            if i % 50 == 0:
                time.sleep(0.2)

    mode = "apply" if args.apply else "audit"
    out = ENGINEERING / f"domain_humanppi_enrichment_{mode}_{TS}.tsv"
    fields = [
        "gene", "report_path", "uniprot", "smart", "domain_ft", "interpro", "pfam",
        "domain_error", "hpa_interaction_url", "humanppi_count", "humanppi_partners",
        "humanppi_error", "changed", "applied",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["report_path"]))
    summary = out.with_suffix(".summary.md")
    summary.write_text(
        "\n".join([
            "# Domain/SMART + humanPPI Enrichment",
            "",
            f"- Mode: {mode}",
            f"- Candidates: {len(todo)}",
            f"- Reports changed: {sum(r['changed'] == 'True' for r in rows)}",
            f"- SMART found: {sum(bool(r['smart']) for r in rows)}",
            f"- humanPPI partners found: {sum(int(r['humanppi_count'] or '0') > 0 for r in rows)}",
            f"- TSV: {out.relative_to(ROOT)}",
        ]),
        encoding="utf-8",
    )
    print(f"mode={mode} candidates={len(todo)} changed={sum(r['changed']=='True' for r in rows)} smart_found={sum(bool(r['smart']) for r in rows)} humanppi_found={sum(int(r['humanppi_count'] or '0')>0 for r in rows)} tsv={out}")


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()
