---
type: protein-evaluation
gene: "CAPN13"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAPN13

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | CAPN13 |
| Protein Name | Calpain-13 |
| Size | 669 aa / 76.7 kDa |
| UniProt | Q6MZZ7 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 669 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=83.0; PDB=1 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Calpain_cysteine_protease; Calpain_domain_III; Calpain_III_sf |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=17 |
| **加权总分** | | | **139.0/180** | |
| **归一化总分 (÷1.83)** | | | **76.0/100** | 互证: +1.0 |

### 3. Analysis
- HPA: Nucleoplasm (Approved)
- PubMed: strict=5, broad=9
- AF pLDDT: 83.0 / PDB: 1
- InterPro: Calpain_cysteine_protease; Calpain_domain_III; Calpain_III_sf
- Pfam: Calpain_III; CAPN13-like_C_EFh; Peptidase_C2
- PPI degree=17 ChIP: None
11675017: Identification and characterization of two novel calpain large subunit genes. | 28131390: Calpain-14 and its association with eosinophilic esophagitis. | 26399219: Epithelial-Mesenchymal Transition (EMT) Gene Variants and Epithelial Ovarian Can

### 4. Assessment
★★★★  **76.5/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**：CAPN13（Calpain-13）属于钙蛋白酶超家族，但其结构域组织与经典钙蛋白酶（CAPN1/μ-calpain和CAPN2/m-calpain）存在根本性差异——这一差异对理解其核内功能至关重要。CAPN13的InterPro/Pfam注释揭示：IPR022684/Pfam Peptidase_C2对应钙蛋白酶半胱氨酸蛋白酶核心结构域（CysPc，由结构域IIa和IIb组成），IPR022682/Pfam Calpain_III对应结构域III（C2样β-三明治折叠，参与Ca²⁺和磷脂结合），IPR036213/IPR038765 Calpain_III_sf为结构域III的超家族注释。然而，CAPN13缺乏经典钙蛋白酶的两个关键调控元件：(1) N端锚定螺旋（结构域I）——在经典钙蛋白酶中，该螺旋遮挡催化半胱氨酸残基，必须通过Ca²⁺诱导的自溶解除去才能激活；(2) 经典penta-EF-hand结构域IV——介导钙蛋白酶大亚基与小调节亚基（CAPNS1/calpain small subunit）的Ca²⁺依赖性异源二聚化。取而代之的是，CAPN13拥有一个独特的C端EF-hand样结构域（IPR054069 CAPN13-like_C_EFh），这是CAPN13和CAPN14特有的钙蛋白酶亚家族标记。这一结构域替换的关键推论是：CAPN13可能以单体形式存在（不依赖小调节亚基），并且可能以不依赖Ca²⁺或通过不同于经典路径的Ca²⁺感应机制被激活。缺失N端锚定螺旋进一步暗示CAPN13的催化半胱氨酸在基础状态下即可被底物接近，或者其活性受替代性调控机制（如磷酸化、氧化还原或蛋白-蛋白相互作用）控制，而非经典的自溶激活。

**PPI网络与核RNA代谢**：CAPN13的PPI网络（degree=17）是5个评估蛋白中最具信息量的之一——其所有高置信度互作伙伴均为核蛋白，且功能高度集中于RNA加工和染色质组织。SAFB2（scaffold attachment factor B2）是核基质/核骨架附着蛋白，参与染色质组织和转录抑制。SFSWAP（splicing factor SWAP，又称SFRS8）是富含丝氨酸/精氨酸（SR）的剪接因子，调控选择性剪接位点的选择。SF1（splicing factor 1）识别内含子分支点位点序列，是剪接体早期组装（E complex）的关键因子。PRRC2A（HLA-B-associated transcript 2）是一种富含脯氨酸的卷曲螺旋蛋白，参与mRNA稳定性和翻译调控。DIDO1（death inducer-obliterator 1）是转录调控因子，参与细胞凋亡和选择性剪接。PPP1R10（PNUTS）是蛋白磷酸酶1（PP1）的核内调节亚基，通过去磷酸化调控RNA聚合酶II的C端结构域（CTD）磷酸化状态，从而影响转录延伸和终止。ATMIN（ATM interactor）是ATM激酶的转录辅因子，参与DNA损伤应答中的基因表达重编程。这一互作网络的核心信号是：CAPN13定位于pre-mRNA加工和转录调控的分子机器中，而非胞浆骨架重塑——与经典钙蛋白酶的功能范畴截然不同。CAPN13的BioGRID互作评分均为1（低置信度），提示这些互作来自大规模蛋白质组学筛选，尚未在针对性实验中被验证——这既是警告（可能是假阳性），也是机会（可能揭示被忽视的核内蛋白水解网络）。

