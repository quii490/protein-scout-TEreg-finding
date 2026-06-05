#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETAIL = ROOT / "detail"
ENGINEERING = ROOT / "audit_work" / "engineering"
ENGINEERING.mkdir(parents=True, exist_ok=True)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_external(src: str) -> bool:
    return bool(re.match(r"^(?:https?:|mailto:|tel:|data:|javascript:)", src, re.I))


def clean_src(src: str) -> str:
    src = src.strip().strip('<>"\'')
    return src.split("#", 1)[0].split("?", 1)[0]


def resolve_local_image(src: str, report_path: Path) -> tuple[Path | None, str]:
    cleaned = clean_src(src)
    if not cleaned:
        return None, "empty_src"
    if is_external(cleaned):
        return None, "external_url"
    p = Path(cleaned)
    candidates: list[Path] = []
    if p.is_absolute():
        candidates.append(p)
    else:
        candidates.extend([
            report_path.parent / cleaned,
            ROOT / cleaned,
            ROOT / "detail" / cleaned,
            report_path.parent / "IF_images" / cleaned,
        ])
    gene = report_path.parent.name
    if "detail/" in cleaned:
        sub = cleaned[cleaned.index("detail/"):]
        candidates.append(ROOT / sub)
        parts = Path(sub).parts
        if len(parts) >= 3:
            candidates.append(report_path.parent / parts[-1])
            if parts[0] == "detail" and len(parts) == 3:
                candidates.extend((ROOT / "detail").glob(f"*/{parts[1]}/{parts[2]}"))
            if "IF_images" in parts:
                idx = parts.index("IF_images")
                candidates.append(report_path.parent.joinpath(*parts[idx:]))
    if Path(cleaned).name == cleaned:
        candidates.extend((ROOT / "detail").glob(f"*/{gene}/{cleaned}"))
        candidates.extend((ROOT / "detail").glob(f"*/{gene}/IF_images/{cleaned}"))
    seen: set[str] = set()
    for cand in candidates:
        key = str(cand)
        if key in seen:
            continue
        seen.add(key)
        try:
            if cand.exists() and cand.is_file():
                return cand.resolve(), "resolved"
        except OSError:
            continue
    return None, "source_not_found"


def image_refs(text: str) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    for m in re.finditer(r"!\[\[([^\]]+)\]\]", text):
        refs.append(("obsidian", m.group(1).split("|", 1)[0].strip()))
    for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        refs.append(("markdown", m.group(1).strip()))
    for m in re.finditer(r"<img\b[^>]*src=[\"']([^\"']+)[\"'][^>]*>", text, re.I):
        refs.append(("html", m.group(1).strip()))
    return refs


def main() -> None:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = ENGINEERING / f"image_reference_audit_{ts}.tsv"
    summary = ENGINEERING / f"image_reference_audit_{ts}.summary.md"
    fields = [
        "gene", "category", "report_path", "syntax", "source_image", "is_external",
        "resolved_path", "exists", "reason", "suggested_markdown_path",
    ]
    rows: list[dict[str, str]] = []
    reports = list(sorted(DETAIL.glob("*/*/*-evaluation.md")))
    reports_with_refs = 0
    for report in reports:
        text = report.read_text(encoding="utf-8", errors="replace")
        refs = image_refs(text)
        if refs:
            reports_with_refs += 1
        gene = report.parent.name
        category = report.parent.parent.name
        for syntax, src in refs:
            resolved, reason = resolve_local_image(src, report)
            external = is_external(clean_src(src))
            suggested = ""
            if resolved:
                suggested = rel(resolved)
                if not str(resolved).startswith(str(ROOT)):
                    reason = "resolved_outside_project"
            rows.append({
                "gene": gene,
                "category": category,
                "report_path": rel(report),
                "syntax": syntax,
                "source_image": src,
                "is_external": str(external),
                "resolved_path": str(resolved) if resolved else "",
                "exists": str(bool(resolved) or external),
                "reason": reason,
                "suggested_markdown_path": suggested,
            })
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    missing = [r for r in rows if r["exists"] == "False"]
    external = [r for r in rows if r["is_external"] == "True"]
    summary.write_text(
        "\n".join([
            "# Image Reference Audit",
            "",
            f"- Reports scanned: {len(reports)}",
            f"- Reports with image refs: {reports_with_refs}",
            f"- Image refs: {len(rows)}",
            f"- Resolved/local or external refs: {len(rows) - len(missing)}",
            f"- Missing local refs: {len(missing)}",
            f"- External refs: {len(external)}",
            f"- TSV: {out.relative_to(ROOT)}",
            "",
            "## First Missing Refs",
            "",
            "\n".join(f"- {r['gene']}: {r['source_image']}" for r in missing[:100]),
        ]),
        encoding="utf-8",
    )
    print(f"refs={len(rows)} missing={len(missing)} reports={len(reports)} audit={out}")


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()
