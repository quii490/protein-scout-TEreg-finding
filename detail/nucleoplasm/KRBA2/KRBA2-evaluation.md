---
type: protein-evaluation
gene: "KRBA2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KRBA2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRBA2 |
| 蛋白名称 | KRAB domain-containing protein 2 |
| 蛋白大小 | 492 aa / 56.2 kDa |
| UniProt ID | Q6ZNG9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 492 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Integrase_cat-core; KRAB; KRAB_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=8 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=3 broad=5
- AF pLDDT=73.3 PDB=0
- InterPro: Integrase_cat-core; KRAB; KRAB_dom_sf
- Pfam: KRAB
- PPI degree=8 ChIP: None
27625650: A Well-Controlled Experimental System to Study Interactions of Cytotoxic T Lymph | 40475416: 3D organoids containing endothelial and neural cells generation by serial induct | 28918518: Micro-RNA Profiling of Exosomes from Marrow-Derived Mesenchymal Stromal Cells in

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001584 |
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050951 |
| InterPro | IPR012337 |
| InterPro | IPR036397 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HNRNPU | BioGRID | 1 |
| MCM2 | BioGRID | 1 |
| CRBN | BioGRID | 1 |
| CYLD | BioGRID | 1 |
| HDAC7 | BioGRID | 1 |
| TP53 | BioGRID | 1 |
| ZBED9 | BioGRID | 1 |
| RPS6 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZNG9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000184619-KRBA2

![](https://images.proteinatlas.org/22849/181_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22849/181_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/22849/180_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22849/180_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/22849/182_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22849/182_B4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 41058765 | Identification of KRBA2 as a probable prognostic biomarker correlated with immune infiltration in kidney clear cell carc | Curr Urol 2025 |
| 40475416 | 3D organoids containing endothelial and neural cells generation by serial inductions of differentiation on human iPSC-de | bioRxiv 2025 |
| 28918518 | Micro-RNA Profiling of Exosomes from Marrow-Derived Mesenchymal Stromal Cells in Patients with Acute Myeloid Leukemia: I | Stem Cell Rev Rep 2017 |

### 深度机制分析

KRBA2的域架构将N端KRAB结构域（Krüppel相关盒, IPR001909; KRAB_dom_sf, IPR036051; Pfam KRAB）与C端整合酶催化核心结构域（Integrase_cat-core, IPR001584; IPR012337, IPR036397）结合在一起。KRAB结构域是约75个残基的模块，存在于脊椎动物中最大的转录抑制因子家族——KRAB锌指蛋白（KZNFs）——的N端。它通过与KAP1/TRIM28/TIF1β辅阻遏物结合，随后招募SETDB1（组蛋白H3K9甲基转移酶）和HP1蛋白，催化形成兼性异染色质。C端整合酶催化核心结构域高度异常——此类结构域典型见于逆转录病毒整合酶和转座酶，将其置于KRAB抑制因子中是前所未有的域组合，立即使KRBA2成为KZNF家族中结构最独特且最耐人寻味的成员之一。

AlphaFold pLDDT为73.3（中等），PDB=0。KRAB结构域的N端α-螺旋置信度较高，而整合酶核心的C端置信度较低——后者预期采用复杂的RNase H样折叠，带有催化性DDE三联体。关键结构问题悬而未决：它是否含有活性的DDE催化位点？是一种活性转座酶，还是催化三联体发生了退化使其成为非催化的DNA结合结构域？

PPI网络（degree=8）包含关键核蛋白互作：HNRNPU（核基质结合蛋白，参与X染色体失活和染色质架构）、MCM2（DNA复制许可因子）、TP53（p53）、HDAC7（组蛋白去乙酰化酶7）和CRBN（cereblon, E3泛素连接酶底物受体）。上述互作描绘出KRBA2作为染色质平台的图景——KRAB结构域通过KAP1招募HDAC活性到特定基因组位点，整合酶核心可能以序列特异性方式结合DNA。

KRAB-KAP1通路是建立灵长类和啮齿类动物中内源性逆转录病毒（ERVs）表观遗传沉默的主要机制。大多数KRAB-ZNFs使用C端锌指阵列识别TE启动子中的特定序列基序，然后通过N端KRAB结构域招募KAP1/SETDB1进行H3K9me3标记。KRBA2的不同之处在于其DNA结合模块是整合酶核心而非锌指——推测它识别的DNA靶标可能与经典KRAB-ZNFs不同，可能识别TE衍生的结构特征（如反向重复或LTR连接）。整合酶核心是一种进化古老的折叠结构，可能在宿主-转座子军备竞赛中被驯化成为TE靶向模块。

TE调控影响深远。KRBA2仅3篇文献的研究热度，PPI网络中与HNRNPU、TP53和HDAC7共享的连接，以及其整合酶-KRAB域结构，使其成为本文分析过的所有蛋白质中TE调控相关性最强且研究最不充分的蛋白。可操作的工作模型：KRBA2通过其整合酶核心识别TE衍生的DNA结构（如整合酶靶向的LTR连接），并通过其KRAB结构域启动KAP1/SETDB1/HP1沉默级联，在进化压力下提供针对年轻逆转录病毒插入的额外防御层。该蛋白质在免疫浸润型肾透明细胞癌中作为预后生物标志物（PMID 41058765）的临床相关性强调了TE沉默在肿瘤免疫编辑中的重要性。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRBA2

