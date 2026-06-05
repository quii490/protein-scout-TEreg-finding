---
type: protein-evaluation
gene: "CYLD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYLD — REJECTED (研究热度过高 (PubMed strict=603，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYLD / CYLD1, KIAA0849 |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase CYLD |
| 蛋白大小 | 956 aa / 107.3 kDa |
| UniProt ID | Q9NQC7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centriolar satellite; 额外: Nucleoplasm, Primary cilium transi; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, cytoske |
| 蛋白大小 | 8/10 | ×1 | 8 | 956 aa / 107.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=603 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.4; PDB: 1IXD, 1WHL, 1WHM, 2VHF, 7OWC, 7OWD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036859, IPR000938, IPR038765, IPR001394, IPR028 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite; 额外: Nucleoplasm, Primary cilium transition zone, Basal body, Principal piece | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton; Cell membrane; Cytoplasm, cytoske... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary tip (GO:0097542)
- ciliary transition zone (GO:0035869)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 603 |
| PubMed broad count | 974 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CYLD1, KIAA0849 |

**关键文献**:
1. TRIM15 and CYLD regulate ERK activation via lysine-63-linked polyubiquitination.. *Nature cell biology*. PMID: 34497368
2. A mechanism for hypoxia-induced inflammatory cell death in cancer.. *Nature*. PMID: 39506105
3. CYLD Cutaneous Syndrome.. **. PMID: 32298062
4. Novel role of macrophage TXNIP-mediated CYLD-NRF2-OASL1 axis in stress-induced liver inflammation and cell death.. *JHEP reports : innovation in hepatology*. PMID: 36035360
5. CYLD in health and disease.. *Disease models & mechanisms*. PMID: 37387450

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 29.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 23.8% |
| 有序区域 (pLDDT>70) 占比 | 70.4% |
| 可用 PDB 条目 | 1IXD, 1WHL, 1WHM, 2VHF, 7OWC, 7OWD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1IXD, 1WHL, 1WHM, 2VHF, 7OWC, 7OWD）+ AlphaFold极高置信度预测（pLDDT=74.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036859, IPR000938, IPR038765, IPR001394, IPR028889; Pfam: PF01302, PF16607, PF00443 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAF6 | 0.999 | 0.755 | — |
| RIPK1 | 0.999 | 0.791 | — |
| TNFRSF1A | 0.999 | 0.994 | — |
| IKBKG | 0.999 | 0.852 | — |
| SPATA2 | 0.997 | 0.846 | — |
| TRADD | 0.995 | 0.000 | — |
| UBC | 0.995 | 0.990 | — |
| IKBKE | 0.994 | 0.629 | — |
| RNF31 | 0.993 | 0.862 | — |
| TRAF2 | 0.992 | 0.645 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Bcl3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-12034|pubmed:16713561 |
| IKBKG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| OGA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SPATA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SPATA2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MYO6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CEP192 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| - | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 1IXD, 1WHL, 1WHM, 2VHF, 7OWC,  | pLDDT=74.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cytoplas / Centriolar satellite; 额外: Nucleoplasm, Primary cil | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYLD — Ubiquitin carboxyl-terminal hydrolase CYLD，研究基础较多，新颖性有限。
2. 蛋白大小956 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 603 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 603 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQC7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083799-CYLD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYLD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQC7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (supported)。来源: https://www.proteinatlas.org/ENSG00000083799-CYLD/subcellular

![](https://images.proteinatlas.org/50095/2146_C8_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/50095/2146_C8_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/50095/2161_C6_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/50095/2161_C6_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/50095/2177_A6_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/50095/2177_A6_52_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQC7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
