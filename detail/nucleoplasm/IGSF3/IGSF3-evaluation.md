---
type: protein-evaluation
gene: "IGSF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IGSF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IGSF3 / EWI3, KIAA0466 |
| 蛋白名称 | Immunoglobulin superfamily member 3 |
| 蛋白大小 | 1194 aa / 135.2 kDa |
| UniProt ID | O75054 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1194 aa / 135.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EWI3, KIAA0466 |

**关键文献**:
1. Genes and Athletic Performance: The 2023 Update.. *Genes*. PMID: 37372415
2. Glioma epileptiform activity and progression are driven by IGSF3-mediated potassium dysregulation.. *Neuron*. PMID: 36787748
3. EWI2 and its relatives in Tetraspanin-enriched membrane domains regulate malignancy.. *Oncogene*. PMID: 36788350
4. IGSF3 mutation identified in patient with severe COPD alters cell function and motility.. *JCI insight*. PMID: 32573489
5. Preliminary report on screening IGSF3 gene mutation in families with congenital absence of lacrimal puncta and canaliculi.. *International journal of ophthalmology*. PMID: 32953570

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 33.5% |
| 置信残基 (pLDDT 70-90) 占比 | 51.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 85.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.5，有序区 85.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR003598; Pfam: PF07686 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD9 | 0.753 | 0.345 | — |
| CD81 | 0.625 | 0.113 | — |
| ERV3-1 | 0.567 | 0.061 | — |
| ERVFRD-1 | 0.567 | 0.061 | — |
| TSPAN7 | 0.562 | 0.113 | — |
| CDR2 | 0.502 | 0.502 | — |
| IGDCC4 | 0.483 | 0.054 | — |
| TSPAN15 | 0.483 | 0.345 | — |
| TSPAN14 | 0.475 | 0.345 | — |
| IGSF11 | 0.475 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H4C16 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RAN | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HDLBP | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SPPL2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAALADL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.5 + PDB: 无 | pLDDT=81.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IGSF3 — Immunoglobulin superfamily member 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1194 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75054
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143061-IGSF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IGSF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75054
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000143061-IGSF3/subcellular

![](https://images.proteinatlas.org/36306/434_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/36306/434_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/36306/450_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/36306/450_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/36306/453_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/36306/453_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75054-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75054 |
| SMART | SM00409;SM00408;SM00406; |
| UniProt Domain [FT] | DOMAIN 20..138; /note="Ig-like C2-type 1"; DOMAIN 143..262; /note="Ig-like C2-type 2"; DOMAIN 276..386; /note="Ig-like C2-type 3"; DOMAIN 401..539; /note="Ig-like C2-type 4"; DOMAIN 545..661; /note="Ig-like C2-type 5"; DOMAIN 676..803; /note="Ig-like C2-type 6"; DOMAIN 813..945; /note="Ig-like C2-type 7"; DOMAIN 949..1097; /note="Ig-like C2-type 8" |
| InterPro | IPR007110;IPR036179;IPR013783;IPR003599;IPR003598;IPR013106;IPR051102; |
| Pfam | PF07686; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143061-IGSF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXO6 | Biogrid, Bioplex | true |
| CDR2 | Bioplex | false |
| CTNNB1 | Biogrid | false |
| FBXO2 | Bioplex | false |
| IGF2R | Biogrid | false |
| KCNK1 | Bioplex | false |
| KRAS | Biogrid | false |
| LGALS1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
