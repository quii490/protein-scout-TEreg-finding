#!/usr/bin/env python3
"""Generate /180 reports for ready genes using harvest packet data.
Skips already complete reports. Uses cached API data for speed."""

import json, os, re, ssl, urllib.request, time, sys

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested"
DETAIL = os.path.join(BASE, "detail")
VAULT_PREFIX = "Projects/TEreg-finding/protein-interested/detail"
HP_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"

TODAY = "2026-06-03"

READY = [
    "FAM102A","FAM102B","FAM104A","FAM104B","FAM107A","FAM110A",
    "FAM114A1","FAM118A","FAM120A","FAM120AOS","FAM120B","FAM120C",
    "FAM122A","FAM124B","FAM131A","FAM131B","FAM131C","FAM133A","FAM133B","FAM135A",
    "FAM136A","FAM149A","FAM149B1","FAM151A","FAM151B","FAM153A","FAM153B","FAM153C",
    "FAM155A","FAM156A","FAM156B","FAM157A","FAM157B","FAM157C",
    "FAM160A1","FAM160A2","FAM161A","FAM161B","FAM162A","FAM167A",
    "FAM168A","FAM168B","FAM169A","FAM169B","FAM170A","FAM171A1",
    "FAM171A2","FAM171B","FAM172A","FAM173A","FAM173B","FAM174A","FAM174B",
    "FAM175A","FAM175B","FAM177A1","FAM178A","FAM178B","FAM180A","FAM181A",
    "FAM184A","FAM184B","FAM185A","FAM186A","FAM186B","FAM187A","FAM187B",
    "FAM188A","FAM189A1","FAM189A2","FAM192A","FAM193A","FAM193B",
    "FAM196A","FAM196B","FAM198A","FAM199X","FAM200A","FAM204A","FAM206A",
    "FAM207A","FAM208A","FAM208B","FAM209A","FAM209B","FAM210A",
    "FAM214A","FAM216A","FAM219A","FAM220A","FAM221A","FAM222A","FAM225A",
    "FAM226B","FAM227A","FAM227B","FAM228A","FAM229B",
    "FAN1","FANCA","FANCB","FANCC","FANCD2OS","FANCE","FANCF","FANCG","FANCI","FANCL","FANCM",
    "FARP1","FARP2","FASTK","FASTKD1","FASTKD2","FASTKD3","FASTKD5",
    "FAU","FBF1","FBL","FBXL18","FBXL2","FBXL20","FBXL3","FBXL5","FBXL8",
    "FBXO10","FBXO11","FBXO15","FBXO16","FBXO17","FBXO18","FBXO2","FBXO21","FBXO22","FBXO24","FBXO25",
]

ctx = ssl.create_default_context()

def fetch_json(url, timeout=45):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except Exception:
            if attempt == 2:
                return None
            time.sleep(1)

def fetch_text(url, timeout=45):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception:
            if attempt == 2:
                return None
            time.sleep(1)

def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 500:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f:
                f.write(resp.read())
        return os.path.getsize(dest) > 500
    except Exception:
        return False


def load_harvest(gene):
    path = os.path.join(HP_DIR, f"{gene}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)

# ============================================================
# SCORING (same as gen_96_ready.py)
# ============================================================

def novelty_score(pubmed_strict):
    if pubmed_strict <= 20: return 10
    if pubmed_strict <= 40: return 8
    if pubmed_strict <= 60: return 6
    if pubmed_strict <= 80: return 4
    if pubmed_strict <= 100: return 2
    return 0

def size_score(aa):
    if 200 <= aa <= 800: return 10
    if (100 <= aa < 200) or (800 < aa <= 1200): return 8
    if (50 <= aa < 100) or (1200 < aa <= 2000): return 5
    if aa < 50 or (2000 < aa <= 3000): return 2
    return 0

def struct_score(pdb_ids, plddt):
    n_pdb = len(pdb_ids) if pdb_ids else 0
    if n_pdb >= 5 and plddt >= 70: return 10
    if n_pdb >= 2 and plddt >= 70: return 9
    if n_pdb >= 1 and plddt >= 70: return 8
    if plddt >= 85: return 8
    if plddt >= 70: return 7
    if plddt >= 50: return 6
    if plddt < 40: return 4
    return 6

def domain_score(domains_text, plddt):
    chromatin_kw = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp",
                    "zinc finger", "homeobox", "homeodomain", "hmg", "forkhead",
                    "bzip", "bhlh", "at-hook", "myb", "cxxc", "swi/snf", "iswi",
                    "histone", "chromatin", "dna-binding", "nucleic acid binding"]
    text = domains_text.lower()
    has_chromatin = any(kw in text for kw in chromatin_kw)
    domain_count = text.count("ipr") + text.count("pf")
    if has_chromatin and domain_count >= 3: return 10
    if has_chromatin or (domain_count >= 2 and plddt >= 80): return 8
    if domain_count > 0: return 7
    if plddt >= 70: return 6
    if plddt >= 50: return 5
    return 4

