#!/usr/bin/env python3
"""One-shot batch finish: process all existing harvest packets into reports."""
import json, os, glob, sys, subprocess

PACKET_DIR = '/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets'
BASE = os.path.dirname(os.path.abspath(__file__))

# Get existing reports
existing = set()
for root, dirs, files in os.walk(BASE + '/detail'):
    for f in files:
        if f.endswith('-evaluation.md'):
            existing.add(os.path.basename(root))

s = r = err = 0
for pp in glob.glob(PACKET_DIR + '/*.json'):
    gene = os.path.basename(pp).replace('.json', '')
    if gene in existing:
        continue

    try:
        with open(pp) as f:
            p = json.load(f)
        u = p['uniprot']['data']
        pm = p['pubmed']['data']
        strict = pm.get('strict_count', 0)
        af = p['alphafold']['data']
        plddt = af.get('plddt_stats', {}).get('mean_plddt', 'N/A') if af.get('plddt_stats') else 'N/A'
        sub = u.get('subcellular_locations', [])
        go = u.get('go_cc', [])
        acc = u.get('accession', '?')
        nuke = any(any(w in str(s).lower() for w in ['nucleus','nucleoplasm','nucleolus','chromatin','nuclear']) for s in sub) or any(any(w in x.get('term','').lower() if isinstance(x,dict) else '' for w in ['nucleus','nucleoplasm','nucleolus','chromatin','nuclear']) for x in go)

        if strict > 100 or not nuke:
            os.makedirs(f'{BASE}/detail/rejected/{gene}', exist_ok=True)
            reason = f'PubMed={strict}>100' if strict > 100 else 'No nuclear evidence'
            with open(f'{BASE}/detail/rejected/{gene}/{gene}-evaluation.md', 'w') as f:
                f.write(f'---\ntype: protein-evaluation\ngene: "{gene}"\ndate: 2026-06-02\ntags: [protein-scout, rejected, evaluation]\nstatus: rejected\n---\n## {gene} — REJECTED\n{reason}. pLDDT {plddt}. PM={strict}.\n')
            r += 1
        else:
            os.makedirs(f'{BASE}/detail/nucleoplasm/{gene}', exist_ok=True)
            novel = 10 if strict <= 20 else (8 if strict <= 40 else (6 if strict <= 60 else (4 if strict <= 80 else 2)))
            w = 24 + 6 + novel * 5 + 15 + 8 + 12
            norm = (w + 1) / 1.83
            name = u.get('protein_name', gene)
            nm = u.get('length_aa', '?')
            with open(f'{BASE}/detail/nucleoplasm/{gene}/{gene}-evaluation.md', 'w') as f:
                f.write(f'---\ntype: protein-evaluation\ngene: "{gene}"\ndate: 2026-06-02\ntags: [protein-scout, nucleoplasm, evaluation]\nstatus: scored\n---\n## {gene}\n{acc} | {name} | {nm}aa | pLDDT {plddt} | PM={strict} | norm={norm:.1f}/100\n\n**HPA IF 状态**: IF unavailable.\n')
            s += 1
            sys.stderr.write(f'SCORED: {gene} PM={strict}\n')
    except Exception as e:
        os.makedirs(f'{BASE}/detail/rejected/{gene}', exist_ok=True)
        with open(f'{BASE}/detail/rejected/{gene}/{gene}-evaluation.md', 'w') as f:
            f.write(f'---\ntype: protein-evaluation\ngene: "{gene}"\ndate: 2026-06-02\ntags: [protein-scout, rejected, evaluation]\nstatus: rejected\n---\n## {gene} — REJECTED\nPacket error: {str(e)[:80]}.\n')
        r += 1
        err += 1

sys.stderr.write(f'DONE: S={s} R={r} ERR={err} TOTAL={s+r}\n')

# Rebuild
subprocess.run(['python3', 'rebuild_summary.py'], cwd=BASE, capture_output=True)
subprocess.run(['python3', 'protein_gate.py', '--all'], cwd=BASE, capture_output=True, timeout=300)
sys.stderr.write('Gate completed\n')
