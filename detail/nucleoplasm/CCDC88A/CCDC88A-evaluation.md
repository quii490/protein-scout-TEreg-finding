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

**HPA IF 状态**: IF thumbnail only — HPA 暂无 IF 原图，仅获取到 60x60 缩略图，不能作为可靠定位证据。核定位基于 UniProt + GO-CC。

![[CCDC88A-PAE.png]]

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

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC88A/CCDC88A-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 37357876 | The association between the CCDC88A gene polymorphism at rs1437396 and alcohol use disorder, with or |
| 39480488 | Breast cancers that disseminate to bone marrow acquire aggressive phenotypes through CX43-related tu |
| 34190023 | CCDC88A/GIV promotes HBV replication and progeny secretion via enhancing endosomal trafficking and b |
| 35493459 | CCDC88A Post-Transcriptionally Regulates VEGF via miR-101 and Subsequently Regulates Hepatocellular  |
| 37798908 | Refining the phenotypic spectrum of CCDC88A-related PEHO-like syndrome. |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC88A/CCDC88A-PAE.png]]
