---
type: protein-evaluation
gene: "TIGD2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## TIGD2 (Tigger transposable element-derived protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TIGD2 |
| 蛋白全称 | Tigger transposable element-derived protein 2 |
| UniProt ID | Q4W5G0 |
| 蛋白大小 | 525 aa / 57.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 525 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR050863; InterPro:IPR004875; InterPro:IPR009057; InterPro:IPR006600; InterPro:IPR007889; Pfam:PF04218 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |
| InterPro | IPR007889 |
| Pfam | PF04218 |
| Pfam | PF03184 |
| Pfam | PF03221 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Tigger transposable element-derived protein 2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |
| InterPro | IPR007889 |
| Pfam | PF04218 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000180346-TIGD2

![](https://images.proteinatlas.org/71168/1547_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71168/1547_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71168/1382_A4_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/71168/1382_A4_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/71168/1419_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71168/1419_A4_3_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00674; |
| InterPro | IPR050863;IPR004875;IPR009057;IPR006600;IPR007889; |
| Pfam | PF04218;PF03184;PF03221; |
| UniProt Domain | DOMAIN 1..52; /note="HTH psq-type"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00320"; DOMAIN 67..139; /note="HTH CENPB-type"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00583"; DOMAIN 168..385; /note="DDE-1"; /evidence="ECO:0000255" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| JRKL | BioGRID | 1 |
| CSK | BioGRID | 0 |
| HIST1H4A | BioGRID | 0 |
| PARK2 | BioGRID | 0 |


### PubMed 文献

**PubMed count: 3**

| 39643897 | Examination of homozygosity runs and selection signatures in native goat breeds of Henan, China. | BMC Genomics 2024 |
| 32887549 | Signatures of selection reveal candidate genes involved in economic traits and cold acclimation in five Swedish cattle b | Genet Sel Evol 2020 |
| 32742312 | Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, revealing recurrent domestication events in  | Mob DNA 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD2

### 深度机制分析

**结构域架构**：TIGD2（UniProt Q4W5G0，525 aa）源自Tigger转座子超家族的IS630-Tc1-mariner类群，经驯化后固定于脊椎动物基因组。其N端携带HTH psq型DNA结合域（1-52 aa，PROSITE:PRU00320）和HTH CENPB型DNA结合域（67-139 aa，PROSITE:PRU00583），这两个螺旋-转角-螺旋（helix-turn-helix）结构域源于转座酶DNA结合模块的驯化。C端区域（168-385 aa）包含DDE-1催化核心域，属于典型的DDE转座酶/整合酶超家族（InterPro:IPR004875, IPR007889），此外Pfam注释还有PF04218（HTH_CENPB）、PF03184（DDE_1）和PF03221（Pogo/Tc1-like domain）。该多域架构明确保留了祖先转座酶的完整结构蓝图——DNA结合域与催化域串联排列，与活跃转座酶的域组织高度一致。

**PPI互作网络**：TIGD2的PPI数据极为有限。BioGRID记录JRKL的互作评分仅为1，CSK、HIST1H4A和PARK2的评分均为0。HIST1H4A（核心组蛋白H4）的低置信互作若可验证，则暗示TIGD2可能具有识别核小体/染色质底物的能力——这与其HTH型DNA结合域的预测功能一致。但目前PPI网络的不完整性使得任何机制推断均需高度谨慎。

**结构-功能关系**：TIGD2代表转座酶驯化（domestication）的经典案例——祖先转座子的DNA切割和整合功能被解除，而保留DNA结合能力以满足宿主新功能需求。HTH psq型和CENPB型串联DNA结合域的共存提示其可识别特定DNA序列基序，而DDE-1域可能已失去催化活性或进化为别构调控域。该蛋白评分在3篇PubMed文献中均为群体遗传学/选择信号分析，缺乏分子功能验证——TrEMBL状态进一步佐证其功能注释的空白状态。

**TE调控机制**：TIGD2来源于转座子但已被宿主驯化，其在TE调控中的潜在角色遵循"以转座制转座"（fighting fire with fire）的经典范式。驯化的转座酶蛋白常被招募为TE转录的抑制因子——例如KRAB-ZFP蛋白家族中的许多成员通过锌指域识别TE序列并招募KAP1/TRIM28进行表观遗传沉默。TIGD2的HTH DNA结合域可能使其能够结合特定TE家族（特别是Tigger/Mariner类群）的末端反向重复（TIR）序列，形成物理屏障以阻止转座酶接近或招募染色质修饰复合体。

**前沿意义**：TIGD2的研究新颖性极高（PubMed严格命中为0），但其转座子驯化蛋白的身份赋予其独特的TE调控研究价值。DDE-1催化域的活性状态是决定其功能方向的关键——若DDE-1域保有残余核酸酶活性，TIGD2可能通过"切割但不整合"的机制破坏TE插入中间体；若已失活，则可能作为TE转录的竞争性抑制因子发挥作用。TIGD2与KRAB-ZFP/TRIM28通路的潜在功能连接是后续验证的关键方向（PMID: 32742312 - pogo超家族进化与驯化事件综述）。

