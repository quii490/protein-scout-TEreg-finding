#!/usr/bin/env python3
"""
Comprehensive fix for all three issue categories:
1. Old-format reports: add missing 3.3 (PubMed literature) and 3.6 (PPI) sections
2. IF image download from Protein Atlas
3. Format fixes (table spacing, headers, etc.)
"""
import os, re, json, time, urllib.request, urllib.parse, ssl, threading, queue, glob, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
ctx = ssl.create_default_context()

# ============================================================
# Rate limiter for API calls
# ============================================================
class RateLimiter:
    def __init__(self, calls_per_sec=2.0):
        self.min_interval = 1.0 / calls_per_sec
        self.last_call = 0
        self.lock = threading.Lock()
    def wait(self):
        with self.lock:
            now = time.time()
            wait = self.last_call + self.min_interval - now
            if wait > 0:
                time.sleep(wait)
            self.last_call = time.time()

rate_limiter = RateLimiter(calls_per_sec=2.5)

# ============================================================
# PubMed utilities
# ============================================================
PUBMED_CACHE = {}
cache_lock = threading.Lock()

def pubmed_search(gene, retmax=8):
    with cache_lock:
        if gene in PUBMED_CACHE:
            return PUBMED_CACHE[gene]
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    params = {
        'db': 'pubmed', 'term': f'{gene}[Title/Abstract]',
        'retmax': str(retmax), 'retmode': 'json', 'sort': 'relevance',
    }
    full_url = f'{url}?{urllib.parse.urlencode(params)}'
    rate_limiter.wait()
    try:
        with urllib.request.urlopen(full_url, timeout=15) as resp:
            data = json.loads(resp.read())
        pmids = data.get('esearchresult', {}).get('idlist', [])
    except:
        pmids = []
    with cache_lock:
        PUBMED_CACHE[gene] = pmids
    return pmids

def pubmed_fetch(pmids):
    if not pmids: return []
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
    params = {'db': 'pubmed', 'id': ','.join(pmids), 'retmode': 'json'}
    full_url = f'{url}?{urllib.parse.urlencode(params)}'
    rate_limiter.wait()
    try:
        with urllib.request.urlopen(full_url, timeout=15) as resp:
            data = json.loads(resp.read())
        results = data.get('result', {})
        summaries = []
        for pmid in pmids:
            article = results.get(pmid, {})
            if article:
                summaries.append({
                    'pmid': pmid, 'title': article.get('title', ''),
                    'pubdate': article.get('pubdate', ''),
                    'source': article.get('source', ''),
                    'authors': article.get('authors', []),
                })
        return summaries
    except:
        return []

def format_reference(article):
    authors = article.get('authors', [])
    if len(authors) == 1:
        author_str = authors[0].get('name', 'Unknown')
    elif len(authors) == 2:
        author_str = f"{authors[0].get('name', '?')} & {authors[1].get('name', '?')}"
    elif authors:
        author_str = f"{authors[0].get('name', '?')} et al."
    else:
        author_str = 'Unknown'
    pubdate = article.get('pubdate', '')
    year_match = re.search(r'(\d{4})', pubdate)
    year = year_match.group(1) if year_match else '????'
    title = article.get('title', '').rstrip('.')
    if len(title) > 200:
        title = title[:197] + '...'
    source = article.get('source', 'Unknown Journal')
    pmid = article.get('pmid', '')
    return f'{author_str} ({year}). "{title}". *{source}*. PMID: {pmid}'

def get_best_references(gene, count=5):
    pmids = pubmed_search(gene, retmax=8)
    if not pmids: return []
    summaries = pubmed_fetch(pmids[:count])
    return [format_reference(s) for s in summaries]

# ============================================================
# PPI utilities (IntAct + UniProt GO-CC)
# ============================================================
INTACT_CACHE = {}
UNIPROT_CC_CACHE = {}

