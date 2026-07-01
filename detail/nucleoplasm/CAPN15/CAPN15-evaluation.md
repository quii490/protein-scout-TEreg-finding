---
type: protein-evaluation
gene: "CAPN15"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAPN15 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CAPN15 |
| 蛋白名称 | Calpain-15 |
| 蛋白大小 | 1086 aa / 117.3 kDa |
| UniProt ID | O75808 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1086 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Calpain_cysteine_protease; Papain-like_cys_pep_sf; Pept_cys_AS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=31 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=9, broad=16
- AF pLDDT: 70.6 / PDB: 0
- InterPro: Calpain_cysteine_protease; Papain-like_cys_pep_sf; Pept_cys_AS
- Pfam: CalpD_C; Peptidase_C2; Zn_ribbon_RanBP
- PPI degree=31 / ChIP: None
37598906: Behavioral characterization of Capn15 conditional knockout mice. | 40485323: Describing the First Canadian Cohort of Oculogastrointestinal Neurodevelopmental | 33951504: MRI of Capn15 Knockout Mice and Analysis of Capn 15 Distribution Reveal Possible

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CAPN15（Calpain-15）是一个1086 aa的大分子钙蛋白酶，具有独特的多结构域架构。其催化核心包含典型的钙蛋白酶半胱氨酸蛋白酶结构域（Pfam Peptidase_C2, InterPro IPR022684），属于木瓜蛋白酶样半胱氨酸蛋白酶超家族（InterPro IPR038765）。N端含有一个泛素结合锌指结构域（Pfam Zn_ribbon_RanBP），C端含有钙蛋白酶D_C端调控域（Pfam CalpD_C）。AlphaFold2预测pLDDT=70.6，无PDB实验结构，多结构域linker区的柔性是影响整体预测置信度的主要因素。

CAPN15的PPI网络度为31，其互作伙伴呈现出显著的泛素化和转录调控偏向。与SOX4（SRY-box转录因子4）的BioGRID互作尤为关键——SOX4是核内关键的发育转录因子，CAPN15通过去泛素化或泛素链编辑可能调控SOX4的蛋白稳定性。与TRIM25（三联基序蛋白25，E3泛素连接酶）和RNF216（RING finger蛋白216）的互作提示CAPN15深度嵌入泛素信号网络。与TRAF2（TNF受体相关因子2）的互作则连接CAPN15与NF-κB炎症信号通路。泛素化底物识别（优先结合Lys-48和Lys-63连接的长链）和钙依赖性E-cadherin/CDH1剪切是CAPN15的核心生化活性（PMID:41380969）。

CAPN15的功能机制代表了非蛋白酶体泛素信号的一个范例——作为泛素导向的非蛋白酶体蛋白酶，CAPN15读取底物的泛素化标记后执行有限剪切，而非完全降解。在核质中，CAPN15可能通过剪切泛素化的转录因子、染色质调控因子或核骨架蛋白来调控核内信号。临床遗传学证据极为有力：PMID:40485323和37598906报道CAPN15致病性变异导致眼胃肠神经发育综合征（OGIN），CAPN15条件性敲除小鼠表现出明确的行为异常。PMID:33951504通过MRI分析揭示了Capn15敲除小鼠的脑结构异常。

作为核质蛋白，CAPN15的研究新颖性极高（PubMed=9，得分10/10），核定位明确（Nucleoplasm Approved，得分9/10）。其泛素导向的蛋白酶活性在核内蛋白稳态和信号调控中的角色几乎完全未被探索。鉴于CAPN15识别poly-Ub链的能力，它可能在核内DNA损伤应答（组蛋白泛素化）或转录因子更新（如SOX4）中发挥关键的蛋白质量控制功能。这一方向代表了钙蛋白酶生物学和核内泛素信号交叉处的一个崭新领域。

### 补充分析 (UniProt API)

**蛋白全称**: Calpain-15

**功能**: Calcium-dependent cysteine protease that functions as a non-proteasomal, ubiquitin-directed protease regulating cell adhesion through cleavage of E-cadherin/CDH1. Binds to ubiquitinated proteins via its N-terminal, preferentially recognizing longer polyubiquitin chains including both 'Lys-48- and 'Lys-63'-linked chains. Recognizes the ubiquitinated E-cadherin-catenin complex and cleaves E-cadherin in a calcium- and ubiquitination-dependent manner resulting in lysosomal degradation of the resulta

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR022684 |
| InterPro | IPR038765 |
| InterPro | IPR000169 |
| InterPro | IPR001300 |
| InterPro | IPR001876 |
| InterPro | IPR036443 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SOX4 | BioGRID | 1 |
| TBL1Y | BioGRID | 1 |
| CDH5 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| CPEB2 | BioGRID | 1 |
| RNF216 | BioGRID | 1 |
| TRAF2 | BioGRID | 1 |
| DAZAP2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O75808-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103326-CAPN15

![](https://images.proteinatlas.org/11960/1113_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/11960/1113_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/11960/1226_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/11960/1226_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/11960/1123_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/11960/1123_G2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 16**

| 42012806 | Multi-Scale Genetic and Transcriptomic Analyses Identify Druggable Targets for Epilepsy. | Curr Med Sci 2026 |
| 41380969 | CAPN15 is a non-proteasomal, ubiquitin-directed calpain protease that regulates cell adhesion by cleaving E-cadherin. | J Biol Chem 2026 |
| 40485323 | Describing the First Canadian Cohort of Oculogastrointestinal Neurodevelopmental Syndrome Caused by CAPN15 Pathogenic Va | Am J Med Genet A 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAPN15

