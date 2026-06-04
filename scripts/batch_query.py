#!/usr/bin/env python3
"""Batch query all data sources for protein evaluation."""
import sys, json, urllib.request, urllib.error, time, os

def ufetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())

def query_all(gene, pubmed_count):
    result = {"gene": gene, "pubmed_count": pubmed_count}

    # ===== UniProt =====
    # Try to find the longest reviewed/TrEMBL entry
    try:
        url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606&format=json&size=5&fields=accession,protein_name,length,cc_subcellular_location,go,ft_domain,structure_3d,gene_names,cc_interaction,cc_function,reviewed"
        data = ufetch(url, 40)
        results = data.get("results", [])
        # Prefer reviewed, then longest
        if results:
            reviewed = [r for r in results if r.get("entryType") == "Swiss-Prot"]
            all_sorted = sorted(results, key=lambda x: x.get("sequence", {}).get("length", 0), reverse=True)
            best = reviewed[0] if reviewed else all_sorted[0] if all_sorted else results[0]
            acc = best.get("primaryAccession", "?")
            name = best.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "")
            if not name:
                name = best.get("proteinDescription", {}).get("submissionNames", [{}])[0].get("fullName", {}).get("value", "")
            length = best.get("sequence", {}).get("length", 0)
            reviewed_flag = best.get("entryType", "") == "Swiss-Prot"

            locs = []
            for c in best.get("comments", []):
                if c.get("commentType") == "SUBCELLULAR LOCATION":
                    for sub in c.get("subcellularLocations", []):
                        locs.append(sub.get("location", {}).get("value", ""))

            funcs = []
            for c in best.get("comments", []):
                if c.get("commentType") == "FUNCTION":
                    for t in c.get("texts", []):
                        funcs.append(t.get("value", "")[:200])

            goc = []
            gocc = []
            for g in best.get("crossReferences", []):
                if g.get("database") == "GO":
                    for p in g.get("properties", []):
                        if p.get("key") == "GoTerm" and "C:" in p.get("value", ""):
                            gocc.append(p["value"].split("C:")[1])

            domains = []
            for f in best.get("features", []):
                if f.get("type") in ("DOMAIN", "DNA_BIND", "ZN_FING", "REGION"):
                    desc = f.get("description", "")
                    loc_str = f"({f.get('location',{}).get('start',{}).get('value','')}-{f.get('location',{}).get('end',{}).get('value','')})"
                    domains.append(f"{desc}{loc_str}")

            pdbs = [x.get("id", "") for x in best.get("uniProtKBCrossReferences", []) if x.get("database") == "PDB"]

            genes = [g.get("geneName", {}).get("value", "") for g in best.get("genes", [])]

            result["uniprot"] = {
                "acc": acc, "name": name, "len": length, "reviewed": reviewed_flag,
                "locs": locs, "gocc": gocc, "domains": domains, "pdbs": pdbs,
                "genes": genes, "funcs": funcs, "raw_name": name
            }
        else:
            result["uniprot"] = {"error": "no results", "locs": [], "gocc": [], "domains": [], "pdbs": [], "len": 0}
    except Exception as e:
        result["uniprot"] = {"error": str(e), "locs": [], "gocc": [], "domains": [], "pdbs": [], "len": 0}

    # ===== Novelty scoring =====
    if pubmed_count <= 20:
        result["novelty_score"] = 10
        result["novelty_label"] = "极度新颖"
    elif pubmed_count <= 50:
        result["novelty_score"] = 8
        result["novelty_label"] = "非常新颖"
    elif pubmed_count <= 100:
        result["novelty_score"] = 6
        result["novelty_label"] = "有一定研究"
    else:
        result["novelty_score"] = 0
        result["novelty_label"] = "淘汰"

    # ===== STRING =====
    try:
        url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=25"
        data = ufetch(url, 30)
        ppis = []
        for item in data:
            ppis.append({
                "partner": item.get("preferredName_B", ""),
                "score": float(item.get("combined_score", 0)),
                "exp": float(item.get("experimentally_determined_interaction", 0)),
                "database_score": float(item.get("database_annotated", 0)),
                "textmining": float(item.get("textmining", 0)),
                "coexpression": float(item.get("coexpression", 0))
            })
        result["string"] = ppis
    except Exception as e:
        result["string"] = []

    # ===== IntAct =====
    try:
        url = f"http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode()
        intact = []
        for line in text.strip().split('\n'):
            if not line.strip(): continue
            parts = line.split('\t')
            if len(parts) >= 15:
                intact.append({
                    "a": parts[0] if len(parts) > 0 else "",
                    "b": parts[1] if len(parts) > 1 else "",
                    "method": parts[6] if len(parts) > 6 else "",
                    "type": parts[8] if len(parts) > 8 else "",
                    "pmid": parts[15] if len(parts) > 15 else "",
                })
        result["intact"] = intact[:30]
    except Exception as e:
        result["intact"] = []

    # ===== AlphaFold =====
    af_acc = result.get("uniprot", {}).get("acc", "")
    if af_acc:
        try:
            url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{af_acc}"
            data = ufetch(url, 40)
            af_data = data[0] if isinstance(data, list) and len(data) > 0 else data
            plddt = af_data.get("plddt", []) if isinstance(af_data, dict) else []
            pae = af_data.get("paeDocUrl", "") if isinstance(af_data, dict) else ""
            result["alphafold"] = {
                "entry_id": af_data.get("entryId", "") if isinstance(af_data, dict) else "",
                "plddt_len": len(plddt),
                "plddt_mean": round(sum(plddt)/len(plddt), 1) if plddt else None,
                "plddt_gt70": round(sum(1 for p in plddt if p > 70) / max(len(plddt),1) * 100, 1) if plddt else None,
                "plddt_gt90": round(sum(1 for p in plddt if p > 90) / max(len(plddt),1) * 100, 1) if plddt else None,
                "pae_url": pae,
            }
        except Exception as e:
            result["alphafold"] = {"error": str(e)}
    else:
        result["alphafold"] = {"error": "no uniprot acc"}

    return result

