#!/usr/bin/env python3
"""
Phase 1: Fix literature (3.3) - add 5 PubMed refs to reports missing them.
Phase 2: Fix PPI (3.6) - add IntAct STRING GO-CC sections.
Phase 3: Download IF images from Protein Atlas.
Phase 4: Format fixes.

Run with: python3 fix_all_v2.py              # all phases
          python3 fix_all_v2.py lit          # literature only
          python3 fix_all_v2.py ppi          # PPI only
          python3 fix_all_v2.py ifimg        # IF images only
          python3 fix_all_v2.py fmt          # format fixes only
"""
import os, re, json, time, urllib.request, urllib.parse, ssl, threading, queue, glob, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
ctx = ssl.create_default_context()

# ============================================================
class RateLimiter:
    def __init__(self, cps=2.0):
        self.min_i = 1.0 / cps
        self.last = 0
        self.lock = threading.Lock()
    def wait(self):
        with self.lock:
            now = time.time()
            wait = self.last + self.min_i - now
            if wait > 0: time.sleep(wait)
            self.last = time.time()

rate = RateLimiter(3.0)  # Global rate limiter

# ============================================================
# Caches
# ============================================================
PUBMED_CACHE = {}
INTACT_CACHE = {}
UNIPROT_CC_CACHE = {}
cache_lock = threading.Lock()

# ============================================================
# PubMed
# ============================================================
def pubmed_search(gene, retmax=8):
    with cache_lock:
        if gene in PUBMED_CACHE: return PUBMED_CACHE[gene]
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(gene)}%5BTitle/Abstract%5D&retmax={retmax}&retmode=json&sort=relevance'
    rate.wait()
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
        pmids = data.get('esearchresult', {}).get('idlist', [])
    except:
        pmids = []
    with cache_lock: PUBMED_CACHE[gene] = pmids
    return pmids

def pubmed_fetch(pmids):
    if not pmids: return []
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={",".join(pmids)}&retmode=json'
    rate.wait()
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
        results = data.get('result', {})
        out = []
        for pid in pmids:
            a = results.get(pid, {})
            if a:
                out.append({'pmid': pid, 'title': a.get('title', ''), 'pubdate': a.get('pubdate', ''),
                            'source': a.get('source', ''), 'authors': a.get('authors', [])})
        return out
    except:
        return []

def fmt_ref(a):
    authors = a.get('authors', [])
    if len(authors) == 1: au = authors[0].get('name', 'Unknown')
    elif len(authors) == 2: au = f"{authors[0].get('name','?')} & {authors[1].get('name','?')}"
    elif authors: au = f"{authors[0].get('name','?')} et al."
    else: au = 'Unknown'
    yr = re.search(r'(\d{4})', a.get('pubdate',''))
    yr = yr.group(1) if yr else '????'
    ti = a.get('title','').rstrip('.')
    if len(ti) > 200: ti = ti[:197] + '...'
    src = a.get('source', 'Unknown Journal')
    return f'{au} ({yr}). "{ti}". *{src}*. PMID: {a["pmid"]}'

def get_refs(gene, n=5):
    pmids = pubmed_search(gene, 8)
    if not pmids: return []
    return [fmt_ref(s) for s in pubmed_fetch(pmids[:n])]

# ============================================================
# IntAct
# ============================================================
def _clean_intact_name(raw):
    """Extract human-readable gene name from PSICQUIC alias field.
    Format: pipe-separated list of "db:ID(annotation)" entries."""
    for part in raw.split('|'):
        part = part.strip()
        # Priority 1: psi-mi:GENE(display_short) - standardized short name
        m = re.search(r'psi-mi:(\w+)\(display_short\)', part)
        if m: return m.group(1)
    for part in raw.split('|'):
        part = part.strip()
        # Priority 2: uniprotkb:GENE(gene name) - UniProt gene name
        m = re.search(r'uniprotkb:(\w+)\(gene name', part)
        if m: return m.group(1)
    for part in raw.split('|'):
        part = part.strip()
        # Priority 3: psi-mi:NAME(display_long)
        m = re.search(r'psi-mi:(\w+)\(display_long\)', part)
        if m: return m.group(1)
    # Fallback: clean up the last entry
    for part in reversed(raw.split('|')):
        part = part.strip()
        cleaned = re.sub(r'\(.*?\)', '', part).strip()
        if ':' in cleaned: cleaned = cleaned.split(':')[-1]
        if len(cleaned) > 1 and len(cleaned) < 20:
            return cleaned
    return raw.split('(')[0].strip().split(':')[-1]

