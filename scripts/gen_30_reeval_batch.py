#!/usr/bin/env python3
"""Generate complete /180 re-evaluation reports for 30 genes from harvest packets.
Downloads and embeds IF images where available. No placeholders."""

import json, os, sys, re, ssl, urllib.request, time

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
PACKET_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
VAULT_PREFIX = "Projects/TEreg-finding/protein-interested/detail"

GENES = [
    "ARK2N", "BRME1", "BROX", "BRPF3", "BSPRY", "BTBD1", "BTBD18", "BTBD3",
    "BTF3L4", "BTNL9", "C10orf71", "C10orf90", "C11orf58", "C11orf68",
    "C14orf39", "C19orf47", "C19orf84", "C1orf146", "C1orf174", "C1orf21",
    "C1orf226", "C1orf35", "C1orf52", "C2CD4A", "C2CD4B", "C2CD6",
    "C2CD4C", "C2CD4D", "C2orf50", "C3orf36",
]

# SSL context for Protein Atlas
ctx = ssl.create_default_context()

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None

def fetch_text(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception:
        return None

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

# --- Scoring helpers (identical to gen_full_reeval.py) ---

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
    domain_count = domains_text.count("IPR") + domains_text.count("PF")
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

def cross_validation(pdb_ids, plddt, uni_loc, hpa_loc, go_cc, string_n, intact_n, domains, has_uni):
    pts = 0
    if pdb_ids and plddt > 0: pts += 0.5
    has_multi_nuc = 0
    if has_uni and uni_loc: has_multi_nuc += 1
    if hpa_loc: has_multi_nuc += 1
    if go_cc: has_multi_nuc += 1
    if has_multi_nuc >= 2: pts += 0.5
    if string_n > 0 and intact_n > 0: pts += 0.5
    if domains and plddt > 70: pts += 0.5
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
        go_text = " ".join(extract_go_terms(go_cc_terms)).lower()
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

def format_string_table(partners):
    if not partners:
        return "| — | — | — | — |"
    lines = []
    for p in partners[:10]:
        name = p.get("partner", "?")
        score = p.get("score", 0)
        exp = p.get("experimental", 0)
        lines.append(f"| {name} | {score:.3f} | {exp:.3f} | — |")
    return "\n".join(lines)

def format_intact_table(partners, gene):
    if not partners:
        return "| — | — | — |"
    seen = set()
    lines = []
    for p in partners:
        partner = p.get("partner", "")
        if partner.lower() in seen: continue
        seen.add(partner.lower())
        if len(seen) > 10: break
        method = p.get("method", "—")
        pmid = p.get("pmid", "—")
        lines.append(f"| {partner} | {method[:50]} | {pmid[:30]} |")
    return "\n".join(lines) if lines else "| — | — | — |"

def get_domain_text(uni_data):
    if not uni_data: return "暂无数据 (UniProt未获取)"
    interpro = uni_data.get("interpro", [])
    pfam = uni_data.get("pfam", [])
    ipr_ids = [i.get("id", "") for i in interpro]
    pf_ids = [p.get("id", "") for p in pfam]
    parts = []
    if ipr_ids: parts.append("InterPro: " + ", ".join(ipr_ids[:5]))
    if pf_ids: parts.append("Pfam: " + ", ".join(pf_ids[:3]))
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
    return "\n".join(f"- {cc.get('term', str(cc))} ({cc.get('id','')})" for cc in go_cc[:6])

def get_reg_partner_info(string_partners, intact_partners, gene):
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


# --- IF Image fetching ---

def search_ensg(gene):
    """Search Protein Atlas for ENSG ID."""
    data = fetch_json(f"https://www.proteinatlas.org/search/{gene}?format=json")
    if isinstance(data, list) and len(data) > 0:
        return data[0].get("Ensembl")
    return None

def extract_if_data(ensg):
    """Extract IF cell line data from Protein Atlas XML."""
    text = fetch_text(f"https://www.proteinatlas.org/{ensg}.xml")
    if not text:
        return None

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

    return results

def fetch_if_images_for_gene(gene, category):
    """Download IF images and return embedding markdown or descriptive note."""
    gene_dir = os.path.join(DETAIL, category, gene)
    if_dir = os.path.join(gene_dir, "IF_images")
    img_prefix = f"{VAULT_PREFIX}/{category}/{gene}/IF_images"

    # Check for existing images
    existing_jpgs = []
    if os.path.isdir(if_dir):
        existing_jpgs = [f for f in os.listdir(if_dir) if f.endswith('.jpg') and 'thumb' not in f]

    if existing_jpgs:
        # Images already exist, build embedding
        jpg_files = [f for f in existing_jpgs if 'thumb' not in f][:2]
        lines = []
        for jpg in jpg_files:
            base = jpg.replace('.jpg', '').replace('_1', '')
            cell_name = base.replace('-', ' ').replace('_', ' ')
            lines.append(f"![[{img_prefix}/{jpg}|{cell_name}]]")
        return "\n".join(lines), "IF图像已嵌入"

    # Fetch from Protein Atlas
    ensg = search_ensg(gene)
    if not ensg:
        return None, "Protein Atlas 中未找到该基因条目（无ENSG匹配），无法获取IF原图。"

    if_data = extract_if_data(ensg)
    if not if_data:
        return None, "Protein Atlas 检索页无可用 subcellular IF 原图（图像未检测到或数据不可用）。"

    # Prefer nucleoplasm cell lines
    nuc_only = [d for d in if_data if all('nucleoplasm' in l.lower() for l in d['locations'])]
    others = [d for d in if_data if d not in nuc_only]
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


# --- PAE image handling ---

def check_pae_image(gene, category):
    """Check if PAE image exists for this gene."""
    paths_to_check = [
        os.path.join(DETAIL, category, gene, f"{gene}-PAE.png"),
        os.path.join(DETAIL, "rejected", gene, f"{gene}-PAE.png"),
    ]
    for p in paths_to_check:
        if os.path.exists(p) and os.path.getsize(p) > 100:
            return f"![[{VAULT_PREFIX}/{category}/{gene}/{gene}-PAE.png]]"
    return None


# --- Main report generator ---

def generate_report(gene):
    packet_path = os.path.join(PACKET_DIR, f"{gene}.json")

    # Handle missing packets (4 genes: C2CD4C, C2CD4D, C2orf50, C3orf36)
    if not os.path.exists(packet_path):
        return generate_no_packet_report(gene), "rejected"

    with open(packet_path) as f:
        pkt = json.load(f)

    uni = pkt.get("uniprot", {}).get("data") if pkt.get("uniprot", {}).get("ok") else None
    has_uni = uni is not None
    af = pkt.get("alphafold", {}).get("data") if pkt.get("alphafold", {}).get("ok") else None
    af_found = af and af.get("found")
    pubmed = pkt.get("pubmed", {}).get("data", {}) if pkt.get("pubmed", {}).get("ok") else {}
    string_p = pkt.get("string", {}).get("data", []) if pkt.get("string", {}).get("ok") else []
    intact_p = pkt.get("intact", {}).get("data", []) if pkt.get("intact", {}).get("ok") else []
    hpa = pkt.get("hpa", {}).get("data", {}) if pkt.get("hpa", {}).get("ok") else {}

    pubmed_strict = pubmed.get("strict_count", 0)
    key_papers = pubmed.get("key_papers", [])

    if has_uni:
        accession = uni.get("accession", gene)
        prot_name = uni.get("protein_name", f"{gene} protein")
        length_aa = uni.get("length_aa", 0)
        mass_kda = uni.get("mass_kda", round(length_aa * 0.11, 1))
        subcell = [s.get("location", "") for s in uni.get("subcellular_locations", [])]
        go_cc = uni.get("go_cc", [])
        function_text = uni.get("function", [])
        pdb_list = [p.get("id", "") for p in uni.get("pdb", [])]
        uniprot_interactions = uni.get("uniprot_interactions", [])
        aliases = uni.get("aliases", [])
    else:
        accession = gene
        prot_name = f"{gene} (UniProt未获取)"
        length_aa = 0
        mass_kda = 0
        subcell = []
        go_cc = []
        function_text = []
        pdb_list = []
        uniprot_interactions = []
        aliases = []

    if af_found:
        plddt = af.get("plddt_stats", {}).get("mean_plddt", 0)
        pct_gt_90 = af.get("plddt_stats", {}).get("pct_gt_90", 0)
        pct_70_90 = af.get("plddt_stats", {}).get("pct_70_90", 0)
        pct_50_70 = af.get("plddt_stats", {}).get("pct_50_70", 0)
        pct_lt_50 = af.get("plddt_stats", {}).get("pct_lt_50", 0)
        af_version = af.get("latest_version", "?")
        ordered_pct = round(pct_gt_90 + pct_70_90, 1)
    else:
        plddt = 0
        pct_gt_90 = 0
        pct_70_90 = 0
        pct_50_70 = 0
        pct_lt_50 = 0
        af_version = "?"
        ordered_pct = 0

    hpa_main = hpa.get("subcellular_main_location", [])
    hpa_addl = hpa.get("subcellular_additional_location", [])
    hpa_rel = hpa.get("reliability_if", "暂无数据")
    hpa_gene_url = hpa.get("hpa_gene_url", "")
    hpa_subcell_url = hpa.get("hpa_subcellular_url", "")
    hpa_status = hpa.get("status", "unknown")
    image_status = hpa.get("image_status", "unknown")

    domain_text = get_domain_text(uni)

    # Calculate scores
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

    # Determine destination directory
    if rejected:
        dest = "rejected"
    else:
        hpa_loc_text = ", ".join(hpa_main + hpa_addl).lower()
        uni_loc_text = " ".join(subcell).lower()
        go_loc_text = " ".join(extract_go_terms(go_cc)).lower()
        all_loc = hpa_loc_text + " " + uni_loc_text + " " + go_loc_text
        if "nuclear bod" in all_loc or "nuclear speck" in all_loc:
            dest = "nuclear-body"
        elif "nucleolus" in all_loc or "fibrillar center" in all_loc:
            dest = "nucleolus"
        elif "nuclear envelope" in all_loc or "nuclear membrane" in all_loc or "nuclear pore" in all_loc:
            dest = "nuclear-envelope"
        elif "nucleoplasm" in all_loc:
            dest = "nucleoplasm"
        elif "chromatin" in all_loc or "chromosome" in all_loc:
            dest = "chromatin"
        else:
            dest = "nucleoplasm"

    # --- IF Image fetching ---
    if_embed = None
    if_note = ""
    if image_status == "if_display_images_available":
        if_embed, if_note = fetch_if_images_for_gene(gene, "rejected")  # Try rejected first, will update path later
        if if_embed is None and if_note:
            if_note = "**IF 图像获取**: " + if_note
        elif if_note:
            if_note = f"**IF 图像获取**: {if_note}"
    else:
        if_note = ("**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。"
                   "核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。")

    # --- PAE image handling ---
    pae_img = None
    # Check if PAE was pre-generated
    pae_path = os.path.join(DETAIL, "rejected", gene, f"{gene}-PAE.png")
    if os.path.exists(pae_path) and os.path.getsize(pae_path) > 100:
        pae_img = f"![[{VAULT_PREFIX}/rejected/{gene}/{gene}-PAE.png]]"
    if pae_img:
        pae_note = pae_img
    else:
        pae_note = "PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。"

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
    else: nov_desc = "有一定研究基础，但仍存在niche空间。"

    pdb_text = ", ".join(pdb_list[:10]) if pdb_list else "无"
    if struct >= 10:
        if plddt >= 85:
            struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold极高置信度预测（pLDDT={plddt}），结构可信度极高。"
        else:
            struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold预测（pLDDT={plddt}），实验结构可用。"
    elif struct >= 9:
        struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold高质量预测（pLDDT={plddt}），结构可信度高。"
    elif struct >= 8:
        if plddt >= 85:
            struct_desc = f"AlphaFold 极高置信度预测（pLDDT={plddt}，有序区 {ordered_pct}%），结构可靠。"
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

    reg = get_reg_partner_info(string_p, intact_p, gene)
    reg_ratio = len(reg) / min(len(string_p), 20) * 100 if string_p else 0
    ppi_desc = f"STRING {len(string_p)} 个预测互作，IntAct {len(intact_p)} 个实验互作。调控相关配体占比 {reg_ratio:.0f}%。"

    papers_text = format_key_papers(key_papers)
    string_table = format_string_table(string_p)
    intact_table = format_intact_table(intact_p, gene)
    go_cc_text = get_go_cc_text(uni)

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

    # Cross-validation details
    cross_details = []
    if pdb_list and plddt > 0: cross_details.append("PDB + AlphaFold 双源验证: +0.5")
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

    # Rejection reasons
    rejection_reasons = []
    if nuc <= 3:
        rejection_reasons.append(f"核定位证据不足 (核定位得分 {nuc}/10 ≤ 3)")
    if pubmed_strict > 100:
        rejection_reasons.append(f"研究热度过高 (PubMed strict={pubmed_strict}，超过100篇阈值)")

    if rejected:
        title_line = f"## {gene} — REJECTED ({'; '.join(rejection_reasons)})"
    else:
        title_line = f"## {gene} 核蛋白评估报告 (Full Re-evaluation)"

    # Build the IF image section
    if if_embed:
        if_section = f"\n**IF 图像**:\n{if_embed}\n"
        if_note = ""
    else:
        if_section = ""

    # Build PAE section
    pae_section = ""
    if pae_img:
        pae_section = f"\n**PAE (Predicted Aligned Error)**:\n{pae_img}\n"
    else:
        pae_section = f"\n**PAE**: {pae_note}\n"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-06-03
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
| 评估日期 | 2026-06-03 |
{if_section}
### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | {nuc}/10 | ×4 | {nuc*4} | HPA: {hpa_loc_text[:60]}; UniProt: {subcell_text[:60]} |
| 📏 蛋白大小 | {sz}/10 | ×1 | {sz} | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| 🆕 研究新颖性 | {nov}/10 | ×5 | {nov*5} | PubMed strict={pubmed_strict} 篇 ({nov_label}) |
| 🏗️ 三维结构 | {struct}/10 | ×3 | {struct*3} | AlphaFold v{af_version} pLDDT={round(plddt,1)}; PDB: {pdb_text[:40]} |
| 🧬 调控结构域 | {dom}/10 | ×2 | {dom*2} | {domain_text[:60]} |
| 🔗 PPI 网络 | {ppi}/10 | ×3 | {ppi*3} | STRING {len(string_p)} partners; IntAct {len(intact_p)} interactions |
| ➕ 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw}/180** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | {hpa_loc_text} | {hpa_rel if hpa_rel else "暂无"} |
| UniProt | {subcell_text[:80]}{"..." if len(subcell_text) > 80 else ""} | {"Swiss-Prot/TrEMBL" if has_uni else "获取失败"} |

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
| PubMed broad count | {pubmed.get("broad_count", "N/A")} |
| 别名(未计入scoring) | {pubmed.get("alias_note", "无")} |

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
| InterPro/Pfam | {domain_text[:150]} |

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
2. {"AlphaFold 预测质量一般（pLDDT=" + str(round(plddt,1)) + "），需要更多实验结构验证" if plddt < 70 else "结构数据质量可接受" if plddt >= 70 else "结构数据暂缺"}

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
- Packet data timestamp: {pkt.get("timestamp", "N/A")}
"""
    return report, dest


def generate_no_packet_report(gene):
    """Generate a minimal report for genes with no harvest packet."""
    return f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## {gene} — REJECTED (数据不可用)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | {gene} |
| 数据状态 | 无 harvest packet |
| 评估日期 | 2026-06-03 |

### 2. 淘汰理由

**数据不可用**: 该基因在 harvest_packets 目录中无对应 JSON 文件，无法进行 /180 标准评分。可能原因包括：
- 该基因末被纳入原始 harvest pipeline
- UniProt 中无对应的人类蛋白条目
- 基因符号命名变化

### 3. 后续建议

- [ ] 确认基因符号是否为新命名（检查 HGNC 最新命名规范）
- [ ] 在 UniProt 检索对应的人类蛋白条目
- [ ] 如找到有效条目，重新运行 harvest pipeline 生成数据包

### 4. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/?query={gene}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
"""


