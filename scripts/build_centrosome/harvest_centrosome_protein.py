#!/usr/bin/env python3
"""
Batch harvest centrosome protein data for full evaluation.

Usage:
    python harvest_centrosome_protein.py --pubmed-only    # Just PubMed pre-screen
    python harvest_centrosome_protein.py --batch N        # Harvest batch N
    python harvest_centrosome_protein.py --gene GENE      # Single gene
"""
import json
import os
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HPA_BASE = "https://www.proteinatlas.org"
SLEEP = 0.35  # NCBI rate limit: 3/sec without API key


def pubmed_count(gene):
    """Get total PubMed count for a gene."""
    url = f"{EUTILS_BASE}/esearch.fcgi?db=pubmed&retmax=0&usehistory=y&term={gene}[Gene]"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml = resp.read().decode()
        # Extract <Count>
        import re
        m = re.search(r'<Count>(\d+)</Count>', xml)
        if m:
            return int(m.group(1))
    except Exception as e:
        print(f"  PubMed query failed for {gene}: {e}")
    return -1


def pubmed_centrosome_count(gene):
    """Get centrosome-specific PubMed count."""
    query = urllib.parse.quote(f"{gene}[Gene] AND (centrosome OR centriole OR cilia)")
    url = f"{EUTILS_BASE}/esearch.fcgi?db=pubmed&retmax=0&usehistory=y&term={query}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml = resp.read().decode()
        import re
        m = re.search(r'<Count>(\d+)</Count>', xml)
        if m:
            return int(m.group(1))
    except:
        pass
    return -1


def download_if_image(ensg, gene, output_dir):
    """Download HPA IF image for a gene."""
    os.makedirs(output_dir, exist_ok=True)
    try:
        url = f"{HPA_BASE}/{ensg}.xml"
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml = resp.read().decode()
        root = ET.fromstring(xml)
        for ce in root.iter('cellExpression'):
            if ce.get('technology', '').startswith('ICC'):
                for img in ce.iter('image'):
                    u = img.find('imageUrl')
                    if u is not None and u.text:
                        img_url = u.text
                        img_path = os.path.join(output_dir, f"{gene}_IF_1.jpg")
                        req2 = urllib.request.Request(img_url, headers={"User-Agent": "protein-scout/1.0"})
                        with urllib.request.urlopen(req2, timeout=30) as resp2:
                            with open(img_path, 'wb') as f:
                                f.write(resp2.read())
                        return img_path
                break
    except Exception as e:
        print(f"    IF download failed for {gene}: {e}")
    return None


def main():
    os.makedirs("centrosome/packets", exist_ok=True)
    os.makedirs("centrosome/logs", exist_ok=True)

    with open("centrosome/data/centrosome_hpa_seed.json") as f:
        seed = json.load(f)

    all_genes = sorted(seed['genes'])

    # Exclude pilot 10
    pilot = {'AURKA','PLK4','CEP192','NEDD1','CETN2','PCM1','CCP110','CCDC14','CEP72','CEP97'}
    genes = [g for g in all_genes if g not in pilot]

    # Get ENSG mapping
    with open('/tmp/hpa_centrosome.json') as f:
        centro = json.load(f)
    with open('/tmp/hpa_satellite.json') as f:
        sat = json.load(f)

    g2e = {}
    g2info = {}
    for item in centro + sat:
        g = item.get('Gene', '')
        if g in genes or g in pilot:
            g2e[g] = item.get('Ensembl', '')
            g2info[g] = {
                'ensembl': item.get('Ensembl', ''),
                'antibody': item.get('Antibody', []),
                'if_reliability': item.get('Reliability (IF)', ''),
                'subcell': item.get('Subcellular location', []),
                'main_location': item.get('Subcellular main location', []),
                'source_centrosome': g in {g2: d for g2, d in seed['gene_details'].items() if d['source_centrosome']},
                'source_satellite': g in {g2: d for g2, d in seed['gene_details'].items() if d['source_centriolar_satellite']},
            }

    # PubMed pre-screen
    print(f"PubMed pre-screening {len(genes)} genes...")
    results = {}
    passed = []
    eliminated = []
    errors = []

    for i, gene in enumerate(genes):
        total = pubmed_count(gene)
        centro_count = pubmed_centrosome_count(gene) if total <= 150 else -1

        info = g2info.get(gene, {})
        packet = {
            'gene': gene,
            'pubmed_total': total,
            'pubmed_centrosome': centro_count,
            'ensembl': info.get('ensembl', ''),
            'source': 'centrosome' if info.get('source_centrosome') else ('satellite' if info.get('source_satellite') else 'both'),
            'harvested_at': datetime.now().isoformat()
        }
        results[gene] = packet

        if total == -1:
            errors.append(gene)
            print(f"  [{i+1}/{len(genes)}] {gene}: ERROR")
        elif total > 100:
            eliminated.append(gene)
            print(f"  [{i+1}/{len(genes)}] {gene}: {total} papers → ELIMINATED")
        else:
            passed.append(gene)
            print(f"  [{i+1}/{len(genes)}] {gene}: {total} papers ✓")

        time.sleep(SLEEP)

    # Save results
    summary = {
        'date': datetime.now().isoformat(),
        'total_screened': len(genes),
        'passed': len(passed),
        'eliminated': len(eliminated),
        'errors': len(errors),
        'passed_genes': passed,
        'eliminated_genes': eliminated,
        'error_genes': errors,
        'results': results
    }

    with open("centrosome/data/pubmed_prescreen_results.json", 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open("centrosome/data/pubmed_prescreen.tsv", 'w') as f:
        f.write("gene\tpubmed_total\tpubmed_centrosome\tdecision\n")
        for g in sorted(genes):
            r = results.get(g, {})
            dec = 'ELIMINATED' if r.get('pubmed_total', -1) > 100 else ('PASSED' if r.get('pubmed_total', -1) >= 0 else 'ERROR')
            f.write(f"{g}\t{r.get('pubmed_total', -1)}\t{r.get('pubmed_centrosome', -1)}\t{dec}\n")

    print(f"\n{'='*50}")
    print(f"PubMed Pre-screen Complete")
    print(f"  Total screened: {len(genes)}")
    print(f"  Passed (≤100):  {len(passed)}")
    print(f"  Eliminated (>100): {len(eliminated)}")
    print(f"  Errors: {len(errors)}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
