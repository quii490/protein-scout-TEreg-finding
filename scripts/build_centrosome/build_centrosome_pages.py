#!/usr/bin/env python3
"""
Build HTML pages for the centrosome module from Markdown evaluation reports.

Outputs:
    docs/centrosome/index.html
    docs/centrosome/protein_index.html
    docs/centrosome/reports/GENE.html (for each gene)
"""
import json
import os
import re
from datetime import datetime


def md_to_html_simple(md_content):
    """Simple Markdown to HTML converter for evaluation reports."""
    lines = md_content.split('\n')
    html = []
    in_code = False
    in_table = False
    in_yaml = False
    yaml_start = 0

    for i, line in enumerate(lines):
        # Skip YAML frontmatter
        if i == 0 and line.strip() == '---':
            in_yaml = True
            continue
        if in_yaml:
            if line.strip() == '---':
                in_yaml = False
            continue

        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                html.append('</code></pre>')
                in_code = False
            else:
                html.append('<pre><code>')
                in_code = True
            continue
        if in_code:
            html.append(line)
            continue

        # Tables
        if line.startswith('|') and '---' not in line:
            if not in_table:
                html.append('<table>')
                in_table = True
                is_header = True
            if in_table:
                cells = [c.strip() for c in line.split('|')][1:-1]
                tag = 'th' if '---' in line or (line.startswith('|') and i < len(lines) and lines[i+1] if i+1 < len(lines) else '').startswith('|---') else 'td'
                html.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
            continue
        elif in_table and not line.startswith('|'):
            html.append('</table>')
            in_table = False

        # Handle separator line in table
        if '|---' in line:
            continue

        # Images
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', line)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2)
            html.append(f'<p><img src="{src}" alt="{alt}" style="max-width:100%;border-radius:4px;margin:8px 0;"></p>')
            continue

        # Skip empty lines
        if not line.strip():
            html.append('')
            continue

        # Headers
        if line.startswith('# '):
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('#### '):
            html.append(f'<h4>{line[5:]}</h4>')
        elif line.startswith('- '):
            html.append(f'<li>{_format_inline(line[2:])}</li>')
        elif line.startswith('**') and ':**' in line:
            # Bold key-value
            key_end = line.index('**', 2)
            key = line[2:key_end]
            val = line[key_end+2:].strip().lstrip(':').strip()
            html.append(f'<p><strong>{key}</strong>: {_format_inline(val)}</p>')
        elif re.match(r'^\d+\.\s', line):
            html.append(f'<p class="numbered">{_format_inline(line)}</p>')
        else:
            html.append(f'<p>{_format_inline(line)}</p>')

    if in_table:
        html.append('</table>')

    return '\n'.join(html)


