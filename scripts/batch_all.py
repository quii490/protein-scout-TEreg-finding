#!/usr/bin/env python3
"""Batch fetch all data for 27 genes and generate reports."""
import json, os, sys, time, urllib.request, urllib.error, re, ssl, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            if attempt == retries - 1:
                print(f"  FAIL [{url[:80]}]: {e}")
                return None
            time.sleep(2)

def fetch_json(url):
    text = fetch(url)
    if text:
        try:
            return json.loads(text)
        except:
            return None
    return None

# Target genes with their UniProt IDs and data from xlsx
GENES = {
    "C1D":       {"uniprot": "Q13901", "size": 141,  "pubmed": 70,  "xlsx_nuc": None,  "hpa": None},
    "CCDC137":   {"uniprot": "Q6PK04", "size": 289,  "pubmed": 40,  "xlsx_nuc": 3.0,   "hpa": None},
    "CDAN1":     {"uniprot": "Q8IWY9", "size": 1227, "pubmed": 56,  "xlsx_nuc": 6.0,   "hpa": "Nuclear speckles|Nucleoplasm"},
    "CDC14A":    {"uniprot": "Q9UNH5", "size": 594,  "pubmed": 84,  "xlsx_nuc": 6.0,   "hpa": "Nuclear speckles"},
    "CENPH":     {"uniprot": "Q9H3R5", "size": 247,  "pubmed": 65,  "xlsx_nuc": 6.0,   "hpa": "Nucleoli|Nucleoplasm"},
    "CENPI":     {"uniprot": "Q92674", "size": 756,  "pubmed": 54,  "xlsx_nuc": 3.0,   "hpa": None},
    "CENPK":     {"uniprot": "Q9BS16", "size": 269,  "pubmed": 50,  "xlsx_nuc": None,  "hpa": None},
    "CENPM":     {"uniprot": "Q9NSP4", "size": 180,  "pubmed": 59,  "xlsx_nuc": 6.0,   "hpa": "Nucleoplasm"},
    "CENPT":     {"uniprot": "Q96BT3", "size": 561,  "pubmed": 71,  "xlsx_nuc": 3.0,   "hpa": None},
    "CENPU":     {"uniprot": "Q71F23", "size": 418,  "pubmed": 53,  "xlsx_nuc": 3.0,   "hpa": None},
    "CENPX":     {"uniprot": "A8MT69", "size": 81,   "pubmed": 62,  "xlsx_nuc": 3.0,   "hpa": "Nucleoplasm"},
    "CHMP1A":    {"uniprot": "Q9HD42", "size": 196,  "pubmed": 66,  "xlsx_nuc": 3.0,   "hpa": None},
    "CHP2":      {"uniprot": "O43745", "size": 196,  "pubmed": 46,  "xlsx_nuc": None,  "hpa": None},
    "CLASP1":    {"uniprot": "Q7Z460", "size": 1538, "pubmed": 94,  "xlsx_nuc": 6.0,   "hpa": "Nucleoplasm"},
    "CLNS1A":    {"uniprot": "P54105", "size": 237,  "pubmed": 64,  "xlsx_nuc": 3.0,   "hpa": None},
    "CRTC3":     {"uniprot": "Q6UUV7", "size": 619,  "pubmed": 100, "xlsx_nuc": 3.0,   "hpa": "Nucleoplasm"},
    "CSRP3":     {"uniprot": "P50461", "size": 194,  "pubmed": 74,  "xlsx_nuc": 3.0,   "hpa": None},
    "CUTC":      {"uniprot": "Q9NTM9", "size": 273,  "pubmed": 62,  "xlsx_nuc": 4.0,   "hpa": "Nucleoplasm"},
    "CASC3":     {"uniprot": "O15234", "size": 703,  "pubmed": 51,  "xlsx_nuc": 6.0,   "hpa": "Nucleoli"},
    "CCAR1":     {"uniprot": "Q8IX12", "size": 1150, "pubmed": 78,  "xlsx_nuc": 6.0,   "hpa": "Nucleoplasm"},
    "CDX4":      {"uniprot": "O14627", "size": 284,  "pubmed": 84,  "xlsx_nuc": 3.0,   "hpa": "Nucleoli"},
    "CEBPG":     {"uniprot": "P53567", "size": 150,  "pubmed": 85,  "xlsx_nuc": 6.0,   "hpa": "Nucleoplasm"},
    "CIPC":      {"uniprot": "Q9C0C6", "size": 399,  "pubmed": 67,  "xlsx_nuc": 4.0,   "hpa": "Nucleoplasm"},
    "CSRP1":     {"uniprot": "P21291", "size": 193,  "pubmed": 54,  "xlsx_nuc": 3.0,   "hpa": "Nuclear bodies|Nucleoplasm"},
    "CSRP2":     {"uniprot": "Q16527", "size": 193,  "pubmed": 88,  "xlsx_nuc": 3.0,   "hpa": "Nucleoplasm"},
    "CSTF2T":    {"uniprot": "Q9H0L4", "size": 616,  "pubmed": 72,  "xlsx_nuc": None,  "hpa": None},
    "CTNNBL1":   {"uniprot": "Q8WYA6", "size": 563,  "pubmed": 42,  "xlsx_nuc": 5.0,   "hpa": "Nucleoplasm"},
}

