---
type: protein-evaluation
gene: "ANAPC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANAPC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC4 / APC4 |
| 蛋白名称 | Anaphase-promoting complex subunit 4 |
| 蛋白大小 | 808 aa / 92.1 kDa |
| UniProt ID | Q9UJX5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 808 aa / 92.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.0; PDB: 4UI9, 5A31, 5BPW, 5G04, 5G05, 5KHR, 5KHU |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR024789, IPR024977, IPR056358, IPR024790, IPR017 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分 (÷1.83)** | | | **77.0/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- anaphase-promoting complex (GO:0005680)
- cytosol (GO:0005829)
- nuclear periphery (GO:0034399)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APC4 |

**关键文献**:
1. Development and Validation of a Prognosis-Prediction Signature for Patients with Lung Adenocarcinoma Based on 11 Telomere-Related Genes.. *Frontiers in bioscience (Landmark edition)*. PMID: 37919072
2. Unraveling the shared genetic architecture of osteoarthritis and metabolic traits through multi-omics insights.. *Osteoarthritis and cartilage*. PMID: 41167325
3. TRMT13 inhibits the growth of papillary thyroid cancer by targeting ANAPC4.. *Acta biochimica et biophysica Sinica*. PMID: 38425244
4. Genetic overlap and causality between COVID-19 and multi-site chronic pain: the importance of immunity.. *Frontiers in immunology*. PMID: 38633255
5. Transcriptome Analysis of Reciprocal Hybrids Between Crassostrea gigas and C. angulata Reveals the Potential Mechanisms Underlying Thermo-Resistant Heterosis.. *Marine biotechnology (New York, N.Y.)*. PMID: 36653591

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 38.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 81.1% |
| 可用 PDB 条目 | 4UI9, 5A31, 5BPW, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4UI9, 5A31, 5BPW, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW）+ AlphaFold预测（pLDDT=81.0），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024789, IPR024977, IPR056358, IPR024790, IPR017169; Pfam: PF12896, PF12894, PF23405 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANAPC13 | 0.999 | 0.984 | — |
| ANAPC11 | 0.999 | 0.998 | — |
| CDC16 | 0.999 | 0.998 | — |
| CCNB1 | 0.999 | 0.994 | — |
| CDC20 | 0.999 | 0.999 | — |
| ANAPC5 | 0.999 | 0.999 | — |
| ANAPC2 | 0.999 | 0.999 | — |
| FBXO5 | 0.999 | 0.999 | — |
| CDC23 | 0.999 | 0.999 | — |
| NEK2 | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sirt2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22014574|imex:IM-16607 |
| anapc4.L | psi-mi:"MI:0030"(cross-linking study) | pubmed:20951947|imex:IM-15161 |
| MGC80529 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20951947|imex:IM-15161 |
| PTEN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| CDC27 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cdc26 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ANAPC16 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11719|pubmed:20360068 |
| ANAPC1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ANAPC5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 4UI9, 5A31, 5BPW, 5G04, 5G05,  | pLDDT=81.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ANAPC4 — Anaphase-promoting complex subunit 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小808 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJX5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000053900-ANAPC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJX5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:49:54

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJX5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UJX5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024789;IPR024977;IPR056358;IPR024790;IPR017169;IPR015943;IPR036322; |
| Pfam | PF12896;PF12894;PF23405; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000053900-ANAPC4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANAPC1 | Biogrid, Opencell | true |
| ANAPC10 | Biogrid, Opencell | true |
| ANAPC11 | Biogrid, Opencell | true |
| ANAPC13 | Biogrid, Opencell, Bioplex | true |
| ANAPC16 | Biogrid, Opencell, Bioplex | true |
| ANAPC2 | Intact, Biogrid, Opencell | true |
| ANAPC5 | Biogrid, Opencell, Bioplex | true |
| ANAPC7 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
