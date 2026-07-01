---
type: protein-evaluation
gene: "RGL2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RGL2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RGL2 |
| 蛋白名称 | Ral guanine nucleotide dissociation stimulator-like 2 |
| 蛋白大小 | 777 aa / 83.5 kDa |
| UniProt ID | O15211 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 777 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=91 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=71.4; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | RA_dom; Ras-like_GEF; Ras-like_Gua-exchang_fac_N |
| PPI | 5/10 | x3 | 15.0 | PPI degree=41 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=91 broad=143
- AF pLDDT=71.4 PDB=2
- InterPro: RA_dom; Ras-like_GEF; Ras-like_Gua-exchang_fac_N
- Pfam: RA; RasGEF; RasGEF_N
- PPI degree=41 ChIP: None
18540861: G-protein binding features and regulation of the RalGDS family member, RGL2. | 29462139: The COP9 Signalosome regulates seed germination by facilitating protein degradat | 35166830: CONSTITUTIVE PHOTOMORPHOGENIC 1 promotes seed germination by destabilizing RGA-L

### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ral guanine nucleotide dissociation stimulator-like 2

**功能**: Probable guanine nucleotide exchange factor. Putative effector of Ras and/or Rap. Associates with the GTP-bound form of Rap 1A and H-Ras in vitro (By similarity)

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

---


### 深度机制分析

**结构域架构**：RGL2（O15211, Ral guanine nucleotide dissociation stimulator-like 2, 777 aa / 83.5 kDa）的主要结构域注释为RA_dom, Ras-like_GEF, Ras-like_Gua-exchang_fac_N。Pfam数据库进一步识别到RA、RasGEF、RasGEF_N等保守域。AlphaFold pLDDT=71.4（中等）——折叠域基本可信，但部分区域置信度较低，建议实验解析。该蛋白已有2个实验PDB结构条目，为机械性研究提供直接的结构基础。PubMed=91，该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=41）——STRING数据库记录的互作伙伴包括HRAS、RPS18、KIFC1、SLC39A7、RXRB、RING1。其中RXRB、RING1、KAT5等具有染色质调控或转录相关功能——提示RGL2可能通过protein-protein interaction平台间接参与核内转录调控网络。

**结构解读**：AlphaFold预测（pLDDT=71.4）整体折叠可信，RA_dom构成结构核心。Pfam域RA、RasGEF的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=71.4提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：RGL2含有Ras-association（RA）domain和RasGEF domain——属于Ras/Rap GTPase signaling cascade的guanylyl nucleotide exchange factor（GEF）。Ras-MAPK signaling pathway已被报道与ERV activation相关——RGL2可能作为Ras signal transducer间接modulate TE expression through downstream transcription factor activation。

**TE调控展望**：RGL2的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）RGL2是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）RGL2是否能够通过其结构域识别TE-derived DNA/RNA element；（3）RGL2的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定RGL2在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HRAS | STRING | 980 |
| RPS18 | STRING | 874 |
| KIFC1 | STRING | 861 |
| SLC39A7 | STRING | 814 |
| RXRB | STRING | 788 |
| RING1 | STRING | 742 |
| KAT5 | BioGRID | 1 |
| KAT7 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O15211-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RGL2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000237441-RGL2

![](https://images.proteinatlas.org/47039/1517_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/47039/1517_B9_2_red_green.jpg)

### PubMed

**Count: 143**

| PMID | Title |
|---|---|
| 42333383 | Comparative regenerative mechanisms of adipose-derived mesenchymal stem cell- and conditioned medium-loaded three-dimensional bioprinted hydrogels in  |
| 42329538 | Stratification overcomes ABA-mediated seed dormancy by uncoupling RGL2/ABI5 inhibition from α-amylase expression. |
| 41629528 | Direct receptor competition gates RGL2 proteolysis for seed germination timing in Arabidopsis. |
| 41554047 | ASTWAS: modeling alternative polyadenylation and SNP effects in kernel-driven TWAS reveal novel genetic associations for complex traits. |
| 41234887 | Unveiling critical genes and molecular subtypes in ovarian cancer: insights into tumor immunity and carbohydrate-lipid metabolism. |
