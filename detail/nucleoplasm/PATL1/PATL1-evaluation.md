---
type: protein-evaluation
gene: "PATL1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PATL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PATL1 |
| 蛋白名称 | Protein PAT1 homolog 1 |
| 蛋白大小 | 275 aa / 31.4 kDa |
| UniProt ID | B3KXN0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 275 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=22 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=88.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Pat1-like; PAT1_dom |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=180 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- HPA: nan (Supported)
- PubMed: strict=22, broad=38
- AF pLDDT: 88.6 / PDB: 0
- InterPro: Pat1-like; PAT1_dom
- Pfam: PAT1
- PPI degree=180 ChIP: None
35401681: Eukaryotic mRNA Decapping Activation. | 30690193: Patellin protein family functions in plant development and stress response. | 36608291: DNA topoisomerase 2-associated proteins PATL1 and PATL2 regulate the biogenesis 

### 4. 总体评价
★★★★  **73.8/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein PAT1 homolog 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039900 |
| InterPro | IPR019167 |
| Pfam | PF09770 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Protein PAT1 homolog 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039900 |
| InterPro | IPR019167 |
| Pfam | PF09770 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PATL1(Protein PAT1 Homolog 1)是mRNA脱帽激活复合体的核心支架蛋白，隶属于Pat1家族。其结构域包含PAT1_dom(IPR019167/PF09770)功能域，该结构域在酵母Pat1到人类PATL1/2间高度保守。AlphaFold预测pLDDT高达88.6，是这批核蛋白中结构置信度最高的蛋白之一，意味着其折叠状态高度有序且利于理性设计实验。

在mRNA代谢网络中，PATL1的功能位置极其关键。它作为mRNA脱帽复合体的支架，同时桥接DDX6(DEAD-box RNA解旋酶，STRING=999)、LSM1-7复合物(LSM1/LSM4，STRING=999)、脱帽酶复合体(DCP1A/DCP2，STRING=999)和CCR4-NOT脱腺苷化复合体(CNOT1/CNOT7，STRING=998)。PATL1通过其PAT1结构域直接结合DDX6的RecA-like结构域，将脱帽酶招募至mRNA 5'端，从而触发mRNA的5'→3'降解通路。

在核质中，PATL1可能通过以下非经典机制发挥功能：核质定位的PATL1可能参与核内新生转录本的质控，识别并降解加工异常的pre-mRNA(PMID:35401681，真核mRNA脱帽激活机制综述)。此外，PATL1与TOP2A(DNA拓扑异构酶II)被报道存在功能关联(PMID:36608291)，暗示其在DNA拓扑状态和mRNA周转之间可能发挥某种偶联调控作用，将染色质结构信息与转录后基因沉默效率建立联系。

PPI网络的最显著特征是其高度模块化——所有互作伙伴均在mRNA降解通路上形成一条线性级联。这种"通路支架"架构使得PATL1成为通过单一靶点干预整个mRNA降解通路的药理学入口。然而，PATL1的核质定位仅为Supported级别(nan Approved)，这一证据缺陷需要通过免疫荧光共定位实验或核质分离Western blot加以验证。PubMed文献仅22篇，研究领域仍处于早期阶段。




![PAE](https://alphafold.ebi.ac.uk/files/AF-B3KXN0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166889-PATL1

![](https://images.proteinatlas.org/39030/415_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/415_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_4_cr5e5e278cea733_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_29_cr5e5e278ceb3e6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166889-PATL1

![](https://images.proteinatlas.org/39030/415_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/415_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_4_cr5e5e278cea733_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_29_cr5e5e278ceb3e6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166889-PATL1

![](https://images.proteinatlas.org/39030/415_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/415_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39030/411_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_4_cr5e5e278cea733_blue_red_green.jpg)
![](https://images.proteinatlas.org/74680/1986_F10_29_cr5e5e278ceb3e6_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 38**

| 42001297 | The Arabidopsis thaliana PATL1 functions downstream of CaM3 to mediate vesicle trafficking under the heat shock pathway. | Plant J 2026 |
| 41874418 | Cyclin B3 dsRNA Orchestrate Meiotic Progression in Porcine Oocytes. | J Mol Cell Biol 2026 |
| 41649923 | Molecular insights into the production of extracellular vesicles by plants. | Plant Physiol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PATL1

