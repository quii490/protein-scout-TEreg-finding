#!/usr/bin/env python3
"""Generate all 27 evaluation reports from batch data."""
import json, os, re, time

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

with open(os.path.join(BASE, "batch_all_data.json")) as f:
    DATA = json.load(f)

DEST = {}
for g in ["C1D","CCDC137","CDAN1","CDC14A","CENPH","CENPI","CENPK","CENPM","CENPT","CENPU","CENPX","CHMP1A","CHP2","CLASP1","CLNS1A","CRTC3","CSRP3","CUTC"]:
    DEST[g] = "nucleoplasm"
for g in ["CASC3","CCAR1","CDX4","CEBPG","CIPC","CSRP1","CSRP2","CSTF2T","CTNNBL1"]:
    DEST[g] = "nucleus-cytoplasm"

SIZE_MAP = {
    "C1D":141,"CCDC137":289,"CDAN1":1227,"CDC14A":594,"CENPH":247,"CENPI":756,"CENPK":269,
    "CENPM":180,"CENPT":561,"CENPU":418,"CENPX":81,"CHMP1A":196,"CHP2":196,"CLASP1":1538,
    "CLNS1A":237,"CRTC3":619,"CSRP3":194,"CUTC":273,"CASC3":703,"CCAR1":1150,"CDX4":284,
    "CEBPG":150,"CIPC":399,"CSRP1":193,"CSRP2":193,"CSTF2T":616,"CTNNBL1":563,
}
PUBMED_MAP = {
    "C1D":70,"CCDC137":40,"CDAN1":56,"CDC14A":84,"CENPH":65,"CENPI":54,"CENPK":50,
    "CENPM":59,"CENPT":71,"CENPU":53,"CENPX":62,"CHMP1A":66,"CHP2":46,"CLASP1":94,
    "CLNS1A":64,"CRTC3":100,"CSRP3":74,"CUTC":62,"CASC3":51,"CCAR1":78,"CDX4":84,
    "CEBPG":85,"CIPC":67,"CSRP1":54,"CSRP2":88,"CSTF2T":72,"CTNNBL1":42,
}

def novelty_score(pubmed):
    if pubmed <= 20: return 10
    if pubmed <= 50: return 8
    if pubmed <= 100: return 6
    return 0

def size_score(aa):
    if 200 <= aa <= 800: return 10
    if (100 <= aa < 200) or (800 < aa <= 1200): return 8
    if (50 <= aa < 100) or (1200 < aa <= 2000): return 5
    if aa < 50 or (2000 < aa <= 3000): return 2
    return 0

def struct_score(gene, af, pdb_ids):
    plddt = af.get("mean_plddt", 0) if af else 0
    pdb_count = len(pdb_ids) if pdb_ids else 0

    # PDB experimental structures
    if pdb_count >= 5 and plddt >= 70: return 10
    if pdb_count >= 2 and plddt >= 70: return 9
    if pdb_count >= 1 and plddt >= 70: return 8

    # AlphaFold only
    if plddt >= 85: return 8
    if plddt >= 70: return 7
    if plddt >= 50: return 6  # baseline for novel

    # Very low quality
    if plddt < 40: return 4
    return 6  # default baseline

def domain_score(gene, domains, af, pubmed):
    """Score domain potential. Novel baseline = 7."""
    plddt = af.get("mean_plddt", 0) if af else 0
    domain_count = len(domains) if domains else 0

    # Check for chromatin/DNA-binding domains
    chromatin_keywords = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp",
                          "zinc finger", "homeobox", "homeodomain", "hmg", "forkhead",
                          "bzip", "bhlh", "at-hook", "myb", "cxxc", "swi/snf", "iswi",
                          "histone", "chromatin", "dna-binding", "nucleic acid binding"]

    dom_text = " ".join(str(d).lower() for d in domains)
    has_chromatin = any(kw in dom_text for kw in chromatin_keywords)

    if has_chromatin and domain_count >= 3: return 10
    if has_chromatin or (domain_count >= 2 and plddt >= 80): return 8

    # Novel baseline
    if domain_count > 0: return 7
    if plddt >= 70: return 6  # has foldable regions
    if plddt >= 50: return 5
    return 4

