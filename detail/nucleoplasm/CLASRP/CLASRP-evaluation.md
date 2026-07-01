---
type: protein-evaluation
gene: "CLASRP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CLASRP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CLASRP |
| 蛋白名称 | CLK4-associating serine/arginine rich protein |
| 蛋白大小 | 674 aa / 77.2 kDa |
| UniProt ID | Q8N2M8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 674 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=6 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=58.7; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | SWAP; SWAP_N_domain |
| 🔗 PPI | 6/10 | ×3 | 18.0 | PPI degree=91 |
| **加权总分** | | | **129/180** | |
| **归一化总分 (÷1.83)** | | | **71.6/100** | 互证: +2 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Supported) |
| PubMed | strict=6, broad=9 |
| AlphaFold | pLDDT=58.7 |
| PDB | 0 entries |
| InterPro | SWAP; SWAP_N_domain |
| Pfam | DRY_EERY |
| PPI | combined degree=91 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CLASRP（CLK4-associating serine/arginine rich protein）是一个674个氨基酸的核内剪接调控因子，其结构特征为SWAP（Suppressor-of-White-Apricot）结构域（IPR019147/PF09750）与SWAP_N_domain（IPR040397）的串联排列。SWAP结构域在进化中保守于pre-mRNA剪接调控蛋白家族，通过识别特定的剪接增强子或沉默子序列调控可变剪接的选择。AlphaFold预测pLDDT为58.7，提示蛋白含有高比例的无序区——这是富含丝氨酸/精氨酸（SR蛋白家族）的典型特征，这些RS二肽重复形成柔性的骨架，充当剪接体组装过程中的蛋白-蛋白互作界面。

CLASRP在PPI网络（degree=91）中的关键伙伴揭示了其在多个细胞过程中的功能辐射。与CLK4的互作（BioGRID）是命名的由来——CLK（CDC-like kinase）家族激酶通过磷酸化SR蛋白的RS结构域调控剪接因子的核内定位与活性。与DYRK1A（BioGRID）的互作则连接至唐氏综合征关键激酶途径。尤其值得注意的是，CLASRP与微管结合蛋白CLASP1/2（STRING评分=958/959）的强互作——这暗示该核蛋白可能通过CLASP依赖的机制参与有丝分裂过程中的染色体排列或胞质分裂调控。

分子机制层面，CLASRP可能作为剪接体组装过程的平台蛋白：其SWAP结构域识别前体mRNA上的剪接调控基序，同时通过磷酸化依赖的RS结构域-蛋白互作模式招募U1/U2 snRNP剪接体组分。这种双重识别模式使得CLASRP能够"桥接"RNA识别与剪接体组装。LINC00482 lncRNA沉默通过下调CLASRP增强非小细胞肺癌对顺铂的敏感性（PMID:37966662），提示CLASRP的促癌功能可能通过其调控抗凋亡基因可变剪接亚型的生成实现。

CLASRP作为癌基因靶点的转化研究价值正快速上升：在结直肠癌中被鉴定为新的致癌靶点（PMID:37658940），在前列腺癌中与比卡鲁胺耐药相关（PMID:37143720）。这些独立发现共同指向CLASRP作为剪接依赖的肿瘤进展驱动因子。尤为重要的是，其核定位（HPA Supported: Nucleoplasm）、与剪接体核心组分（CLK4、DYRK1A）的直接互作、以及仅6篇PubMed文献的新颖性，使CLASRP成为适合作为TE调控候选蛋白的前沿靶点——可变剪接失调与转座子激活的交叉领域正在成为新的研究热点。

**蛋白全称**: CLK4-associating serine/arginine rich protein

**功能**: Probably functions as an alternative splicing regulator. May regulate the mRNA splicing of genes such as CLK1. May act by regulating members of the CLK kinase family (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040397 |
| InterPro | IPR019147 |
| Pfam | PF09750 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CLASP2 | STRING | 959 |
| CLASP1 | STRING | 958 |
| GCC2 | STRING | 954 |
| KIF2C | STRING | 708 |
| DAB2 | STRING | 703 |
| RHOXF2 | BioGRID | 1 |
| DYRK1A | BioGRID | 1 |
| CLK4 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N2M8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000104859-CLASRP

![](https://images.proteinatlas.org/60469/1045_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/60469/1045_B12_4_red_green.jpg)
![](https://images.proteinatlas.org/60469/1136_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/60469/1136_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/60469/1049_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/60469/1049_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/62455/1127_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/62455/1127_B12_4_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 37966662 | Long noncoding RNA LINC00482 silencing sensitizes non-small cell lung cancer cells to cisplatin by downregulating CLASRP | Funct Integr Genomics 2023 |
| 37658940 | CLASRP oncogene as a novel target for colorectal cancer. | Funct Integr Genomics 2023 |
| 37143720 | Identification of bicalutamide resistance-related genes and prognosis prediction in patients with prostate cancer. | Front Endocrinol (Lausanne) 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CLASRP

