---
type: protein-evaluation
gene: "POGK"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## POGK 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | POGK |
| 蛋白名称 | Pogo transposable element with KRAB domain |
| 蛋白大小 | 609 aa / 69.4 kDa |
| UniProt ID | Q9P215 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 609 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=68.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | aKRAB; Brinker_DNA-bd; CenT-Element_Derived |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=27 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Enhanced) |
| PubMed | strict=7, broad=10 |
| AF pLDDT | 68.2 |
| PDB | 0 |
| InterPro | aKRAB; Brinker_DNA-bd; CenT-Element_Derived |
| Pfam | BrkDBD; DDE_1; HTH_Tnp_Tc5 |
| PPI degree | 27 |
| ChIP | None |

**Papers**: 36761433: Poor Prognostic Biomarker KIAA1522 Is Associated with Immune Infiltrates in Hepa | 38048229: Identification and validation of feature genes associated with M1 macrophages in | 36878930: Identification of a novel circRNA-miRNA-mRNA regulatory axis in hepatocellular c

### 4. 总体评价
★★★★  **71.6/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Pogo transposable element with KRAB domain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003655 |
| InterPro | IPR018586 |
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UCHL3 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| APP | BioGRID | 1 |
| HSP90AA1 | BioGRID | 1 |
| TCEAL1 | BioGRID | 1 |
| CCNDBP1 | BioGRID | 1 |
| TRIM28 | BioGRID | 1 |
| TRIM11 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9P215-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000143157-POGK

![](https://images.proteinatlas.org/31630/405_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/31630/405_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/31630/409_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/31630/409_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/31630/402_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/31630/402_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/75919/1924_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/75919/1924_F11_4_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 40709894 | Four Pharmacogenomic Variants Strongly Linked to Corticosteroid-Induced Avascular Necrosis in Children with Cancer. | J Clin Pharmacol 2025 |
| 39814373 | Pogo transposons provide tools to restrict cancer growth. | Mol Oncol 2025 |
| 39547880 | POGK is a domesticated KRAB domain-containing transposable element with tumor suppressive functions in breast cancer. | Trends Cell Biol 2025 |

### 深度机制分析

POGK（609 aa, 69.4 kDa）是本批次候选蛋白中最具TE调控直接潜力的蛋白之一，原因在于其独特的结构域架构和进化起源。POGK的结构域组合极为罕见——同时含有祖先KRAB结构域（aKRAB, IPR003655）、Brinker DNA结合域（Brinker_DNA-bd, IPR018586）和中心粒衍生元件（CenT-Element_Derived, IPR050863），以及HTH_Tnp_Tc5转座酶同源结构域（PF03221）和DDE_1整合酶/转座酶催化结构域（PF03184）。这一架构清楚地表明POGK是驯化的（domesticated）转座酶蛋白——其祖先是一个活跃的DNA转座子，在进化中被宿主基因组捕获并赋予新的细胞功能。DDE_1结构域是三氨基酸催化基序（Asp-Asp-Glu），典型存在于Mariner/Tc样转座子和逆转录病毒整合酶中，但在POGK中是否保留催化活性有待验证。

POGK作为驯化KRAB结构域转座元件，其肿瘤抑制功能已在乳腺癌中获得功能验证（PMID:39547880）。KRAB结构域是最大的转录抑制结构域家族（KZNF蛋白），通过招募TRIM28/KAP1-SETDB1复合物催化H3K9me3修饰的形成，从而建立局部异染色质环。POGK的PPI网络中最关键的发现是TRIM28（BioGRID评分=1）的互作——TRIM28是KZNF/转座子沉默通路的核心枢纽蛋白。POGK与TRIM28的互作意味着它可能接入KZNF-TRIM28-SETDB1的表观遗传沉默机器。

Brinker DNA结合域已知在果蝇Brk蛋白中通过识别GNCTGTNC共识序列作为转录抑制因子发挥作用。在人类中，该结构域可能赋予POGK序列特异性的DNA结合能力。HTH_Tnp_Tc5和DDE_1结构域源自Tc1/Mariner超家族的DNA转座子，它们在驯化后可能保留了与DNA骨架的非特异性亲和力，辅助POGK扫描基因组并识别靶位点。HPA Nucleoplasm（Enhanced级别）定位与这一核内转录/转座子沉默功能完美匹配。

POGK与TRIM11（BioGRID评分=1）的互作值得特别关注——TRIM11是另一个具有E3泛素连接酶活性的TRIM家族蛋白，可能协同POGK/TRIM28进行泛素化修饰调控。POGK与TRIM72一样与HSP90AA1（分子伴侣）互作，提示其折叠和稳定性受分子伴侣系统调控。文献虽少（PubMed=7），但PMID:39814373明确提出了"Pogo转座子提供限制癌症生长的工具"这一概念，为POGK通过沉默致癌TE或重复序列来抑制肿瘤提供了概念框架。建议的最高优先级实验：（1）ChIP-Seq鉴定POGK全基因组结合位点，分析TE/重复序列富集；（2）POGK敲除后的H3K9me3 ChIP-Seq检测全基因组异染色质变化；（3）RNA-Seq检测TE家族表达变化；（4）验证DDE_1结构域是否保留催化活性。

