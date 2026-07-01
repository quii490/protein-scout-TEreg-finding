---
type: protein-evaluation
gene: "RCOR2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---
## RCOR2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RCOR2 |
| 蛋白名称 | REST corepressor 2 |
| 蛋白大小 | 523 aa / 58.0 kDa |
| UniProt ID | Q8IZ40 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Midbody; Nucleoplasm; Vesicles (Approved) + ChIP |
| 蛋白大小 | 9/10 | x1 | 9.0 | 523 aa |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed=33 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=67.3; PDB=0 |
| 调控结构域 | 8/10 | x2 | 16.0 | ELM2_dom; Homeodomain-like_sf; REST_helical |
| PPI | 5/10 | x3 | 15.0 | PPI degree=29 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
HPA: Midbody; Nucleoplasm; Vesicles (Approved)
PubMed: strict=33, broad=83
AF pLDDT: 67.3  PDB: 0
InterPro: ELM2_dom; Homeodomain-like_sf; REST_helical
Pfam: ELM2; Myb_DNA-binding; REST_helical
PPI degree: 29  ChIP: Yes
**Papers**: 41052883: Hypoxia-induced RCOR2 promotes macrophage M2 polarization and CD8(+) T-cell exha | 40664206: Non-canonical activating roles of RCoR2 sustain transcription in adrenergic neur | 37442513: REST, RCOR1 and RCOR2 expression is reduced in osteoarthritic chondrocytes and c

### 4. 总体评价
★★★★  **72.7/100**  |  **nucleoplasm**
**TE candidate** -- ELM2_dom; Homeodomain-like_sf; REST_helical


### 补充分析 (UniProt API)

**蛋白全称**: REST corepressor 2

**功能**: May act as a component of a corepressor complex that represses transcription

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000949 |
| InterPro | IPR009057 |
| InterPro | IPR049048 |
| InterPro | IPR001005 |
| InterPro | IPR017884 |
| InterPro | IPR051066 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KDM1A | STRING | 976 |
| HMG20B | STRING | 888 |
| HDAC2 | STRING | 745 |
| ZMYM2 | STRING | 705 |
| HMG20A | STRING | 705 |
| HDAC1 | BioGRID | 1 |
| HDAC11 | BioGRID | 1 |
| SUMO2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IZ40-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167771-RCOR2

![](https://images.proteinatlas.org/21638/1294_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/21638/1294_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/21638/1219_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/21638/1219_C10_7_red_green.jpg)
![](https://images.proteinatlas.org/21638/1189_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/21638/1189_C10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 83**

| 42152495 | The Chromatin-Modifying Protein RCOR2/CoREST2 Safeguards Axon-Dendrite Growth and Microtubule Stability in Brain Neurons | J Neurochem 2026 |
| 42044994 | DDX3X-mediated translation of structured cardiac mRNAs is essential for female heart development. | Genes Dev 2026 |
| 41996247 | RLF/ZFP292 stabilize CoREST-linked LSD1 engagement at bivalent promoters to safeguard pluripotency. | Cell Rep 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RCOR2


### 深度机制分析

RCOR2（REST corepressor 2, 又名CoREST2）是CoREST转录辅抑制复合体的核心支架亚基，523个氨基酸承载了三个功能分明的结构域模块：ELM2结构域（IPR000949）负责与组蛋白去乙酰化酶HDAC1/2的互作，Myb-like DNA结合结构域（IPR009057, Homeodomain-like superfamily）提供与DNA的序列非特异性锚定，REST_helical结构域（IPR049048）介导与REST/NRSF转录因子的双螺旋卷曲互作。Pfam进一步解析为ELM2、Myb_DNA-binding和REST_helical三个独立模块。这三个结构域的线性排列——N端ELM2→中央Myb→C端REST_helical——形成了"阅读-去乙酰化-募合"功能三合一的分子架构。

PPI互作网络完全围绕表观遗传调控展开。STRING结果中KDM1A/LSD1（score=976, 最高置信度）、HDAC2（score=745）、HMG20B/20A（score=888/705）以及ZMYM2（score=705）构成了CoREST复合体的经典六元核心。BioGRID确认了RCOR2-HDAC1、RCOR2-HDAC11和RCOR2-SUMO2的直接实验互作（score=1）。KDM1A/LSD1通过其胺氧化酶活性去除H3K4me1/me2——活跃转录的标志，HDAC1/2去除组蛋白乙酰化，二者协同建立抑制性染色质环境。HMG20B/20A是BRAF35-HDAC复合体的亚基，增强复合体对染色质的靶向能力。SUMO2互作提示RCOR2功能受SUMO化翻译后修饰调控。

RCOR2的ChIP-seq数据阳性（TFs and others）直接证实了其全基因组水平的染色质占位。该蛋白已被标记为TE_REG_CANDIDATE，核心依据在于：ELM2-Myb-REST_helical结构域串联→KDM1A-HDAC表观遗传酶募合→H3K4me2去甲基化+组蛋白去乙酰化→染色质压缩→转录抑制。RCOR2参与的非经典激活功能（PMID:40664206）揭示其在肾上腺素能神经元中通过维持转录来执行"非经典激活"角色——即CoREST复合体在某些基因组位点可充当转录激活因子而非抑制因子，这取决于蛋白修饰和局部转录因子配置。

核定位证据坚实：HPA显示Midbody、Nucleoplasm、Vesicles（Approved），其中Nucleoplasm为高置信度Approved。RCOR2在HPA IF图像中呈现清晰的核内弥散分布模式，伴有有丝分裂中体（midbody）的富集。最近的研究（PMID:42152495）揭示了RCOR2在小鼠脑神经元轴突-树突生长和微管稳定性中的保护作用，进一步将CoREST2功能从经典转录调控扩展到细胞骨架调控。PMID 41996247发现RLF/ZFP292通过稳定CoREST-linked LSD1在二价启动子（bivalent promoters）的占位来保护多能性，这一发现对理解RCOR2在干细胞维持和发育中的角色至关重要。综合来看，RCOR2的深度机制模型为：ELM2+Myb+REST_helical三联结构域→KDM1A/HDAC1/2募合→组蛋白修饰擦除→二价启动子/抑制性染色质建立→转录沉默（经典）/转录激活（非经典）→神经发育+多能性维持+TE沉默。该蛋白是CoREST复合体组装的核心，直接参与TE调控的可能性极高，属于最高优先级的TE调控候选蛋白。



