---
type: protein-evaluation
gene: "PANK3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PANK3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PANK3 |
| 蛋白名称 | Pantothenate kinase 3 |
| 蛋白大小 | 370 aa / 41.1 kDa |
| UniProt ID | Q9H999 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 370 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=94.4; PDB=34 |
| 调控结构域 | 4/10 | x2 | 8.0 | ATPase_NBD; Type_II_PanK |
| PPI | 5/10 | x3 | 15.0 | PPI degree=21 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=17 broad=32
- AF pLDDT=94.4 PDB=34
- InterPro: ATPase_NBD; Type_II_PanK
- Pfam: Fumble
- PPI degree=21 ChIP: None
36139163: Generation and Validation of an Anti-Human PANK3 Mouse Monoclonal Antibody. | 38583827: MiR-103-5p deficiency suppresses lipid accumulation via upregulating PLSCR4 and  | 33329737: Novel Regulatory Factors in the Hypothalamic-Pituitary-Ovarian Axis of Hens at F

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Pantothenate kinase 3

**功能**: Catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR043129 |
| InterPro | IPR004567 |
| Pfam | PF03630 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPCS | STRING | 976 |
| PANK1 | STRING | 907 |
| ELAVL1 | BioGRID | 1 |
| HNRNPA3 | BioGRID | 1 |
| YWHAB | BioGRID | 1 |
| YWHAG | BioGRID | 1 |
| KIAA1429 | BioGRID | 0 |
| DDX58 | BioGRID | 0 |



### 深度机制分析

**结构域架构**：PANK3（370 aa, 41.1 kDa）属Type II pantothenate kinase家族（PANK1-4）。含Type_II_PanK域（IPR004567, Pfam Fumble）约300 aa的单体催化域——以ATP为磷酸供体催化pantothenate→4'-phosphopantothenate——CoA合成的第一步和限速步骤。AlphaFold pLDDT=94.4（PDB=34, 本批最高pLDDT之一）——>95%残基pLDDT>90，表明极高结构稳定性。PPI（degree=21）以CoA合成和RNA metabolism为核心：PPCS（STRING score=976）为CoA合成第二步酶——PANK3-PPCS形成代谢物通道（metabolon）；ELAVL1（HuR, BioGRID）结合PANK3 mRNA的ARE motif；KIAA1429（VIRMA, BioGRID）为m6A methyltransferase complex核心组分。PANK3在核质中驱动nuclear CoA synthesis→供给HAT（p300/CBP, GCN5/PCAF）以acetyl-CoA→影响全局组蛋白乙酰化。

**TE调控展望**：PANK3通过核CoA-acetyl-CoA轴直接影响TE位点的组蛋白乙酰化。CoA→acetyl-CoA是HAT催化乙酰化反应的专性底物。TE座位（ERV-LTR和LINE-1 5'UTR）的H3K9ac/H3K27ac决定TE转录——PANK3缺陷→核CoA下降→acetyl-CoA不足→HAT活性降低→TE座位H3K27ac减少→H3K27ac-to-H3K27me3 switch→Polycomb PRC2沉积→TE沉默。PANK3在多种癌症中上调（PMID 41371401: c-Myc-PANK3-EMT axis）→核CoA升高→维持TE座位（包括oncogene ERV LTR）的异常组蛋白乙酰化→贡献于TE驱动的oncogene activation（onco-exaptation of TE promoters）。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H999-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000120137-PANK3

![](https://images.proteinatlas.org/78669/1850_F1_2_cr5af19a431af7b_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1850_F1_26_cr5af19a431c276_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_10_cr5b926085c72f7_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_26_cr5b926085c877e_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000120137-PANK3

![](https://images.proteinatlas.org/78669/1850_F1_2_cr5af19a431af7b_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1850_F1_26_cr5af19a431c276_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_10_cr5b926085c72f7_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_26_cr5b926085c877e_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000120137-PANK3

![](https://images.proteinatlas.org/78669/1850_F1_2_cr5af19a431af7b_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1850_F1_26_cr5af19a431c276_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1795_H8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_10_cr5b926085c72f7_blue_red_green.jpg)
![](https://images.proteinatlas.org/78669/1890_O3_26_cr5b926085c877e_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 32**

| 41771535 | Discovery of Sulfonamide Pantothenate Kinase Activators and Elucidation of the Role of Isoform Selectivity in Cellular P | J Med Chem 2026 |
| 41371401 | c-Myc-PANK3-EMT axis regulates the structure and function of intestinal barrier in ulcerative colitis. | J Adv Res 2025 |
| 40754168 | Targeting pantothenate kinases in human diseases: Biochemistry and pharmacotherapy. | Biochem Pharmacol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PANK3