def _format_inline(text):
    """Format inline Markdown to HTML."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def build_report_pages():
    """Build individual gene report HTML pages."""
    detail_dir = "centrosome/detail"
    os.makedirs("docs/centrosome/reports", exist_ok=True)

    count = 0
    for gene_dir in sorted(os.listdir(detail_dir)):
        md_path = os.path.join(detail_dir, gene_dir, f"{gene_dir}-centrosome-evaluation.md")
        if not os.path.exists(md_path):
            continue

        with open(md_path) as f:
            md_content = f.read()

        html_body = md_to_html_simple(md_content)

        html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{gene_dir} — Centrosome Module | Protein Scout</title>
<style>
:root {{
  --bg: #fafafa;
  --fg: #1a1a1a;
  --accent: #7c3aed;
  --accent-light: #ede9fe;
  --border: #e5e7eb;
  --muted: #6b7280;
  --card: #ffffff;
  --success: #059669;
  --warn: #d97706;
  --danger: #dc2626;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.7; }}
.topbar {{ background: var(--accent); color: #fff; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 10; }}
.topbar a {{ color: #fff; text-decoration: none; margin-left: 16px; opacity: 0.9; }}
.topbar a:hover {{ opacity: 1; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 24px; }}
h1 {{ font-size: 1.8rem; margin: 24px 0 16px; color: var(--accent); }}
h2 {{ font-size: 1.3rem; margin: 20px 0 12px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }}
h3 {{ font-size: 1.1rem; margin: 16px 0 8px; }}
h4 {{ font-size: 1rem; margin: 12px 0 6px; color: var(--muted); }}
p {{ margin: 8px 0; }}
li {{ margin: 4px 0 4px 20px; }}
strong {{ color: var(--accent); }}
code {{ background: var(--accent-light); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }}
table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
th {{ background: var(--accent); color: #fff; padding: 10px 12px; text-align: left; font-weight: 600; }}
td {{ padding: 10px 12px; border-bottom: 1px solid var(--border); }}
tr:nth-child(even) {{ background: var(--accent-light); }}
.badge {{ display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.8rem; font-weight: 600; }}
.badge-candidate {{ background: #d1fae5; color: #065f46; }}
.badge-eliminated {{ background: #e5e7eb; color: #6b7280; }}
.badge-low-priority {{ background: #fef3c7; color: #92400e; }}
.badge-manual-review {{ background: #fee2e2; color: #991b1b; }}
.back-link {{ margin: 24px 0; }}
.back-link a {{ color: var(--accent); text-decoration: none; }}
</style>
</head>
<body>
<div class="topbar">
    <strong>🧬 Centrosome Module — {gene_dir}</strong>
    <div>
        <a href="../index.html">Centrosome Home</a>
        <a href="../protein_index.html">All Proteins</a>
    </div>
</div>
<div class="container">
{html_body}
<div class="back-link">
    <a href="../protein_index.html">← Back to Centrosome Index</a>
</div>
</div>
</body>
</html>"""

        out_path = f"docs/centrosome/reports/{gene_dir}.html"
        with open(out_path, 'w') as f:
            f.write(html_page)
        count += 1

    print(f"  Built {count} report HTML pages")


