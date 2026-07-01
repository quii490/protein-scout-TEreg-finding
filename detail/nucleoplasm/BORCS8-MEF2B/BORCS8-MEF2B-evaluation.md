---
type: protein-evaluation
gene: "BORCS8-MEF2B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## BORCS8-MEF2B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | BORCS8-MEF2B |
| 蛋白名称 | BORCS8-MEF2B readthrough |
| 蛋白大小 | 382 aa / 40.5 kDa |
| UniProt ID | H3BNR1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cell Junctions; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 382 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=53.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | MEF2-like_N; TF_MADSbox; TF_MADSbox_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- HPA: Cell Junctions; Cytosol; Nucleoplasm (Approved)
- PubMed: strict=1, broad=1
- AF pLDDT: 53.5 / PDB: 0
- InterPro: MEF2-like_N; TF_MADSbox; TF_MADSbox_sf
- Pfam: SRF-TF
- PPI degree: 0 / ChIP: None
**Papers**: 33362776: Effects of In Vivo Gluten Challenge on PBMC Gene Expression Profiles in Diet Tre

### 4. 总体评价
★★★★  **71.6/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: BORCS8-MEF2B readthrough

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033896 |
| InterPro | IPR002100 |
| InterPro | IPR036879 |
| Pfam | PF00319 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: BORCS8-MEF2B readthrough

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033896 |
| InterPro | IPR002100 |
| InterPro | IPR036879 |
| Pfam | PF00319 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-H3BNR1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000064489-BORCS8-MEF2B

![](https://images.proteinatlas.org/4734/113_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/4734/113_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/4734/112_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/4734/112_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/4734/967_A5_5_red_green.jpg)
![](https://images.proteinatlas.org/4734/967_A5_6_red_green.jpg)

### PubMed 文献

**PubMed count: 1**

| 33362776 | Effects of In Vivo Gluten Challenge on PBMC Gene Expression Profiles in Diet Treated Celiac Disease. | Front Immunol 2020 |

### 深度机制分析

BORCS8-MEF2B（382 aa, 40.5 kDa）是一个通读（readthrough）融合蛋白，由相邻基因BORCS8和MEF2B通过转录通读产生，是基因间剪接重组的自然产物。该蛋白的结构域架构独特——保留了MEF2B的N端MADS-box/MEF2样结构域（MEF2-like_N, IPR033896）和完整的SRF型转录因子DNA结合域（TF_MADSbox, IPR002100），而丢失了BORCS8原有的功能。MADS-box结构域是古老的真核转录因子折叠，以α/β夹层结构识别DNA上的CArG盒[CC(A/T)6GG]序列，介导蛋白二聚化和DNA结合。AlphaFold预测pLDDT仅53.5，显著低于典型MEF2蛋白的折叠质量，提示通读融合可能部分破坏了结构域的折叠完整性。

经典的MEF2B是MEF2转录因子家族成员之一，在肌肉发育、神经分化和免疫细胞（特别是B细胞）功能中发挥核心作用。MEF2B通过N端的MADS-box/MEF2结构域结合DNA，通过C端的转录激活结构域募集共激活因子（如p300/CBP）。BORCS8-MEF2B通读蛋白保留了DNA结合和二聚化结构域但缺失了C端激活域，提示其可能作为显性负调控因子——通过与全长MEF2蛋白形成异源二聚体来占据CArG盒DNA位点但不激活转录。

PPI网络（STRING，无BioGRID实验互作）强烈支持这一假说。MEF2B（STRING 980）、MEF2C（STRING 405）、MEF2D（STRING 513）的高置信度互作证实BORCS8-MEF2B可整合入MEF2二聚化网络。与HDAC9（STRING 944，组蛋白去乙酰化酶）、CABIN1（STRING 770，钙调神经磷酸酶结合蛋白/转录抑制因子）、NFATC1-4（STRING 920/915/918/545）和MAPK11/12（STRING 813/757）的互作进一步暗示该通读蛋白与钙信号-转录偶联通路存在深度交叉。

在TE调控方面，MEF2转录因子家族的DNA结合基序（CArG盒）在多种TE家族中被发现，包括MER、LTR和ERV类反转录转座子中。若BORCS8-MEF2B作为显性负调控因子竞争性结合TE内的CArG样序列，它可能通过封闭这些位点来阻止全长MEF2蛋白激活邻近基因或TE本身的转录。此外，MEF2-HDAC9复合物的形成可能将组蛋白去乙酰化酶直接招募至TE位点，触发局部染色质压缩和TE转录抑制。文献极度稀缺（PubMed=1，PMID:33362776——乳糜泻PBMC基因表达）既说明了研究新颖性的优势（新颖性50/50），也暴露了功能注释的缺乏。建议通过ChIP-Seq鉴定BORCS8-MEF2B在全基因组范围的结合位点，并特别分析TE序列区域的富集情况。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAPK12 | STRING | 757 |
| MYOG | STRING | 529 |
| NCAN | STRING | 755 |
| MEF2D | STRING | 513 |
| NFATC3 | STRING | 918 |
| RFXANK | STRING | 591 |
| NKX2-5 | STRING | 554 |
| MAPK11 | STRING | 813 |
| MEF2C | STRING | 405 |
| NFATC2 | STRING | 915 |
| CABIN1 | STRING | 770 |
| NFATC4 | STRING | 545 |
| NFATC1 | STRING | 920 |
| MEF2B | STRING | 980 |
| HDAC9 | STRING | 944 |
