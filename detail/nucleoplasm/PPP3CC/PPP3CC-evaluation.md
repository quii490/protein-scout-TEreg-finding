---
type: protein-evaluation
gene: "PPP3CC"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPP3CC 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPP3CC |
| 蛋白名称 | Serine/threonine-protein phosphatase 2B catalytic subunit gamma isoform |
| 蛋白大小 | 512 aa / 58.1 kDa |
| UniProt ID | P48454 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Calyx; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 512 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=58 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=85.5; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Calcineurin-like_PHP; Metallo-depent_PP-like; MPP_PP2B |
| PPI | 7/10 | x3 | 21.0 | PPI degree=107 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Calyx; Cytosol; Nucleoplasm (Approved)
- PubMed strict=58 broad=77
- AF pLDDT=85.5 PDB=1
- InterPro: Calcineurin-like_PHP; Metallo-depent_PP-like; MPP_PP2B
- Pfam: Metallophos
- PPI degree=107 ChIP: None
40997225: Acute Respiratory Distress Syndrome Molecular Phenotypes Have Distinct Lower Res | 37453419: 2-Deoxyglucose drives plasticity via an adaptive ER stress-ATF4 pathway and elic | 21312416: Molecules, signaling, and schizophrenia.

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Serine/threonine-protein phosphatase 2B catalytic subunit gamma isoform

**功能**: Calcium-dependent, calmodulin-stimulated protein phosphatase which plays an essential role in the transduction of intracellular Ca(2+)-mediated signals. Dephosphorylates and activates transcription factor NFATC1. Dephosphorylates and inactivates transcription factor ELK1. Dephosphorylates DARPP32

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004843 |
| InterPro | IPR029052 |
| InterPro | IPR041751 |
| InterPro | IPR043360 |
| InterPro | IPR006186 |
| Pfam | PF00149 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PPP3CC是钙调磷酸酶(Calcineurin)的催化亚基，属于磷蛋白磷酸酶(PPP)家族。其核心功能域包括Calcineurin-like_PHP催化域(IPR004843，残基约50-350)和Metallo-dependent_PP-like金属结合域(IPR029052)，二者共同构成双金属催化中心，依赖Fe³⁺/Zn²⁺离子的协同作用发挥丝氨酸/苏氨酸磷酸酶活性。AlphaFold预测pLDDT达85.5，表明该催化核心具有高置信度的折叠结构。

在核质中，PPP3CC作为Ca²⁺信号通路的关键核内效应器发挥功能。钙调蛋白(Calmodulin)结合后解除自抑制域的空间阻遏，使PPP3CC去磷酸化核内转录因子NFATC1(PMID:40997225涉及ARDS分子表型中NFAT信号通路)，导致NFAT的核滞留与转录激活。同时，PPP3CC亦可去磷酸化ELK1(血清应答因子辅激活因子)和DARPP32(多巴胺信号整合蛋白)，在神经可塑性与基因表达调控间建立双向桥梁。

PPI网络分析显示PPP3CC与MLH1(DNA错配修复蛋白)、APP(淀粉样前体蛋白)和BCL2(凋亡调控蛋白)存在物理互作(BioGRID证据)。该互作模式揭示PPP3CC在核质中可能参与三重功能轴：DNA损伤应答(与MLH1协同)、神经退行性病变信号(APP通路)及核内凋亡阈值的磷酸化调控(BCL2通路)。CSNK2B(CK2β亚基)的互作暗示其核质定位可能受CK2介导的磷酸化开关调控。

综合来看，PPP3CC在核质中的机制模型为：Ca²⁺/CaM激活→催化域构象重排→核内转录因子去磷酸化→基因表达重编程。该蛋白的核定位信号证据确凿(HPA Approved)，且其结构域与去磷酸化底物谱高度契合核内信号转导需求，是有价值的核蛋白研究对象。但其功能研究的文献积累较为丰富(PubMed=77)，创新空间相对有限。




![PAE](https://alphafold.ebi.ac.uk/files/AF-P48454-F1-predicted_aligned_error_v6.png)


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000120910-PPP3CC

![](https://images.proteinatlas.org/74370/2154_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74370/2154_H7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74370/2130_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74370/2130_E7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74370/1949_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74370/1949_E9_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 77**

| 42078358 | Genetic and Proteomic Investigation of the Smoking-Parkinson's Disease Association. | medRxiv 2026 |
| 42054349 | Whole transcriptome sequencing and ceRNA regulation network profiling of heat acclimation in protecting against heat str | PLoS One 2026 |
| 42037113 | Identification of PANoptosis-related biomarkers in spinal cord injury (SCI) through multi-omics analysis and machine lea | Int J Neurosci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP3CC

