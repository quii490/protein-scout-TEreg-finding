#!/usr/bin/env python3
"""Batch query STRING for all 34 proteins."""
import subprocess, json, time

GENES = "CCDC174 CSRNP3 CYB561A3 CCDC82 CSRNP2 CCDC85C CPNE4 CARNMT1 CRAMP1 CABLES2 CWC15 CCDC86 CGRRF1 CREBL2 CENPP COLGALT2 CAMTA2 CSTF1 COMMD10 CCDC92 CWC27 COMMD3 CEBPZ CRIPT CHML CSTF3 CHMP7 CYREN CRIP2 CSRNP1 C12orf43 CREB3L4 CBFA2T2 COG5".split()

for gene in GENES:
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=30"
    try:
        r = subprocess.run(["curl", "-sk", url], capture_output=True, text=True, timeout=15)
        data = json.loads(r.stdout)
        out = []
        for item in data:
            if isinstance(item, dict):
                out.append({
                    "partner": item.get("preferredName_B", item.get("stringId_B", "?")),
                    "score": item.get("score", 0),
                    "exp": item.get("experiments", 0),
                    "db": item.get("database", 0),
                    "text": item.get("textmining", 0),
                    "coexp": item.get("coexpression", 0),
                })
        with open(f"/tmp/string_{gene}.json", "w") as f:
            json.dump(out, f, indent=2)
        print(f"STRING {gene}: {len(out)} partners")
    except Exception as e:
        print(f"STRING {gene}: ERROR: {e}")
    time.sleep(0.2)
print("\nDone.")