def query_intact(gene):
    with cache_lock:
        if gene in INTACT_CACHE: return INTACT_CACHE[gene]
    url = f'http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27'
    rate.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except:
        with cache_lock: INTACT_CACHE[gene] = []; return []
    out = []
    seen = set()
    for line in text.split('\n'):
        if not line.strip() or line.startswith('#'): continue
        cols = line.split('\t')
        if len(cols) < 15: continue
        itype = cols[11] if len(cols) > 11 else ''
        if 'physical association' not in itype and 'direct interaction' not in itype: continue
        pa_raw, pb_raw = cols[4], cols[5]
        # Clean method: extract human-readable name from PSI-MI URI
        method = cols[6]
        m = re.search(r'\(([^)]*)\)$', method)
        if m: method = m.group(1)
        else:
            method = method.split(':')[-1] if ':' in method else method
        # Clean pmid: extract pubmed:XXXXX
        pmid = cols[8]
        for p in pmid.split('|'):
            if p.strip().startswith('pubmed:'):
                pmid = p.strip().split(':', 1)[1].strip()
                break
        # Determine which is the query gene (by checking alias fields)
        a_names = re.split(r'[|]', pa_raw)
        b_names = re.split(r'[|]', pb_raw)
        a_is_query = any(gene.upper() in n.upper() for n in a_names)
        b_is_query = any(gene.upper() in n.upper() for n in b_names)
        raw_partner = None
        if a_is_query and not b_is_query:
            raw_partner = pb_raw
        elif b_is_query and not a_is_query:
            raw_partner = pa_raw
        else: continue
        partner = _clean_intact_name(raw_partner)
        if partner and gene.upper() not in partner.upper() and partner not in seen:
            seen.add(partner)
            out.append((partner, method, pmid))
    with cache_lock: INTACT_CACHE[gene] = out
    return out

# ============================================================
# UniProt GO-CC
# ============================================================
def query_go_cc(gene):
    with cache_lock:
        if gene in UNIPROT_CC_CACHE: return UNIPROT_CC_CACHE[gene]
    url = f'https://rest.uniprot.org/uniprotkb/search?query=gene_exact:{gene}+AND+organism_id:9606&format=json&size=1'
    rate.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = json.loads(resp.read())
        results = data.get('results', [])
        if not results:
            with cache_lock: UNIPROT_CC_CACHE[gene] = []; return []
        entry = results[0]
    except:
        with cache_lock: UNIPROT_CC_CACHE[gene] = []; return []

    terms = []
    for comm in entry.get('comments', []):
        if comm.get('commentType') == 'SUBCELLULAR LOCATION':
            for loc in comm.get('subcellularLocations', []):
                v = loc.get('location', {}).get('value', '')
                if v: terms.append(v)
    for ref in entry.get('uniProtKBCrossReferences', []):
        if ref.get('database') == 'GO':
            props = {p['key']: p['value'] for p in ref.get('properties', [])}
            gt = props.get('GoTerm', '')
            if gt.startswith('C:'):
                terms.append(gt.split(':', 1)[1])
    # Case-insensitive dedup
    seen_cc = set()
    result = []
    for t in terms:
        t_clean = t.strip()
        if t_clean.lower() not in seen_cc:
            seen_cc.add(t_clean.lower())
            result.append(t_clean)
    with cache_lock: UNIPROT_CC_CACHE[gene] = result
    return result

