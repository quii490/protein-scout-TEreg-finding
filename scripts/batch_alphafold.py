#!/usr/bin/env python3
"""Batch query AlphaFold API for all 34 proteins. Downloads pLDDT JSON."""
import subprocess, json, os, time

# Gene -> UniProt ACC mapping from earlier batch
GENE_ACC = {
    "CCDC174": "Q6PII3", "CSRNP3": "Q8WYN3", "CYB561A3": "Q8NBI2",
    "CCDC82": "Q8N4S0", "CSRNP2": "Q9H175", "CCDC85C": "A6NKD9",
    "CPNE4": "Q96A23", "CARNMT1": "Q8N4J0", "CRAMP1": "Q96RY5",
    "CABLES2": "Q9BTV7", "CWC15": "Q9P013", "CCDC86": "Q9H6F5",
    "CGRRF1": "Q99675", "CREBL2": "O60519", "CENPP": "Q6IPU0",
    "COLGALT2": "Q8IYK4", "CAMTA2": "O94983", "CSTF1": "Q05048",
    "COMMD10": "Q9Y6G5", "CCDC92": "Q53HC0", "CWC27": "Q6UX04",
    "COMMD3": "Q9UBI1", "CEBPZ": "Q03701", "CRIPT": "Q9P021",
    "CHML": "P26374", "CSTF3": "Q12996", "CHMP7": "Q8WUX9",
    "CYREN": "Q9BWK5", "CRIP2": "P52943", "CSRNP1": "Q96S65",
    "C12orf43": "Q96C57", "CREB3L4": "Q8TEY5", "CBFA2T2": "O43439",
    "COG5": "Q9UP83",
}

for gene, acc in GENE_ACC.items():
    try:
        url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{acc}"
        r = subprocess.run(["curl", "-skL", "--max-time", "30", url], capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and r.stdout.strip():
            data = json.loads(r.stdout)
            # Save full response
            with open(f"/tmp/af_{gene}.json", "w") as f:
                json.dump(data, f, indent=2)
            # Extract key metrics
            # Check if it's an array (multiple entries)
            entries = data if isinstance(data, list) else [data]
            entry = entries[0] if entries else {}
            plddt_str = entry.get("pLDDT", "")
            if plddt_str:
                import numpy as np
                plddt_vals = json.loads(plddt_str) if isinstance(plddt_str, str) else plddt_str
                avg = sum(plddt_vals) / len(plddt_vals)
                above70 = sum(1 for x in plddt_vals if x > 70) / len(plddt_vals) * 100
                above90 = sum(1 for x in plddt_vals if x > 90) / len(plddt_vals) * 100
                below50 = sum(1 for x in plddt_vals if x < 50) / len(plddt_vals) * 100
                print(f"AF {gene} ({acc}): len={len(plddt_vals)}, avg_pLDDT={avg:.1f}, >70={above70:.1f}%, >90={above90:.1f}%, <50={below50:.1f}%")
            else:
                print(f"AF {gene} ({acc}): no pLDDT data, keys={list(entry.keys())[:5]}")
        else:
            print(f"AF {gene} ({acc}): empty response or error")
    except Exception as e:
        print(f"AF {gene} ({acc}): ERROR: {e}")
    time.sleep(0.2)
print("\nDone.")
