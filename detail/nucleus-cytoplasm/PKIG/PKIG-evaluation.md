---
type: protein-evaluation
gene: "PKIG"
date: 2026-05-31
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## PKIG 核-胞质蛋白

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | GO cytoplasm IBA + nucleus IBA |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 76 aa (~7.9 kDa) |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=11, broad=19 |
| 三维结构 | 5/10 | ×3 | 15.0 | AlphaFold pLDDT 62.9 |
| 调控结构域 | 5/10 | ×2 | 10.0 | PKA inhibitor domain |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING: PKIA/PKIB family; IntAct: PKA catalytic subunits |
| **加权总分** | | | **114/180**** | |
| 互证加分 | | | +0.0 | IBA evidence only |
| **归一化总分 (÷1.83)** | | | **62.3/100**** | |

**核定位证据**: GO cytoplasm IBA + nucleus IBA. cAMP-dependent protein kinase inhibitor gamma.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[PKIG-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| PKIA | STRING | score=0.982, exp=0 | PKA inhibitor family; textmining |
| ADA | STRING | score=0.771, exp=0 | Adenosine deaminase; textmining |
| PRKACB | STRING | score=0.764, exp=0.700 | PKA catalytic subunit beta; strong experimental |
| PRKACA | STRING | score=0.653, exp=0.564 | PKA catalytic subunit alpha; also IntAct (coIP) |
| PKIB | STRING | score=0.637, exp=0 | PKA inhibitor family; textmining |
| PRKACG | IntAct | anti tag coIP | PKA catalytic subunit gamma; also STRING exp=0.435 |
| KPTN | IntAct | anti bait coIP | Kaptin; actin binding |
| DYNLL1 | IntAct | two hybrid prey pooling | Dynein light chain |
| DYNLL2 | IntAct | two hybrid array | Dynein light chain |

**IntAct 数据**: PRKACA, PRKACB, PRKACG (coIP), KPTN, RPA3, RAB25, DYNLL1, DYNLL2, TYMS, TPM2, MEOX2 等 12 条互作记录。STRING 中 PRKACB (exp=0.700) 和 PRKACA (exp=0.564) 有强实验信号。无 BioGrid 补充数据。UniProt 未记载互作伙伴。

Low-confidence nucleus-cytoplasm; IBA evidence only.

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/PKIG/PKIG-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 10880337 | Cloning and mapping of human PKIB and PKIG, and comparison of tissue expression patterns of three me |
| 39548579 | Blood mir-331-3p is a potential diagnostic marker for giant panda (Ailuropoda melanoleuca) testicula |
| 40395612 | Assessment of molecular and morphological dynamics during long-time in vitro cultivation of cryopres |
| 37653016 | [Exploration of the Perturbation of PKIG in Lung Squamous Cell Carcinoma and the Role in Tumor Micro |
| 33885249 | Glucose deprivation affects the expression of genes encoding cAMP-activated protein kinase and relat |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/PKIG/PKIG-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000168734-PKIG/subcellular

![](https://images.proteinatlas.org/42703/2171_H4_53_blue_red_green.jpg)
![](https://images.proteinatlas.org/42703/2171_H4_68_blue_red_green.jpg)
![](https://images.proteinatlas.org/42703/468_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/42703/468_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/42703/470_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/42703/470_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
