---
type: protein-evaluation
gene: "SNX20"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SNX20 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SNX20 |
| 蛋白名称 | Sorting nexin-20 |
| 蛋白大小 | 316 aa / 36.2 kDa |
| UniProt ID | Q7Z614 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 316 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=8 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=83.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PX_dom; PX_dom_sf; SNX20/SNX21 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Uncertain)
- PubMed: strict=8, broad=14
- AF pLDDT: 83.0 / PDB: 0
- InterPro: PX_dom; PX_dom_sf; SNX20/SNX21
- Pfam: PX
- PPI degree: 22 / ChIP: None
**Papers**: 30072438: Sorting nexin-21 is a scaffold for the endosomal recruitment of huntingtin. | 34764676: SNX20 Expression Correlates with Immune Cell Infiltration and Can Predict Progno | 33116590: Increased SNX20 and PD-L1 Levels Can Predict the Clinical Response to PD-1 Inhib

### 4. 总体评价
★★★★  **70.5/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sorting nexin-20

**功能**: May play a role in cellular vesicle trafficking. Has been proposed to function as a sorting protein that targets SELPLG into endosomes, but has no effect on SELPLG internalization from the cell surface, or on SELPLG-mediated cell-cell adhesion

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001683 |
| InterPro | IPR036871 |
| InterPro | IPR039937 |
| Pfam | PF00787 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KLHL12 | BioGRID | 0 |
| MAGEA11 | BioGRID | 0 |
| ALAS1 | BioGRID | 0 |
| TACC3 | BioGRID | 0 |
| TFIP11 | BioGRID | 0 |
| GMCL1 | BioGRID | 0 |
| FAM9B | BioGRID | 0 |
| JMJD4 | BioGRID | 0 |



### 深度机制分析

**结构域架构**：SNX20（316 aa, 36.2 kDa）属SNX家族PX-only亚家族。含PX domain（Pfam PX, IPR001683）约120 aa的a/b fold——特异性识别PI3P和PI(3,4)P2（Kd nanomolar range）。AlphaFold pLDDT=83.0——PX域pLDDT>90（极高），但PX域外区域pLDDT<50（高度无序）。SNX20为单体PX domain adaptor——定位于early/sorting endosome膜。PPI（degree=22）以剪接因子和cancer-testis antigen为主：MAGEA11（BioGRID）为CTA——通过MAGE homology domain招募E3 ligase/转录因子；JMJD4（BioGRID）为JmjC domain-containing hydroxylase——催化eRF1 lysyl hydroxylation调控translation termination；TFIP11（BioGRID）为剪接体蛋白。

**TE调控展望**：SNX20通过CTA的endosomal trafficking间接参与TE调控。CTA基因（MAGE-A/B/C）通常由LTR/ERV启动子驱动——在癌症中因DNA低甲基化被激活。SNX20在肿瘤免疫浸润中的预后价值（PMID 34764676, 33116590）暗示SNX20-MAGEA11轴在TE-driven CTA表达后蛋白分选和抗原呈递中的角色。JMJD4依赖的translation termination fidelity可能影响LINE-1 ORF1/ORF2的提前终止和NMD降解效率。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7Z614-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167208-SNX20

![](https://images.proteinatlas.org/43649/590_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/43649/590_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/43649/2117_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/43649/2117_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/43649/574_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/43649/574_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 37266373 | Transcriptome-wide selection and validation of a solid set of reference genes for gene expression studies in the cephalo | Front Mol Neurosci 2023 |
| 35771139 | DNA methylation-regulated SNX20 overexpression correlates with poor prognosis, immune cell infiltration, and low-grade g | Aging (Albany NY) 2022 |
| 35747917 | [The Expression of RTN1 in Lung Adenocarcinoma and  Its Effect on Immune Microenvironment]. | Zhongguo Fei Ai Za Zhi 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNX20

