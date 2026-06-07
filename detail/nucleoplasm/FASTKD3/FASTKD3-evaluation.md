---
type: protein-evaluation
gene: "FASTKD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FASTKD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FASTKD3 |
| 蛋白名称 | FAST kinase domain-containing protein 3, mitochondrial |
| 蛋白大小 | 662 aa / 75.7 kDa |
| UniProt ID | Q14CZ7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FASTKD3/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FASTKD3/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Mitochondria; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 662 aa / 75.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Supported |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- ribonucleoprotein granule (GO:0035770)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Systematic Analysis of FASTK Gene Family Alterations in Cancer.. *International journal of molecular sciences*. PMID: 34768773
2. Fast kinase domain-containing protein 3 is a mitochondrial protein essential for cellular respiration.. *Biochemical and biophysical research communications*. PMID: 20869947
3. Role of FAST Kinase Domains 3 (FASTKD3) in Post-transcriptional Regulation of Mitochondrial Gene Expression.. *The Journal of biological chemistry*. PMID: 27789713
4. Identification of the Six-RNA-Binding Protein Signature for Prognosis Prediction in Bladder Cancer.. *Frontiers in genetics*. PMID: 32983230
5. Report of a chimeric origin of transposable elements in a bovine-coding gene.. *Genetics and molecular research : GMR*. PMID: 18273826

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.7 |
| 高置信度残基 (pLDDT>90) 占比 | 58.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 81.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FASTKD3/FASTKD3-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=81.7，有序区 81.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam: PF06743, PF08368, PF08373 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTCD1 | 0.855 | 0.292 | — |
| DHX30 | 0.769 | 0.329 | — |
| MRPS31 | 0.766 | 0.329 | — |
| IARS2 | 0.762 | 0.368 | — |
| MRPS22 | 0.760 | 0.329 | — |
| PNPT1 | 0.752 | 0.329 | — |
| LRPPRC | 0.733 | 0.329 | — |
| MTO1 | 0.727 | 0.292 | — |
| FASTKD2 | 0.726 | 0.292 | — |
| GFM1 | 0.719 | 0.311 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SLAMF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPACA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LAMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPY2R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BSG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MUC20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA12 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.7 + PDB: 无 | pLDDT=81.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion / Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FASTKD3 — FAST kinase domain-containing protein 3, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小662 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14CZ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124279-FASTKD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FASTKD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14CZ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FASTKD3/FASTKD3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14CZ7 |
| SMART | SM00952; |
| UniProt Domain [FT] | DOMAIN 591..649; /note="RAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00619" |
| InterPro | IPR013579;IPR050870;IPR010622;IPR013584; |
| Pfam | PF06743;PF08368;PF08373; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124279-FASTKD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTRAP | Intact | false |
| FAM9B | Intact | false |
| FASTKD1 | Biogrid | false |
| GPR182 | Bioplex | false |
| MAGEA12 | Intact | false |
| PDHA1 | Biogrid | false |
| TMEM9 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
