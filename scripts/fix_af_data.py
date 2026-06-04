#!/usr/bin/env python3
"""Fix AlphaFold data collection and generate all 27 evaluation reports."""
import json, os, re, time, urllib.request, urllib.error, ssl, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

ctx = ssl.create_default_context()

def fetch_json(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except Exception as e:
            if attempt == retries - 1: return None
            time.sleep(2)

def fetch_text(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            if attempt == retries - 1: return None
            time.sleep(2)

def download_file(url, dest):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(resp.read())
            return True
    except: return False

# Load existing batch data
with open(os.path.join(BASE, "batch_all_data.json")) as f:
    batch_data = json.load(f)

# Fix AlphaFold data
print("Fixing AlphaFold data...")
for gene, info in batch_data.items():
    uniprot = info.get("uniprot", {})
    uid = uniprot.get("uniprot_id", "") if uniprot else ""
    if not uid:
        uid = next((v for k,v in {
            "C1D":"Q13901","CCDC137":"Q6PK04","CDAN1":"Q8IWY9","CDC14A":"Q9UNH5",
            "CENPH":"Q9H3R5","CENPI":"Q92674","CENPK":"Q9BS16","CENPM":"Q9NSP4",
            "CENPT":"Q96BT3","CENPU":"Q71F23","CENPX":"A8MT69","CHMP1A":"Q9HD42",
            "CHP2":"O43745","CLASP1":"Q7Z460","CLNS1A":"P54105","CRTC3":"Q6UUV7",
            "CSRP3":"P50461","CUTC":"Q9NTM9","CASC3":"O15234","CCAR1":"Q8IX12",
            "CDX4":"O14627","CEBPG":"P53567","CIPC":"Q9C0C6","CSRP1":"P21291",
            "CSRP2":"Q16527","CSTF2T":"Q9H0L4","CTNNBL1":"Q8WYA6"
        }.items() if k == gene), "")

    if not uid: continue

    url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{uid}"
    af = fetch_json(url)
    if not af or not isinstance(af, list) or len(af) == 0:
        info["alphafold"] = None
        continue

    d = af[0]

    # Get pLDDT data
    plddt_mean = d.get("globalMetricValue", 0)
    plddt_very_high = d.get("fractionPlddtVeryHigh", 0)
    plddt_confident = d.get("fractionPlddtConfident", 0)
    plddt_low = d.get("fractionPlddtLow", 0)
    plddt_very_low = d.get("fractionPlddtVeryLow", 0)

    info["alphafold"] = {
        "mean_plddt": round(plddt_mean, 1) if plddt_mean else 0,
        "plddt_very_high": plddt_very_high,
        "plddt_confident": plddt_confident,
        "plddt_low": plddt_low,
        "plddt_very_low": plddt_very_low,
        "pdb_url": d.get("pdbUrl", ""),
        "pae_image_url": d.get("paeImageUrl", ""),
        "plddt_doc_url": d.get("plddtDocUrl", ""),
        "pae_doc_url": d.get("paeDocUrl", ""),
        "version": d.get("latestVersion", 0),
    }
    print(f"  {gene}: pLDDT={plddt_mean}, vH={plddt_very_high}, C={plddt_confident}, v={d.get('latestVersion')}")
    time.sleep(0.3)

# Fix missing STRING data
print("\nRetrying STRING for failed genes...")
for gene, info in batch_data.items():
    if info.get("string") and len(info.get("string", [])) > 0:
        continue
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=20"
    data = fetch_json(url)
    if data:
        info["string"] = data
        print(f"  {gene}: {len(data)} partners (fixed)")
    else:
        print(f"  {gene}: still failed")
    time.sleep(0.5)

# Save updated data
with open(os.path.join(BASE, "batch_all_data.json"), 'w') as f:
    json.dump(batch_data, f, indent=2)
print("Data updated.")

# Print summary
for gene in sorted(batch_data.keys()):
    d = batch_data[gene]
    af = d.get("alphafold", {})
    plddt = af.get("mean_plddt", "N/A") if af else "N/A"
    string_n = len(d.get("string", []))
    intact_n = len(d.get("intact", []))
    uni = d.get("uniprot", {})
    pdb_n = len(uni.get("pdb_ids", [])) if uni else 0
    print(f"  {gene}: pLDDT={plddt} PDB={pdb_n} STRING={string_n} IntAct={intact_n}")
