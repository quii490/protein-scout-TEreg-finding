#!/usr/bin/env python3
"""Query UniProt for a list of genes and output structured info."""
import sys, json, urllib.request, urllib.error

def query_uniprot(gene):
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606&format=json&size=1&fields=accession,protein_name,length,sequence,cc_subcellular_location,go,ft_domain,structure_3d,gene_names,cc_interaction"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        return f"NOT_FOUND:{e}"

    if not data.get("results"):
        return "NOT_FOUND:no results"

    r = data["results"][0]
    acc = r.get("primaryAccession", "?")
    name = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "?")
    length = r.get("sequence", {}).get("length", "?")

    genes = [g.get("geneName", {}).get("value", "?") for g in r.get("genes", [])]

    locs = []
    for c in r.get("comments", []):
        if c.get("commentType") == "SUBCELLULAR LOCATION":
            for sub in c.get("subcellularLocations", []):
                locs.append(sub.get("location", {}).get("value", "?"))

    goc = []
    for g in r.get("crossReferences", []):
        if g.get("database") == "GO":
            for p in g.get("properties", []):
                if p.get("key") == "GoTerm" and "C:" in p.get("value", ""):
                    goc.append(p["value"].split("C:")[1])

    domains = []
    for f in r.get("features", []):
        if f.get("type") == "DOMAIN":
            domains.append(f.get("description", "?"))

    pdbs = [x.get("id", "") for x in r.get("uniProtKBCrossReferences", []) if x.get("database") == "PDB"]

    interactions = []
    for c2 in r.get("comments", []):
        if c2.get("commentType") == "INTERACTION":
            for inter in c2.get("interactions", []):
                i1 = inter.get("interactantOne", {}).get("uniProtKBAccession", "")
                i2 = inter.get("interactantTwo", {}).get("uniProtKBAccession", "")
                interactions.append(f"{i1}-{i2}")

    print(f"{gene}|ACC:{acc}|NAME:{name}|LEN:{length}|GENES:{';'.join(genes)}")
    print(f"{gene}|LOCS:{';'.join(locs)}")
    print(f"{gene}|GOC:{';'.join(goc[:8])}")
    print(f"{gene}|DOMS:{';'.join(domains[:10])}")
    print(f"{gene}|PDBS:{';'.join(pdbs[:8])}")
    print(f"{gene}|INTER:{';'.join(interactions[:5])}")
    print(f"---END---")
    return acc

if __name__ == "__main__":
    genes = sys.argv[1:] if len(sys.argv) > 1 else []
    if not genes:
        genes = ["DUS1L"]
    for gene in genes:
        query_uniprot(gene)
