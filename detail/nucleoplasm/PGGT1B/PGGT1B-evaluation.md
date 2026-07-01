---
type: protein-evaluation
gene: "PGGT1B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PGGT1B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PGGT1B |
| 蛋白名称 | Geranylgeranyl transferase type-1 subunit beta |
| 蛋白大小 | 377 aa / 42.4 kDa |
| UniProt ID | P53609 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Endoplasmic reticulum; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 377 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=21 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=94.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | GGTase_I_beta; PGGT1B-like; Prenyltrans |
| PPI | 5/10 | x3 | 15.0 | PPI degree=26 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Cytosol; Endoplasmic reticulum; Nucleoplasm (Approved)
- PubMed strict=21 broad=26
- AF pLDDT=94.4 PDB=0
- InterPro: GGTase_I_beta; PGGT1B-like; Prenyltrans
- Pfam: Prenyltrans
- PPI degree=26 ChIP: None
36745138: Genetic and Epigenetic Regulation of the Innate Immune Response to Gout. | 40883609: Pyrin inflammasome-driven erosive arthritis caused by unprenylated RHO GTPase si | 31722972: Mevalonate metabolism-dependent protein geranylgeranylation regulates thymocyte 

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Geranylgeranyl transferase type-1 subunit beta

**功能**: Catalyzes the transfer of a geranyl-geranyl moiety from geranyl-geranyl pyrophosphate to a cysteine at the fourth position from the C-terminus of proteins having the C-terminal sequence Cys-aliphatic-aliphatic-X. Known substrates include RAC1, RAC2, RAP1A and RAP1B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR041960 |
| InterPro | IPR045089 |
| InterPro | IPR001330 |
| InterPro | IPR008930 |
| Pfam | PF00432 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EHD1 | BioGRID | 0 |
| PDE12 | BioGRID | 0 |
| STAT6 | BioGRID | 0 |
| UBA6 | BioGRID | 0 |
| AKTIP | BioGRID | 0 |
| AMMECR1L | BioGRID | 0 |
| HEYL | BioGRID | 0 |
| SRGAP3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P53609-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164219-PGGT1B

![](https://images.proteinatlas.org/30646/930_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/30646/930_D8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 464**

| 42316434 | Bisphosphonate zoledronic acid blocks secretory autophagy and inhibits bone resorptive functions in osteoclasts. | Autophagy 2026 |
| 41892366 | CpG Methylation of Protein Prenyltransferase Genes FNTA, FNTB, PGGT1B and RABGGTA in Cancer Cell Lines. | Epigenomes 2026 |
| 41722442 | FGTI-2734 prevents ERK-mediated resistance and enhances MRTX1133 efficacy in KRAS G12D pancreatic cancer. | Eur J Cancer 2026 |

### 深度机制分析

PGGT1B是I型香叶基香叶基转移酶（GGTase-I）的催化β亚基，催化20碳香叶基香叶基脂质基团向靶蛋白C端CAAX基序中半胱氨酸的共价转移。其结构域架构包括Prenyltrans（IPR001330/PF00432）、GGTase_I_beta（IPR041960）和PGGT1B-like（IPR045089），形成经典的异戊二烯转移酶折叠。AlphaFold pLDDT高达94.4，是整个蛋白集中结构置信度最高的蛋白之一，但无实验PDB结构。认识底物包括RAC1、RAC2、RAP1A和RAP1B等小GTP酶，PPI网络（degree=26）中STAT6和AKTIP的互作提示其可能参与转录因子和端粒相关过程。

核质定位（HPA Approved）是PGGT1B的多维定位特征中最令人意外的——该蛋白传统上被认为定位于胞质和内质网。香叶基香叶基化是RHO家族GTP酶膜锚定和功能激活的先决条件（PMID:31722972），而PGGT1B在核质中的存在提出了一种新颖的可能性：核内小GTP酶的局部异戊二烯化修饰。STAT6作为PGGT1B的潜在核质互作伙伴，进一步暗示PGGT1B可能在核内对转录因子进行脂质修饰，进而影响其核定位和转录活性。

临床上，PGGT1B处于甲羟戊酸途径（mevalonate pathway）的关键下游。双膦酸盐类药物唑来膦酸可阻断分泌性自噬（PMID:42316434），而PGGT1B启动子CpG甲基化在癌细胞系中被鉴定（PMID:41892366），提示表观遗传调控可影响其表达。吡咯炎症小体驱动的侵蚀性关节炎由未异戊二烯化的RHO GTP酶信号引起（PMID:40883609），而KRAS G12D胰腺癌中FGTI-2734（GGTase-I抑制剂）可克服ERK介导的耐药（PMID:41722442），表明PGGT1B是癌症和炎症治疗的潜在靶点。酶活检测与核定位突变体分析将是验证其核质功能的关键。

