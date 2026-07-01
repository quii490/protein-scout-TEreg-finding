---
type: protein-evaluation
gene: "EEF1AKMT4-ECE2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## EEF1AKMT4-ECE2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EEF1AKMT4-ECE2 |
| 蛋白名称 | EEF1AKMT4-ECE2 readthrough transcript protein |
| 蛋白大小 | 883 aa / 99.8 kDa |
| UniProt ID | P0DPD8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 883 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=91.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | MetalloPept_cat_dom_sf; Methyltransf_25; Peptidase_M13 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=0 broad=0
- AF pLDDT=91.2 PDB=0
- InterPro: MetalloPept_cat_dom_sf; Methyltransf_25; Peptidase_M13
- Pfam: Methyltransf_25; Peptidase_M13; Peptidase_M13_N
- PPI degree=0 ChIP: None


### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

EEF1AKMT4-ECE2是一个通过转录通读（transcriptional readthrough）产生的融合蛋白，由EEF1AKMT4（eEF1A赖氨酸甲基转移酶4）和ECE2（内皮素转换酶2）两个原本独立基因的编码序列拼接而成，总计883个氨基酸。这种罕见的基因组结构赋予了该融合蛋白双重的催化功能域：N端的Methyltransf_25结构域（IPR041698/PF13649）负责甲基转移酶活性，而C端的Peptidase_M13（IPR000718/PF01431）和Peptidase_M13_N（IPR008753）则是锌金属肽酶催化核心。AlphaFold预测pLDDT高达91.2，属本批最高的水平之一，反映了两个催化域的独立有序折叠。

在生化功能层面，该融合蛋白的N端EEF1AKMT4部分催化eEF1A（真核翻译延伸因子1A）特定赖氨酸残基的甲基化——这是一种影响翻译保真度的关键修饰。C端ECE2部分则承担"big内皮素→内皮素"的蛋白水解加工功能，属于内皮素系统的限速激活酶。两种催化活性在一条多肽链上的物理偶联可能具有协同进化意义——例如，内皮素信号诱导的翻译重编程可能需要eEF1A甲基化状态的快速调节。然而，"融合"是否真的发生在蛋白水平（即是否被翻译为全长融合蛋白，还是仅作为独立的两个蛋白）尚未经实验验证。

HPA的Uncertain核质定位（Cytosol; Nucleoplasm）和PPI degree=0的孤立网络是该蛋白最大的特征与瓶颈。作为一种含量极低、表达高度受限的通读产物，该融合蛋白可能仅在特定组织或细胞类型中被翻译——这可能解释了其缺乏PPI互作伙伴的现象。但在STRING数据库的推测互作中，IDE（胰岛素降解酶，STRING=446）既属于M16金属肽酶家族（与M13共享进化起源），其出现提供了一条关于ECE2结构域功能的有趣线索。

从TE调控角度，EEF1AKMT4-ECE2作为PubMed=0的真正"零文献蛋白"，是极端新靶点——任何实验发现都会是原创性成果。然而，研究该蛋白面临显著的技术挑战——如果其在体内极少被翻译，则需要使用强制表达系统。融合蛋白的"双催化活性"赋予了其独特的化学生物学潜力——设计同时靶向两个活性位点的小分子探针可用于功能获得/缺失实验。在TE研究中，eEF1A作为翻译延伸因子的核心角色与转座子mRNA的翻译密切相关——eEF1AKMT4通过甲基化修饰eEF1A可能影响TE mRNA的翻译效率，这是一个崭新且极富创新性的研究方向。

**蛋白全称**: EEF1AKMT4-ECE2 readthrough transcript protein

**功能**: Converts big endothelin-1 to endothelin-1. May also have methyltransferase activity (By similarity). May play a role in amyloid-beta processing (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR024079 |
| InterPro | IPR041698 |
| InterPro | IPR000718 |
| InterPro | IPR018497 |
| InterPro | IPR042089 |
| InterPro | IPR008753 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-P0DPD8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/EEF1AKMT4-ECE2

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IDE | STRING | 446 |
| APP | STRING | 457 |
| ACE | STRING | 403 |
| ICE1 | STRING | 505 |
| PRKCE | STRING | 491 |
| EDNRA | STRING | 761 |
| EDN3 | STRING | 826 |
| EEF1AKMT2 | STRING | 416 |
| EDN2 | STRING | 749 |
| EDNRB | STRING | 591 |
| EDN1 | STRING | 758 |
| ECE2-2 | STRING | 447 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000284917-EEF1AKMT4-ECE2

![](https://images.proteinatlas.org/62215/1148_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/62215/1148_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/62215/1192_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/62215/1192_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/62215/1106_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/62215/1106_A6_2_red_green.jpg)
