---
type: protein-evaluation
gene: "CCDC88A"
date: 2026-05-31
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## CCDC88A 核质蛋白 (Girdin)

UniProt: Q3V6T2.

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | GO nucleoplasm IDA:HPA; membrane/centrosome/lamellipodium in UniProt |
| 蛋白大小 | 2/10 | ×1 | 2.0 | 1871 aa (~216 kDa) |
| 研究新颖性 | 6/10 | ×5 | 30.0 | Strict=48 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 66.3; PDB 6MHF |
| 调控结构域 | 6/10 | ×2 | 12.0 | G-protein modulator; AKT-mTOR signaling hub |
| PPI 网络 | 7/10 | ×3 | 21.0 | STRING/IntAct: GNAI3, AKT1, EGFR network |
| **加权总分** | | | **111/180********** | |
| 互证加分 | | | +1.5 | Nucleoplasm IDA:HPA + centrosome IDA:HPA |
| **归一化总分 (÷1.83)** | | | **60.7/100********** | |

PubMed strict: 48



**核定位证据**: GO nucleoplasm IDA:HPA. Membrane/centrosome/lamellipodium in UniProt. Girdin -- EGFR/AKT-mTOR signaling hub. PDB 6MHF.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。


PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| GNAI3 | STRING | score=0.918, exp=0.770 | G protein alpha subunit; strong experimental evidence |
| DISC1 | STRING | score=0.863, exp=0.342 | Neuronal development; also IntAct (two hybrid) |
| AKT1 | STRING | score=0.826, exp=0.532 | AKT-mTOR pathway; key signaling effector |
| NDEL1 | STRING | score=0.738, exp=0.342 | Dynein regulator; also IntAct (two hybrid) |
| EGFR | STRING | score=0.591, exp=0.469 | EGFR signaling; membrane retention |
| DCTN1 | STRING | score=0.576, exp=0.544 | Dynactin; motor protein |
| GNAI2 | IntAct | anti tag coIP | G protein alpha subunit |
| PARD3 | IntAct | anti tag coIP | Cell polarity |
| YWHAB | IntAct | anti tag coIP | 14-3-3 scaffold |

**IntAct 数据**: GNAI2, YWHAB, PARD3, DISC1, NDEL1, PRKACA, BRAF, YWHAZ 等多条互作记录（涵盖 coIP, two hybrid, TAP 等方法）。STRING 有强实验信号 (GNAI3 exp=0.770, AKT1 exp=0.532)。无 BioGrid 补充数据。UniProt 未记载互作伙伴。

Large signaling protein with HPA-derived nuclear annotation.



#### 关键文献
| PMID | 标题 |
|---|---|
| 37357876 | The association between the CCDC88A gene polymorphism at rs1437396 and alcohol use disorder, with or |
| 39480488 | Breast cancers that disseminate to bone marrow acquire aggressive phenotypes through CX43-related tu |
| 34190023 | CCDC88A/GIV promotes HBV replication and progeny secretion via enhancing endosomal trafficking and b |
| 35493459 | CCDC88A Post-Transcriptionally Regulates VEGF via miR-101 and Subsequently Regulates Hepatocellular  |
| 37798908 | Refining the phenotypic spectrum of CCDC88A-related PEHO-like syndrome. |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000115355-CCDC88A/subcellular

![](https://images.proteinatlas.org/38102/2179_D2_30_red_green.jpg)
![](https://images.proteinatlas.org/38102/2179_D2_42_red_green.jpg)
![](https://images.proteinatlas.org/38102/2242_F1_53_red_green.jpg)
![](https://images.proteinatlas.org/38102/2242_F1_79_red_green.jpg)
![](https://images.proteinatlas.org/38102/404_G3_3_red_green.jpg)
![](https://images.proteinatlas.org/38102/404_G3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3V6T2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3V6T2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 12..132; /note="Calponin-homology (CH)"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044" |
| InterPro | IPR001715;IPR036872;IPR043936; |
| Pfam | PF19047; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115355-CCDC88A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKT1 | Biogrid | false |
| CTNNA2 | Biogrid | false |
| CTNNB1 | Biogrid | false |
| EGFR | Biogrid | false |
| GJA1 | Biogrid | false |
| GNAI3 | Biogrid | false |
| INSR | Biogrid | false |
| KRAS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
