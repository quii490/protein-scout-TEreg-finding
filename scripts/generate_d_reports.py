#!/usr/bin/env python3
"""Generate evaluation reports for all D proteins based on batch_query results."""
import json, os, sys, re, urllib.request, time, glob

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

def ufetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except:
        return None

def download_file(url, path):
    """Download a file to path."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(path, 'wb') as f:
                f.write(resp.read())
            return True
    except Exception as e:
        print(f"  Download failed: {e}")
        return False

def score_nuclear(locs, func_text=""):
    """Score nuclear localization."""
    if not locs:
        return 0, "无定位信息"
    loc_str = ";".join(locs).lower()

    # Check for primary nucleus
    has_nucleus = any("nucleus" in l.lower() for l in locs)
    has_cytoplasm = any("cytoplasm" in l.lower() for l in locs)
    has_membrane = any("membrane" in l.lower() for l in locs)
    has_cytoskeleton = any("cytoskeleton" in l.lower() for l in locs)
    has_secreted = any("secret" in l.lower() for l in locs)
    has_mito = any("mitochond" in l.lower() for l in locs)
    has_er = any("endoplasmic" in l.lower() for l in locs)
    has_golgi = any("golgi" in l.lower() for l in locs)
    has_pm = any("cell membrane" in l.lower() or "plasma membrane" in l.lower() for l in locs)
    has_centrosome = any("centrosome" in l.lower() for l in locs)
    has_nucleolus = any("nucleolus" in l.lower() for l in locs)

    # Homeobox/DNA binding/transcription factor = nuclear
    is_tf = any(kw in func_text.lower() for kw in ["transcription factor", "homeobox", "dna-binding",
                                                     "dna binding", "transcriptional repressor",
                                                     "transcriptional activator", "chromatin"])

    # Primary non-nuclear locations that disqualify
    primary_non_nuclear = has_cytoskeleton or has_secreted or has_er or has_mito

    if has_nucleus and not has_cytoplasm:
        if is_tf:
            return 9, "UniProt Nucleus + 转录因子/同源盒/DNA结合蛋白"
        return 7, "UniProt Nucleus (单一核定位)"
    elif has_nucleus and has_cytoplasm:
        if is_tf:
            return 7, "UniProt Nucleus+Cytoplasm, 转录因子功能提示核为主"
        return 4, "UniProt Nucleus+Cytoplasm (核质双分布)"
    elif has_nucleus and (has_membrane or has_cytoskeleton):
        return 4, "UniProt Nucleus+其他区室, 非特异核定位"
    elif not has_nucleus and has_cytoplasm:
        # Check if there's any nuclear functional hint
        if is_tf:
            return 3, "UniProt Cytoplasm only, 但功能提示核相关"
        return 0, "UniProt Cytoplasm only"
    elif primary_non_nuclear:
        return 0, "Primary non-nuclear"
    elif not locs:
        return 0, "无定位注释"

    return 0, "Cannot determine"

def score_size(length):
    """Score protein size."""
    if 200 <= length <= 800:
        return 10, f"{length} aa (200-800 aa, 适宜)"
    elif 100 <= length < 200 or 800 < length <= 1200:
        return 8, f"{length} aa (100-200/800-1200 aa)"
    elif 50 <= length < 100 or 1200 < length <= 2000:
        return 5, f"{length} aa (50-100/1200-2000 aa)"
    elif length < 50:
        return 2, f"{length} aa (<50 aa)"
    elif 2000 < length <= 3000:
        return 2, f"{length} aa (2000-3000 aa)"
    else:
        return 0, f"{length} aa (>3000 aa)"

def score_domain(uniprot_data, func_text, pubmed_novel):
    """Score domain/chromatin potential."""
    domains = uniprot_data.get("domains", [])
    func = (func_text or "").lower()
    gene = uniprot_data.get("raw_name", "").lower()

    # Check for known chromatin/DNA domains
    chromatin_kw = ["homeobox", "homeodomain", "zinc finger", "c2h2", "at-hook", "hmg",
                    "bromodomain", "chromodomain", "phd finger", "sant", "whd", "tudor",
                    "mbt", "pwwp", "swi/snf", "iswi", "cxxc", "t-box", "mads-box",
                    "myb", "forkhead", "bzip", "bhlh", "dm domain", "dachshund",
                    "set domain", "jumanji", "jmjc", "macro domain", "double homeobox",
                    "dmrt", "dach", "dbx", "drgx"]

    dom_text = ";".join(domains).lower() + " " + func + " " + gene
    has_chromatin_dom = any(kw in dom_text for kw in chromatin_kw)

    # Special TF families
    is_homeobox = "homeobox" in dom_text
    is_dmrt = "doublesex" in dom_text or "mab-3" in dom_text
    is_dach = "dachshund" in dom_text
    is_double_homeobox = "double homeobox" in dom_text

    if is_homeobox or is_double_homeobox:
        return 10, f"明确的DNA结合同源盒结构域 ({'double homeobox' if is_double_homeobox else 'homeobox'})"
    elif is_dmrt:
        return 10, "明确的DM DNA结合结构域 (DMRT家族)"
    elif is_dach:
        return 9, "Dachshund结构域 (转录共抑制因子)"
    elif has_chromatin_dom:
        return 8, f"DNA/chromatin相关结构域: {[d for d in domains if any(k in d.lower() for k in chromatin_kw)][:3]}"
    elif pubmed_novel <= 50:
        # Novel proteins get baseline 7
        return 7, "新颖蛋白基线 (无注释结构域属正常)"
    elif pubmed_novel <= 100:
        return 7, "PubMed≤100基线 (无注释结构域)"
    else:
        return 5, "已研究蛋白无注释结构域"

def score_structure(alphafold_data, pdb_list, pubmed_novel):
    """Score 3D structure."""
    pdbs = pdb_list or []
    af = alphafold_data or {}
    plddt_m = af.get("plddt_mean")
    plddt70 = af.get("plddt_gt70")

    has_af = plddt_m is not None
    has_pdb = len([p for p in pdbs if p]) > 0

    if has_pdb and has_af and plddt_m and plddt_m > 70:
        return 10, f"PDB实验结构 ({len(pdbs)}条目) + AlphaFold高质量 (pLDDT={plddt_m})"
    elif has_pdb:
        return 9, f"PDB实验结构 ({len(pdbs)}条目)"
    elif has_af and plddt_m and plddt_m > 80:
        return 8, f"AlphaFold高质量 (pLDDT={plddt_m}, >70%={plddt70}%)"
    elif has_af and plddt_m and plddt_m > 65:
        return 7, f"AlphaFold中等 (pLDDT={plddt_m})"
    elif pubmed_novel <= 100:
        # Novel proteins get baseline 6
        return 6, f"新颖蛋白基线 (无PDB/AlphaFold预测差属正常)"
    else:
        return 5, "无可靠结构"

def score_ppi(intact_data, string_data, uniprot_data):
    """Score PPI network."""
    intact = intact_data or []
    string = string_data or []

    # Count physical interactions (co-IP, pull-down, two-hybrid)
    physical_methods = ["coimmunoprecipitation", "pull down", "two hybrid", "cross-linking",
                        "anti tag coimmunoprecipitation", "anti bait coimmunoprecipitation"]
    physical_intact = [i for i in intact if any(m in i.get("method", "").lower() for m in physical_methods)]

    # High-confidence STRING
    hi_string = [s for s in string if s.get("score", 0) > 0.7]
    hi_exp_string = [s for s in string if s.get("exp", 0) > 0.5]

    # Check for chromatin/transcription regulator partners
    chromatin_kw = ["transcription", "chromatin", "histone", "methyltransferase",
                    "acetyltransferase", "deacetylase", "hdac", "swi/snf", "nurd",
                    "polycomb", "trithorax", "mll", "setd", "kmt", "kdm", "dnmt",
                    "baf", "pba", "ino80", "iswi", "chd", "smarca", "arid",
                    "bromodomain", "chromodomain", "homeobox", "dna binding"]

    all_partners = set()
    regulatory_partners = set()
    for i in physical_intact:
        partner = i.get("a", "") + i.get("b", "")
        all_partners.add(partner)
        if any(kw in partner.lower() for kw in chromatin_kw):
            regulatory_partners.add(partner)

    for s in hi_string:
        partner = s.get("partner", "")
        all_partners.add(partner)
        if any(kw in partner.lower() for kw in chromatin_kw):
            regulatory_partners.add(partner)

    if physical_intact and len(regulatory_partners) > 0:
        reg_ratio = len(regulatory_partners) / max(len(all_partners), 1) * 100
        if reg_ratio > 40:
            return 10, f"物理互作证据 + 邻居>40%调控因子 ({len(physical_intact)}物理互作, {reg_ratio:.0f}%调控)"
        elif reg_ratio > 20:
            return 8, f"物理互作证据 + 邻居20-40%调控因子 ({len(physical_intact)}物理互作, {reg_ratio:.0f}%调控)"
        else:
            return 6, f"有物理互作 ({len(physical_intact)}条), 调控邻居占比低"
    elif hi_exp_string:
        return 6, f"STRING实验分>0.5 ({len(hi_exp_string)}条), 无IntAct物理互作"
    elif hi_string:
        return 4, f"STRING综合分>0.7 ({len(hi_string)}条), 主要为预测"
    elif string:
        return 3, f"仅有低置信度STRING关联 ({len(string)}条)"
    else:
        return 1, "PPI数据极少"

def determine_subloc(nuc_score, locs, func_text):
    """Determine subnuclear localization category."""
    if nuc_score <= 3:
        return "rejected"

    loc_str = ";".join(locs).lower()
    func_lower = (func_text or "").lower()

    if "nucleolus" in loc_str or "nucleolar" in loc_str:
        return "nucleolus"
    elif "speckle" in loc_str or "nuclear speckle" in loc_str:
        return "nuclear-speckle"
    elif "nuclear body" in loc_str or "pml body" in loc_str or "cajal" in loc_str:
        return "nuclear-body"
    elif "nuclear matrix" in loc_str:
        return "nuclear-matrix"
    elif "chromatin" in loc_str or "chromosome" in loc_str or "centromere" in loc_str or "kinetochore" in loc_str:
        return "chromatin"
    elif "nuclear envelope" in loc_str or "nuclear membrane" in loc_str or "lamina" in loc_str:
        return "nuclear-envelope"
    elif "nucleus" in loc_str and "cytoplasm" in loc_str:
        return "nucleus-cytoplasm"
    elif "nucleus" in loc_str:
        return "nucleoplasm"
    else:
        return "nucleoplasm"

def generate_report(gene, data):
    """Generate evaluation markdown."""
    u = data.get("uniprot", {})
    pubmed = data["pubmed_count"]
    nov_score = data["novelty_score"]
    nov_label = data["novelty_label"]
    intact = data.get("intact", [])
    string = data.get("string", [])
    af = data.get("alphafold", {})

    locs = u.get("locs", [])
    func_text = " ".join(u.get("funcs", [""]))
    length = u.get("len", 0)
    name = u.get("name", gene)
    acc = u.get("acc", "?")
    genes = u.get("genes", [gene])
    aliases = " | ".join(genes)
    pdbs = u.get("pdbs", [])
    domains = u.get("domains", [])
    gocc = u.get("gocc", [])

    # Scoring
    nuc_score, nuc_evidence = score_nuclear(locs, func_text)
    size_score, size_evidence = score_size(length)
    dom_score, dom_evidence = score_domain(u, func_text, pubmed)
    struct_score, struct_evidence = score_structure(af, pdbs, pubmed)
    ppi_score, ppi_evidence = score_ppi(intact, string, u)

    # Cross-validation bonus
    cross_score = 0
    cross_details = []

    # Check if UniProt nuclear + homeobox/TF = cross-validation
    has_nucleus = any("nucleus" in l.lower() for l in locs)
    is_tf = any(kw in func_text.lower() for kw in ["transcription factor", "homeobox",
                                                     "transcriptional repressor",
                                                     "transcriptional activator"])
    if has_nucleus and is_tf:
        cross_score += 1.0
        cross_details.append("核定位+转录因子功能一致 (+1.0)")

    if pdbs and len([p for p in pdbs if p]) > 0:
        cross_score += 1.0
        cross_details.append(f"PDB实验结构确认 ({len(pdbs)}条目) (+1.0)")

    if intact and len(intact) > 5:
        cross_score += 0.5
        cross_details.append(f"IntAct实验互作数据丰富 ({len(intact)}条) (+0.5)")

    if string and any(s.get("exp", 0) > 0.7 for s in string):
        cross_score += 0.5
        cross_details.append("STRING实验分>0.7互作确认 (+0.5)")

    raw = (nuc_score * 4) + (size_score * 1) + (nov_score * 5) + (struct_score * 3) + (dom_score * 2) + (ppi_score * 3) + cross_score
    norm = round(raw / 1.83, 1)

    # Determine subloc
    subloc = determine_subloc(nuc_score, locs, func_text)

    # Check for rejection
    if nuc_score <= 3:
        subloc = "rejected"
        status = "rejected"
    elif pubmed > 100:
        subloc = "rejected"
        status = "rejected"
    else:
        status = "scored"

    out_dir = os.path.join(DETAIL, subloc, gene)
    os.makedirs(out_dir, exist_ok=True)

    # PAE image path
    pae_path = f"Projects/TEreg-finding/protein-interested/detail/{subloc}/{gene}/{gene}-PAE.png"
    if not os.path.exists(os.path.join(out_dir, f"{gene}-PAE.png")):
        pae_embed = "暂无PAE图"
    else:
        pae_embed = f"![[{pae_path}]]"

    # IF images - check if any exist
    if_dir = os.path.join(out_dir, "IF_images")
    if_jpgs = glob.glob(os.path.join(if_dir, "*.jpg")) if os.path.exists(if_dir) else []
    if_embed = ""
    if if_jpgs:
        for jpg in sorted(if_jpgs)[:2]:
            fname = os.path.basename(jpg)
            cell_line = fname.replace(".jpg", "").replace("_red_green", "").replace("_", " ")
            if_embed += f"![[Projects/TEreg-finding/protein-interested/detail/{subloc}/{gene}/IF_images/{fname}|{cell_line}]]\n"

    cross_str = f"+{cross_score}" if cross_score > 0 else "0"
    if isinstance(cross_score, float) and cross_score == int(cross_score):
        cross_str = f"+{int(cross_score)}"

    if status == "rejected":
        reason = f"核定位 ≤3 ({nuc_score}/10)" if nuc_score <= 3 else f"PubMed >100 ({pubmed}篇)"
        if nuc_score <= 3:
            reason_extra = nuc_evidence
        else:
            reason_extra = f"PubMed={pubmed}>100"

        report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-05-29
tags: [protein-scout, rejected]
status: rejected
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白大小 | {length} aa |
| UniProt ID | {acc} |
| 评估日期 | 2026-05-29 |

### 2. 淘汰原因

**{reason}**

{reason_extra}

PubMed 总数: {pubmed} 篇

### 3. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
"""
        with open(os.path.join(out_dir, f"{gene}-evaluation.md"), 'w') as f:
            f.write(report)
        return subloc, gene, nuc_score, size_score, nov_score, struct_score, dom_score, ppi_score, cross_score, norm

    # Domain detail
    dom_detail = "- " + "\n- ".join(domains[:8]) if domains else "- 无注释结构域"

    # PPI detail - IntAct table
    physical_methods = ["coimmunoprecipitation", "pull down", "two hybrid"]
    phys_intact = [i for i in intact if any(m in i.get("method", "").lower() for m in physical_methods)][:5]

    intact_rows = ""
    for i in phys_intact:
        partner_a = i.get("a", "").replace("uniprotkb:", "")
        partner_b = i.get("b", "").replace("uniprotkb:", "")
        partner = partner_a if gene.upper() not in partner_a.upper() else partner_b
        method = i.get("method", "").replace('psi-mi:', '').replace('"MI:', '').replace('"', '')
        intact_rows += f"| {partner[:20]} | {method[:40]} | {i.get('pmid', '-')[:20]} | - | - |\n"

    if not intact_rows:
        intact_rows = "| 无实验验证的物理互作 | - | - | - | - |\n"

    # STRING rows
    hi_string = [s for s in string if s.get("score", 0) > 0.5][:8]
    string_rows = ""
    for s in hi_string:
        string_rows += f"| {s.get('partner', '')} | {s.get('score', 0)} | - | - |\n"
    if not string_rows:
        string_rows = "| 无高置信度STRING互作 | - | - | - |\n"

    # GO-CC
    gocc_text = "\n".join(f"- {g}" for g in gocc[:8]) if gocc else "- 无复合体注释"

    # pLDDT analysis
    plddt_m = af.get("plddt_mean", "N/A")
    plddt70 = af.get("plddt_gt70", "N/A")
    plddt90 = af.get("plddt_gt90", "N/A")

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白大小 | {length} aa |
| UniProt ID | {acc} |
| 蛋白名称 | {name} |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | {nuc_score}/10 | ×4 | {nuc_score*4} | {nuc_evidence[:80]} |
| 📏 蛋白大小 | {size_score}/10 | ×1 | {size_score} | {size_evidence[:80]} |
| 🆕 研究新颖性 | {nov_score}/10 | ×5 | {nov_score*5} | PubMed={pubmed}篇 ({nov_label}) |
| 🏗️ 三维结构 | {struct_score}/10 | ×3 | {struct_score*3} | {struct_evidence[:80]} |
| 🧬 调控结构域 | {dom_score}/10 | ×2 | {dom_score*2} | {dom_evidence[:80]} |
| 🔗 PPI 网络 | {ppi_score}/10 | ×3 | {ppi_score*3} | {ppi_evidence[:80]} |
| ➕ 互证加分 | — | max +3 | {cross_str} | {'; '.join(cross_details) if cross_details else '无'} |
| **原始总分** | | | **{raw} / 183** | |
| **归一化总分** | | | **{norm} / 100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | {"; ".join(locs[:5]) if locs else "无注释"} | Swiss-Prot/TrEMBL |

