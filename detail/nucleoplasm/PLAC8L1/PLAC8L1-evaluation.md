---
type: protein-evaluation
gene: "PLAC8L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLAC8L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLAC8L1 |
| 蛋白名称 | PLAC8-like protein 1 |
| 蛋白大小 | 177 aa / 19.9 kDa |
| UniProt ID | A1L4L8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 177 aa / 19.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006461; Pfam: PF04749 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. miRNA-mRNA analysis of sheep adrenal glands reveals the network regulating reproduction.. *BMC genomic data*. PMID: 35710353
2. RNA sequencing to study gene expression and SNP variations associated with growth in zebrafish fed a plant protein-based diet.. *Marine biotechnology (New York, N.Y.)*. PMID: 25702041

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 50.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 27.1% |
| 有序区域 (pLDDT>70) 占比 | 58.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.6，有序区 58.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006461; Pfam: PF04749 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM172A | 0.709 | 0.000 | — |
| GRIK3 | 0.560 | 0.000 | — |
| PCYOX1 | 0.523 | 0.000 | — |
| RNPC3 | 0.522 | 0.000 | — |
| HMHB1 | 0.506 | 0.000 | — |
| TDRD3 | 0.461 | 0.000 | — |
| ENKUR | 0.453 | 0.000 | — |
| GRXCR2 | 0.453 | 0.000 | — |
| NCOA1 | 0.448 | 0.183 | — |
| NCOA3 | 0.448 | 0.183 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTPRD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SERPINB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| S100A7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SERPINB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZDHHC13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZDHHC17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POF1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 无 | pLDDT=72.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLAC8L1 — PLAC8-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1L4L8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173261-PLAC8L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLAC8L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1L4L8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173261-PLAC8L1/subcellular

![](https://images.proteinatlas.org/74266/1709_D2_13_cr580481b53aa5a_red_green.jpg)
![](https://images.proteinatlas.org/74266/1709_D2_3_cr580481aa0ba5d_red_green.jpg)
![](https://images.proteinatlas.org/74266/1791_F5_3_red_green.jpg)
![](https://images.proteinatlas.org/74266/1791_F5_4_red_green.jpg)
![](https://images.proteinatlas.org/74266/1820_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/74266/1820_F5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A1L4L8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A1L4L8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006461; |
| Pfam | PF04749; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173261-PLAC8L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT4 | Bioplex | false |
| CCT6A | Bioplex | false |
| CCT6B | Bioplex | false |
| CCT7 | Bioplex | false |
| PDCL | Bioplex | false |
| PDCL3 | Bioplex | false |
| TCP1 | Bioplex | false |
| ZDHHC13 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