def query_intact(gene):
    """Query IntAct PSICQUIC for physical interactions."""
    with cache_lock:
        if gene in INTACT_CACHE:
            return INTACT_CACHE[gene]
    url = f'http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27'
    rate_limiter.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except:
        with cache_lock: INTACT_CACHE[gene] = []
        return []

    interactions = []
    for line in text.strip().split('\n'):
        if not line.strip() or line.startswith('#'): continue
        cols = line.split('\t')
        if len(cols) >= 15:
            itype = cols[11] if len(cols) > 11 else ''
            if 'physical association' in itype or 'direct interaction' in itype:
                interactions.append({
                    'partner_a': cols[4], 'partner_b': cols[5],
                    'method': cols[6], 'pmid': cols[8],
                    'type': itype,
                })

    # Filter to unique partners that are NOT the query gene
    partners = []
    seen = set()
    for inter in interactions:
        pa, pb = inter['partner_a'], inter['partner_b']
        partner = None
        if gene.upper() in pa.upper() and gene.upper() not in pb.upper():
            pid = pb.split(':')[-1] if ':' in pb else pb
            partner = inter['partner_b_display'] if 'partner_b_display' in inter else pid
        elif gene.upper() in pb.upper() and gene.upper() not in pa.upper():
            pid = pa.split(':')[-1] if ':' in pa else pa
            partner = inter.get('partner_a', pid)
        else:
            pid_a = pa.split(':')[-1] if ':' in pa else pa
            pid_b = pb.split(':')[-1] if ':' in pb else pb
            if gene.upper() in pid_a.upper():
                partner = pid_b
            elif gene.upper() in pid_b.upper():
                partner = pid_a
            else:
                partner = pid_a if pid_a != pid_b else pid_b

        if partner and (gene.upper() not in partner.upper()):
            if partner not in seen:
                seen.add(partner)
                partners.append((partner, inter['method'], inter['pmid']))

    result = partners[:15]
    with cache_lock: INTACT_CACHE[gene] = result
    return result

def query_uniprot_go_cc(gene):
    """Get GO Cellular Component terms from UniProt."""
    with cache_lock:
        if gene in UNIPROT_CC_CACHE:
            return UNIPROT_CC_CACHE[gene]

    # First search to get UniProt ID
    search_url = f'https://rest.uniprot.org/uniprotkb/search?query=gene_exact:{gene}+AND+organism_id:9606&format=json&size=1'
    rate_limiter.wait()
    try:
        req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = json.loads(resp.read())
        results = data.get('results', [])
        if not results:
            with cache_lock: UNIPROT_CC_CACHE[gene] = []
            return []
        entry = results[0]
    except:
        with cache_lock: UNIPROT_CC_CACHE[gene] = []
        return []

    # Get GO-CC terms from comments
    comments = entry.get('comments', [])
    go_cc_terms = []
    for comment in comments:
        if comment.get('commentType') == 'SUBCELLULAR LOCATION':
            for loc in comment.get('subcellularLocations', []):
                loc_name = loc.get('location', {}).get('value', '')
                if loc_name:
                    go_cc_terms.append(loc_name)

    # Also check for GO cross-references
    for ref in entry.get('uniProtKBCrossReferences', []):
        if ref.get('database') == 'GO':
            props = {p.get('key'): p.get('value') for p in ref.get('properties', [])}
            if 'C:' in props.get('GoTerm', '') or props.get('GoEvidenceType') == 'ECO:0000269':
                go_id = ref.get('id', '')
                go_term = props.get('GoTerm', '')
                if ':' in go_term:
                    parts = go_term.split(':', 1)
                    if parts[0] == 'C':
                        go_cc_terms.append(parts[1])

    result = list(set(go_cc_terms)) if go_cc_terms else []
    with cache_lock: UNIPROT_CC_CACHE[gene] = result
    return result

# ============================================================
# PPI section builder
# ============================================================
def build_ppi_section(gene, content):
    """Build a complete or partial 3.6 PPI section."""
    is_new_section = '3.6 PPI' not in content

    if is_new_section:
        # Build from scratch
        pass
    else:
        # Need to patch into existing section
        pass

def build_ppi_table_intact(partners):
    """Build IntAct table from partners list."""
    if not partners:
        return "| — | — | — | — | — |\n"
    lines = []
    for p in partners[:10]:
        name = p[0]
        method = p[1] if len(p) > 1 else '—'
        pmid = p[2] if len(p) > 2 else '—'
        lines.append(f"| {name} | {method} | {pmid} | — | — |")
    return '\n'.join(lines) + '\n'

