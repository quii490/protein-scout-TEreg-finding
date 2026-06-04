#!/usr/bin/env python3
"""Batch query UniProt for a list of genes. Outputs JSON per gene."""
import json, subprocess, sys

GENES = "CCDC174 CSRNP3 CYB561A3 CCDC82 CSRNP2 CCDC85C CPNE4 CARNMT1 CRAMP1 CABLES2 CWC15 CCDC86 CGRRF1 CREBL2 CENPP COLGALT2 CAMTA2 CSTF1 COMMD10 CCDC92 CWC27 COMMD3 CEBPZ CRIPT CHML CSTF3 CHMP7 CYREN CRIP2 CSRNP1 C12orf43 CREB3L4 CBFA2T2 COG5".split()

def fetch_gene(gene):
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606&format=json&fields=accession,length,protein_name,cc_subcellular_location,go_p,go_c,structure_3d,cc_interaction,gene_names"
    r = subprocess.run(["curl", "-sk", url], capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        return {"gene": gene, "error": f"curl failed: {r.stderr}"}
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"gene": gene, "error": "JSON parse error", "raw": r.stdout[:200]}
    results = data.get("results", [])
    if not results:
        return {"gene": gene, "error": "not found"}
    r = results[0]
    acc = r.get("primaryAccession", "")
    seq_len = r.get("sequence", {}).get("length", 0)
    name = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "")
    genes = []
    for g in r.get("genes", []):
        gn = g.get("geneName", {}).get("value", "")
        if gn:
            genes.append(gn)
    # Subcellular location
    subcell = []
    for c in r.get("comments", []):
        if c.get("commentType") == "SUBCELLULAR LOCATION":
            for loc in c.get("subcellularLocations", []):
                loc_text = loc.get("location", {}).get("value", "")
                if loc_text:
                    subcell.append(loc_text)
    # GO-CC
    go_cc = []
    for ref in r.get("uniProtKBCrossReferences", []):
        db = ref.get("database", "")
        if db == "GO":
            props = ref.get("properties", [])
            for p in props:
                v = p.get("value", "")
                if v.startswith("C:"):
                    go_cc.append(v)
    # PDB
    pdbs = []
    for ref in r.get("uniProtKBCrossReferences", []):
        if ref.get("database") == "PDB":
            pdbs.append(ref.get("id", ""))
    # Interactions
    interactions = []
    for c in r.get("comments", []):
        if c.get("commentType") == "INTERACTION":
            for i in c.get("interactions", []):
                p1 = i.get("interactantOne", {}).get("uniProtKBAccession", "")
                p2 = i.get("interactantTwo", {}).get("uniProtKBAccession", "")
                interactions.append(f"{p1}-{p2}")
    return {
        "gene": gene,
        "acc": acc,
        "length": seq_len,
        "name": name,
        "aliases": genes,
        "subcell": subcell,
        "go_cc": go_cc,
        "pdbs": pdbs,
        "interactions": interactions,
    }

# Fetch all sequentially to avoid rate limiting
for gene in GENES:
    result = fetch_gene(gene)
    # Write to file
    fname = f"/tmp/prot_{gene}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    print(f"OK: {gene} -> {result.get('acc', 'NOT_FOUND')} ({result.get('length', '?')} aa)")
    if result.get("acc"):
        print(f"  Subcell: {'; '.join(result['subcell'][:5]) or 'none'}")
        print(f"  PDBs: {result['pdbs']}")
        print(f"  GO-CC: {'; '.join(result['go_cc'][:5]) or 'none'}")
