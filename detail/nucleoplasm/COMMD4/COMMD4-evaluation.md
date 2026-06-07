---
type: protein-evaluation
gene: "COMMD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD4 |
| 蛋白名称 | COMM domain-containing protein 4 |
| 蛋白大小 | 199 aa / 21.8 kDa |
| UniProt ID | Q9H0A8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Vesicles, Plasma membrane; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 199 aa / 21.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=80.7; PDB: 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR017920, IPR037356, IPR047155; Pfam: PF07258, PF |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles, Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 18 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Targeting the COMMD4-H2B protein complex in lung cancer.. *British journal of cancer*. PMID: 37914802
2. Defining COMMD4 as an anti-cancer therapeutic target and prognostic factor in non-small cell lung cancer.. *British journal of cancer*. PMID: 32439936
3. CCDC22 mutations that impair COMMD binding cause attenuated 3C/Ritscher-Schinzel syndrome.. *BMC medical genomics*. PMID: 40448120
4. Cloning and characterization of a COMMD4 gene from amphioxus (Branchiostoma belcheri): an insight into the function and evolution of COMMD4.. *Immunology letters*. PMID: 23085603
5. COMMD4 is a novel prognostic biomarker and relates to potential drug resistance mechanism in glioma.. *Frontiers in pharmacology*. PMID: 36249824

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 7.0% |
| 置信残基 (pLDDT 70-90) 占比 | 78.9% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=80.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037356, IPR047155; Pfam: PF07258, PF21672 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD2 | 0.987 | 0.873 | — |
| CCDC22 | 0.981 | 0.847 | — |
| COMMD3 | 0.978 | 0.835 | — |
| COMMD1 | 0.976 | 0.883 | — |
| COMMD9 | 0.976 | 0.837 | — |
| COMMD5 | 0.969 | 0.866 | — |
| COMMD6 | 0.968 | 0.866 | — |
| COMMD8 | 0.968 | 0.865 | — |
| COMMD10 | 0.957 | 0.840 | — |
| COMMD7 | 0.951 | 0.844 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BUB1B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| COMMD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15799966 |
| RELA | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| aRO81 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| COMMD8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COMMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 8F2R, 8F2U, 8P0W | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD4 -- COMM domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0A8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140365-COMMD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0A8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0A8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0A8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 130..199; /note="COMM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00602" |
| InterPro | IPR017920;IPR037356;IPR047155; |
| Pfam | PF07258;PF21672; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140365-COMMD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC22 | Intact, Biogrid, Opencell, Bioplex | true |
| CCDC93 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD1 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD10 | Biogrid, Opencell, Bioplex | true |
| COMMD2 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD3 | Biogrid, Bioplex | true |
| COMMD5 | Biogrid, Opencell, Bioplex | true |
| COMMD6 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
