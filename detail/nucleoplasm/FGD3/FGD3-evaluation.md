---
type: protein-evaluation
gene: "FGD3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FGD3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FGD3 |
| 蛋白名称 | FYVE, RhoGEF and PH domain-containing protein 3 |
| 蛋白大小 | 725 aa / 79.4 kDa |
| UniProt ID | Q5JSP0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 725 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=25 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=68.6; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | DBL_dom_sf; DH_dom; FGD1-4_PH2 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=13 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=25 broad=40
- AF pLDDT=68.6 PDB=1
- InterPro: DBL_dom_sf; DH_dom; FGD1-4_PH2
- Pfam: FYVE; PH; RhoGEF
- PPI degree=13 ChIP: None
32620603: FGD3 Gene as a New Prognostic Factor in Breast Cancer. | 31645624: Expression of FGD3 gene as prognostic factor in young breast cancer patients. | 30817990: Isolated glucocorticoid deficiency: Genetic causes and animal models.

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: FYVE, RhoGEF and PH domain-containing protein 3

**功能**: Promotes the formation of filopodia. May activate CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. Plays a role in regulating the actin cytoskeleton and cell shape (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR035899 |
| InterPro | IPR000219 |
| InterPro | IPR035941 |
| InterPro | IPR051092 |
| InterPro | IPR011993 |
| InterPro | IPR001849 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BTRC | BioGRID | 0 |
| CDC42 | BioGRID | 0 |
| FGD4 | BioGRID | 0 |
| ARHGAP22 | BioGRID | 0 |
| DDX39A | BioGRID | 0 |
| DNAJB6 | BioGRID | 0 |
| RASGRF2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5JSP0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000127084-FGD3

![](https://images.proteinatlas.org/21018/178_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/21018/178_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/21018/247_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/21018/247_E10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 40**

| 42308175 | Genetic diversity, population structure, and combined detection of selection signatures in Iranian versus Afghan Baluchi | PLoS One 2026 |
| 42271337 | FGD3 as a prognostic and immunological biomarker: a pan-cancer analysis of its role in tumor progression and the immune  | Cancer Cell Int 2026 |
| 42192951 | A Zinc Finger Protein-Based Prognostic Model in Lung Adenocarcinoma Identifies FGD3 as a Marker Associated with Lorlatin | Cancers (Basel) 2026 |

### 深度机制分析

FGD3（725 aa, 79.4 kDa）是一个多结构域RhoGEF（鸟苷酸交换因子），其结构域架构从N端到C端依次为：DH（Dbl同源）结构域（IPR000219）、PH（pleckstrin同源）结构域（IPR011993和IPR001849，含两个PH类似折叠）和FYVE锌指结构域。这种DH-PH-FYVE的三联体组合是含FYVE结构域的GEF家族的典型特征。DH结构域催化GDP/GTP交换以激活Rho家族小GTPase（特别是CDC42），PH结构域辅助膜定位（结合PIPs），而FYVE锌指选择性结合磷脂酰肌醇-3-磷酸（PI3P）引导蛋白至早期内体膜。AlphaFold预测pLDDT=68.6，整体结构含有较多柔性区域，但各折叠结构域的核心置信度尚可。

FGD3的主要生化功能是激活CDC42以促进丝状伪足（filopodia）形成，从而调控肌动蛋白细胞骨架重塑和细胞形态。PPI网络（BioGRID degree=13）中，与BTRC（E3泛素连接酶亚基）和DDX39A（DEAD-box RNA解旋酶）的互作提示FGD3可能在蛋白降解和RNA代谢层面存在额外的非经典功能。与ARHGAP22（RhoGAP，负调控Rho信号）的互作则意味着FGD3的GEF活性可能受到GAP蛋白的拮抗性微调。

HPA将FGD3定位为Cytosol; Nucleoplasm（Approved级别），这与多个GEF蛋白可在胞质和核质之间穿梭的报道一致。核内的RhoGEF可能在核内肌动蛋白动力学、染色质重塑复合物组装或RNA聚合酶II转录调控中发挥作用。文献提示FGD3作为乳腺癌新预后因子（PMID:32620603；PMID:31645624），且近期pan-cancer分析（PMID:42271337）揭示了其在肿瘤进展和免疫微环境中的广泛作用。在TE调控方面，FGD3的核定位可能使其通过以下机制间接影响TE：激活核内CDC42→调控核肌动蛋白网络→影响染色质结构域的空间组织→改变TE位点的表观遗传状态。考虑到FGD3在细胞骨架-核骨架（LINC复合物）信号转导中的潜在位置，核膜-胞质机械力耦合可能成为TE调控的新维度。

