---
type: protein-evaluation
gene: "CCDC62"
date: 2026-05-31
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## CCDC62 核-胞质蛋白

UniProt: Q6P9F0. Nuclear receptor coactivator (ESR1/ESR2).

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt Nucleus + Cytoplasm ECO:0000269; GO nucleus IDA |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 684 aa |
| 研究新颖性 | 8/10 | ×5 | 50.0 | PubMed strict=21, broad=36 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT 64.4 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Nuclear receptor coactivator |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING/IntAct: ESR2 core partner |
| **加权总分** | | | **119/180************ | |
| 互证加分 | | | +1.5 | Nucleus IDA + coactivator function |
| **归一化总分 (÷1.83)** | | | **65.0/100************ | |

**核定位证据**: UniProt Nucleus + Cytoplasm + Acrosome ECO:0000269. GO nucleus IDA:ParkinsonsUK-UCL. Nuclear receptor coactivator -- functional confirmation of nuclear localization.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。


PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| HIP1R | STRING | score=0.873, exp=0 | Textmining only |
| ESR2 | STRING | score=0.706, exp=0.292 | Estrogen receptor beta; also UniProt (6 experiments) + IntAct (two hybrid) |
| CCND1 | STRING | score=0.598, exp=0.292 | Cyclin D1; co-expression |
| SDHA | IntAct | cross-linking | Succinate dehydrogenase |
| PLEC | IntAct | cross-linking | Plectin |
| CFTR | IntAct | pull down | Cystic fibrosis transporter |

**IntAct 数据**: ESR2 (two hybrid, ChIP), SDHA (cross-linking), PLEC (cross-linking), CFTR (pull down) 。UniProt 记载 ESR2（6 个实验）。无 BioGrid 补充数据。

Strong nuclear receptor coactivator.



#### 关键文献
| PMID | 标题 |
|---|---|
| 22507762 | Psychotropic drug effects on gene transcriptomics relevant to Parkinson's disease. |
| 28339613 | A nonsense mutation in Ccdc62 gene is responsible for spermiogenesis defects and male infertility in |
| 19126643 | CCDC62/ERAP75 functions as a coactivator to enhance estrogen receptor beta-mediated transactivation  |
| 36047070 | Globozoospermia: A Case Report and Systematic Review of Literature. |
| 24335092 | CCDC62 variant rs12817488 is associated with the risk of Parkinson's disease in a Han Chinese popula |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000130783-CCDC62/subcellular

![](https://images.proteinatlas.org/39021/435_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39021/435_E6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39021/445_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39021/445_E6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39021/448_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39021/448_E6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P9F0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P9F0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | 未检出 |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130783-CCDC62/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ESR2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