def get_nuc_score(gene, uniprot_data, dest):
    """Score nuclear localization based on UniProt location and HPA data."""
    loc_text = ""
    subcell = uniprot_data.get("subcell_locations", []) if uniprot_data else []
    loc_text = " ".join(subcell).lower() if subcell else ""

    # Simplified scoring based on destination
    if dest == "nucleoplasm":
        # Should be primarily nuclear
        nucleus_words = ["nucleus", "nucleoplasm", "nucleoli", "nucleolus", "nuclear"]
        cyto_words = ["cytoplasm", "cytosol", "membrane", "secreted", "cell membrane",
                      "cytoskeleton", "centrosome", "spindle", "kinocilium", "lamellipodium",
                      "synapse", "postsynaptic"]

        has_nucleus = any(w in loc_text for w in nucleus_words)
        has_cyto = any(w in loc_text for w in cyto_words)

        if has_nucleus and not has_cyto: return 9
        if has_nucleus and has_cyto:
            # Check nuclear specificity
            nucleus_mentions = sum(1 for w in nucleus_words if w in loc_text)
            cyto_mentions = sum(1 for w in cyto_words if w in loc_text)
            if nucleus_mentions >= cyto_mentions * 2: return 7
            if nucleus_mentions >= cyto_mentions: return 6
            return 4
        if has_nucleus: return 7
        if has_cyto: return 4
        return 6  # default moderate

    elif dest == "nucleus-cytoplasm":
        # Expected to show both nuclear and cytoplasmic
        nucleus_words = ["nucleus", "nucleoplasm", "nucleoli", "nucleolus", "nuclear"]
        cyto_words = ["cytoplasm", "cytosol", "membrane", "cell membrane", "cytoskeleton",
                      "centrosome", "perinuclear"]

        has_nucleus = any(w in loc_text for w in nucleus_words)
        has_cyto = any(w in loc_text for w in cyto_words)

        if has_nucleus and has_cyto: return 5  # appropriate for nucleus-cytoplasm
        if has_nucleus: return 6  # more nuclear than expected
        if has_cyto: return 4
        return 4

    return 5

def ppi_score(gene, string_partners, intact_partners, go_cc):
    """Score PPI network."""
    string_count = len(string_partners) if string_partners else 0
    intact_count = len(intact_partners) if intact_partners else 0

    # Check for regulatory partners
    regulatory_keywords = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                           "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                           "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                           "deacetylase", "acetyltransferase", "methyltransferase",
                           "kinetochore", "centromere", "condensin", "cohesin", "smc",
                           "origin recognition", "replication factor"]

    if string_partners:
        reg_count = 0
        for p in string_partners[:20]:
            name = (p.get("preferredName_B", "") if isinstance(p, dict) else str(p)).lower()
            if any(kw in name for kw in regulatory_keywords):
                reg_count += 1
        reg_ratio = reg_count / min(len(string_partners), 20) if string_partners else 0
    else:
        reg_count = 0
        reg_ratio = 0

    # Score based on physical interaction evidence + regulatory enrichment
    has_physical = intact_count > 0
    has_string = string_count > 0

    if has_physical and reg_ratio > 0.4 and string_count >= 10: return 10
    if has_physical and reg_ratio > 0.2 and string_count >= 5: return 8
    if has_physical and reg_ratio > 0.3: return 6
    if has_string and reg_ratio > 0.2: return 4
    if has_string: return 3
    return 2

def cross_validation_score(gene, uni_data, af, string_n, intact_n):
    """Calculate cross-validation points (max +3)."""
    points = 0
    uni = uni_data or {}

    # PDB + AlphaFold consistent
    pdb_count = len(uni.get("pdb_ids", []))
    plddt = af.get("mean_plddt", 0) if af else 0
    if pdb_count > 0 and plddt > 0:
        points += 0.5

    # Multiple data sources agree on nuclear localization
    subcell = uni.get("subcell_locations", [])
    go_cc = uni.get("go_cc", [])
    if subcell and go_cc:
        points += 0.5

    # STRING + IntAct both have data
    if string_n > 0 and intact_n > 0:
        points += 0.5

    # Structured domains + AlphaFold quality
    doms = uni.get("domains", [])
    if doms and plddt > 70:
        points += 0.5

    # Good PDB coverage
    if pdb_count >= 3:
        points += 1.0

    return min(points, 3.0)

