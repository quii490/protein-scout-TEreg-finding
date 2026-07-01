---
type: protein-evaluation
gene: "PANK4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PANK4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PANK4 |
| 蛋白名称 | 4'-phosphopantetheine phosphatase |
| 蛋白大小 | 773 aa / 86.0 kDa |
| UniProt ID | Q9NVE7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 773 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARMT-1-like_metal-bd_sf; ARMT1-like_metal-bd; At2g17340_3_helix_bundle |
| PPI | 6/10 | x3 | 18.0 | PPI degree=78 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=8 broad=27
- AF pLDDT=86.9 PDB=0
- InterPro: ARMT-1-like_metal-bd_sf; ARMT1-like_metal-bd; At2g17340_3_helix_bundle
- Pfam: ARMT1-like_dom; Fumble
- PPI degree=78 ChIP: None
30927326: Human pantothenate kinase 4 is a pseudo-pantothenate kinase. | 41640369: A systems biology framework uncovers multi-level genetic regulation of dizziness | 42341992: Precision metabolic therapy for propionic acidemia.

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: 4'-phosphopantetheine phosphatase

**功能**: Phosphatase which shows a preference for 4'-phosphopantetheine and its oxidatively damaged forms (sulfonate or S-sulfonate), providing strong indirect evidence that the phosphatase activity pre-empts damage in the coenzyme A (CoA) pathway (PubMed:27322068). Hydrolyzing excess 4'-phosphopantetheine could constitute a directed overflow mechanism to prevent its oxidation to the S-sulfonate, sulfonate, or other forms (PubMed:27322068). Hydrolyzing 4'-phosphopantetheine sulfonate or S-sulfonate would

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036075 |
| InterPro | IPR002791 |
| InterPro | IPR035073 |
| InterPro | IPR043129 |
| InterPro | IPR015844 |
| InterPro | IPR004567 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

PANK4（4'-phosphopantetheine phosphatase，UniProt: Q9NVE7，773 aa / 86.0 kDa）的结构域架构分析显示：InterPro结构域包括IPR002791, IPR004567, IPR015844, IPR035073, IPR036075, IPR043129。 AlphaFold预测的pLDDT均值为86.9，表明结构预测置信度较高，核心结构域折叠可靠，但部分柔性区域可能存在构象不确定性。

蛋白质互作网络分析揭示PANK4与以下关键因子存在相互作用：PPCS、PTPN6、CDK20、NSUN2、ACTR2（PPI度为78）。 功能注释显示Phosphatase which shows a preference for 4'-phosphopantetheine and its oxidatively damaged forms (sulfonate or S-sulfonate), providing strong indirect evidence that the phosphatase activity pre-empts。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，PANK4的亚细胞定位为，核定位证据尚不充分，需要免疫荧光或亚细胞分级实验进一步验证。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，PANK4的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得8篇文献，文献报道极少，属于低研究密度蛋白，适合作为独立探索方向。 代表性文献包括PMID:42341992, 42212001, 42047666等。

综上所述，PANK4作为一个773 aa / 86.0 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=86.9的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPCS | STRING | 929 |
| PTPN6 | BioGRID | 1 |
| CDK20 | BioGRID | 1 |
| NSUN2 | BioGRID | 1 |
| ACTR2 | BioGRID | 1 |
| BAG1 | BioGRID | 1 |
| EEF2K | BioGRID | 1 |
| OSGEP | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NVE7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000157881-PANK4

![](https://images.proteinatlas.org/11723/1443_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1443_B1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000157881-PANK4

![](https://images.proteinatlas.org/11723/1443_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1443_B1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000157881-PANK4

![](https://images.proteinatlas.org/11723/1443_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1443_B1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11723/1778_A2_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 27**

| 42341992 | Precision metabolic therapy for propionic acidemia. | Biochem Pharmacol 2026 |
| 42212001 | Nuclear accumulation of PANK4 in hippocampal astrocytes aggravates cuproptosis in association with mild cognitive impair | Front Aging Neurosci 2026 |
| 42047666 | PANK4 Regulates YAP to Modulate the Glycolytic Pathway in LEC for Driving LECs-EMT in Early Diabetic Cataract Pathogenes | Invest Ophthalmol Vis Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PANK4