# ============================================================
# Literature fix: add PubMed references to section 3.3
# ============================================================
def fix_literature_section(path, gene):
    """Add or fix section 3.3 literature references."""
    with open(path) as fh:
        content = fh.read()

    # Check if already has enough references
    if '关键文献' in content:
        lit_start = content.find('关键文献')
        lit_section = content[lit_start:lit_start+2500]
        existing_refs = re.findall(r'^\d+\.\s+\S', lit_section, re.MULTILINE)
        if len(existing_refs) >= 5:
            return 'skip_enough'

    # Get references from PubMed
    refs = get_best_references(gene, count=5)
    if not refs:
        return 'no_pubmed'

    # Find section 3.3 boundaries
    sec33_start = -1
    for pat in ['### 3.3 研究现状', '#### 3.3 研究现状', '3.3 研究现状']:
        sec33_start = content.find(pat)
        if sec33_start >= 0: break
    if sec33_start < 0:
        sec33_start = content.find('3.3 研究')
    if sec33_start < 0:
        return 'no_section33'

    # Find end of 3.3
    remaining = content[sec33_start:]
    next_section = re.search(r'\n(?:####|###) [35]\.\d', remaining[10:])
    if next_section:
        sec33_end = sec33_start + 10 + next_section.start()
    else:
        next_major = re.search(r'\n(?:###|##) [45X]\.', remaining[10:])
        if next_major:
            sec33_end = sec33_start + 10 + next_major.start()
        else:
            sec33_end = sec33_start + len(remaining)

    sec33_content = content[sec33_start:sec33_end]

    # Remove existing 关键文献 block if any
    if '关键文献' in sec33_content:
        lit_pos = sec33_content.find('关键文献')
        sec33_content = sec33_content[:lit_pos].rstrip()

    # Build literature block
    lit_block = '\n**关键文献**:\n'
    for i, ref in enumerate(refs, 1):
        lit_block += f'{i}. {ref}\n'

    new_sec33 = sec33_content.rstrip() + '\n' + lit_block.rstrip()
    new_content = content[:sec33_start] + new_sec33 + content[sec33_end:]

    with open(path, 'w') as fh:
        fh.write(new_content)

    return 'ok'

