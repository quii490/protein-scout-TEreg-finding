---
type: protein-evaluation
gene: "SPINK9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPINK9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPINK9 |
| 蛋白名称 | Serine protease inhibitor Kazal-type 9 |
| 蛋白大小 | 86 aa / 9.8 kDa |
| UniProt ID | Q5DT21 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 86 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=91.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kazal-type_SerProtInhib; Kazal_dom; Kazal_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=3 broad=13
- AF pLDDT=91.1 PDB=0
- InterPro: Kazal-type_SerProtInhib; Kazal_dom; Kazal_dom_sf
- Pfam: Kazal_1
- PPI degree=5 ChIP: None
41616039: Identification of deleterious missense variants of serine peptidase inhibitor Ka | 22505519: Characterization of SPINK9, a KLK5-specific inhibitor expressed in palmo-plantar | 19190773: Identification of lympho-epithelial Kazal-type inhibitor 2 in human skin as a ka

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Serine protease inhibitor Kazal-type 9

**功能**: Serine protease inhibitor which specifically inhibits KLK5. May contribute to the regulation of the desquamation process in skin by inhibiting KLK5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050159 |
| InterPro | IPR002350 |
| InterPro | IPR036058 |
| InterPro | IPR001239 |
| Pfam | PF00050 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

SPINK9（Serine protease inhibitor Kazal-type 9）是本评估队列中分子量最小的蛋白：仅86个氨基酸（9.8 kDa），几乎完全由一个Kazal型丝氨酸蛋白酶抑制结构域构成。结构域注释包括：Kazal-type_SerProtInhib（IPR050159）、Kazal_dom（IPR002350）、Kazal_dom_sf（IPR036058），Pfam为Kazal_1（PF00050）。Kazal结构域采用典型的α/β折叠，含有一个反应位点环（reactive site loop, RSL），通过类似底物的方式与靶蛋白酶活性位点结合，但切割极为缓慢，从而实现对丝氨酸蛋白酶的竞争性抑制。pLDDT=91.1是本批次中最高的结构预测分数之一，表明这个86 aa的单结构域蛋白具有极高的折叠稳定性和结构有序度。

SPINK9的经典功能定位于皮肤角质层的表皮分化过程。作为KLK5（激肽释放酶相关肽酶5）的特异性抑制剂，SPINK9通过抑制KLK5来调控皮肤脱屑（desquamation）过程（PMID 22505519, PMID 19190773）。KLK5是表皮中关键的丝氨酸蛋白酶，直接切割角质桥粒蛋白（corneodesmosomal proteins），驱动角质细胞的脱落。SPINK9作为一个微调的刹车来避免过度脱屑，维护皮肤屏障的完整性。然而，HPA免疫荧光显示Nucleoplasm; Vesicles (Approved)——核质定位对一个分泌型蛋白酶抑制剂来说极为意外。

对于SPINK9的核质定位，可能的机制包括：（1）虽然SPINK9含有信号肽用于分泌途径，但在特定条件下可能发生分泌途径逃逸或内吞后通过核孔扩散进入核质（其9.8 kDa的小分子量低于被动扩散阈值约40-60 kDa，理论上可自由穿越核孔）；（2）SPINK9可能在核内抑制核定位的KLK5或类似蛋白酶——值得注意的是，KLK家族中的一些成员（如KLK4）已报道在核内具有功能，参与染色质蛋白的蛋白水解加工。然而，PPI degree=5的低互作度（仅TRPC6和SGTA）限制了进一步推理。

从TE调控角度，SPINK9的潜力非常有限。其TE调控相关性如果存在，仅能通过极间接的机制：KLK5在肿瘤微环境中参与蛋白酶激活受体（PAR）信号，影响EMT和细胞外基质重塑——这些过程与全局表观遗传重编程和TE去抑制存在间接关联。但其核质定位的功能意义和TE调控中是否发挥任何角色，需要先回答一个更基本的问题：SPINK9在核内究竟做什么？PubMed strict=3篇文献的极端新颖性表明该蛋白的核内功能完全未被探索。鉴于其极小的分子量和极高的结构置信度，SPINK9可能更适合作为结构生物学工具（如蛋白结晶学对照）而非TE调控研究的首要候选。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRPC6 | BioGRID | 0 |
| SGTA | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5DT21-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204909-SPINK9

![](https://images.proteinatlas.org/38288/455_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/38288/455_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/38288/1842_H2_64_red_green.jpg)
![](https://images.proteinatlas.org/38288/1842_H2_65_red_green.jpg)
![](https://images.proteinatlas.org/38288/452_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/38288/452_G2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 13**

| 41616039 | Identification of deleterious missense variants of serine peptidase inhibitor Kazal type 2 gene and their impact on KAZA | J Biomol Struct Dyn 2026 |
| 36882550 | Special transcriptome landscape and molecular prognostic signature of non-smoking head and neck cancer patients. | Funct Integr Genomics 2023 |
| 36175575 | Identification of novel differentially expressed genes in type 1 diabetes mellitus complications using transcriptomic pr | Sci Rep 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SPINK9

