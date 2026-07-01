---
type: protein-evaluation
gene: "TRIM72"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TRIM72 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TRIM72 |
| 蛋白名称 | Tripartite motif-containing protein 72 |
| 蛋白大小 | 477 aa / 52.7 kDa |
| UniProt ID | Q6ZMU5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 477 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=100 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=90.7; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | B30.2/SPRY; B30.2/SPRY_sf; Butyrophylin_SPRY |
| PPI | 6/10 | x3 | 18.0 | PPI degree=55 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=100 broad=175
- AF pLDDT=90.7 PDB=3
- InterPro: B30.2/SPRY; B30.2/SPRY_sf; Butyrophylin_SPRY
- Pfam: PRY; SPRY; zf-B_box
- PPI degree=55 ChIP: None
39281689: Pathogenic mechanisms of disease in idiopathic inflammatory myopathies: autoanti | 39585917: Trim72 is a major host factor protecting against lethal Candida albicans infecti | 38681139: MG53/TRIM72: multi-organ repair protein and beyond.

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Tripartite motif-containing protein 72

**功能**: Muscle-specific E3 ubiquitin-protein ligase that plays a central role in cell membrane repair by nucleating the assembly of the repair machinery at injury sites (PubMed:36944613). Its ubiquitination activity is mediated by E2 ubiquitin-conjugating enzymes UBE2D1, UBE2D2 and UBE2D3 (By similarity). Acts as a sensor of oxidation: upon membrane damage, entry of extracellular oxidative environment results in disulfide bond formation and homooligomerization at the injury site (By similarity). This ol

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001870 |
| InterPro | IPR043136 |
| InterPro | IPR003879 |
| InterPro | IPR013320 |
| InterPro | IPR006574 |
| InterPro | IPR003877 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ANXA1 | STRING | 938 |
| ANXA6 | STRING | 868 |
| CAVIN1 | STRING | 839 |
| UBE2H | STRING | 823 |
| IRS1 | STRING | 802 |
| UBE2I | BioGRID | 1 |
| UBE2N | BioGRID | 1 |
| PTK2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZMU5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000177238-TRIM72

![](https://images.proteinatlas.org/54909/1781_A5_32_red_green.jpg)
![](https://images.proteinatlas.org/54909/1781_A5_36_red_green.jpg)
![](https://images.proteinatlas.org/54909/1806_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/54909/1806_D5_8_red_green.jpg)

### PubMed 文献

**PubMed count: 176**

| 42334177 | TRIM Expression and Its Association With Disease Activity in Systemic Lupus Erythematosus. | Kaohsiung J Med Sci 2026 |
| 42320722 | MG53-mediated membrane repair attenuates pulmonary fibrosis by antagonizing TGF-β1-driven epithelial mesenchymal transit | Exp Cell Res 2026 |
| 42297154 | The newly identified role of TRIM72, an E3 ligase, in NINJ1-mediated plasma membrane rupture: focus on its anti-inflamma | Immunol Lett 2026 |

### 深度机制分析

TRIM72（477 aa, 52.7 kDa）是TRIM（Tripartite Motif）蛋白家族成员，其结构域架构遵循经典的RBCC（RING-B-box-Coiled-coil）三联体——N端RING锌指（E3泛素连接酶催化结构域）、B-box锌指（IPR003879）和卷曲螺旋二聚化区域，C端带有B30.2/SPRY结构域（IPR001870, IPR043136），后者是蛋白-蛋白互作和底物识别的结合模块。AlphaFold预测pLDDT高达90.7，为所有25个候选蛋白中最优之一，并已有3个PDB条目提供实验结构。TRIM72因此是本批次中结构信息最丰富的候选蛋白。

TRIM72（亦称MG53）的生化和功能机制已被深度解析——它是肌肉特异性的E3泛素连接酶，在细胞膜修复中发挥核心作用（PMID:36944613）。其工作机制是一种精巧的氧化感应：膜损伤后，细胞外氧化环境进入细胞→TRIM72的二硫键形成和同源寡聚化在损伤位点触发→E3连接酶活性通过UBE2D1/D2/D3 E2酶介导→底物的K63连接多聚泛素化→修复机器的成核组装。TRIM72因此作为细胞膜损伤的分子"哨兵"。

HPA定位为Nucleoplasm; Vesicles（Approved级别），核质定位与TRIM家族蛋白的常见胞质分布有所不同。TRIM家族中多个成员（如TRIM28/KAP1、TRIM24/TIF1α、TRIM19/PML）均在核内有明确功能，其中TRIM28是TE沉默的核心调控因子。TRIM72核定位的功能意义尚未探索，但提供了通过E3泛素连接酶活性在核内调控蛋白稳态和转录的可能性。

PPI网络（BioGRID degree=55, STRING扩展）涵盖膜修复（ANXA1/ANXA6, CAVIN1）、泛素化（UBE2H/I/N）和胰岛素信号（IRS1, PTK2）通路。文献量巨大（PubMed=176），近期研究鉴定出TRIM72的新角色——通过NINJ1调控质膜破裂的抗炎功能（PMID:42297154），以及TRIM表达与系统性红斑狼疮疾病活动的关联（PMID:42334177）。

在TE调控方面，TRIM72最具潜力的通路是通过其E3泛素连接酶活性在核质中泛素化修饰TE沉默相关蛋白。TRIM蛋白家族在TE调控中的中心地位（TRIM28-SETDB1-H3K9me3轴）提示TRIM72的核定位可能使其参与类似但独特的表观遗传调控通路。TRIM72作为氧化还原传感器的特性提供了另一维度——氧化应激下的核内蛋白氧化修饰态可能调控TRIM72的核定位或泛素化底物偏好性，从而连接氧化应激和TE去抑制。建议实验：核质分离后鉴定TRIM72在核内的泛素化底物（通过TUBE-MS），以及TRIM72敲除后H3K9me3和5mC在TE位点的分布变化。

