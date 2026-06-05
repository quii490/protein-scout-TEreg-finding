#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
DETAIL = ROOT / "detail"
ENGINEERING = ROOT / "audit_work" / "engineering"
ENGINEERING.mkdir(parents=True, exist_ok=True)


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def detail_path_from_row(line: str) -> str:
    m = re.search(r"detail/([^/\]|)]+)/([^/\]|)]+)/([^/\]|)]+?-evaluation)(?:\.md)?", line)
    if not m:
        return ""
    return f"detail/{m.group(1)}/{m.group(2)}/{m.group(3)}.md"


def main() -> None:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = ENGINEERING / f"summary_scoring_incompatibility_audit_{ts}.tsv"
    summary = ENGINEERING / f"summary_scoring_incompatibility_audit_{ts}.summary.md"
    fields = ["gene", "category", "report_path", "issue", "field", "value", "reason"]
    rows: list[dict[str, str]] = []
    text = SUMMARY.read_text(encoding="utf-8", errors="replace")
    current_cat = ""
    summary_paths: set[str] = set()

    for raw in text.splitlines():
        line = raw.strip()
        h = re.match(r"^##\s+(.+)$", line)
        if h:
            current_cat = h.group(1).strip()
            continue
        if not line.startswith("|") or line.startswith("|---") or "基因" in line:
            continue
        cells = split_row(line)
        if len(cells) < 5:
            continue
        report_path = detail_path_from_row(line)
        if report_path:
            summary_paths.add(report_path)
        if current_cat == "已淘汰":
            continue
        gene = cells[1] if len(cells) > 1 else ""
        names = ["核", "大", "新", "结", "域", "PPI", "互证", "总分"]
        values = cells[2:10]
        for field, value in zip(names, values):
            if value in {"?", "？"}:
                rows.append({"gene": gene, "category": current_cat, "report_path": report_path, "issue": "QUESTION_MARK_SCORE", "field": field, "value": value, "reason": "summary score is unparseable"})
                continue
            numeric = value.lstrip("+")
            try:
                val = float(numeric)
            except ValueError:
                continue
            if field in {"核", "大", "新", "结", "域", "PPI"} and val > 10:
                rows.append({"gene": gene, "category": current_cat, "report_path": report_path, "issue": "DIMENSION_GT10", "field": field, "value": value, "reason": "dimension score should be 0-10"})
            if field == "互证" and val > 3:
                rows.append({"gene": gene, "category": current_cat, "report_path": report_path, "issue": "CROSS_GT3", "field": field, "value": value, "reason": "cross-validation bonus should be <=3"})
            if field == "总分" and val > 100:
                rows.append({"gene": gene, "category": current_cat, "report_path": report_path, "issue": "TOTAL_GT100", "field": field, "value": value, "reason": "normalized total should be <=100"})

    detail_paths = {str(path.relative_to(ROOT)) for path in DETAIL.glob("*/*/*-evaluation.md") if "detail/rejected/" not in str(path.relative_to(ROOT))}
    missing_from_summary = sorted(detail_paths - summary_paths)
    for report_path in missing_from_summary:
        parts = Path(report_path).parts
        rows.append({"gene": parts[2] if len(parts) > 2 else "", "category": parts[1] if len(parts) > 1 else "", "report_path": report_path, "issue": "SCORED_DETAIL_NOT_IN_SUMMARY", "field": "", "value": "", "reason": "rebuild_summary did not include this scored report"})

    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["issue"]] = counts.get(row["issue"], 0) + 1
    summary.write_text(
        "\n".join([
            "# Summary Scoring Incompatibility Audit",
            "",
            f"- TSV: {out.relative_to(ROOT)}",
            f"- Issues: {len(rows)}",
            "",
            "## Counts",
            "",
            "\n".join(f"- {k}: {v}" for k, v in sorted(counts.items())),
        ]),
        encoding="utf-8",
    )
    print(f"issues={len(rows)} audit={out}")


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()