def ppi_score(string_n, intact_n, string_partners):
    reg_keywords = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                    "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                    "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                    "deacetylase", "acetyltransferase", "methyltransferase",
                    "kinetochore", "centromere", "condensin", "cohesin", "smc",
                    "origin recognition", "replication factor"]
    if not string_partners:
        return 2
    reg_count = 0
    for p in string_partners[:20]:
        name = p.get("partner", "").lower()
        if any(kw in name for kw in reg_keywords):
            reg_count += 1
    reg_ratio = reg_count / min(len(string_partners), 20)
    has_physical = intact_n > 0
    has_string = string_n > 0
    if has_physical and reg_ratio > 0.4 and string_n >= 10: return 10
    if has_physical and reg_ratio > 0.2 and string_n >= 5: return 8
    if has_physical and reg_ratio > 0.3: return 6
    if has_string and reg_ratio > 0.2: return 4
    if has_string: return 3
    return 2

def cross_validation(pdb_ids, plddt, uni_loc, hpa_main, go_cc, string_n, intact_n, domains, has_uni):
    pts = 0
    if pdb_ids and plddt > 0: pts += 0.5
    has_multi_nuc = 0
    if has_uni and uni_loc: has_multi_nuc += 1
    if hpa_main: has_multi_nuc += 1
    if go_cc: has_multi_nuc += 1
    if has_multi_nuc >= 2: pts += 0.5
    if string_n > 0 and intact_n > 0: pts += 0.5
    if domains and "暂无" not in domains and plddt > 70: pts += 0.5
    if len(pdb_ids) >= 3: pts += 1.0
    return min(pts, 3.0)

def nuclear_score(uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc_terms, has_uni):
    nucleolus_kw = ["nucleol"]
    nucleus_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
    non_nuc_kw = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
                  "membrane", "secreted", "cytoskeleton", "centrosome", "spindle",
                  "microtubule", "vesicle", "kinocilium", "lamellipodium",
                  "synapse", "postsynaptic", "cilia", "flagella",
                  "cell projection", "plasma membrane", "extracellular",
                  "acrosome", "principal piece"]

    hpa_nuc = False
    hpa_non = False
    hpa_main_text = " ".join(hpa_main).lower()
    hpa_addl_text = " ".join(hpa_addl).lower()

    if any(kw in hpa_main_text for kw in nucleolus_kw):
        hpa_nuc = True
    elif any(kw in hpa_main_text for kw in nucleus_kw):
        hpa_nuc = True
    if any(kw in hpa_addl_text for kw in nucleus_kw) and not any(kw in hpa_main_text for kw in nucleus_kw):
        hpa_nuc = True
    if any(kw in hpa_main_text for kw in non_nuc_kw):
        hpa_non = True

    uni_nuc = False
    uni_non = False
    if has_uni:
        uni_text = " ".join(uni_subcell).lower()
        if any(kw in uni_text for kw in nucleus_kw):
            uni_nuc = True
        if any(kw in uni_text for kw in non_nuc_kw):
            uni_non = True

    go_nuc = False
    go_non = False
    if go_cc_terms:
        go_terms = []
        for cc in go_cc_terms:
            if isinstance(cc, dict):
                go_terms.append(cc.get("term", ""))
            else:
                go_terms.append(str(cc))
        go_text = " ".join(go_terms).lower()
        if any(kw in go_text for kw in nucleus_kw):
            go_nuc = True
        if any(kw in go_text for kw in non_nuc_kw):
            go_non = True

    nuc_sources = sum([hpa_nuc, uni_nuc, go_nuc])
    non_sources = sum([hpa_non, uni_non, go_non])

    if nuc_sources == 0 and non_sources == 0:
        return 3
    if nuc_sources >= 2 and non_sources == 0:
        return 9 if nuc_sources >= 3 else 8
    if nuc_sources >= 2 and non_sources >= 1:
        return 7
    if nuc_sources == 1 and non_sources == 0:
        if hpa_nuc and hpa_rel in ["Approved", "Enhanced"]:
            return 7
        return 5
    if hpa_non and not hpa_nuc and (uni_nuc or go_nuc):
        if go_nuc:
            return 4
        return 3
    if nuc_sources == 1 and non_sources == 1:
        return 4
    if nuc_sources >= 1 and non_sources > nuc_sources:
        return 4
    if non_sources >= 2 and nuc_sources == 0:
        return 2
    if non_sources == 1 and nuc_sources == 0:
        return 2
    return 3

def get_domain_text(uni_data):
    if not uni_data: return "暂无数据 (UniProt未获取)"
    interpro = uni_data.get("interpro", [])
    pfam = uni_data.get("pfam", [])
    ipr_names = [i.get("name", "") or i.get("id", "") for i in interpro]
    pf_names = [p.get("name", "") or p.get("id", "") for p in pfam]
    parts = []
    if ipr_names:
        parts.append("InterPro: " + ", ".join(ipr_names[:5]))
    if pf_names:
        parts.append("Pfam: " + ", ".join(pf_names[:3]))
    return "; ".join(parts) if parts else "无注释结构域"

