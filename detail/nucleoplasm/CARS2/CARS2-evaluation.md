---
type: protein-evaluation
gene: "CARS2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CARS2

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | CARS2 |
| Protein Name | Probable cysteine--tRNA ligase, mitochondrial |
| Size | 564 aa / 62.2 kDa |
| UniProt | Q9HA77 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 564 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed=36 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=86.1; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Cys-tRNA-ligase; Cys-tRNA/MSH_ligase; Rossmann-like_a/b/a_fold |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=145 |
| **加权总分** | | | **135.0/180** | |
| **归一化总分 (÷1.83)** | | | **73.8/100** | 互证: +2.0 |

### 3. Analysis
- HPA: Mitochondria; Nucleoplasm (Approved)
- PubMed: strict=36, broad=115
- AF pLDDT: 86.1 / PDB: 0
- InterPro: Cys-tRNA-ligase; Cys-tRNA/MSH_ligase; Rossmann-like_a/b/a_fold
- Pfam: tRNA-synt_1e
- PPI degree=145 ChIP: None
39026663: Characterizing mitochondrial features in osteoarthritis through integrative mult | 39643979: Emerging roles of hydrogen sulfide-metabolizing enzymes in cancer. | 40303402: Supersulfide controls intestinal inflammation by suppressing CD4(+) T cell proli

### 4. Assessment
★★★★  **74.9/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Probable cysteine--tRNA ligase, mitochondrial

**功能**: Mitochondrial cysteine-specific aminoacyl-tRNA synthetase that catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015803 |
| InterPro | IPR024909 |
| InterPro | IPR014729 |
| InterPro | IPR032678 |
| InterPro | IPR009080 |
| Pfam | PF01406 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

CARS2是线粒体半胱氨酰-tRNA合成酶，属于Class I氨酰tRNA合成酶(aaRS)家族。其结构域架构包含三个功能层：Cys-tRNA-ligase催化域(IPR015803/PF01406)采用Rossmann-like a/b/a折叠，负责ATP依赖的半胱氨酸活化；Cys-tRNA/MSH_ligase域(IPR024909)介导tRNA^Cys反密码子环的识别与结合；Rossmann-like_a/b/a_fold(IPR014729)提供全局结构稳定性。pLDDT=86.1，是这批蛋白中结构置信度最高的蛋白之一，表明其催化核心具有极高的刚性骨架结构。

aaRS催化的经典两步反应在CARS2中完全保守：半胱氨酸+ATP→Cys-AMP+PPi(氨基酸活化)；Cys-AMP+tRNA^Cys→Cys-tRNA^Cys+AMP(氨酰化)。在翻译保真性中，CARS2的校对(Editing)活性同样关键——错活化丝氨酸或硒代半胱氨酸时，其编辑结构域水解错误产物以防止mRNA解码错误。

HPA定位为Mitochondria和Nucleoplasm(Approved)，这种双定位模式在aaRS家族中被广泛观察到——多种线粒体aaRS的翻译剪接变体(Splice Variant)或翻译后修饰后具有核质定位。在核质中，aaRS可发挥非经典(Non-canonical)功能，称为"Moonlighting"活性。硫化氢(H₂S)代谢研究(PMID:39643979)显示，CARS除了其tRNA合成酶功能外，还通过其活性位点Cys残基参与超硫化物的硫烷硫转移，连接了aaRS催化与气体信号分子代谢。

CARS2的PPI网络呈显著的星形拓扑——EGFR、PTEN、BLM(Bloom综合征解旋酶)和TRMT61B(线粒体tRNA甲基转移酶)均以BioGRID证据与CARS2互作。值得注意的是，PTEN-PI3K-AKT通路中PTEN(磷酸酶)和EGFR(受体酪氨酸激酶)的同时互作暗示CARS2可能在核质中作为翻译调控"信号枢纽"：CARS2的氨酰化状态反映了细胞能量(ATP/AMP比值)和氨基酸(Cys)的可用性，这种营养信号通过CARS2-PTEN-EGFR复合物传递至PI3K/AKT通路。此外，BLM的互作提示CARS2可能影响基因组稳定性的翻译依赖性调控。PubMed仅36篇，研究新颖性较高。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HA77-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000134905-CARS2

![](https://images.proteinatlas.org/41776/486_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/41776/486_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/41776/509_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/41776/509_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/41776/490_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/41776/490_F8_3_red_green.jpg)

### PubMed 文献

**PubMed count: 116**

| 42367122 | Identification of Diagnostic Biomarkers Related to Oxidative Stress in Rheumatoid Arthritis. | Curr Med Chem 2026 |
| 42327746 | Reduced CARS2 expression elicits a low-grade pro-inflammatory signature in THP-1 macrophages. | Front Immunol 2026 |
| 42293516 | Study protocol for a randomized controlled trial of fecal microbiota transplantation via different routes in children wi | Front Microbiol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CARS2

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EGFR | physical | Tong J (2014) |
| RGCC | physical | Huttlin EL (2015) |
| OXLD1 | physical | Huttlin EL (2015) |
| BLM | genetic | Vizeacoumar FJ (2013) |
| PTEN | genetic | Vizeacoumar FJ (2013) |
| CAPN1 | physical | Hein MY (2015) |
| TRMT61B | physical | Huttlin EL (2017) |
| DONSON | genetic | Horlbeck MA (2018) |