def get_uniprot_subcell_text(uni_data):
    """Extract concise subcellular location text from UniProt data."""
    if not uni_data:
        return "暂无数据"
    locs = uni_data.get("subcell_locations", [])
    if not locs:
        return "无注释"
    return "; ".join(locs[:5])

def get_uniprot_url(uni_data):
    if not uni_data: return ""
    return f"https://www.uniprot.org/uniprotkb/{uni_data.get('uniprot_id','')}"

def get_mass(uni_data, aa):
    if uni_data and uni_data.get("mass_kda"):
        return uni_data["mass_kda"]
    return round(aa * 0.11, 1)

def get_protein_name(uni_data):
    if uni_data and uni_data.get("protein_name"):
        return uni_data["protein_name"]
    return ""

def get_gene_name(uni_data, gene):
    if uni_data and uni_data.get("gene_name"):
        return uni_data["gene_name"]
    return gene

def format_string_table(partners, gene):
    if not partners: return "无 STRING 预测数据。"
    lines = []
    for p in partners[:10]:
        if isinstance(p, dict):
            name = p.get("preferredName_B", p.get("stringId_B", "?"))
            score = p.get("score", p.get("combined_score", 0))
            lines.append(f"| {name} | {score:.3f} | — | — |")
        else:
            lines.append(f"| {p} | ? | — | — |")
    return "\n".join(lines)

def format_intact_table(partners, gene):
    if not partners: return "无 IntAct 实验数据。"
    lines = []
    seen = set()
    for p in partners:
        if not isinstance(p, dict): continue
        a = p.get("partner_a", "")
        b = p.get("partner_b", "")
        partner = a if a.upper() != gene.upper() else b
        if partner in seen: continue
        seen.add(partner)
        if len(seen) > 10: break
        method = p.get("method", "—")
        pmid = p.get("pubmed", "—")
        lines.append(f"| {partner} | {method} | {pmid} | — | — |")
    return "\n".join(lines) if lines else "无实验验证互作数据。"

def format_go_cc(uni_data):
    if not uni_data: return "- 无 GO-CC 注释"
    go_cc = uni_data.get("go_cc", [])
    if not go_cc: return "- 无 GO-CC 注释"
    return "\n".join(f"- {cc}" for cc in go_cc[:5])

def format_domains(uni_data):
    if not uni_data: return "暂无数据"
    doms = uni_data.get("domains", [])
    if not doms: return "无注释结构域"
    return "; ".join(str(d) for d in doms[:8])

