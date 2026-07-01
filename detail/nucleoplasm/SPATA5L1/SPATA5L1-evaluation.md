---
type: protein-evaluation
gene: "SPATA5L1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPATA5L1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPATA5L1 |
| 蛋白名称 | ATPase family gene 2 protein homolog B |
| 蛋白大小 | 753 aa / 80.7 kDa |
| UniProt ID | Q9BVQ7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 753 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=10 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=77.1; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | AAA+_ATPase; AAA_ATPase_domain; AAA_lid_3 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=107 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=10 broad=14
- AF pLDDT=77.1 PDB=2
- InterPro: AAA+_ATPase; AAA_ATPase_domain; AAA_lid_3
- Pfam: AAA; AAA_lid_3
- PPI degree=107 ChIP: None
35688146: Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb | 34626583: Bi-allelic variants in SPATA5L1 lead to intellectual disability, spastic-dystoni | 38554706: The SPATA5-SPATA5L1 ATPase complex directs replisome proteostasis to ensure geno

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SPATA5L1（又称AFG2B）是AAA+ ATPase家族中的染色质相关分子伴侣，其753个氨基酸的蛋白骨架核心由典型的AAA+ ATPase结构域（IPR003593/AAA_ATPase_domain）与AAA_lid_3（IPR041569）调控盖结构域构成。AlphaFold预测pLDDT为77.1，配合2个PDB晶体条目，为该蛋白的结构功能研究提供了较为可靠的原子模型。AAA+ ATPase通过ATP水解驱动的构象变化产生机械力，用于底物蛋白的去折叠、解聚或重塑——这种"分子马达"机制是SPATA5L1作为55LCC（SPATA5-SPATA5L1-C1orf109-CINP）异源六聚体复合物核心组分的基础。

在功能机制上，SPATA5L1与SPATA5协同形成ATPase复合体，直接参与复制体（replisome）蛋白稳态的维持（PMID:38554706）。更具体而言，55LCC复合体定位于停滞的复制叉，其ATPase活性被复制叉DNA特异性增强——这一"DNA传感器"机制确保ATPase仅在需要时才被激活。激活后，ATPase将复制体底物（如CMG解旋酶组分）转运至复合体内部的半胱氨酸蛋白酶活性位点进行裂解，从而清理受损的复制叉并促进复制重启。此功能对于姐妹染色单体黏连与染色体稳定性至关重要。

PPI网络（degree=107）进一步锚定SPATA5L1在复制应激反应中的核心位置：与CINP（STRING评分=844）、C1ORF109（STRING评分=836）的强互作印证了55LCC复合体的组成；与UFD1（STRING评分=839）的互作则连接至泛素-蛋白酶体系统，暗示底物裂解后产生的多肽片段可能通过UFD1/NPL4复合体转运至蛋白酶体降解。已报道的SPATA5L1双等位基因变异导致智力障碍、痉挛性肌张力障碍与听力丧失（PMID:34626583），充分说明了55LCC功能在神经发育中的不可或缺性。

尽管HPA核定位证据为"nan"（核定位特异性5/10），SPATA5L1作为染色质相关复制体调控蛋白的功能明确指向其核内定位。核质评分的缺失可能反映HPA图像数据中该蛋白表达丰度低或细胞周期依赖性表达。鉴于SPATA5L1的PubMed文献仅10篇，其作为复制应激的"守门人"在肿瘤发生（复制应激普遍增强）中的角色几乎未被挖掘，这使其成为DNA复制胁迫领域极具潜力的新颖靶点。其与C1ORF109的紧密功能性耦合同时提示这两个NEW核蛋白可作为共调控单元进行联合功能筛选。

**蛋白全称**: ATPase family gene 2 protein homolog B

**功能**: ATP-dependent chaperone part of the 55LCC heterohexameric ATPase complex which is chromatin-associated and promotes replisome proteostasis to maintain replication fork progression and genome stability. Required for replication fork progression, sister chromatid cohesion, and chromosome stability. The ATPase activity is specifically enhanced by replication fork DNA and is coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. Uses ATPase ac

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003593 |
| InterPro | IPR050168 |
| InterPro | IPR041569 |
| InterPro | IPR003959 |
| InterPro | IPR003960 |
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CINP | STRING | 844 |
| UFD1 | STRING | 839 |
| C1ORF109 | STRING | 836 |
| UBXN7 | STRING | 703 |
| CUL3 | BioGRID | 1 |
| NXF1 | BioGRID | 1 |
| FAS | BioGRID | 1 |
| CAMKMT | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BVQ7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171763-SPATA5L1

![](https://images.proteinatlas.org/43679/512_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/43679/512_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/43679/501_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/43679/501_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/43679/498_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/43679/498_C4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 41390732 | AFG2B gene variants and elevated protein expression in lupus nephritis: new insights into childhood-onset systemic lupus | Adv Rheumatol 2025 |
| 41375745 | Neurodevelopmental Disorder with Psychomotor Delay, Hearing Loss, and Spasticity Caused by Compound Heterozygous SPATA5L | J Clin Med 2025 |
| 40268917 | Cryo-EM structure of the AAA+ SPATA5 complex and its role in human cytoplasmic pre-60S maturation. | Nat Commun 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SPATA5L1