**结论**: {nuc_evidence}

#### 3.2 蛋白大小评估

**评价**: {size_evidence}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | {pubmed} |
| 新颖性分级 | {nov_label} |

**评价**: PubMed {pubmed} 篇，{nov_label}。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | {plddt_m} |
| 有序区域 (pLDDT>70) 占比 | {plddt70}% |
| 高置信度 (pLDDT>90) 占比 | {plddt90}% |
| 可用 PDB 条目 | {"; ".join(pdbs) if pdbs else "无"} |

{pae_embed}

**评价**: {struct_evidence}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | {'; '.join(domains[:5]) if domains else '无注释'} |

**染色质调控潜力分析**: {dom_evidence}

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
{intact_rows}
**STRING 预测互作** (combined score >0.5):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
{string_rows}
**已知复合体成员** (GO Cellular Component):
{gocc_text}

**PPI 互证分析**:
{ppi_evidence}

**评价**: {ppi_evidence}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt | {'Nucleus' if has_nucleus else 'Non-nuclear'} | {'是' if has_nucleus else '否'} |
| 结构域 | UniProt | {len(domains)}个注释域 | {'一致' if domains else 'N/A'} |
| PPI | STRING+IntAct | IntAct:{len(intact)}, STRING:{len(string)} | 一致 |

