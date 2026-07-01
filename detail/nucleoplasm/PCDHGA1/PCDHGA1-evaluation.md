---
type: protein-evaluation
gene: "PCDHGA1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA1 |
| 蛋白名称 | Protocadherin gamma-A1 |
| 蛋白大小 | 931 aa / 101.2 kDa |
| UniProt ID | Q9Y5H4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 931 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=74.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=3 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=9 broad=10
- AF pLDDT=74.8 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=3 ChIP: None
32814111: In Colorectal Cancer Cells With Mutant KRAS, SLC25A22-Mediated Glutaminolysis Re | 34895303: Genome-wide methylation patterns in Marfan syndrome. | 34704810: Identification and Prognostic Value Exploration of Cyclophosphamide (Cytoxan)-Ce

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A1

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PCDHGA1（Protocadherin gamma-A1）属于protocadherin gamma基因簇成员。该蛋白包含经典的钙粘蛋白结构域架构：InterPro注释显示其含有Cadherin-like_dom（IPR002126）、Cadherin-like_sf（IPR015919）、Cadherin_C（IPR032455）以及额外的IPR031904和IPR020894（Cadherin conserved site）结构域，Pfam匹配Cadherin（PF00028）、Cadherin_2和Cadherin_C_2（PF16459）。AlphaFold v6预测整体pLDDT=74.8，931个氨基酸的大蛋白中钙粘蛋白胞外域（EC）重复区域通常折叠良好，但胞内域可能包含较多无序区域。PAE图（见上述嵌入图像）可揭示EC域间及跨膜区-胞内域的折叠独立性。

钙粘蛋白超家族传统上作为钙依赖性细胞粘附分子发挥作用，主要在神经元连接的建立和维持中起作用。PCDHGA1被注释为"潜在的钙依赖性细胞粘附蛋白，可能参与脑内特定神经元连接的建立和维持"（UniProt功能注释）。然而，在本次评估中HPA IF显示PCDHGA1定位于胞质溶胶、核质、质膜和囊泡（Uncertain），这种混合定位模式提示该蛋白可能具有超越经典细胞粘附的非经典功能。

PPI网络高度稀疏：STRING和BioGRID仅鉴定到PARK2（Parkin E3泛素连接酶）和HIST1H2BD（组蛋白H2B）两个互作伙伴。与PARK2的互作暗示PCDHGA1可能参与线粒体自噬或泛素化降解途径的调控，而与组蛋白H2B的潜在关联（尽管评分较低）则为染色质层面的功能提供了微弱线索。

PubMed严格检索仅9篇文献（broad=10篇），研究方向主要集中于DNA甲基化和肿瘤相关基因表达谱（PMID:42362890、PMID:41260607、PMID:40343304、PMID:35968320、PMID:35574540）。新颖性评分达10/10（≤20篇），但其核定位证据仅为7/10（HPA Uncertain），且缺乏明确的核定位信号（NLS）或DNA/染色质结合结构域是评估其TE调控潜力的主要制约因素。若核质定位得到独立验证（如核质分离Western blot或核定位信号突变分析），则其作为非经典核钙粘蛋白的调控机制（类似于δ-catenin和p120-catenin的核功能）值得深入探究。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PARK2 | BioGRID | 0 |
| HIST1H2BD | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5H4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA1

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204956-PCDHGA1

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed

**Count: 10**

| PMID | Title |
|---|---|
| 42362890 | Meta-analysis of DNA methylation aging signatures in 17 human tissues. |
| 41260607 | MYB Alterations in Angiocentric Gliomas. |
| 40343304 | DNA methylation in peripheral blood leukocytes in late onset Alzheimer's disease. |
| 35968320 | A novel 8-gene panel for prediction of early biochemical recurrence in patients with prostate cancer after radical prostatectomy. |
| 35574540 | Genetic Alteration Analysis of IDH1, IDH2, CDKN2A, MYB and MYBL1 in Pediatric Low-Grade Gliomas. |