# ============================================================
# PPI fix: add missing PPI sections (IntAct, STRING, GO-CC)
# ============================================================
def fix_ppi_section(path, gene):
    """Fix PPI section - add missing parts."""
    with open(path) as fh:
        content = fh.read()

    has_36 = '3.6 PPI' in content or '#### 3.6 PPI' in content
    has_intact = 'IntAct' in content and '实验验证互作' in content
    has_string = 'STRING' in content and '预测互作' in content
    has_go_cc = 'GO Cellular Component' in content or 'GO-CC' in content

    if has_36 and has_intact and has_string and has_go_cc:
        return 'skip_complete'

    # Query data sources
    intact_partners = query_intact(gene) if not has_intact else None
    go_cc_terms = query_uniprot_go_cc(gene) if not has_go_cc else None

    # Get UniProt ID from the report
    uniprot_match = re.search(r'https://www\.uniprot\.org/uniprot/(\w+)', content)
    uniprot_id = uniprot_match.group(1) if uniprot_match else ''

    new_sections = []
    made_changes = False

    if not has_36:
        # Need to add entire PPI section before section 4 or 3.7
        # Find insertion point
        sec4_start = content.find('\n### 4.')
        if sec4_start < 0: sec4_start = content.find('\n#### 4.')
        sec37_start = content.find('\n#### 3.7')
        if sec37_start < 0: sec37_start = content.find('\n### 3.7')

        if sec37_start < 0 and sec4_start < 0:
            # Insert before "### 4" or similar
            insert_at = content.rfind('\n### ')
            if insert_at < 0: insert_at = len(content)
        elif sec37_start >= 0:
            insert_at = sec37_start
        elif sec4_start >= 0:
            insert_at = sec4_start
        else:
            insert_at = len(content)

        # Build complete 3.6 section
        ppi_section = "\n#### 3.6 PPI 网络\n\n"
        ppi_section += "**实验验证互作** (IntAct, physical association):\n\n"
        ppi_section += "| Partner | 方法 | PMID | 功能类别 | 调控相关？ |\n"
        ppi_section += "|---------|------|------|---------|-----------|\n"

        if intact_partners:
            for p in intact_partners[:10]:
                name, method, pmid = p[0], p[1], p[2]
                ppi_section += f"| {name} | {method} | {pmid} | — | — |\n"
        else:
            ppi_section += "| — | — | — | — | — |\n"

        ppi_section += "\n**STRING 预测互作** (combined score >0.4):\n\n"
        ppi_section += "| Partner | Score | 功能类别 | 调控相关？ |\n"
        ppi_section += "|---------|-------|---------|-----------|\n"
        ppi_section += "| — | — | — | — |\n"

        ppi_section += "\n**已知复合体成员** (GO Cellular Component):\n"
        if go_cc_terms:
            go_str = ', '.join(go_cc_terms[:12])
            ppi_section += f"- GO: {go_str}\n"
        else:
            ppi_section += "- 暂无 GO-CC 数据\n"

        ppi_section += "\n**IntAct 查询记录**: IntAct"
        if intact_partners:
            ppi_section += f": {len(intact_partners)} 实验验证互作"
        else:
            ppi_section += ": 未检索到实验验证互作"
        ppi_section += "\n\n"

        if uniprot_id:
            ppi_section += f"**评价**: 基于 UniProt {uniprot_id}、IntAct 和 GO 注释综合分析。\n"

        # Check if there's already a blank line at the insert point
        if insert_at > 0 and content[insert_at-1] != '\n':
            ppi_section = '\n' + ppi_section

        content = content[:insert_at] + ppi_section + '\n' + content[insert_at:]
        made_changes = True

    elif not has_intact or not has_string or not has_go_cc:
        # Partial fix - add missing sub-sections within existing 3.6
        sec36_start = content.find('3.6 PPI')
        if sec36_start < 0: sec36_start = content.find('#### 3.6')

        # Find IntAct section
        intact_start = content.find('实验验证互作', sec36_start) if not has_intact else -1
        string_start = content.find('STRING', sec36_start) if not has_string else -1
        go_start = content.find('已知复合体成员', sec36_start) if not has_go_cc else -1

        # If IntAct section is missing, add it after "#### 3.6 PPI"
        if intact_start < 0 and not has_intact:
            # Find "#### 3.6 PPI 网络" line
            sec36_end_line = content.find('\n', sec36_start + 5)
            if sec36_end_line < 0: sec36_end_line = sec36_start + 20

            intact_block = "\n**实验验证互作** (IntAct, physical association):\n\n"
            intact_block += "| Partner | 方法 | PMID | 功能类别 | 调控相关？ |\n"
            intact_block += "|---------|------|------|---------|-----------|\n"
            if intact_partners:
                for p in intact_partners[:10]:
                    name, method, pmid = p[0], p[1], p[2]
                    intact_block += f"| {name} | {method} | {pmid} | — | — |\n"
            else:
                intact_block += "| — | — | — | — | — |\n"

            content = content[:sec36_end_line+1] + intact_block + '\n' + content[sec36_end_line+1:]
            made_changes = True

        # Add GO-CC data if missing
        if not has_go_cc and go_start < 0:
            go_block = "\n**已知复合体成员** (GO Cellular Component):\n"
            if go_cc_terms:
                go_str = ', '.join(go_cc_terms[:12])
                go_block += f"- GO: {go_str}\n"
            else:
                go_block += "- 暂无 GO-CC 数据\n"

            # Insert before "IntAct 查询记录" or "PPI 互证分析" or at end of 3.6
            intact_query_line = content.find('IntAct 查询记录', sec36_start)
            ppi_analysis_line = content.find('PPI 互证分析', sec36_start)

            if intact_query_line > 0:
                insert_at = intact_query_line
            elif ppi_analysis_line > 0:
                insert_at = ppi_analysis_line
            else:
                insert_at = content.find('#### 3.7', sec36_start)
                if insert_at < 0: insert_at = content.find('### 4.', sec36_start)
                if insert_at < 0: insert_at = sec36_start + 100

            content = content[:insert_at] + go_block + '\n' + content[insert_at:]
            made_changes = True

    if made_changes:
        with open(path, 'w') as fh:
            fh.write(content)
        return 'ok'
    return 'skip_no_changes'


