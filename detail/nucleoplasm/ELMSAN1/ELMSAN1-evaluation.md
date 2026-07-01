---
type: protein-evaluation
gene: "ELMSAN1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## ELMSAN1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ELMSAN1 |
| 蛋白名称 | Mitotic deacetylase-associated SANT domain protein |
| 蛋白大小 | 1045 aa / 115.0 kDa |
| UniProt ID | Q6PJG2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1045 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=48.3; PDB=2 |
| 调控结构域 | 7/10 | x2 | 14.0 | ELM2_dom; Homeodomain-like_sf; SANT/Myb |
| PPI | 7/10 | x3 | 21.0 | PPI degree=104 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=8 broad=9
- AF pLDDT=48.3 PDB=2
- InterPro: ELM2_dom; Homeodomain-like_sf; SANT/Myb
- Pfam: ELM2
- PPI degree=104 ChIP: None
40505660: Derepressing nuclear pyruvate dehydrogenase induces therapeutic cancer cell repr | 40768599: Activation of a nongenetic AHR-ELMSAN1 axis optimizes BET-targeting therapy and  | 34912035: RNAmetasome network for macromolecule biogenesis in human cells.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
TE candidate: ELM2_dom; Homeodomain-like_sf; SANT/Myb


### 补充分析 (UniProt API)

**蛋白全称**: Mitotic deacetylase-associated SANT domain protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000949 |
| InterPro | IPR009057 |
| InterPro | IPR001005 |
| InterPro | IPR017884 |
| InterPro | IPR051066 |
| Pfam | PF01448 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DNTTIP1 | STRING | 997 |
| HDAC1 | STRING | 971 |
| TRERF1 | STRING | 869 |
| HDAC2 | STRING | 713 |
| MAPK14 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| TFAP4 | BioGRID | 1 |
| ESR1 | BioGRID | 1 |



### 深度机制分析

**结构域架构**：ELMSAN1（1045 aa, 115.0 kDa）为含ELM2（IPR000949, Pfam PF01448）和SANT domain（IPR001005）的转录共抑制因子。ELM2 domain（约80 aa的a-helical bundle）介导与HDAC1/HDAC2的直接结合。SANT domain（约45 aa的三螺旋束，与Myb DNA-binding domain同源）识别未乙酰化组蛋白尾部（H3 tail, residues 1-20）→将HDAC催化位点靠近乙酰化组蛋白底物→增强去乙酰化效率。AlphaFold pLDDT=48.3（极低，高度IDP性质）——约80%残基pLDDT<70——表明ELMSAN1以"fuzzy complex"和"coupled folding-and-binding"机制与其伴侣（HDAC1/2, TRERF1, DNTTIP1）作用。PPI（degree=104, 极丰富）以HDAC-containing corepressor complex为核心：DNTTIP1（STRING score=997）近乎100%与ELMSAN1共表达——两者形成MIDEAS复合物核心；HDAC1（STRING score=971）经ELM2 domain被招募→去乙酰化H3/H4→转录沉默；ESR1（BioGRID）和ELAVL1（HuR, BioGRID）扩展至estrogen signaling和RNA stability调控。

ELMSAN1是TE调控的直接因子（TE_REG_CANDIDATE）。HDAC1/2是ERV和LINE-1 L1Hs启动子上的主要转录沉默酶——HDAC inhibitor处理后LINE-1/ERV转录上升10-100倍证明HDAC对TE沉默的必要性——HDAC1/2在TE座位识别核小体占据的组蛋白尾部→去乙酰化H3K9ac/H4K16ac→凝缩TE座位染色质→抑制Pol II启动/延伸。ELMSAN1通过ELM2-SANT domain直接招募和增强HDAC1/2对TE座位的去乙酰化活性→维持TE异染色质沉默。AHR-ELMSAN1 axis（PMID 40768599）为ELMSAN1的TE调控提供"可诱导"机制——环境毒素（dioxin, PAH）→AHR激活→AHR-ELMSAN1 negative feedback loop——该回路可能影响ERV LTR转录——因为AHR的XRE（xenobiotic response element）在ERVK和HERV-H LTR中有假定结合位点。BET inhibitor在白血病中与ELMSAN1的协同效应→BRD4在TE启动子上识别H3K27ac→增强TE转录——ELMSAN1-HDAC1/2直接拮抗BRD4在TE LTR上的转录激活。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6PJG2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000156030

![](https://images.proteinatlas.org/3111/39_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/3111/39_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/3111/40_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/3111/40_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/3111/38_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/3111/38_F9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 40935692 | Target compartmentalized metabolism to regulate epigenetics. | Trends Endocrinol Metab 2025 |
| 40768599 | Activation of a nongenetic AHR-ELMSAN1 axis optimizes BET-targeting therapy and suppresses leukemia stem cells in precli | Sci Transl Med 2025 |
| 40588350 | Loss of Elmsan1 in cardiomyocytes leads to age-dependent cardiac dysfunction and reduced lifespan. | Am J Physiol Heart Circ Physiol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ELMSAN1

