#!/usr/bin/env python3
"""Batch query IntAct for all 34 proteins."""
import subprocess, json, time, re

GENES = "CCDC174 CSRNP3 CYB561A3 CCDC82 CSRNP2 CCDC85C CPNE4 CARNMT1 CRAMP1 CABLES2 CWC15 CCDC86 CGRRF1 CREBL2 CENPP COLGALT2 CAMTA2 CSTF1 COMMD10 CCDC92 CWC27 COMMD3 CEBPZ CRIPT CHML CSTF3 CHMP7 CYREN CRIP2 CSRNP1 C12orf43 CREB3L4 CBFA2T2 COG5".split()

for gene in GENES:
    url = f"http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27"
    try:
        r = subprocess.run(["curl", "-sk", "--max-time", "20", url], capture_output=True, text=True, timeout=20)
        lines = r.stdout.strip().split('\n')
        interactions = []
        for line in lines:
            if not line.strip() or line.startswith('#'):
                continue
            cols = line.split('\t')
            if len(cols) >= 15:
                interactions.append({
                    "partner_a": cols[4] if len(cols) > 4 else '',
                    "partner_b": cols[5] if len(cols) > 5 else '',
                    "method": cols[6] if len(cols) > 6 else '',
                    "pmid": cols[8] if len(cols) > 8 else '',
                    "type": cols[11] if len(cols) > 11 else '',
                })
        with open(f"/tmp/intact_{gene}.json", "w") as f:
            json.dump(interactions, f, indent=2)
        phys = [x for x in interactions if 'physical association' in x.get('type', '') or 'direct interaction' in x.get('type', '')]
        print(f"IntAct {gene}: {len(interactions)} total, {len(phys)} physical")
    except Exception as e:
        print(f"IntAct {gene}: ERROR: {e}")
        with open(f"/tmp/intact_{gene}.json", "w") as f:
            json.dump({"error": str(e)}, f)
    time.sleep(0.3)
print("\nDone.")
