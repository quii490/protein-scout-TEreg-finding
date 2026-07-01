---
type: protein-evaluation
gene: "GSTZ1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GSTZ1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GSTZ1 |
| 蛋白名称 | Maleylacetoacetate isomerase |
| 蛋白大小 | 216 aa / 24.2 kDa |
| UniProt ID | O43708 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 216 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=85 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=97.3; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | Glutathione-S-Trfase_C-like; Glutathione-S-Trfase_C_sf; Glutathione_S-Trfase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=38 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=85 broad=167
- AF pLDDT=97.3 PDB=2
- InterPro: Glutathione-S-Trfase_C-like; Glutathione-S-Trfase_C_sf; Glutathione_S-Trfase
- Pfam: GST_C_3; GST_N_2
- PPI degree=38 ChIP: None
15822171: Glutathione transferases. | 37742772: Clinical physiology and pharmacology of GSTZ1/MAAI. | 39649424: Machine Learning and Experimental Validation Identified Ferroptosis Signature an

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Maleylacetoacetate isomerase

**功能**: Bifunctional enzyme showing minimal glutathione-conjugating activity with ethacrynic acid and 7-chloro-4-nitrobenz-2-oxa-1,3-diazole and maleylacetoacetate isomerase activity. Also has low glutathione peroxidase activity with T-butyl and cumene hydroperoxides. Is able to catalyze the glutathione dependent oxygenation of dichloroacetic acid to glyoxylic acid

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR010987 |
| InterPro | IPR036282 |
| InterPro | IPR040079 |
| InterPro | IPR004045 |
| InterPro | IPR004046 |
| InterPro | IPR005955 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

GSTZ1（Maleylacetoacetate isomerase，UniProt: O43708，216 aa / 24.2 kDa）的结构域架构分析显示：InterPro结构域包括IPR004045, IPR004046, IPR005955, IPR010987, IPR036282, IPR040079。 AlphaFold预测的pLDDT均值为97.3，表明整体结构预测置信度极高，各结构域折叠状态可靠。

蛋白质互作网络分析揭示GSTZ1与以下关键因子存在相互作用：HPGDS、GSTZ1、PPP1CC、BAG3、RCAN2（PPI度为38）。 功能注释显示Bifunctional enzyme showing minimal glutathione-conjugating activity with ethacrynic acid and 7-chloro-4-nitrobenz-2-oxa-1,3-diazole and maleylacetoacetate isomerase activity. Also has low glutathione。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，GSTZ1的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，GSTZ1的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得85篇文献，已有较多文献积累，需从TE调控这一非经典视角寻找差异化研究切入点。 代表性文献包括PMID:42240478, 41908562, 41810912等。

综上所述，GSTZ1作为一个216 aa / 24.2 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=97.3的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HPGDS | STRING | 964 |
| GSTZ1 | BioGRID | 1 |
| PPP1CC | BioGRID | 1 |
| BAG3 | BioGRID | 1 |
| RCAN2 | BioGRID | 1 |
| SOD1 | BioGRID | 1 |
| PRDX6 | BioGRID | 1 |
| RBPMS | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43708-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100577-GSTZ1

![](https://images.proteinatlas.org/4701/6_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/6_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100577-GSTZ1

![](https://images.proteinatlas.org/4701/6_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/6_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100577-GSTZ1

![](https://images.proteinatlas.org/4701/6_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/6_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4701/4_E2_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 167**

| 42240478 | Targeting GSTZ1 Sensitizes KRASG12C-Mutant Lung Cancer Cells by Overcoming Glutathione and Glycolysis Pathway Rewiring. | Cancer Res Commun 2026 |
| 41908562 | Whole-genome characterization and functional-structural analysis of GST variants in Orang Asli with comparative insights | In Silico Pharmacol 2026 |
| 41810912 | Identification and Verification of Mitochondria-Related Diagnostic Markers of Spinal Cord Injury by WGCNA and Machine Le | Behav Neurol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GSTZ1

