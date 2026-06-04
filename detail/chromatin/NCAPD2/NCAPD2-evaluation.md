---
type: protein-evaluation
gene: "NCAPD2"
date: 2026-06-01
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## NCAPD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NCAPD2 / CAPD2, CNAP1, KIAA0159 |
| 蛋白全名 | Condensin complex subunit 1 |
| 蛋白大小 | 1401 aa / 157.2 kDa |
| UniProt ID | Q15021 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | UniProt: Nucleus/Chromosome (ECO:0000269); HPA Nucleoplasm main; condensin complex IDA |
| 蛋白大小 | 4/10 | x1 | 4.0 | 1401 aa, 157 kDa -- large condensin subunit |
| 研究新颖性 | 8/10 | x5 | 40.0 | Strict=25 |
| 三维结构 | 6/10 | x3 | 18.0 | AlphaFold pLDDT 79.6; 无 PDB 实验结构 |
| 调控结构域 | 6/10 | x2 | 12.0 | Condensin-specific Cnd1 domain; Armadillo-type fold |
| PPI 网络 | 7/10 | x3 | 21.0 | Condensin I complex (SMC2/SMC4/NCAPG/NCAPH) 均 0.999 |
| **加权总分** | | | **127/180********** | |
| 互证加分 | | | +2.0 | UniProt+HPA 一致: Nucleoplasm/Chromosome |
| **归一化总分 (÷1.83)** | | | **69.4/100********** | |

PubMed strict: 25

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269); Cytoplasm (ECO:0000269); Chromosome (ECO:0000269) | Experimental |
| GO-CC | condensin complex IDA:UniProtKB; condensed nuclear chromosome ISO; nucleoplasm IDA:HPA | Direct assay |
| HPA (IF) | Nucleoplasm (main), Cytosol (main), Nucleoli/centriolar satellite (additional); Reliability: Supported | IF available |

**HPA IF 状态**: IF available -- HPA Supported。主定位 Nucleoplasm + Cytosol。condensin I 复合体在有丝分裂期定位于 condensed chromosome，间期分布于核质。IF 图像已下载。

![[NCAPD2-PAE.png]]

**PAE 状态**: 已获取 PAE 图像。AlphaFold pLDDT 79.6 (mean), 40.9% >90, 13.6% <50。1401 aa 大蛋白存在较多无序区域，折叠域（Armadillo/HEAT repeats）预测良好。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| SMC2 | STRING | 0.999 (experimental 0.993) |
| SMC4 | STRING | 0.999 (experimental 0.993) |
| NCAPG | STRING + UniProt | 0.999 (experimental 0.978) |
| NCAPH | STRING + UniProt | 0.999 (experimental 0.992) |
| NCAPG2 | STRING | 0.988 (database/textmining) |
| NCAPD3 | STRING | 0.984 (database) |
| AURKB | STRING | 0.792 (experimental 0.194) |
| CDK1 | STRING | 0.789 (experimental 0.292) |

**核心发现**: NCAPD2 是 condensin I 复合体的 scaffold 亚基，PPI 网络以 condensin 复合体成员 (SMC2/SMC4/NCAPG/NCAPH) 为主，均为 0.999 最高置信度。AURKB/CDK1 为已知的 condensin 调控激酶。

IntAct 15 条记录（含 CSNK2A1 磷酸化实验、ESR1/RRP1B co-IP 等）。UniProt 记录 NCAPG/NCAPH 两个互作 partner。

### 5. 结构域与染色质调控潜力
| 来源 | 结构域 |
|---|---|
| InterPro | IPR026971 (Cnd1), IPR032682 (Cnd1 N-term), IPR007673 (Cnd1/Pcs1), IPR011989 (Armadillo-like helical), IPR016024 (Armadillo-type fold) |
| Pfam | PF12717 (Cnd1), PF12922 (Cnd1 N-terminal) |

NCAPD2 作为 condensin I scaffold，通过 Armadillo/HEAT repeat 折叠介导蛋白-蛋白互作，组装 SMC2/SMC4 异二聚体形成 condensin I 全酶。具有 ATP-dependent DNA supercoiling 和 chromosome compaction 功能。染色质调控潜力的直接性极高（condensin 本身就是染色质结构调控因子），但需注意其功能主要在有丝分裂期而非间期基因表达调控。

### 6. 总体评价
NCAPD2 是 condensin I 复合体的核心 scaffold 亚基，具有明确的染色质/染色体定位（condensed chromosome + nucleoplasm）。PPI 网络以 condensin 复合体为主，置信度极高。优势在于极端染色质特异性和 condensin 生物学重要性，劣势在于蛋白过大 (1401 aa) 和缺乏间期转录调控证据。作为低研究新颖性染色质结构蛋白靶点评分良好。

**推荐等级**: 3/5

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/NCAPD2/IF_images/NCAPD2_IF_638_E4_2_blue_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


![[Projects/TEreg-finding/protein-interested/detail/chromatin/NCAPD2/NCAPD2-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 41319185 | NCAPD2 promotes the progression of lung adenocarcinoma through an AKT/MDM2/E2F1 positive feedback lo |
| 36701707 | NCAPD2 is a novel marker for the poor prognosis of lung adenocarcinoma and is associated with immune |
| 37498296 | Non-SMC condensin I complex subunit D2 (NCAPD2) reveals its prognostic and immunologic features in h |
| 40245749 | Impact of Non-SMC Condensin I Complex Subunit D2 Upregulation on Oral Squamous Cell Carcinoma Progno |
| 39092569 | NCAPD2 augments the tumorigenesis and progression of human liver cancer via the PI3K‑Akt‑mTOR signal |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/NCAPD2/NCAPD2-PAE.png]]
