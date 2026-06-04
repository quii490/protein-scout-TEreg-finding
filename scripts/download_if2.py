#!/usr/bin/env python3
"""Download IF images from Protein Atlas (v2 with correct API)."""
import json, os, urllib.request, ssl, re, time

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
ctx = ssl.create_default_context()

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception as e:
        print(f"    API error: {e}")
        return None

def fetch_text(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"    Fetch error: {e}")
        return None

def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500: return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(resp.read())
        return os.path.getsize(dest) > 500
    except Exception as e:
        print(f"    Download error: {e}")
        return False

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
    print(f"\n{gene} ({dest})...")
    if_dir = os.path.join(DETAIL, dest, gene, "IF_images")
    existing = []
    if os.path.exists(if_dir):
        existing = [f for f in os.listdir(if_dir) if f.endswith(".jpg")]
    if len(existing) >= 2:
        print(f"  Already have {len(existing)} images")
        continue

    # Step 1: Get Ensembl ID via search
    search_url = f"https://www.proteinatlas.org/search/{gene}?format=json&columns=g,sc"
    search_data = fetch_json(search_url)
    if not search_data:
        print(f"  Search failed")
        continue

    ensg = None
    for item in search_data:
        if item.get("Gene", "").upper() == gene.upper():
            ensg = item.get("Ensembl", "")
            break

    if not ensg:
        print(f"  No Ensembl ID")
        continue
    print(f"  Ensembl: {ensg}")

    # Step 2: Get XML with image data
    xml_url = f"https://www.proteinatlas.org/{ensg}.xml"
    xml_text = fetch_text(xml_url)
    if not xml_text:
        print(f"  XML failed")
        continue

    # Step 3: Extract IF image URLs
    image_urls = re.findall(r'https://images\.proteinatlas\.org/[^\s"\']+_red_green\.jpg', xml_text)
    if not image_urls:
        image_urls = re.findall(r'<imageUrl>([^<]+_red_green\.jpg)</imageUrl>', xml_text)

    print(f"  Found {len(image_urls)} IF URLs")
    if image_urls:
        print(f"    Sample: {image_urls[0][:80]}...")

    # Step 4: Download 2 images
    downloaded = 0
    for url in image_urls:
        if downloaded >= 2: break
        fname = url.split("/")[-1] if "/" in url else f"{gene}_{downloaded+1}.jpg"
        dest_path = os.path.join(if_dir, fname)
        if download(url, dest_path):
            print(f"    OK: {fname}")
            downloaded += 1
            time.sleep(0.5)
        else:
            print(f"    FAIL: {fname}")

    if downloaded == 0 and not image_urls:
        print(f"  No subcellular IF images found for {gene}")

    time.sleep(1)

print("\nDone")
