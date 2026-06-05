---
type: protein-evaluation
gene: "SPOUT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPOUT1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPOUT1 / C9orf114 |
| 蛋白名称 | 28S rRNA (uridine-N(3))-methyltransferase |
| 蛋白大小 | 376 aa / 42.0 kDa |
| UniProt ID | Q5T280 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, spindle; Chromosome, centromere, ki |
| 蛋白大小 | 10/10 | ×1 | 10 | 376 aa / 42.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.4; PDB: 4RG1, 8QSU, 8QSV, 8QSW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029028, IPR012340, IPR003750, IPR029026; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton, spindle; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, micr... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- kinetochore (GO:0000776)
- mitotic spindle (GO:0072686)
- spindle pole centrosome (GO:0031616)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf114 |

**关键文献**:
1. RNA methyltransferase SPOUT1/CENP-32 links mitotic spindle organization with the neurodevelopmental disorder SpADMiSS.. *Nature communications*. PMID: 39962046
2. SPOUT1 variants associated with autosomal-recessive developmental and epileptic encephalopathy.. *Acta epileptologica*. PMID: 40217412
3. Malakoplakia with aberrant ALK expression by immunohistochemistry: a case report.. *Diagnostic pathology*. PMID: 37644531
4. RNA methyltransferase SPOUT1/CENP-32 links mitotic spindle organization with the neurodevelopmental disorder SpADMiSS.. *medRxiv : the preprint server for health sciences*. PMID: 38260255
5. System Biology-Guided Chemical Proteomics to Discover Protein Targets of Monoethylhexyl Phthalate in Regulating Cell Cycle.. *Environmental science & technology*. PMID: 33459556

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 87.7% |
| 可用 PDB 条目 | 4RG1, 8QSU, 8QSV, 8QSW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4RG1, 8QSU, 8QSV, 8QSW）+ AlphaFold高质量预测（pLDDT=88.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029028, IPR012340, IPR003750, IPR029026; Pfam: PF02598 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBC1D13 | 0.935 | 0.000 | — |
| KYAT1 | 0.929 | 0.000 | — |
| IMP4 | 0.892 | 0.000 | — |
| ENDOG | 0.886 | 0.000 | — |
| WDR46 | 0.736 | 0.000 | — |
| PISD | 0.717 | 0.000 | — |
| UTP11 | 0.712 | 0.091 | — |
| RRP8 | 0.697 | 0.000 | — |
| NOC4L | 0.696 | 0.000 | — |
| METTL17 | 0.662 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| INCA1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| CCDC59 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MECP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H1-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRNP70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 4RG1, 8QSU, 8QSV, 8QSW | pLDDT=88.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, spindle; Chromosome, cent / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SPOUT1 — 28S rRNA (uridine-N(3))-methyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小376 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T280
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198917-SPOUT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPOUT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T280
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T280-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
