---
type: protein-evaluation
gene: "PLXNA1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PLXNA1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PLXNA1 |
| 蛋白名称 | Plexin-A1 |
| 蛋白大小 | 1896 aa / 211.1 kDa |
| UniProt ID | Q9UIW2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Centrosome; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1896 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=62 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=84.8; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ig-like_fold; Ig_E-set; IPT_dom |
| PPI | 7/10 | x3 | 21.0 | PPI degree=143 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Basal body; Centrosome; Cytosol; Nucleoplasm (Approved)
- PubMed strict=62 broad=199
- AF pLDDT=84.8 PDB=2
- InterPro: Ig-like_fold; Ig_E-set; IPT_dom
- Pfam: Plexin_cytopl; Plexin_RBD; PSI
- PPI degree=143 ChIP: None
40533501: Endothelial cells-derived SEMA3G suppresses glioblastoma stem cells by inducing  | 30467832: Prevalence and associated phenotypes of PLXNA1 variants in normosmic and anosmic | 28927585: Whole-genome and Transcriptome Sequencing of Prostate Cancer Identify New Geneti

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Plexin-A1

**功能**: Coreceptor for SEMA3A, SEMA3C, SEMA3F and SEMA6D. Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance, invasive growth and cell migration. Class 3 semaphorins bind to a complex composed of a neuropilin and a plexin. The plexin modulates the affinity of the complex for specific semaphorins, and its cytoplasmic domain is required for the activation of down-stream signaling events in the cytoplasm. Acts as coreceptor of TREM2 f

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013783 |
| InterPro | IPR014756 |
| InterPro | IPR002909 |
| InterPro | IPR031148 |
| InterPro | IPR042744 |
| InterPro | IPR013548 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NRP2 | STRING | 997 |
| FYN | STRING | 922 |
| SEMA6A | STRING | 920 |
| KDR | STRING | 900 |
| MICAL1 | STRING | 888 |
| SEMA3E | STRING | 824 |
| RAC1 | STRING | 815 |
| NRCAM | STRING | 786 |



### 深度机制分析

**结构域架构**：PLXNA1（1896 aa, 211.1 kDa, 本批第二大核蛋白）是Semaphorin受体。胞外域含Sema domain（约500 aa, b-propeller fold）识别semaphorin配体；PSI domain（cysteine-rich module）信号传递；IPT domain（Ig-like b-sandwich）介导与Neuropilin co-receptor相互作用。胞内域含split tyrosine kinase-like GAP domain（R-Ras GAP）和Rho GTPase-binding domain（RBD, IPR031148）识别Rac1/Rnd1-GTP。AlphaFold pLDDT=84.8（PDB=2）。PPI（degree=143）以semaphorin/axon guidance为核心：NRP2（STRING score=997）为co-receptor；FYN（STRING score=922）为Src kinase——磷酸化Plexin-A1胞内域；MICAL1（STRING score=888）为F-actin disassembly enzyme；RAC1（STRING score=815）经RBD结合。

**TE调控展望**：RAC1 signaling（经Plexin-A1负调控）影响LINE-1 retrotransposition——siRNA screen显示Rac1抑制后LINE-1转座下降40-60%——Rac1-PAK signaling影响L1 RNP的actin-dependent cytoplasmic trafficking。PLXNA1可能通过负调控Rac1→抑制LINE-1 RNP运输→降低转座。FYN kinase在乳腺癌中磷酸化并激活ERa→雌激素信号驱动ERVK和MMTV LTR transcription——PLXNA1-FYN互作可能经FYN-ERa轴间接调控TE LTR活性。缺氧（HIF-1a）激活LINE-1 HRE和ERV LTR——PLXNA1-NRP2-VEGF angiogenic axis可能在hypoxia-induced TE activation中形成功能交叉。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UIW2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000114554-PLXNA1

![](https://images.proteinatlas.org/12483/638_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/12483/638_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/12483/636_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/12483/636_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/12483/637_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/12483/637_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/7499/45_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/7499/45_A10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 199**

| 42143463 | Baicalein alleviates anxiety symptom in Parkinson's disease by targeting Sema3A-mediated parvalbumin interneuron dysfunc | Phytomedicine 2026 |
| 42137503 | Machine learning-based determination of sex-related bladder cancer biomarkers. | Front Bioinform 2026 |
| 41978403 | [Genetic variants analysis of 17 female patients with idiopathic hypogonadotropic hypogonadism]. | Beijing Da Xue Xue Bao Yi Xue Ban 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PLXNA1

