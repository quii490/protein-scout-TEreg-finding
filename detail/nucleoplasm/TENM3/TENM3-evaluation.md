---
type: protein-evaluation
gene: "TENM3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TENM3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TENM3 |
| 蛋白名称 | Teneurin-3 |
| 蛋白大小 | 2699 aa / 300.9 kDa |
| UniProt ID | Q9P273 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 2699 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=40 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | 6-blade_b-propeller_TolB-like; CarboxyPept-like_regulatory; EGF |
| PPI | 6/10 | x3 | 18.0 | PPI degree=59 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 分析
- Cell Junctions; Cytosol; Nucleoplasm (Approved)
- PubMed strict=40 broad=81
- AF pLDDT=77.4 PDB=0
- InterPro: 6-blade_b-propeller_TolB-like; CarboxyPept-like_regulatory; EGF
- Pfam: EGF_TEN; FN-plug_TEN1-4; GBD_Tenm3
- PPI degree=59 ChIP: None
41250119: GRPR-induced FAM135A expression promote perineural invasion in prostate cancer. | 40410244: Genome-wide association study identified novel loci and gene-environment interac | 38713721: Cartography of teneurin and latrophilin expression reveals spatiotemporal axis h

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Teneurin-3

**功能**: Involved in neural development by regulating the establishment of proper connectivity within the nervous system. Acts in both pre- and postsynaptic neurons in the hippocampus to control the assembly of a precise topographic projection: required in both CA1 and subicular neurons for the precise targeting of proximal CA1 axons to distal subiculum, probably by promoting homophilic cell adhesion. Required for proper dendrite morphogenesis and axon targeting in the vertebrate visual system, thereby p

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011042 |
| InterPro | IPR008969 |
| InterPro | IPR000742 |
| InterPro | IPR057627 |
| InterPro | IPR022385 |
| InterPro | IPR056823 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

TENM3（Teneurin-3，UniProt: Q9P273，2699 aa / 300.9 kDa）的结构域架构分析显示：InterPro结构域包括IPR000742, IPR008969, IPR011042, IPR022385, IPR056823, IPR057627。 AlphaFold预测的pLDDT均值为77.4，整体结构置信度中等，部分区域可能为内在无序区，需要注意其构象柔性对功能的影响。

蛋白质互作网络分析揭示TENM3与以下关键因子存在相互作用：SMAD4、CLU、MME、TRADD、TANK（PPI度为59）。 功能注释显示Involved in neural development by regulating the establishment of proper connectivity within the nervous system. Acts in both pre- and postsynaptic neurons in the hippocampus to control the assembly o。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，TENM3的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，TENM3的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得40篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42315977, 42162855, 41957359等。

综上所述，TENM3作为一个2699 aa / 300.9 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=77.4的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SMAD4 | BioGRID | 1 |
| CLU | BioGRID | 1 |
| MME | BioGRID | 1 |
| TRADD | BioGRID | 1 |
| TANK | BioGRID | 1 |
| TRAF2 | BioGRID | 1 |
| TNIP2 | BioGRID | 1 |
| KIF14 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9P273-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000218336-TENM3

![](https://images.proteinatlas.org/47043/807_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/47043/807_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/47043/742_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/47043/742_E9_3_red_green.jpg)
![](https://images.proteinatlas.org/47043/846_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/47043/846_E2_4_red_green.jpg)
![](https://images.proteinatlas.org/70233/1896_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/70233/1896_A8_3_red_green.jpg)

### PubMed 文献

**PubMed count: 81**

| 42315977 | Expanding the phenotypic and genotypic spectrum of TENM3-related syndromic microphthalmia. | Ophthalmic Genet 2026 |
| 42162855 | Attenuation of postoperative cognitive dysfunction by Mongolian medical warm acupuncture associates with suppressed neur | Exp Neurol 2026 |
| 41957359 | CRISPR activation screens identify oncogenic lncRNAs that are susceptible to CDK4/6 inhibitor treatment. | Nat Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TENM3

