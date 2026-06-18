#!/usr/bin/env python3
"""Parse protein-finding.md and generate a standalone interactive heatmap HTML."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
INTERESTED = ROOT / "interested_proteins.tsv"
OUTPUT = ROOT / "docs" / "heatmap.html"

# ── colour palette ──────────────────────────────────────────────
# Blues -> purples for scores (0 → 100)
HEAT_COLORS = [
    "#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6",
    "#4292c6", "#2171b5", "#08519c", "#08306b",
]
# Rejected zone colour
REJECTED_COLOR = "#d9d9d9"
# Rejected by PubMed >100 gets a slightly different shade
PUBMED_REJECTED_COLOR = "#bdbdbd"

CATEGORY_LABELS = {
    "chromatin": "Chromatin",
    "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuclear Speckle",
    "nucleus-cytoplasm": "Nucleus-Cytoplasm",
    "nucleoplasm": "Nucleoplasm",
    "nuclear-envelope": "Nuclear Envelope",
    "nuclear-body": "Nuclear Body",
}

CATEGORY_SHORT = {
    "chromatin": "chromatin",
    "nucleolus": "nucleolus",
    "nuclear-speckle": "nuc-speckle",
    "nucleus-cytoplasm": "nuc-cyto",
    "nucleoplasm": "nucleoplasm",
    "nuclear-envelope": "nuc-envelope",
    "nuclear-body": "nuc-body",
}

CATEGORY_COLORS = {
    "chromatin": "#e41a1c",
    "nucleolus": "#377eb8",
    "nuclear-speckle": "#4daf4a",
    "nucleus-cytoplasm": "#984ea3",
    "nucleoplasm": "#ff7f00",
    "nuclear-envelope": "#a65628",
    "nuclear-body": "#f781bf",
}


@dataclass
class Protein:
    gene: str
    category: str
    score: float | None = None
    nuc: int | None = None
    size: int | None = None
    nov: int | None = None
    struct: int | None = None
    dom: int | None = None
    ppi: int | None = None
    cross: str = ""
    stars: str = ""
    recommendation: str = ""
    rejected_reason: str = ""
    pubmed: str = ""
    index_in_category: int = 0
    interested: bool = False
    interested_note: str = ""


@dataclass
class HeatmapData:
    scored: list[Protein] = field(default_factory=list)
    rejected: list[Protein] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    cat_counts: dict[str, int] = field(default_factory=dict)
    cat_ranges: dict[str, tuple[int, int]] = field(default_factory=dict)


def load_interested(path: Path) -> dict[str, str]:
    """Load interested_proteins.tsv -> {gene: note}. Creates template if missing."""
    if not path.exists():
        path.write_text("gene\tnote\nHP1BP3\t示例: H1-like linker histone, 染色质调控核心\n", encoding="utf-8")
        return {}
    interested: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        gene = parts[0].strip().upper()
        note = parts[1].strip() if len(parts) > 1 else ""
        interested[gene] = note
    return interested


def score_to_color(score: float, min_s: float, max_s: float) -> str:
    """Map score to hex colour in the blues gradient."""
    if score is None or max_s == min_s:
        return HEAT_COLORS[4]
    t = (score - min_s) / (max_s - min_s)
    t = max(0.0, min(1.0, t))
    idx = t * (len(HEAT_COLORS) - 1)
    lo = int(idx)
    hi = min(lo + 1, len(HEAT_COLORS) - 1)
    frac = idx - lo
    c1 = _hex_to_rgb(HEAT_COLORS[lo])
    c2 = _hex_to_rgb(HEAT_COLORS[hi])
    r = int(c1[0] + (c2[0] - c1[0]) * frac)
    g = int(c1[1] + (c2[1] - c1[1]) * frac)
    b = int(c1[2] + (c2[2] - c1[2]) * frac)
    return f"#{r:02x}{g:02x}{b:02x}"


def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def parse_summary(path: Path, interested: dict[str, str]) -> HeatmapData:
    text = path.read_text(encoding="utf-8")
    data = HeatmapData()

    scored_categories = [
        "chromatin", "nucleolus", "nuclear-speckle",
        "nucleus-cytoplasm", "nucleoplasm", "nuclear-envelope", "nuclear-body",
    ]

    # Find the scored section start (after the stats line)
    sections = {}
    for cat in scored_categories:
        m = re.search(rf"\n## {cat}\n", text)
        if m:
            sections[cat] = m.start()

    # Find eliminated section
    elim_m = re.search(r"\n## 已淘汰\n", text)
    elim_start = elim_m.start() if elim_m else len(text)

    # Order sections by position
    ordered = sorted(sections.items(), key=lambda x: x[1])
    for i, (cat, start) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else elim_start
        section = text[start:end]
        data.categories.append(cat)
        parse_scored_section(section, cat, data, interested)

    # Parse eliminated
    if elim_m:
        elim_section = text[elim_start:]
        parse_eliminated_section(elim_section, data, interested)

    # Compute category ranges for the heatmap (global row indices)
    idx = 0
    for cat in data.categories:
        count = data.cat_counts.get(cat, 0)
        if count > 0:
            data.cat_ranges[cat] = (idx, idx + count)
            idx += count
    # Rejected
    if data.rejected:
        data.cat_ranges["rejected"] = (idx, idx + len(data.rejected))

    return data


def parse_scored_section(section: str, cat: str, data: HeatmapData, interested: dict[str, str]):
    """Parse a scored category table section."""
    rows: list[Protein] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("| ") or "---" in line or "基因" in line or "详情" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 11:
            continue
        try:
            rank = int(cells[0])
            gene = cells[1].strip()
            nuc = int(cells[2])
            size = int(cells[3])
            nov = int(cells[4])
            struct = int(cells[5])
            dom = int(cells[6])
            ppi = int(cells[7])
            cross = cells[8].strip()
            score = float(cells[9])
            stars = cells[10].strip()
        except (ValueError, IndexError):
            continue

        p = Protein(
            gene=gene,
            category=cat,
            score=score,
            nuc=nuc, size=size, nov=nov, struct=struct, dom=dom, ppi=ppi,
            cross=cross, stars=stars,
            index_in_category=rank,
            interested=(gene.upper() in interested),
            interested_note=interested.get(gene.upper(), ""),
            recommendation=stars,
        )
        rows.append(p)

    rows.sort(key=lambda x: x.score if x.score is not None else 0, reverse=True)
    for i, p in enumerate(rows):
        p.index_in_category = i + 1
    data.scored.extend(rows)
    data.cat_counts[cat] = len(rows)


def parse_eliminated_section(section: str, data: HeatmapData, interested: dict[str, str]):
    rows: list[Protein] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("| ") or "---" in line or "基因" in line or "详情" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        try:
            gene = cells[1].strip()
            reason = cells[2].strip()
            pubmed = cells[3].strip()
        except (ValueError, IndexError):
            continue

        p = Protein(
            gene=gene,
            category="rejected",
            score=None,
            nuc=None, size=None, nov=None, struct=None, dom=None, ppi=None,
            cross="", stars="",
            rejected_reason=reason,
            pubmed=pubmed,
            interested=(gene.upper() in interested),
            interested_note=interested.get(gene.upper(), ""),
        )
        rows.append(p)
    data.rejected = rows


def build_html(data: HeatmapData, interested_count: int) -> str:
    """Build a standalone HTML page with embedded data and interactive heatmap."""
    all_scored = data.scored
    all_rejected = data.rejected
    total = len(all_scored) + len(all_rejected)

    # Score stats
    scores = [p.score for p in all_scored if p.score is not None]
    min_score = min(scores) if scores else 0
    max_score = max(scores) if scores else 100

    # Build row-by-row colour data
    row_data = []
    for p in all_scored:
        row_data.append({
            "gene": p.gene,
            "cat": p.category,
            "catLabel": CATEGORY_LABELS.get(p.category, p.category),
            "score": p.score,
            "nuc": p.nuc, "size": p.size, "nov": p.nov,
            "struct": p.struct, "dom": p.dom, "ppi": p.ppi,
            "cross": p.cross,
            "stars": p.stars,
            "interested": p.interested,
            "note": p.interested_note,
            "rejected": False,
        })
    for p in all_rejected:
        row_data.append({
            "gene": p.gene,
            "cat": "rejected",
            "catLabel": "Rejected",
            "score": None,
            "nuc": None, "size": None, "nov": None,
            "struct": None, "dom": None, "ppi": None,
            "cross": None,
            "stars": None,
            "rejected": True,
            "reason": p.rejected_reason,
            "pubmed": p.pubmed,
            "interested": p.interested,
            "note": p.interested_note,
        })

    # Category metadata
    cat_meta = {}
    for cat in data.categories:
        count = data.cat_counts.get(cat, 0)
        cat_meta[cat] = {
            "label": CATEGORY_LABELS.get(cat, cat),
            "short": CATEGORY_SHORT.get(cat, cat),
            "color": CATEGORY_COLORS.get(cat, "#888"),
            "count": count,
        }
    cat_meta["rejected"] = {
        "label": "Rejected",
        "short": "rejected",
        "color": "#999",
        "count": len(all_rejected),
    }

    rows_json = json.dumps(row_data, ensure_ascii=False)
    cat_json = json.dumps(cat_meta, ensure_ascii=False)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Protein Scout · Screening Heatmap</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background:#1a1a2e; color:#e0e0e0; overflow:hidden; height:100vh; display:flex; }}
:root {{ --marker:#fbbf24; --selected:#60a5fa; --header-bg:#16213e; --panel-bg:#0f3460; }}

/* ── LEFT: density strip ── */
#left {{ flex:1; display:flex; flex-direction:column; min-width:300px; }}
#toolbar {{ background:var(--header-bg); padding:10px 16px; display:flex; gap:12px; align-items:center; flex-wrap:wrap; border-bottom:1px solid #2a2a4a; }}
#toolbar h1 {{ font-size:16px; font-weight:600; white-space:nowrap; color:#f0f0f0; }}
#toolbar .stat {{ font-size:12px; color:#94a3b8; }}
#toolbar .stat b {{ color:#fbbf24; }}
#toolbar .sep {{ width:1px; height:20px; background:#2a2a4a; }}

#heatmap-container {{ flex:1; overflow-y:auto; overflow-x:hidden; position:relative; }}
#heatmap-canvas {{ display:block; width:100%; }}

/* ── RIGHT: detail panel ── */
#right {{ width:420px; background:var(--panel-bg); display:flex; flex-direction:column; border-left:1px solid #2a2a4a; }}
#right-header {{ background:var(--header-bg); padding:12px 16px; border-bottom:1px solid #2a2a4a; }}
#right-header h2 {{ font-size:14px; font-weight:600; }}
#search-box {{ width:100%; padding:8px 12px; border-radius:6px; border:1px solid #334; background:#1a1a2e; color:#e0e0e0; font-size:13px; margin-top:8px; outline:none; }}
#search-box:focus {{ border-color:#60a5fa; }}

#detail-list {{ flex:1; overflow-y:auto; padding:4px 0; }}
.detail-row {{ display:flex; align-items:center; padding:4px 12px; gap:8px; font-size:12px; cursor:pointer; border-bottom:1px solid #1a1a2e; transition:background .1s; }}
.detail-row:hover {{ background:rgba(255,255,255,.05); }}
.detail-row.active {{ background:rgba(96,165,250,.15); }}
.detail-row .gene {{ font-weight:700; min-width:80px; font-size:13px; }}
.detail-row .cat-tag {{ font-size:10px; padding:1px 6px; border-radius:3px; white-space:nowrap; }}
.detail-row .score-badge {{ font-weight:700; min-width:42px; text-align:right; font-size:14px; }}
.detail-row .stars {{ font-size:11px; min-width:60px; text-align:right; }}
.detail-row .marker-dot {{ width:6px; height:6px; border-radius:50%; background:var(--marker); flex-shrink:0; }}

/* ── floating tooltip ── */
#tooltip {{ position:fixed; pointer-events:none; background:#1e293b; border:1px solid #334; border-radius:8px; padding:10px 14px; font-size:12px; display:none; z-index:999; max-width:260px; box-shadow:0 4px 12px rgba(0,0,0,.4); }}
#tooltip .tt-gene {{ font-size:14px; font-weight:700; margin-bottom:4px; }}
#tooltip .tt-cat {{ color:#94a3b8; margin-bottom:6px; }}
#tooltip .tt-marker {{ color:var(--marker); font-style:italic; margin-bottom:4px; display:none; }}
#tooltip .tt-grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:2px 8px; font-size:11px; }}
#tooltip .tt-dim {{ color:#94a3b8; }}
#tooltip .tt-val {{ font-weight:600; text-align:right; }}

/* ── scrollbar ── */
::-webkit-scrollbar {{ width:6px; }}
::-webkit-scrollbar-track {{ background:transparent; }}
::-webkit-scrollbar-thumb {{ background:#334; border-radius:3px; }}
::-webkit-scrollbar-thumb:hover {{ background:#445; }}

/* ── filter pills ── */
#filter-bar {{ display:flex; gap:6px; flex-wrap:wrap; padding:8px 16px; background:var(--header-bg); border-bottom:1px solid #2a2a4a; }}
.pill {{ font-size:11px; padding:3px 10px; border-radius:12px; cursor:pointer; border:1px solid transparent; background:#1a1a2e; color:#94a3b8; transition:.15s; white-space:nowrap; }}
.pill.on {{ border-color:currentColor; }}
.pill.all {{ color:#e0e0e0; }}
.pill.interested {{ color:var(--marker); }}
.pill:hover {{ opacity:.8; }}

/* ── legend ── */
#legend {{ display:flex; align-items:center; gap:4px; padding:6px 16px; background:var(--header-bg); border-top:1px solid #2a2a4a; font-size:11px; color:#94a3b8; }}
#legend .gradient {{ width:120px; height:10px; border-radius:5px; }}
#legend .gradient.rej {{ width:20px; background:var(--rejected); }}
</style>
</head>
<body>

<!-- LEFT PANEL -->
<div id="left">
  <div id="toolbar">
    <h1>🔬 Protein Scout · Screening Heatmap</h1>
    <span class="sep"></span>
    <span class="stat">Scored: <b>{len(all_scored):,}</b></span>
    <span class="stat">Rejected: <b>{len(all_rejected):,}</b></span>
    <span class="stat">Total: <b>{total:,}</b></span>
    <span class="sep"></span>
    <span class="stat">⭐ Marked: <b id="marker-count">{interested_count}</b></span>
  </div>
  <div id="filter-bar">
    <span class="pill all on" data-filter="all">All</span>
    <span class="pill interested" data-filter="interested">⭐ Marked</span>
    <span class="pill" data-filter="scored">Scored</span>
    <span class="pill" data-filter="rejected">Rejected</span>
  </div>
  <div id="heatmap-container">
    <canvas id="heatmap-canvas"></canvas>
  </div>
  <div id="legend">
    Score: <span class="gradient" style="background:linear-gradient(90deg,{HEAT_COLORS[0]},{HEAT_COLORS[-1]});"></span>
    0 — 100 &nbsp;|&nbsp;
    Rejected: <span class="gradient rej" style="background:{REJECTED_COLOR};"></span>
    &nbsp;|&nbsp; ⭐ = Marked
  </div>
</div>

<!-- RIGHT PANEL -->
<div id="right">
  <div id="right-header">
    <h2>Detail Table</h2>
    <input id="search-box" type="search" placeholder="Search gene symbol...">
  </div>
  <div id="detail-list"></div>
</div>

<!-- TOOLTIP -->
<div id="tooltip">
  <div class="tt-gene"></div>
  <div class="tt-cat"></div>
  <div class="tt-marker"></div>
  <div class="tt-grid"></div>
</div>

<script>
const ROWS = {rows_json};
const CATS = {cat_json};
const MIN_SCORE = {min_score};
const MAX_SCORE = {max_score};
const REJECTED_COLOR = "{REJECTED_COLOR}";
const PUBMED_REJECTED_COLOR = "{PUBMED_REJECTED_COLOR}";
const HEAT_COLORS = {json.dumps(HEAT_COLORS)};
const ROW_HEIGHT = 3;

// ── Build flat row index → ROWS ──
let allRows = ROWS;
let visibleRows = [...ROWS];
let currentFilter = 'all';
let selectedRowIdx = -1;
let searchQuery = '';

// ── Category boundary lookup ──
let catRanges = {{}};
let curCat = null;
for (let i = 0; i < ROWS.length; i++) {{
    if (ROWS[i].cat !== curCat) {{
        curCat = ROWS[i].cat;
        if (!catRanges[curCat]) catRanges[curCat] = {{ start: i, end: i }};
    }}
    catRanges[curCat].end = i + 1;
}}

// ── Score → colour ──
function scoreColor(score) {{
    if (score == null) return REJECTED_COLOR;
    const t = (score - MIN_SCORE) / (MAX_SCORE - MIN_SCORE);
    const idx = Math.max(0, Math.min(1, t)) * (HEAT_COLORS.length - 1);
    const lo = Math.floor(idx);
    const hi = Math.min(lo + 1, HEAT_COLORS.length - 1);
    const frac = idx - lo;
    const c1 = hexRgb(HEAT_COLORS[lo]);
    const c2 = hexRgb(HEAT_COLORS[hi]);
    const r = Math.round(c1[0] + (c2[0] - c1[0]) * frac);
    const g = Math.round(c1[1] + (c2[1] - c1[1]) * frac);
    const b = Math.round(c1[2] + (c2[2] - c1[2]) * frac);
    return `rgb(${{r}},${{g}},${{b}})`;
}}
function hexRgb(h) {{ return [parseInt(h.slice(1,3),16), parseInt(h.slice(3,5),16), parseInt(h.slice(5,7),16)]; }}

// ── Canvas ──
const canvas = document.getElementById('heatmap-canvas');
const ctx = canvas.getContext('2d');
const container = document.getElementById('heatmap-container');
const tooltip = document.getElementById('tooltip');
const detailList = document.getElementById('detail-list');
const searchBox = document.getElementById('search-box');
const markerCount = document.getElementById('marker-count');

function resize() {{
    const dpr = window.devicePixelRatio || 1;
    const w = container.clientWidth;
    const h = Math.max(visibleRows.length * ROW_HEIGHT, container.clientHeight);
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
}}

let catStartY = [];  // [{{startY, endY, cat}}]

function draw() {{
    const w = canvas.style.width ? parseFloat(canvas.style.width) : container.clientWidth;
    const h = visibleRows.length * ROW_HEIGHT;

    ctx.clearRect(0, 0, w, h);

    // Category separators
    catStartY = [];
    let prevCat = null;

    const markerArea = 16; // left column for interested markers
    const barStart = markerArea + 4;
    const barWidth = w - barStart - 4;

    for (let i = 0; i < visibleRows.length; i++) {{
        const row = visibleRows[i];
        const y = i * ROW_HEIGHT;

        // Category header background
        if (row.cat !== prevCat) {{
            catStartY.push({{ y, cat: row.cat, label: CATS[row.cat]?.label || row.cat, color: CATS[row.cat]?.color || '#888' }});
            if (prevCat !== null) {{
                // Draw separator line
                ctx.fillStyle = '#334155';
                ctx.fillRect(0, y - 1, w, 2);
            }}
            prevCat = row.cat;
        }}

        // Marker column (gold if interested)
        if (row.interested) {{
            ctx.fillStyle = '#fbbf24';
            ctx.fillRect(2, y + 0.5, markerArea - 4, ROW_HEIGHT - 1);
        }} else {{
            ctx.fillStyle = 'rgba(255,255,255,0.03)';
            ctx.fillRect(2, y + 0.5, markerArea - 4, ROW_HEIGHT - 1);
        }}

        // Score colour bar
        ctx.fillStyle = scoreColor(row.score);
        ctx.fillRect(barStart, y, barWidth, ROW_HEIGHT);
    }}

    // Draw category labels on the left side
    ctx.save();
    ctx.font = '11px -apple-system, sans-serif';
    for (const cs of catStartY) {{
        const midY = cs.y + (ROW_HEIGHT * (catRanges[cs.cat]?.end || visibleRows.length) - catRanges[cs.cat]?.start || 0) * ROW_HEIGHT / 2;
        ctx.fillStyle = cs.color;
        ctx.textBaseline = 'middle';
        ctx.fillText(cs.label, 20, Math.max(cs.y + 8, midY));
    }}
    ctx.restore();
}}

// ── Hover ──
canvas.addEventListener('mousemove', (e) => {{
    const rect = canvas.getBoundingClientRect();
    const y = e.clientY - rect.top;
    const rowIdx = Math.floor(y / ROW_HEIGHT);
    if (rowIdx < 0 || rowIdx >= visibleRows.length) {{
        tooltip.style.display = 'none';
        return;
    }}
    const row = visibleRows[rowIdx];

    const ttGene = tooltip.querySelector('.tt-gene');
    const ttCat = tooltip.querySelector('.tt-cat');
    const ttMarker = tooltip.querySelector('.tt-marker');
    const ttGrid = tooltip.querySelector('.tt-grid');

    ttGene.textContent = row.gene;
    ttCat.textContent = row.catLabel + (row.rejected ? '' : ' · ' + (row.score != null ? row.score.toFixed(1) : '?') + ' pts');
    ttGrid.innerHTML = '';

    if (row.interested) {{
        ttMarker.style.display = 'block';
        ttMarker.textContent = '⭐ Marked' + (row.note ? ': ' + row.note : '');
    }} else {{
        ttMarker.style.display = 'none';
    }}

    if (!row.rejected && row.nuc != null) {{
        ttGrid.innerHTML = `
            <span class="tt-dim">核</span><span class="tt-val">${{row.nuc}}</span>
            <span class="tt-dim">大</span><span class="tt-val">${{row.size}}</span>
            <span class="tt-dim">新</span><span class="tt-val">${{row.nov}}</span>
            <span class="tt-dim">结</span><span class="tt-val">${{row.struct}}</span>
            <span class="tt-dim">域</span><span class="tt-val">${{row.dom}}</span>
            <span class="tt-dim">PPI</span><span class="tt-val">${{row.ppi}}</span>
            <span class="tt-dim">互证</span><span class="tt-val">${{row.cross}}</span>
            <span class="tt-dim">推荐</span><span class="tt-val">${{row.stars || '-'}}</span>
        `;
    }} else if (row.rejected) {{
        ttGrid.innerHTML = `
            <span class="tt-dim" style="grid-column:1/5">${{row.reason || ''}}</span>
            <span class="tt-dim" style="grid-column:1/3">PubMed</span><span class="tt-val" style="grid-column:3/5;text-align:left">${{row.pubmed || '-'}}</span>
        `;
    }}

    tooltip.style.display = 'block';
    tooltip.style.left = (e.clientX + 18) + 'px';
    tooltip.style.top = (e.clientY - 10) + 'px';
}});

canvas.addEventListener('mouseleave', () => {{
    tooltip.style.display = 'none';
}});

canvas.addEventListener('click', (e) => {{
    const rect = canvas.getBoundingClientRect();
    const y = e.clientY - rect.top;
    const rowIdx = Math.floor(y / ROW_HEIGHT);
    if (rowIdx < 0 || rowIdx >= visibleRows.length) return;
    const row = visibleRows[rowIdx];
    // Find this row in allRows
    const globalIdx = ROWS.indexOf(row);
    selectRow(globalIdx);
    // Scroll detail list to match
    const detailRow = detailList.querySelector(`[data-idx="${{globalIdx}}"]`);
    if (detailRow) detailRow.scrollIntoView({{ block: 'center', behavior: 'smooth' }});
}});

// ── Detail table ──
function renderDetailList() {{
    detailList.innerHTML = '';
    let rows = searchQuery ? ROWS.filter(r => r.gene.toUpperCase().includes(searchQuery.toUpperCase())) : visibleRows;

    for (let i = 0; i < rows.length; i++) {{
        const row = rows[i];
        const idx = ROWS.indexOf(row);
        const div = document.createElement('div');
        div.className = 'detail-row' + (idx === selectedRowIdx ? ' active' : '');
        div.dataset.idx = idx;

        let markerHtml = row.interested ? '<span class="marker-dot"></span>' : '<span style="width:6px;flex-shrink:0"></span>';
        let scoreHtml = row.score != null
            ? `<span class="score-badge">${{row.score.toFixed(1)}}</span><span class="stars">${{row.stars || ''}}</span>`
            : `<span class="score-badge" style="color:#94a3b8">—</span><span class="stars" style="color:#94a3b8">${{row.reason ? row.reason.slice(0,20) : 'eliminated'}}</span>`;

        div.innerHTML = `
            ${{markerHtml}}
            <span class="gene">${{row.gene}}</span>
            <span class="cat-tag" style="background:${{CATS[row.cat]?.color || '#888'}}22;color:${{CATS[row.cat]?.color || '#888'}}">${{CATS[row.cat]?.short || row.cat}}</span>
            ${{scoreHtml}}
        `;

        div.addEventListener('click', () => selectRow(idx));
        div.addEventListener('mouseenter', () => highlightRow(idx));
        div.addEventListener('mouseleave', () => highlightRow(-1));
        detailList.appendChild(div);
    }}
    document.getElementById('right-header').querySelector('h2').textContent =
        searchQuery ? `Search: "${{searchQuery}}" (${{rows.length}} results)` : `Detail Table (${{visibleRows.length}} visible)`;
}}

let highlightIdx = -1;
function highlightRow(idx) {{
    highlightIdx = idx;
    draw();
    // Redraw highlight overlay
    if (idx >= 0) {{
        const visIdx = visibleRows.indexOf(ROWS[idx]);
        if (visIdx >= 0) {{
            const w = canvas.style.width ? parseFloat(canvas.style.width) : container.clientWidth;
            const y = visIdx * ROW_HEIGHT;
            ctx.fillStyle = 'rgba(255,255,255,0.15)';
            ctx.fillRect(0, y, w, ROW_HEIGHT);
        }}
    }}
}}

function selectRow(idx) {{
    selectedRowIdx = idx;
    renderDetailList();
    // Scroll map to position
    if (idx >= 0) {{
        const visIdx = visibleRows.indexOf(ROWS[idx]);
        if (visIdx >= 0) {{
            const scrollY = visIdx * ROW_HEIGHT - container.clientHeight / 2;
            container.scrollTop = Math.max(0, scrollY);
        }}
    }}
}}

// ── Filter ──
document.getElementById('filter-bar').addEventListener('click', (e) => {{
    const pill = e.target.closest('.pill');
    if (!pill) return;
    const filter = pill.dataset.filter;

    document.querySelectorAll('.pill').forEach(p => p.classList.remove('on'));
    pill.classList.add('on');
    currentFilter = filter;

    applyFilter();
}});

function applyFilter() {{
    if (currentFilter === 'all') {{
        visibleRows = [...ROWS];
    }} else if (currentFilter === 'interested') {{
        visibleRows = ROWS.filter(r => r.interested);
    }} else if (currentFilter === 'scored') {{
        visibleRows = ROWS.filter(r => !r.rejected);
    }} else if (currentFilter === 'rejected') {{
        visibleRows = ROWS.filter(r => r.rejected);
    }}

    const scrolledCats = {{}};
    let ci = 0;
    for (const row of visibleRows) {{
        scrolledCats[row.cat] = (scrolledCats[row.cat] || 0) + 1;
        ci++;
    }}
    // Also recalc catRanges for visible
    catStartY = [];
    prevCat = null;

    resize();
    renderDetailList();
    updateMarkerCount();
}}

function updateMarkerCount() {{
    const cnt = ROWS.filter(r => r.interested).length;
    markerCount.textContent = cnt;
}}

// ── Search ──
searchBox.addEventListener('input', () => {{
    searchQuery = searchBox.value.trim();
    renderDetailList();
}});

// ── Init ──
container.addEventListener('scroll', () => {{
    // Redraw on scroll (canvas is virtual-scrolled — we draw the whole thing)
}});
window.addEventListener('resize', resize);
resize();
renderDetailList();
updateMarkerCount();
</script>
</body>
</html>"""


def main() -> None:
    interested = load_interested(INTERESTED)
    data = parse_summary(SUMMARY, interested)
    interested_count = sum(1 for p in data.scored if p.interested) + sum(1 for p in data.rejected if p.interested)

    print(f"Parsed: {len(data.scored)} scored + {len(data.rejected)} rejected = {len(data.scored) + len(data.rejected)} total")
    print(f"Categories: {list(data.categories)}")
    for cat, (start, end) in data.cat_ranges.items():
        print(f"  {cat}: rows {start}-{end} ({end - start})")
    print(f"Interested proteins: {interested_count}")

    html = build_html(data, interested_count)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Written: {OUTPUT} ({len(html):,} bytes)")
    print(f"Open: file://{OUTPUT}")


if __name__ == "__main__":
    main()
