#!/usr/bin/env python3
"""Download PAE PNG images for all 27 genes from AlphaFold."""
import json, os, urllib.request, ssl, time, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

ctx = ssl.create_default_context()

def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500:
        print(f"    Already exists ({os.path.getsize(dest)} bytes)")
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"    Downloaded ({size} bytes)")
        return size > 500
    except Exception as e:
        print(f"    Failed: {e}")
        return False

uid_map = {
    "C1D":"Q13901","CCDC137":"Q6PK04","CDAN1":"Q8IWY9","CDC14A":"Q9UNH5",
    "CENPH":"Q9H3R5","CENPI":"Q92674","CENPK":"Q9BS16","CENPM":"Q9NSP4",
    "CENPT":"Q96BT3","CENPU":"Q71F23","CENPX":"A8MT69","CHMP1A":"Q9HD42",
    "CHP2":"O43745","CLASP1":"Q7Z460","CLNS1A":"P54105","CRTC3":"Q6UUV7",
    "CSRP3":"P50461","CUTC":"Q9NTM9","CASC3":"O15234","CCAR1":"Q8IX12",
    "CDX4":"O14627","CEBPG":"P53567","CIPC":"Q9C0C6","CSRP1":"P21291",
    "CSRP2":"Q16527","CSTF2T":"Q9H0L4","CTNNBL1":"Q8WYA6"
}

dest_map = {}
for g in ["C1D","CCDC137","CDAN1","CDC14A","CENPH","CENPI","CENPK","CENPM","CENPT","CENPU","CENPX","CHMP1A","CHP2","CLASP1","CLNS1A","CRTC3","CSRP3","CUTC"]:
    dest_map[g] = "nucleoplasm"
for g in ["CASC3","CCAR1","CDX4","CEBPG","CIPC","CSRP1","CSRP2","CSTF2T","CTNNBL1"]:
    dest_map[g] = "nucleus-cytoplasm"

print("Downloading PAE PNGs...")
success = 0
failed = 0
for gene, uid in uid_map.items():
    dest_dir = os.path.join(DETAIL, dest_map[gene], gene)
    dest = os.path.join(dest_dir, f"{gene}-PAE.png")
    # Use v6 PAE image
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uid}-F1-predicted_aligned_error_v6.png"
    print(f"  {gene}...")
    if download(url, dest):
        success += 1
    else:
        # Try v4
        url4 = f"https://alphafold.ebi.ac.uk/files/AF-{uid}-F1-predicted_aligned_error_v4.png"
        if download(url4, dest):
            success += 1
        else:
            failed += 1
    time.sleep(0.3)

print(f"\nPAE download: {success} OK, {failed} failed")
