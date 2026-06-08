#!/usr/bin/env python3
"""
Build centrosome report index from centrosome/detail/ evaluation reports.

Outputs:
    centrosome/data/centrosome_report_index.tsv
    centrosome/data/centrosome_report_index.csv
    centrosome/data/centrosome_report_index.json
    docs/centrosome/data/centrosome_report_index.json
"""
import json
import os
import sys
import csv
import re
from datetime import datetime


def parse_evaluation(path):
    """Parse a centrosome evaluation markdown report."""
    with open(path) as f:
        content = f.read()

    lines = content.split('\n')
    gene = os.path.basename(os.path.dirname(path))

    # Parse YAML frontmatter (manual parse to avoid pyyaml dependency)
    frontmatter = {}
    if content.startswith('---'):
        yaml_end = content.find('---', 3)
        if yaml_end > 0:
            for line in content[3:yaml_end].split('\n'):
                line = line.strip()
                if ':' in line:
                    k, v = line.split(':', 1)
                    frontmatter[k.strip()] = v.strip().strip('"').strip("'")

    status = frontmatter.get('status', '')

    # Parse scoring table
    scores = {}
    in_table = False
    for line in lines:
        if '| Dimension | Score' in line or '| 维度 | 评分' in line or '| 维度 | Score' in line:
            in_table = True
            continue
        if in_table and line.startswith('|') and '---' not in line and line.count('|') >= 3:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                dim = parts[1]
                score_str = parts[2]
                try:
                    val = float(score_str.split('/')[0].strip())
                    scores[dim] = val
                except:
                    pass
        if in_table and not line.startswith('|') and not line.startswith('-'):
            in_table = False

    # Parse final score (may be outside table)
    for line in lines:
        if 'Final centrosome score' in line or 'Final score' in line or 'final score' in line.lower() or '最终评分' in line:
            score_match = re.search(r'\*{0,2}(\d+)\s*/\s*100\*{0,2}', line)
            if score_match:
                scores['final'] = float(score_match.group(1))
                break

    # Parse assessment info
    pubmed_total = 0
    pm = re.search(r'Total PubMed.*?(\d[\d,]*)\s*papers', content)
    if pm:
        pubmed_total = int(pm.group(1).replace(',', ''))

    # Source info
    source_centro = 'centrosome' in frontmatter.get('tags', '') or 'Centrosome' in content[:500]
    source_sat = 'centriolar satellite' in content[:500].lower()

    has_hpa = 'HPA' in content and 'IF image' in content
    has_pdb = 'PDB' in content and ('Available' in content or 'available' in content)

    return {
        'gene': gene,
        'status': status,
        'final_centrosome_score': scores.get('final', 0),
        'centrosome_evidence_score': scores.get('Centrosome evidence', 0) or scores.get('中心体证据', 0),
        'te_relevance_score': 0,  # Deprecated, always 0
        'pubmed_score': scores.get('PubMed/literature', 0) or scores.get('文献/PubMed', 0) or scores.get('PubMed', 0) or 0,
        'ppi_score': scores.get('PPI/network', 0) or scores.get('PPI/互作网络', 0) or scores.get('PPI', 0) or 0,
        'structure_domain_score': scores.get('Structure/domain', 0) or scores.get('结构/结构域', 0) or scores.get('Structure', 0) or 0,
        'novelty_specificity_score': scores.get('Novelty/specificity', 0) or scores.get('新颖性/特异性', 0) or scores.get('Novelty', 0) or 0,
        'source_centrosome': '$centro' in content,
        'source_centriolar_satellite': False,
        'source_both': False,
        'in_main_atlas': 'Main atlas overlap: Yes' in content,
        'main_status': '',
        'main_category': '',
        'report_path': path,
        'docs_report_path': f"docs/centrosome/reports/{gene}.html",
        'has_hpa_seed': has_hpa,
        'has_pubmed': pubmed_total > 0,
        'has_ppi_humanppi': 'STRING' in content or 'IntAct' in content,
        'has_structure_domain': 'AlphaFold' in content or 'pLDDT' in content,
        'manual_review': 'MANUAL_REVIEW' in status,
    }