def extract_go_terms(go_cc):
    if not go_cc: return []
    terms = []
    for cc in go_cc:
        if isinstance(cc, dict):
            terms.append(cc.get("term", str(cc)))
        else:
            terms.append(str(cc))
    return terms

def get_go_cc_text(uni_data):
    if not uni_data: return "- 无 GO-CC 注释 (UniProt未获取)"
    go_cc = uni_data.get("go_cc", [])
    if not go_cc: return "- 无 GO-CC 注释"
    return "\n".join(f"- {cc.get('term', str(cc))} ({cc.get('id','')})" for cc in go_cc[:8])

def format_key_papers(papers):
    if not papers:
        return "无关键文献数据。"
    lines = []
    for i, p in enumerate(papers[:5], 1):
        title = p.get("title", "N/A")
        journal = p.get("journal", "N/A")
        pmid = p.get("pmid", "N/A")
        lines.append(f"{i}. {title}. *{journal}*. PMID: {pmid}")
    return "\n".join(lines)

def format_string_table(partners, score_threshold=0.4):
    if not partners:
        return "| — | — | — | — |"
    filtered = [p for p in partners if p.get("score", 0) >= score_threshold]
    if not filtered:
        return "| — | — | — | — |"
    lines = []
    for p in filtered[:10]:
        name = p.get("partner", "?")
        score = p.get("score", 0)
        exp = p.get("experimental", 0)
        lines.append(f"| {name} | {score:.3f} | {exp:.3f} | — |")
    return "\n".join(lines)

def format_intact_table(partners):
    if not partners:
        return "| — | — | — |"
    seen = set()
    lines = []
    for p in partners:
        partner = p.get("partner", "")
        if partner.lower() in seen:
            continue
        seen.add(partner.lower())
        if len(seen) > 10:
            break
        method = p.get("method", "—")
        pmid = p.get("pmid", "—")
        lines.append(f"| {partner} | {method[:50]} | {pmid[:30]} |")
    return "\n".join(lines) if lines else "| — | — | — |"

def get_reg_partner_info(string_partners, intact_partners):
    reg_keywords = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                    "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                    "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                    "deacetylase", "acetyltransferase", "methyltransferase",
                    "kinetochore", "centromere", "condensin", "cohesin", "smc",
                    "origin recognition", "replication factor", "eif4e", "translation",
                    "ubiquitin", "e3", "ligase"]
    reg_partners = []
    if string_partners:
        for p in string_partners[:20]:
            name = p.get("partner", "").lower()
            if any(kw in name for kw in reg_keywords):
                reg_partners.append(p.get("partner", "?"))
    return reg_partners


# ============================================================
# IF IMAGES (from HPA, using cached data + download)
# ============================================================

def fetch_if_images_for_gene(gene, dest, hpa_ensembl):
    gene_dir = os.path.join(DETAIL, dest, gene)
    if_dir = os.path.join(gene_dir, "IF_images")
    img_prefix = f"{VAULT_PREFIX}/{dest}/{gene}/IF_images"

    existing_jpgs = []
    if os.path.isdir(if_dir):
        existing_jpgs = [f for f in os.listdir(if_dir) if f.endswith('.jpg') and 'thumb' not in f]
    if existing_jpgs:
        jpg_files = existing_jpgs[:2]
        lines = []
        for jpg in jpg_files:
            base = jpg.replace('.jpg', '')
            cell_name = base.replace('-', ' ').replace('_', ' ')
            lines.append(f"![[{img_prefix}/{jpg}|{cell_name}]]")
        return "\n".join(lines), "IF图像已嵌入"

    if not hpa_ensembl:
        return None, "Protein Atlas 中未找到该基因条目（无ENSG匹配），无法获取IF原图。"

    text = fetch_text(f"https://www.proteinatlas.org/{hpa_ensembl}.xml")
    if not text:
        return None, "Protein Atlas XML 数据获取失败。"

    blocks = re.findall(r'<data>.*?</data>', text, re.DOTALL)
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
            safe_name = re.sub(r'[^a-zA-Z0-9\-\.]', '', cell_name.replace(' ', '-').replace('/', '-'))
            if safe_name not in seen_cells:
                seen_cells.add(safe_name)
                results.append({
                    'cell': cell_name,
                    'safe_name': safe_name,
                    'locations': locations,
                    'image_url': blue_imgs[0]
                })

    if not results:
        return None, "HPA XML中无可用IF原图（图像未检测到或数据不可用）。"

    nuc_only = [d for d in results if all('nucleoplasm' in l.lower() for l in d['locations'])]
    others = [d for d in results if d not in nuc_only]
    selected = (nuc_only + others)[:2]

    os.makedirs(if_dir, exist_ok=True)
    downloaded = []
    for d in selected:
        out_path = os.path.join(if_dir, f"{d['safe_name']}_1.jpg")
        if download(d['image_url'], out_path):
            downloaded.append(d)

    if downloaded:
        lines = []
        for d in downloaded:
            lines.append(f"![[{img_prefix}/{d['safe_name']}_1.jpg|{d['cell']}]]")
        return "\n".join(lines), f"IF图像已下载并嵌入 ({len(downloaded)}张)"

    return None, "IF图像下载失败（API可访问但图像传输失败）。"


