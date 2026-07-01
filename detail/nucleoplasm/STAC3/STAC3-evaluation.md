---
type: protein-evaluation
gene: "STAC3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## STAC3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | STAC3 |
| 蛋白名称 | SH3 and cysteine-rich domain-containing protein 3 |
| 蛋白大小 | 364 aa / 41.5 kDa |
| UniProt ID | Q96MF2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 364 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=63 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=69.3; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | C1-like_sf; PKC_DAG/PE; SH3-like_dom_sf |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=76 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Enhanced)
- PubMed strict=63 broad=103
- AF pLDDT=69.3 PDB=5
- InterPro: C1-like_sf; PKC_DAG/PE; SH3-like_dom_sf
- Pfam: C1_1; SH3_1; SH3_2
- PPI degree=76 ChIP: None
33820833: Phenotypic spectrum and genomics of undiagnosed arthrogryposis multiplex congeni | 31219695: STAC3 Disorder. | 33060286: Neurogenetic fetal akinesia and arthrogryposis: genetics, expanding genotype-phe

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 and cysteine-rich domain-containing protein 3

**功能**: Required for normal excitation-contraction coupling in skeletal muscle and for normal muscle contraction in response to membrane depolarization. Required for normal Ca(2+) release from the sarcplasmic reticulum, which ultimately leads to muscle contraction. Probably functions via its effects on muscle calcium channels (PubMed:23736855, PubMed:29078335). Increases CACNA1S channel activity, in addition to its role in enhancing the expression of CACNA1S at the cell membrane. Has a redundant role in

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR046349 |
| InterPro | IPR002219 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| InterPro | IPR039688 |
| InterPro | IPR035736 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

STAC3（SH3 and cysteine-rich domain-containing protein 3，UniProt: Q96MF2，364 aa / 41.5 kDa）的结构域架构分析显示：InterPro结构域包括IPR001452, IPR002219, IPR035736, IPR036028, IPR039688, IPR046349。 AlphaFold预测的pLDDT均值为69.3，整体结构置信度较低，该蛋白可能含有大量内在无序区域或高度柔性片段。

蛋白质互作网络分析揭示STAC3与以下关键因子存在相互作用：CACNA1D、HSPA2、PPARA、STAC3、ZCCHC10（PPI度为76）。 功能注释显示Required for normal excitation-contraction coupling in skeletal muscle and for normal muscle contraction in response to membrane depolarization. Required for normal Ca(2+) release from the sarcplasmic。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，STAC3的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.9/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，STAC3的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得63篇文献，已有较多文献积累，需从TE调控这一非经典视角寻找差异化研究切入点。 代表性文献包括PMID:42189464, 41892369, 41805301等。

综上所述，STAC3作为一个364 aa / 41.5 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=69.3的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CACNA1D | STRING | 810 |
| HSPA2 | STRING | 723 |
| PPARA | BioGRID | 1 |
| STAC3 | BioGRID | 1 |
| ZCCHC10 | BioGRID | 1 |
| JMJD6 | BioGRID | 1 |
| CSNK2A1 | BioGRID | 1 |
| DIP2A | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96MF2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000185482-STAC3

![](https://images.proteinatlas.org/39285/1177_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/39285/1177_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/39285/633_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/39285/633_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/39285/632_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/39285/632_A3_4_red_green.jpg)
![](https://images.proteinatlas.org/39527/1162_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/39527/1162_F11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 103**

| 42189464 | A proposed North American approach for genetic testing of individuals at risk for malignant hyperthermia. | Can J Anaesth 2026 |
| 41892369 | Epigenetics of Genes Displaying High and Preferential Expression in Myoblasts. | Epigenomes 2026 |
| 41805301 | A Proposed North American Approach for Genetic Testing of Individuals at Risk for Malignant Hyperthermia. | Anesthesiology 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STAC3

