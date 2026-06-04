#!/usr/bin/env python3
"""Batch query PubMed for all 34 proteins."""
import subprocess, json, time

GENES = "CCDC174 CSRNP3 CYB561A3 CCDC82 CSRNP2 CCDC85C CPNE4 CARNMT1 CRAMP1 CABLES2 CWC15 CCDC86 CGRRF1 CREBL2 CENPP COLGALT2 CAMTA2 CSTF1 COMMD10 CCDC92 CWC27 COMMD3 CEBPZ CRIPT CHML CSTF3 CHMP7 CYREN CRIP2 CSRNP1 C12orf43 CREB3L4 CBFA2T2 COG5".split()

results = {}
for gene in GENES:
    # Search using gene name in title/abstract
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=5&sort=relevance&term=%22{gene}%22%5BTitle/Abstract%5D+AND+(protein%5BTitle/Abstract%5D+OR+gene%5BTitle/Abstract%5D)'
    try:
        r = subprocess.run(["curl", "-sk", url], capture_output=True, text=True, timeout=15)
        data = json.loads(r.stdout)
        count = int(data.get("esearchresult", {}).get("count", 0))
        pmids = data.get("esearchresult", {}).get("idlist", [])
        results[gene] = {"count": count, "top_pmids": pmids}
        print(f"{gene}: PubMed={count}")
    except Exception as e:
        results[gene] = {"count": -1, "error": str(e)}
        print(f"{gene}: ERROR: {e}")
    time.sleep(0.3)  # Be nice to NCBI

# Write results
with open("/tmp/pubmed_results.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nDone. {len(results)} genes queried.")
