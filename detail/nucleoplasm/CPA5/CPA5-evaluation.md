---
type: protein-evaluation
gene: "CPA5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## CPA5 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CPA5 |
| 蛋白名称 | Carboxypeptidase A5 |
| 蛋白大小 | 436 aa / 49.0 kDa |
| UniProt ID | Q8WXQ8 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 436 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=16 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=92.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CARBOXYPEPT_ZN_1; CARBOXYPEPT_ZN_2; CPA_M14_CPD |
| PPI | 5/10 | x3 | 15.0 | PPI degree=21 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |
### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=16, broad=31
- AF pLDDT: 92.0 / PDB: 0
- InterPro: CARBOXYPEPT_ZN_1; CARBOXYPEPT_ZN_2; CPA_M14_CPD
- Pfam: Peptidase_M14; Propep_M14
- PPI degree=21 / ChIP: None
12801587: Neuropeptide-processing carboxypeptidases. | 37921454: Alteriqipengyuania flavescens sp. nov., isolated from Pearl River Estuary sedime | 33745502: Predicted gene 31453 (Gm31453) and the gene encoding carboxypeptidase A5 (Cpa5) 
### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Carboxypeptidase A5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR057246 |
| InterPro | IPR057247 |
| InterPro | IPR034248 |
| InterPro | IPR036990 |
| InterPro | IPR003146 |
| InterPro | IPR000834 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TP53 | BioGRID | 1 |
| POTEE | BioGRID | 1 |
| FOXF1 | BioGRID | 1 |
| EPHA4 | BioGRID | 0 |
| KIRREL | BioGRID | 0 |
| MPZL1 | BioGRID | 0 |
| HSPA5 | BioGRID | 0 |
| CANX | BioGRID | 0 |


### 深度机制分析

CPA5属于M14金属羧肽酶家族（InterPro: CARBOXYPEPT_ZN_1/2, CPA_M14_CPD; Pfam: Peptidase_M14, Propep_M14），该家族成员通常定位于分泌途径或胞外空间，负责神经肽和激素的C端加工（PMID:12801587）。CPA5的核质定位（HPA Approved, 核定位特异性9/10）与经典羧肽酶的亚细胞定位存在显著偏差，提示其可能具有非经典的核内功能。AlphaFold预测结构质量较高（pLDDT=92.0），但缺乏实验结构（PDB=0），其N端Propep_M14结构域可能作为分子内调节模块控制酶活性，而C端Peptidase_M14催化域中的锌离子结合位点在核内环境下是否保持催化活性仍待阐明。

从蛋白互作网络来看，CPA5与TP53（BioGRID评分1）的互作尤其值得关注——TP53作为核内核心转录因子和基因组守护者，CPA5可能通过去羧基化修饰调控TP53或TP53靶蛋白的活性。此外，CPA5与内质网分子伴侣HSPA5和CANX的互作暗示其可能在核膜附近参与蛋白质质量控制，尽管这些互作评分较低（score=0）。PPI度仅为21，表明CPA5并非广泛互作的中心节点，而更可能发挥底物特异的精细调控功能。

考虑到M14羧肽酶的结构保守性（pLDDT=92.0表明折叠良好）和底物口袋的序列特异性，CPA5在核质中可能靶向含特定C端残基的核蛋白进行加工，从而影响转录调控、DNA损伤应答（通过TP53途径）或染色质重塑过程。目前PubMed文献仅16篇，且无ChIP数据，该蛋白的核内底物、催化机制及其调控TE元件的潜力仍为完全空白领域，亟需通过底物组学（degradomics）和功能获得/缺失实验进行系统性解析。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8WXQ8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158525-CPA5

![](https://images.proteinatlas.org/20322/1375_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/20322/1375_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/20322/1413_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/20322/1413_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/20322/1384_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/20322/1384_A3_4_red_green.jpg)

### PubMed 文献

**PubMed count: 31**

| 42081108 | Dissecting shared genetic architecture between pan-cancer and aging-related traits: a genome-wide cross-trait analysis. | Biogerontology 2026 |
| 41771430 | Expression and function of zebrafish carboxypeptidase A5 in neutrophils and mast cells. | Fish Shellfish Immunol 2026 |
| 41560696 | A bi-functional pH-responsive chip with a soft hydrogel-supported 3D-like renal tumor model for sustained drug delivery. | Soft Matter 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CPA5

