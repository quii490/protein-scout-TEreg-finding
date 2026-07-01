---
type: protein-evaluation
gene: "PCDHA3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHA3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHA3 |
| 蛋白名称 | Protocadherin alpha-3 |
| 蛋白大小 | 950 aa / 102.4 kDa |
| UniProt ID | Q9Y5H8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 950 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD |
| PPI | 5/10 | x3 | 15.0 | PPI degree=34 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=5 broad=10
- AF pLDDT=73.7 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD
- Pfam: Cadherin; Cadherin_2; Cadherin_tail
- PPI degree=34 ChIP: None
34859219: Maternal immune activation downregulates schizophrenia genes in the foetal mouse | 23192925: Exome sequencing in a family with restless legs syndrome. | 33756103: Novel ultra-rare exonic variants identified in a founder population implicate ca

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHA3（Protocadherin alpha-3）是原钙粘蛋白α簇的核心成员，拥有950 aa的大分子量（102.4 kDa）。其结构域架构体现了原钙粘蛋白家族的"可变-恒定"拼接策略：N端可变区包含6个钙粘蛋白重复结构域（InterPro IPR002126, IPR015919），赋予每个α亚型独特的黏附特异性；C端胞内结构域（InterPro IPR031904）是α和γ簇共用的恒定区（α-恒定区），含钙粘蛋白胞内CBD结构域（InterPro IPR050174）和一个保守的Cadherin_tail（Pfam Cadherin_tail）。AlphaFold2预测pLDDT=73.7（得分5/10），无PDB实验结构。

PCDHA3的PPI网络度为34，其互作特征在此批PCDH蛋白中最为突出：互作伙伴高度集中于PCDHA亚家族成员——PCDHA10、PCDHA6、PCDHA9、PCDHA1、PCDHA11均与PCDHA3在BioGRID中形成互作。这种亚家族内的密集互作网络反映了原钙粘蛋白在神经元表面通过顺式多聚化形成黏附单元的分子机制——同一神经元表达多种PCDHA亚型，它们在膜表面形成随机顺式四聚体，这种组合多样性是神经元自我识别和突触特异性的分子基础。与ABHD6（α/β水解酶结构域蛋白6，内源性大麻素水解酶）和KCNT2（钠激活钾通道亚家族T成员2）的互作则提示PCDHA3可能在突触信号调控中发挥超越黏附的功能。

PCDHA3在核质中的功能涉及其共用的α-恒定区胞内结构域。PCDH-α和PCDH-γ簇的恒定区胞内结构域在核内具有明确的转录调控功能——被剪切后入核的胞内片段能够调控神经元基因表达。PMID:34859219发现母体免疫激活下调胎儿小鼠大脑中精神分裂症基因——PCDHA3出现在该研究的差异表达基因列表中，提示PCDHA3可能在神经发育的免疫应激应答中发挥作用。PMID:40988636发现PCDHA基因簇变异与日本人群短根异常可能相关，这是一项形态遗传学研究，暗示PCDHA3在颅面发育中的非神经元功能。

PCDHA3属于研究新颖性极高的核质蛋白（PubMed=5，得分10/10），Nucleoplasm Approved定位（得分9/10）。其在Golgi apparatus与Nucleoplasm的双定位模式支持了剪切-转运模型——PCDHA3可能在Golgi中经过加工修饰后通过逆行运输至内质网，内质网-核膜连接处可能作为其入核的入口。PCDHA3在精神分裂症和神经发育障碍中的遗传关联（PMID:23192925, 33756103）证实其临床相关性，但其核内功能的分子机制仍是完全未开发的领域。

### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin alpha-3

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |
| InterPro | IPR050174 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCDHA10 | BioGRID | 0 |
| PCDHA6 | BioGRID | 0 |
| PCDHA9 | BioGRID | 0 |
| PCDHA1 | BioGRID | 0 |
| PCDHA11 | BioGRID | 0 |
| ABHD6 | BioGRID | 0 |
| KCNT2 | BioGRID | 0 |
| MLYCD | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5H8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000255408-PCDHA3

![](https://images.proteinatlas.org/35667/1471_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/35667/1471_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/35667/1669_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/35667/1669_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/35667/442_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/35667/442_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/35667/2275_F3_13_red_green.jpg)
![](https://images.proteinatlas.org/35667/2275_F3_366_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 42089102 | A risk scoring model for lung squamous cell carcinoma based on epithelial-mesenchymal transition-related genes: an integ | PeerJ 2026 |
| 40988636 | Protocadherin alpha gene cluster variants are potentially associated with short root anomaly in Japanese. | Eur J Orthod 2025 |
| 37329382 | miR-218-5p and miR-320a-5p as Biomarkers for Brain Disorders: Focus on the Major Depressive Disorder and Parkinson's Dis | Mol Neurobiol 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHA3

