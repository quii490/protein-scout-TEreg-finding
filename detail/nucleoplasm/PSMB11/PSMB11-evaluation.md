---
type: protein-evaluation
gene: "PSMB11"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMB11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMB11 |
| 蛋白名称 | Proteasome subunit beta type-11 |
| 蛋白大小 | 300 aa / 32.5 kDa |
| UniProt ID | A5LHX3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 300 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ntn_hydrolases_N; Pept_T1A_subB; Proteasome_bsu_CS |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **66.1/100** | 互证: +1 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=9, broad=33 |
| AF pLDDT | 80.4 |
| PDB | 0 |
| InterPro | Ntn_hydrolases_N; Pept_T1A_subB; Proteasome_bsu_CS |
| Pfam | Proteasome |
| PPI degree | 39 |
| ChIP | None |

**Papers**: 33537838: Thymus and autoimmunity. | 30567730: PSMB11 Orchestrates the Development of CD4 and CD8 Thymocytes via Regulation of  | 27493218: Alternative haplotypes of antigen processing genes in zebrafish diverged early i

### 4. 总体评价
★★★★  **66.1/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Proteasome subunit beta type-11

**功能**: The proteasome is a multicatalytic proteinase complex which is characterized by its ability to cleave peptides with Arg, Phe, Tyr, Leu, and Glu adjacent to the leaving group at neutral or slightly basic pH. The proteasome has an ATP-dependent proteolytic activity. Incorporated instead of PSMB5 or PSMB8, this unit reduces the chymotrypsin-like activity of the proteasome (By similarity). Plays a pivotal role in development of CD8-positive T cells (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029055 |
| InterPro | IPR000243 |
| InterPro | IPR016050 |
| InterPro | IPR001353 |
| InterPro | IPR023333 |
| Pfam | PF00227 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PSMB11（Proteasome subunit beta type-11，也称β5t）是胸腺特异性蛋白酶体亚基。其结构域架构包含典型的N端亲核水解酶折叠：InterPro注释为IPR029055（Ntn_hydrolases_N，谷氨酰胺磷酸核糖焦磷酸酰胺转移酶样）、IPR000243（Peptidase T1A, proteasome beta-subunit）、IPR016050（Proteasome beta-type subunit, conserved site）、IPR001353（Proteasome subunit beta-type）和IPR023333（Proteasome B-type subunit），Pfam匹配PF00227（Proteasome subunit）。AlphaFold v6预测整体pLDDT=80.4，是12个蛋白中结构预测质量最高的之一，300个氨基酸的紧凑折叠确保了高置信度（有序区域占比应>80%）。

PSMB11的核心功能机制已被良好表征：在胸腺皮质上皮细胞（cTEC）中，PSMB11取代组成型催化亚基PSMB5或免疫蛋白酶体亚基PSMB8整合入20S核心颗粒，从而降低蛋白酶体的糜蛋白酶样活性（By similarity）。这种亚基替换产生了独特的"胸腺蛋白酶体"（thymoproteasome），其切割特异性改变导致产生与组成型或免疫蛋白酶体不同的肽段谱，这一机制对CD8阳性T细胞的阳性选择至关重要。

PPI网络（PPI degree=39）丰度较高且具有功能特异性。BioGRID记录的互作伙伴包括ATG5（自噬相关蛋白5）、HGS（HGF-regulated tyrosine kinase substrate，ESCRT-0组分）、ILF3（白细胞介素增强子结合因子3，NFAT调控因子）、RNF8（E3泛素连接酶，DNA损伤应答关键因子）和PITX1/TLX3/PROP1（发育转录因子）。这些互作提示PSMB11的功能可能超越蛋白酶体降解，延伸至自噬-蛋白酶体crosstalk、DNA损伤信号和转录调控。

PubMed严格计数仅9篇（broad=33篇），但研究质量较高：Apavaloaei等人（2024, PMID:42261593）阐述了小鼠和人类胸腺皮质上皮Psmb11编码的β5t；两项2021年的研究（PMID:34496243, PMID:34496235）分别揭示了PSMB11调控cTEC基因表达和特异性影响蛋白酶体亚基组成。值得注意的是，PSMB11调控基因表达（PMID:34496243）的发现暗示其具有超越蛋白降解的功能——可能通过改变特定转录因子或信号分子的蛋白酶体加工来间接影响转录程序。

然而，PSMB11的核定位证据极为薄弱（评分5/10，HPA数据为nan）。尽管蛋白酶体亚基可在细胞核中发挥功能（核蛋白酶体参与转录调控和DNA修复），PSMB11在核质中的特异性定位和功能尚未被独立验证。由于PSMB11的核心功能定位于cTEC胞质中的蛋白酶体组装，其作为TE调控因子的直接潜力有限。但其间接作用——通过调控T细胞发育中关键的转录程序——仍为免疫相关TE调控提供了一个独特的研究视角。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ATG5 | BioGRID | 0 |
| PITX1 | BioGRID | 0 |
| TLX3 | BioGRID | 0 |
| PROP1 | BioGRID | 0 |
| HGS | BioGRID | 0 |
| ILF3 | BioGRID | 0 |
| RNF8 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A5LHX3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMB11

### PubMed

**Count: 33**

| PMID | Title |
|---|---|
| 42261593 | Thymic cortical epithelial Psmb11-encoded β5t in mouse and human. |
| 37180153 | Klf4 protects thymus integrity during late pregnancy. |
| 36375838 | Diversity in Cortical Thymic Epithelial Cells Occurs through Loss of a Foxn1-Dependent Gene Signature Driven by Stage-Specific Thymocyte Cross-Talk. |
| 34496243 | PSMB11 regulates gene expression in cortical thymic epithelial cells. |
| 34496235 | Specific impact of β5t on proteasome subunit composition in cortical thymic epithelial cells. |
