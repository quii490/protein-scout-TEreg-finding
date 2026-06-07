---
type: protein-evaluation
gene: "HAUS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HAUS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAUS2 / C15orf25, CEP27 |
| 蛋白名称 | HAUS augmin-like complex subunit 2 |
| 蛋白大小 | 235 aa / 26.9 kDa |
| UniProt ID | Q9NVX0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 26.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.5; PDB: 7SQK |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028346, IPR026242; Pfam: PF15003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- HAUS complex (GO:0070652)
- mitotic spindle microtubule (GO:1990498)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf25, CEP27 |

**关键文献**:
1. A prognostic model based on the Augmin family genes for LGG patients.. *Scientific reports*. PMID: 37161065
2. Brain Epitranscriptomic Analysis Revealed Altered A-to-I RNA Editing in Septic Patients.. *Frontiers in genetics*. PMID: 35559016
3. ZNF131 suppresses centrosome fragmentation in glioblastoma stem-like cells through regulation of HAUS5.. *Oncotarget*. PMID: 28596487

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.5 |
| 高置信度残基 (pLDDT>90) 占比 | 42.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 7SQK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.5，有序区 74.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028346, IPR026242; Pfam: PF15003 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HAUS1 | 0.999 | 0.973 | — |
| HAUS3 | 0.999 | 0.965 | — |
| HAUS8 | 0.999 | 0.985 | — |
| HAUS7 | 0.999 | 0.988 | — |
| HAUS6 | 0.999 | 0.986 | — |
| HAUS5 | 0.999 | 0.984 | — |
| HAUS4 | 0.998 | 0.965 | — |
| TUBG1 | 0.841 | 0.165 | — |
| CEP290 | 0.815 | 0.000 | — |
| ZNF223 | 0.777 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FXYD6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Haus4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| XRCC4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.5 + PDB: 7SQK | pLDDT=80.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Cytosol; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HAUS2 — HAUS augmin-like complex subunit 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVX0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137814-HAUS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAUS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVX0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000137814-HAUS2/subcellular

![](https://images.proteinatlas.org/39965/460_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39965/460_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39965/465_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39965/465_E11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39965/467_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39965/467_E11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVX0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVX0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028346;IPR026242; |
| Pfam | PF15003; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137814-HAUS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HAUS1 | Intact, Biogrid | true |
| HAUS6 | Intact, Biogrid | true |
| HAUS7 | Intact, Biogrid | true |
| HAUS8 | Intact, Biogrid | true |
| ARFIP1 | Opencell | false |
| HAUS3 | Biogrid | false |
| HAUS4 | Biogrid | false |
| HAUS5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
