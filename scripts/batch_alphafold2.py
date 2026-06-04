#!/usr/bin/env python3
"""Batch query AlphaFold API v2 - extracts pLDDT metrics from summary endpoint."""
import subprocess, json, time, os, sys

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

BASE_DIR = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"

for gene, acc in GENE_ACC.items():
    try:
        url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{acc}"
        r = subprocess.run(["curl", "-skL", "--max-time", "30", url], capture_output=True, text=True, timeout=30)
        if r.returncode != 0 or not r.stdout.strip():
            print(f"AF {gene} ({acc}): no response")
            continue
        data = json.loads(r.stdout)
        entries = data if isinstance(data, list) else [data]
        if not entries:
            print(f"AF {gene} ({acc}): empty")
            continue
        entry = entries[0]
        avg_plddt = entry.get("globalMetricValue", 0)
        vlow = entry.get("fractionPlddtVeryLow", 0)
        low = entry.get("fractionPlddtLow", 0)
        conf = entry.get("fractionPlddtConfident", 0)
        vhigh = entry.get("fractionPlddtVeryHigh", 0)
        model_id = entry.get("modelEntityId", "")

        plddt_above70 = (conf + vhigh) * 100
        plddt_above90 = vhigh * 100
        plddt_below50 = vlow * 100

        print(f"AF {gene} ({acc}): avg_pLDDT={avg_plddt:.1f}, >70={plddt_above70:.1f}%, >90={plddt_above90:.1f}%, <50={plddt_below50:.1f}%")

        # Download PDB and PAE PNG
        gene_dir = None
        for subdir in ["nucleoplasm", "nucleolus", "chromatin", "nuclear-speckle", "nucleus-cytoplasm", "nuclear-envelope", "rejected"]:
            d = os.path.join(BASE_DIR, subdir, gene)
            if os.path.exists(d):
                gene_dir = d
                break

        if gene_dir:
            # Download PDB
            pdb_url = f"https://alphafold.ebi.ac.uk/files/{model_id}.pdb"
            pdb_path = os.path.join(gene_dir, f"{gene}-alphafold.pdb")
            if not os.path.exists(pdb_path):
                subprocess.run(["curl", "-skL", "--max-time", "30", pdb_url, "-o", pdb_path], capture_output=True, timeout=30)

            # Download PAE PNG
            pae_png_url = f"https://alphafold.ebi.ac.uk/files/{model_id}-predicted_aligned_error_v4.png"
            pae_png_path = os.path.join(gene_dir, f"{gene}-PAE.png")
            if not os.path.exists(pae_png_path):
                subprocess.run(["curl", "-skL", "--max-time", "30", pae_png_url, "-o", pae_png_path], capture_output=True, timeout=30)

            # Download pLDDT JSON
            plddt_url = f"https://alphafold.ebi.ac.uk/files/{model_id}-confidence_v4.json"
            plddt_path = os.path.join(gene_dir, f"{gene}-plddt.json")
            if not os.path.exists(plddt_path):
                subprocess.run(["curl", "-skL", "--max-time", "30", plddt_url, "-o", plddt_path], capture_output=True, timeout=30)

            # Save AF data for later use
            af_data = {
                "avg_plddt": avg_plddt,
                "plddt_above70": plddt_above70,
                "plddt_above90": plddt_above90,
                "plddt_below50": plddt_below50,
                "model_id": model_id,
                "version": entry.get("latestVersion", ""),
            }
            af_path = os.path.join(gene_dir, f"{gene}-af_data.json")
            with open(af_path, "w") as f:
                json.dump(af_data, f)
            print(f"  Downloaded: PDB, PAE PNG, pLDDT JSON to {gene_dir}")
        else:
            print(f"  WARNING: no directory found for {gene}")

    except Exception as e:
        print(f"AF {gene} ({acc}): ERROR: {e}")
    time.sleep(0.1)
print("\nDone.")
