---
type: protein-evaluation
gene: "FAM184A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM184A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM184A / C6orf60 |
| 蛋白名称 | Protein FAM184A |
| 蛋白大小 | 1140 aa / 133.0 kDa |
| UniProt ID | Q8NB25 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centriolar satellite, Basal body, Cytosol; 额外: Vesicles; UniProt: Cytoplasm, P-body; Cytoplasm, cytoskeleton, microtubule orga |
| 蛋白大小 | 8/10 | ×1 | 8 | 1140 aa / 133.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039478; Pfam: PF15665 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite, Basal body, Cytosol; 额外: Vesicles | Supported |
| UniProt | Cytoplasm, P-body; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar sa... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- P-body (GO:0000932)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf60 |

**关键文献**:
1. Identification of Potential Crucial Genes Associated With the Pathogenesis and Prognosis of Endometrial Cancer.. *Frontiers in genetics*. PMID: 31105744
2. A Ten-N(6)-Methyladenosine (m(6)A)-Modified Gene Signature Based on a Risk Score System Predicts Patient Prognosis in Rectum Adenocarcinoma.. *Frontiers in oncology*. PMID: 33680913
3. Identification of potential biomarkers for osteoporosis and chronic kidney disease through bioinformatics and machine learning algorithm.. *PloS one*. PMID: 42081554
4. Comprehensive transcriptomics and proteome analysis to identify prognostic risk factors for MYCN non-amplified high-risk neuroblastoma.. *Human genomics*. PMID: 42050733
5. Novel biomarkers of preterm brain injury from blood transcriptome in sheep model of intrauterine asphyxia.. *Pediatric research*. PMID: 38822135

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 75.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 76.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039478; Pfam: PF15665 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC27 | 0.709 | 0.700 | — |
| LRRC61 | 0.613 | 0.613 | — |
| SHISAL1 | 0.543 | 0.000 | — |
| PCM1 | 0.469 | 0.461 | — |
| PLEKHO2 | 0.469 | 0.469 | — |
| OR5H1 | 0.432 | 0.000 | — |
| ZNF155 | 0.403 | 0.000 | — |
| PRR20B | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SMARCA2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KTN1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PPP1R13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 1 / 8 = 12%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, P-body; Cytoplasm, cytoskeleton, microt / Centriolar satellite, Basal body, Cytosol; 额外: Ves | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM184A — Protein FAM184A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1140 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NB25
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111879-FAM184A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM184A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NB25
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NB25-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
