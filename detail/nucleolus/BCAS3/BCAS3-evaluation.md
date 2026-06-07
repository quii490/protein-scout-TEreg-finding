---
type: protein-evaluation
gene: "BCAS3"
date: 2026-06-03
tags: [protein-scout, nucleolus, evaluation]
status: scored
---

## BCAS3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BCAS3 / 无 |
| 蛋白全名 | BCAS3 microtubule associated cell migration factor |
| 蛋白大小 | 928 aa / 101.2 kDa |
| UniProt ID | Q9H6U6 (BCAS3_HUMAN) |
| 功能描述 | Plays a role in angiogenesis. Participates in the regulation of cell polarity and directional endothelial cell migration by mediating both the activation and recruitment of CDC42 and the reorganization of the actin cytoskeleton at the cell leading edge. Promotes filipodia formation (By similarity). Functions synergistically with PELP1 as a transcriptional coactivator of estrogen receptor-responsiv... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | UniProt experimental nuclear + (Nucleus, Cytoplasm, Cytoplasm, cytoskeleton, Preautophagosomal structure) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 928 aa / 101.2 kDa, <300或>800 |
| 研究新颖性 | 6/10 | x5 | 30.0 | PubMed strict=46（中等偏少，41-60→6分） |
| 三维结构 | 4/10 | x3 | 12.0 | AF low-moderate: mean pLDDT 64.6 |
| 调控结构域 | 8/10 | x2 | 16.0 | Chromatin-associated regulatory protein |
| PPI 网络 | 3/10 | x3 | 9.0 | IntAct experiment: 15 partners (1 regulatory: GATA3) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **109/180**************** | |
| **归一化总分 (÷1.83)** | | | **59.6/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Nucleoli |
| HPA 额外定位 | 无数据 |
| 抗体可靠性 | Approved |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 46 |
| symbol_only (Title/Abstract) | 68 |
| broad (all fields) | 69 |

1. PMID 38869949: Franco-Romero A, Morbidoni V, Milan G (2024 Jun 13). "C16ORF70/MYTHO promotes healthy aging in C.elegans and prevents cellular senescence in mammals.." *The Journal of clinical investigation*.
2. PMID 37231097: Chen CY, Tian R, Ge T (2023 Jun). "The impact of rare protein coding genetic variation on adult cognitive function.." *Nature genetics*.
3. PMID 40481608: Liu H, Sun N, Liu Z (2025 Jun 6). "Knockout of bcas3 gene causes neurodevelopment defects in zebrafish.." *Biological research*.
4. PMID 32116088: Yamada Y, Schaap P (2021 Mar). "The proppin Bcas3 and its interactor KinkyA localize to the early phagophore and regulate autophagy.." *Autophagy*.
5. PMID 33499712: Kojima W, Yamano K, Kosako H (2021 Aug). "Mammalian BCAS3 and C16orf70 associate with the phagophore assembly site in response to selective and non-selective autophagy.." *Autophagy*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 64.6 |
| pLDDT >90 | 30.3% |
| pLDDT 70-90 | 16.9% |
| pLDDT 50-70 | 12.4% |
| pLDDT <50 | 40.4% |

**评价**: AlphaFold 预测置信度较低（mean pLDDT 64.6），40% 残基 <50，蛋白可能含有大量无序区域。



### 6. PDB 条目

0 entries found.

### 7. InterPro/Pfam 结构域

| InterPro | IPR045142 | IPR entry IPR045142 |
| InterPro | IPR022175 | IPR entry IPR022175 |
| InterPro | IPR048382 | IPR entry IPR048382 |
| InterPro | IPR015943 | IPR entry IPR015943 |
| InterPro | IPR036322 | IPR entry IPR036322 |
| Pfam | PF12490 | Pfam entry PF12490 |
| Pfam | PF21034 | Pfam entry PF21034 |

**评价**: BCAS3 微管结合蛋白，参与微管乙酰化和稳定性调控。其功能与细胞骨架动态相关，非经典核蛋白。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| BCAS4 | 0.983 | 0.000 | 0.000 | 0.983 |
| C16orf70 | 0.947 | 0.850 | 0.000 | 0.613 |
| WIPI2 | 0.877 | 0.834 | 0.000 | 0.256 |
| MTA1 | 0.704 | 0.000 | 0.000 | 0.704 |
| VIM | 0.698 | 0.510 | 0.000 | 0.410 |
| TBX4 | 0.697 | 0.000 | 0.000 | 0.697 |
| ESR1 | 0.639 | 0.292 | 0.000 | 0.512 |
| TBX2 | 0.638 | 0.000 | 0.000 | 0.628 |
| APPBP2 | 0.559 | 0.000 | 0.000 | 0.517 |
| MAGEE1 | 0.558 | 0.558 | 0.000 | 0.000 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| VIM | psi-mi:"MI:0663"(confocal microscopy) | pubmed:22300583|imex:IM-20589 | psi-mi:"MI:0403"(colocalization) |
| PHAF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubme | psi-mi:"MI:0915"(physical association) |
| CTBP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 | psi-mi:"MI:0915"(physical association) |
| CDC23 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 | psi-mi:"MI:0915"(physical association) |
| CTBP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 | psi-mi:"MI:0915"(physical association) |
| RAB2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| VWA5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| PLEKHF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| DOCK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| IL17RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| CDC23 | 3 |
| CTBP1 | 3 |
| CTBP2 | 3 |
| PHAF1 | 4 |
| PLEKHF2 | 3 |
| VIM | 3 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**核心优势**:
1. 核定位证据充分（得分 9/10），多源验证一致

**风险/不确定性**:

**分类**: nucleolus
**综合评分**: 60/100

---

**数据来源**: UniProt Q9H6U6, HPA ENSG00000141376, AlphaFold AF-Q9H6U6-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000141376-BCAS3/subcellular

![](https://images.proteinatlas.org/57289/1432_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/57289/1432_C8_6_red_green.jpg)
![](https://images.proteinatlas.org/57289/963_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/57289/963_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/57289/968_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/57289/968_F6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H6U6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045142;IPR022175;IPR048382;IPR015943;IPR036322; |
| Pfam | PF12490;PF21034; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141376-BCAS3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PHAF1 | Intact, Biogrid | true |
| CAPZB | Opencell | false |
| CDC23 | Intact | false |
| DDB1 | Biogrid | false |
| ESR1 | Biogrid | false |
| H3C1 | Biogrid | false |
| PELP1 | Biogrid | false |
| PLEKHF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
