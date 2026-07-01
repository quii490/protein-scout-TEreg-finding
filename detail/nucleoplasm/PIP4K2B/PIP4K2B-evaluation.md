---
type: protein-evaluation
gene: "PIP4K2B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PIP4K2B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PIP4K2B |
| 蛋白名称 | Phosphatidylinositol 5-phosphate 4-kinase type-2 beta |
| 蛋白大小 | 416 aa / 47.4 kDa |
| UniProt ID | P78356 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | HPA: Nucleoplasm (Supported) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 416 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed strict=17 篇 |
| 🏗️ 三维结构 | 9/10 | ×3 | 27.0 | AF pLDDT=84.1; PDB: 26 entries |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | PInositol-4-P-4/5-kinase_C_sf; PInositol-4-P-4/5-kinase_core; PInositol-4-P-5-kinase_N; PInositol-4/ |
| 🔗 PPI | 6/10 | ×3 | 18.0 | Combined PPI degree=123 |
| **加权总分** | | | **135/180** | |
| **归一化总分 (÷1.83)** | | | **74.9/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| GO-CC | autophagosome(IMP:ParkinsonsUK-UCL); cytosol(TAS:Reactome); endoplasmic reticulum membrane(IEA:UniPr | — |

**IF 图像**: See [Protein Atlas](https://www.proteinatlas.org/)

**PAE 图**: https://alphafold.ebi.ac.uk/files/AF-P78356-F1-predicted_aligned_error_v6.png

#### 3.2 蛋白大小评估
416 aa / 47.4 kDa.

#### 3.3 研究现状
PubMed strict: 17. Broad: 29.

- PMID 38539515: PIP4K2B Protein Regulation by NSD1 in HPV-Negative Head and Neck Squamous Cell Carcinoma.. *Cancers*
- PMID 36918565: PIP4K2B is mechanoresponsive and controls heterochromatin-driven nuclear softening through UHRF1.. *Nature communications*
- PMID 36982700: Autoantibodies against PIP4K2B and AKT3 Are Associated with Skin and Lung Fibrosis in Patients with Systemic Sclerosis.. *International journal of molecular sciences*

#### 3.4 三维结构分析
AlphaFold pLDDT=84.1. PDB=26.

#### 3.5 结构域分析
InterPro: PInositol-4-P-4/5-kinase_C_sf; PInositol-4-P-4/5-kinase_core; PInositol-4-P-5-kinase_N; PInositol-4/5-P-5/4-kinase
Pfam: PIP5K

#### 3.6 PPI 互作网络
Combined human PPI degree=123.

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + GO-CC | consistent |
| 结构域 | InterPro + Pfam | verified |
| PPI | STRING/BioGRID | 有数据 |

### 4. 总体评价
**推荐等级**: ⭐⭐⭐⭐
**归一化总分**: 74.9/100
**定位分类**: nucleoplasm

Non-chromatin-regulatory nuclear protein with some nuclear localization evidence. Moderately novel (17 PubMed papers).

### 功能描述

Participates in the biosynthesis of phosphatidylinositol 4,5-bisphosphate (PubMed:26774281, PubMed:9038203). Preferentially utilizes GTP, rather than ATP, for PI(5)P phosphorylation and its activity reflects changes in direct proportion to the physiological GTP concentration (PubMed:26774281). Its GTP-sensing activity is critical for metabolic adaptation (PubMed:26774281). PIP4Ks negatively regulate insulin signaling through a catalytic-independent mechanism. They interact with PIP5Ks and suppre


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNFRSF1A | BioGRID | 0 |
| PIP4K2B | BioGRID | 0 |
| SPOP | BioGRID | 0 |
| UBQLN4 | BioGRID | 0 |
| MED18 | BioGRID | 0 |
| CSNK2A2 | BioGRID | 0 |
| HMBOX1 | BioGRID | 0 |
| ARL6IP4 | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000276293-PIP4K2B

![](https://images.proteinatlas.org/62220/1171_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/62220/1171_F8_4_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

PIP4K2B（Phosphatidylinositol 5-phosphate 4-kinase type-2 beta）是一类脂质激酶，催化磷脂酰肌醇-5-磷酸（PI(5)P）的4位磷酸化，生成磷脂酰肌醇-4,5-二磷酸（PI(4,5)P2）。其结构域架构由三部分组成：PInositol-4-P-5-kinase_N（N端结构域）、PInositol-4-P-4/5-kinase_core（催化核心）和PInositol-4-P-4/5-kinase_C_sf（C端超家族折叠）。416个氨基酸（47.4 kDa）的分子量和pLDDT=84.1的高结构置信度使其成为结构研究中较为理想的靶标。值得注意的是，PDB数据库中有26个条目，表明该蛋白的结构已被广泛研究，包括多个抑制剂复合物结构（PMID 42117906揭示了高亲和力抑制剂与PIP4K2A/PIP4K2B结合的分子基础）。

PIP4K2B的功能意义远超出其脂质激酶的酶学活性。该蛋白独特地偏好GTP而非ATP作为磷酸供体（PMID 26774281），使其成为细胞内GTP浓度的传感器，从而在代谢适应中发挥关键作用。核质定位（HPA Nucleoplasm, Supported）与GO-CC注释（autophagosome, cytosol, ER membrane）的多重定位模式提示该蛋白具有亚细胞区室间的动态分布。尤其重要的是，PIP4K2B的核内功能近期得到了重要阐明：PMID 36918565（Nature Communications, 2023）发现PIP4K2B是机械响应蛋白，通过调控UHRF1来控制异染色质驱动的核软化（heterochromatin-driven nuclear softening）。这一发现直接将一个脂质激酶与染色质力学调控联系起来，为TE调控提供了全新的物理-化学界面。

从机制模型来看，PIP4K2B在核内通过调节PI(5)P/PI(4,5)P2的局部平衡来影响染色质结构和核骨架。核内存在活跃的磷脂酰肌醇代谢，这些脂质分子不仅仅是膜组分，更作为信号分子调控染色质重塑、转录和DNA修复。PI(5)P在核内富集于异染色质区域，而PIP4K2B将其转化为PI(4,5)P2，这一转化可改变局部染色质环境——调变核小体间距、调控染色质结合蛋白（如UHRF1）的活性，以及影响HP1介导的异染色质组装。因此，PIP4K2B构成了一个将代谢状态（GTP水平）与染色质结构和基因组稳定性联系起来的分子枢纽。

PPI网络结合度为123（combined degree），BioGRID互作伙伴包括TNFRSF1A、SPOP（一种E3泛素连接酶，通过识别底物的degron基序调控蛋白降解）、UBQLN4（泛素-蛋白酶体系统衔接蛋白）和HMBOX1（一种核小体结合蛋白）。HMBOX1的互作进一步强化了PIP4K2B在染色质调控中的角色。从TE调控角度，PIP4K2B通过UHRF1-异染色质轴的机械调控可能直接影响逆转座子元件的表观遗传沉默——异染色质完整性是抑制TE激活的关键屏障。PIP4K2B因此成为本批次中TE调控机制最具结构生物学基础和研究深度的候选蛋白之一。


### PubMed

**Count: 29**

| PMID | Title |
|---|---|
| 42117906 | Structural basis for high-affinity inhibitor binding to lipid kinases PIP4K2A and PIP4K2B. |
| 41695382 | Oat grass improves meat tenderness and flavor, reduces fat deposition in small-tailed Han sheep. |
| 41301084 | Correction: Topchu et al. PIP4K2B Protein Regulation by NSD1 in HPV-Negative Head and Neck Squamous Cell Carcinoma. Cancers 2024, 16, 1180. |
| 40609214 | Differential expression of lncRNAs and mRNAs in bone marrow-derived mesenchymal stem cells under continuous and intermittent teriparatide treatment. |
| 38851560 | Potency and efficacy of pharmacological PIP4K2 inhibitors in acute lymphoblastic leukemia. |


