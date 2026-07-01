---
type: protein-evaluation
gene: "SGPP1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SGPP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SGPP1 |
| 蛋白名称 | Sphingosine-1-phosphate phosphatase 1 |
| 蛋白大小 | 441 aa / 49.1 kDa |
| UniProt ID | Q9BX95 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 441 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=41 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PAP2/HPO; PAP2/HPO_sf |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=78 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Supported)
- PubMed strict=41 broad=78
- AF pLDDT=80.8 PDB=0
- InterPro: PAP2/HPO; PAP2/HPO_sf
- Pfam: PAP2
- PPI degree=78 ChIP: None
36197604: Functional Association of miR-133b and miR-21 Through Novel Gene Targets ATG5, L | 35081855: MicroRNA-656-3p inhibits colorectal cancer cell migration, invasion, and chemo-r | 35401845: Sevoflurane Suppresses the Proliferation, Migration and Invasion of Colorectal C

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sphingosine-1-phosphate phosphatase 1

**功能**: Specifically dephosphorylates sphingosine 1-phosphate (S1P), dihydro-S1P, and phyto-S1P. Does not act on ceramide 1-phosphate, lysophosphatidic acid or phosphatidic acid (PubMed:16782891). Sphingosine-1-phosphate phosphatase activity is needed for efficient recycling of sphingosine into the sphingolipid synthesis pathway (PubMed:11756451, PubMed:12815058, PubMed:16782891). Regulates the intracellular levels of the bioactive sphingolipid metabolite S1P that regulates diverse biological processes 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000326 |
| InterPro | IPR036938 |
| Pfam | PF01569 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

SGPP1（Sphingosine-1-phosphate phosphatase 1，UniProt: Q9BX95，441 aa / 49.1 kDa）的结构域架构分析显示：InterPro结构域包括IPR000326, IPR036938；Pfam注释为PF01569。 AlphaFold预测的pLDDT均值为80.8，表明结构预测置信度较高，核心结构域折叠可靠，但部分柔性区域可能存在构象不确定性。

蛋白质互作网络分析揭示SGPP1与以下关键因子存在相互作用：ASAH1、CERS6、SGMS1、SGMS2、UBP1（PPI度为78）。 功能注释显示Specifically dephosphorylates sphingosine 1-phosphate (S1P), dihydro-S1P, and phyto-S1P. Does not act on ceramide 1-phosphate, lysophosphatidic acid or phosphatidic acid. Sphingosine。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，SGPP1的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，SGPP1的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得41篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42168685, 42044130, 41971325等。

综上所述，SGPP1作为一个441 aa / 49.1 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=80.8的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ASAH1 | STRING | 955 |
| CERS6 | STRING | 951 |
| SGMS1 | STRING | 947 |
| SGMS2 | STRING | 942 |
| UBP1 | STRING | 765 |
| ELAVL1 | BioGRID | 1 |
| SCGN | BioGRID | 1 |
| PTH1R | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BX95-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 78**

| 42168685 | Comprehensive bioinformatics analysis targeting sphingosine-related genes in head and neck cancer. | Discov Oncol 2026 |
| 42044130 | Dysregulation of fatty acid and sphingolipid metabolism is involved in abnormal nasal epithelial differentiation. | Int Arch Allergy Immunol 2026 |
| 41971325 | Multi-omics profiling implicates gut microbiota-sphingolipid interplay in the neuroprotective effects of semaglutide on  | Front Microbiol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SGPP1

