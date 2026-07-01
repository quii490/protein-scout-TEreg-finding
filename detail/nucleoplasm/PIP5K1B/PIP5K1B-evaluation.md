---
type: protein-evaluation
gene: "PIP5K1B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PIP5K1B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PIP5K1B |
| 蛋白名称 | Phosphatidylinositol 4-phosphate 5-kinase type-1 beta |
| 蛋白大小 | 540 aa / 61.0 kDa |
| UniProt ID | O14986 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 540 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=26 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=69.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PInositol-4-P-4/5-kinase_C_sf; PInositol-4-P-4/5-kinase_core; PInositol-4-P-5-ki |
| PPI | 6/10 | x3 | 18.0 | PPI degree=64 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=26 broad=43
- AF pLDDT=69.0 PDB=0
- InterPro: PInositol-4-P-4/5-kinase_C_sf; PInositol-4-P-4/5-kinase_core; PInositol-4-P-5-kinase_N
- Pfam: PIP5K
- PPI degree=64 ChIP: None
24194977: Friedreich's ataxia, frataxin, PIP5K1B: echo of a distant fracas. | 40444664: Renal Dysfunction Induced by Sodium p-Perfluorous Nonenoxybenzenesulfonate in Mi | 23909401: Collaboration of AMPK and PKC to induce phosphorylation of Ser413 on PIP5K1B res

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Phosphatidylinositol 4-phosphate 5-kinase type-1 beta

**功能**: Catalyzes the phosphorylation of phosphatidylinositol 4-phosphate (PtdIns(4)P/PI4P) to form phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2/PIP2), a lipid second messenger that regulates several cellular processes such as signal transduction, vesicle trafficking, actin cytoskeleton dynamics, cell adhesion, and cell motility (By similarity). PtdIns(4,5)P2 can directly act as a second messenger or can be utilized as a precursor to generate other second messengers: inositol 1,4,5-trisphosphate

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027483 |
| InterPro | IPR002498 |
| InterPro | IPR027484 |
| InterPro | IPR023610 |
| Pfam | PF01504 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PI4KA | STRING | 958 |
| PIP5K1C | STRING | 942 |
| PIK3CB | STRING | 933 |
| PIK3C2G | STRING | 923 |
| RHOA | STRING | 921 |
| OCRL | STRING | 921 |
| PIK3R1 | STRING | 919 |
| PTEN | STRING | 917 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O14986-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107242-PIP5K1B

![](https://images.proteinatlas.org/9687/1525_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/9687/1525_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/9687/1399_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/9687/1399_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/9687/101_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/9687/101_G9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 43**

| 42336665 | Differential and compensatory roles for type I phosphatidylinositol-4-phosphate-5-kinase isoforms in retinal function an | J Neurosci 2026 |
| 42311015 | Multi-Omics Analysis of the Dual Role of PIP5K1B in Gastric Adenocarcinoma: Regulation of Myofibroblasts, Remodeling of  | Curr Med Chem 2026 |
| 42181893 | Targeting PIP5K ameliorates hepatic cancer by inhibiting PI3K/AKT and the autophagy mechanism and enhancing ROS-mediated | Front Pharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PIP5K1B


### 深度机制分析

PIP5K1B（Phosphatidylinositol 4-phosphate 5-kinase type-1 beta）是I型PIP5K激酶家族的核心成员，催化磷脂酰肌醇信号的第二信使合成。结构上该蛋白由三个保守结构域模块组成：C端催化核心折叠PInositol-4-P-4/5-kinase_C_sf（IPR027483），中间的PInositol-4-P-4/5-kinase_core（IPR002498）提供底物PtdIns(4)P的识别和磷酸转移活性，N端调节结构域PInositol-4-P-5-kinase_N（IPR027484）负责亚细胞靶向和蛋白互作。Pfam单一注释为PIP5K（PF01504），覆盖了完整的催化模块。AlphaFold预测总体置信度为pLDDT=69.0，其中催化核心区段可能折叠较好，而N端和连接区段含有大量柔性环（loop），导致全局pLDDT被稀释。无PDB实验结构（PDB=0），但同家族成员PIP5K1A和PIP5K1C的晶体结构可用作同源建模基准。

PIP5K1B催化的核心生化反应是：PtdIns(4)P（PI4P）+ ATP → PtdIns(4,5)P2（PIP2）+ ADP。PIP2是最重要的脂质第二信使之一，可直接作用于多种效应蛋白的PH结构域和碱性残基簇，或经PI-PLC水解生成IP3（内质网钙释放）和DAG（PKC激活）。PPI互作网络（degree=64）以STRING高置信度伙伴为主，包括PI4KA（score=958, PI4P合成上游酶）、PIP5K1C（score=942, I型PIP5K的另一个同工型）、PIK3CB（score=933, PI3K催化亚基）、RHOA（score=921, 小GTP酶）、PTEN（score=917, PIP3磷酸酶）和OCRL（score=921, PIP2 5-磷酸酶）。这个互作网络揭示了PIP5K1B在磷酸肌醇代谢循环中的枢纽位置——它既是PIP2合成的最后一步酶，又通过RHOA和OCRL的互作参与PIP2周转的动态调控。

功能层面，PIP5K1B通过PIP2的时空特异性合成调节多个关键细胞过程：囊泡运输（PIP2招募AP2/网格蛋白至质膜）、肌动蛋白细胞骨架重塑（PIP2激活WASP/ARP2/3路径）、细胞黏附和迁移（PIP2调控整合素信号）、以及信号转导（PIP2作为PLC/IP3/DAG前体）。UniProt详细记载了PIP2既可以"直接作为第二信使"，又可以"作为前体生成其他第二信使：肌醇1,4,5-三磷酸（IP3）和二酰甘油（DAG）"。

核定位方面，PIP5K1B在HPA中显示Nucleoplasm和Vesicles（Approved），确认了该脂质激酶存在功能性核库（nuclear pool）。核内PIP2在多种核事件中发挥作用——包括RNA聚合酶II转录调控、pre-mRNA剪接、染色质重塑和核小体组装。PIP5K1B的核定位信号可能由N端调控结构域介导。但需要注意的是，PIP5K1B的主要功能定位仍在质膜和胞质内膜系统，核内功能是其一类较为次要的兼职活动。综合来看，PIP5K1B的深度机制模型为：N端靶向+C端催化折叠→PtdIns(4)P磷酸化→PIP2第二信使合成→下游效应蛋白招募（PH结构域结合PIP2）→囊泡运输/细胞骨架/信号转导/核内转录调控。该蛋白通过核内PIP2库间接参与转录调控，但其直接参与TE特异性调控的证据不足（TE调控评估：极低）。