# ============================================================
# PAE IMAGE
# ============================================================

def download_pae_image(gene, accession, dest):
    pae_path = os.path.join(DETAIL, dest, gene, f"{gene}-PAE.png")
    if os.path.exists(pae_path) and os.path.getsize(pae_path) > 100:
        return f"![[{VAULT_PREFIX}/{dest}/{gene}/{gene}-PAE.png]]", True

    data = fetch_json(f"https://alphafold.ebi.ac.uk/api/prediction/{accession}")
    if not data:
        return None, False
    entry = data[0] if isinstance(data, list) else data
    if not entry:
        return None, False
    pae_url = entry.get("paeImageUrl", "")
    if not pae_url:
        return None, False

    dest_dir = os.path.join(DETAIL, dest, gene)
    os.makedirs(dest_dir, exist_ok=True)
    if download(pae_url, pae_path):
        return f"![[{VAULT_PREFIX}/{dest}/{gene}/{gene}-PAE.png]]", True
    return None, False


# ============================================================
# REPORT GENERATION FROM HARVEST DATA
# ============================================================

def already_complete(gene):
    for dname in os.listdir(DETAIL):
        dpath = os.path.join(DETAIL, dname)
        if not os.path.isdir(dpath):
            continue
        rp = os.path.join(dpath, gene, f"{gene}-evaluation.md")
        if os.path.exists(rp):
            sz = os.path.getsize(rp)
            if sz > 2000:
                with open(rp) as f:
                    content = f.read()
                    if "/180" in content:
                        return True, rp
    return False, None

def determine_dest(nuc, pubmed_strict, hpa_main, hpa_addl, subcell, go_cc):
    if nuc <= 3 or pubmed_strict > 100:
        return "rejected"
    hpa_loc_text = ", ".join(hpa_main + hpa_addl).lower()
    uni_loc_text = " ".join(subcell).lower()
    go_terms = extract_go_terms(go_cc)
    go_loc_text = " ".join(go_terms).lower()
    all_loc = hpa_loc_text + " " + uni_loc_text + " " + go_loc_text
    if "nuclear bod" in all_loc or "nuclear speck" in all_loc:
        return "nuclear-body"
    elif "nucleolus" in all_loc or "fibrillar center" in all_loc:
        return "nucleolus"
    elif "nuclear envelope" in all_loc or "nuclear membrane" in all_loc or "nuclear pore" in all_loc:
        return "nuclear-envelope"
    elif "nucleoplasm" in all_loc:
        return "nucleoplasm"
    elif "chromatin" in all_loc or "chromosome" in all_loc:
        return "chromatin"
    elif "nucleus" in all_loc:
        return "nucleoplasm"
    else:
        return "nucleoplasm"


def parse_string_partners(string_data):
    """Parse STRING partners from harvest packet format."""
    if not string_data:
        return []
    partners = []
    for p in string_data:
        partners.append({
            "partner": p.get("partner", ""),
            "score": float(p.get("score", 0)),
            "experimental": float(p.get("experimental", 0)),
        })
    return partners

def parse_intact_partners(intact_data):
    """Parse IntAct partners from harvest packet format."""
    if not intact_data:
        return []
    return intact_data

