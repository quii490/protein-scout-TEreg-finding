---
type: protein-evaluation
gene: "OVOL3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## OVOL3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | OVOL3 |
| 蛋白名称 | Putative transcription factor ovo-like protein 3 |
| 蛋白大小 | 190 aa / 21.3 kDa |
| UniProt ID | O00110 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) + ChIP |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 190 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=68.8; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Ovo-like; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Cytosol; Nucleoplasm; Vesicles (Approved) |
| PubMed | strict=4, broad=4 |
| AF pLDDT | 68.8 |
| PDB | 0 |
| InterPro | Ovo-like; Znf_C2H2_sf; Znf_C2H2_type |
| Pfam | zf-H2C2_2 |
| PPI degree | 0 |
| ChIP | Yes |

**Papers**: 36394757: A novel nomogram associated with regulatory T cells infiltration by weighted gen | 34345183: Comprehensive Analysis of the Expression, Prognosis, and Biological Significance | 37033105: Comprehensive analysis of the expression, prognostic value and biological import

### 4. 总体评价
★★★★  **74.9/100**  |  **nucleoplasm**
**TE candidate** -- Ovo-like; Znf_C2H2_sf; Znf_C2H2_type


### 补充分析 (UniProt API)

**蛋白全称**: Putative transcription factor ovo-like protein 3

**功能**: May act as a transcription regulator

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027756 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF13465 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

OVOL3（Putative transcription factor ovo-like protein 3）是本批次评估中TE调控潜力最值得关注的候选蛋白之一。其InterPro结构域注释包括Ovo-like（IPR027756）、Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087），Pfam注释为zf-H2C2_2（PF13465）。C2H2锌指结构域是经典的真核转录因子DNA结合结构域，通过锌离子配位的Cys2His2残基形成ββα折叠，识别并结合特定的DNA序列（通常为3-4 bp的核心基序）。OVOL3含有多个C2H2锌指基序，使其具有典型的转录因子结构架构。HPA免疫荧光显示Cytosol; Nucleoplasm; Vesicles (Approved)的定位模式，且有ChIP实验数据支持其染色质结合活性，进一步确认了其作为核转录因子的身份。

尽管具备典型的转录因子结构域拓扑，OVOL3在UniProt中的功能注释仅为"May act as a transcription regulator"，反映了其生物学功能研究的高度匮乏。PubMed strict=4篇文献均发表于2021-2023年，且全部为肿瘤中的表达谱和预后分析研究（PMID 37033105, Oncol Lett 2023; PMID 36394757, Eur Rev Med Pharmacol Sci 2022; PMID 34345183, Int J Gen Med 2021），缺乏直接的分子机制研究。其190个氨基酸（21.3 kDa）的小分子量以及pLDDT=68.8的低结构置信度提示该蛋白可能含有较大比例的内在无序区域（IDR），这在转录因子中常见——IDR可通过液-液相分离（LLPS）促进转录凝聚体（transcriptional condensates）的形成。

PPI网络分析显示STRING数据库预测的互作伙伴主要为中等评分（400-500）的膜蛋白和功能未知蛋白：TMEM221（483）、TMEM211（420）、TMEM150C（417）、SDHAF1（475）、BANF2（458）。值得注意的是KAT14（408）——一种组蛋白乙酰转移酶复合体亚基——的出现，为OVOL3参与染色质修饰提供了线索。但PPI degree=0且ChIP有阳性的矛盾数据提示当前互作数据库可能对OVOL3的覆盖严重不足。

OVOL3作为OVO样转录因子家族的成员，其在TE调控中的潜在角色值得深入探索。OVO家族转录因子在进化上高度保守，从果蝇到哺乳动物参与表皮分化、生殖发育和上皮-间质转化（EMT）的调控。OVOL3是OVOL1和OVOL2的旁系同源基因，而OVOL1/2已知在EMT中通过直接抑制ZEB1转录来维持上皮表型。鉴于EMT与TE（转座子元件）激活之间的密切联系——EMT过程伴随广泛的表观遗传重编程和重复序列的去抑制——OVOL3可能在维持基因组稳定性方面通过调控TE元件的表观遗传沉默发挥作用。建议优先通过ChIP-seq解析OVOL3的全基因组结合图谱，结合RNA-seq鉴定其转录靶标，以阐明其TE调控的分子机制。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-O00110-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000105261-OVOL3

![](https://images.proteinatlas.org/47540/2064_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/47540/2064_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/47540/2075_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/47540/2075_A3_8_red_green.jpg)
![](https://images.proteinatlas.org/47540/1942_C7_4_cr5d2c48dcc82ef_red_green.jpg)
![](https://images.proteinatlas.org/47540/1942_C7_26_cr5d2c48dcc9b91_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 37033105 | Comprehensive analysis of the expression, prognostic value and biological importance of OVO‑like proteins in clear cell  | Oncol Lett 2023 |
| 36394757 | A novel nomogram associated with regulatory T cells infiltration by weighted gene co-expression network analysis for pre | Eur Rev Med Pharmacol Sci 2022 |
| 34345183 | Comprehensive Analysis of the Expression, Prognosis, and Biological Significance of OVOLs in Breast Cancer. | Int J Gen Med 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/OVOL3

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRODH2 | STRING | 431 |
| SNX32 | STRING | 414 |
| GPR162 | STRING | 406 |
| GPR137C | STRING | 419 |
| RBBP9 | STRING | 406 |
| TMEM221 | STRING | 483 |
| SDHAF1 | STRING | 475 |
| TMEM211 | STRING | 420 |
| KAT14 | STRING | 408 |
| TMEM150C | STRING | 417 |
| BANF2 | STRING | 458 |
| OVOL3 | STRING | 405 |
