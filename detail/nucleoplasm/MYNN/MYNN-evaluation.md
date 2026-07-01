---
type: protein-evaluation
gene: "MYNN"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## MYNN 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MYNN |
| 蛋白名称 | Myoneurin |
| 蛋白大小 | 610 aa / 68.7 kDa |
| UniProt ID | Q9NPC7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) + ChIP |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 610 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=21 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=64.4; PDB=1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | BTB/POZ_dom; SKP1/BTB/POZ_sf; Znf_C2H2_sf |
| 🔗 PPI | 4/10 | ×3 | 12.0 | PPI degree=16 |
| **加权总分** | | | **125/180** | |
| **归一化总分 (÷1.83)** | | | **69.9/100** | 互证: +3 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: Nucleoplasm (Supported)
UniProt: SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:14694499}.

IF 图像: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
610 aa / 68.7 kDa

#### 3.3 研究现状
PubMed strict=21, broad=33
- PMID 30120764: The Association of MYNN and TERC Gene Polymorphisms and Bladder Cancer in a Turkish Population. *Urology journal*
- PMID 35712083: Myoneurin regulates BMP signaling by competing with Ppm1a for Smad binding. *iScience*
- PMID 38165846: Comprehensive characterization of coding and non-coding single nucleotide polymorphisms of the Myoneurin (MYNN) gene usi *PloS one*

#### 3.4 三维结构
AF pLDDT=64.4, PDB=1

#### 3.5 结构域
InterPro: BTB/POZ_dom; SKP1/BTB/POZ_sf; Znf_C2H2_sf
Pfam: BTB; zf-C2H2; zf-C2H2_6
**TE/chromatin regulatory potential**

#### 3.6 PPI 互作网络
Combined degree=16

### 4. 总体评价
⭐⭐⭐⭐
**69.9/100** | **nucleoplasm**
TE regulatory candidate — domain/complex analysis supports chromatin/TE function


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LRRC34 | STRING | 810 |
| RIOK2 | STRING | 777 |
| PAK1 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| COPS5 | BioGRID | 1 |
| CUL3 | BioGRID | 1 |
| USP7 | BioGRID | 1 |
| ANP32B | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000085274-MYNN

![](https://images.proteinatlas.org/45149/591_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/45149/591_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/45149/579_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/45149/579_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/45149/581_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/45149/581_G6_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

MYNN（Myoneurin，UniProt: Q9NPC7，610 aa / 68.7 kDa）的结构域架构分析显示：结构域注释数据有限。 AlphaFold预测的pLDDT均值为64.4，整体结构置信度较低，该蛋白可能含有大量内在无序区域或高度柔性片段。

蛋白质互作网络分析揭示MYNN与以下关键因子存在相互作用：LRRC34、RIOK2、PAK1、ELAVL1、COPS5（PPI度为16）。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，MYNN的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.9/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，MYNN的结构域数据不足以推断TE调控机制。 研究新颖性方面，PubMed检索获得21篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42237046, 41772215, 39986329等。

综上所述，MYNN作为一个610 aa / 68.7 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=64.4的结构预测可作为设计突变体和结构-功能关系研究的起点。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NPC7-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 33**

| PMID | Title |
|---|---|
| 42237046 | A genomic structural equation modelling analysis of the shared genetic architecture of the aging spine. |
| 41772215 | Integrated multi-omics and machine learning prioritize key immune genes for multiple sclerosis risk prediction. |
| 39986329 | A large-scale genome-wide association study on female genital tract polyps highlights role of DNA repair, cell proliferation, and cell growth. |
| 38464965 | Identification and validation of NAD+ metabolism-related biomarkers in patients with diabetic peripheral neuropathy. |
| 38411850 | Effects of Halloysite Nanotubes and Multi-walled Carbon Nanotubes on Kruppel-like Factor 15-Mediated Downstream Events in Mouse Hearts After Intraveno |