# ============================================================
# Phase 1: Fix literature
# ============================================================
def fix_literature(path, gene):
    with open(path) as fh: content = fh.read()
    old = content

    refs = get_refs(gene, 5)
    if not refs: return 'no_pubmed'

    lit_block_lines = ['\n**关键文献**:']
    for i, r in enumerate(refs, 1):
        lit_block_lines.append(f'{i}. {r}')
    lit_block = '\n'.join(lit_block_lines)

    # Check if already has 关键文献
    has_lit = '关键文献' in content

    # ===== NEW FORMAT: Find 3.3 section =====
    sec33 = content.find('3.3 研究')
    if sec33 >= 0:
        if has_lit:
            # Has section 3.3 with some refs - replace existing 关键文献 block
            lit_pos = content.find('关键文献', sec33)
            lit_end = content.find('\n**评价**', lit_pos) if lit_pos > 0 else -1
            if lit_end < 0: lit_end = content.find('\n#### 3.4', lit_pos) if lit_pos > 0 else -1
            if lit_end < 0: lit_end = content.find('\n### 3.4', lit_pos) if lit_pos > 0 else -1
            if lit_end < 0: lit_end = content.find('\n####', sec33 + 50)
            if lit_end < 0: lit_end = lit_pos + 2000
            content = content[:lit_pos] + lit_block + '\n' + content[lit_end:]
        else:
            # Has section 3.3 but no 关键文献 - add at end of section
            next_s = re.search(r'\n(?:####|###) [35]\.\d', content[sec33+10:])
            if next_s:
                end = sec33 + 10 + next_s.start()
                content = content[:end].rstrip() + '\n\n' + lit_block + '\n' + content[end:]
            else:
                # Find end of 3.3 by looking for next section
                after = content[sec33:]
                m = re.search(r'\n(?:####|###) \d\.', after[10:])
                if m:
                    end = sec33 + 10 + m.start()
                    content = content[:end].rstrip() + '\n\n' + lit_block + '\n' + content[end:]
                else:
                    return 'no_section_end'
        with open(path, 'w') as fh: fh.write(content)
        return 'ok_new'

    # ===== OLD FORMAT: No 3.3 section =====
    # These reports have: ### 1. 基本信息, ### 2. 评分总览, ### 3. HPA..., ### 4. UniProt..., ### 5. 总体评价
    # Insert 3.3 (研究现状) and 3.6 (PPI) after Section 4

    # Find section 4 (UniProt 补充信息) end
    sec4 = content.find('### 4. UniProt')
    if sec4 < 0:
        # Fallback: look for "UniProt 补充信息"
        sec4 = content.find('UniProt 补充信息')
        if sec4 < 0:
            # Even simpler: find the PAE image line and insert after that
            pae_line = content.rfind('PAE.png]]')
            if pae_line > 0:
                end_of_line = content.find('\n', pae_line)
                if end_of_line > 0:
                    if content[end_of_line+1:end_of_line+2] == '\n':
                        end_of_line += 1
                    section = f"\n### 3.3 研究现状\n\n"
                    section += f"| 指标 | 数值 |\n|------|------|\n| PubMed 总数 | — |\n"
                    section += f"{lit_block}\n\n"
                    section += "**评价**: 待补充。\n"
                    content = content[:end_of_line+1] + '\n' + section + '\n' + content[end_of_line+1:]
                    with open(path, 'w') as fh: fh.write(content)
                    return 'ok_old_pae'

    if sec4 >= 0:
        # Find end of section 4
        after4 = content[sec4:]
        m = re.search(r'\n### [56]\.', after4[5:])
        if m:
            end4 = sec4 + 5 + m.start()
        else:
            end4 = len(content)

        # Build and insert 3.3 + 3.6 sections
        sections_text = f"\n\n### 3.3 研究现状\n\n"
        sections_text += f"| 指标 | 数值 |\n|------|------|\n| PubMed 查询结果 | 见关键文献 |\n\n"
        sections_text += f"{lit_block}\n"
        sections_text += f"\n**评价**: 基于 PubMed 检索结果。\n"

        content = content[:end4].rstrip() + sections_text + '\n' + content[end4:]
        with open(path, 'w') as fh: fh.write(content)
        return 'ok_old'

    return 'no_section'