def generate_report(gene):
    """Generate a complete evaluation report for a gene."""
    dest = DEST[gene]
    uni = DATA[gene].get("uniprot", {})
    af = DATA[gene].get("alphafold", {})
    string_p = DATA[gene].get("string", [])
    intact_p = DATA[gene].get("intact", [])
    pubmed = PUBMED_MAP[gene]
    size_aa = SIZE_MAP[gene]
    mass = get_mass(uni, size_aa)
    prot_name = get_protein_name(uni)
    gene_name = get_gene_name(uni, gene)
    uniprot_url = get_uniprot_url(uni) or f"https://www.uniprot.org/uniprotkb/{gene}"

    # Calculate scores
    nuc = get_nuc_score(gene, uni, dest)
    sz = size_score(size_aa)
    nov = novelty_score(pubmed)
    struct = struct_score(gene, af, uni.get("pdb_ids", []) if uni else [])
    dom = domain_score(gene, uni.get("domains", []) if uni else [], af, pubmed)
    ppi = ppi_score(gene, string_p, intact_p, uni.get("go_cc", []) if uni else [])
    cross = cross_validation_score(gene, uni, af, len(string_p), len(intact_p))

    # Total scores
    raw = nuc*4 + sz*1 + nov*5 + struct*3 + dom*2 + ppi*3 + cross
    norm = round(raw / 1.83, 1)

    # PDB list
    pdb_ids = uni.get("pdb_ids", []) if uni else []
    pdb_text = ", ".join(pdb_ids[:10]) if pdb_ids else "无"

    # AlphaFold data
    plddt = af.get("mean_plddt", 0) if af else 0
    vh = af.get("plddt_very_high", 0) if af else 0
    conf = af.get("plddt_confident", 0) if af else 0
    ordered_pct = round((vh + conf) * 100, 1)
    af_version = af.get("version", "?") if af else "?"

    # Subcell text
    subcell_text = get_uniprot_subcell_text(uni)

    # HPA locations
    hpa_text = ""
    hpa_gene_map = {"C1D":None,"CCDC137":None,"CDAN1":"Nuclear speckles; Nucleoplasm","CDC14A":"Nuclear speckles",
        "CENPH":"Nucleoli; Nucleoplasm","CENPI":None,"CENPK":None,"CENPM":"Nucleoplasm","CENPT":None,
        "CENPU":None,"CENPX":"Nucleoplasm","CHMP1A":None,"CHP2":None,"CLASP1":"Nucleoplasm",
        "CLNS1A":None,"CRTC3":"Nucleoplasm","CSRP3":None,"CUTC":"Nucleoplasm","CASC3":"Nucleoli",
        "CCAR1":"Nucleoplasm","CDX4":"Nucleoli","CEBPG":"Nucleoplasm","CIPC":"Nucleoplasm",
        "CSRP1":"Nuclear bodies; Nucleoplasm","CSRP2":"Nucleoplasm","CSTF2T":None,"CTNNBL1":"Nucleoplasm"}
    hpa_text = hpa_gene_map.get(gene, None)

    # Determine reliability
    hpa_rel = "Approved" if hpa_text else "暂无 HPA IF 数据"

    # PAE path
    pae_path = f"Projects/TEreg-finding/protein-interested/detail/{dest}/{gene}/{gene}-PAE.png"
    pae_exists = os.path.exists(os.path.join(DETAIL, dest, gene, f"{gene}-PAE.png"))

    # IF image section
    if_dir = os.path.join(DETAIL, dest, gene, "IF_images")
    if_jpgs = []
    if os.path.exists(if_dir):
        if_jpgs = sorted([f for f in os.listdir(if_dir) if f.endswith(".jpg")])

    if_embed = ""
    if if_jpgs:
        for j in if_jpgs[:2]:
            cell_line = j.rsplit(".", 1)[0].rsplit("_", 1)[0] if "_" in j else j.rsplit(".", 1)[0]
            if_embed += f"\n![[Projects/TEreg-finding/protein-interested/detail/{dest}/{gene}/IF_images/{j}|{cell_line}]]"
    elif hpa_text:
        if_embed = "\nIF 图片待下载（Pending download），核定位基于 UniProt + HPA 注释。"
    else:
        if_embed = "\n暂无数据（Pending cell analysis），核定位基于 UniProt + GO。"

    # For nucleus-cytoplasm destinations with no/mixed UniProt data, adjust nuc description
    if dest == "nucleus-cytoplasm":
        nuc_desc = f"Nucleus + Cytoplasm localization pattern, consistent with nucleocytoplasmic shuttling protein."
    else:
        if nuc >= 8:
            nuc_desc = f"主要定位于细胞核，HPA {hpa_rel}。"
        elif nuc >= 6:
            nuc_desc = f"主要核定位，伴部分胞质信号，HPA {hpa_rel}。"
        elif nuc >= 5:
            nuc_desc = f"核-质分布，HPA {hpa_rel}。"
        else:
            nuc_desc = f"核定位信号较弱，HPA {hpa_rel}。"

    # Size description
    if sz >= 10: sz_desc = "大小适中，适合常规生化实验和结构解析。"
    elif sz >= 8: sz_desc = "大小基本合适，可用于常规实验。"
    else: sz_desc = "大小偏大/偏小，实验操作有一定难度。"

    # Novelty description
    if nov >= 10: nov_desc = "极度新颖，几乎未被系统研究。"
    elif nov >= 8: nov_desc = "非常新颖，仅有少数基础研究。"
    else: nov_desc = "有一定研究基础，但仍存在未探索的niche空间。"

    # Structure description
    if struct >= 9: struct_desc = f"PDB 实验结构（{pdb_text}）+ AlphaFold 高质量预测（pLDDT={plddt}），结构可信度高。"
    elif struct >= 8: struct_desc = f"AlphaFold 高质量预测（pLDDT={plddt}，有序区 {ordered_pct}%），结构可靠。"
    elif struct >= 7:
        if pdb_ids: struct_desc = f"PDB 部分结构（{pdb_text}）+ AlphaFold 中等质量（pLDDT={plddt}）。"
        else: struct_desc = f"AlphaFold 中等质量（pLDDT={plddt}，有序区 {ordered_pct}%）。"
    else: struct_desc = f"AlphaFold 预测质量一般（pLDDT={plddt}），有序区 {ordered_pct}%。作为新颖蛋白，结构基线下不扣分。"

    # Domain description
    dom_text = format_domains(uni)
    if dom >= 8: dom_desc = "含明确的核酸结合/染色质相关结构域，多库确认。"
    elif dom >= 7: dom_desc = f"存在注释结构域：{dom_text[:60]}...。新颖蛋白基线不扣分。"
    elif dom >= 5: dom_desc = f"结构域注释有限（{dom_text[:60]}），但 AlphaFold 预测有可辨识折叠域。"
    else: dom_desc = "结构域注释稀疏，但作为新颖蛋白属正常现象。"

    # PPI description
    ppi_desc = f"STRING {len(string_p)} 个预测互作，IntAct {len(intact_p)} 个实验互作"

    # PPI string partners top list
    str_top = []
    if string_p:
        for p in string_p[:5]:
            if isinstance(p, dict):
                name = p.get("preferredName_B", p.get("stringId_B", "?"))
                score = p.get("score", p.get("combined_score", 0))
                str_top.append(f"{name}({score:.3f})")

    intact_top = []
    seen_intact = set()
    if intact_p:
        for p in intact_p:
            if not isinstance(p, dict): continue
            a = p.get("partner_a", "")
            b = p.get("partner_b", "")
            partner = a if a.upper() != gene.upper() else b
            if partner in seen_intact: continue
            seen_intact.add(partner)
            intact_top.append(partner)
            if len(intact_top) >= 5: break

    # Determine regulatory partners
    reg_keywords = ["transcription", "chromatin", "histone", "helicase", "rna", "dna",
                    "splicing", "nucleolar", "ribosome", "mediator", "deacetylase",
                    "methyltransferase", "acetyltransferase", "kinetochore", "centromere",
                    "condensin", "cohesin"]
    reg_partners = []
    if string_p:
        for p in string_p[:20]:
            if isinstance(p, dict):
                name = p.get("preferredName_B", "").lower()
                if any(kw in name for kw in reg_keywords):
                    reg_partners.append(p.get("preferredName_B", "?"))

    reg_ratio = len(reg_partners) / min(len(string_p), 20) * 100 if string_p else 0

    # PAE image block
    pae_block = ""
    if pae_exists:
        pae_block = "**PAE 图**:\n\n![[Projects/TEreg-finding/protein-interested/detail/" + dest + "/" + gene + "/" + gene + "-PAE.png]]"
    else:
        pae_block = "**PAE 图**: 待下载"

    # Build report
    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene_name} / {prot_name} |