if __name__ == "__main__":
    # Process all D proteins
    proteins = [
        ("DUS1L", 2), ("DENND4A", 3), ("DRICH1", 3), ("DEPDC7", 6),
        ("DMRTB1", 14), ("DCTN3", 15), ("DUXB", 15), ("DENND2D", 15),
        ("DPH5", 15), ("DMRTA1", 17), ("DBX2", 17), ("DMRTC2", 18),
        ("DNTTIP1", 23), ("DSCC1", 24), ("DAZ2", 28), ("DMBX1", 29),
        ("DENND1B", 30), ("DYNC1LI1", 30), ("DUXA", 33), ("DMRTA2", 33),
        ("DSN1", 33), ("DACH2", 34), ("DRAP1", 37), ("DOCK10", 38),
        ("DRGX", 38), ("DDIT4L", 39), ("DET1", 42), ("DIP2C", 42),
        ("DIDO1", 45), ("DONSON", 46), ("DMRT3", 47), ("DPH1", 52),
        ("DMAP1", 53), ("DNTT", 53), ("DRG2", 55), ("DBR1", 59),
        ("DEF6", 61), ("DXO", 67), ("DAZAP1", 69), ("DTX2", 82),
        ("DBX1", 84), ("DAPK3", 92), ("DPY30", 95), ("DEPDC1", 99),
    ]

    results = {}
    for i, (gene, pubmed) in enumerate(proteins):
        print(f"[{i+1}/44] Querying {gene} (PubMed={pubmed})...", file=sys.stderr)
        try:
            r = query_all(gene, pubmed)
            results[gene] = r
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            results[gene] = {"gene": gene, "error": str(e)}
        time.sleep(0.3)  # rate limit

    print(json.dumps(results, indent=2, ensure_ascii=False))