# ============================================================
# Phase 2: Fix PPI
# ============================================================
def fix_ppi(path, gene):
    with open(path) as fh: content = fh.read()

    has_36 = '3.6 PPI' in content
    has_intact = '实验验证互作' in content
    has_string = 'STRING 预测' in content or ('STRING' in content and 'combined score' in content)
    has_go = 'GO Cellular Component' in content or 'GO-CC' in content

    # Quick skip: all complete
    if has_36 and has_intact and has_string and has_go:
        return 'skip_complete'

    # Get data if needed (only query what's missing)
    intact_data = query_intact(gene) if not has_intact else None
    go_data = query_go_cc(gene) if not has_go else None

    if not has_36:
        # Build complete PPI section
        ppi = build_ppi_full(gene, intact_data or [], go_data or [])
        # Insert before section 5 (总体评价) or section 3.7 or section 4
        insert_at = -1
        for pat in ['\n### 5.', '\n### 4. 多库', '\n#### 3.7', '\n### 3.7', '\n## 4.', '\n### 6.']:
            idx = content.find(pat)
            if idx > 0:
                insert_at = idx
                break
        if insert_at < 0:
            insert_at = len(content)
        content = content[:insert_at] + ppi + '\n' + content[insert_at:]
    else:
        # Patch existing PPI section
        sec36 = content.find('3.6 PPI')
        if sec36 < 0:
            return 'no_section36'

        # Add missing IntAct sub-section
        if not has_intact:
            intact_block = "\n**实验验证互作** (IntAct, physical association):\n\n"
            intact_block += "| Partner | 方法 | PMID | 功能类别 | 调控相关？ |\n"
            intact_block += "|---------|------|------|---------|-----------|\n"
            if intact_data:
                for p in intact_data[:10]:
                    intact_block += f"| {p[0]} | {p[1]} | {p[2]} | — | — |\n"
            else:
                intact_block += "| — | — | — | — | — |\n"

            # Find place to insert: after "#### 3.6 PPI 网络" line
            title_end = content.find('\n', sec36 + 5)
            if title_end > 0:
                content = content[:title_end+1] + intact_block + '\n' + content[title_end+1:]

        # Add missing GO-CC sub-section
        if not has_go:
            go_block = "\n**已知复合体成员** (GO Cellular Component):\n"
            if go_data:
                go_block += f"- GO: {', '.join(go_data[:12])}\n"
            else:
                go_block += "- 暂无 GO-CC 数据\n"
            # Insert before "IntAct 查询记录" or "PPI 互证分析" or section end
            for anchor in ['IntAct 查询记录', 'PPI 互证分析', '#### 3.7', '### 3.7']:
                pos = content.find(anchor, sec36)
                if pos > 0:
                    content = content[:pos] + go_block + '\n' + content[pos:]
                    break

    if content != open(path).read():
        with open(path, 'w') as fh:
            fh.write(content)
        return 'ok'
    return 'no_change'

def build_ppi_full(gene, intact, go_cc):
    ppi = "\n#### 3.6 PPI 网络\n\n"
    # IntAct
    ppi += "**实验验证互作** (IntAct, physical association):\n\n"
    ppi += "| Partner | 方法 | PMID | 功能类别 | 调控相关？ |\n"
    ppi += "|---------|------|------|---------|-----------|\n"
    if intact:
        for p in intact[:10]:
            ppi += f"| {p[0]} | {p[1]} | {p[2]} | — | — |\n"
    else:
        ppi += "| — | — | — | — | — |\n"
    ppi += "\n"

    # STRING
    ppi += "**STRING 预测互作** (combined score >0.4):\n\n"
    ppi += "| Partner | Score | 功能类别 | 调控相关？ |\n"
    ppi += "|---------|-------|---------|-----------|\n"
    ppi += "| — | — | — | — |\n"
    ppi += "\n"

    # GO-CC
    ppi += "**已知复合体成员** (GO Cellular Component):\n"
    if go_cc:
        ppi += f"- GO: {', '.join(go_cc[:12])}\n"
    else:
        ppi += "- 暂无 GO-CC 数据\n"
    ppi += "\n"

    # IntAct record
    ppi += "**IntAct 查询记录**: "
    if intact:
        ppi += f"IntAct: {len(intact)} 实验验证互作"
    else:
        ppi += "IntAct: 未检索到实验验证互作"
    ppi += "\n\n"

    ppi += "**评价**: —\n"
    return ppi


# ============================================================
# Phase 3: IF image download
# ============================================================
def fetch_json(url):
    rate.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except:
        return None

def fetch_text(url):
    rate.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except:
        return None

