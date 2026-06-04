#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import html
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
REPORT_IMAGE_ROOT = ASSETS / "report-images"
ENGINEERING = ROOT / "audit_work" / "engineering"
TS = dt.datetime.now().strftime("%Y%m%d_%H%M%S")

for p in [DOCS, ASSETS / "css", ASSETS / "js", DOCS / "data", DOCS / "reports", DOCS / "category", REPORT_IMAGE_ROOT, ENGINEERING]:
    p.mkdir(parents=True, exist_ok=True)

CATEGORY_DESCRIPTIONS = {
    "nucleoplasm": "Candidates primarily associated with the nucleoplasm or diffuse nuclear compartment.",
    "nucleus-cytoplasm": "Candidates with evidence spanning nuclear and cytoplasmic localization.",
    "nuclear-speckle": "Candidates enriched in nuclear speckles or RNA-processing-associated nuclear bodies.",
    "nuclear-body": "Candidates associated with discrete nuclear bodies, DNA damage foci, or related assemblies.",
    "nucleolus": "Candidates localized to or functionally tied to the nucleolus.",
    "nuclear-envelope": "Candidates associated with the nuclear envelope, lamina, or nuclear pore region.",
    "chromatin": "Candidates with chromatin, chromosome, histone, or DNA-associated localization/evidence.",
    "rejected": "Reports eliminated or rejected by screening rules; retained for transparency and auditability.",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_index() -> tuple[dict, list[dict]]:
    data = json.loads((DOCS / "data" / "protein_report_index.json").read_text(encoding="utf-8"))
    return data.get("metadata", {}), data.get("records", [])


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_") or "item"


def is_external(src: str) -> bool:
    return bool(re.match(r"^(?:https?:|mailto:|tel:|data:|javascript:)", src, re.I))


def unique_dest(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    for i in range(2, 1000):
        cand = dest.with_name(f"{stem}__{i}{suffix}")
        if not cand.exists():
            return cand
    raise RuntimeError(f"Could not allocate image destination for {dest}")


def resolve_local_image(src: str, report_path: Path) -> Path | None:
    cleaned = src.strip().strip('<>"\'')
    if not cleaned or is_external(cleaned) or cleaned.startswith('#'):
        return None
    cleaned = cleaned.split('#', 1)[0].split('?', 1)[0]
    p = Path(cleaned)
    candidates = [p] if p.is_absolute() else [report_path.parent / cleaned, ROOT / cleaned, ROOT / "detail" / cleaned, report_path.parent / "IF_images" / cleaned]
    gene = report_path.parent.name
    marker = "detail/"
    if marker in cleaned:
        sub = cleaned[cleaned.index(marker):]
        candidates.append(ROOT / sub)
        parts = Path(sub).parts
        if len(parts) >= 3:
            candidates.append(report_path.parent / parts[-1])
            if parts[0] == "detail" and len(parts) == 3:
                candidates.extend((ROOT / "detail").glob(f"*/{parts[1]}/{parts[2]}"))
            if "IF_images" in parts:
                try:
                    idx = parts.index("IF_images")
                    candidates.append(report_path.parent.joinpath(*parts[idx:]))
                except ValueError:
                    pass
    if Path(cleaned).name == cleaned:
        candidates.extend((ROOT / "detail").glob(f"*/{gene}/{cleaned}"))
        candidates.extend((ROOT / "detail").glob(f"*/{gene}/IF_images/{cleaned}"))
    for cand in candidates:
        try:
            if cand.exists() and cand.is_file():
                return cand.resolve()
        except OSError:
            continue
    return None


class ImageRewriter:
    def __init__(self, rec: dict):
        self.rec = rec
        self.report_path = ROOT / rec["report_path"]
        self.dest_dir = REPORT_IMAGE_ROOT / slug(rec["gene"])
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        self.map_rows: list[dict] = []

    def copy_src(self, src: str) -> str:
        if is_external(src) or src.startswith('#'):
            return src
        source = resolve_local_image(src, self.report_path)
        if source is None:
            self.map_rows.append({"gene": self.rec["gene"], "report_path": self.rec["report_path"], "source_image": src, "copied_image": "", "copied": "False", "reason": "source_not_found"})
            return None
        dest = self.dest_dir / source.name
        if dest.exists() and source.resolve() != dest.resolve():
            try:
                if source.read_bytes() != dest.read_bytes():
                    dest = unique_dest(dest)
            except OSError:
                dest = unique_dest(dest)
        if not dest.exists():
            shutil.copy2(source, dest)
        page_path = DOCS / self.rec["docs_report_path"]
        web_src = quote(os.path.relpath(dest, page_path.parent).replace('\\', '/'))
        self.map_rows.append({"gene": self.rec["gene"], "report_path": self.rec["report_path"], "source_image": str(source), "copied_image": rel(dest), "copied": "True", "reason": "copied_or_reused"})
        return web_src

    def missing_image(self, src: str) -> str:
        return f'<div class="missing-image">Missing local image: <code>{html.escape(src)}</code></div>'

    def markdown_image(self, match: re.Match) -> str:
        alt = html.escape(match.group(1) or "image")
        raw_src = match.group(2).strip()
        src = self.copy_src(raw_src)
        if src is None:
            return self.missing_image(raw_src)
        return f'<figure><img src="{html.escape(src)}" alt="{alt}"></figure>'

    def obsidian_image(self, match: re.Match) -> str:
        raw = match.group(1).strip()
        raw_src = raw.split('|', 1)[0].strip()
        alt = html.escape(Path(raw_src).name or "image")
        rewritten = self.copy_src(raw_src)
        if rewritten is None:
            return self.missing_image(raw_src)
        return f'<figure><img src="{html.escape(rewritten)}" alt="{alt}"></figure>'

    def html_img(self, match: re.Match) -> str:
        tag = match.group(0)
        src = match.group(1)
        rewritten = self.copy_src(src)
        if rewritten is None:
            return self.missing_image(src)
        return tag.replace(src, html.escape(rewritten), 1)


def inline_format(text: str, rewriter: ImageRewriter | None = None) -> str:
    if rewriter:
        text = re.sub(r"!\[\[([^\]]+)\]\]", rewriter.obsidian_image, text)
        text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", rewriter.markdown_image, text)
        text = re.sub(r"<img\b[^>]*src=[\"']([^\"']+)[\"'][^>]*>", rewriter.html_img, text, flags=re.I)
    placeholders: list[str] = []
    def hold(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"@@HTML{len(placeholders)-1}@@"
    text = re.sub(r"<figure>.*?</figure>|<img\b[^>]*>", hold, text, flags=re.I | re.S)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)
    for i, raw in enumerate(placeholders):
        text = text.replace(f"@@HTML{i}@@", raw)
    return text


def render_table(lines: list[str], rewriter: ImageRewriter | None) -> str:
    rows = [[inline_format(c.strip(), rewriter) for c in line.strip().strip('|').split('|')] for line in lines]
    if not rows:
        return ""
    out = ['<div class="table-wrap"><table>']
    start = 0
    if len(rows) > 1 and all(re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in rows[1]):
        out.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in rows[0]) + '</tr></thead><tbody>')
        start = 2
    else:
        out.append('<tbody>')
    for row in rows[start:]:
        out.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out)


