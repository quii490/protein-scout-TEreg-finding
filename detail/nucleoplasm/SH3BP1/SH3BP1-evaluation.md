---
type: protein-evaluation
gene: "SH3BP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3BP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3BP1 |
| 蛋白名称 | SH3 domain-binding protein 1 |
| 蛋白大小 | 701 aa / 75.7 kDa |
| UniProt ID | Q9Y3L3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 701 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=20 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=70.8; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | AH/BAR_dom_sf; BAR_dom; RHG17/44/SH3BP1-like |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=44 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Supported)
- PubMed: strict=20, broad=31
- AF pLDDT: 70.8 / PDB: 2
- InterPro: AH/BAR_dom_sf; BAR_dom; RHG17/44/SH3BP1-like
- Pfam: BAR; RhoGAP
- PPI degree: 44 / ChIP: None
**Papers**: 41249595: Multi-omics unravel heterogeneity of glucose metabolism reprogramming in gastric | 37114076: SH3BP1 Regulates Melanoma Progression Through Race1/Wace2 Signaling Pathway. | 35352878: Reciprocal interactions among Cobll1, PACSIN2, and SH3BP1 regulate drug resistan

### 4. 总体评价
★★★★  **70.5/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 domain-binding protein 1

**功能**: GTPase activating protein (GAP) which specifically converts GTP-bound Rho-type GTPases including RAC1 and CDC42 in their inactive GDP-bound form. By specifically inactivating RAC1 at the leading edge of migrating cells, it regulates the spatiotemporal organization of cell protrusions which is important for proper cell migration (PubMed:21658605). Also negatively regulates CDC42 in the process of actin remodeling and the formation of epithelial cell junctions (PubMed:22891260). Through its GAP ac

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR004148 |
| InterPro | IPR047165 |
| InterPro | IPR008936 |
| InterPro | IPR000198 |
| Pfam | PF03114 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ABL1 | BioGRID | 0 |
| SRC | BioGRID | 0 |
| CRK | BioGRID | 0 |
| TERF1 | BioGRID | 0 |
| POT1 | BioGRID | 0 |
| CD2AP | BioGRID | 0 |
| HECW2 | BioGRID | 0 |
| TRIP10 | BioGRID | 0 |



### 深度机制分析

**结构域架构**：SH3BP1（701 aa, 75.7 kDa）含N端BAR domain（Pfam BAR, IPR004148）和C端RhoGAP domain（Pfam RhoGAP, IPR000198）。BAR domain（约200 aa）为新月形二聚化模块——正电荷富集凹面通过静电作用感知/诱导膜曲率。RhoGAP domain（约150 aa）以保守Arg finger激活Rho GTPase的GTP水解——将GTP-RAC1/CDC42转化为GDP-inactive form→负调控Rac/Cdc42信号。AlphaFold pLDDT=70.8（PDB=2），BAR域pLDDT>80，RhoGAP域pLDDT>85，中间linker为IDR（phosphorylation-regulated hinge）。PPI network（degree=44）以cytoskeletal dynamics和端粒维持为核心：ABL1/SRC（酪氨酸激酶, BioGRID）磷酸化SH3BP1 linker→调控活性；TERF1（TRF1, BioGRID）和POT1（BioGRID）为Shelterin端粒保护复合物组分——连接SH3BP1至端粒维持。

**TE调控展望**：SH3BP1通过端粒维持间接影响TE调控。LINE-1在端粒区域（subtelomeric regions）高度富集，SH3BP1与Shelterin（TERF1/POT1）互作参与端粒保护——端粒脱保护→DDR→p53→基因组不稳定→LINE-1/ERV转录激活。SH3BP1的端粒保护功能可能间接抑制端粒功能障碍诱导的TE激活。CRK-ABL1通路在CML（BCR-ABL1）导致TE激活——SH3BP1作为效应器可能在白血病中调控TE表达。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y3L3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100092-SH3BP1

![](https://images.proteinatlas.org/757/51_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/51_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100092-SH3BP1

![](https://images.proteinatlas.org/757/51_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/51_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100092-SH3BP1

![](https://images.proteinatlas.org/757/51_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/51_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/52_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/757/50_D9_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 31**

| 41558058 | Seco-neokadsuranic acid A antagonizes SH3BP1 to suppress hepatocellular carcinoma progression through PPAR pathway activ | Phytomedicine 2026 |
| 41249595 | Multi-omics unravel heterogeneity of glucose metabolism reprogramming in gastric cancer. | Clin Exp Med 2025 |
| 41003855 | Estimation of genome-wide patterns of homozygosity, heterozygosity and inbreeding in crossbred dairy cattle population i | Trop Anim Health Prod 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3BP1

