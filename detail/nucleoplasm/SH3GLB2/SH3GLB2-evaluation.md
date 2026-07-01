---
type: protein-evaluation
gene: "SH3GLB2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3GLB2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3GLB2 |
| 蛋白名称 | Endophilin-B2 |
| 蛋白大小 | 395 aa / 44.0 kDa |
| UniProt ID | Q9NR46 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 395 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=14 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=78.3; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | AH/BAR_dom_sf; BAR_dom; Endophilin_B2_SH3 |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=102 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Supported)
- PubMed strict=14 broad=19
- AF pLDDT=78.3 PDB=0
- InterPro: AH/BAR_dom_sf; BAR_dom; Endophilin_B2_SH3
- Pfam: BAR; SH3_9
- PPI degree=102 ChIP: None
39238187: Multi-omics Analysis to Identify Key Immune Genes for Osteoporosis based on Mach | 38542478: Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration. | 36498839: Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration.

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Endophilin-B2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR004148 |
| InterPro | IPR035640 |
| InterPro | IPR050384 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

SH3GLB2(Endophilin-B2)是BAR结构域超家族(Endophilin/BIN/Amphiphysin/Rvs)成员，介导膜重塑与囊泡运输。其395 aa蛋白包含两个核心功能模块：N端BAR_dom(IPR004148/AH/BAR_dom_sf)采用香蕉形同源二聚体拓扑，通过其正电性凹面结合带负电的细胞膜并诱导/感知膜曲率；C端Endophilin_B2_SH3(IPR035640/PF14604)是典型的SH3(SRC Homology 3)结构域，选择性结合富含脯氨酸基序(PXXP)的配体蛋白。pLDDT=78.3，反映了BAR-SH3双模结构域在AlphaFold中的良好预测置信度。

在胞内膜运输中，Endophilin-B2的功能分为两步：(1)BAR结构域结合高曲率膜管(内吞颈或自噬体膜边缘)，通过静电-膜脂相互作用稳定曲率；(2)SH3结构域招募下游效应因子——dynamin GTP酶(BIN1互作，STRING=703)通过富含脯氨酸尾与SH3结合，催化膜剪切断裂。CBL家族E3泛素连接酶(CBLC、CBLB，STRING score>800)与SH3GLB2通过SH3-PXXP互作，将泛素化信号整合入膜重塑过程——这是调控内吞受体(receptor tyrosine kinase, RTK)下调和蛋白分选的重要机制。

HPA定位为Cytosol和Nucleoplasm(Supported)。SH3GLB2的核质定位最能通过以下机制合理化：SH3GLB2通过SH3结构域与GADD45G和PA2G4(增殖相关蛋白2G4/Ebp1，BioGRID互作)结合。GADD45G和PA2G4均是受p53调控的核蛋白，参与DNA去甲基化和细胞周期抑制。Endophilin-B2在核质中可能通过SH3结构域的配体适配器功能锚定于核蛋白互作网络，而非通过膜重塑活性发挥作用。

近年蛋白组学将SH3GLB2与WWOX(肿瘤抑制因子WW氧化还原酶)和Zfra(锌指样蛋白)信号通路联系起来(PMID:38542478, PMID:36498839)。Zfra-WWOX-TRAPPC6A通路涉及神经退行性疾病的蛋白聚集与小胶质细胞炎症。鉴于Endophilin-B2在自噬体成熟中的已知角色，其在核质中的出现可能反映了自噬-核质信号耦合(cross-talk)的存在。PubMed仅14篇，该蛋白的研究尚处于早期阶段。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NR46-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000148341-SH3GLB2

![](https://images.proteinatlas.org/21438/147_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/21438/147_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/21438/146_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/21438/146_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/21438/148_A9_1_red_green.jpg)

### PubMed 文献

**PubMed count: 19**

| 40241169 | Bioinformatics analysis of oxidative phosphorylation-related differentially expressed genes in osteoporosis. | Eur J Med Res 2025 |
| 39924156 | Predicting Diabetic Retinopathy Using a Machine Learning Approach Informed by Whole-Exome Sequencing Studies. | Biomed Environ Sci 2025 |
| 39238187 | Multi-omics Analysis to Identify Key Immune Genes for Osteoporosis based on Machine Learning and Single-cell Analysis. | Orthop Surg 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3GLB2

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CBLC | STRING | 801 |
| CBLB | STRING | 800 |
| BIN1 | STRING | 703 |
| MAGEA1 | physical | Rual JF (2005) |
| CCDC158 | physical | Rual JF (2005) |
| SH3KBP1 | physical | Petrelli A (2002) |
| SH3GLB1 | physical | Pierrat B (2001) |
| UBA5 | physical | Behrends C (2010) |

