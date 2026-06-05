---
type: protein-evaluation
gene: "TALDO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TALDO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TALDO1 / TAL, TALDO, TALDOR |
| 蛋白名称 | Transaldolase |
| 蛋白大小 | 337 aa / 37.5 kDa |
| UniProt ID | P37837 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 337 aa / 37.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.6; PDB: 1F05 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013785, IPR001585, IPR004730, IPR018225; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TAL, TALDO, TALDOR |

**关键文献**:
1. Proteomic Profiling of Serum Extracellular Vesicles Identifies Diagnostic Signatures and Therapeutic Targets in Breast Cancer.. *Cancer research*. PMID: 38900939
2. Chemo-proteomics reveals dihydrocaffeic acid exhibits anti-inflammation effects via Transaldolase 1 mediated PERK-NF-κB pathway.. *Cell communication and signaling : CCS*. PMID: 39910568
3. Deacetylation of TALDO1 by HDAC6 promotes glycolysis and nasopharyngeal carcinoma progression through a moonlighting function.. *Cell death & disease*. PMID: 41120289
4. Prognostic and Immune Infiltration Analysis of Transaldolase 1 (TALDO1) in Hepatocellular Carcinoma.. *International journal of general medicine*. PMID: 38089714
5. Plasma proteomic signature for preoperative prediction of microvascular invasion in HCC.. *JHEP reports : innovation in hepatology*. PMID: 40823177

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 95.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 2.7% |
| 有序区域 (pLDDT>70) 占比 | 95.6% |
| 可用 PDB 条目 | 1F05 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.6，有序区 95.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013785, IPR001585, IPR004730, IPR018225; Pfam: PF00923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TKTL1 | 0.999 | 0.125 | — |
| TKTL2 | 0.999 | 0.289 | — |
| TKT | 0.999 | 0.416 | — |
| RPIA | 0.998 | 0.091 | — |
| GPI | 0.995 | 0.000 | — |
| TPI1 | 0.994 | 0.135 | — |
| FBP1 | 0.992 | 0.000 | — |
| FBP2 | 0.989 | 0.000 | — |
| PFKM | 0.988 | 0.000 | — |
| GAPDH | 0.986 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHD3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| ZHX1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 1F05 | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TALDO1 — Transaldolase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小337 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P37837
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177156-TALDO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TALDO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P37837
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000177156-TALDO1/subcellular

![](https://images.proteinatlas.org/40373/1874_E5_44_cr5b7163c43ea91_blue_red_green.jpg)
![](https://images.proteinatlas.org/40373/1874_E5_49_cr5b7163c43ee1a_blue_red_green.jpg)
![](https://images.proteinatlas.org/40373/1933_B9_26_cr5d11cc279e189_blue_red_green.jpg)
![](https://images.proteinatlas.org/40373/1933_B9_4_cr5d11cc279ba2c_blue_red_green.jpg)
![](https://images.proteinatlas.org/40373/2103_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40373/2103_B7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P37837-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
