---
type: protein-evaluation
gene: "BCL2L2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## BCL2L2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | BCL2L2 |
| 蛋白名称 | Bcl-2-like protein 2 |
| 蛋白大小 | 193 aa / 20.7 kDa |
| UniProt ID | Q92843 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 193 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=99 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=81.2; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Apop_reg_BclW; Bcl-2-like_sf; Bcl-2_BH1-3 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=87 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Uncertain)
- PubMed strict=99 broad=321
- AF pLDDT=81.2 PDB=5
- InterPro: Apop_reg_BclW; Bcl-2-like_sf; Bcl-2_BH1-3
- Pfam: Bcl-2; BH4
- PPI degree=87 ChIP: None
36272652: Sequence and expression regulation of the BCL2L2 gene in pigs. | 35894779: Novel read-through fusion transcript Bcl2l2-Pabpn1 in glioblastoma cells. | 24467740: The role of apoptosis in megakaryocytes and platelets.

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Bcl-2-like protein 2

**功能**: Promotes cell survival. Blocks dexamethasone-induced apoptosis. Mediates survival of postmitotic Sertoli cells by suppressing death-promoting activity of BAX

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013280 |
| InterPro | IPR036834 |
| InterPro | IPR046371 |
| InterPro | IPR026298 |
| InterPro | IPR002475 |
| InterPro | IPR020717 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PMAIP1 | STRING | 998 |
| PABPN1 | STRING | 989 |
| MCL1 | STRING | 988 |
| BECN1 | STRING | 987 |
| BCL2L1 | STRING | 933 |
| BAX | STRING | 930 |
| PABPN1L | STRING | 918 |
| BCL2L10 | STRING | 880 |


### 深度机制分析

BCL2L2（193 aa, pLDDT=79.1）是Bcl-2家族的抗凋亡成员Bcl-w。其结构域包含所有Bcl-2家族共有的BH1-BH4基序，通过疏水沟槽结合促凋亡蛋白（如BAX, BAK, BIM）以抑制其线粒体外膜通透化活性。BCL2L2的核质定位（Uncertain, 加权评分68.3）暗示其在非凋亡条件下的核内功能。Bcl-2家族蛋白在核内的研究主要集中于核膜定位和核内凋亡信号调控——BCL2L2可能通过结合核内BAX防止核被膜破裂，间接维持核内染色质结构完整性。从TE调控角度，线粒体外膜通透化（MOMP）释放的mtDNA和凋亡因子caspase非依赖性地促进IFN-I和TE转录，而BCL2L2通过维持线粒体完整性限制此通路。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q92843-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/BCL2L2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000129473-BCL2L2

![](https://images.proteinatlas.org/48740/798_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/48740/798_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/48740/791_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/48740/791_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/48740/794_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/48740/794_D11_3_red_green.jpg)

### PubMed

**Count: 321**

| PMID | Title |
|---|---|
| 42099139 | Unveiling the Anti-cancer Potential of Vulpinic Acid: A Selective Therapeutic Agent Against Oral Squamous Cell Carcinoma. |
| 41820464 | Mitochondrial apoptosis gene-based pathomics for ovarian cancer prognosis. |
| 41743908 | Suppression of miR-195 attenuates oxygen-glucose deprivation/reperfusion-induced BBB destruction, possibly via targeting BCL2L2. |
| 41677970 | Identification of mitochondrial associated genes as diagnostic biomarkers for basal cell carcinoma: Comprehensive bioinformatics analysis and experime |
| 41633477 | Extracellular vesicles derived from HSCs transmitted circPVT1 to ameliorate oxidative damage to hepatocytes by targeting the miR-125b-5p/BCL2L2 signal |