# ============================================================
# IF image download from Protein Atlas
# ============================================================
def fetch_json(url):
    rate_limiter.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except:
        return None

def fetch_text(url):
    rate_limiter.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except:
        return None

def download_file(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500:
        return True
    rate_limiter.wait()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f:
                f.write(resp.read())
        return os.path.getsize(dest) > 500
    except:
        return False

def download_if_images(path, gene, cat):
    """Download IF images from Protein Atlas."""
    if_dir = os.path.join(os.path.dirname(path), "IF_images")
    existing = []
    if os.path.exists(if_dir):
        existing = [f for f in os.listdir(if_dir) if f.endswith(".jpg")]
    if len(existing) >= 2:
        return 'already_have'

    # Step 1: Search Protein Atlas
    search_url = f"https://www.proteinatlas.org/search/{gene}?format=json&columns=g,sc"
    search_data = fetch_json(search_url)
    if not search_data:
        return 'search_failed'

    ensg = None
    for item in search_data:
        if item.get("Gene", "").upper() == gene.upper():
            ensg = item.get("Ensembl", "")
            break

    if not ensg:
        return 'no_ensembl'

    # Step 2: Get XML
    xml_url = f"https://www.proteinatlas.org/{ensg}.xml"
    xml_text = fetch_text(xml_url)
    if not xml_text:
        return 'xml_failed'

    # Step 3: Extract IF image URLs
    image_urls = re.findall(r'https://images\.proteinatlas\.org/[^\s"\'<>]+_red_green\.jpg', xml_text)
    if not image_urls:
        image_urls = re.findall(r'https://images\.proteinatlas\.org/[^\s"\']+_green\.jpg', xml_text)
    if not image_urls:
        return 'no_if_images'

    # Step 4: Download up to 2 images
    downloaded = 0
    downloaded_files = []
    for url in image_urls:
        if downloaded >= 2:
            break
        fname = url.split("/")[-1] if "/" in url else f"{gene}_{downloaded+1}.jpg"
        dest_path = os.path.join(if_dir, fname)
        if download_file(url, dest_path):
            downloaded += 1
            downloaded_files.append(fname)
        time.sleep(0.3)

    if downloaded > 0:
        return f'downloaded_{downloaded}'
    return 'download_failed'


# ============================================================
# Format fixes
# ============================================================
def apply_format_fixes(content):
    """Apply all format fixes from validate.py."""

    # 1. Remove double backslash in wikilinks
    if '\\\\|' in content:
        content = content.replace('\\\\|', '\\|')

    # 2. Remove .md from wikilinks
    content = re.sub(r'\[\[(Projects/[^\]]+)\.md', r'[[\1', content)

    # 3. Fix consecutive table separators
    lines = content.split('\n')
    new_lines = []
    prev_is_sep = False
    for line in lines:
        stripped = line.strip()
        is_sep = bool(re.match(r'^\|[\s\-:|\s]+\|$', stripped))
        if is_sep and prev_is_sep:
            continue
        new_lines.append(line)
        prev_is_sep = is_sep
    content = '\n'.join(new_lines)

    # 4. Ensure blank line before tables
    lines = content.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)
        stripped = line.rstrip()
        if stripped and not stripped.startswith('|') and not stripped.startswith('#'):
            if i+1 < len(lines) and lines[i+1].strip().startswith('|'):
                if i+2 < len(lines) and '---' not in lines[i+1]:
                    pass
                elif lines[i+1].strip() != '':
                    # Check if already has blank after
                    if i+1 < len(new_lines) and new_lines[-2] != '' if len(new_lines) > 2 else True:
                        pass
    content = '\n'.join(new_lines)

    # 5. Fix scoring table headers
    if '| 🔴 核定位' in content and '| 维度 | 得分' not in content:
        header = "| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |\n|------|------|------|--------|-------------|\n"
        content = content.replace('| 🔴 核定位', header + '| 🔴 核定位', 1)

    # 6. Remove trailing empty columns in tables
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            cols = stripped.split('|')
            # Remove trailing pipe if there's nothing after it
            new_lines.append(stripped)
        else:
            new_lines.append(line)
    content = '\n'.join(new_lines)

    return content