def markdown_to_html(markdown: str, rewriter: ImageRewriter | None = None) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_lines: list[str] = []
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                out.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
                in_code = False
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if not line.strip():
            i += 1
            continue
        if line.strip() in {'---', '***', '___'}:
            out.append('<hr>')
            i += 1
            continue
        if line.strip().startswith('|') and line.strip().endswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines, rewriter))
            continue
        h = re.match(r"^(#{1,6})\s+(.+)$", line)
        if h:
            level = min(len(h.group(1)) + 1, 6)
            out.append(f'<h{level}>{inline_format(h.group(2), rewriter)}</h{level}>')
            i += 1
            continue
        if re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*+]\s+", "", lines[i]))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{inline_format(item, rewriter)}</li>' for item in items) + '</ul>')
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('|') and not re.match(r"^(#{1,6})\s+", lines[i]) and not re.match(r"^\s*[-*+]\s+", lines[i]) and not lines[i].strip().startswith('```'):
            para.append(lines[i].strip())
            i += 1
        out.append('<p>' + inline_format(' '.join(para), rewriter) + '</p>')
    if in_code:
        out.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
    return '\n'.join(out)


def html_page(title: str, body: str, depth: int = 0, extra_class: str = "") -> str:
    prefix = "../" * depth
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · Protein Scout</title>
  <link rel="stylesheet" href="{prefix}assets/css/style.css">
