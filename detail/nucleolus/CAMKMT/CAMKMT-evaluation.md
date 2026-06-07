---
type: protein-evaluation
gene: "CAMKMT"
date: 2026-05-31
tags: [protein-scout, nucleolus, evaluation]
status: scored
---

## CAMKMT 核仁蛋白

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | GO nucleolus IDA:HPA + nucleoplasm IDA:HPA |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 323 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=11, broad=15 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 84.8; PDB 4PWY (X-ray 1.90A) |
| 调控结构域 | 5/10 | ×2 | 10.0 | Methyltransferase domain |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING methyltransferase network; IntAct limited |
| **加权总分** | | | **131/180********** | |
| 互证加分 | | | +2.0 | Nucleolus + nucleoplasm IDA:HPA |
| **归一化总分 (÷1.83)** | | | **71.6/100********** | |

**核定位证据**: UniProt Cytoplasm + Nucleus + Golgi ECO:0000269. GO **nucleolus IDA:HPA** + **nucleoplasm IDA:HPA** -- strong subnuclear evidence. Calmodulin-lysine N-methyltransferase.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[CAMKMT-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| PREPL | STRING | score=0.976, exp=0 | Textmining only; prolyl endopeptidase-like |
| PPM1B | STRING | score=0.953, exp=0 | Textmining only; protein phosphatase |
| PLOD1 | STRING | score=0.900, exp=0 | Database (0.9); lysyl hydroxylase |
| EHMT2 | STRING | score=0.861, exp=0 | Histone methyltransferase (database 0.65) |
| DOT1L | STRING | score=0.861, exp=0 | Histone methyltransferase (database 0.65) |
| SELENBP1 | IntAct | anti tag coIP | Selenium binding protein |
| H1-5 | IntAct | cross-linking | Histone linker H1 |
| CALM1 | IntAct | anti tag coIP | Calmodulin (substrate) |

**IntAct 数据**: SELENBP1, H1-5, COL1A1, COL1A2, CALM1, SPX 等 (均为 coIP 或 cross-linking)。STRED 连接多基于数据库/文本挖掘 (exp=0)，实验证据薄弱。无 BioGrid 补充数据。UniProt 未记载互作伙伴。

Nucleolus + nucleoplasm IDA:HPA makes this a strong nucleolus candidate.

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CAMKMT/CAMKMT-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 34548933 | Genetic Biomarkers in Association with Depressive Disorder in UAE Residents: A Pilot Case Study. |
| 38949516 | Genome-wide comparative analyses highlight selection signatures underlying saline adaptation in Chil |
| 31886626 | Genome-wide association study of shared liability to anxiety disorders in Army STARRS. |
| 30085123 | ZBTB24 is a transcriptional regulator that coordinates with DNMT3B to control DNA methylation. |
| 27435482 | Effect of polymorphisms in the CAMKMT gene on growth traits in Ujumqin sheep. |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/CAMKMT/CAMKMT-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143919-CAMKMT/subcellular

![](https://images.proteinatlas.org/67912/1250_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/67912/1250_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/67912/1255_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/67912/1255_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/67912/1284_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/67912/1284_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z624 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025800;IPR019410;IPR029063; |
| Pfam | PF10294; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143919-CAMKMT/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