# --- Main execution ---

print("Generating 30 complete /180 re-evaluation reports...")
print("=" * 70)

results = []
for i, gene in enumerate(GENES):
    try:
        print(f"\n[{i+1}/30] {gene}...", end=" ", flush=True)
        report, dest = generate_report(gene)
        report_dir = os.path.join(DETAIL, dest, gene)
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, f"{gene}-evaluation.md")
        with open(report_path, "w") as f:
            f.write(report)
        size = len(report.encode("utf-8"))
        has_180 = "/180" in report
        if size > 2000 and has_180:
            status = "OK"
        elif size <= 2000:
            status = "SHORT"
        else:
            status = "NO_180"
        print(f"-> {dest:20s} ({size:5d} bytes) [{status}]")
        results.append({"gene": gene, "dest": dest, "size": size, "status": status})
    except Exception as e:
        print(f"-> ERROR: {e}")
        import traceback
        traceback.print_exc()
        results.append({"gene": gene, "dest": "ERROR", "size": 0, "status": f"ERROR: {e}"})

    # Rate limiting for Protein Atlas API
    if i > 0 and i % 5 == 0:
        time.sleep(1)

print("\n" + "=" * 70)
ok = sum(1 for r in results if r["status"] == "OK")
short = sum(1 for r in results if r["status"] == "SHORT")
no_180 = sum(1 for r in results if r["status"] == "NO_180")
err = sum(1 for r in results if r["status"].startswith("ERROR"))
print(f"Summary: {ok} OK, {short} SHORT, {no_180} NO_180, {err} ERROR")
print(f"Destinations: {', '.join(sorted(set(r['dest'] for r in results)))}")
print("\nDone.")