</head>
<body class="{extra_class}">
{body}
<script src="{prefix}assets/js/app.js"></script>
</body>
</html>
'''


def nav(prefix: str = "") -> str:
    return f'''<header class="topbar">
  <a class="brand" href="{prefix}index.html">Protein Scout</a>
  <nav>
    <a href="{prefix}protein_index.html">Protein Index</a>
    <a href="{prefix}category/nucleoplasm.html">Nucleoplasm</a>
    <a href="{prefix}category/nuclear-body.html">Nuclear body</a>
    <a href="{prefix}category/rejected.html">Rejected</a>
  </nav>
</header>'''


def badge(text: str, good: bool | None = None) -> str:
    cls = "badge"
    if good is True:
        cls += " good"
    elif good is False:
        cls += " muted"
    return f'<span class="{cls}">{html.escape(str(text))}</span>'


def evidence_badges(rec: dict) -> str:
    keys = [("HPA", "has_hpa"), ("IF", "has_if_image"), ("PAE", "has_pae"), ("PDB", "has_pdb"), ("PPI", "has_ppi"), ("PubMed", "has_pubmed")]
    return '<div class="badges">' + ''.join(badge(label, bool(rec.get(key))) for label, key in keys) + '</div>'


def protein_rows(records: list[dict], prefix: str = "") -> str:
    rows = []
    for rec in records:
        score = rec.get("score") if rec.get("score") is not None else ""
        nuclear = rec.get("nuclear_score") if rec.get("nuclear_score") is not None else ""
        backlog = rec.get("known_backlog_flags") or ""
        rows.append(f'''<tr data-gene="{html.escape(rec['gene'].lower())}" data-status="{html.escape(rec['status'])}" data-category="{html.escape(rec['category'])}" data-score="{score or ''}" data-nuclear-score="{nuclear or ''}">
<td><a class="gene-link" href="{prefix}{html.escape(rec['docs_report_path'])}">{html.escape(rec['gene'])}</a></td>
<td>{badge(rec['status'], rec['status'] == 'scored')}</td>
<td><a href="{prefix}category/{html.escape(rec['category'])}.html">{html.escape(rec['category'])}</a></td>
<td class="num">{html.escape(str(score or ''))}</td>
<td class="num">{html.escape(str(nuclear or ''))}</td>
<td>{evidence_badges(rec)}</td>
<td class="flags">{html.escape(backlog)}</td>
<td><a class="button small" href="{prefix}{html.escape(rec['docs_report_path'])}">Open</a></td>
</tr>''')
    return '\n'.join(rows)


def table_block(records: list[dict], prefix: str = "") -> str:
    return f'''<section class="panel table-panel">
  <div class="controls" data-controls>
    <input type="search" data-search placeholder="Search gene symbol" aria-label="Search gene symbol">
    <select data-status-filter aria-label="Filter by status"><option value="">All status</option><option value="scored">Scored</option><option value="rejected">Rejected</option></select>
    <select data-category-filter aria-label="Filter by category"><option value="">All categories</option></select>
    <button class="button" type="button" data-sort-score>Sort score</button>
    <button class="button" type="button" data-sort-nuclear>Sort nuclear score</button>
    <button class="button ghost" type="button" data-clear>Clear</button>
  </div>
  <div class="table-meta"><span data-visible-count>{len(records)}</span> visible / {len(records)} records</div>
  <div class="table-wrap">
    <table class="protein-table" data-protein-table>
      <thead><tr><th>Gene</th><th>Status</th><th>Category</th><th>Score</th><th>Nuclear score</th><th>Evidence</th><th>Backlog / manual</th><th>Detail</th></tr></thead>
      <tbody>{protein_rows(records, prefix)}</tbody>
    </table>
  </div>