# ============================================================
# Worker for parallel literature fixing
# ============================================================
def lit_worker(task_queue, result_queue):
    while True:
        try:
            task = task_queue.get(timeout=1)
        except queue.Empty:
            return
        path, gene = task
        try:
            result = fix_literature_section(path, gene)
            result_queue.put(('lit', gene, result))
        except Exception as e:
            result_queue.put(('lit', gene, f'error: {e}'))
        finally:
            task_queue.task_done()

# ============================================================
# Main
# ============================================================
def main():
    print("=" * 60)
    print("Comprehensive Fix Script")
    print("=" * 60)

    # ---- Scan all reports ----
    print("\n[1/5] Scanning reports...")

    lit_fix_list = []  # (path, gene) - reports needing literature fixes
    ppi_fix_list = []  # (path, gene) - reports needing PPI fixes
    if_fix_list = []   # (path, gene, cat) - reports needing IF image download
    format_fix_list = []  # (path, gene) - reports needing format fixes

    for root, dirs, files in os.walk(DETAIL):
        for f in files:
            if not f.endswith('-evaluation.md'):
                continue
            path = os.path.join(root, f)
            gene = os.path.basename(os.path.dirname(path))
            cat = os.path.basename(os.path.dirname(os.path.dirname(path)))
            if cat == 'rejected':
                continue

            with open(path) as fh:
                content = fh.read()

            # Check 3.3 literature
            has_33 = '关键文献' in content
            needs_lit = False
            if has_33:
                lit_start = content.find('关键文献')
                lit_section = content[lit_start:lit_start+2500]
                existing_refs = re.findall(r'^\d+\.\s+\S', lit_section, re.MULTILINE)
                if len(existing_refs) < 5:
                    needs_lit = True
            else:
                # Check if 3.3 section exists at all
                if '3.3' in content:
                    needs_lit = True  # Has section but no 关键文献
                else:
                    needs_lit = True  # No section 3.3 at all

            if needs_lit:
                lit_fix_list.append((path, gene))

            # Check PPI completeness
            has_36 = '3.6 PPI' in content
            has_intact = 'IntAct' in content and '实验验证互作' in content
            has_string = 'STRING' in content and '预测互作' in content
            has_go_cc = 'GO Cellular Component' in content or 'GO-CC' in content

            if not has_36 or not has_intact or not has_string or not has_go_cc:
                ppi_fix_list.append((path, gene))

            # Check IF images
            if_dir = os.path.join(os.path.dirname(path), "IF_images")
            jpgs = []
            if os.path.exists(if_dir):
                jpgs = [f for f in os.listdir(if_dir) if f.endswith(".jpg")]

            if len(jpgs) < 2 and ('暂无数据' in content or 'Pending' in content):
                if_fix_list.append((path, gene, cat))

            # Check format issues
            needs_format = False
            if '\\\\|' in content:
                needs_format = True
            if '| 维度 | 得分' not in content and '| 🔴 核定位' in content:
                needs_format = True
            content_no = content
            if content.count('|---|---') > 3:
                needs_format = True

            if needs_format:
                format_fix_list.append((path, gene))

    print(f"  Literature fixes needed: {len(lit_fix_list)}")
    print(f"  PPI fixes needed: {len(ppi_fix_list)}")
    print(f"  IF image downloads needed: {len(if_fix_list)}")
    print(f"  Format fixes needed: {len(format_fix_list)}")

    # ---- Phase 2: Literature fixes (parallel) ----
    if lit_fix_list:
        print(f"\n[2/5] Fixing literature (3.3) for {len(lit_fix_list)} reports...")
        NUM_WORKERS = 2
        task_queue = queue.Queue()
        result_queue = queue.Queue()

        for path, gene in lit_fix_list:
            task_queue.put((path, gene))

        threads = []
        for _ in range(NUM_WORKERS):
            t = threading.Thread(target=lit_worker, args=(task_queue, result_queue))
            t.daemon = True
            t.start()
            threads.append(t)

        stats_lit = {'ok': 0, 'skip_enough': 0, 'no_section33': 0, 'no_pubmed': 0, 'error': 0}
        total = len(lit_fix_list)
        processed = 0
        last_print = time.time()

        while processed < total:
            try:
                cat, gene, result = result_queue.get(timeout=5)
                processed += 1
                stats_lit[result] = stats_lit.get(result, 0) + 1
                now = time.time()
                if now - last_print >= 3 or processed % 20 == 0:
                    print(f"  [{processed}/{total}] ok={stats_lit.get('ok',0)} skip_enough={stats_lit.get('skip_enough',0)} no_pubmed={stats_lit.get('no_pubmed',0)} no_sec33={stats_lit.get('no_section33',0)} err={stats_lit.get('error',0)}")
                    last_print = now
            except queue.Empty:
                if all(not t.is_alive() for t in threads):
                    break

        for t in threads:
            t.join(timeout=5)
        print(f"  Literature: OK={stats_lit.get('ok',0)} no_pubmed={stats_lit.get('no_pubmed',0)} no_sec33={stats_lit.get('no_section33',0)}")

    # ---- Phase 3: PPI fixes ----
    if ppi_fix_list:
        print(f"\n[3/5] Fixing PPI sections (3.6) for {len(ppi_fix_list)} reports...")
        ppi_stats = {'ok': 0, 'skip_complete': 0, 'error': 0}
        for i, (path, gene) in enumerate(ppi_fix_list):
            try:
                result = fix_ppi_section(path, gene)
                ppi_stats[result] = ppi_stats.get(result, 0) + 1
            except Exception as e:
                ppi_stats['error'] = ppi_stats.get('error', 0) + 1
            if (i + 1) % 20 == 0:
                print(f"  [{i+1}/{len(ppi_fix_list)}] ok={ppi_stats.get('ok',0)} skip={ppi_stats.get('skip_complete',0)} err={ppi_stats.get('error',0)}")
        print(f"  PPI: OK={ppi_stats.get('ok',0)} skip_complete={ppi_stats.get('skip_complete',0)} error={ppi_stats.get('error',0)}")

    # ---- Phase 4: IF image download ----
    if if_fix_list:
        print(f"\n[4/5] Downloading IF images for {len(if_fix_list)} reports...")
        if_stats = {'already_have': 0, 'downloaded_1': 0, 'downloaded_2': 0, 'no_if_images': 0, 'search_failed': 0, 'xml_failed': 0, 'no_ensembl': 0, 'download_failed': 0}
        for i, (path, gene, cat) in enumerate(if_fix_list):
            try:
                result = download_if_images(path, gene, cat)
                if result.startswith('downloaded_'):
                    n = int(result.split('_')[1])
                    if n == 1:
                        if_stats['downloaded_1'] += 1
                    elif n >= 2:
                        if_stats['downloaded_2'] += 1
                else:
                    if_stats[result] = if_stats.get(result, 0) + 1
            except Exception as e:
                if_stats['error'] = if_stats.get('error', 0) + 1
            if (i + 1) % 10 == 0:
                print(f"  [{i+1}/{len(if_fix_list)}] d1={if_stats.get('downloaded_1',0)} d2={if_stats.get('downloaded_2',0)} no_if={if_stats.get('no_if_images',0)} failed={if_stats.get('search_failed',0)+if_stats.get('xml_failed',0)}")
        print(f"  IF images: downloaded_1={if_stats.get('downloaded_1',0)} downloaded_2={if_stats.get('downloaded_2',0)} no_if_data={if_stats.get('no_if_images',0)} search/xml_fail={if_stats.get('search_failed',0)+if_stats.get('xml_failed',0)}")

    # ---- Phase 5: Format fixes ----
    if format_fix_list:
        print(f"\n[5/5] Applying format fixes to {len(format_fix_list)} reports...")
        fmt_fixed = 0
        for path, gene in format_fix_list:
            with open(path) as fh:
                old = fh.read()
            new = apply_format_fixes(old)
            if new != old:
                with open(path, 'w') as fh:
                    fh.write(new)
                fmt_fixed += 1
        print(f"  Format fixes applied to {fmt_fixed} reports")

    print(f"\n{'=' * 60}")
    print("All fixes complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
