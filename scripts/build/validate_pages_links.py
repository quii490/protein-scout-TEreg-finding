#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUT = ROOT / "audit_work" / "engineering"
OUT.mkdir(parents=True, exist_ok=True)
TS = dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def is_external(url: str) -> bool:
    return bool(re.match(r"^(?:https?:|mailto:|tel:|data:|javascript:)", url, re.I))


def classify(url: str) -> tuple[bool, bool]:
    is_img = bool(re.search(r"\.(?:png|jpe?g|gif|webp|svg|tiff?|bmp)(?:[#?].*)?$", url, re.I))
    is_page = bool(re.search(r"\.html(?:[#?].*)?$", url, re.I))
    return is_img, is_page


def resolve(source: Path, url: str) -> Path | None:
    clean = url.strip()
    if not clean or clean.startswith('#') or is_external(clean):
        return None
    clean = clean.split('#', 1)[0].split('?', 1)[0]
    if not clean:
        return source
    return (source.parent / clean).resolve()


def main() -> None:
    required = [DOCS / "index.html", DOCS / "protein_index.html", DOCS / "data" / "protein_report_index.json"]
    rows = []
    for req in required:
        rows.append({
            "source_html": "REQUIRED", "link_or_src": str(req.relative_to(ROOT)), "resolved_path": str(req),
            "exists": str(req.exists()), "is_image": "False", "is_external": "False", "is_internal_page": str(req.suffix == '.html'),
            "broken": str(not req.exists()), "reason": "required_file"
        })
    html_files = sorted(DOCS.rglob("*.html"))
    for html_path in html_files:
        text = html_path.read_text(encoding="utf-8", errors="replace")
        refs = []
        refs.extend((m.group(1), False) for m in re.finditer(r"href=[\"']([^\"']+)[\"']", text, re.I))
        refs.extend((m.group(1), True) for m in re.finditer(r"src=[\"']([^\"']+)[\"']", text, re.I))
        for url, attr_is_image in refs:
            external = is_external(url)
            resolved = resolve(html_path, url)
            image_by_ext, is_page = classify(url)
            is_image = attr_is_image or image_by_ext
            exists = True if external or url.startswith('#') else bool(resolved and resolved.exists())
            broken = (not external) and (not url.startswith('#')) and (not exists)
            rows.append({
                "source_html": str(html_path.relative_to(ROOT)), "link_or_src": url,
                "resolved_path": "" if resolved is None else str(resolved), "exists": str(exists),
                "is_image": str(is_image), "is_external": str(external), "is_internal_page": str(is_page),
                "broken": str(broken), "reason": "external_not_checked" if external else ("anchor" if url.startswith('#') else "ok" if exists else "missing")
            })
    tsv = OUT / f"step4b_pages_link_validation_{TS}.tsv"
    fields = ["source_html", "link_or_src", "resolved_path", "exists", "is_image", "is_external", "is_internal_page", "broken", "reason"]
    with tsv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader(); writer.writerows(rows)
    broken_internal = sum(1 for r in rows if r["broken"] == "True" and r["is_image"] == "False")
    broken_images = sum(1 for r in rows if r["broken"] == "True" and r["is_image"] == "True")
    report_count = len(list((DOCS / "reports").glob("*.html")))
    category_count = len(list((DOCS / "category").glob("*.html")))
    summary = OUT / f"step4b_pages_link_validation_{TS}.summary.md"
    with summary.open("w", encoding="utf-8") as f:
        f.write("# Step 4B Pages Link Validation\n\n")
        f.write(f"- Timestamp: {TS}\n")
        f.write(f"- HTML files checked: {len(html_files)}\n")
        f.write(f"- docs/reports HTML count: {report_count}\n")
        f.write(f"- docs/category HTML count: {category_count}\n")
        f.write(f"- Broken internal links count: {broken_internal}\n")
        f.write(f"- Broken image links count: {broken_images}\n")
        f.write(f"- Validation TSV: `{tsv}`\n")
    print(f"broken_internal={broken_internal} broken_images={broken_images} reports={report_count} categories={category_count}")
    if broken_internal or broken_images:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
