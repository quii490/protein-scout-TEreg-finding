#!/usr/bin/env python3
"""Download IF images from Protein Atlas for specific genes."""
import json, os, urllib.request, urllib.parse, ssl, re, time

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

def fetch_text(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except: return None

def download_file(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500: return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(resp.read())
        return os.path.getsize(dest) > 500
    except: return False

# Genes that need IF images downloaded (HPA data exists, no IF images)
TARGETS = {
    "CENPH": "nucleoplasm",
    "CENPM": "nucleoplasm",
    "CENPX": "nucleoplasm",
    "CLASP1": "nucleoplasm",
    "CRTC3": "nucleoplasm",
    "CUTC": "nucleoplasm",
    "CASC3": "nucleus-cytoplasm",
    "CSRP1": "nucleus-cytoplasm",
    "CSRP2": "nucleus-cytoplasm",
}

for gene, dest in TARGETS.items():
    print(f"\n{gene}...")
    if_dir = os.path.join(DETAIL, dest, gene, "IF_images")
    existing = [f for f in os.listdir(if_dir) if f.endswith(".jpg")] if os.path.exists(if_dir) else []
    if len(existing) >= 2:
        print(f"  Already have {len(existing)} images")
        continue

    # Step 1: Search Protein Atlas to get Ensembl ID
    search_url = f"https://www.proteinatlas.org/api/search/{gene}?format=json"
    search_data = fetch_json(search_url)
    if not search_data:
        print(f"  Search failed")
        continue

    ensg = None
    for item in search_data:
        if item.get("Gene", "").upper() == gene.upper():
            ensg = item.get("Ensembl", "")
            print(f"  Ensembl: {ensg}")
            break

    if not ensg:
        print(f"  No Ensembl ID found")
        continue

    # Step 2: Get subcellular location data (XML with image URLs)
    xml_url = f"https://www.proteinatlas.org/{ensg}.xml"
    xml_text = fetch_text(xml_url)
    if not xml_text:
        print(f"  XML download failed")
        continue

    # Step 3: Extract IF image URLs for subcellular location
    # Look for image URLs in the subcellular section
    image_urls = []
    # Match URLs with antibody IDs (HPA/CAB) for subcellular IF
    for m in re.finditer(r'<imageUrl>([^<]+_red_green\.jpg)</imageUrl>', xml_text):
        url = m.group(1)
        image_urls.append(url)

    if not image_urls:
        # Try alternative pattern
        for m in re.finditer(r'https://images\.proteinatlas\.org/[^"\s]+_red_green\.jpg', xml_text):
            image_urls.append(m.group(0))

    print(f"  Found {len(image_urls)} IF images")

    # Step 4: Download up to 2 images
    downloaded = 0
    for url in image_urls[:4]:
        if downloaded >= 2: break
        # Extract cell line from URL
        parts = url.split("/")
        fname = parts[-1] if parts else f"{gene}_{downloaded+1}.jpg"
        dest_path = os.path.join(if_dir, fname)

        if download_file(url, dest_path):
            print(f"    Downloaded: {fname}")
            downloaded += 1
        else:
            print(f"    Failed: {fname}")

    if downloaded == 0:
        print(f"  No images downloaded")
    time.sleep(1)

print("\nDone")
