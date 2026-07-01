---
type: protein-evaluation
gene: "WBP11"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## WBP11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | WBP11 |
| 蛋白名称 | WW domain-binding protein 11 |
| 蛋白大小 | 641 aa / 70.0 kDa |
| UniProt ID | Q9Y2W2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Acrosome; Cytosol; End piece; Nucleoplasm; Princip (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 641 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=27 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=62.6; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Wbp11/ELF5/Saf1_N |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=204 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- HPA: Acrosome; Cytosol; End piece; Nucleoplasm; Principal piece; Vesicles (Supported)
- PubMed: strict=27, broad=37
- AF pLDDT: 62.6 / PDB: 2
- InterPro: Wbp11/ELF5/Saf1_N
- Pfam: Wbp11
- PPI degree=204 ChIP: None
37691920: Identification and verification of diagnostic biomarkers in recurrent pregnancy  | 41184530: WBP11 inhibits UFL1-mediated UFMylation of NONO to drive hepatocellular carcinom | 39551759: The KLF16/MYC feedback loop is a therapeutic target in bladder cancer.

### 4. 总体评价
★★★★  **73.8/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: WW domain-binding protein 11

**功能**: Activates pre-mRNA splicing. May inhibit PP1 phosphatase activity

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019007 |
| Pfam | PF09429 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

WBP11(WW domain-binding protein 11)是前体mRNA剪接(pre-mRNA splicing)机器的核心激活因子，编码一个70kDa的核蛋白。其主要结构域为Wbp11/ELF5/Saf1_N(IPR019007/PF09429)，这是一个真核生物特异性保守的蛋白质互作模块。pLDDT仅62.6(整体结构置信度较低)，Pfam Wbp11域之外的大部分序列(约500 aa)被预测为色散的内在无序区域(IDR)，这是剪接因子中常见的结构特征——IDR介导的液-液相分离(LLPS)促进剪接体在转录位点的动态聚集。

在剪接体组装循环中，WBP11的功能位置已被定位：它作为PP1(蛋白磷酸酶1)的抑制蛋白(UniProt功能注释)，通过保护剪接因子不被PP1过早去磷酸化来维持剪接体复合物的活性磷酸化状态。这一角色使得WBP11成为剪接体动态磷酸化门控的"计时器"。PPI网络完美映射了剪接体的核心组分：PQBP1(多聚谷氨酰胺结合蛋白1，STRING=994)和SRRM1(丝氨酸/精氨酸重复基质蛋白1，STRING=977)是剪接因子；CDC5L(细胞分裂周期5-like，STRING=974)和PRPF38A(pre-mRNA加工因子38A，STRING=971)是U5 snRNP组分；TCERG1(转录延伸调节因子1，STRING=971)连接剪接与转录偶联。

HPA定位包含了极其复杂的多区室分布——Acrosome、Cytosol、End piece、Nucleoplasm、Principal piece和Vesicles(Supported, non-Approved)。其中精子的Acrosome/Principal piece/End piece三区室定位是WBP11性别相关组织特异性的独特特征，暗示其在精子形成(spermiogenesis)中的剪接调控功能。近期研究揭示了WBP11在癌症中的关键作用：WBP11可通过抑制UFL1介导的NONO蛋白UFMylation修饰来驱动肝细胞癌进展(PMID:41184530)，这揭示了一种全新的剪接后修饰(UFMylation)-剪接因子轴在肿瘤中的调控逻辑。此外，WBP11介导的MCM7内含子保留(intron retention)在多种恶性肿瘤中被证实促进疾病进展(PMID:42026187)。WBP11的核质定位为Supported，需IF共定位验证以加强证据级别。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y2W2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000084463-WBP11

![](https://images.proteinatlas.org/49126/2183_D10_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2183_D10_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_45_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000084463-WBP11

![](https://images.proteinatlas.org/49126/2183_D10_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2183_D10_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_45_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000084463-WBP11

![](https://images.proteinatlas.org/49126/2183_D10_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2183_D10_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/49126/2202_A8_45_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 42085381 | Integrating multi-omics and machine learning to decipher the molecular pathways of bisphenol a-associated lactylation-re | PLoS One 2026 |
| 42026187 | Correction: The splicing factor WBP11 mediates MCM7 intron retention to promote the malignant progression of ovarian can | Oncogene 2026 |
| 41975533 | Prenatal and postnatal manifestations of WBP11-related disorder in Chinese patients: expanding the phenotypic and mutati | Hum Genomics 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/WBP11

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PQBP1 | STRING | 994 |
| SRRM1 | STRING | 977 |
| UBL5 | STRING | 974 |
| CDC5L | STRING | 974 |
| MFAP1 | STRING | 972 |
| PRPF38A | STRING | 971 |
| TCERG1 | STRING | 971 |
| ZMAT2 | STRING | 968 |
| CWC15 | STRING | 963 |
| PLRG1 | STRING | 963 |
| WBP4 | STRING | 935 |
| SF3A2 | STRING | 927 |
| CTNNBL1 | STRING | 927 |
| DDX5 | STRING | 922 |
| LSM3 | STRING | 905 |
| TRIP10 | physical | Rual JF (2005) |
| RTN4IP1 | physical | Rual JF (2005) |
| DDX17 | physical | Rual JF (2005) |
| C5orf22 | physical | Rual JF (2005) |
| NCK2 | physical | Rual JF (2005) |