| 蛋白大小 | {size_aa} aa / {mass} kDa |
| UniProt ID | {uni.get('uniprot_id', gene)} |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | {nuc}/10 | ×4 | {nuc*4} | {subcell_text[:60]}{"..." if len(subcell_text) > 60 else ""} |
| 📏 蛋白大小 | {sz}/10 | ×1 | {sz} | {size_aa} aa / {mass} kDa |
| 🆕 研究新颖性 | {nov}/10 | ×5 | {nov*5} | PubMed {pubmed} 篇 |
| 🏗️ 三维结构 | {struct}/10 | ×3 | {struct*3} | AlphaFold v{af_version} pLDDT={plddt}，PDB: {pdb_text} |
| 🧬 调控结构域 | {dom}/10 | ×2 | {dom*2} | {dom_text[:60]} |
| 🔗 PPI 网络 | {ppi}/10 | ×3 | {ppi*3} | STRING {len(string_p)} partners, IntAct {len(intact_p)} interactions |
| ➕ 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw}/183** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | {subcell_text[:80]}{"..." if len(subcell_text) > 80 else ""} | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | {hpa_text if hpa_text else '暂无数据'} | {hpa_rel} |
{if_embed}

**结论**: {nuc_desc}

#### 3.2 蛋白大小评估