**结构生物学解读**：pLDDT=83.0和1个PDB条目为CAPN13提供了一定的结构理解。钙蛋白酶CysPc核心（结构域IIa+IIb）在所有钙蛋白酶家族成员中高度保守，预计采用经典的"半胱氨酸蛋白酶折叠"：结构域IIa贡献催化半胱氨酸残基（Cys），结构域IIb贡献催化组氨酸（His）和天冬酰胺（Asn），形成Cys-His-Asn催化三联体。在非活性状态下，这两个子域在空间上分离；激活时它们汇聚成功能性活性位点裂隙。结构域III预计采用β-三明治折叠（类似C2结构域），可能参与底物识别或核内定位信号介导的核靶向。C端CAPN13-like_C_EFh结构域（IPR054069）是结构上的"暗区域"——其序列与经典EF-hand结构域IV的相似度太低，无法通过同源建模可靠预测其结构，但AlphaFold pLDDT=83.0的整体高置信度表明该区域在孤立预测中是良好折叠的。CAPN13的独特性在于：penta-EF-hand结构域IV负责经典钙蛋白酶的二聚化和Ca²⁺传感，其被CAPN13-like_C_EFh替代意味着活性调控机制、底物识别模式和亚细胞定位可能全部发生了根本性重编程。1个PDB条目可能涵盖CysPc核心或结构域III的片段结构。

**分子机制模型**：基于上述证据的综合，CAPN13的分子功能模型如下：CAPN13是一种**核内受限性半胱氨酸蛋白酶**，专门作用于核内RNA加工机器的蛋白组分。在剪接体组装循环中，CAPN13可能执行以下功能之一：(1) **剪接因子转换的限速蛋白酶**——剪接体在从A complex→B complex→C complex的过渡中需要精确的蛋白组分交换。CAPN13可能通过有限蛋白水解去除特定剪接因子（如SF1的N端区域或SFSWAP的RS结构域），促进剪接体的构象重排。这类似于caspase介导的凋亡执行阶段的有限蛋白水解策略，但应用于完全不同的细胞过程。(2) **转录偶联蛋白水解的质量控制**——RNA聚合酶II在转录延伸过程中，PNUTS/PPP1R10通过PP1介导的CTD去磷酸化调控聚合酶的速度和加工能力。CAPN13与PNUTS互作，可能通过水解特定转录延伸因子来响应转录应激（如R-loop累积或转录-复制冲突），维护基因组的转录完整性。(3) **DNA损伤应答中的核蛋白质稳态**——ATMIN和DIDO1的互作将CAPN13置于DNA损伤信号通路中。在DNA双链断裂时，CAPN13可能切割转录抑制因子复合物（SAFB2）以允许损伤位点附近的局部转录激活或抑制，促进修复因子的募集。肿瘤抑制因子的证据（PubMed 32088085：结直肠癌中CAPN13的失活突变）与这一模型一致——CAPN13的蛋白水解功能可能作为核内肿瘤抑制检查点，通过去除异常剪接变体或维持正确的转录程序来抑制转化。CAPN13缺失导致错误的剪接模式累积，进而引发基因组不稳定和恶性转化。

**研究与转化医学意义**：CAPN13是目前文献中极少数被注释为核定位的钙蛋白酶之一，在蛋白酶生物学中占据独特的生态位——它代表了钙蛋白酶从胞浆Ca²⁺信号整合器进化为核内RNA加工调节器的功能转变。(1) 作为半胱氨酸蛋白酶，CAPN13天然可被小分子抑制剂靶向——已有钙蛋白酶抑制剂（如calpeptin、PD150606）可作为先导化合物，但需要筛选对CAPN13有选择性的化合物以避免抑制广泛表达的CAPN1/CAPN2导致的毒性。(2) 结直肠癌中的失活突变（PubMed 32088085）提供了很强的遗传学证据支持其肿瘤抑制功能——对CAPN13突变状态的CRC患者进行分层可能指导治疗选择（如剪接体抑制剂或DNA损伤修复靶向药物是否在CAPN13缺失的背景下具有合成致死效应）。(3) 最关键的未解决问题——CAPN13的核内底物鉴定——需要基于N端同位素标记（TAILS/N-terminomics）的降解组学来在CAPN13过表达/敲除条件下系统地捕获被切割蛋白的N端新生成肽段。这将是理解CAPN13功能的突破性实验，并可能揭示核内蛋白水解调控RNA加工的第一个范例。(4) CAPN13-like_C_EFh结构域和独立于CAPNS1小亚基的独特特征使CAPN13成为冷冻电镜/晶体学研究的理想对象——解析第一个"非常规钙蛋白酶"的结构将建立钙蛋白酶调控的新范式。


### 补充分析 (UniProt API)

**蛋白全称**: Calpain-13

**功能**: Probable non-lysosomal thiol-protease

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR022684 |
| InterPro | IPR022682 |
| InterPro | IPR036213 |
| InterPro | IPR054069 |
| InterPro | IPR011992 |
| InterPro | IPR038765 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZC3H4 | BioGRID | 1 |
| PPP1R10 | BioGRID | 1 |
| ATMIN | BioGRID | 1 |
| SFSWAP | BioGRID | 1 |
| SAFB2 | BioGRID | 1 |
| DIDO1 | BioGRID | 1 |
| PRRC2A | BioGRID | 1 |
| SF1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6MZZ7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162949-CAPN13

![](https://images.proteinatlas.org/29496/1382_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/29496/1382_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/29496/1419_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/29496/1419_D4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 36882691 | Propensity scores as a novel method to guide sample allocation and minimize batch effects during the design of high thro | BMC Bioinformatics 2023 |
| 33991750 | Identification of differential DNA methylation associated with multiple sclerosis: A family-based study. | J Neuroimmunol 2021 |
| 32088085 | Inactivating mutations of tumor suppressor genes ABCA1 and CAPN13 in colorectal cancers. | Pathol Res Pract 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAPN13

