#!/usr/bin/env python3
"""
Fetch IF images from Protein Atlas for all proteins missing them.
Prioritizes nucleoplasm first, then remaining categories.
Skips rejected/ proteins.
"""

import os
import re
import subprocess
import json
import time
import sys
import traceback

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"
VAULT_PREFIX = "Projects/TEreg-finding/protein-interested/detail"
LOG_FILE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/fetch_if_log.txt"

def log(msg):
    timestamp = time.strftime("%H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    sys.stdout.flush()
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
        f.flush()

def curl(url, timeout=45):
    """Simple curl wrapper with retry."""
    result = subprocess.run(
        ["curl", "-sL", "--connect-timeout", "15", "--max-time", str(timeout),
         "--retry", "1", "--retry-delay", "2",
         "-H", "User-Agent: Mozilla/5.0", url],
        capture_output=True, text=True
    )
    return result.stdout.strip(), result.returncode

def search_ensg(gene):
    """Search Protein Atlas for ENSG ID."""
    stdout, rc = curl(f"https://www.proteinatlas.org/search/{gene}?format=json", timeout=20)
    if rc != 0 or not stdout:
        return None
    try:
        data = json.loads(stdout)
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("Ensembl")
    except:
        pass
    return None

def extract_if_data(ensg):
    """Extract IF cell line data from Protein Atlas XML."""
    stdout, rc = curl(f"https://www.proteinatlas.org/{ensg}.xml", timeout=30)
    if rc != 0 or not stdout:
        return None

    # Find all <data> blocks containing blue_red_green images
    blocks = re.findall(r'<data>.*?</data>', stdout, re.DOTALL)
    results = []
    seen_cells = set()

    for block in blocks:
        blue_imgs = re.findall(
            r'<imageUrl>(https://images\.proteinatlas\.org/\d+/\d+_\w+_\w+_blue_red_green\.jpg)</imageUrl>',
            block
        )
        if not blue_imgs:
            continue

        cell_match = re.search(r'<cellLine[^>]*>([^<]+)</cellLine>', block)
        locations = re.findall(r'<location[^>]*>([^<]+)</location>', block)

        if cell_match:
            cell_name = cell_match.group(1).strip()
            # Clean up cell line name for filename (remove special chars)
            safe_name = re.sub(r'[^a-zA-Z0-9\-\.]', '', cell_name.replace(' ', '-').replace('/', '-'))

            if safe_name not in seen_cells:
                seen_cells.add(safe_name)
                results.append({
                    'cell': cell_name,
                    'safe_name': safe_name,
                    'locations': locations,
                    'image_url': blue_imgs[0]  # Take first image per cell line
                })

    return results

def has_if_in_report(eval_path):
    """Check if evaluation report already has IF images embedded."""
    if not os.path.exists(eval_path):
        return False
    try:
        with open(eval_path, 'r') as f:
            content = f.read()
        return bool(re.search(r'IF_images.*?\.jpg', content))
    except:
        return True  # Skip if can't read

def update_report(eval_path, gene, if_data, category):
    """Update the evaluation report with IF image embeddings."""
    if not os.path.exists(eval_path):
        log(f"  WARN: Report not found: {eval_path}")
        return False

    with open(eval_path, 'r') as f:
        content = f.read()

    # Remove existing "暂无IF数据" or similar placeholder
    content = re.sub(r'\*\*IF 图像\*\*:.*?(\n|$)', '', content)

    # Build image embeddings - take up to 2 from different cell lines
    img_dir = f"{BASE}/{category}/{gene}/IF_images"

    # Choose images: prefer nucleoplasm-only cell lines, then any
    nuc_only = [d for d in if_data if all('nucleoplasm' in l.lower() for l in d['locations'])]
    others = [d for d in if_data if d not in nuc_only]

    selected = (nuc_only + others)[:2]
    img_lines = ["**IF 图像**:\n"]
    for d in selected:
        cell_display = d['cell']
        img_lines.append(f"![[{VAULT_PREFIX}/{category}/{gene}/IF_images/{d['safe_name']}_1.jpg|{cell_display}]]\n")

    # Insert after "评估日期 |" line
    date_pattern = re.compile(r'(\| 评估日期 \|.*\n)')
    insert_text = "\n" + "".join(img_lines)

    if date_pattern.search(content):
        content = date_pattern.sub(r'\1' + insert_text, content, count=1)
    else:
        # Fallback: insert after the 基本信息 section header
        content = content.replace("### 1. 基本信息", "### 1. 基本信息\n" + insert_text)

    with open(eval_path, 'w') as f:
        f.write(content)

    return True

def main():
    # Get list of proteins to process, prioritizing nucleoplasm
    categories = [
        "nucleoplasm",
        "nucleolus",
        "chromatin",
        "nucleus-cytoplasm",
        "nuclear-speckle",
        "nuclear-envelope",
        "nuclear-body"
    ]

    # Build the full work list
    work_list = []
    for cat in categories:
        cat_path = os.path.join(BASE, cat)
        if not os.path.isdir(cat_path):
            continue
        for gene in sorted(os.listdir(cat_path)):
            gene_path = os.path.join(cat_path, gene)
            if not os.path.isdir(gene_path):
                continue
            eval_path = os.path.join(gene_path, f"{gene}-evaluation.md")
            if not os.path.exists(eval_path):
                continue
            if has_if_in_report(eval_path):
                continue

            if_dir = os.path.join(gene_path, "IF_images")
            work_list.append((gene, cat, eval_path, if_dir))

    total = len(work_list)
    log(f"Total proteins to process: {total}")

    # Process nucleoplasm first (first 100), then rest
    nuc_work = [(g, c, e, d) for g, c, e, d in work_list if c == "nucleoplasm"]
    other_work = [(g, c, e, d) for g, c, e, d in work_list if c != "nucleoplasm"]

    # Limit to 100 nucleoplasm first
    nuc_work = nuc_work[:100]
    ordered_work = nuc_work + other_work

    log(f"Processing {len(nuc_work)} nucleoplasm + {len(other_work)} others = {len(ordered_work)} total")

    success = 0
    no_if = 0
    failed = 0
    skipped = 0

    for i, (gene, cat, eval_path, if_dir) in enumerate(ordered_work):
        sys.stdout.flush()
        log(f"\n[{i+1}/{len(ordered_work)}] {gene} ({cat})")
        sys.stdout.flush()

        # Check if IF_images dir already has JPG files
        if os.path.isdir(if_dir) and any(f.endswith('.jpg') for f in os.listdir(if_dir)):
            # Images exist but not embedded - just update report
            log(f"  Images exist, updating report...")
            # Find existing images
            jpg_files = [f for f in os.listdir(if_dir) if f.endswith('.jpg')]
            if jpg_files:
                # Reconstruct IF data from filenames
                if_data = []
                for jpg in jpg_files:
                    # Extract cell line from filename like "A-431_1.jpg"
                    base = jpg.replace('.jpg', '')
                    parts = base.rsplit('_', 1)
                    cell = parts[0] if len(parts) > 1 else base
                    if_data.append({'cell': cell, 'safe_name': cell, 'locations': [], 'image_url': ''})

                if if_data:
                    if update_report(eval_path, gene, if_data, cat):
                        success += 1
                        log(f"  OK: Updated report with {len(if_data)} existing images")
                    else:
                        failed += 1
                continue

        # Search Protein Atlas
        ensg = search_ensg(gene)
        if not ensg:
            log(f"  SKIP: Not found in Protein Atlas")
            no_if += 1
            continue

        log(f"  ENSG: {ensg}")

        # Extract IF data from XML
        if_data = extract_if_data(ensg)

        if not if_data:
            log(f"  No IF data available")
            no_if += 1
            # Update report to mark no IF
            with open(eval_path, 'r') as f:
                content = f.read()
            if "暂无IF数据" not in content and "暂无HPA数据" not in content:
                content = content.replace(
                    "**IF 图像**: 暂无数据",
                    "**IF 图像**: 暂无HPA数据"
                )
                if "暂无HPA数据" not in content:
                    # Add the note if not already there
                    pass
            with open(eval_path, 'w') as f:
                f.write(content)
            continue

        # Select up to 2 images from different cell lines
        nuc_only = [d for d in if_data if all('nucleoplasm' in l.lower() for l in d['locations'])]
        others = [d for d in if_data if d not in nuc_only]
        preferred = nuc_only + others
        selected = preferred[:2]

        log(f"  Found {len(if_data)} cell lines with IF data, downloading {len(selected)} images")
        for d in selected:
            log(f"    {d['cell']}: {d['locations']}")

        # Create IF_images directory
        os.makedirs(if_dir, exist_ok=True)

        # Download images
        downloaded = []
        for j, d in enumerate(selected):
            out_path = os.path.join(if_dir, f"{d['safe_name']}_1.jpg")
            result = subprocess.run(
                ["curl", "-skL", "--connect-timeout", "15", "--max-time", "30",
                 "-o", out_path, d['image_url']],
                capture_output=True
            )

            if result.returncode == 0 and os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                downloaded.append(d)
                log(f"    Downloaded: {d['safe_name']}_1.jpg ({os.path.getsize(out_path)} bytes)")
            else:
                log(f"    FAILED: {d['safe_name']} from {d['image_url']}")

        if downloaded:
            if update_report(eval_path, gene, downloaded, cat):
                success += 1
                log(f"  OK: Downloaded {len(downloaded)} images and updated report")
            else:
                failed += 1
        elif if_data:
            # IF data exists but download failed
            no_if += 1
            log(f"  Download failed for all images")
        else:
            no_if += 1

        # Rate limiting
        time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"DONE: success={success} no_if={no_if} failed={failed} skipped={skipped}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