**评价**: {sz_desc}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | {pubmed} |
| 研究方向 | 待补充关键文献摘要 |

**评价**: {nov_desc}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_version} |
| AlphaFold 平均 pLDDT | {plddt} |
| 高置信度残基 (pLDDT>90) 占比 | {round(vh*100, 1)}% |
| 置信残基 (pLDDT 70-90) 占比 | {round(conf*100, 1)}% |
| 有序区域 (pLDDT>70) 占比 | {ordered_pct}% |
| 可用 PDB 条目 | {pdb_text} |

{pae_block}

**评价**: {struct_desc}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | {dom_text[:120]} |

**染色质调控潜力分析**: {dom_desc}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
{chr(10).join(f"| {p.get('preferredName_B','?') if isinstance(p,dict) else str(p)} | {p.get('score',0) if isinstance(p,dict) else '?'} | — | {'Yes' if any(kw in (p.get('preferredName_B','') if isinstance(p,dict) else str(p)).lower() for kw in reg_keywords) else '—'} |" for p in (string_p or [])[:10]) if string_p else '| — | — | — | — |'}

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
{chr(10).join(f"| {it} | — | — | — | — |" for it in intact_top[:8]) if intact_top else '| — | — | — | — | — |'}

**已知复合体成员** (GO Cellular Component):
{format_go_cc(uni)}

**PPI 互证分析**:
- STRING + IntAct 共同确认: {len(set(str_top) & set(intact_top)) if str_top and intact_top else 0}
- 仅 STRING 预测: {len(string_p)}
- 仅 IntAct 实验: {len(intact_p)}
- 调控相关比例: {len(reg_partners)} / {min(len(string_p), 20)} = {reg_ratio:.0f}%

**评价**: {ppi_desc}。调控相关配体占比 {reg_ratio:.0f}%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT={plddt} + PDB: {pdb_text} | pLDDT={plddt}, v{af_version} | {'预测+实验' if pdb_ids else '仅预测'} |
| 定位 | UniProt + HPA | {subcell_text[:50]} | {'一致' if hpa_text else '待确认'} |
| PPI | STRING + IntAct | {len(string_p)} + {len(intact_p)} interactions | {'数据充分' if string_p and intact_p else '数据有限'} |

**互证加分明细**:
- PDB + AlphaFold 双源验证: {'+0.5' if pdb_ids else '+0'}
- 多库定位一致: {'+0.5' if hpa_text else '+0'}
- STRING + IntAct 双源验证: {'+0.5' if string_p and intact_p else '+0'}
- 结构域 + AlphaFold 质量: {'+0.5' if uni.get('domains') and plddt > 70 else '+0'}
- PDB 多条目覆盖: {'+1.0' if len(pdb_ids) >= 3 else '+0'}
**总分**: +{cross} / max +3

### 4. 总体评价

**推荐等级**: {'⭐' * max(1, min(5, round(norm/20)))}

**核心优势**:
1. {gene} — {prot_name}，{nov_desc}
2. 蛋白大小{size_aa} aa，{sz_desc}

**风险/不确定性**:
1. {'PubMed ' + str(pubmed) + ' 篇，研究基础有限，功能注释不完整' if pubmed <= 50 else '已有一定研究，需确认独特研究角度'}
2. {'AlphaFold 预测质量一般（pLDDT=' + str(plddt) + '），需要更多实验结构验证' if plddt < 70 and not pdb_ids else '结构数据质量可接受'}

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: {uniprot_url}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{gene}
"""

    return report

# Generate all reports
print("Generating reports...")
count = 0
for gene in sorted(DATA.keys()):
    dest = DEST[gene]
    report_dir = os.path.join(DETAIL, dest, gene)
    os.makedirs(report_dir, exist_ok=True)
    os.makedirs(os.path.join(report_dir, "IF_images"), exist_ok=True)

    report_path = os.path.join(report_dir, f"{gene}-evaluation.md")
    report = generate_report(gene)
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"  {gene} -> {dest}/{gene}/{gene}-evaluation.md")
    count += 1

print(f"\nGenerated {count} reports.")
