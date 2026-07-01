---
type: protein-evaluation
gene: "SMIM24"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SMIM24 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMIM24 |
| 蛋白名称 | Small integral membrane protein 24 |
| 蛋白大小 | 130 aa / 15.0 kDa |
| UniProt ID | O75264 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 130 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=65.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PDZK1IP1/SMIM24 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=6 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=8 broad=11
- AF pLDDT=65.4 PDB=0
- InterPro: PDZK1IP1/SMIM24
- Pfam: MAP17
- PPI degree=6 ChIP: None
38488671: RETRACTED: Exploring the tumor microenvironment: Chemokine-related genes and imm | 37438770: Longitudinal APOE4- and amyloid-dependent changes in the blood transcriptome in  | 41003765: Big data analysis reveals miR-874 as a suppressor and therapeutic target in the 

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 24

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031627 |
| Pfam | PF15807 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 24

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031627 |
| Pfam | PF15807 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPS6 | BioGRID | 1 |
| SLC22A1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O75264-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000095932-SMIM24

![](https://images.proteinatlas.org/56027/1041_G1_3_red_green.jpg)
![](https://images.proteinatlas.org/56027/1041_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/56027/1144_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/56027/1144_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/56027/996_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/56027/996_G1_4_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 42306095 | Genetic analysis of three familial cases of pure terminal 19p13.3 duplication caused by maternal balanced translocation  | Front Genet 2026 |
| 41971124 | A multi-omics prognostic model and functional validation of HPGD in clear cell renal cell carcinoma. | Transl Androl Urol 2026 |
| 41003765 | Big data analysis reveals miR-874 as a suppressor and therapeutic target in the progression from endometriosis to ovaria | Discov Oncol 2025 |

### 深度机制分析

SMIM24（130 aa, 15.0 kDa）是一个小整合膜蛋白，属于PDZK1IP1/SMIM24家族（IPR031627, MAP17/PF15807）。该家族的特征性折叠是一个约100个氨基酸的疏水核心区域，形成单个跨膜α-螺旋，两侧有短小的胞外和胞内尾部。因蛋白极小且结构预测有限，AlphaFold预测pLDDT仅65.4——跨膜螺旋区域预测置信度可接受，但侧翼尾部基本无折叠。无PDB实验结构。

SMIM24的已知分子功能几乎空白——UniProt甚至未提供功能注释，这在该蛋白家族中并不罕见，因SMIM（小整合膜蛋白）是基因组中定义最不充分的功能类群之一。MAP17（PDZK1IP1）是SMIM24的同源蛋白，已知通过结合PDZK1的PDZ结构域参与膜蛋白运输和信号复合物的组织。SMIM24可能以类似机制作为支架蛋白。

PPI网络（BioGRID degree=6）中关键互作是与RPS6（核糖体蛋白S6，BioGRID评分=1）的结合。RPS6是40S核糖体亚基的组分，位于mRNA通道的出口附近，其磷酸化状态调控翻译起始和延伸。SMIM24-RPS6互作提示这个小型膜蛋白可能通过调控核糖体功能来间接影响蛋白合成——可能作为内质网膜-核糖体互作的调节因子。与SLC22A1（有机阳离子转运蛋白）的互作则指示了跨膜运输功能。

HPA定位为Cytosol; Nucleoplasm（Approved级别），核质定位对于典型的跨膜蛋白而言是非典型的。小型整合膜蛋白在合成后通常通过Sec61转位子插入内质网膜，SMIM24的核质信号可能反映新合成蛋白在靶向细胞膜之前的ER-核膜连续体中的瞬时定位，也可能是真正的功能性核内驻留。

在TE调控方面，SMIM24的有限功能注释使得机制推论需谨慎。最合理的假说是通过RPS6互作间接参与翻译调控——RPS6磷酸化是mTORC1通路的核心输出之一，该通路调控TOP（5'末端寡聚嘧啶）mRNA和某些TE来源mRNA的翻译效率。若SMIM24调控RPS6在核糖体上的有效利用，它可能影响特定类别mRNA（包括TE来源转录本）的翻译偏好性。文献稀缺（PubMed=8）和蛋白较小的特性限制了其作为直接TE调控靶点的可能性，但其在肿瘤微环境相关基因分析中的出现（PMID:38488671）提示其表达可能在疾病状态中发生改变。建议通过polysome profiling检测SMIM24过表达/敲低对TE来源mRNA翻译效率的影响。

