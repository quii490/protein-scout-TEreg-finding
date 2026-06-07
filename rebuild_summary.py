#!/usr/bin/env python3
"""Rebuild protein-finding.md from detail/ reports. NEVER modifies detail reports. Only overwrites summary table."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
SUMMARY = os.path.join(BASE, "protein-finding.md")

def fmt_score(value):
    return ("%.2f" % value).rstrip("0").rstrip(".")

def split_md_row(line):
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        return []
    return [c.strip().replace("**", "") for c in line.strip("|").split("|")]

def extract_180_scores(content):
    """Parse alternate /180 tables and convert dimensions back to 0-10 scale.

    The public summary table uses the legacy dimensions:
    (核x4 + 大x1 + 新x5 + 结x3 + 域x2 + PPIx3 + 互证) / 1.83.
    Some repaired reports contain a different table with columns
    Dimension | Max | Score. In that format Score is weighted/raw within a
    custom max. Convert Score/Max to 0-10 before rebuilding the summary.
    """
    if "Dimension" not in content or "Max" not in content or "Score" not in content:
        return {}
    aliases = {
        "核定位": ["nuclear localization", "核定位"],
        "蛋白大小": ["protein size", "蛋白大小"],
        "新颖性": ["research novelty", "新颖"],
        "三维结构": ["3d structure", "三维", "structure"],
        "调控结构域": ["regulatory domains", "调控结构域", "domain"],
        "PPI": ["ppi network", "ppi"],
    }
    out = {}
    for line in content.splitlines():
        cells = split_md_row(line)
        if len(cells) < 3:
            continue
        label = re.sub(r"^\d+\.\s*", "", cells[0]).strip().lower()
        if not label or re.fullmatch(r":?-+:?", label.replace(" ", "")):
            continue
        try:
            max_score = float(re.search(r"[\d.]+", cells[1]).group(0))
            raw_score = float(re.search(r"[\d.]+", cells[2]).group(0))
        except Exception:
            continue
        if max_score <= 0:
            continue
        for dim, names in aliases.items():
            if any(name in label for name in names):
                val = raw_score / max_score * 10 if max_score > 10 else raw_score
                if 0 <= val <= 10:
                    out[dim] = fmt_score(val)
                break
    return out

def extract_score(content, dim):
    """Extract dimension score from a report. Handles both '8/10' and '8' formats.
    Supports both Chinese and English scoring table headers."""
    alt_180 = extract_180_scores(content)
    if dim in alt_180:
        return alt_180[dim]

    scoring_start = content.find('评分总览')
    if scoring_start < 0:
        scoring_start = content.find('Scoring Overview')
    if scoring_start < 0:
        scoring_start = 0
    scoring_section = content[scoring_start:]

    # Bilingual dimension name mapping
    dim_aliases = [dim]
    en_map = {
        '核定位': 'Nuclear Localization', '蛋白大小': 'Protein Size',
        '新颖性': 'Research Novelty', '三维结构': '3D Structure',
        '调控结构域': 'Regulatory Domains', 'PPI': 'PPI Network',
    }
    if dim in en_map:
        dim_aliases.append(en_map[dim])

    for alias in dim_aliases:
        patterns = [
            rf'{alias}[^|]*\|\s*(\d+)\s*/\s*10',
            rf'{alias}[^|]*\|\s*(\d+)\s*\|\s*10',
            rf'{alias}[^|]*\|\s*(\d+)/10',
        ]
        for p in patterns:
            m = re.search(p, scoring_section)
            if m: return m.group(1)

        idx = scoring_section.find(alias)
        if idx > 0:
            chunk = scoring_section[idx:idx+150]
            nums = re.findall(r'\b(\d+)\b', chunk.split('\n')[0])
            for n in nums:
                val = int(n)
                if 0 <= val <= 10: return n
    return '?'

def extract_norm(content):
    """Extract normalized score (Chinese or English reports)."""
    alt_180 = extract_180_scores(content)
    if alt_180:
        required = ["核定位", "蛋白大小", "新颖性", "三维结构", "调控结构域", "PPI"]
        if all(k in alt_180 for k in required):
            nuc = float(alt_180["核定位"])
            size = float(alt_180["蛋白大小"])
            nov = float(alt_180["新颖性"])
            struct = float(alt_180["三维结构"])
            dom = float(alt_180["调控结构域"])
            ppi = float(alt_180["PPI"])
            cross_m = re.search(r'互证加分.*?max\s*\+\s*3\s*\|\s*\+?([\d.]+)', content)
            cross = float(cross_m.group(1)) if cross_m else 0.0
            return round((nuc * 4 + size + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross) / 1.83, 1)

    # Try Chinese patterns
    for pat in [r'归一化总分.*?\*\*([\d.]+)\*\*', r'归一化总分.*?([\d.]+)\s*/\s*100']:
        m = re.search(pat, content)
        if m:
            v = float(m.group(1))
            if v > 1: return v
    # Try English patterns
    for pat in [r'Normalized.*?\*\*([\d.]+)\*\*', r'Normalized.*?([\d.]+)\s*/\s*100']:
        m = re.search(pat, content)
        if m:
            v = float(m.group(1))
            if v > 1: return v
    # Try last bold number in scoring section
    scoring_start = content.find('评分总览')
    if scoring_start < 0: scoring_start = content.find('Scoring Overview')
    if scoring_start < 0: scoring_start = 0
    section = content[scoring_start:scoring_start+2000]
    bold_nums = re.findall(r'\*\*([\d.]+)\*\*', section)
    for n in reversed(bold_nums):
        v = float(n)
        if 10 < v < 100: return v

    # Last fallback for older scored reports that list the six dimension
    # scores but omit an explicit normalized total.
    required = ['核定位', '蛋白大小', '新颖性', '三维结构', '调控结构域', 'PPI']
    dim_scores = [extract_score(content, dim) for dim in required]
    if all(score != '?' for score in dim_scores):
        nuc, size, nov, struct, dom, ppi = [float(score) for score in dim_scores]
        cross = float(extract_cross(content).lstrip('+') or 0)
        return round((nuc * 4 + size + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross) / 1.83, 1)
    return None

def extract_cross(content):
    # Skip past "max +3" in the table to get the actual cross score
    m = re.search(r'互证加分.*?max\s*\+\s*3\s*\|\s*\+?([\d.]+)', content)
    if m: return f"+{m.group(1)}"
    # Fallback: find any +number after 互证加分
    m = re.search(r'互证加分.*?\+([\d.]+)', content)
    if m: return f"+{m.group(1)}"
    return "0"

def rebuild():
    rows_by_cat = {}
    not_found = []

    for root, dirs, files in os.walk(DETAIL):
        for f in files:
            if not f.endswith("-evaluation.md"): continue
            path = os.path.join(root, f)
            gene = os.path.basename(os.path.dirname(path))
            cat = os.path.basename(os.path.dirname(os.path.dirname(path)))
            if cat == "rejected" or not cat or cat == "detail": continue

            with open(path) as fh: c = fh.read()

            nuc = extract_score(c, '核定位')
            size = extract_score(c, '蛋白大小')
            nov = extract_score(c, '新颖性')
            struct = extract_score(c, '三维结构')
            dom = extract_score(c, '调控结构域')
            ppi = extract_score(c, 'PPI')
            cross = extract_cross(c)
            norm = extract_norm(c)

            if not norm or nuc == '?':
                not_found.append(f"{cat}/{gene}")
                continue

            rows_by_cat.setdefault(cat, []).append((norm, gene, nuc, size, nov, struct, dom, ppi, cross))

    if not_found:
        print(f"WARNING: {len(not_found)} reports have unparseable scores:")
        for nf in not_found: print(f"  {nf}")

    # Read existing summary to preserve frontmatter + eliminated section
    with open(SUMMARY) as fh: pf = fh.read()

    # Find eliminated section
    elim_idx = pf.find("\n## 已淘汰")
    if elim_idx < 0: elim_idx = pf.find("\n### 已淘汰")

    top = pf[:elim_idx].rstrip() if elim_idx > 0 else pf
    bottom = pf[elim_idx:] if elim_idx > 0 else ""

    # Remove old scored tables from top
    for cat_name in ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm", "nucleoplasm", "nuclear-envelope", "nuclear-body"]:
        idx = top.find(f"\n## {cat_name}\n")
        if idx > 0: top = top[:idx]

    # Previous rebuilds could accumulate many blockquote-only blank lines near
    # the statistics header. Keep the summary introduction deterministic.
    cleaned_top_lines = []
    for line in top.splitlines():
        if line.strip() == ">":
            continue
        cleaned_top_lines.append(line.rstrip())
    top = "\n".join(cleaned_top_lines).rstrip()

    # Build new scored tables
    header = "| # | 基因 | 核 | 大 | 新 | 结 | 域 | PPI | 互证 | 总分 | 推荐 | 详情 |"
    sep    = "|---|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|------|"

    result = top.rstrip() + "\n\n"
    all_cats = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm", "nucleoplasm", "nuclear-envelope", "nuclear-body"]

    def stars(norm_score):
        if norm_score >= 85: return "⭐⭐⭐⭐⭐"
        elif norm_score >= 75: return "⭐⭐⭐⭐"
        elif norm_score >= 65: return "⭐⭐⭐"
        elif norm_score >= 55: return "⭐⭐"
        else: return "⭐"

    for cat in all_cats:
        rows = sorted(rows_by_cat.get(cat, []), key=lambda x: x[0], reverse=True)
        if not rows: continue
        result += f"## {cat}\n{header}\n{sep}\n"
        for rank, (norm, gene, nuc, size, nov, struct, dom, ppi, cross) in enumerate(rows, 1):
            link = f"[[Projects/TEreg-finding/protein-interested/detail/{cat}/{gene}/{gene}-evaluation\\|→]]"
            s = stars(norm)
            result += f"| {rank} | {gene} | {nuc} | {size} | {nov} | {struct} | {dom} | {ppi} | {cross} | {norm} | {s} | {link} |\n"
        result += "\n"

    # Also rebuild eliminated table from detail/rejected/
    # Pre-load UniProt subcellular location data for nuc_reason (once, outside loop)
    _sheet_data_cache = {}
    try:
        import pandas as pd
        sheet_path = '/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/Final_TE_finding.xlsx'
        df = pd.read_excel(sheet_path, sheet_name='Sheet1')
        _sheet_data_cache = {str(r['human_symbol']): str(r['human_uniprot_subcellular_location']) if pd.notna(r['human_uniprot_subcellular_location']) else '' for _, r in df.iterrows()}
    except:
        pass

    def get_nuc_reason(gene_symbol, report_content):
        loc = _sheet_data_cache.get(gene_symbol, '').lower()
        if 'mitochondr' in loc: reason = '线粒体蛋白'
        elif 'peroxisom' in loc: reason = '过氧化物酶体蛋白'
        elif 'golgi' in loc: reason = '高尔基体蛋白'
        elif 'endoplasmic' in loc or 'sarcoplasmic' in loc: reason = '内质网蛋白'
        elif 'lysosom' in loc: reason = '溶酶体蛋白'
        elif 'secreted' in loc: reason = '分泌蛋白'
        elif 'cytoskeleton' in loc or 'actin' in loc: reason = '细胞骨架蛋白'
        elif 'centrosom' in loc or 'centriol' in loc: reason = '中心体蛋白'
        elif 'plasma membrane' in loc: reason = '质膜蛋白'
        elif 'cell junction' in loc or 'adherens' in loc: reason = '细胞连接蛋白'
        elif 'stress granule' in loc or 'p-body' in loc: reason = '应激颗粒蛋白'
        elif 'cytosol' in loc or 'cytoplasm' in loc: reason = '胞质蛋白'
        elif 'membrane' in loc: reason = '膜蛋白'
        elif 'nucleus' in loc or 'nucleoplasm' in loc or 'nucleolar' in loc or 'chromosome' in loc or 'chromatin' in loc:
            reason = '需人工复核'
        else: reason = '非核蛋白'
        return f"核定位 ≤3（{reason}）"

    nuc_rejects, pub_rejects = [], []
    for root2, dirs2, files2 in os.walk(os.path.join(DETAIL, "rejected")):
        for f2 in files2:
            if not f2.endswith("-evaluation.md"): continue
            path2 = os.path.join(root2, f2)
            gene2 = os.path.basename(os.path.dirname(path2))
            with open(path2) as fh2: c2 = fh2.read()
            pub_m = re.search(r'PubMed.*?总数[^|]*\|\s*(\d+)', c2)
            if not pub_m: pub_m = re.search(r'PubMed.*?(\d{2,5})[^0-9]', c2)
            pub2 = pub_m.group(1) if pub_m else "—"
            # Extract nuclear score for classification (multiple formats)
            nuc_match = re.search(r'核定位[特分].*?\|\s*(\d+)', c2)
            if not nuc_match: nuc_match = re.search(r'核定位.*?得分.*?(\d+)', c2)
            if not nuc_match: nuc_match = re.search(r'核定位[特分].*?:\s*(\d+)\s*/\s*10', c2)
            if not nuc_match: nuc_match = re.search(r'核定位[^:\n]*?[评得]+\s*[：:]*\s*(\d+)', c2)
            nuc_score = int(nuc_match.group(1)) if nuc_match else None
            # Classify: explicit rejection text first, then score-based fallback
            # Classify: explicit rejection text first, then score-based fallback
            if re.search(r'PubMed.*超过|淘汰类型.*PubMed|PubMed\s*>\s*100|PubMed.*阈值', c2):
                pub_rejects.append((gene2, pub2))
            elif nuc_score is not None and nuc_score <= 3:
                nuc_rejects.append((gene2, get_nuc_reason(gene2, c2), pub2))
            elif pub2 != "—" and int(pub2) > 100:
                pub_rejects.append((gene2, pub2))
            else:
                nuc_rejects.append((gene2, get_nuc_reason(gene2, c2), pub2))
    nuc_rejects.sort(key=lambda x: x[0])
    pub_rejects.sort(key=lambda x: int(x[1]) if x[1].isdigit() else 0, reverse=True)

    elim_table = "## 已淘汰\n\n| # | 基因 | 原因 | PubMed | 详情 |\n|---|------|------|:------:|------|\n"
    idx = 1
    for item in nuc_rejects:
        g, reason, p = item
        elim_table += f"| {idx} | {g} | {reason} | {p} | [[Projects/TEreg-finding/protein-interested/detail/rejected/{g}/{g}-evaluation\\|→]] |\n"; idx += 1
    for g, p in pub_rejects:
        elim_table += f"| {idx} | {g} | PubMed >100 | {p} | [[Projects/TEreg-finding/protein-interested/detail/rejected/{g}/{g}-evaluation\\|→]] |\n"; idx += 1

    scored_count = sum(len(v) for v in rows_by_cat.values())
    result += f"\n\n{elim_table}"

    # Update stats
    result = re.sub(r'^\s*>?\s*\*\*评估统计\*\*:.*\n', '', result, flags=re.M)
    stats = f'> **评估统计**: {scored_count} 个蛋白通过评分（{len(rows_by_cat)} 个定位分类），{idx-1} 个淘汰（{len(nuc_rejects)} 个核定位 ≤3 + {len(pub_rejects)} 个 PubMed >100）\n'
    hdr_end = result.find('\n## chromatin')
    if hdr_end < 0: hdr_end = result.find('\n## nucleoplasm')
    result = result[:hdr_end].rstrip() + '\n\n' + stats + '\n' + result[hdr_end:].lstrip()

    with open(SUMMARY, 'w') as fh: fh.write(result)

    counts = {k: len(v) for k, v in rows_by_cat.items()}
    print(f"Rebuilt: {scored_count} scored + {idx-1} eliminated = {scored_count+idx-1} total ({len(rows_by_cat)} cats: {counts})")
    return not_found

if __name__ == "__main__":
    rebuild()