def main():
    base = "centrosome/detail"
    reports = []

    for gene_dir in sorted(os.listdir(base)):
        dir_path = os.path.join(base, gene_dir)
        if not os.path.isdir(dir_path):
            continue
        md_path = os.path.join(dir_path, f"{gene_dir}-centrosome-evaluation.md")
        if os.path.exists(md_path):
            try:
                report = parse_evaluation(md_path)
                reports.append(report)
                print(f"  Parsed: {gene_dir} → score={report['final_centrosome_score']}")
            except Exception as e:
                print(f"  ERROR parsing {gene_dir}: {e}")

    if not reports:
        print("No reports found!")
        return

    # Sort by score descending
    reports.sort(key=lambda r: r['final_centrosome_score'], reverse=True)

    # Write TSV
    fields = [
        'gene', 'protein_full_name', 'uniprot_id', 'status', 'final_centrosome_score',
        'centrosome_evidence_score', 'pubmed_score', 'ppi_score',
        'structure_domain_score', 'novelty_specificity_score',
        'pubmed_strict_count', 'pubmed_broad_count', 'pubmed_display_count',
        'source_centrosome', 'source_centriolar_satellite', 'source_both',
        'hpa_location_text', 'has_if_image', 'has_hpa_image_url',
        'has_string_ppi', 'ppi_status', 'has_structure_domain',
        'in_main_atlas', 'main_status', 'main_category',
        'report_path', 'docs_report_path', 'has_hpa_seed', 'has_pubmed',
        'has_ppi_humanppi', 'has_structure_domain', 'manual_review',
        'te_relevance_score'  # deprecated, always 0
    ]

    os.makedirs("centrosome/data", exist_ok=True)
    os.makedirs("docs/centrosome/data", exist_ok=True)

    # TSV
    with open("centrosome/data/centrosome_report_index.tsv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(reports)
    print(f"  TSV: centrosome/data/centrosome_report_index.tsv ({len(reports)} records)")

    # CSV
    with open("centrosome/data/centrosome_report_index.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(reports)
    print(f"  CSV: centrosome/data/centrosome_report_index.csv ({len(reports)} records)")

    # JSON
    index_data = {
        "metadata": {
            "module": "centrosome",
            "generated_at": datetime.now().isoformat(),
            "total_reports": len(reports),
            "independent": True,
            "not_in_main_atlas_count": True
        },
        "records": reports
    }

    json_str = json.dumps(index_data, indent=2, ensure_ascii=False)

    # --- Post-processing: enrich with external data ---
    # Load PubMed prescreen data
    pubmed_data = {}
    prescreen_path = "centrosome/data/pubmed_prescreen_results.json"
    if os.path.exists(prescreen_path):
        with open(prescreen_path) as f:
            ps = json.load(f)
        for g, r in ps.get('results', {}).items():
            pubmed_data[g] = r.get('pubmed_total', -1)
    # Pilot PubMed overrides
    pilot_pubmed = {'AURKA':3081,'PLK4':591,'CEP192':101,'NEDD1':79,'CETN2':111,
                    'PCM1':367,'CCP110':77,'CCDC14':7,'CEP72':70,'CEP97':43,
                    'ANP32D':7,'PIK3C2G':57,'PRKAR2B':172,'SDCCAG8':73,'ZNF322':15}
    pubmed_data.update(pilot_pubmed)

    # Load HPA gene descriptions for protein names
    gene_desc = {}
    for hpa_file in ['/tmp/hpa_centrosome.json', '/tmp/hpa_satellite.json']:
        if os.path.exists(hpa_file):
            with open(hpa_file) as f:
                for item in json.load(f):
                    g = item.get('Gene','')
                    if g: gene_desc[g] = item.get('Gene description','')

    for r in reports:
        g = r['gene']
        pm = pubmed_data.get(g)
        r['pubmed_strict_count'] = pm if pm is not None and pm >= 0 else None
        r['pubmed_broad_count'] = pm if pm is not None and pm >= 0 else None
        r['pubmed_display_count'] = pm if pm is not None and pm >= 0 else None
        r['protein_full_name'] = gene_desc.get(g, '')
        r['uniprot_id'] = ''

    # Enzyme lookup from HPA Protein class
    enzyme_genes = set()
    for hpa_file in ['/tmp/hpa_centrosome.json', '/tmp/hpa_satellite.json']:
        if os.path.exists(hpa_file):
            with open(hpa_file) as f:
                for item in json.load(f):
                    pc = item.get('Protein class', [])
                    if any('enzyme' in c.lower() for c in pc):
                        enzyme_genes.add(item.get('Gene', ''))
    for r in reports:
        r['is_enzyme'] = r['gene'] in enzyme_genes

    # Re-serialize
    json_str = json.dumps(index_data, indent=2, ensure_ascii=False)

    with open("centrosome/data/centrosome_report_index.json", 'w') as f:
        f.write(json_str)
    with open("docs/centrosome/data/centrosome_report_index.json", 'w') as f:
        f.write(json_str)
    print(f"  JSON: centrosome/data/centrosome_report_index.json ({len(reports)} records)")
    print(f"  JSON: docs/centrosome/data/centrosome_report_index.json ({len(reports)} records)")

    print("Done.")


if __name__ == "__main__":
    main()
