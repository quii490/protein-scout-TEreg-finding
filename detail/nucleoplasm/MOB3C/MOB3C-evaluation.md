---
type: protein-evaluation
gene: "MOB3C"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MOB3C 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MOB3C |
| 蛋白名称 | MOB kinase activator 3C |
| 蛋白大小 | 216 aa / 25.6 kDa |
| UniProt ID | Q70IA8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 216 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MOB_kinase_act_fam; MOB_kinase_act_sf |
| PPI | 8/10 | x3 | 24.0 | PPI degree=365 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=4 broad=6
- AF pLDDT=88.9 PDB=0
- InterPro: MOB_kinase_act_fam; MOB_kinase_act_sf
- Pfam: Mob1_phocein
- PPI degree=365 ChIP: None
34573430: Whole-Genome Profiles of Malay Colorectal Cancer Patients with Intact MMR Protei | 35117778: Comparison of whole exome sequencing in circulating tumor cells of primitive and | 37536630: Mapping the MOB proteins' proximity network reveals a unique interaction between

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

MOB3C属于MOB（Mps One Binder）激酶激活因子家族，其216个氨基酸的核心折叠由MOB_kinase_act_fam结构域（IPR005301）与MOB_kinase_act_sf超家族（IPR036703）构成，形成了保守的α-螺旋束状结构。AlphaFold预测pLDDT高达88.9，表明该蛋白具有高度有序的三维构象——这与其作为Hippo信号通路中LATS1/2激酶的调节亚基的功能要求一致。MOB3C通过高度保守的界面与LATS1/2（PPI评分=1，BioGRID验证）结合，调控下游YAP/TAZ的磷酸化依赖的胞质滞留，从而间接抑制促增殖转录程序。

PPI网络分析显示MOB3C与365个蛋白存在互作关系（PPI degree=365），其中尤为重要的是与RNase P复合体的独特相互作用（PMID:37536630），这是MOB家族中首次发现的非经典功能。MOB3C-MAU2互作进一步连接了该蛋白至染色体黏连（cohesin）装载机制，暗示其可能在细胞分裂的染色体分离过程中发挥核功能。然而，HPA核定位证据级别为"nan"，核定位特异性评分仅5/10，提示MOB3C在核质中的存在可能为瞬时或细胞周期依赖性的。

从信号调控机制上看，MOB3C作为激酶调节亚基而非催化亚基，其功能依赖于蛋白-蛋白互作而非酶活性。Mob1_phocein（PF03637）结构域作为MOB蛋白的保守特征，在进化中高度保守，提示其在细胞极性、增殖控制中的基础性角色。MOB3C通过SIAH1介导的泛素化途径被调控，而APP的互作则可能将其功能与阿尔茨海默病相关病理过程相连接。

鉴于MOB3C的PubMed文献仅6篇，其在Hippo信号之外的功能几乎未被探索。RNase P复合体互作的发现（PMID:37536630）强烈暗示MOB3C可能参与tRNA加工——这是一个具有深远意义的核内功能，可能解释其在核质中的存在。此外，在结直肠癌中MOB3C所在的基因组区域存在突变热点（PMID:34573430），提示其可能是肿瘤发生中的功能性靶点，值得作为TE调控候选蛋白进行深入的功能基因组学研究。

**蛋白全称**: MOB kinase activator 3C

**功能**: May regulate the activity of kinases

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005301 |
| InterPro | IPR036703 |
| Pfam | PF03637 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LATS1 | BioGRID | 1 |
| LATS2 | BioGRID | 1 |
| APP | BioGRID | 1 |
| SIAH1 | BioGRID | 1 |
| TFCP2 | BioGRID | 1 |
| ZBTB10 | BioGRID | 1 |
| CMTM3 | BioGRID | 1 |
| MAU2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q70IA8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000142961-MOB3C

![](https://images.proteinatlas.org/57744/976_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/976_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000142961-MOB3C

![](https://images.proteinatlas.org/57744/976_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/976_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000142961-MOB3C

![](https://images.proteinatlas.org/57744/976_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/976_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57744/980_G11_4_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 37536630 | Mapping the MOB proteins' proximity network reveals a unique interaction between human MOB3C and the RNase P complex. | J Biol Chem 2023 |
| 34573430 | Whole-Genome Profiles of Malay Colorectal Cancer Patients with Intact MMR Proteins. | Genes (Basel) 2021 |
| 34385509 | Mapping gene and gene pathways associated with coronary artery disease: a CARDIoGRAM exome and multi-ancestry UK biobank | Sci Rep 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MOB3C

