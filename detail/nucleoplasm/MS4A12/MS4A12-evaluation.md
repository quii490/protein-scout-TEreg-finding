---
type: protein-evaluation
gene: "MS4A12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MS4A12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MS4A12 |
| 蛋白名称 | Membrane-spanning 4-domains subfamily A member 12 |
| 蛋白大小 | 267 aa / 28.1 kDa |
| UniProt ID | Q9NXJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoli, Endoplasmic reticulu; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 267 aa / 28.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007237, IPR030417; Pfam: PF04103 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoli, Endoplasmic reticulum, Golgi apparatus | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CLCA4 and MS4A12 as the significant gene biomarkers of primary colorectal cancer.. *Bioscience reports*. PMID: 32797167
2. Role of enterocyte-specific gene polymorphisms in response to adjuvant treatment for stage III colorectal cancer.. *Pharmacogenetics and genomics*. PMID: 32732498
3. Decreased expression of MS4A12 inhibits differentiation and predicts early stage survival in colon cancer.. *Neoplasma*. PMID: 27881006
4. MS4A12 is a colon-selective store-operated calcium channel promoting malignant cell processes.. *Cancer research*. PMID: 18451174
5. Plasma Membrane Localized GCaMP-MS4A12 by Orai1 Co-Expression Shows Thapsigargin- and Ca(2+)-Dependent Fluorescence Increases.. *Molecules and cells*. PMID: 33935043

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 39.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 32.6% |
| 有序区域 (pLDDT>70) 占比 | 55.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.4，有序区 55.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007237, IPR030417; Pfam: PF04103 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MS4A6E | 0.931 | 0.000 | — |
| MS4A4E | 0.915 | 0.000 | — |
| ZG16 | 0.801 | 0.000 | — |
| GUCA2A | 0.716 | 0.000 | — |
| CLCA4 | 0.706 | 0.000 | — |
| AQP8 | 0.704 | 0.000 | — |
| GUCA2B | 0.659 | 0.000 | — |
| TMIGD1 | 0.624 | 0.000 | — |
| KRT20 | 0.602 | 0.000 | — |
| NXPE4 | 0.545 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLLP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MALL | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM3A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| STOM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM63B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP6V0A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYADM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP6V0A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 无 | pLDDT=71.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cytosol; 额外: Nucleoli, Endoplasmi | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

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
1. MS4A12 — Membrane-spanning 4-domains subfamily A member 12，非常新颖，仅有少数基础研究。
2. 蛋白大小267 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000071203-MS4A12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MS4A12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000071203-MS4A12/subcellular

![](https://images.proteinatlas.org/48616/1838_E2_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/48616/1838_E2_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/48616/1868_G10_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/48616/1868_G10_32_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NXJ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXJ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007237;IPR030417; |
| Pfam | PF04103; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000071203-MS4A12/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP6V0A2 | Bioplex | false |
| MALL | Intact | false |
| MYADM | Bioplex | false |
| PLLP | Intact | false |
| STOM | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