def generate_report_from_harvest(gene, hp, if_embed=None, if_note="", pae_img=None, pae_note=""):
    # UniProt data
    uni_ok = hp["uniprot"]["ok"]
    uni_data = hp["uniprot"].get("data", {}) if uni_ok else {}
    has_uni = uni_ok and uni_data.get("found", False)

    if has_uni:
        accession = uni_data.get("accession", gene)
        prot_name = uni_data.get("protein_name", f"{gene} protein")
        length_aa = uni_data.get("length_aa", 0)
        mass_kda = uni_data.get("mass_kda", round(length_aa * 0.11, 1))
        subcell = [s.get("location", "") for s in uni_data.get("subcellular_locations", [])]
        go_cc = uni_data.get("go_cc", [])
        function_text = uni_data.get("function", [])
        pdb_raw = uni_data.get("pdb", [])
        pdb_list = [p.get("id", "") for p in pdb_raw]
        aliases = uni_data.get("aliases", [])
    else:
        accession = gene
        prot_name = f"{gene} (UniProt未获取)"
        length_aa = 0
        mass_kda = 0
        subcell = []
        go_cc = []
        function_text = []
        pdb_list = []
        aliases = []

    # AlphaFold data
    af_ok = hp["alphafold"]["ok"]
    af_data = hp["alphafold"].get("data", {}) if af_ok else {}
    af_found = af_ok and af_data.get("found", False)

    if af_found:
        stats = af_data.get("plddt_stats", {})
        plddt = stats.get("mean_plddt", 0)
        pct_gt_90 = stats.get("pct_gt_90", 0)
        pct_70_90 = stats.get("pct_70_90", 0)
        pct_50_70 = stats.get("pct_50_70", 0)
        pct_lt_50 = stats.get("pct_lt_50", 0)
        af_version = af_data.get("latest_version", "?")
        ordered_pct = round(pct_gt_90 + pct_70_90, 1)
    else:
        plddt = 0
        pct_gt_90 = 0
        pct_70_90 = 0
        pct_50_70 = 0
        pct_lt_50 = 0
        af_version = "?"
        ordered_pct = 0

    # PubMed data
    pubmed_ok = hp["pubmed"]["ok"]
    pubmed_data = hp["pubmed"].get("data", {}) if pubmed_ok else {}
    pubmed_strict = pubmed_data.get("strict_count", 0)
    pubmed_broad = pubmed_data.get("broad_count", 0)
    alias_note = pubmed_data.get("alias_note", "")
    key_papers = pubmed_data.get("key_papers", [])

    # HPA data
    hpa_ok = hp["hpa"]["ok"]
    hpa_data = hp["hpa"].get("data", {}) if hpa_ok else {}
    hpa_main = hpa_data.get("subcellular_main_location", [])
    hpa_addl = hpa_data.get("subcellular_additional_location", [])
    hpa_rel = hpa_data.get("reliability_if", "暂无数据")
    hpa_ensembl = hpa_data.get("ensembl", "")
    hpa_subcell_url = hpa_data.get("hpa_subcellular_url", "")
    image_status = hpa_data.get("image_status", "unknown")

    # STRING data
    string_ok = hp["string"]["ok"]
    string_raw = hp["string"].get("data", []) if string_ok else []
    string_p = parse_string_partners(string_raw)

    # IntAct data
    intact_ok = hp["intact"]["ok"]
    intact_raw = hp["intact"].get("data", []) if intact_ok else []
    intact_p = parse_intact_partners(intact_raw)

    # Scoring
    domain_text = get_domain_text(uni_data if has_uni else None)
    nuc = nuclear_score(subcell, hpa_main, hpa_addl, hpa_rel, go_cc, has_uni)
    sz = size_score(length_aa) if length_aa > 0 else 5
    nov = novelty_score(pubmed_strict)
    struct = struct_score(pdb_list, plddt) if af_found else 4
    dom = domain_score(domain_text, plddt)
    ppi = ppi_score(len(string_p), len(intact_p), string_p)
    cross = cross_validation(pdb_list, plddt, subcell, hpa_main, go_cc, len(string_p), len(intact_p), domain_text, has_uni)

    raw = nuc * 4 + sz * 1 + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross
    norm = round(raw / 1.80, 1)

    rejected = nuc <= 3 or pubmed_strict > 100
    status = "rejected" if rejected else "scored"
    dest = determine_dest(nuc, pubmed_strict, hpa_main, hpa_addl, subcell, go_cc)

    # IF note (image content passed in from main)
    if not if_note:
        if image_status == "if_display_images_available" or hpa_rel in ("Approved", "Enhanced", "Supported"):
            if_note = "**IF 图像获取**: 尝试获取IF原图中..."
        else:
            if_note = ("**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。"
                       "核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。")

    # PAE note (image content passed in from main)
    if not pae_note:
        if af_found:
            pae_note = "PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。"
        else:
            pae_note = "AlphaFold 数据未获取，无 PAE 可用。"

    # Descriptions
    nuc_desc_map = {
        9: "多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。",
        8: "主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。",
        7: "主要核定位，HPA 可靠性良好，有辅助数据源支持。",
        6: "存在核定位证据但部分来源支持较弱或缺失。",
        5: "核定位证据存在但较为混杂，部分数据源指向非核区室。",
        4: "核定位信号较弱，多个数据源显示混合定位或非核偏好。",
        3: "核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。",
        2: "核定位证据极弱，主要数据源均不指向细胞核。",
        1: "无核定位证据。",
    }
    nuc_desc = nuc_desc_map.get(nuc, "核定位不确定。")

    if sz >= 10: sz_desc = "大小适中（200-800 aa），适合常规生化实验和结构解析。"
    elif sz >= 8: sz_desc = "大小基本合适，可用于常规实验。"
    elif sz >= 5: sz_desc = "蛋白偏小/偏大，实验操作有一定难度。"
    else: sz_desc = "大小偏离理想范围，实验设计需特殊考虑。"

    if nov >= 10: nov_desc = "极度新颖，几乎未被系统研究（PubMed ≤20篇）。"
    elif nov >= 8: nov_desc = "非常新颖，仅有少数基础研究。"
    elif nov >= 6: nov_desc = "较新颖，有一定研究但存在未探索领域。"
    elif nov >= 4: nov_desc = "已有一定研究基础，但仍存在niche空间。"
    else: nov_desc = "研究基础较多，新颖性有限。"

    pdb_text = ", ".join(pdb_list[:10]) if pdb_list else "无"
    if struct >= 10:
        struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold极高置信度预测（pLDDT={round(plddt,1)}），结构可信度极高。"
    elif struct >= 9:
        struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold高质量预测（pLDDT={round(plddt,1)}），结构可信度高。"
    elif struct >= 8:
        if plddt >= 85:
            struct_desc = f"AlphaFold 极高置信度预测（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构可靠。"
        else:
            struct_desc = f"AlphaFold 高质量预测（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构可靠。"
    elif struct >= 7:
        struct_desc = f"AlphaFold 中等质量（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构基本可用。"
    else:
        struct_desc = f"AlphaFold 预测质量有限（pLDDT={round(plddt,1)}），有序残基占 {ordered_pct}%。"

    if dom >= 9:
        dom_desc = "含明确的核酸结合/染色质相关结构域，多库确认。"
    elif dom >= 8:
        dom_desc = "多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。"
    elif dom >= 7:
        dom_desc = "存在已知结构域注释，可作为功能研究的结构基础。"
    elif dom >= 5:
        dom_desc = "结构域注释有限，AlphaFold预测有可辨识折叠域。"
    else:
        dom_desc = "结构域注释稀疏，属新颖蛋白正常现象。"

    reg = get_reg_partner_info(string_p, intact_p)
    reg_ratio = len(reg) / min(len(string_p), 20) * 100 if string_p else 0
    ppi_desc = f"STRING {len(string_p)} 个预测互作，IntAct {len(intact_p)} 个实验互作。调控相关配体占比 {reg_ratio:.0f}%。"

    papers_text = format_key_papers(key_papers)
    string_table = format_string_table(string_p)
    intact_table = format_intact_table(intact_p)
    go_cc_text = get_go_cc_text(uni_data if has_uni else None)

    if has_uni:
        subcell_text = "; ".join(subcell) if subcell else "无注释"
    else:
        subcell_text = "暂无数据（UniProt获取失败）"

    hpa_loc_text = ", ".join(hpa_main) if hpa_main else ""
    if hpa_addl:
        hpa_loc_text += ("; 额外: " + ", ".join(hpa_addl)) if hpa_loc_text else ", ".join(hpa_addl)
    if not hpa_loc_text:
        hpa_loc_text = "暂无HPA定位数据"

    alias_text = ", ".join(aliases[:5]) if aliases else ""
    mass = mass_kda if mass_kda else (round(length_aa * 0.11, 1) if length_aa else "未知")
    uniprot_url = f"https://www.uniprot.org/uniprotkb/{accession}" if accession else ""

    nov_label = "≤20→10" if pubmed_strict <= 20 else ("≤40→8" if pubmed_strict <= 40 else ("≤60→6" if pubmed_strict <= 60 else ("≤80→4" if pubmed_strict <= 80 else ("≤100→2" if pubmed_strict <= 100 else ">100→REJECTED"))))

    cross_details = []
    if pdb_list and plddt > 0: cross_details.append("PDB + AlphaFold 双源验证: +0.5")
    else: cross_details.append("PDB + AlphaFold 双源验证: +0")
    has_multi_nuc = 0
    if has_uni and subcell: has_multi_nuc += 1
    if hpa_main: has_multi_nuc += 1
    if go_cc: has_multi_nuc += 1
    if has_multi_nuc >= 2: cross_details.append(f"多库定位一致 ({has_multi_nuc}源): +0.5")
    else: cross_details.append("多库定位一致: +0")
    if string_p and intact_p: cross_details.append("STRING + IntAct 双源验证: +0.5")
    else: cross_details.append("STRING + IntAct 双源验证: +0")
    if domain_text and "暂无" not in domain_text and plddt > 70: cross_details.append("结构域 + AlphaFold 质量: +0.5")
    else: cross_details.append("结构域 + AlphaFold 质量: +0")
    if len(pdb_list) >= 3: cross_details.append("PDB 多条目覆盖 (≥3): +1.0")
    else: cross_details.append("PDB 多条目覆盖: +0")

    rejection_reasons = []
    if nuc <= 3:
        rejection_reasons.append(f"核定位证据不足 (核定位得分 {nuc}/10 ≤ 3)")
    if pubmed_strict > 100:
        rejection_reasons.append(f"研究热度过高 (PubMed strict={pubmed_strict}，超过100篇阈值)")

    if rejected:
        title_line = f"## {gene} — REJECTED ({'; '.join(rejection_reasons)})"
    else:
        title_line = f"## {gene} 核蛋白评估报告 (Full Re-evaluation)"

    if_section = ""
    if if_embed:
        if_section = f"\n**IF 图像**:\n{if_embed}\n"

    pae_section = ""
    if pae_img:
        pae_section = f"\n**PAE (Predicted Aligned Error)**:\n{pae_img}\n"
    else:
        pae_section = f"\n**PAE**: {pae_note}\n"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, {"rejected" if rejected else "nuclear-protein"}, evaluation]
