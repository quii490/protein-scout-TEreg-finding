#!/usr/bin/env python3
"""Download AlphaFold PAE/pLDDT/PDB and Protein Atlas IF images for D proteins."""
import json, os, sys, urllib.request, glob, time

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

# UniProt accession -> gene mapping for nuclear D proteins
NUCLEAR_PROTEINS = {
    "Q96MA1": "DMRTB1",
    "Q6ZNG2": "DBX2",
    "Q5VZB9": "DMRTA1",
    "M0R2D7": "DMRTC2",
    "Q5W0Z5": "DMRT3",
    "F2Z2A4": "DNTTIP1",
    "Q96NX9": "DACH2",
    "H0YN79": "DET1",
    "A0A1W2PPF3": "DUXB",
    "Q8NFW5": "DMBX1",
    "A6NNA5": "DRGX",
    "B7ZLH1": "DMRTA2",
    "A6NLW8": "DUXA",
    "Q4G1A1": "DSN1",
    "Q9C005": "DPY30",
    "Q9BTC0": "DIDO1",
    "Q5TG40": "DMAP1",
    "E9PNC7": "DRAP1",
    "Q9BVC3": "DSCC1",
    "Q9UK59": "DBR1",
    "Q14182": "DNTT",
    "E9PL61": "DEPDC1",
    "A6NMT0": "DBX1",
    "F8WD19": "DONSON",
    "F8WC68": "DXO",
    "M0QYW5": "DAPK3",
    "Q6P2H0": "DTX2",
    "E9PBY2": "DAZ2",
    "Q5IRM7": "DAZAP1",
    "A0A8V8TNX4": "DEF6",
    "I3L1H5": "DPH1",
    "A8MZF9": "DRG2",
    "Q6P1R4": "DUS1L",
}

def download_file(url, path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            if len(data) < 100:
                return False, f"too small ({len(data)} bytes)"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(data)
            return True, f"OK ({len(data)} bytes)"
    except Exception as e:
        return False, str(e)

def main():
    # Check which proteins already have AlphaFold data
    for acc, gene in NUCLEAR_PROTEINS.items():
        # Find report location
        for root, dirs, files in os.walk(DETAIL):
            if os.path.basename(root) == gene and f"{gene}-evaluation.md" in files:
                out_dir = root
                break
        else:
            print(f"SKIP {gene}: report not found", file=sys.stderr)
            continue

        # Download AlphaFold data
        pae_png = os.path.join(out_dir, f"{gene}-PAE.png")
        pdb_file = os.path.join(out_dir, f"{gene}-alphafold.pdb")
        plddt_file = os.path.join(out_dir, f"{gene}-plddt.json")

        # Check if already done
        if os.path.exists(pae_png) and os.path.getsize(pae_png) > 500:
            print(f"{gene}: PAE already exists")
        else:
            pae_url = f"https://alphafold.ebi.ac.uk/files/AF-{acc}-F1-predicted_aligned_error_v4.png"
            ok, msg = download_file(pae_url, pae_png)
            print(f"{gene}: PAE download: {msg}")

        if os.path.exists(pdb_file) and os.path.getsize(pdb_file) > 1000:
            print(f"{gene}: PDB already exists")
        else:
            pdb_url = f"https://alphafold.ebi.ac.uk/files/AF-{acc}-F1-model_v4.pdb"
            ok, msg = download_file(pdb_url, pdb_file)
            print(f"{gene}: PDB download: {msg}")

        if os.path.exists(plddt_file) and os.path.getsize(plddt_file) > 100:
            print(f"{gene}: pLDDT already exists")
        else:
            # Fetch pLDDT from API
            try:
                url = f"https://alphafold.ebi.ac.uk/api/prediction/{acc}"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode())
                if isinstance(data, list) and len(data) > 0:
                    data = data[0]
                plddt = data.get("plddt", []) if isinstance(data, dict) else []
                if plddt:
                    with open(plddt_file, 'w') as f:
                        json.dump({"plddt": plddt, "mean": round(sum(plddt)/len(plddt), 1)}, f)
                    print(f"{gene}: pLDDT saved (mean={round(sum(plddt)/len(plddt),1)})")
                else:
                    print(f"{gene}: no pLDDT in AlphaFold API")
            except Exception as e:
                print(f"{gene}: pLDDT fetch failed: {e}")

        time.sleep(0.3)

    # Download Protein Atlas IF images
    print("\n=== Protein Atlas IF images ===", file=sys.stderr)
    for acc, gene in list(NUCLEAR_PROTEINS.items())[:15]:  # Top 15 first
        for root, dirs, files in os.walk(DETAIL):
            if os.path.basename(root) == gene:
                if_dir = os.path.join(root, "IF_images")
                existing = glob.glob(os.path.join(if_dir, "*.jpg")) if os.path.exists(if_dir) else []
                if existing:
                    print(f"{gene}: IF images already exist ({len(existing)})")
                    break

                os.makedirs(if_dir, exist_ok=True)

                # Try HPA API for IF images
                try:
                    # Search HPA for the gene
                    url = f"https://www.proteinatlas.org/search/{gene}?format=json"
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        hpa_data = json.loads(resp.read().decode())

                    # Look for IF images
                    img_count = 0
                    for item in hpa_data[:5]:
                        ensg = item.get("Ensembl", "")
                        if not ensg: continue

                        # Try to get subcellular data
                        sub_url = f"https://www.proteinatlas.org/{ensg}.json"
                        try:
                            req2 = urllib.request.Request(sub_url, headers={"User-Agent": "Mozilla/5.0"})
                            with urllib.request.urlopen(req2, timeout=30) as resp2:
                                sub_data = json.loads(resp2.read().decode())
                        except:
                            continue

                        # Look for IF images in subcellular data
                        antibodies = sub_data.get("antibodies", [])
                        for ab in antibodies:
                            for cell_line_data in ab.get("cell_lines", [])[:2]:
                                img_url = cell_line_data.get("image", "")
                                cell_name = cell_line_data.get("cell_line", "unknown")
                                if img_url and img_count < 2:
                                    safe_name = cell_name.replace(" ", "_").replace("/", "_")
                                    fname = f"{safe_name}.jpg"
                                    fpath = os.path.join(if_dir, fname)
                                    ok, msg = download_file(img_url, fpath)
                                    if ok:
                                        img_count += 1
                                        print(f"{gene}: IF downloaded {fname}")
                            if img_count >= 2:
                                break
                    if img_count == 0:
                        print(f"{gene}: no IF images found in HPA")
                except Exception as e:
                    print(f"{gene}: HPA query failed: {e}")
                break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