# Assign destination categories
DEST = {}
# nucleoplasm list
for g in ["C1D","CCDC137","CDAN1","CDC14A","CENPH","CENPI","CENPK","CENPM","CENPT","CENPU","CENPX","CHMP1A","CHP2","CLASP1","CLNS1A","CRTC3","CSRP3","CUTC"]:
    DEST[g] = "nucleoplasm"
# nucleus-cytoplasm list
for g in ["CASC3","CCAR1","CDX4","CEBPG","CIPC","CSRP1","CSRP2","CSTF2T","CTNNBL1"]:
    DEST[g] = "nucleus-cytoplasm"

all_data = {}

def fetch_uniprot(uniprot_id):
    """Fetch UniProt data via REST API."""
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    data = fetch_json(url)
    if not data:
        return None

    result = {"protein_name": "", "gene_name": "", "size_aa": 0, "mass_kda": 0,
              "subcell_locations": [], "go_cc": [], "domains": [], "pdb_ids": [], "sequence": ""}

    result["protein_name"] = data.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "")
    genes = data.get("genes", [])
    if genes:
        result["gene_name"] = genes[0].get("geneName", {}).get("value", "")
    result["sequence"] = data.get("sequence", {}).get("value", "")
    result["size_aa"] = data.get("sequence", {}).get("length", 0)
    masses = data.get("sequence", {}).get("molWeight", 0)
    result["mass_kda"] = round(masses / 1000, 1) if masses else 0

    for comment in data.get("comments", []):
        if comment["commentType"] == "SUBCELLULAR LOCATION":
            for loc in comment.get("subcellularLocations", []):
                result["subcell_locations"].append(loc.get("location", {}).get("value", ""))

    for ref in data.get("uniProtKBCrossReferences", []):
        db = ref.get("database", "")
        if db == "GO":
            props = {p.get("key",""): p.get("value","") for p in ref.get("properties", [])}
            if props.get("goTerm", "").startswith("C:") and "nucle" in props.get("goTerm","").lower():
                result["go_cc"].append(f"{props.get('goTerm','')} ({props.get('goEvidenceType','')})")
        elif db == "PDB":
            result["pdb_ids"].append(ref.get("id", ""))
        elif db in ("Pfam", "InterPro", "SMART"):
            result["domains"].append(f"{db}: {ref.get('id','')} - {ref.get('properties',[{}])[0].get('value','') if ref.get('properties') else ''}")

    return result

def fetch_alphafold(uniprot_id):
    """Fetch AlphaFold prediction data."""
    url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
    return fetch_json(url)

def fetch_string(gene):
    """Fetch STRING interaction partners."""
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=20"
    return fetch_json(url)

def fetch_intact(gene):
    """Fetch IntAct physical interactions."""
    url = f"http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27"
    text = fetch(url)
    if not text:
        return []
    results = []
    for line in text.strip().split("\n"):
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) >= 15:
            results.append({
                "partner_a": cols[2].split("(")[0].strip() if "(" in cols[2] else cols[2].strip(),
                "partner_b": cols[3].split("(")[0].strip() if "(" in cols[3] else cols[3].strip(),
                "method": cols[6].split("(")[0].strip() if "(" in cols[6] else cols[6].strip(),
                "pubmed": cols[8].split(":")[-1] if ":" in cols[8] else cols[8],
                "interaction_type": cols[11].split("(")[0].strip() if "(" in cols[11] else cols[11],
            })
    return results

