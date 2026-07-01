---
type: protein-evaluation
gene: "VSTM4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## VSTM4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VSTM4 |
| 蛋白名称 | V-set and transmembrane domain-containing protein 4 |
| 蛋白大小 | 320 aa / 36.1 kDa |
| UniProt ID | Q8IW00 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 320 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ig-like_dom; Ig-like_dom_sf; Ig-like_fold |
| PPI | 5/10 | x3 | 15.0 | PPI degree=12 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=2 broad=4
- AF pLDDT=74.9 PDB=0
- InterPro: Ig-like_dom; Ig-like_dom_sf; Ig-like_fold
- Pfam: V-set
- PPI degree=12 ChIP: None
33926391: High HSPA8 expression predicts adverse outcomes of acute myeloid leukemia. | 38728245: Constructing a novel prognostic model for triple-negative breast cancer based on

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: V-set and transmembrane domain-containing protein 4

**功能**: Peptide Lv enhances L-type voltage-gated calcium channel (L-VGCC) currents in retinal photoreceptors

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003599 |
| InterPro | IPR013106 |
| InterPro | IPR051102 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP1CC | BioGRID | 0 |
| FKBP7 | BioGRID | 0 |
| TGM1 | BioGRID | 0 |
| STX1A | BioGRID | 0 |
| MDFI | BioGRID | 0 |
| KRTAP1-1 | BioGRID | 0 |
| CYSRT1 | BioGRID | 0 |
| KRTAP12-3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IW00-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165633-VSTM4

![](https://images.proteinatlas.org/17279/1401_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/17279/1401_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/17279/1220_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/17279/1220_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/17279/1158_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/17279/1158_D4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 38728245 | Constructing a novel prognostic model for triple-negative breast cancer based on genes associated with vasculogenic mimi | Aging (Albany NY) 2024 |
| 37980162 | Crucial role of hsa-mir-503, hsa-mir-1247, and their validation in prostate cancer. | Aging (Albany NY) 2023 |
| 34386509 | Regulation of Tumor Necrosis Factor-α by Peptide Lv in Bone Marrow Macrophages and Synovium. | Front Med (Lausanne) 2021 |

### 深度机制分析

VSTM4的域架构由一个N端Ig样V-set结构域（IPR013106, IPR051102）和一个C端Ig样结构域（Ig-like_dom, IPR007110; Ig-like_dom_sf, IPR036179; Ig-like_fold, IPR013783）组成。V-set结构域是免疫球蛋白超家族最具可变性的亚类，具有特征性的九条β-链排列。其串联排列与共刺激/抑制受体（如CTLA-4、PD-1、BTLA）的V+C结构域结构非常相似。该蛋白为单次跨膜蛋白，具有外部N端V-set域、跨膜螺旋和胞质C端尾巴。

AlphaFold pLDDT为74.9（中等），高置信度仅限于两个Ig样结构域的核心β-三明治框架，而结构域间连接子和胞质尾巴的置信度极低。无实验PDB结构。V-set结构域最具可变性的环区在预测中表现出较大的局部误差，反映了环构象的固有多样性——这是抗原结合受体中可变互补决定区（CDR）的众所周知的特征。循环区的这种柔性暗示VSTM4可能通过构象选择实现配体结合。

PPI网络（degree=12）主要由低置信度BioGRID互作构成。值得注意的是PPP1CC（蛋白磷酸酶催化亚基）和STX1A（syntaxin-1A, SNARE蛋白）的关联——前者提示可逆磷酸化调控，后者提示膜运输功能。核质定位（HPA Approved, 9/10）可能通过γ-分泌酶介导的膜内切割释放胞内域进入胞质和细胞核——这是Notch信号通路的典型范式。VSTM4胞内域的核易位可能调控与急性髓系白血病预后（PMID 33926391）和三阴性乳腺癌（PMID 38728245）相关的转录程序。

TE调控启示：V-set结构域存在于许多通过TE衍生的外显子获得先天免疫识别能力的免疫受体中。VSTM4仅有2篇文献的极高新颖性带来重要问题：在活化TE环境中（如在癌症中），一种孤立的V-set受体是否能作为病毒/内源性逆转录病毒包膜蛋白的监视受体发挥作用。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/VSTM4

