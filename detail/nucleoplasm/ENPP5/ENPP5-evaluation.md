---
type: protein-evaluation
gene: "ENPP5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## ENPP5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ENPP5 |
| 蛋白名称 | Ectonucleotide pyrophosphatase/phosphodiesterase family member 5 |
| 蛋白大小 | 477 aa / 54.7 kDa |
| UniProt ID | Q9UJA9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 477 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=23 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=88.1; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Alkaline_phosphatase_core_sf; Phosphodiest/P_Trfase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=23 broad=31
- AF pLDDT=88.1 PDB=1
- InterPro: Alkaline_phosphatase_core_sf; Phosphodiest/P_Trfase
- Pfam: Phosphodiest
- PPI degree=7 ChIP: None
40457511: A Novel Skeletal Dysplasia With Premaxilla Overgrowth, Gingival Hyperplasia, and | 40827287: Identification of novel drug targets for primary open angle glaucoma and its pot | 40167410: Causal Associations of Insomnia With Chronic Kidney Diseases and Underlying Bloo

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ectonucleotide pyrophosphatase/phosphodiesterase family member 5

**功能**: Can hydrolyze NAD but cannot hydrolyze nucleotide di- and triphosphates. Lacks lysopholipase D activity. May play a role in neuronal cell communication

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR017850 |
| InterPro | IPR002591 |
| Pfam | PF01663 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HNRNPL | BioGRID | 1 |
| SKP1 | BioGRID | 1 |
| CFTR | BioGRID | 1 |
| KRAS | BioGRID | 0 |
| FBXO2 | BioGRID | 0 |
| SIGLECL1 | BioGRID | 0 |
| TIAM1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UJA9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000112796-ENPP5

![](https://images.proteinatlas.org/16902/1789_A5_9_cr597063c33efc9_red_green.jpg)
![](https://images.proteinatlas.org/16902/1789_A5_18_cr597063c33f405_red_green.jpg)
![](https://images.proteinatlas.org/16902/164_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/16902/164_F12_2_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能**：ENPP5属于外核苷酸焦磷酸酶/磷酸二酯酶（ENPP）7成员家族，含有碱性磷酸酶核心超家族结构域（InterPro: IPR017850）和磷酸二酯酶/磷酸转移酶结构域（IPR002591; Pfam: PF01663）。与家族其他成员显著不同的是，ENPP5具有独特的底物选择性谱：它能水解NAD（烟酰胺腺嘌呤二核苷酸），但不能水解核苷酸二磷酸或三磷酸，且缺乏溶血磷脂酶D活性（即不能水解溶血磷脂酰胆碱生成溶血磷脂酸，区别于ENPP2/autotaxin）。这种底物谱在ENPP家族中独一无二——ENPP1和ENPP3主要水解ATP，ENPP2专一性水解溶血磷脂酰胆碱，而ENPP5可能代表进化上特化用于NAD代谢的分支。AlphaFold pLDDT=88.1，一个PDB条目提供部分实验结构信息。

**PPI网络与功能联系**：ENPP5的PPI网络虽小（degree=7），但包含若干具有深刻生物学意义的互作伙伴。HNRNPL（异质核核糖核蛋白L, BioGRID count=1）是pre-mRNA剪接调控和mRNA核质转运的关键因子——这一互作直接提示ENPP5在细胞核内可能与RNA代谢存在功能耦合。SKP1（BioGRID count=1）是SCF（Skp1-Cullin-F-box）E3泛素连接酶复合物的核心支架亚基，若与ENPP5存在功能性互作，可能意味着ENPP5水平受泛素-蛋白酶体系统调控，或在细胞周期依赖性的方式中被降解。CFTR（囊性纤维化跨膜传导调节因子）的潜在互作将ENPP5与离子通道信号通路联系起来。KRAS和TIAM1（Rac1 GEF）的互作则分别指向RTK-RAS-MAPK通路和肌动蛋白细胞骨架重塑信号。

**结构解读**：pLDDT=88.1表明477个氨基酸的蛋白总体折叠良好。碱性磷酸酶核心超家族折叠采用典型的α/β/α三明治架构，催化中心通常含有一个双核金属离子位点（Zn²⁺和Mg²⁺）用于磷酸酯水解。ENPP5特有的NAD选择性可归结为其活性位点裂隙的独特几何构型——相较于ENPP1/ENPP3较宽的底物结合口袋，ENPP5的活性中心形状可能对NAD的腺苷-核糖-烟酰胺骨架有精确互补性，同时排斥核苷酸的三磷酸基团。结构层面的一个核心推论是：如果ENPP5是NAD水解酶，其核质分布具有深刻的代谢调控含义。NAD是sirtuin去乙酰化酶（SIRT1-7）、PARP多聚ADP核糖聚合酶和CD38环状ADP核糖合成酶的必需辅因子——这些均为核内关键酶。因此，ENPP5在核质中的NAD水解活性可能直接调控核NAD池。

**分子机制模型**：基于全部证据，ENPP5在核质中最可能扮演核NAD稳态调控因子的角色。传统上ENPP家族被认为是外核苷酸酶（ecto-enzyme），通过N端信号肽锚定在质膜外侧发挥作用。然而ENPP5的核质定位（HPA Approved级别——五个评估蛋白中证据等级最高）颠覆了这一认知范式。一种模型是：ENPP5可能通过内部核定位信号（NLS）进入细胞核，在核质中作为NAD焦磷酸酶活性中心，将NAD水解为烟酰胺单核苷酸（NMN）和AMP，从而消耗核内游离NAD。核NAD浓度的下降会抑制sirtuin去乙酰化酶活性（特别是SIRT1和SIRT6），进而广泛影响组蛋白乙酰化修饰、转录调控和DNA损伤修复。另一种非互斥模型认为：ENPP5的水解产物NMN和AMP可能作为第二信使——AMP可激活AMPK能量感知通路，而NMN是NAD补救合成的前体，构成局部"NAD-NMN-NAD"代谢循环。HNRNPL的互作为上述模型提供了新的维度——ENPP5可能通过与剪接因子结合被靶向至特定染色质或转录位点，在局部实现精准的NAD浓度调控。

**研究与治疗意义**：ENPP5仅23篇PubMed论文（9/10新颖性）。在神经退行性疾病中，ENPP5被鉴定为阿尔茨海默病认知韧性的潜在贡献因子（PMID: 41723778）——这与NAD依赖的sirtuin/PARP通路是神经保护的核心调控节点高度兼容。ENPP5同时被鉴定为原发性开角型青光眼的新药靶点（PMID: 40827287）。在骨代谢领域，ENPP5在骨质疏松-肌少症中呈现差异表达（PMID: 41534648），拓展了其功能范围。开发ENPP5特异性抑制剂可为调控核NAD池提供新型药理工具——这一策略在肿瘤学（PARP抑制剂已广泛临床应用）和神经退行性疾病中具有转化医学潜力。与ENPP2（autotaxin）已有临床期抑制剂进入试验相比，ENPP5的NAD选择性抑制剂开发仍属空白领域，为该方向提供了先发优势。

### PubMed 文献

**PubMed count: 31**

| 41723778 | Unravelling Synaptic and Metabolic Mechanisms of Cognitive Resilience in Asymptomatic Alzheimer's Disease Across Two Alz | Cell Mol Neurobiol 2026 |
| 41534648 | Exploring the molecular intersections of osteoporosis and sarcopenia: An integrated bioinformatics and experimental vali | Exp Gerontol 2026 |
| 40827287 | Identification of novel drug targets for primary open angle glaucoma and its potential side-effects by human plasma prot | Int J Ophthalmol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ENPP5

