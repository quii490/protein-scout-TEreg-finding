---
type: protein-evaluation
gene: "ARSK"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## ARSK (Arylsulfatase K) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ARSK |
| 蛋白全称 | Arylsulfatase K |
| UniProt ID | Q6UWY0 |
| 蛋白大小 | 536 aa / 59.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 536 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR017850; InterPro:IPR047892; InterPro:IPR051849; InterPro:IPR000917; Pfam:PF00884 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Catalyzes the hydrolysis of pseudosubstrates such as p-nitrocatechol sulfate and p-nitrophenyl sulfate (PubMed:23986440). Catalyzes the hydrolysis of the 2-sulfate groups of the 2-O-sulfo-D-glucuronate residues of chondroitin sulfate, heparin and heparitin sulfate (PubMed:28055182, PubMed:34916232). Acts selectively on 2-sulfoglucuronate and lacks activity against 2-sulfoiduronate (PubMed:28055182

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR017850 |
| InterPro | IPR047892 |
| InterPro | IPR051849 |
| InterPro | IPR000917 |
| Pfam | PF00884 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

ARSK编码芳基硫酸酯酶K（Arylsulfatase K）的TrEMBL变体，其结构域架构以硫酸酯酶超家族催化模块为特征：采用经典的碱性磷酸酶样折叠（IPR017850、IPR051849），其活性位点含有保守的硫酸酯酶特征基序——甲酰甘氨酸（FGly）残基由SUMF1/Egs经翻译后氧化修饰产生，是催化硫酸酯水解所必需的亲核体。IPR047892指向ARSK在硫酸软骨素/肝素2-O-硫酸酯特异性水解中的选择性功能（PubMed:28055182、34916232，PMID均已验证）。IPR000917（硫酸酯酶家族）和Pfam PF00884覆盖催化核心区域。

536 aa（59.0 kDa）的中型分子量在溶酶体/细胞外基质降解酶中较为典型。AlphaFold预测结构可用。PPI数据显示少量BioGRID互作：ZFP36L2（RNA结合锌指蛋白）、DDX39A（RNA解旋酶）、S100P（Ca2+结合蛋白）、TAZ（Hippo信号转录辅因子），以及Tissue Factor和IGHG等其他蛋白。其中ZFP36L2和DDX39A的连接暗示ARSK可能存在非经典的核酸相关互作角色。

TE调控相关性的机制链条极为间接：ARSK主要功能为硫酸软骨素/肝素降解，属于细胞外基质（ECM）和溶酶体代谢酶类。其与TE调控的潜在连接包括：（1）通过调控细胞表面硫酸软骨素蛋白多糖浓度影响细胞外信号（如FGF、BMP、Wnt）的信号传导效率，这些信号最终通过下游转录因子影响TE表达；（2）通过ZFP36L2互作间接参与RNA代谢——ZFP36L2是一个RNA结合蛋白，参与mRNA降解调控；（3）TAZ蛋白的互作暗示可能参与Hippo-YAP/TAZ信号输出，该通路在机械力感知和染色质调控中发挥作用。

但无已知核定位注释（核定位特异性仅4/10），PubMed 24篇赋予了较好的新颖性（10/10），但核心功能与TE调控无关。归一化总分67.8/100。不建议作为TE调控靶标，其ECM降解功能与TE调控的距离过远。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRSS37 | BioGRID | 1 |
| ZFP36L2 | BioGRID | 1 |
| DDX39A | BioGRID | 1 |
| S100P | BioGRID | 1 |
| ZNF621 | BioGRID | 1 |
| GGH | BioGRID | 1 |
| TGOLN2 | BioGRID | 1 |
| TAZ | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ARSK

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164291-ARSK

![](https://images.proteinatlas.org/42384/748_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/748_E2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164291-ARSK

![](https://images.proteinatlas.org/42384/748_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/748_E2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164291-ARSK

![](https://images.proteinatlas.org/42384/748_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/748_E2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/896_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/42384/728_E2_6_blue_red_green.jpg)

### PubMed

**Count: 24**

| PMID | Title |
|---|---|
| 41469517 | Identification and validation of prognostic markers for cuproptosis-related macrophage polarization genes in hepatocellular carcinoma. |
| 41449816 | Correction to "Syndrome of the Month: ARSK-Related Mucopolysaccharidosis Type 10". |
| 40763656 | Arylsulfatase K attenuates airway epithelial cell senescence in COPD by regulating parkin-mediated mitophagy. |
| 40742107 | ARSK-Related Mucopolysaccharidosis Type 10. |
| 39214089 | Discovery of a neuropeptide that acts as an autotomy-promoting factor. |


