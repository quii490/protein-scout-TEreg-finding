---
type: protein-evaluation
gene: "TRIP10"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TRIP10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TRIP10 |
| 蛋白名称 | Cdc42-interacting protein 4 |
| 蛋白大小 | 601 aa / 68.4 kDa |
| UniProt ID | Q15642 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Vesicles (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 601 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=26 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=79.8; PDB=3 |
| 调控结构域 | 4/10 | ×2 | 8.0 | AH/BAR_dom_sf; F_BAR_dom; FCH_dom |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=111 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Supported)
- PubMed strict=26 broad=86
- AF pLDDT=79.8 PDB=3
- InterPro: AH/BAR_dom_sf; F_BAR_dom; FCH_dom
- Pfam: FCH; HR1_TOCA; SH3_1
- PPI degree=111 ChIP: None
27922008: Defining functional interactions during biogenesis of epithelial junctions. | 40124574: Genetic factors associated with erectile dysfunction- mendelian randomisation an | 21299869: Functional characterization of Trip10 in cancer cell growth and survival.

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cdc42-interacting protein 4

**功能**: Required for translocation of GLUT4 to the plasma membrane in response to insulin signaling (By similarity). Required to coordinate membrane tubulation with reorganization of the actin cytoskeleton during endocytosis. Binds to lipids such as phosphatidylinositol 4,5-bisphosphate and phosphatidylserine and promotes membrane invagination and the formation of tubules. Also promotes CDC42-induced actin polymerization by recruiting WASL/N-WASP which in turn activates the Arp2/3 complex. Actin polymer

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR031160 |
| InterPro | IPR001060 |
| InterPro | IPR057871 |
| InterPro | IPR011072 |
| InterPro | IPR057870 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

TRIP10（Thyroid receptor-interacting protein 10），又名CIP4（Cdc42-interacting protein 4），是F-BAR（Fes/CIP4 homology Bin-Amphiphysin-Rvs）蛋白家族的成员。其结构域架构包含三部分：N端的F-BAR/FCH域（IPR031160/IPR001060 / Pfam FCH），介导膜弯曲感知和诱导；中部的HR1_TOCA域（IPR057871, Pfam HR1_TOCA），负责Cdc42的结合；以及C端的SH3域（IPR057870, Pfam SH3_1），招募下游效应蛋白如WASL/N-WASP。601个氨基酸（68.4 kDa）的分子量和pLDDT=79.8的结构分数指示一个多结构域蛋白，其中F-BAR域形成香蕉形的同源二聚体，感应特定曲率的膜表面。PDB数据库中有3个条目的部分结构信息。

TRIP10的经典功能是作为Cdc42信号通路到肌动蛋白细胞骨架重塑的衔接分子。(1) 通过F-BAR域结合含PI(4,5)P2和磷脂酰丝氨酸的膜，促进膜内陷和小管形成；(2) 通过HR1域结合活性GTP-Cdc42，将Rho家族GTP酶信号转化为膜重塑事件；(3) 通过SH3域招募并激活WASL/N-WASP，后者触发Arp2/3复合体介导的肌动蛋白聚合。这一"膜-信号-细胞骨架"三合一的衔接机制使TRIP10成为内吞作用、细胞迁移和胰岛素刺激下GLUT4转运的关键调控因子。HPA免疫荧光显示Nucleoplasm; Vesicles (Supported)——核质定位再次挑战了对细胞质膜重塑蛋白的既有认知。

PPI网络极为稳健：STRING数据显示WAS（998分）是最高置信度的伙伴——这是Wiskott-Aldrich综合征蛋白，N-WASP的同家族成员，直接激活Arp2/3。FCHO1（963分）、BIN1（859分）、PACSIN2（787分）和ITSN1（752分）均为内吞机制的F-BAR/SH3家族成员，共同形成一个协同作用于膜弯曲和囊泡裂解的核心网络。PACSIN1（746分）作为突触中F-BAR蛋白，和HTT（730分，亨廷顿蛋白，参与囊泡运输）的互作进一步扩展了TRIP10的膜运输调控网络。TSEN2（822分，tRNA剪接内切酶）的互作值得特别关注——它将TRIP10的膜运输功能与RNA加工联系在了一起。

从TE调控角度，TRIP10的潜力主要通过以下两条途径体现。第一，TRIP10-Cdc42-WASP信号轴调控的肌动蛋白聚合在核内具有重要功能——核内肌动蛋白参与染色质重塑复合体的组装、转录延伸和DNA损伤修复。核内G-actin/F-actin的动态平衡直接影响RNA聚合酶II的转录活性和染色质结构，包括异染色质区域的稳态。第二，TRIP10参与的内吞机制调控多种生长因子和细胞因子受体（如胰岛素受体、EGF受体）的信号强度和持续时间——这些信号通路的下游转录因子（如STAT、AP-1、NF-κB）直接调控TE元件的转录。PPI degree=111和STRING网络的稳健性使TRIP10成为信号网络中的关键节点，但其核内功能的具体机制仍待实验阐明。PMID 41404753（J Am Heart Assoc, 2026）关于靶向CIP4-钙调磷酸酶信号小体改善心肌结构和功能的研究，揭示了该蛋白在病理信号整合中的重要性。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WAS | STRING | 998 |
| FCHO1 | STRING | 963 |
| BIN1 | STRING | 859 |
| TSEN2 | STRING | 822 |
| PACSIN2 | STRING | 787 |
| ITSN1 | STRING | 752 |
| PACSIN1 | STRING | 746 |
| HTT | STRING | 730 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q15642-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000125733-TRIP10

![](https://images.proteinatlas.org/41934/814_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/41934/814_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/41934/755_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/41934/755_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/41934/759_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/41934/759_G4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 86**

| 42277639 | Regulatory networks involved in modulating fat deposition in pigs identified by gene co-expression analysis. | BMC Genomics 2026 |
| 41404753 | Targeting of Cdc42-Interacting Protein 4-Calcineurin Signalosomes Improves Cardiac Structure and Function After Myocardi | J Am Heart Assoc 2026 |
| 40462891 | Targeting of CIP4-Calcineurin Signalosomes Improves Cardiac Structure and Function After Myocardial Infarction. | bioRxiv 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TRIP10

