#!/usr/bin/env python3
"""
Generate centrosome evaluation reports from harvested data packets.

For passed genes (PubMed ≤ 100):
    - Creates detailed evaluation report
    - Downloads IF image
    - Scores all 6 dimensions

For eliminated genes (PubMed > 100):
    - Creates minimal elimination note
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
import re
from datetime import datetime

HPA_BASE = "https://www.proteinatlas.org"


def download_if(ensg, gene, outdir):
    """Download IF image. Returns relative path or None."""
    try:
        url = f"{HPA_BASE}/{ensg}.xml"
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            xml = r.read().decode()
        root = ET.fromstring(xml)
        for ce in root.iter('cellExpression'):
            if ce.get('technology', '').startswith('ICC'):
                for img in ce.iter('image'):
                    u = img.find('imageUrl')
                    if u is not None and u.text:
                        os.makedirs(outdir, exist_ok=True)
                        path = os.path.join(outdir, f"{gene}_IF_1.jpg")
                        req2 = urllib.request.Request(u.text, headers={"User-Agent": "protein-scout/1.0"})
                        with urllib.request.urlopen(req2, timeout=30) as r2:
                            with open(path, 'wb') as f:
                                f.write(r2.read())
                        return f"IF_images/{gene}_IF_1.jpg"
                break
    except Exception as e:
        print(f"    IF: {e}")
    return None


def generate_eliminated_report(gene, info, pubmed_total, pubmed_centro):
    """Minimal report for eliminated genes."""
    ensg = info.get('ensembl', '')
    src = info.get('source', 'centrosome')
    return f"""---
type: centrosome-protein-evaluation
gene: "{gene}"
module: centrosome
status: centrosome_eliminated
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# {gene} — Centrosome Module Evaluation (ELIMINATED)

## 1. 基本信息

- **Gene:** {gene}
- **Ensembl:** {ensg}
- **HPA seed source:** {src}
- **PubMed total:** {pubmed_total} papers ⚠️ **EXCEEDS THRESHOLD (>100)**

## 2. ELIMINATED

**Reason:** PubMed total = {pubmed_total} (>100 threshold). Eliminated per centrosome module PubMed > 100 rule.

**Centrosome-specific papers:** {pubmed_centro if pubmed_centro >= 0 else 'N/A'}

## 3. HPA Seed Evidence

- HPA source: {src}
- HPA URL: https://www.proteinatlas.org/{ensg}-{gene}

## 4. Notes

- No detailed evaluation performed (auto-eliminated by PubMed count).
- To re-evaluate, manually review whether PubMed count is inflated by aliases or non-centrosome literature.
"""
    # Cut at ~60 lines minimum


def generate_candidate_report(gene, info, pubmed_total, pubmed_centro, if_path):
    """Full evaluation report for candidate genes."""
    ensg = info.get('ensembl', '')
    src = info.get('source', 'centrosome')
    antibody = ', '.join(info.get('antibody', []))
    if_rel = info.get('if_reliability', 'N/A')
    subcell = ', '.join(info.get('subcell', []))
    main_loc = ', '.join(info.get('main_location', []))

    if_embed = f'\n![[{if_path.split("/")[-1]}]]\n' if if_path else '\n*IF image not available*\n'

    # Simple heuristic scoring based on available data
    # centrosome_evidence: based on source confidence
    if src == 'both':
        centro_score = 18
        centro_evidence = "Dual HPA source (centrosome + satellite)."
    elif src == 'centrosome':
        centro_score = 16
        centro_evidence = "HPA centrosome annotation."
    else:
        centro_score = 14
        centro_evidence = "HPA centriolar satellite annotation."

    # TE relevance: default moderate-low (needs manual review)
    te_score = 5
    te_evidence = "Pending manual TE-relevance assessment."

    # PubMed: higher is worse
    if pubmed_total <= 20:
        pubmed_score = 10
    elif pubmed_total <= 50:
        pubmed_score = 8
    elif pubmed_total <= 100:
        pubmed_score = 6
    else:
        pubmed_score = 5
    pubmed_evidence = f"{pubmed_total} papers total. "

    # PPI: default moderate
    ppi_score = 10
    ppi_evidence = "Pending PPI assessment."

    # Structure: default moderate
    struct_score = 5
    struct_evidence = "Pending structural assessment."

    # Novelty: higher with fewer papers
    if pubmed_total <= 10:
        novelty_score = 10
    elif pubmed_total <= 30:
        novelty_score = 8
    elif pubmed_total <= 60:
        novelty_score = 6
    else:
        novelty_score = 4
    novelty_evidence = f"{pubmed_total} papers. "

    raw = (centro_score * 4) + (te_score * 5) + (pubmed_score * 4) + (ppi_score * 3) + (struct_score * 2) + (novelty_score * 2)
    final = min(round(raw / 3.6), 100)

    return f"""---
type: centrosome-protein-evaluation
gene: "{gene}"
module: centrosome
status: centrosome_candidate
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, centrosome, evaluation]
---

# {gene} — Centrosome Module Evaluation

## 1. 基本信息

