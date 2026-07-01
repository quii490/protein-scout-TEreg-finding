---
type: protein-evaluation
gene: "TMEM45B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM45B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM45B |
| 蛋白名称 | Transmembrane protein 45B |
| 蛋白大小 | 275 aa / 31.8 kDa |
| UniProt ID | Q96B21 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 275 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=90.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | DUF716; TMEM45 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=46 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=22 broad=25
- AF pLDDT=90.8 PDB=0
- InterPro: DUF716; TMEM45
- Pfam: DUF716
- PPI degree=46 ChIP: None
41451134: Tmem45b modulates itch via endoplasmic reticulum calcium regulation. | 36322717: Tmem45b is essential for inflammation- and tissue injury-induced mechanical pain | 35938871: TMEΜ45B Interacts with Sindbis Virus Nsp1 and Nsp4 and Inhibits Viral Replicatio

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 45B

**功能**: Plays a role in innate immunity (PubMed:35938871). Mechanistically, promotes alphaviruses RNA degradation by interacting with the viral polymerase nsP4 and the mRNA-capping enzyme nsP1 and thereby interfering with the interaction between viral RNA and nsP1 (PubMed:35938871). Essential for inflammation- and tissue injury-induced mechanical pain hypersensitivity (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006904 |
| InterPro | IPR042127 |
| Pfam | PF04819 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NSG1 | BioGRID | 1 |
| LAT | BioGRID | 1 |
| METTL18 | BioGRID | 1 |
| HIST1H1E | BioGRID | 1 |
| VKORC1 | BioGRID | 0 |
| TINAG | BioGRID | 0 |
| UBE2G2 | BioGRID | 0 |
| SYNGR1 | BioGRID | 0 |


### 深度机制分析

TMEM45B属于DUF716/TMEM45跨膜蛋白家族（InterPro: IPR006904; Pfam: PF04819），该家族在真核生物中高度保守，但功能长期不明。最近的研究揭示TMEM45B具有两个显著的功能维度：先天免疫中的抗病毒角色（PMID:35938871）和感觉神经元的瘙痒/疼痛转导（PMID:41451134）。从机制上看，TMEM45B通过与甲病毒（Sindbis virus）非结构蛋白nsP1和nsP4直接互作，干扰病毒RNA与加帽酶nsP1的结合，从而促进病毒RNA降解——这一"胞内固有免疫防御"功能可能发生在其内质网定位中。然而HPA Approved的核质定位（核定位特异性9/10）远偏离其预测的膜蛋白拓扑学，意味着TMEM45B可能在核内也具有独立功能。

TMEM45B的核质定位可能与该蛋白的ER-核膜连续体（ER-nuclear envelope continuum）运输相关。作为预测含跨膜结构域的DUF716家族成员，其AlphaFold pLDDT高达90.8（PDB=0），表明尽管含有TM螺旋，整体折叠高度有序。PPI网络鉴定出HIST1H1E（连接组蛋白H1.4, BioGRID评分1）的互作——H1连接组蛋白是染色质高级结构的核心组织者，通过与核小体连接DNA结合促进30nm染色质纤维的形成。若TMEM45B确实与H1.4发生直接互作，其可能在核质中参与染色质压缩/去压缩的动态调控，尤其在先天免疫应答过程中——已知许多抗病毒基因的表达受染色质结构调控。

此外，TMEM45B与LAT（T细胞活化连接蛋白）、UBE2G2（泛素结合酶E2 G2）和METTL18（甲基转移酶样蛋白18）的互作暗示其跨越多种细胞区室的功能可塑性。在感觉神经元中，TMEM45B通过内质网钙信号调控介导瘙痒和机械性疼痛（PMID:36322717, PMID:42050202），但在核质中，结合其抗病毒活性和与染色质蛋白的互作，更合理的模型是：TMEM45B在ER-核膜界面作为"免疫信号桥梁"，感知胞质病毒RNA后将信号传递至核内，通过调节染色质结构影响抗病毒基因的转录输出。PubMed仅22篇使其仍属高新颖性靶标，其"核质-内质网双重驻留"的机制基础以及其在TE调控中的潜在角色远未阐明。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96B21-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151715-TMEM45B

![](https://images.proteinatlas.org/15474/1905_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/15474/1905_A8_4_red_green.jpg)
![](https://images.proteinatlas.org/15474/1843_B8_31_red_green.jpg)
![](https://images.proteinatlas.org/15474/1843_B8_32_red_green.jpg)
![](https://images.proteinatlas.org/15474/1901_K10_1_red_green.jpg)
![](https://images.proteinatlas.org/15474/1901_K10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 25**

| 42050202 | Transmembrane protein 45b in peripheral sensory neurons selectively mediates IL-31-dependent chemical itch. | J Anesth 2026 |
| 41998230 | Elevated TMEM45B expression promotes liver cancer progression and is associated with MET signaling activation. | Sci Rep 2026 |
| 41959721 | TMEM45 protein family - Ancient residents of the cell endomembrane. | Front Mol Biosci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM45B

