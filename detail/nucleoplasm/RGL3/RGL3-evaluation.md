---
type: protein-evaluation
gene: "RGL3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RGL3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RGL3 |
| 蛋白名称 | Ral guanine nucleotide dissociation stimulator-like 3 |
| 蛋白大小 | 710 aa / 78.1 kDa |
| UniProt ID | Q3MIN7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 710 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=42 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=72.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | RA_dom; Ras-like_GEF; Ras-like_Gua-exchang_fac_N |
| PPI | 6/10 | x3 | 18.0 | PPI degree=51 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=42 broad=66
- AF pLDDT=72.0 PDB=0
- InterPro: RA_dom; Ras-like_GEF; Ras-like_Gua-exchang_fac_N
- Pfam: RA; RasGEF; RasGEF_N
- PPI degree=51 ChIP: None
10869344: A novel RalGEF-like protein, RGL3, as a candidate effector for rit and Ras. | 33793917: The gibberellin signaling negative regulator RGA-LIKE3 promotes seed storage pro | 17382517: Identification of Rgl3 as a potential binding partner for Rap-family small G-pro

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ral guanine nucleotide dissociation stimulator-like 3

**功能**: Guanine nucleotide exchange factor (GEF) for Ral-A. Potential effector of GTPase HRas and Ras-related protein M-Ras. Negatively regulates Elk-1-dependent gene induction downstream of HRas and MEKK1 (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000159 |
| InterPro | IPR008937 |
| InterPro | IPR000651 |
| InterPro | IPR019804 |
| InterPro | IPR023578 |
| InterPro | IPR001895 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

RGL3（Ral guanine nucleotide dissociation stimulator-like 3，UniProt: Q3MIN7，710 aa / 78.1 kDa）的结构域架构分析显示：InterPro结构域包括IPR000159, IPR000651, IPR001895, IPR008937, IPR019804, IPR023578。 AlphaFold预测的pLDDT均值为72.0，整体结构置信度中等，部分区域可能为内在无序区，需要注意其构象柔性对功能的影响。

蛋白质互作网络分析揭示RGL3与以下关键因子存在相互作用：HRAS、CHCHD3、NFKBIB、SIRT6、DCTN3（PPI度为51）。 功能注释显示Guanine nucleotide exchange factor (GEF) for Ral-A. Potential effector of GTPase HRas and Ras-related protein M-Ras. Negatively regulates Elk-1-dependent gene induction downstream of HRas and MEKK1 (B。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，RGL3的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，RGL3的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得42篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42274237, 42037589, 41699318等。

综上所述，RGL3作为一个710 aa / 78.1 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=72.0的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HRAS | STRING | 732 |
| CHCHD3 | BioGRID | 1 |
| NFKBIB | BioGRID | 1 |
| SIRT6 | BioGRID | 1 |
| DCTN3 | BioGRID | 1 |
| YPEL3 | BioGRID | 1 |
| HES6 | BioGRID | 1 |
| TFPT | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q3MIN7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000205517-RGL3

![](https://images.proteinatlas.org/64578/1258_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/64578/1258_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/64578/1392_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/64578/1392_B2_3_red_green.jpg)
![](https://images.proteinatlas.org/64578/1249_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/64578/1249_D5_4_red_green.jpg)

### PubMed 文献

**PubMed count: 66**

| 42274237 | Cytokinin regulates flowering time in Arabidopsis thaliana through the gibberellin pathway. | J Exp Bot 2026 |
| 42037589 | ARF6 integrates auxin and gibberellin signaling to promote stone cell lignification in pear via the HB49-MYB169 module. | New Phytol 2026 |
| 41699318 | Distinct radial glia subtypes regulate midbrain dopaminergic neuron development. | Nat Neurosci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RGL3

