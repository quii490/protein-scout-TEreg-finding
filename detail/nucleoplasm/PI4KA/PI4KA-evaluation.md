---
type: protein-evaluation
gene: "PI4KA"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PI4KA 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PI4KA |
| 蛋白名称 | Phosphatidylinositol 4-kinase alpha |
| 蛋白大小 | 2102 aa / 236.8 kDa |
| UniProt ID | P42356 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 2102 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=59 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=79.7; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARM-type_fold; Kinase-like_dom_sf; PI3/4_kinase |
| PPI | 8/10 | x3 | 24.0 | PPI degree=245 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=59 broad=101
- AF pLDDT=79.7 PDB=4
- InterPro: ARM-type_fold; Kinase-like_dom_sf; PI3/4_kinase
- Pfam: PI3_PI4_kinase; PI3Ka; PI4K_N
- PPI degree=245 ChIP: None
34663815: Palmitoylation targets the calcineurin phosphatase to the phosphatidylinositol 4 | 36341355: A synonymous mutation in PI4KA impacts the transcription and translation process | 38003592: Genetic Heterogeneity Underlying Phenotypes with Early-Onset Cerebellar Atrophy.

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PI4KA（Phosphatidylinositol 4-kinase alpha）是一个巨大的脂质激酶（2102 aa, 236.8 kDa），其多结构域架构如同一座分子机器。催化核心为PI3/PI4激酶结构域（Pfam PI3_PI4_kinase, InterPro IPR000403），负责将磷脂酰肌醇（PtdIns）磷酸化为PtdIns4P——这是肌醇磷脂信号系统的第一步关键反应。N端含有PI4K-N调控结构域（Pfam PI4K_N），中间包含ARM型折叠重复区（InterPro IPR016024）和PI3Ka螺旋结构域（Pfam PI3Ka）。AlphaFold2预测pLDDT=79.7（得分7/10），PDB有4个实验结构，但由于蛋白巨大，全长结构仍未解析。

PI4KA的PPI网络是此批25个核蛋白中最为庞大的（degree=245，得分8/10），其STRING网络呈现出高度富集的磷脂酰肌醇信号互作簇。PIP5K1C（STRING=966）和PIP5K1B（STRING=958）是PtdIns4P的下游激酶，将PtdIns4P进一步磷酸化为PIP2。PIK3R1（STRING=924）和PIK3R2（STRING=925）是PI3K的调控亚基，暗示PI4KA和PI3K信号之间存在复杂的反馈和前馈调控。PTEN（STRING=916），经典的PIP3磷酸酶，也出现在互作网络中。OCRL（Lowe眼脑肾综合征蛋白，STRING=773）是一种PIP2 5-磷酸酶，其互作连接PI4KA与高尔基体和内体膜运输。

PI4KA调控核内膜脂质环境的机制由其经典的质膜功能外推而来。PtdIns4P不仅是PIP2和PIP3的前体，其本身也是一个重要的信号脂质分子，通过募集含PH结构域或OSBP相关结构域的效应蛋白调控膜运输和信号转导。在核质Approved级别定位的背景下，PI4KA可能通过调控核内膜的PtdIns4P水平影响核内脂质信号和核膜动力学。最新研究（PMID:42258130）发现E-Syt1将PI4KA招募至内质网-质膜连接处增强PtdIns4P合成，类似机制可能存在于内核膜-核质界面。

PI4KA的临床意义已被大量遗传学研究证实。PI4KA突变导致早发性小脑萎缩（PMID:38003592），影响转录和翻译过程（PMID:36341355）。棕榈酰化修饰将钙调磷酸酶靶向PI4KA（PMID:34663815），揭示了脂质信号和钙信号的交叉调控。59篇PubMed文献（得分7/10）的研究基础结合巨大的PPI网络，使PI4KA成为核内脂质调控研究中一个信息密集的中心节点。其巨大的分子量（236.8 kDa）需要主动核输入机制，目前在核质中PI4KA的入核信号和核内底物特异性仍完全未知。

### 补充分析 (UniProt API)

**蛋白全称**: Phosphatidylinositol 4-kinase alpha

**功能**: Acts on phosphatidylinositol (PtdIns) in the first committed step in the production of the second messenger inositol-1,4,5,-trisphosphate

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016024 |
| InterPro | IPR011009 |
| InterPro | IPR015433 |
| InterPro | IPR000403 |
| InterPro | IPR036940 |
| InterPro | IPR018936 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIP5K1C | STRING | 966 |
| PIP5K1B | STRING | 958 |
| PIK3R2 | STRING | 925 |
| PIK3R1 | STRING | 924 |
| PTEN | STRING | 916 |
| TEP1 | STRING | 916 |
| PIK3C2G | STRING | 911 |
| OCRL | STRING | 773 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P42356-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000241973-PI4KA

![](https://images.proteinatlas.org/75515/1592_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/75515/1592_A5_3_red_green.jpg)
![](https://images.proteinatlas.org/75515/1585_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/75515/1585_B12_4_red_green.jpg)
![](https://images.proteinatlas.org/75515/1616_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/75515/1616_B12_3_red_green.jpg)

### PubMed 文献

**PubMed count: 101**

| 42360433 | Phosphatidylserine and RhoB connect PI4P and PA metabolism to maintain plasma membrane identity. | J Cell Biol 2026 |
| 42258130 | E-Syt1 recruits PI4KA to endoplasmic reticulum-plasma membrane junctions to enhance PI4P synthesis. | Sci China Life Sci 2026 |
| 42218382 | Integrated environmental and genomic analysis reveals the drivers and genetic mechanisms of agro-climatic adaptation in  | BMC Genomics 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PI4KA