status: {status}
---

{title_line}

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene}{f" / {alias_text}" if alias_text else ""} |
| 蛋白名称 | {prot_name} |
| 蛋白大小 | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| UniProt ID | {accession} |
| 评估日期 | {TODAY} |
{if_section}
### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | {nuc}/10 | ×4 | {nuc*4} | HPA: {hpa_loc_text[:60]}; UniProt: {subcell_text[:60]} |
| 蛋白大小 | {sz}/10 | ×1 | {sz} | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| 研究新颖性 | {nov}/10 | ×5 | {nov*5} | PubMed strict={pubmed_strict} 篇 ({nov_label}) |
| 三维结构 | {struct}/10 | ×3 | {struct*3} | AlphaFold v{af_version} pLDDT={round(plddt,1)}; PDB: {pdb_text[:40]} |
| 调控结构域 | {dom}/10 | ×2 | {dom*2} | {domain_text[:60]} |
| PPI 网络 | {ppi}/10 | ×3 | {ppi*3} | STRING {len(string_p)} partners; IntAct {len(intact_p)} interactions |
| 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw}/180** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | {hpa_loc_text} | {hpa_rel if hpa_rel else "暂无"} |
| UniProt | {subcell_text[:100]}{"..." if len(subcell_text) > 100 else ""} | {"Swiss-Prot/TrEMBL" if has_uni else "获取失败"} |

