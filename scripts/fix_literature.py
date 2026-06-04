#!/usr/bin/env python3
"""
Fix missing literature in protein evaluation reports - parallel version.
Uses PubMed E-utils with concurrent workers for faster processing.
"""
import os, re, json, time, urllib.request, urllib.parse, threading, queue

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

PRIORITY_CATS = ['nucleoplasm', 'nucleus-cytoplasm']

# Thread-safe PubMed cache
PUBMED_CACHE = {}
cache_lock = threading.Lock()

# Rate limiter: max 3 req/sec without API key
class RateLimiter:
    def __init__(self, max_per_sec=2.5):
        self.max_per_sec = max_per_sec
        self.min_interval = 1.0 / max_per_sec
        self.last_call = 0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            now = time.time()
            wait = self.last_call + self.min_interval - now
            if wait > 0:
                time.sleep(wait)
            self.last_call = time.time()

rate_limiter = RateLimiter(max_per_sec=2.5)

def pubmed_search(gene, retmax=8):
    """Search PubMed for a gene and return PMIDs."""
    with cache_lock:
        if gene in PUBMED_CACHE:
            return PUBMED_CACHE[gene]

    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    params = {
        'db': 'pubmed',
        'term': f'{gene}[Title/Abstract]',
        'retmax': str(retmax),
        'retmode': 'json',
        'sort': 'relevance',
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f'{url}?{query_string}'

    rate_limiter.wait()
    try:
        with urllib.request.urlopen(full_url, timeout=15) as resp:
            data = json.loads(resp.read())
        pmids = data.get('esearchresult', {}).get('idlist', [])
    except Exception as e:
        pmids = []

    with cache_lock:
        PUBMED_CACHE[gene] = pmids
    return pmids


def pubmed_fetch(pmids):
    """Fetch summaries for a list of PMIDs."""
    if not pmids:
        return []

    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
    params = {
        'db': 'pubmed',
        'id': ','.join(pmids),
        'retmode': 'json',
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f'{url}?{query_string}'

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
                    'pmid': pmid,
                    'title': article.get('title', ''),
                    'pubdate': article.get('pubdate', ''),
                    'source': article.get('source', ''),
                    'authors': article.get('authors', []),
                })
        return summaries
    except Exception:
        return []


def format_reference(article):
    """Format a PubMed article as a reference string."""
    authors = article.get('authors', [])
    if authors:
        if len(authors) == 1:
            author_str = authors[0].get('name', 'Unknown')
        elif len(authors) == 2:
            author_str = f"{authors[0].get('name', '?')} & {authors[1].get('name', '?')}"
        else:
            author_str = f"{authors[0].get('name', '?')} et al."
    else:
        author_str = 'Unknown'

    pubdate = article.get('pubdate', '')
    year_match = re.search(r'(\d{4})', pubdate)
    year = year_match.group(1) if year_match else '????'

    title = article.get('title', '').rstrip('.')

    # Truncate long titles
    if len(title) > 200:
        title = title[:197] + '...'

    source = article.get('source', 'Unknown Journal')
    pmid = article.get('pmid', '')

    return f'{author_str} ({year}). "{title}". *{source}*. PMID: {pmid}'


def get_best_references(gene, count=5):
    """Get the best references for a gene from PubMed."""
    pmids = pubmed_search(gene, retmax=8)
    if not pmids:
        return []

    selected_pmids = pmids[:count]
    summaries = pubmed_fetch(selected_pmids)

    refs = []
    for s in summaries:
        ref_str = format_reference(s)
        refs.append(ref_str)

    return refs


