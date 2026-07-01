---
type: protein-evaluation
gene: "KIF26A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KIF26A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KIF26A |
| 蛋白名称 | Kinesin-like protein KIF26A |
| 蛋白大小 | 1882 aa / 194.6 kDa |
| UniProt ID | Q9ULI4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Connecting piece; Cytosol; Flagellar centriole; Nu (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1882 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=21 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=47.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | HTH_KIF26A_B_1st; Kinesin-like_fam; Kinesin_motor_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=14 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +1 |

### 3. 分析
- Connecting piece; Cytosol; Flagellar centriole; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=21 broad=30
- AF pLDDT=47.1 PDB=0
- InterPro: HTH_KIF26A_B_1st; Kinesin-like_fam; Kinesin_motor_dom
- Pfam: HTH_KIF26A_B_1st; Kinesin
- PPI degree=14 ChIP: None
37486637: Exome Sequencing and the Identification of New Genes and Shared Mechanisms in Po | 33542431: Genetic background-dependent abnormalities of the enteric nervous system and int | 38866323: Congenital cranial dysinnervation disorder with homozygous KIF26A variant.

### 4. 总体评价
**67.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Kinesin-like protein KIF26A

**功能**: Atypical kinesin that plays a key role in enteric neuron development. Acts by repressing a cell growth signaling pathway in the enteric nervous system development, possibly via its interaction with GRB2 that prevents GRB2-binding to SHC, thereby attenating the GDNF-Ret signaling (By similarity). Binds to microtubules but lacks microtubule-based motility due to the absence of ATPase activity (By similarity). Plays a critical role in cerebral cortical development. It probably acts as a microtubule

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR057090 |
| InterPro | IPR027640 |
| InterPro | IPR001752 |
| InterPro | IPR036961 |
| InterPro | IPR027417 |
| Pfam | PF23081 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：KIF26A（Q9ULI4, Kinesin-like protein KIF26A, 1882 aa / 194.6 kDa）的主要结构域注释为IPR057090, IPR027640, IPR001752, IPR036961。Pfam数据库进一步识别到PF23081等保守域。AlphaFold pLDDT=47.1（中低置信度）——结构预测显示较大无序区域，可能含IDR或需要结合伴侣才能有序折叠。该蛋白暂无实验PDB结构（PDB=0），当前结构信息依赖AlphaFold预测。PubMed=21（低文献量），该蛋白处于早期研究阶段。

**PPI互作网络解读**：PPI network（degree=14）——BioGRID数据库记录的关键互作伙伴包括MAPK10、ARRB1、DPF2、KIAA1429、PPP1CC、TBC1D21。其中DPF2、PPP1CC、CTAG1B等具有染色质调控或转录相关功能——提示KIF26A可能通过PPI平台间接参与核内转录调控网络。

**结构解读**：InterPro注释到5个保守结构域：IPR057090、IPR027640、IPR001752——这些domain signature暗示了该蛋白的功能类别。Pfam域PF23081的保守性进一步验证了该蛋白特定的进化约束。结构预测置信度有限，需实验结构解析确证。

**机制模型**：KIF26A的精确分子机制目前尚待阐明。基于结构域注释（IPR057090、IPR027640、IPR001752）——可推测该蛋白可能参与macromolecular complex assembly或signaling cascade。在核定位context中，该蛋白可能需要与已知nuclear factor形成functional complex才能执行完整生物学功能。

**TE调控展望**：KIF26A的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于：（1）KIF26A与chromatin remodeling complex（SWI/SNF, NuRD, PRC1/2）的physical association；（2）KIF26A能否通过其结构域识别TE-derived element；（3）KIF26A的depletion是否改变LINE-1或ERV family的expression level。建议affinity purification-MS鉴定KIF26A在核内的完整interactome。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAPK10 | BioGRID | 0 |
| ARRB1 | BioGRID | 0 |
| DPF2 | BioGRID | 0 |
| KIAA1429 | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| TBC1D21 | BioGRID | 0 |
| CTAG1B | BioGRID | 0 |
| CTAG1A | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9ULI4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KIF26A

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000066735-KIF26A

![](https://images.proteinatlas.org/46882/2239_B3_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/46882/2239_B3_40_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000066735-KIF26A

![](https://images.proteinatlas.org/46882/2239_B3_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/46882/2239_B3_40_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000066735-KIF26A

![](https://images.proteinatlas.org/46882/2239_B3_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/46882/2239_B3_40_blue_red_green.jpg)

### PubMed

**Count: 30**

| PMID | Title |
|---|---|
| 42239235 | The unconventional kinesin Kif26a is required for the guidance of major axon tracts in the developing mouse brain. |
| 42003912 | Kinesin Family Member 26A Disrupts DNA-Dependent Protein Kinase Complex Formation to Enhance Chemoradiotherapy Sensitivity in Colorectal Cancer. |
| 41360914 | KIF26A regulates the development and function of the main olfactory epithelium in mice. |
| 41246799 | Blood and adipose tissue DNA methylation in adults born preterm with a very low birth weight - a sibling comparison study. |
| 40458763 | Screening of functional genes affecting the quality of translucent eggshell membranes based on RNA-seq analysis and DIA proteomics. |