{if_note}

**GO Cellular Component**:
{go_cc_text}

**结论**: {nuc_desc}

#### 3.2 蛋白大小评估

**评价**: {sz_desc}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | {pubmed_strict} |
| PubMed broad count | {pubmed_broad} |
| 别名(未计入scoring) | {alias_note if alias_note else "无"} |

**关键文献**:
{papers_text}

**评价**: {nov_desc}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_version} |
| AlphaFold 平均 pLDDT | {round(plddt,1)} |
| 高置信度残基 (pLDDT>90) 占比 | {pct_gt_90}% |
| 置信残基 (pLDDT 70-90) 占比 | {pct_70_90}% |
| 中等置信 (pLDDT 50-70) 占比 | {pct_50_70}% |
| 低置信 (pLDDT<50) 占比 | {pct_lt_50}% |
| 有序区域 (pLDDT>70) 占比 | {ordered_pct}% |
| 可用 PDB 条目 | {pdb_text} |

{pae_section}
**评价**: {struct_desc}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | {domain_text[:200]} |

**染色质调控潜力分析**: {dom_desc}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
{string_table}

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
{intact_table}

**PPI 互证分析**:
- {"STRING + IntAct 均有数据" if string_p and intact_p else "仅STRING预测" if string_p else "仅IntAct实验" if intact_p else "无PPI数据"}
- STRING partners: {len(string_p)}，IntAct interactions: {len(intact_p)}
- 调控相关比例: {len(reg)} / {min(len(string_p), 20)} = {reg_ratio:.0f}%

**评价**: {ppi_desc}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT={round(plddt,1)} + PDB: {pdb_text[:30]} | pLDDT={round(plddt,1)}, v{af_version} | {"预测+实验" if pdb_list else "仅预测"} |
| 定位 | UniProt + HPA | {subcell_text[:50]} / {hpa_loc_text[:50]} | {"一致" if has_multi_nuc >= 2 else "待确认"} |
| PPI | STRING + IntAct | {len(string_p)} + {len(intact_p)} interactions | {"数据充分" if string_p and intact_p else "数据有限"} |

**互证加分明细**:
{chr(10).join(f"- {d}" for d in cross_details)}
**总分**: +{cross} / max +3

### 4. 总体评价

**推荐等级**: {"⭐" * max(1, min(5, round(norm/20)))}{" (REJECTED)" if rejected else ""}

**核心优势**:
1. {gene} — {prot_name}，{nov_desc}
2. 蛋白大小{length_aa if length_aa else "未知"} aa，{sz_desc}

**风险/不确定性**:
1. {"PubMed " + str(pubmed_strict) + " 篇，研究基础极有限，功能注释不完整" if pubmed_strict <= 20 else "PubMed " + str(pubmed_strict) + " 篇，已有一定研究基础" if pubmed_strict <= 100 else "PubMed " + str(pubmed_strict) + " 篇，研究热度过高（>100），不符合新颖性要求"}
2. {"AlphaFold 预测质量一般（pLDDT=" + str(round(plddt,1)) + "），需要更多实验结构验证" if plddt < 70 and af_found else "结构数据质量可接受" if plddt >= 70 else "结构数据暂缺"}

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
{"- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**" if nuc <= 3 else ""}{"**该蛋白PubMed文献数 " + str(pubmed_strict) + " > 100，研究热度过高，不符合novelty筛选标准。**" if pubmed_strict > 100 and nuc > 3 else ""}