</section>'''


def write_css() -> None:
    css = r''':root {
  --bg: #f7f8fa; --surface: #ffffff; --ink: #1f2933; --muted: #667085; --line: #d8dee8;
  --accent: #0f766e; --warn: #b45309; --good: #047857; --chip: #eef2f7;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.5; }
a { color: #0b5cab; text-decoration: none; } a:hover { text-decoration: underline; }
.topbar { position: sticky; top: 0; z-index: 10; display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 12px 24px; border-bottom: 1px solid var(--line); background: rgba(255,255,255,.96); backdrop-filter: blur(8px); }
.brand { font-weight: 760; color: var(--ink); letter-spacing: 0; }
.topbar nav { display: flex; flex-wrap: wrap; gap: 14px; font-size: 14px; }
.container { width: min(1440px, calc(100% - 32px)); margin: 0 auto; padding: 28px 0 56px; }
.hero { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(280px, .8fr); gap: 28px; align-items: end; padding: 26px 0 18px; }
h1 { margin: 0 0 10px; font-size: 38px; line-height: 1.12; letter-spacing: 0; } h2 { margin: 28px 0 12px; font-size: 24px; letter-spacing: 0; } h3 { margin: 22px 0 10px; font-size: 18px; letter-spacing: 0; }
.lede { max-width: 880px; color: var(--muted); font-size: 16px; }
.stats-grid { display: grid; grid-template-columns: repeat(6, minmax(120px, 1fr)); gap: 12px; margin: 18px 0 24px; }
.stat { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 14px; }
.stat .label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }
.stat .value { display: block; margin-top: 6px; font-size: 24px; font-weight: 760; }
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 16px; margin: 16px 0; }
.nav-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; }
.button { display: inline-flex; align-items: center; justify-content: center; min-height: 36px; padding: 8px 12px; border: 1px solid var(--line); border-radius: 6px; background: #fff; color: var(--ink); font-weight: 650; cursor: pointer; }
.button:hover { border-color: var(--accent); text-decoration: none; } .button.primary { background: var(--accent); color: #fff; border-color: var(--accent); } .button.ghost { color: var(--muted); } .button.small { min-height: 30px; padding: 5px 9px; font-size: 13px; }
.controls { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-bottom: 12px; }
input, select { min-height: 36px; border: 1px solid var(--line); border-radius: 6px; padding: 7px 10px; background: #fff; color: var(--ink); font: inherit; } input[type="search"] { min-width: min(360px, 100%); }
.table-meta { color: var(--muted); font-size: 13px; margin-bottom: 8px; }
.table-wrap { overflow: auto; border: 1px solid var(--line); border-radius: 8px; background: #fff; }
table { width: 100%; border-collapse: collapse; font-size: 14px; } th, td { padding: 9px 10px; border-bottom: 1px solid var(--line); vertical-align: top; text-align: left; }
th { position: sticky; top: 49px; background: #f3f5f8; color: #344054; font-size: 12px; text-transform: uppercase; letter-spacing: .04em; z-index: 1; }
tr:hover td { background: #f8fbff; } .num { text-align: right; font-variant-numeric: tabular-nums; } .gene-link { font-weight: 760; }
.badges { display: flex; flex-wrap: wrap; gap: 5px; } .badge { display: inline-flex; align-items: center; min-height: 22px; padding: 2px 7px; border-radius: 999px; background: var(--chip); color: #344054; font-size: 12px; font-weight: 650; white-space: nowrap; } .badge.good { background: #dff6ed; color: var(--good); } .badge.muted { background: #f1f3f5; color: #98a2b3; }
.flags { max-width: 260px; color: var(--warn); font-size: 13px; }
.report-shell { display: grid; grid-template-columns: minmax(0, 1fr); gap: 16px; } .report-meta { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.source-path { color: var(--muted); font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; overflow-wrap: anywhere; }
.report-body { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 20px; } .report-body h2:first-child { margin-top: 0; }
.report-body pre { overflow: auto; background: #101828; color: #f9fafb; padding: 12px; border-radius: 8px; } .report-body code { background: #eef2f7; padding: 1px 4px; border-radius: 4px; } .report-body pre code { background: transparent; padding: 0; }
.report-body figure { margin: 14px 0; } .report-body img { max-width: 100%; height: auto; border: 1px solid var(--line); border-radius: 6px; background: #fff; }
.missing-image { margin: 12px 0; padding: 10px 12px; border: 1px dashed var(--warn); border-radius: 6px; color: var(--warn); background: #fff7ed; overflow-wrap: anywhere; }
.footer-note { color: var(--muted); font-size: 13px; margin-top: 26px; }
@media (max-width: 900px) { .topbar { align-items: flex-start; flex-direction: column; } .hero { grid-template-columns: 1fr; } .stats-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } h1 { font-size: 30px; } th { top: 98px; } }
'''
    (ASSETS / "css" / "style.css").write_text(css, encoding="utf-8")


def write_js() -> None:
    js = r'''function initProteinTables() {
  document.querySelectorAll('[data-protein-table]').forEach((table) => {
    const panel = table.closest('.table-panel') || document;
    const search = panel.querySelector('[data-search]');
    const statusFilter = panel.querySelector('[data-status-filter]');
    const categoryFilter = panel.querySelector('[data-category-filter]');
    const clear = panel.querySelector('[data-clear]');
    const sortScore = panel.querySelector('[data-sort-score]');
    const sortNuclear = panel.querySelector('[data-sort-nuclear]');
    const visibleCount = panel.querySelector('[data-visible-count]');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const categories = Array.from(new Set(rows.map((row) => row.dataset.category).filter(Boolean))).sort();
    if (categoryFilter && categoryFilter.options.length <= 1) {
      categories.forEach((cat) => { const opt = document.createElement('option'); opt.value = cat; opt.textContent = cat; categoryFilter.appendChild(opt); });
    }
    function apply() {
      const q = (search?.value || '').trim().toLowerCase();
      const status = statusFilter?.value || '';
      const category = categoryFilter?.value || '';
      let shown = 0;
      rows.forEach((row) => {
        const ok = (!q || row.dataset.gene.includes(q)) && (!status || row.dataset.status === status) && (!category || row.dataset.category === category);
        row.hidden = !ok; if (ok) shown += 1;
      });
      if (visibleCount) visibleCount.textContent = String(shown);
    }
    function sortBy(field) {
      const sorted = rows.slice().sort((a, b) => {
        const av = parseFloat(a.dataset[field] || '-Infinity');
        const bv = parseFloat(b.dataset[field] || '-Infinity');
        return bv - av || a.dataset.gene.localeCompare(b.dataset.gene);
      });
      sorted.forEach((row) => tbody.appendChild(row));
    }
    search?.addEventListener('input', apply); statusFilter?.addEventListener('change', apply); categoryFilter?.addEventListener('change', apply);
    clear?.addEventListener('click', () => { if (search) search.value = ''; if (statusFilter) statusFilter.value = ''; if (categoryFilter) categoryFilter.value = ''; apply(); });
    sortScore?.addEventListener('click', () => sortBy('score'));
    sortNuclear?.addEventListener('click', () => sortBy('nuclearScore'));
    apply();
  });
}
document.addEventListener('DOMContentLoaded', initProteinTables);
'''
    (ASSETS / "js" / "app.js").write_text(js, encoding="utf-8")


def build_home(meta: dict, records: list[dict]) -> None:
    status_counts = Counter(r["status"] for r in records)
    cat_counts = Counter(r["category"] for r in records)
    duplicate_records = sum(1 for r in records if int(r.get("duplicate_count") or 1) > 1)
    backlog_records = sum(1 for r in records if r.get("known_backlog_flags"))
    preview = sorted([r for r in records if r["status"] == "scored"], key=lambda r: float(r.get("score") or -1), reverse=True)[:80]
    stat_cards = ''.join([
        f'<div class="stat"><span class="label">Total reports</span><span class="value">{len(records):,}</span></div>',
        f'<div class="stat"><span class="label">Scored</span><span class="value">{status_counts.get("scored",0):,}</span></div>',
        f'<div class="stat"><span class="label">Rejected</span><span class="value">{status_counts.get("rejected",0):,}</span></div>',
        f'<div class="stat"><span class="label">Categories</span><span class="value">{len(cat_counts):,}</span></div>',
        f'<div class="stat"><span class="label">Duplicates</span><span class="value">{duplicate_records:,}</span></div>',
        f'<div class="stat"><span class="label">Backlog flags</span><span class="value">{backlog_records:,}</span></div>',
    ])
    nav_buttons = ''.join(f'<a class="button" href="category/{cat}.html">{html.escape(cat)} <span class="badge">{cat_counts.get(cat,0)}</span></a>' for cat in CATEGORY_DESCRIPTIONS)
    body = nav("") + f'''<main class="container">
  <section class="hero"><div><h1>Protein Scout / TEreg Finding Atlas</h1><p class="lede">A static research atlas for TE-regulation candidate protein evaluations. The site is generated from the existing master summary and the original per-protein reports without modifying scientific report content.</p></div><div class="panel"><h2>Screening focus</h2><p>Nuclear localization, domain evidence, novelty, structure evidence, protein interactions, and literature support are summarized for fast review.</p></div></section>
  <section class="stats-grid">{stat_cards}</section>
  <section class="panel"><h2>Current data state</h2><p>Excel coverage is recorded as 4,756/4,756. Known non-blocking backlog remains visible: 832 need reharvest backlog, 43 duplicate conflicts, and pre-existing gate errors.</p></section>
  <section class="panel"><h2>Browse</h2><div class="nav-grid"><a class="button primary" href="protein_index.html">All proteins</a>{nav_buttons}</div></section>
  <h2>High-scoring preview</h2>{table_block(preview, '')}
</main>'''
    (DOCS / "index.html").write_text(html_page("Home", body, 0, "home"), encoding="utf-8")


def build_index(records: list[dict]) -> None:
    body = nav("") + f'''<main class="container"><h1>Protein Index</h1><p class="lede">Search, filter, and sort all generated protein report records. Detail pages preserve the original evaluation report body as rendered HTML.</p>{table_block(records, '')}</main>'''
    (DOCS / "protein_index.html").write_text(html_page("Protein Index", body), encoding="utf-8")


def build_categories(records: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        by_cat[rec["category"]].append(rec)
    all_categories = list(CATEGORY_DESCRIPTIONS)
    for cat in sorted(set(by_cat) - set(all_categories)):
        all_categories.append(cat)
    for cat in all_categories:
        recs = sorted(by_cat.get(cat, []), key=lambda r: (-(float(r.get("score") or -1)), r["gene"]))
        body = nav("../") + f'''<main class="container"><h1>Category: {html.escape(cat)}</h1><p class="lede">{html.escape(CATEGORY_DESCRIPTIONS.get(cat, "Generated category page."))}</p><section class="stats-grid"><div class="stat"><span class="label">Records</span><span class="value">{len(recs):,}</span></div></section><p><a class="button" href="../index.html">Home</a> <a class="button" href="../protein_index.html">All proteins</a></p>{table_block(recs, '../')}</main>'''
        (DOCS / "category" / f"{cat}.html").write_text(html_page(f"Category {cat}", body, 1), encoding="utf-8")


def build_reports(records: list[dict]) -> list[dict]:
    image_rows: list[dict] = []
    for rec in records:
        src = ROOT / rec["report_path"]
        text = src.read_text(encoding="utf-8", errors="replace")
        rewriter = ImageRewriter(rec)
        rendered = markdown_to_html(text, rewriter)
        image_rows.extend(rewriter.map_rows)
        score = rec.get("score") if rec.get("score") is not None else "NA"
        nuclear = rec.get("nuclear_score") if rec.get("nuclear_score") is not None else "NA"
        body = nav("../") + f'''<main class="container report-shell"><section class="panel"><h1>{html.escape(rec['gene'])}</h1><div class="report-meta">{badge(rec['status'], rec['status'] == 'scored')}{badge(rec['category'])}{badge('Score: ' + str(score))}{badge('Nuclear: ' + str(nuclear))}<a class="button small" href="../protein_index.html">Protein Index</a><a class="button small" href="../category/{html.escape(rec['category'])}.html">Category page</a></div><p class="source-path">Original detail path: {html.escape(rec['report_path'])}</p></section><article class="report-body">{rendered}</article></main>'''
        out = DOCS / rec["docs_report_path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_page(rec["gene"], body, 1, "report-page"), encoding="utf-8")
    return image_rows


def write_image_map(rows: list[dict]) -> Path:
    path = ENGINEERING / f"step4b_image_copy_map_{TS}.tsv"
    fields = ["gene", "report_path", "source_image", "copied_image", "copied", "reason"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader(); writer.writerows(rows)
    return path


def main() -> None:
    meta, records = load_index()
    write_css(); write_js(); build_home(meta, records); build_index(records); build_categories(records)
    image_rows = build_reports(records)
    image_map = write_image_map(image_rows)
    copied = sum(1 for r in image_rows if r.get("copied") == "True")
    print(f"pages_reports={len(records)} copied_images={copied} image_map={image_map}")

if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()
