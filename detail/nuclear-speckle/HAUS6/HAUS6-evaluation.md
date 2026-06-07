---
type: protein-evaluation
gene: "HAUS6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HAUS6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAUS6 / DGT6, FAM29A, KIAA1574 |
| 蛋白名称 | HAUS augmin-like complex subunit 6 |
| 蛋白大小 | 955 aa / 108.6 kDa |
| UniProt ID | Q7Z4H7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centriolar satellite, Cytosol, Acrosome; 额外: Nuclear speckle; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle; C |
| 蛋白大小 | 8/10 | ×1 | 8 | 955 aa / 108.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.9; PDB: 7SQK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026797, IPR028163; Pfam: PF14661 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite, Cytosol, Acrosome; 额外: Nuclear speckles, Connecting piece, Mid piece, Principal piece | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, microtubule orga... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- HAUS complex (GO:0070652)
- mitotic spindle microtubule (GO:1990498)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DGT6, FAM29A, KIAA1574 |

**关键文献**:
1. Genetic Control of Kinetochore-Driven Microtubule Growth in Drosophila Mitosis.. *Cells*. PMID: 35883570
2. HAUS6 as a potential prognostic and immunological biomarker: validation from pan-cancer analysis to hepatocellular carcinoma.. *Cancer cell international*. PMID: 41286847
3. A prognostic model based on the Augmin family genes for LGG patients.. *Scientific reports*. PMID: 37161065
4. Mitotic spindle assembly and γ-tubulin localisation depend on the integral nuclear membrane protein Samp1.. *Journal of cell science*. PMID: 29514856
5. Identification of ZCCHC8 as fusion partner of ROS1 in a case of congenital glioblastoma multiforme with a t(6;12)(q21;q24.3).. *Genes, chromosomes & cancer*. PMID: 27121553

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.9 |
| 高置信度残基 (pLDDT>90) 占比 | 9.2% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 48.8% |
| 有序区域 (pLDDT>70) 占比 | 35.5% |
| 可用 PDB 条目 | 7SQK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.9），有序残基占 35.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026797, IPR028163; Pfam: PF14661 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HAUS5 | 0.999 | 0.971 | — |
| HAUS7 | 0.999 | 0.986 | — |
| HAUS2 | 0.999 | 0.986 | — |
| HAUS8 | 0.999 | 0.989 | — |
| HAUS1 | 0.999 | 0.974 | — |
| HAUS4 | 0.999 | 0.965 | — |
| HAUS3 | 0.999 | 0.993 | — |
| NEDD1 | 0.993 | 0.314 | — |
| TUBG1 | 0.941 | 0.091 | — |
| NUMA1 | 0.924 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000070504.8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ENSP00000369871.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TAF9 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| UVRAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Haus4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Haus1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.9 + PDB: 7SQK | pLDDT=55.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / Centriolar satellite, Cytosol, Acrosome; 额外: Nucle | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HAUS6 — HAUS augmin-like complex subunit 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小955 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4H7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147874-HAUS6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAUS6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4H7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (approved)。来源: https://www.proteinatlas.org/ENSG00000147874-HAUS6/subcellular

![](https://images.proteinatlas.org/20965/2215_D10_27_blue_red_green.jpg)
![](https://images.proteinatlas.org/20965/2215_D10_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/20965/1772_B2_6_red_green.jpg)
![](https://images.proteinatlas.org/20965/1772_B2_7_red_green.jpg)
![](https://images.proteinatlas.org/20965/177_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/20965/177_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4H7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4H7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026797;IPR028163; |
| Pfam | PF14661; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147874-HAUS6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HAUS1 | Intact, Biogrid | true |
| HAUS2 | Intact, Biogrid | true |
| HAUS3 | Intact, Biogrid | true |
| HAUS4 | Intact, Biogrid | true |
| HAUS5 | Intact, Biogrid | true |
| HAUS7 | Intact, Biogrid | true |
| HAUS8 | Intact, Biogrid | true |
| KDM1A | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
