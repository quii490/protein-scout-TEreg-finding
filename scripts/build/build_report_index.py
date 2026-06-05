#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DETAIL = ROOT / "detail"
SUMMARY = ROOT / "data" / "summary"
DOCS_DATA = ROOT / "docs" / "data"
FULL_NAME_TABLE = SUMMARY / "protein_full_names.tsv"
SUMMARY.mkdir(parents=True, exist_ok=True)
DOCS_DATA.mkdir(parents=True, exist_ok=True)

FIELDNAMES = [
    "gene", "protein_full_name", "status", "category", "score", "nuclear_score",
    "size_score", "novelty_score", "structure_score", "domain_score", "ppi_score", "corroboration_score",
    "recommendation", "pubmed_count", "localization", "rejection_reason",
    "source_table_status", "source_table_category", "report_path", "docs_report_path", "category_page", "lines",
    "has_hpa", "has_if_image", "has_pae", "has_pdb", "has_ppi", "has_pubmed", "has_scoring_table", "has_manual_review",
    "duplicate_count", "duplicate_type", "is_primary_candidate", "known_backlog_flags", "parse_quality", "parse_notes",
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_protein_full_names() -> dict[str, str]:
    if not FULL_NAME_TABLE.exists():
        return {}
    out: dict[str, str] = {}
    with FULL_NAME_TABLE.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            gene = (row.get("gene") or "").strip()
            name = (row.get("protein_full_name") or "").strip()
            if gene and name:
                out[gene.casefold()] = name
    return out


def parse_simple_yaml(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, val = line.split(":", 1)
        out[key.strip().lower().replace("-", "_")] = val.strip().strip('"\'')
    return out


def split_md_table_row(line: str) -> list[str]:
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        return []
    return [cell.strip() for cell in line.strip("|").split("|")]


def numeric_from_text(value: str) -> str | None:
    nums = re.findall(r"(?<![A-Za-z0-9])(?:100(?:\.0+)?|[0-9]{1,2}(?:\.[0-9]+)?)(?![A-Za-z0-9])", value or "")
    vals = [float(n) for n in nums if 0 <= float(n) <= 100]
    if not vals:
        return None
    return ("%.2f" % vals[-1]).rstrip("0").rstrip(".")


def clean_metric(value: str | None) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if value in {"?", "？", "-", "NA", "N/A", "na", "n/a"}:
        return ""
    return value


def score_value(value: str | None) -> float | None:
    value = (value or "").replace("**", "").strip()
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*/\s*([0-9]+(?:\.[0-9]+)?)", value)
    if m:
        val = float(m.group(1))
        return val if 0 <= val <= 100 else None
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)", value)
    if not m:
        return None
    val = float(m.group(1))
    return val if 0 <= val <= 1000 else None


def format_score(value: float | None) -> str:
    if value is None:
        return ""
    return ("%.2f" % value).rstrip("0").rstrip(".")


def normalize_dimension(score: float | None, max_score: float | None) -> str:
    if score is None:
        return ""
    if max_score and max_score > 10:
        score = score / max_score * 10
    if score > 10:
        return ""
    return format_score(score)


def parse_dimension_scores(text: str) -> dict[str, str]:
    aliases = {
        "nuclear_score": ["nuclear localization", "核定位", "nuclear"],
        "size_score": ["protein size", "蛋白大小", "size"],
        "novelty_score": ["research novelty", "研究新颖", "novelty"],
        "structure_score": ["3d structure", "三维结构", "structure", "alphafold"],
        "domain_score": ["regulatory domains", "调控结构域", "domain"],
        "ppi_score": ["ppi network", "ppi", "互作"],
        "corroboration_score": ["corroboration", "互证"],
    }
    out: dict[str, str] = {}
    for line in text.splitlines():
        cells = split_md_table_row(line)
        if len(cells) < 2:
            continue
        label = re.sub(r"[*_`#]", "", cells[0]).strip().lower()
        if not label or re.fullmatch(r":?-+:?", label.replace(" ", "")):
            continue
        if "total" in label or "总分" in label or "综合" in label:
            vals = [score_value(c) for c in cells[1:4]]
            vals = [v for v in vals if v is not None]
            if vals:
                out["score"] = format_score(vals[-1])
            continue
        target = None
        for key, words in aliases.items():
            if any(word in label for word in words):
                target = key
                break
        if target is None:
            continue
        max_score = None
        raw_score = None
        if len(cells) >= 3:
            first = score_value(cells[1])
            second = score_value(cells[2])
            if first is not None and second is not None:
                max_score, raw_score = first, second
            else:
                raw_score = first or second
        else:
            raw_score = score_value(cells[1])
        normalized = normalize_dimension(raw_score, max_score)
        if normalized:
            out[target] = normalized
    return out


def sane_dimension(value: str | None) -> str:
    value = clean_metric(value)
    val = score_value(value)
    if val is not None and val > 10:
        return ""
    return value


def parse_score(text: str) -> str | None:
    patterns = [
        r"(?:归一化总分|Normalized\s+(?:Total\s+)?Score|Final\s+score|综合评分|总分)[^0-9\n|]{0,80}([0-9]+(?:\.[0-9]+)?)",
        r"\|[^\n]*(?:归一化总分|Final score|总分)[^\n]*\|",
    ]
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            score = numeric_from_text(m.group(0)) or numeric_from_text(m.group(1) if m.lastindex else "")
            if score is not None:
                return score
    return None


def parse_nuclear_score(text: str) -> str | None:
    patterns = [
        r"(?:核定位(?:分数)?|Nuclear(?:\s+localization)?(?:\s+score)?)[^0-9\n|]{0,80}([0-9]+(?:\.[0-9]+)?)",
        r"\|[^\n]*(?:核定位|Nuclear)[^\n]*\|",
    ]
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            score = numeric_from_text(m.group(0)) or numeric_from_text(m.group(1) if m.lastindex else "")
            if score is not None:
                return score
    return None


def parse_pubmed_count(text: str) -> str | None:
    count_value = r"([<>]?\s*[0-9,]+(?:\s*-\s*[0-9,]+)?)"
    patterns = [
        rf"PubMed\s*=\s*{count_value}",
        rf"PubMed\s*~\s*{count_value}",
        rf"PubMed\s+{count_value}\s+articles",
        r"PubMed strict(?:\s*\(Title/Abstract\))?\s*[:=|]\s*([0-9]+)",
        r"PubMed strict\s*:\s*([0-9]+)",
        r"PubMed Count:\s*([0-9]+)",
        r"\|\s*\*{0,2}PubMed\s*\(strict\)\*{0,2}\s*\|\s*~?\s*([0-9,]+)\s*\|",
        r"\|\s*\*{0,2}PubMed strict\*{0,2}\s*\|\s*~?\s*([0-9,]+)\s*\|",
        r"\|\s*\*{0,2}PubMed count\s*\(Title/Abstract\)\*{0,2}\s*\|\s*~?\s*([0-9,]+)\s*\|",
        r"\|\s*PubMed\s+总数(?:\s*\([^)]*\))?\s*\|\s*([0-9,]+)\s*(?:篇)?\s*\|",
        r"\|\s*PubMed\s+严格搜索(?:\s*\([^)]*\))?\s*\|\s*([0-9,]+)\s*(?:篇)?\s*\|",
        rf"\|\s*PubMed\s+strict query(?:\s*\([^)]*\))?\s*\|\s*{count_value}\s*(?:articles)?\s*\|",
        rf"\|\s*PubMed\s+estimated count\s*\|\s*~?\s*{count_value}\s*(?:articles)?\s*\|",
        rf"\|\s*PubMed\s*\([^)]*\)\s*\|\s*{count_value}\s*(?:articles)?\s*\|",
        r"\|\s*PubMed\s+\"[^\"]+\"\[Title/Abstract\]\s*\|\s*([0-9,]+)\s*(?:篇)?\s*\|",
        r"\|\s*Strict\s*\(Title/Abstract\)\s*\|\s*([0-9]+)\s*\|",
        r"\|\s*PubMed(?:\s+strict)?\s*\|\s*([0-9]+)\s*\|",
        r"PubMed\s+([0-9]+)\s*篇",
        r"([0-9,]+)\s*篇\s*PubMed",
        r"PubMed\s+>\s*100[^0-9]{0,40}([0-9]+)",
        r"研究新颖性[^\n]*PubMed strict\s*[:=]\s*([0-9]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            return re.sub(r"\s+", "", m.group(1).replace(",", ""))
    return None


def parse_protein_full_name(text: str) -> str | None:
    patterns = [
        r"\|\s*\*{0,2}蛋白全(?:名|称)\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"\*\*Protein Name:\*\*\s*([^\n]+)",
        r"\*\*Protein full name:\*\*\s*([^\n]+)",
        r"\|\s*\*{0,2}Protein Name\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"\|\s*\*{0,2}Protein full name\*{0,2}\s*\|\s*([^|]+?)\s*\|",
        r"Protein Name:\s*([^\n]+)",
        r"^#\s+[A-Za-z0-9._-]+\s+\(([^)]+)\)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if not m:
            continue
        value = re.sub(r"\s+", " ", m.group(1)).strip().strip("*")
        if value and len(value) <= 180:
            return value
    return None


def parse_localization(text: str, fallback: str) -> str:
    patterns = [
        r"\|\s*Protein Atlas \(IF\)\s*\|\s*([^|]+?)\s*\|",
        r"\|\s*HPA(?:\s+IF)?\s*\|\s*([^|]+?)\s*\|",
        r"Main location\s*[:|]\s*([^|\n]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            value = re.sub(r"\s+", " ", m.group(1)).strip()
            value = re.sub(r"\*\*|`", "", value)
            if value and len(value) <= 90 and "####" not in value and "评分" not in value:
                return value
    return fallback


def has_markdown_image(text: str) -> bool:
    return bool(re.search(r"!\[[^\]]*\]\([^)]*\)|!\[\[[^\]]+\]\]|<img\b", text, re.I))


def evidence_flags(text: str) -> dict[str, bool]:
    low = text.lower()
    return {
        "has_hpa": any(k in low for k in ["human protein atlas", "protein atlas", "proteinatlas", "hpa", "cell atlas"]),
        "has_if_image": any(k in low for k in ["red_green", "immunofluorescence", "if image", "if图", "if 图", "confocal", "cell atlas"]) or bool(re.search(r"!\[[^\]]*\]\([^)]*(?:red_green|proteinatlas|cellatlas|if)[^)]*\)", text, re.I)),
        "has_pae": "pae" in low or "predicted aligned error" in low,
        "has_pdb": bool(re.search(r"\bPDB\b|RCSB|structure|crystal|alphafold", text, re.I)),
        "has_ppi": any(k in low for k in ["ppi", "string", "biogrid", "intact", "interact", "互作", "protein-protein"]),
        "has_pubmed": any(k in low for k in ["pubmed", "pmid", "literature", "文献"]),
        "has_scoring_table": any(k in low for k in ["scoring", "score", "评分", "总分"]) and "|" in text,
        "has_manual_review": any(k in low for k in ["manual review", "manual-review", "人工复核", "待复核", "review flag"]),
    }


def parse_report_path_from_row(joined: str) -> tuple[str | None, str | None, str | None]:
    m_path = re.search(r"detail/([^/\]|)]+)/([^/\]|)]+)/([^/\]|)]+?-evaluation)(?:\.md)?", joined)
    if not m_path:
        return None, None, None
    category, gene, stem = m_path.group(1), m_path.group(2), m_path.group(3)
    return gene, category, f"detail/{category}/{gene}/{stem}.md"


def parse_source_table() -> dict[tuple[str, str], dict[str, str]]:
    path = ROOT / "protein-finding.md"
    if not path.exists():
        return {}
    text = read_text(path)
    seed: dict[tuple[str, str], dict[str, str]] = {}
    current_header: list[str] = []
    current_section = ""
    for raw in text.splitlines():
        line = raw.strip()
        heading = re.match(r"^#{1,4}\s+(.+?)\s*$", line)
        if heading:
            current_section = heading.group(1)
        if not line.startswith("|"):
            continue
        cells = split_md_table_row(line)
        if not cells or all(re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in cells):
            continue
        if any(c in cells for c in ["基因", "Gene", "Symbol"]) or ("总分" in cells and "详情" in cells):
            current_header = cells
            continue
        if not current_header or ("-evaluation" not in line and "detail/" not in line):
            continue
        joined = " | ".join(cells)
        gene = None
        report_path = None
        gene, path_category, report_path = parse_report_path_from_row(joined)
        if not gene:
            m_gene = re.search(r"\b([A-Za-z0-9][A-Za-z0-9._-]{1,30})-evaluation(?:\.md)?\b", joined)
            if m_gene:
                gene = m_gene.group(1)
        if not gene and len(cells) > 1:
            gene = re.sub(r"\W+", "", cells[1]).strip()
        if not gene:
            continue
        row = {h: cells[i] if i < len(cells) else "" for i, h in enumerate(current_header)}
        is_rejected = "淘汰" in current_section or (path_category == "rejected")
        total = row.get("总分") or row.get("Score") or ""
        nuclear = row.get("核") or row.get("核定位") or row.get("Nuclear") or ""
        cat = "rejected" if is_rejected else (path_category or current_section)
        entry = {
            "source_table_status": "rejected" if is_rejected else "scored",
            "source_table_category": cat or current_section,
            "source_table_score": numeric_from_text(total) or "",
            "source_table_nuclear_score": numeric_from_text(nuclear) or "",
            "size_score": clean_metric(row.get("大", "")),
            "novelty_score": clean_metric(row.get("新", "")),
            "structure_score": clean_metric(row.get("结", "")),
            "domain_score": clean_metric(row.get("域", "")),
            "ppi_score": clean_metric(row.get("PPI", "")),
            "corroboration_score": clean_metric(row.get("互证", "")),
            "recommendation": row.get("推荐", ""),
            "pubmed_count": row.get("PubMed", ""),
            "rejection_reason": row.get("原因", ""),
        }
        key = (gene, report_path or "")
        seed[key] = entry
        seed[(gene.casefold(), report_path or "")] = entry
        if report_path:
            seed[("", report_path)] = entry
    return seed


def table_seed_for(seed: dict[tuple[str, str], dict[str, str]], gene: str, report_path: str) -> dict[str, str]:
    return (
        seed.get((gene, report_path))
        or seed.get((gene.casefold(), report_path))
        or seed.get(("", report_path))
        or seed.get((gene, ""))
        or seed.get((gene.casefold(), ""))
        or {}
    )


def docs_name(gene: str, category: str, index: int, total: int) -> str:
    safe_gene = re.sub(r"[^A-Za-z0-9._-]+", "_", gene)
    safe_cat = re.sub(r"[^A-Za-z0-9._-]+", "_", category)
    if total == 1:
        return f"reports/{safe_gene}.html"
    if index == 1:
        return f"reports/{safe_gene}__{safe_cat}.html"
    return f"reports/{safe_gene}__{safe_cat}__{index}.html"


def build_records() -> list[dict[str, Any]]:
    seed = parse_source_table()
    full_names = load_protein_full_names()
    records: list[dict[str, Any]] = []
    for path in sorted(DETAIL.glob("*/*/*-evaluation.md")):
        text = read_text(path)
        yaml = parse_simple_yaml(text)
        lines = text.count("\n") + (1 if text else 0)
        category = path.parent.parent.name
        gene = yaml.get("gene") or yaml.get("symbol") or path.name.removesuffix("-evaluation.md")
        path_status = "rejected" if category == "rejected" else "scored"
        report_path = rel(path)
        source = table_seed_for(seed, gene, report_path)
        if not source.get("source_table_status"):
            continue
        status = (source.get("source_table_status") or path_status).lower().strip()
        if status not in {"scored", "rejected", "eliminated"}:
            status = path_status
        if status == "eliminated":
            status = "rejected"
        parsed_score = parse_score(text)
        parsed_nuclear = parse_nuclear_score(text)
        parsed_dimensions = parse_dimension_scores(text)
        source_has_summary = bool(source.get("source_table_status"))
        if source_has_summary:
            score = source.get("source_table_score") or parsed_score
            nuclear_score = source.get("source_table_nuclear_score") or parsed_nuclear
            size_score = source.get("size_score", "")
            novelty_score = source.get("novelty_score", "")
            structure_score = source.get("structure_score", "")
            domain_score = source.get("domain_score", "")
            ppi_score = source.get("ppi_score", "")
            corroboration_score = source.get("corroboration_score", "")
        else:
            score = parsed_dimensions.get("score") or parsed_score
            nuclear_score = parsed_dimensions.get("nuclear_score") or sane_dimension(parsed_nuclear)
            size_score = parsed_dimensions.get("size_score", "")
            novelty_score = parsed_dimensions.get("novelty_score", "")
            structure_score = parsed_dimensions.get("structure_score", "")
            domain_score = parsed_dimensions.get("domain_score", "")
            ppi_score = parsed_dimensions.get("ppi_score", "")
            corroboration_score = parsed_dimensions.get("corroboration_score", "")
        if status == "rejected":
            score = None
        pubmed_count = source.get("pubmed_count") or parse_pubmed_count(text)
        protein_full_name = full_names.get(gene.casefold()) or parse_protein_full_name(text) or ""
        localization = parse_localization(text, category)
        flags = evidence_flags(text)
        notes: list[str] = []
        if lines < 25:
            notes.append("thin_report_lt25_lines")
        if status == "scored" and score is None:
            notes.append("score_not_parsed")
        if not flags["has_hpa"]:
            notes.append("missing_hpa_marker")
        if not flags["has_pubmed"]:
            notes.append("missing_pubmed_marker")
        if lines >= 25 and gene and category and (status == "rejected" or score is not None):
            parse_quality = "GOOD"
        elif gene and category and lines >= 10:
            parse_quality = "PARTIAL"
        else:
            parse_quality = "WEAK"
        backlog = []
        if parse_quality != "GOOD":
            backlog.append(f"parse_quality:{parse_quality}")
        if flags["has_manual_review"]:
            backlog.append("manual_review")
        records.append({
            "gene": gene, "protein_full_name": protein_full_name, "status": status, "category": category, "score": score, "nuclear_score": nuclear_score,
            "size_score": size_score,
            "novelty_score": novelty_score,
            "structure_score": structure_score,
            "domain_score": domain_score,
            "ppi_score": ppi_score,
            "corroboration_score": corroboration_score,
            "recommendation": source.get("recommendation", ""),
            "pubmed_count": pubmed_count,
            "localization": localization,
            "rejection_reason": source.get("rejection_reason", ""),
            "source_table_status": source.get("source_table_status", ""),
            "source_table_category": source.get("source_table_category", ""),
            "report_path": report_path, "docs_report_path": "", "category_page": f"category/{category}.html", "lines": lines,
            **flags,
            "duplicate_count": 1, "duplicate_type": "NONE", "is_primary_candidate": True,
            "known_backlog_flags": ";".join(backlog), "parse_quality": parse_quality,
            "parse_notes": ";".join(notes) if notes else "ok",
        })
    by_gene: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rec in records:
        by_gene[rec["gene"]].append(rec)
    for gene, group in by_gene.items():
        statuses = Counter(r["status"] for r in group)
        if len(group) == 1:
            dtype = "NONE"
        elif statuses.get("scored", 0) and statuses.get("rejected", 0):
            dtype = "SCORED_REJECTED_CONFLICT"
        elif statuses.get("scored", 0) > 1:
            dtype = "MULTI_SCORED_CONFLICT"
        else:
            dtype = "MULTI_REPORT"
        cat_seen: Counter[str] = Counter()
        for rec in sorted(group, key=lambda r: (r["category"], r["report_path"])):
            cat_seen[rec["category"]] += 1
            rec["duplicate_count"] = len(group)
            rec["duplicate_type"] = dtype
            rec["is_primary_candidate"] = dtype == "NONE" or (dtype == "MULTI_REPORT" and rec["status"] == "scored")
            rec["docs_report_path"] = docs_name(gene, rec["category"], cat_seen[rec["category"]], len(group))
            if dtype != "NONE":
                flags = [x for x in str(rec["known_backlog_flags"]).split(";") if x]
                flags.append(f"duplicate:{dtype}")
                rec["known_backlog_flags"] = ";".join(dict.fromkeys(flags))
    used_casefold: set[str] = set()
    for rec in sorted(records, key=lambda r: (r["docs_report_path"].casefold(), r["gene"], r["report_path"])):
        key = rec["docs_report_path"].casefold()
        if key in used_casefold:
            path = Path(rec["docs_report_path"])
            suffix = slug = re.sub(r"[^A-Za-z0-9._-]+", "_", rec["gene"])
            candidate = f"{path.with_suffix('').as_posix()}__{suffix}{path.suffix}"
            n = 2
            while candidate.casefold() in used_casefold:
                candidate = f"{path.with_suffix('').as_posix()}__{suffix}__{n}{path.suffix}"
                n += 1
            rec["docs_report_path"] = candidate
            key = candidate.casefold()
        used_casefold.add(key)
    return sorted(records, key=lambda r: (-(float(r.get("score") or -1)), r["category"], r["gene"], r["report_path"]))


def write_outputs(records: list[dict[str, Any]]) -> None:
    for path, delimiter in [(SUMMARY / "protein_report_index.tsv", "\t"), (SUMMARY / "protein_report_index.csv", ",")]:
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=delimiter)
            writer.writeheader()
            for rec in records:
                writer.writerow({k: rec.get(k, "") for k in FIELDNAMES})
    meta = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "primary_source_table": "protein-finding.md",
        "detail_root": "detail/",
        "total_records": len(records),
        "status_counts": dict(Counter(r["status"] for r in records)),
        "category_counts": dict(Counter(r["category"] for r in records)),
        "duplicate_records": sum(1 for r in records if r["duplicate_count"] > 1),
        "fields": FIELDNAMES,
    }
    with (DOCS_DATA / "protein_report_index.json").open("w", encoding="utf-8") as f:
        json.dump({"metadata": meta, "records": records}, f, ensure_ascii=False, indent=2)
    with (ROOT / "docs" / "protein_index.md").open("w", encoding="utf-8") as f:
        f.write("# Protein Report Index\n\n")
        f.write(f"Generated records: {len(records)}\n\n")
        f.write("| Gene | Protein full name | Status | Category | 核 | 大 | 新 | 结 | 域 | PPI | 互证 | 总分 | PubMed | Detail |\n")
        f.write("|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n")
        for rec in records:
            markdown_detail = "../" + rec["report_path"]
            f.write(f"| {rec['gene']} | {rec.get('protein_full_name') or ''} | {rec['status']} | {rec['category']} | {rec.get('nuclear_score') or ''} | {rec.get('size_score') or ''} | {rec.get('novelty_score') or ''} | {rec.get('structure_score') or ''} | {rec.get('domain_score') or ''} | {rec.get('ppi_score') or ''} | {rec.get('corroboration_score') or ''} | {rec.get('score') or ''} | {rec.get('pubmed_count') or ''} | [{rec['report_path']}]({markdown_detail}) |\n")


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    records = build_records()
    write_outputs(records)
    print(f"records={len(records)}")