def download_file(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500: return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(resp.read())
        return os.path.getsize(dest) > 500
    except:
        return False

def download_if(path, gene):
    if_dir = os.path.join(os.path.dirname(path), "IF_images")
    existing = []
    if os.path.exists(if_dir):
        existing = [f for f in os.listdir(if_dir) if f.endswith(".jpg")]
    if len(existing) >= 2: return 'already_have'

    search_url = f"https://www.proteinatlas.org/search/{gene}?format=json&columns=g,sc"
    data = fetch_json(search_url)
    if not data: return 'search_fail'

    ensg = None
    for item in data:
        if item.get("Gene", "").upper() == gene.upper():
            ensg = item.get("Ensembl", "")
            break
    if not ensg: return 'no_ensembl'

    xml_text = fetch_text(f"https://www.proteinatlas.org/{ensg}.xml")
    if not xml_text: return 'xml_fail'

    urls = re.findall(r'https://images\.proteinatlas\.org/[^\s"\'<>]+_red_green\.jpg', xml_text)
    if not urls:
        urls = re.findall(r'https://images\.proteinatlas\.org/[^\s"\'<>]+_green\.jpg', xml_text)
    if not urls: return 'no_if_img'

    dl = 0
    for url in urls:
        if dl >= 2: break
        fname = url.split("/")[-1]
        if download_file(url, os.path.join(if_dir, fname)):
            dl += 1
            time.sleep(0.2)
    return f'dl_{dl}' if dl > 0 else 'dl_fail'


# ============================================================
# Phase 4: Format fixes
# ============================================================
def format_fix(filepath):
    with open(filepath) as fh: old = fh.read()
    c = old
    # Double backslash
    if '\\\\|' in c: c = c.replace('\\\\|', '\\|')
    # Remove .md from wikilinks
    c = re.sub(r'\[\[(Projects/[^\]]+)\.md', r'[[\1', c)
    # Add scoring table header if missing
    if '| 🔴 核定位' in c and '| 维度 | 得分' not in c:
        hdr = "| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |\n|------|------|------|--------|-------------|\n"
        c = c.replace('| 🔴 核定位', hdr + '| 🔴 核定位', 1)
    if c != old:
        with open(filepath, 'w') as fh: fh.write(c)
        return True
    return False


# ============================================================
# Worker for parallel PPI
# ============================================================
def ppi_worker(inq, outq):
    while True:
        try: task = inq.get(timeout=1)
        except queue.Empty: return
        path, gene = task
        try:
            r = fix_ppi(path, gene)
            outq.put(r)
        except Exception as e:
            outq.put(f'err')
        inq.task_done()

# ============================================================
# Worker for parallel literature
# ============================================================
def lit_worker(inq, outq):
    while True:
        try: task = inq.get(timeout=1)
        except queue.Empty: return
        path, gene = task
        try:
            r = fix_literature(path, gene)
            outq.put(r)
        except Exception as e:
            outq.put(f'err:{e}')
        inq.task_done()

# ============================================================
# Main
# ============================================================
def main():
    phases = set(sys.argv[1:]) if len(sys.argv) > 1 else {'lit', 'ppi', 'ifimg', 'fmt'}
    if 'all' in phases: phases = {'lit', 'ppi', 'ifimg', 'fmt'}

    # ---- Scan ----
    print("[0] Scanning reports...")
    lit_targets = []  # (path, gene)
    ppi_targets = []  # (path, gene)
    if_targets = []   # (path, gene)
    fmt_targets = []  # path

    for root, dirs, files in os.walk(DETAIL):
        for f in files:
            if not f.endswith('-evaluation.md'): continue
            path = os.path.join(root, f)
            gene = os.path.basename(os.path.dirname(path))
            cat = os.path.basename(os.path.dirname(os.path.dirname(path)))
            if cat == 'rejected': continue

            with open(path) as fh: content = fh.read()

            # --- Literature check ---
            has_33_sec = '3.3 研究' in content
            has_lit = '关键文献' in content
            needs_lit = False
            if has_lit:
                p = content.find('关键文献')
                chunk = content[p:p+2500]
                nrefs = len(re.findall(r'^\d+\.\s+\S', chunk, re.MULTILINE))
                if nrefs < 5: needs_lit = True
            else:
                needs_lit = True  # no 关键文献 at all

            if needs_lit:
                lit_targets.append((path, gene))

            # --- PPI check ---
            has_36 = '3.6 PPI' in content
            has_int = '实验验证互作' in content
            has_str = 'STRING 预测' in content or ('STRING' in content and 'combined score' in content)
            has_go = 'GO Cellular Component' in content or 'GO-CC' in content
            if not has_36 or not has_int or not has_str or not has_go:
                ppi_targets.append((path, gene))

            # --- IF check ---
            ifd = os.path.join(os.path.dirname(path), "IF_images")
            jpgs = []
            if os.path.exists(ifd):
                jpgs = [f for f in os.listdir(ifd) if f.endswith(".jpg")]
            if len(jpgs) < 2 and ('暂无数据' in content or 'Pending' in content):
                if_targets.append((path, gene))

            # --- Format check ---
            needs_fmt = False
            if '\\\\|' in content: needs_fmt = True
            if '| 🔴 核定位' in content and '| 维度 | 得分' not in content: needs_fmt = True
            if needs_fmt: fmt_targets.append(path)

    print(f"  Literature targets: {len(lit_targets)}")
    print(f"  PPI targets: {len(ppi_targets)}")
    print(f"  IF targets: {len(if_targets)}")
    print(f"  Format targets: {len(fmt_targets)}")

    # ---- Phase 1: Literature ----
    if 'lit' in phases and lit_targets:
        print(f"\n[1] Literature fix for {len(lit_targets)} reports (parallel, 2 workers)...")
        inq = queue.Queue()
        outq = queue.Queue()
        for t in lit_targets: inq.put(t)
        threads = []
        for _ in range(2):
            t = threading.Thread(target=lit_worker, args=(inq, outq)); t.daemon = True
            t.start(); threads.append(t)

        stats = {}
        total = len(lit_targets)
        done = 0
        lt = time.time()
        while done < total:
            try: r = outq.get(timeout=5); done += 1; stats[r] = stats.get(r,0)+1
            except queue.Empty:
                if all(not t.is_alive() for t in threads): break
            if time.time() - lt >= 3 or done % 20 == 0:
                print(f"  [{done}/{total}] " + " ".join(f"{k}={v}" for k,v in sorted(stats.items())))
                lt = time.time()
        for t in threads: t.join(5)
        print(f"  Literature done: " + " ".join(f"{k}={v}" for k,v in sorted(stats.items())))

    # ---- Phase 2: PPI ----
    if 'ppi' in phases and ppi_targets:
        print(f"\n[2] PPI fix for {len(ppi_targets)} reports (parallel, 2 workers)...")
        ppi_inq = queue.Queue()
        ppi_outq = queue.Queue()
        for t in ppi_targets: ppi_inq.put(t)

        ppi_threads = []
        for _ in range(2):
            t = threading.Thread(target=ppi_worker, args=(ppi_inq, ppi_outq)); t.daemon = True
            t.start(); ppi_threads.append(t)

        ppi_stats = {}
        ppi_total = len(ppi_targets)
        ppi_done = 0
        ppi_lt = time.time()
        while ppi_done < ppi_total:
            try:
                r = ppi_outq.get(timeout=5)
                ppi_done += 1
                ppi_stats[r] = ppi_stats.get(r, 0) + 1
                if ppi_done % 10 == 0 or ppi_done == 1:
                    elapsed = time.time() - ppi_lt
                    rate_val = ppi_done / elapsed if elapsed > 0 else 0
                    print(f"  [{ppi_done}/{ppi_total} {rate_val:.1f}/s] " + " ".join(f"{k}={v}" for k,v in sorted(ppi_stats.items())))
            except queue.Empty:
                if all(not t.is_alive() for t in ppi_threads): break
        for t in ppi_threads: t.join(5)
        print(f"  PPI done: " + " ".join(f"{k}={v}" for k,v in sorted(ppi_stats.items())))

    # ---- Phase 3: IF images ----
    if 'ifimg' in phases and if_targets:
        print(f"\n[3] IF image download for {len(if_targets)} reports...")
        stats = {}
        for i, (path, gene) in enumerate(if_targets):
            try:
                r = download_if(path, gene)
                stats[r] = stats.get(r, 0) + 1
            except Exception as e:
                stats['err'] = stats.get('err', 0) + 1
            if (i+1) % 15 == 0 or (i+1) == len(if_targets):
                print(f"  [{i+1}/{len(if_targets)}] " + " ".join(f"{k}={v}" for k,v in sorted(stats.items())))
        print(f"  IF done.")

    # ---- Phase 4: Format ----
    if 'fmt' in phases and fmt_targets:
        print(f"\n[4] Format fixes for {len(fmt_targets)} reports...")
        n = 0
        for path in fmt_targets:
            if format_fix(path): n += 1
        print(f"  {n} reports fixed (of {len(fmt_targets)} checked)")

    print(f"\n{'='*60}")
    print("ALL DONE")
    print("="*60)

if __name__ == "__main__":
    main()