### 5. 数据来源
- UniProt: {uniprot_url}
- Protein Atlas: {hpa_subcell_url if hpa_subcell_url else "https://www.proteinatlas.org/search/" + gene}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{accession}
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: {TODAY}
"""
    return report, dest, rejected


# ============================================================
# MAIN
# ============================================================

def main():
    to_process = []
    for gene in READY:
        complete, cpath = already_complete(gene)
        if complete:
            print(f"  SKIP {gene} - already complete at {cpath}")
            continue
        to_process.append(gene)

    if not to_process:
        print("All genes already have complete reports. Nothing to do.")
        return

    print(f"\n{'='*70}")
    print(f"Processing {len(to_process)} genes from harvest packets...")
    print(f"{'='*70}\n")

    results = []
    for i, gene in enumerate(to_process):
        try:
            hp = load_harvest(gene)
            if not hp:
                print(f"[{i+1}/{len(to_process)}] {gene:12s} -> NO HARVEST PACKET")
                results.append({"gene": gene, "dest": "SKIP", "size": 0, "status": "NO_HP", "rejected": True})
                continue

            print(f"[{i+1}/{len(to_process)}] {gene:12s}", end="", flush=True)

            # Quick pre-check
            pubmed_ok = hp["pubmed"]["ok"]
            pubmed_strict = hp["pubmed"].get("data", {}).get("strict_count", 0) if pubmed_ok else 0

            uni_ok = hp["uniprot"]["ok"]
            uni_data = hp["uniprot"].get("data", {}) if uni_ok else {}
            has_uni = uni_ok and uni_data.get("found", False)
            subcell = [s.get("location", "") for s in uni_data.get("subcellular_locations", [])] if has_uni else []
            go_cc = uni_data.get("go_cc", [])

            hpa_data = hp["hpa"].get("data", {}) if hp["hpa"]["ok"] else {}
            hpa_main = hpa_data.get("subcellular_main_location", [])
            hpa_addl = hpa_data.get("subcellular_additional_location", [])
            hpa_rel = hpa_data.get("reliability_if", "")

            # Quick nuclear score to determine destination first
            nuc_quick = nuclear_score(subcell, hpa_main, hpa_addl, hpa_rel, go_cc, has_uni)
            dest = determine_dest(nuc_quick, pubmed_strict, hpa_main, hpa_addl, subcell, go_cc)

            # IF images (only for non-rejected)
            if_embed = None
            if_note = ""
            if nuc_quick > 3 and pubmed_strict <= 100:
                image_status = hpa_data.get("image_status", "unknown")
                print(" IF...", end="", flush=True)
                if image_status == "if_display_images_available" or hpa_rel in ("Approved", "Enhanced", "Supported"):
                    hpa_ensembl = hpa_data.get("ensembl", "")
                    if_embed, if_note_raw = fetch_if_images_for_gene(gene, dest, hpa_ensembl)
                    if if_note_raw:
                        if_note = f"**IF 图像获取**: {if_note_raw}"

            # PAE image (only for non-rejected, if AF available)
            pae_img = None
            pae_note = ""
            if nuc_quick > 3 and pubmed_strict <= 100:
                accession = gene
                if has_uni:
                    accession = uni_data.get("accession", gene)
                af_ok = hp["alphafold"]["ok"]
                af_data = hp["alphafold"].get("data", {}) if af_ok else {}
                if af_data.get("found"):
                    pae_img, has_pae = download_pae_image(gene, accession, dest)
                    if pae_img:
                        pae_note = pae_img
                    else:
                        pae_note = "PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。"

            # Now generate full report
            print(" report...", end="", flush=True)
            report, dest, rejected = generate_report_from_harvest(gene, hp, if_embed, if_note, pae_img, pae_note)

            report_dir = os.path.join(DETAIL, dest, gene)
            os.makedirs(report_dir, exist_ok=True)
            report_path = os.path.join(report_dir, f"{gene}-evaluation.md")
            with open(report_path, "w") as f:
                f.write(report)

            size = len(report.encode("utf-8"))
            has_180 = "/180" in report
            if size > 2000 and has_180:
                st = "OK"
            elif size <= 2000:
                st = "SHORT"
            else:
                st = "NO_180"

            status_tag = "REJECTED" if rejected else "SCORED"
            print(f" -> {dest:20s} ({size:5d}b) [{st}] {status_tag}")
            results.append({"gene": gene, "dest": dest, "size": size, "status": st, "rejected": rejected})

        except Exception as e:
            print(f"  -> ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append({"gene": gene, "dest": "ERROR", "size": 0, "status": f"ERROR: {e}", "rejected": True})

        if (i + 1) % 5 == 0 and i > 0:
            time.sleep(1)

    print(f"\n{'='*70}")
    ok = sum(1 for r in results if r["status"] == "OK")
    rejected = sum(1 for r in results if r["rejected"])
    scored = sum(1 for r in results if not r["rejected"])
    err = sum(1 for r in results if r["status"].startswith("ERROR"))
    skipped = sum(1 for r in results if r["status"] == "NO_HP")
    print(f"Summary: {ok} OK, {rejected} REJECTED, {scored} SCORED, {err} ERROR, {skipped} SKIPPED")
    dests = sorted(set(r["dest"] for r in results if r["dest"] not in ("ERROR", "SKIP")))
    print(f"Destinations: {', '.join(dests)}")
    print("\nDone.")


if __name__ == "__main__":
    main()
