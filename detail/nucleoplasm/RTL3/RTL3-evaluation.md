---
type: protein-evaluation
gene: "RTL3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---
## RTL3 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RTL3 |
| 蛋白名称 | Retrotransposon Gag-like protein 3 |
| 蛋白大小 | 475 aa / 52.8 kDa |
| UniProt ID | Q8N8U3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 475 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=58.9; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | DUF4939; RTL1-rel; Znf_CCHC |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
HPA: Golgi apparatus; Nucleoplasm; Plasma membrane (Approved)
PubMed: strict=3, broad=5
AF pLDDT: 58.9  PDB: 0
InterPro: DUF4939; RTL1-rel; Znf_CCHC
Pfam: DUF4939; zf-CCHC
PPI degree: 1  ChIP: None
**Papers**: 33043724: A retrotransposon gag-like-3 gene RTL3 and SOX-9 co-regulate the expression of C | 38507667: The Diverse Evolutionary Histories of Domesticated Metaviral Capsid Genes in Mam | 31710242: Predicting the Lung Squamous Cell Carcinoma Diagnosis and Prognosis Markers by U

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
**TE candidate** -- DUF4939; RTL1-rel; Znf_CCHC


### 补充分析 (UniProt API)

**蛋白全称**: Retrotransposon Gag-like protein 3

**功能**: May function as a transcriptional regulator. Plays a role in postnatal myogenesis, may be involved in the regulation of satellite cells self-renewal

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR032549 |
| InterPro | IPR032567 |
| InterPro | IPR001878 |
| InterPro | IPR036875 |
| Pfam | PF16297 |
| Pfam | PF00098 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

RTL3(Retrotransposon Gag-like protein 3)是"驯化"自逆转录病毒Gag蛋白的哺乳动物基因组编码蛋白，代表着病毒-宿主共同进化的分子化石。在长达数百万年的进化中，原始Gag的逆转录酶和整合酶结构域已丢失，保留了Gag-like DUF4939结构域(IPR032549)和Znf_CCHC锌指结构(IPR001878/PF00098)。CCHC锌指是经典的反转录病毒核壳蛋白核心，负责与病毒RNA基因组的psi包装信号特异性结合。pLDDT仅58.9(整体结构质量最低)，表明RTL3可能具有较高的结构性无序，这与Gag蛋白的非结构化N端和柔性连接区域特征一致。

RTL3已被本评估系统标记为高优先级TE(yourself regulation)候选因子(TE_REG_CANDIDATE)。作为Gag同源蛋白，RTL3可能保留了祖先Gag蛋白的核酸结合功能。在核质的已知功能中，RTL3可与SOX9转录因子协同调控软骨细胞中COL2A1(II型胶原)的表达(PMID:33043724)——这是RTL3基因功能的唯一直接实验证据。RTL3含有的Znf_CCHC锌指可通过RNA或DNA结合将SOX9稳定于COL2A1增强子区域，形成RTL3-SOX9-COL2A1转录调控三元复合体模型。

PPI网络极度稀疏(degree=1，仅与RTL6互作，STRING=747)。这种孤独的互作模式是Gag驯化蛋白的典型特征——在驯化过程中，病毒蛋白的大多数互作伙伴被进化压力清除，仅保留对宿主有益的少数功能性相互作用。HPA定位为Golgi apparatus、Nucleoplasm和Plasma membrane(Approved)，这与Gag蛋白在病毒生命周期中的定位模式惊人相似——Gag在膜上组装、在核质中进行RNA结合。

RTL3的DUF4939结构域功能完全未知——这是病毒驯化基因研究的前沿领域。已知RTL1(同样是驯化Gag蛋白)的突变可导致Kagami-Ogata和Temple综合征(亲本印记连锁)，RTL3是否在人类疾病中具有类似的印记调控功能尚不可知。该领域的一个关键悬而未决的问题是：在哺乳动物基因组中，驯化Gag蛋白(RTL1-6)是否仍保留对LTR/ERV序列的残留亲和力，而成为"内源性病毒序列的宿主监管者"？RTL3的测试可提供关键证据。PubMed仅3篇，是前沿蓝海研究领域。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000179300-RTL3

![](https://images.proteinatlas.org/75136/1585_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/75136/1585_G11_4_red_green.jpg)
![](https://images.proteinatlas.org/75136/1625_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/75136/1625_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/75136/1616_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/75136/1616_G11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 38507667 | The Diverse Evolutionary Histories of Domesticated Metaviral Capsid Genes in Mammals. | Mol Biol Evol 2024 |
| 33043724 | A retrotransposon gag-like-3 gene RTL3 and SOX-9 co-regulate the expression of COL2A1 in chondrocytes. | Connect Tissue Res 2021 |
| 31710242 | Predicting the Lung Squamous Cell Carcinoma Diagnosis and Prognosis Markers by Unique DNA Methylation and Gene Expressio | J Comput Biol 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RTL3

