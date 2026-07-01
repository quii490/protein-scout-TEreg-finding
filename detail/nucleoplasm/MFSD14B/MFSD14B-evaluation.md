---
type: protein-evaluation
gene: "MFSD14B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MFSD14B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MFSD14B |
| 蛋白名称 | Solute carrier family 71 member 2 |
| 蛋白大小 | 506 aa / 54.5 kDa |
| UniProt ID | Q5SR56 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 506 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=1 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MFS; MFS_dom; MFS_trans_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=1 broad=3
- AF pLDDT=76.8 PDB=0
- InterPro: MFS; MFS_dom; MFS_trans_sf
- Pfam: MFS_1
- PPI degree=0 ChIP: None
28179877: Putative Membrane-Bound Transporters MFSD14A and MFSD14B Are Neuronal and Affect

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Solute carrier family 71 member 2

**功能**: Probable membrane-bound transporter. May play a role in neuronal nutrient sensing and energy homeostasis

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011701 |
| InterPro | IPR020846 |
| InterPro | IPR036259 |
| InterPro | IPR005829 |
| InterPro | IPR001958 |
| Pfam | PF07690 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

MFSD14B属于主要促进超家族（Major Facilitator Superfamily, MFS），其InterPro结构域注释包括MFS（IPR011701）、MFS_dom（IPR020846）和MFS_trans_sf（IPR036259），Pfam注释为MFS_1（PF07690）。MFS超家族是自然界最大的次级转运蛋白家族之一，其典型折叠由12个跨膜螺旋组成两个对称的6-螺旋束，通过交替访问机制（alternating access）实现底物跨膜转运。然而，MFSD14B的HPA免疫荧光定位显示其在核质（Nucleoplasm）和胞质溶胶（Cytosol）中均被检测到，这一观察对经典的膜转运蛋白定位范式提出了挑战——一个典型的MFS转运蛋白如何定位于核质？

AlphaFold预测的pLDDT值为76.8，提示蛋白整体折叠可信但存在显著无序区域。结合其506个氨基酸（54.5 kDa）的较大分子量，该蛋白可能含有超出MFS结构域的额外调控区域。PPI网络分析揭示了以STRING评分驱动的同家族互作网络：MFSD5（784）、SLC35A3（614）、MFSD6（564）、SLC37A3（484）、MFSD6L（482）和MFSD12（482）均为高置信度互作伙伴。这种MFS家族内部的成簇互作模式提示MFSD14B可能与其他MFS成员形成转运复合体或调控网络，而非独立发挥转运功能。

从机制角度，MFSD14B的核质定位可能与神经元营养感知功能相关。PMID 28179877（Front Mol Neurosci, 2017）证实MFSD14A和MFSD14B是神经元蛋白并受营养可用性影响，提示其在能量稳态中的角色。考虑到细胞核是代谢传感信号整合的关键场所（如SIRT1、AMPK信号通路在核内调控转录），MFSD14B在核质的定位可能代表一种非经典的代谢物传感机制——该蛋白可能作为代谢物转运体将特定小分子底物递送至核内，或作为核膜上的营养传感器来调控基因表达。

MFSD14B的研究新颖性极高（PubMed strict=1），仅有3篇文献涉及，且仅1篇直接研究该基因功能。这一极端的新颖性既是优势（无竞争）也是风险（缺乏功能验证基础）。若其核质定位的代谢传感假说成立，MFSD14B可能成为连接细胞代谢状态与核内转录调控的新型分子桥梁。验证实验可围绕：（1）鉴定其转运底物（代谢组学筛选）；（2）确定核定位信号（NLS）或核定位机制；（3）解析其在营养剥夺条件下的核质穿梭动力学展开。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5SR56-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000148110-MFSD14B

![](https://images.proteinatlas.org/17978/173_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/17978/173_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/17978/140_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/17978/140_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/17978/168_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/17978/168_D9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 31552087 | Machine Learning Classifiers for Endometriosis Using Transcriptomics and Methylomics Data. | Front Genet 2019 |
| 28179877 | Putative Membrane-Bound Transporters MFSD14A and MFSD14B Are Neuronal and Affected by Nutrient Availability. | Front Mol Neurosci 2017 |
| 27723779 | Genome-Wide Interaction Analyses between Genetic Variants and Alcohol Consumption and Smoking for Risk of Colorectal Can | PLoS Genet 2016 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MFSD14B

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MFSD13A | STRING | 444 |
| MFSD9 | STRING | 443 |
| MFSD3 | STRING | 421 |
| SLC37A3 | STRING | 484 |
| MFSD6L | STRING | 482 |
| MFSD10 | STRING | 425 |
| LRRC71 | STRING | 462 |
| MFSD12 | STRING | 482 |
| SPNS3 | STRING | 415 |
| SLC35A3 | STRING | 614 |
| MFSD14B | STRING | 438 |
| MFSD6 | STRING | 564 |
| MFSD5 | STRING | 784 |