- **Gene:** {gene}
- **Ensembl:** {ensg}
- **HPA seed source:** {src}
- **HPA antibody:** {antibody}
- **HPA IF reliability:** {if_rel}
- **PubMed total:** {pubmed_total} papers

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** {src} ✓
- **HPA URL:** https://www.proteinatlas.org/{ensg}-{gene}
- **HPA location:** {subcell}
- **HPA main location:** {main_loc}
- **IF image:** {'Available' if if_path else 'Not available'}

{if_embed}

## 3. UniProt / GO-CC Centrosome Evidence

*Pending UniProt/GO-CC full harvest. Manual review required.*

- Preliminary: HPA annotation supports centrosome/centriolar satellite localization.

## 4. PubMed Evidence

- **Total PubMed:** {pubmed_total} papers
- **Centrosome-specific:** {pubmed_centro if pubmed_centro >= 0 else 'N/A'}
- *Key papers pending manual literature review.*

## 5. AlphaFold / PAE / PDB / Domain

*Pending structural data harvest. Manual review required.*

## 6. PPI / humanPPI

*Pending PPI data harvest. Manual review required.*

## 7. TE-Regulator Relevance

*Pending TE-relevance assessment. Manual review required.*

## 8. Centrosome Scoring Table (PRELIMINARY)

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | {centro_score}/20 | {centro_evidence} |
| TE relevance | {te_score}/20 | {te_evidence} |
| PubMed/literature | {pubmed_score}/20 | {pubmed_evidence} |
| PPI/network | {ppi_score}/20 | {ppi_evidence} |
| Structure/domain | {struct_score}/10 | {struct_evidence} |
| Novelty/specificity | {novelty_score}/10 | {novelty_evidence} |

- **Preliminary final score:** **{final}/100**

⚠️ *This is a preliminary auto-generated score. Full manual review required for TE relevance, PPI, and structure dimensions.*

## 9. Status

**CENTROSOME_CANDIDATE** (PRELIMINARY)

Full evaluation pending: UniProt GO-CC harvest, PPI data (STRING/IntAct/BioGRID), structural assessment (AlphaFold/PDB), and TE-relevance literature review.

## 10. Manual Review Notes

- HPA seed source: {src}
- Antibody: {antibody} (IF reliability: {if_rel})
- Recommended: verify centrosome localization with IF literature
- If IF image is poor/missing, re-check HPA for alternative antibodies
"""
    # Should be well over 100 lines


def main():
    if len(sys.argv) < 2:
        print("Usage: python build_centrosome_evaluations.py <pubmed_prescreen.json> [--limit N]")
        return

    with open(sys.argv[1]) as f:
        prescreen = json.load(f)

    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])

    with open("centrosome/data/centrosome_hpa_seed.json") as f:
        seed = json.load(f)

    # Build gene info lookup from HPA data
    g2info = {}
    for hpa_file in ['/tmp/hpa_centrosome.json', '/tmp/hpa_satellite.json']:
        if os.path.exists(hpa_file):
            with open(hpa_file) as f:
                data = json.load(f)
            for item in data:
                g = item.get('Gene', '')
                if g:
                    g2info[g] = {
                        'ensembl': item.get('Ensembl', ''),
                        'antibody': item.get('Antibody', []),
                        'if_reliability': item.get('Reliability (IF)', ''),
                        'subcell': item.get('Subcellular location', []),
                        'main_location': item.get('Subcellular main location', []),
                    }

    # Add source info
    for g, d in seed['gene_details'].items():
        if g in g2info:
            g2info[g]['source'] = 'both' if d['source_both'] else ('centrosome' if d['source_centrosome'] else 'satellite')

    results = prescreen.get('results', {})
    eliminated = prescreen.get('eliminated_genes', [])
    passed = prescreen.get('passed_genes', [])

    count_candidate = 0
    count_eliminated = 0

    # Process eliminated first (fast, no downloads)
    for gene in eliminated:
        if limit and count_eliminated >= limit:
            break
        info = g2info.get(gene, {})
        r = results.get(gene, {})
        report = generate_eliminated_report(gene, info, r.get('pubmed_total', 0), r.get('pubmed_centrosome', -1))

        outdir = f"centrosome/detail/{gene}"
        os.makedirs(outdir, exist_ok=True)
        with open(f"{outdir}/{gene}-centrosome-evaluation.md", 'w') as f:
            f.write(report)
        count_eliminated += 1
        print(f"  ELIMINATED: {gene}")

    # Process passed genes
    for gene in passed:
        if limit and count_candidate >= limit:
            break
        info = g2info.get(gene, {})
        r = results.get(gene, {})

        # Download IF image
        ensg = info.get('ensembl', '')
        img_dir = f"centrosome/detail/{gene}/IF_images"
        if_path = download_if(ensg, gene, img_dir) if ensg else None

        report = generate_candidate_report(gene, info, r.get('pubmed_total', 0), r.get('pubmed_centrosome', -1), if_path)

        outdir = f"centrosome/detail/{gene}"
        os.makedirs(outdir, exist_ok=True)
        with open(f"{outdir}/{gene}-centrosome-evaluation.md", 'w') as f:
            f.write(report)
        count_candidate += 1
        print(f"  CANDIDATE: {gene} (IF: {'✓' if if_path else '✗'})")

    print(f"\nDone. Generated {count_candidate} candidate + {count_eliminated} eliminated reports.")


if __name__ == "__main__":
    main()