def download_file(url, dest_path):
    """Download a file to dest_path."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'wb') as f:
                f.write(resp.read())
            return True
    except Exception as e:
        print(f"    Download failed: {e}")
        return False

def download_pae_png(uniprot_id, gene, dest_dir):
    """Download PAE PNG from AlphaFold."""
    # AlphaFold v4 PAE image
    urls = [
        f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-predicted_aligned_error_v4.png",
        f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-predicted_aligned_error_v3.png",
        f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-predicted_aligned_error_v2.png",
    ]
    dest = os.path.join(dest_dir, f"{gene}-PAE.png")
    if os.path.exists(dest) and os.path.getsize(dest) > 500:
        return True
    for url in urls:
        if download_file(url, dest):
            print(f"    PAE downloaded ({(os.path.getsize(dest))} bytes)")
            return True
    return False

def download_alphafold_pdb(uniprot_id, gene, dest_dir):
    """Download AlphaFold PDB."""
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
    dest = os.path.join(dest_dir, f"{gene}-alphafold.pdb")
    if os.path.exists(dest):
        return True
    return download_file(url, dest)

def download_if_images(gene, dest_dir):
    """Download IF images from Protein Atlas."""
    if_dir = os.path.join(dest_dir, "IF_images")
    os.makedirs(if_dir, exist_ok=True)
    existing = [f for f in os.listdir(if_dir) if f.endswith(".jpg")]
    if len(existing) >= 2:
        return existing[:2]

    # Try Protein Atlas XML/search API
    search_url = f"https://www.proteinatlas.org/search/{gene}?format=json"
    data = fetch_json(search_url)
    if not data:
        return []

    # Get the ensembl id
    ensg = None
    for item in data:
        if item.get("Gene", "").upper() == gene.upper():
            ensg = item.get("Ensembl", "")
            break

    if not ensg:
        return []

    # Try the subcellular location API
    sub_url = f"https://www.proteinatlas.org/api/search_download.php?search={gene}&format=json&columns=g,sc"
    sub_data = fetch_json(sub_url)

    # Alternative: build image URLs directly
    # Format: https://images.proteinatlas.org/ENSG.../cell_line/..._red_green.jpg
    # Simpler: try HPA XML API
    xml_url = f"https://www.proteinatlas.org/{ensg}.xml"
    xml_text = fetch(xml_url)
    if not xml_text:
        return []

    images = []
    # Parse XML for IF image URLs
    for m in re.finditer(r'<imageUrl[^>]*>([^<]+\.jpg)</imageUrl>', xml_text):
        img_url = m.group(1)
        if "_red_green" in img_url:
            images.append(img_url)

    if not images:
        return []

    downloaded = []
    for i, img_url in enumerate(images[:4]):
        # Extract cell line from URL
        parts = img_url.split("/")
        fname = parts[-1] if parts else f"{gene}_{i+1}.jpg"
        dest = os.path.join(if_dir, fname)
        if download_file(img_url, dest):
            downloaded.append(fname)

    return downloaded[:2]


print("=" * 60)
print("Phase 1: UniProt data collection")
print("=" * 60)

for gene, info in GENES.items():
    uniprot = info["uniprot"]
    if not uniprot or uniprot == "nan":
        print(f"  {gene}: No UniProt ID")
        continue
    print(f"  {gene} ({uniprot})...")
    data = fetch_uniprot(uniprot)
    if data:
        all_data[gene] = {"uniprot": data}
        print(f"    Size: {data['size_aa']}aa, PDBs: {data['pdb_ids']}, Domains: {len(data['domains'])}")
    else:
        all_data[gene] = {"uniprot": None}
        print(f"    FAILED")
    time.sleep(0.3)

print()
print("=" * 60)
print("Phase 2: AlphaFold data")
print("=" * 60)

for gene, info in GENES.items():
    uniprot = info["uniprot"]
    if not uniprot or uniprot == "nan":
        continue
    print(f"  {gene}...")
    af = fetch_alphafold(uniprot)
    if af:
        entry = af[0] if isinstance(af, list) else af
        all_data.setdefault(gene, {})["alphafold"] = {
            "mean_plddt": entry.get("meanPlddt", 0),
            "pae_url": entry.get("paeImageUrl", ""),
            "uniprot_id": entry.get("uniprotAccession", ""),
            "version": str(entry.get("latestVersion", "")),
        }
        print(f"    pLDDT: {entry.get('meanPlddt', 'N/A')}")
    else:
        all_data.setdefault(gene, {})["alphafold"] = None
        print(f"    No AlphaFold prediction")
    time.sleep(0.3)

print()
print("=" * 60)
print("Phase 3: STRING data")
print("=" * 60)

for gene in GENES:
    print(f"  {gene}...")
    string_data = fetch_string(gene)
    if string_data:
        all_data.setdefault(gene, {})["string"] = string_data
        print(f"    Partners: {len(string_data)}")
    else:
        all_data.setdefault(gene, {})["string"] = []
        print(f"    No STRING data")
    time.sleep(0.5)

print()
print("=" * 60)
print("Phase 4: IntAct data")
print("=" * 60)

for gene in GENES:
    print(f"  {gene}...")
    intact_data = fetch_intact(gene)
    all_data.setdefault(gene, {})["intact"] = intact_data
    print(f"    Interactions: {len(intact_data)}")
    time.sleep(0.5)

# Save all data
outfile = os.path.join(BASE, "batch_all_data.json")
with open(outfile, 'w') as f:
    json.dump(all_data, f, indent=2)

print()
print(f"Data saved to {outfile}")
print(f"Genes with data: {len(all_data)}")
