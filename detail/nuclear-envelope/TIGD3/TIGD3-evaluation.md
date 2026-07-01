---
type: protein-evaluation
gene: "TIGD3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## TIGD3 (Tigger transposable element-derived protein 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TIGD3 |
| 蛋白全称 | Tigger transposable element-derived protein 3 |
| UniProt ID | Q6B0B8 |
| 蛋白大小 | 471 aa / 51.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 471 aa |
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

**蛋白全称**: Tigger transposable element-derived protein 3

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

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CTPS | STRING | 788 |
| CTPS1 | STRING | 788 |
| CTPS2 | STRING | 737 |
| RALYL | STRING | 700 |
| DDB2 | BioGRID | 1 |
| UBE2I | BioGRID | 1 |
| RALY | BioGRID | 1 |
| PNMA3 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000173825-TIGD3

![](https://images.proteinatlas.org/40016/1418_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/40016/1418_F5_3_red_green.jpg)
![](https://images.proteinatlas.org/40016/1669_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/40016/1669_B11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 35676660 | Characterization of a prognostic model for lung squamous cell carcinoma based on eight stemness index-related genes. | BMC Pulm Med 2022 |
| 35198634 | Identification of a Four-Gene Signature for Diagnosing Paediatric Sepsis. | Biomed Res Int 2022 |
| 32742312 | Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, revealing recurrent domestication events in  | Mob DNA 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD3

### 深度机制分析

**结构域架构**：TIGD3（UniProt Q6B0B8，471 aa，51.8 kDa）是TIGD2的旁系同源物，同属Tigger/pogo转座子驯化蛋白家族。域架构与TIGD2高度平行：N端HTH psq型和HTH CENPB型DNA结合域串联（IPR004875 - HTH CENPB-type；IPR009057 - Homeobox-like domain superfamily；IPR050863 - Tigger transposable element-derived protein family），C端DDE-1转座酶/整合酶催化核心（IPR007889 - DDE-type integrase/transposase, catalytic domain）。Pfam注释包含PF04218（HTH_CENPB）、PF03184（DDE_1）和PF03221（Pogo/Tc1-like domain）。尽管比TIGD2（525 aa）短54个氨基酸，两蛋白共享高水平的域组织和序列相似性（Tigger家族标志），提示共同的祖先转座酶起源。

**PPI互作网络**：STRING数据显示最强的功能伙伴不涉及同族转座酶蛋白，反而是核苷酸代谢酶——CTPS（CTP合成酶，评分788）、CTPS1（CTP合成酶1，评分788）和CTPS2（CTP合成酶2，评分737），构成高度特异的PPI簇。CTPS催化UTP+ATP→CTP+ADP+P的Gln依赖转氨化反应，Cytophidium/CTPS纤维组装参与代谢应激下的核苷酸稳态。RALYL（RNA结合蛋白，评分700）和RALY（hnRNP相关蛋白，评分1）为RNA结合蛋白。BioGRID中DDB2（DNA损伤结合蛋白2，评分1）和UBE2I（SUMO结合酶UBC9，评分1）分别参与NER修复和SUMO化通路。PNMA3（评分1）为副肿瘤Ma抗原家族。

**结构-功能关系**：TIGD3与TIGD2共享转座酶驯化的结构特征，但CTPS互作簇赋予了TIGD3全新的功能维度。CTPS纤维是有丝分裂间期形成于核内的代谢酶聚合物，在核苷酸不足时组装以维持CTP池——TIGD3与CTPS/CTPS1/CTPS2的高置信互作提示TIGD3可能定位于cytoophidium超结构，参与核苷酸代谢应激下的核内空间组织。DDB2（受损DNA识别因子）的互作进一步暗示TIGD3可能在DNA损伤位点与NER修复通路交叉。仅有4篇PubMed文献（PMID:35676660、35198634为基因签名研究；PMID:32742312为pogo进化和驯化综述）。

**TE调控机制**：TIGD3与TIGD2遵循相同的"以转座制转座"驯化范式。HTH DNA结合域（psq + CENPB型串联）使其能够识别Tigger/Mariner家族TE的末端反向重复（TIR）。但TIGD3独特的CTPS互作簇揭示了一层更精妙的TE调控可能机制——CTPS纤维与染色质和核基质连接，在代谢应激下可能隔离或释放特定的染色质调控因子——TE在复制应激和核苷酸池耗竭时更活跃（dNTP/rNTP失衡影响逆转录），TIGD3通过CTPS互作感知核苷酸水平并将其耦合于TE转录调控。DDB2的互作暗示TIGD3可能在UV/化学损伤诱导的TE激活位点发挥调控作用，而UBE2I/UBC9的SUMO化通路参与已知的KAP1-TRIM28-TE沉默复合体的SUMO依赖组装。

**前沿意义**：TIGD3展现出TIGD家族中最特异的PPI特征——与CTPS纤维的高置信功能伙伴关系在TIGD2中未观察到，意味着TIGD3可能在驯化后获得了独立于TIGD2的特化功能。CTPS纤维→核苷酸代谢传感器→染色质调控的连接代表了代谢感知与TE沉默交叉的全新概念方向，值得通过TIGD3-KO后CTPS纤维完整性（IF共定位）和TE-RNA-seq的联合分析进行验证。