def build_index_page():
    """Build the centrosome module home page."""
    with open("centrosome/data/centrosome_report_index.json") as f:
        index = json.load(f)

    records = index['records']
    candidates = [r for r in records if 'candidate' in r.get('status', '').lower() and 'low' not in r.get('status', '').lower() and 'eliminated' not in r.get('status', '').lower() and 'manual' not in r.get('status', '').lower()]
    eliminated = [r for r in records if 'eliminated' in r.get('status', '').lower()]
    low_priority = [r for r in records if 'low_priority' in r.get('status', '').lower()]
    manual_review = [r for r in records if 'manual_review' in r.get('status', '').lower()]

    # Top 10 by score
    top10 = sorted(records, key=lambda r: r.get('final_centrosome_score', 0), reverse=True)[:10]

    top_rows = '\n'.join(
        f'<tr><td><a href="reports/{r["gene"]}.html">{r["gene"]}</a></td>'
        f'<td><span class="badge badge-{"eliminated" if "eliminated" in r.get("status","").lower() else "candidate" if "candidate" in r.get("status","").lower() else "low-priority" if "low" in r.get("status","").lower() else "manual-review"}">{r["status"]}</span></td>'
        f'<td>{r.get("final_centrosome_score", "-")}</td></tr>'
        for r in top10
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Centrosome Module | Protein Scout</title>
<style>
:root {{
  --bg: #fafafa; --fg: #1a1a1a; --accent: #7c3aed;
  --accent-light: #ede9fe; --border: #e5e7eb; --muted: #6b7280; --card: #ffffff;
  --success: #059669; --warn: #d97706; --danger: #dc2626;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.7; }}
.topbar {{ background: var(--accent); color: #fff; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 10; }}
.topbar a {{ color: #fff; text-decoration: none; margin-left: 16px; opacity: 0.9; }}
.topbar a:hover {{ opacity: 1; }}
.container {{ max-width: 960px; margin: 0 auto; padding: 24px; }}
h1 {{ font-size: 2rem; margin: 24px 0 8px; }}
h2 {{ font-size: 1.3rem; margin: 32px 0 12px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }}
.note {{ background: var(--accent-light); border-left: 4px solid var(--accent); padding: 16px; margin: 24px 0; border-radius: 4px; }}
.note strong {{ color: var(--accent); }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 24px 0; }}
.stat-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; text-align: center; }}
.stat-card .num {{ font-size: 2rem; font-weight: 700; color: var(--accent); }}
.stat-card .label {{ font-size: 0.85rem; color: var(--muted); margin-top: 4px; }}
table {{ width: 100%; border-collapse: collapse; margin: 16px 0; background: var(--card); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }}
th {{ background: var(--accent); color: #fff; padding: 10px 14px; text-align: left; font-weight: 600; }}
td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); }}
tr:hover {{ background: var(--accent-light); }}
.badge {{ display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }}
.badge-candidate {{ background: #d1fae5; color: #065f46; }}
.badge-eliminated {{ background: #e5e7eb; color: #6b7280; }}
.badge-low-priority {{ background: #fef3c7; color: #92400e; }}
.badge-manual-review {{ background: #fee2e2; color: #991b1b; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<div class="topbar">
    <strong>🧬 Centrosome Module</strong>
    <div>
        <a href="protein_index.html">All Proteins</a>
    </div>
</div>
<div class="container">
    <h1>🧬 Centrosome Module</h1>
    <div class="note">
        <strong>Independent Extension</strong> — This centrosome module is a separate
        evaluation pipeline from the main protein-scout TEreg-finding atlas.
        Centrosome proteins are evaluated using centrosome-specific criteria.
        <strong>Not counted in main atlas statistics.</strong>
    </div>

    <h2>Pilot Statistics</h2>
    <div class="stats">
        <div class="stat-card">
            <div class="num">{len(records)}</div>
            <div class="label">Pilot Genes Evaluated</div>
        </div>
        <div class="stat-card">
            <div class="num">{len(candidates)}</div>
            <div class="label">CENTROSOME_CANDIDATE</div>
        </div>
        <div class="stat-card">
            <div class="num">{len(eliminated)}</div>
            <div class="label">ELIMINATED</div>
        </div>
        <div class="stat-card">
            <div class="num">{len(low_priority)}</div>
            <div class="label">LOW_PRIORITY</div>
        </div>
        <div class="stat-card">
            <div class="num">{len(manual_review)}</div>
            <div class="label">MANUAL_REVIEW</div>
        </div>
    </div>

    <h2>Top Ranked Proteins</h2>
    <table>
        <tr><th>Gene</th><th>Status</th><th>Score</th></tr>
        {top_rows}
    </table>

    <p style="margin-top:24px; color: var(--muted);">
        <a href="protein_index.html">→ View full centrosome protein index</a>
    </p>
    <p style="margin-top:8px; color: var(--muted);">
        Pilot built: {datetime.now().strftime('%Y-%m-%d')} ·
        HPA seed: {len(records)} genes evaluated
    </p>
</div>
</body>
</html>"""

    with open("docs/centrosome/index.html", 'w') as f:
        f.write(html)
    print("  Built docs/centrosome/index.html")


def build_protein_index():
    """Build the full centrosome protein table page."""
    with open("centrosome/data/centrosome_report_index.json") as f:
        index = json.load(f)

    records = sorted(index['records'], key=lambda r: r.get('final_centrosome_score', 0), reverse=True)

    rows = '\n'.join(
        f'<tr>'
        f'<td><a href="reports/{r["gene"]}.html">{r["gene"]}</a></td>'
        f'<td><span class="badge badge-{"eliminated" if "eliminated" in r.get("status","").lower() else "candidate" if "candidate" in r.get("status","").lower() else "low-priority" if "low" in r.get("status","").lower() else "manual-review"}">{r["status"]}</span></td>'
        f'<td>{r.get("final_centrosome_score", "-")}</td>'
        f'<td>{r.get("centrosome_evidence_score", "-")}</td>'
        f'<td>{r.get("te_relevance_score", "-")}</td>'
        f'<td>{r.get("pubmed_score", "-")}</td>'
        f'<td>{r.get("ppi_score", "-")}</td>'
        f'<td>{r.get("structure_domain_score", "-")}</td>'
        f'<td>{r.get("novelty_specificity_score", "-")}</td>'
        f'</tr>'
        for r in records
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Centrosome Protein Index | Protein Scout</title>
<style>
:root {{
  --bg: #fafafa; --fg: #1a1a1a; --accent: #7c3aed;
  --accent-light: #ede9fe; --border: #e5e7eb; --muted: #6b7280; --card: #ffffff;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.7; }}
.topbar {{ background: var(--accent); color: #fff; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 10; }}
.topbar a {{ color: #fff; text-decoration: none; margin-left: 16px; opacity: 0.9; }}
.topbar a:hover {{ opacity: 1; }}
.container {{ max-width: 1200px; margin: 0 auto; padding: 24px; }}
h1 {{ font-size: 1.5rem; margin: 16px 0; }}
.controls {{ display: flex; gap: 12px; margin: 16px 0; flex-wrap: wrap; }}
.controls input, .controls select {{ padding: 8px 12px; border: 1px solid var(--border); border-radius: 6px; font-size: 0.9rem; }}
.controls input {{ flex: 1; min-width: 200px; }}
table {{ width: 100%; border-collapse: collapse; margin: 16px 0; background: var(--card); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; font-size: 0.9rem; }}
th {{ background: var(--accent); color: #fff; padding: 8px 10px; text-align: left; font-weight: 600; cursor: pointer; white-space: nowrap; }}
th:hover {{ opacity: 0.9; }}
td {{ padding: 8px 10px; border-bottom: 1px solid var(--border); }}
tr:hover {{ background: var(--accent-light); }}
.badge {{ display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 0.7rem; font-weight: 600; }}
.badge-candidate {{ background: #d1fae5; color: #065f46; }}
.badge-eliminated {{ background: #e5e7eb; color: #6b7280; }}
.badge-low-priority {{ background: #fef3c7; color: #92400e; }}
.badge-manual-review {{ background: #fee2e2; color: #991b1b; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.count {{ color: var(--muted); font-size: 0.9rem; }}
</style>
</head>
<body>
<div class="topbar">
    <strong>🧬 Centrosome Module — Protein Index</strong>
    <div>
        <a href="index.html">Home</a>
    </div>
</div>
<div class="container">
    <h1>Centrosome Protein Index <span class="count">({len(records)} proteins)</span></h1>
    <div class="controls">
        <input type="text" id="search" placeholder="Search gene..." oninput="filterTable()">
        <select id="statusFilter" onchange="filterTable()">
            <option value="">All Statuses</option>
            <option value="CANDIDATE">CENTROSOME_CANDIDATE</option>
            <option value="LOW_PRIORITY">LOW_PRIORITY</option>
            <option value="MANUAL_REVIEW">MANUAL_REVIEW</option>
        </select>
    </div>
    <table id="proteinTable">
        <thead>
            <tr>
                <th onclick="sortTable(0)">Gene</th>
                <th onclick="sortTable(1)">Status</th>
                <th onclick="sortTable(2)">Score</th>
                <th onclick="sortTable(3)">Centrosome</th>
                <th onclick="sortTable(4)">TE</th>
                <th onclick="sortTable(5)">PubMed</th>
                <th onclick="sortTable(6)">PPI</th>
                <th onclick="sortTable(7)">Structure</th>
                <th onclick="sortTable(8)">Novelty</th>
            </tr>
        </thead>
        <tbody>
{rows}
        </tbody>
    </table>
</div>
<script>
function filterTable() {{
    const search = document.getElementById('search').value.toLowerCase();
    const status = document.getElementById('statusFilter').value;
    const rows = document.querySelectorAll('#proteinTable tbody tr');
    rows.forEach(row => {{
        const gene = row.cells[0].textContent.toLowerCase();
        const st = row.cells[1].textContent;
        const matchSearch = gene.includes(search);
        const matchStatus = !status || st.includes(status);
        row.style.display = (matchSearch && matchStatus) ? '' : 'none';
    }});
}}

function sortTable(col) {{
    const tbody = document.querySelector('#proteinTable tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const sorted = rows.sort((a, b) => {{
        let va = a.cells[col].textContent.trim();
        let vb = b.cells[col].textContent.trim();
        let na = parseFloat(va), nb = parseFloat(vb);
        if (!isNaN(na) && !isNaN(nb)) return nb - na;
        return va.localeCompare(vb);
    }});
    sorted.forEach(r => tbody.appendChild(r));
}}
</script>
</body>
</html>"""

    with open("docs/centrosome/protein_index.html", 'w') as f:
        f.write(html)
    print("  Built docs/centrosome/protein_index.html")


def main():
    print("Building centrosome HTML pages...")
    build_report_pages()
    build_index_page()
    build_protein_index()
    print("Done.")


if __name__ == "__main__":
    main()