def add_literature_to_report(path, gene):
    """Add key literature references to a report's section 3.3."""
    with open(path) as fh:
        content = fh.read()

    # Check if already has 关键文献
    if '关键文献' in content:
        lit_start = content.find('关键文献')
        lit_section = content[lit_start:lit_start+2500]
        existing_refs = re.findall(r'^\d+\.\s+\S', lit_section, re.MULTILINE)
        if len(existing_refs) >= 5:
            return 'skip_has_enough'

    # Find section 3.3
    sec33_start = -1
    for pattern in ['#### 3.3 研究现状', '### 3.3 研究现状', '3.3 研究现状']:
        sec33_start = content.find(pattern)
        if sec33_start >= 0:
            break
    if sec33_start < 0:
        # Try broader patterns
        for pattern in ['#### 3.3', '### 3.3']:
            sec33_start = content.find(pattern)
            if sec33_start >= 0:
                break
    if sec33_start < 0:
        return 'skip_no_section33'

    # Find the end of section 3.3 (next #### or ###)
    remaining = content[sec33_start:]
    next_section = re.search(r'\n(?:####|###) 3\.\d', remaining[10:])
    if next_section:
        sec33_end = sec33_start + 10 + next_section.start()
    else:
        next_major = re.search(r'\n(?:###|##) [45X]\.', remaining[10:])
        if next_major:
            sec33_end = sec33_start + 10 + next_major.start()
        else:
            sec33_end = sec33_start + len(remaining)

    sec33_content = content[sec33_start:sec33_end]

    # Get PubMed references
    refs = get_best_references(gene, count=5)
    if not refs:
        return 'skip_no_pubmed'

    # Build literature block
    lit_block = '\n**关键文献**:\n'
    for i, ref in enumerate(refs, 1):
        lit_block += f'{i}. {ref}\n'

    # Insert after section 3.3 content
    new_sec33 = sec33_content.rstrip() + '\n' + lit_block.rstrip()
    new_content = content[:sec33_start] + new_sec33 + content[sec33_end:]

    with open(path, 'w') as fh:
        fh.write(new_content)

    return 'ok'


def worker(task_queue, result_queue):
    """Worker thread for processing reports."""
    while True:
        try:
            task = task_queue.get(timeout=1)
        except queue.Empty:
            return

        cat, gene, path = task
        try:
            result = add_literature_to_report(path, gene)
            result_queue.put((cat, gene, result))
        except Exception as e:
            result_queue.put((cat, gene, f'error: {e}'))
        finally:
            task_queue.task_done()


def main():
    """Fix literature in reports without adequate references."""
    reports_to_fix = []

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

            if '关键文献' in content:
                lit_start = content.find('关键文献')
                lit_section = content[lit_start:lit_start+2500]
                existing_refs = re.findall(r'^\d+\.\s+\S', lit_section, re.MULTILINE)
                if len(existing_refs) >= 5:
                    continue

            reports_to_fix.append((cat, gene, path))

    # Sort by priority
    def priority_key(item):
        cat = item[0]
        if cat in PRIORITY_CATS:
            return (0, cat, item[1])
        return (1, cat, item[1])

    reports_to_fix.sort(key=priority_key)

    print(f"Reports to fix: {len(reports_to_fix)}")
    priority_count = sum(1 for r in reports_to_fix if r[0] in PRIORITY_CATS)
    print(f"Priority (nucleoplasm + nucleus-cytoplasm): {priority_count}")
    print()

    # Setup parallel workers (2 workers = ~5 genes/sec max)
    NUM_WORKERS = 2
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    for task in reports_to_fix:
        task_queue.put(task)

    threads = []
    for _ in range(NUM_WORKERS):
        t = threading.Thread(target=worker, args=(task_queue, result_queue))
        t.daemon = True
        t.start()
        threads.append(t)

    # Monitor progress
    stats = {'ok': 0, 'skip_has_enough': 0, 'skip_no_section33': 0, 'skip_no_pubmed': 0, 'error': 0}
    total = len(reports_to_fix)
    last_print = time.time()

    processed = 0
    while processed < total:
        try:
            cat, gene, result = result_queue.get(timeout=5)
            processed += 1
            stats[result] = stats.get(result, 0) + 1

            now = time.time()
            if now - last_print >= 3 or processed % 50 == 0:
                pct = processed * 100 // total
                print(f"[{processed}/{total} ({pct}%)] ok={stats['ok']} no_pubmed={stats['skip_no_pubmed']} no_sec33={stats['skip_no_section33']} err={stats['error']}")
                last_print = now
        except queue.Empty:
            # Check if all threads are done
            if all(not t.is_alive() for t in threads):
                break

    for t in threads:
        t.join(timeout=5)

    print(f"\n{'='*50}")
    print(f"Total: {total}")
    print(f"  OK (added refs): {stats.get('ok', 0)}")
    print(f"  Skip (already has >=5): {stats.get('skip_has_enough', 0)}")
    print(f"  Skip (no section 3.3): {stats.get('skip_no_section33', 0)}")
    print(f"  Skip (no PubMed results): {stats.get('skip_no_pubmed', 0)}")
    print(f"  Errors: {stats.get('error', 0)}")


if __name__ == "__main__":
    main()
