---
type: protein-evaluation
gene: "PLPP6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLPP6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLPP6 / PDP1, PPAPDC2 |
| 蛋白名称 | Polyisoprenoid diphosphate/phosphate phosphohydrolase PLPP6 |
| 蛋白大小 | 295 aa / 32.2 kDa |
| UniProt ID | Q8IY26 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane; Nucleus envelope; Nucleus in |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 32.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000326, IPR036938; Pfam: PF01569 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane; Nucleus envelope; Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PDP1, PPAPDC2 |

**关键文献**:
1. Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.. *medRxiv : the preprint server for health sciences*. PMID: 40196253
2. Whole-genome sequencing reveals individual and cohort level insights into chromosome 9p syndromes.. *Genome medicine*. PMID: 41137173
3. Preliminary Study: Proteomic Profiling Uncovers Potential Proteins for Biomonitoring Equine Melanocytic Neoplasm.. *Animals : an open access journal from MDPI*. PMID: 34199079

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 44.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 30.5% |
| 有序区域 (pLDDT>70) 占比 | 62.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.5，有序区 62.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000326, IPR036938; Pfam: PF01569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLPP1 | 0.941 | 0.000 | — |
| EPHX2 | 0.814 | 0.000 | — |
| PIGC | 0.557 | 0.000 | — |
| PLPP5 | 0.545 | 0.000 | — |
| GPR182 | 0.513 | 0.143 | — |
| PLPP4 | 0.512 | 0.000 | — |
| PRRC2C | 0.506 | 0.000 | — |
| PLPP2 | 0.490 | 0.000 | — |
| PUDP | 0.476 | 0.000 | — |
| MTMR9 | 0.474 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| RNF5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GPX8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| VSIR | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CREB3L1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MS4A3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM210B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SMAGP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| STX1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 无 | pLDDT=72.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus envelope;  / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
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
1. PLPP6 — Polyisoprenoid diphosphate/phosphate phosphohydrolase PLPP6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205808-PLPP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLPP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000205808-PLPP6/subcellular

![](https://images.proteinatlas.org/18096/144_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/18096/144_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/18096/145_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/18096/145_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/18096/1846_A1_10_cr5ab9265104ba4_red_green.jpg)
![](https://images.proteinatlas.org/18096/1846_A1_19_cr5ab9265106214_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IY26-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IY26 |
| SMART | SM00014; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000326;IPR036938; |
| Pfam | PF01569; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205808-PLPP6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AMIGO1 | Intact | false |
| AQP6 | Intact | false |
| AQP8 | Intact | false |
| C16orf92 | Intact | false |
| CD79A | Intact | false |
| CIAO2A | Intact | false |
| CLDN9 | Intact | false |
| CLEC4M | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