**互证加分明细**:
{chr(10).join(f'- {d}' for d in cross_details) if cross_details else '- 无额外互证加分'}
**总分**: {cross_str} / max +3

### 4. 总体评价

**推荐等级**: {'⭐' * min(5, max(1, int(norm/20 + 1)))} ({norm}/100)

**核心优势**:
1. {nov_label} (PubMed={pubmed})
2. {nuc_evidence[:80]}

**风险/不确定性**:
1. 无Protein Atlas IF验证
2. 无AlphaFold结构或结构质量待验证

**下一步建议**:
- [ ] Protein Atlas IF实验验证核定位
- [ ] AlphaFold结构预测验证

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
"""

    with open(os.path.join(out_dir, f"{gene}-evaluation.md"), 'w') as f:
        f.write(report)

    return subloc, gene, nuc_score, size_score, nov_score, struct_score, dom_score, ppi_score, cross_score, norm


def main():
    with open(os.path.join(BASE, "batch_results.json")) as f:
        content = f.read()
    idx = content.find('{')
    if idx > 0:
        content = content[idx:]
    data = json.loads(content)

    results = []
    for gene in sorted(data.keys()):
        print(f"Generating report for {gene}...", file=sys.stderr)
        try:
            r = generate_report(gene, data[gene])
            results.append(r)
        except Exception as e:
            print(f"  ERROR generating {gene}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()

    # Summary
    print("\n=== Summary ===", file=sys.stderr)
    scored = [r for r in results if r[0] != "rejected"]
    rejected = [r for r in results if r[0] == "rejected"]

    print(f"\nScored: {len(scored)} proteins", file=sys.stderr)
    for cat, gene, nuc, sz, nov, struct, dom, ppi, cross, norm in sorted(scored, key=lambda x: -x[9]):
        print(f"  [{cat}] {gene}: norm={norm} (nuc={nuc}, nov={nov}, struct={struct}, dom={dom}, ppi={ppi}, cross={cross})", file=sys.stderr)

    print(f"\nRejected: {len(rejected)} proteins", file=sys.stderr)
    for cat, gene, nuc, sz, nov, struct, dom, ppi, cross, norm in rejected:
        print(f"  {gene}: nuc={nuc}, pubmed={data[gene]['pubmed_count']}", file=sys.stderr)

if __name__ == "__main__":
    main()
