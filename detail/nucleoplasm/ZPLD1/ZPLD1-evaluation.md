---
type: protein-evaluation
gene: "ZPLD1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## ZPLD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ZPLD1 |
| 蛋白名称 | Zona pellucida-like domain-containing protein 1 |
| 蛋白大小 | 415 aa / 45.5 kDa |
| UniProt ID | Q8TCW7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 415 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=12 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ZP-C; ZP-C_dom; ZP-N |
| PPI | 5/10 | x3 | 15.0 | PPI degree=11 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=12 broad=17
- AF pLDDT=77.3 PDB=0
- InterPro: ZP-C; ZP-C_dom; ZP-N
- Pfam: Zona_pellucida; ZP-N
- PPI degree=11 ChIP: None
31455802: Spontaneous mutations of the Zpld1 gene in mice cause semicircular canal dysfunc | 36430381: Zona Pellucida like Domain Protein 1 (ZPLD1) Polymerization Is Regulated by Two  | 42287969: Increased head-turning, hyperactivity and low-penetrance circling behaviour in m

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Zona pellucida-like domain-containing protein 1

**功能**: Glycoprotein which is a component of the gelatinous extracellular matrix in the cupulae of the vestibular organ

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR055355 |
| InterPro | IPR042235 |
| InterPro | IPR055356 |
| InterPro | IPR001507 |
| Pfam | PF00100 |
| Pfam | PF23344 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RARG | BioGRID | 1 |
| TMX1 | BioGRID | 1 |
| WDTC1 | BioGRID | 1 |
| CEACAM8 | BioGRID | 0 |
| GNPTAB | BioGRID | 0 |
| LRRC16A | BioGRID | 0 |
| RTN4 | BioGRID | 0 |
| SDF2L1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TCW7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170044-ZPLD1

![](https://images.proteinatlas.org/77519/1789_H8_4_cr596f26028ddf8_red_green.jpg)
![](https://images.proteinatlas.org/77519/1789_H8_20_cr596f26028d9b7_red_green.jpg)

### PubMed 文献

**PubMed count: 17**

| 42287969 | Increased head-turning, hyperactivity and low-penetrance circling behaviour in mice lacking ZPLD1, a protein that scaffo | Hear Res 2026 |
| 41582362 | Exploring ZPLD1 as a Prognostic Indicator and Therapeutic Target in Bladder Cancer. | Curr Med Chem 2026 |
| 41386630 | Genome-wide association study of tolerance to acute hypoxia in the olive flounder (Paralichthys olivaceus) using individ | Gene 2026 |

### 深度机制分析

ZPLD1（415 aa, 45.5 kDa）属于含有ZP结构域的蛋白家族，其结构域架构包括ZP-N（IPR055355）和ZP-C（IPR001507）两个核心模块，这两个模块以串联方式组织，形成约260个氨基酸的ZP模块。ZP模块以其在透明带（zona pellucida）糖蛋白中的聚合功能而闻名——ZP-N/ZP-C模块通过分子间互作介导蛋白的聚合形成丝状基质。AlphaFold预测pLDDT=77.3，无PDB实验结构，但该家族的ZP模块折叠高度保守，预测可信度足以支持结构域边界的划定。

功能上，ZPLD1是前庭器官壶腹帽（cupulae）中凝胶状胞外基质的组分（PMID:31455802），其聚合特性对壶腹帽的结构完整性至关重要。近期研究揭示了两个保守的半胱氨酸在ZPLD1聚合调控中的作用（PMID:36430381），提示其聚合状态受氧化还原调控。ZPLD1敲除小鼠表现出头部转动增加、过度活跃和低渗透率转圈行为（PMID:42287969），证明其通过架构半规管中的胞外脚手架来维持平衡功能。

值得注意的是，HPA将ZPLD1定位于Nucleoplasm（Approved级别），这与典型的分泌/胞外基质蛋白的定位明显不同。一种可能机制是：ZPLD1作为新生多肽在翻译过程中或翻译后短暂滞留于内质网-核膜连续体中，其ZP模块在此可能作为蛋白质量控制信号，导致部分蛋白被导向核质。PPI网络（BioGRID degree=11）中含RARG（视黄酸受体γ）、TMX1（硫氧还蛋白相关跨膜蛋白）和RTN4（网状蛋白4），暗示ZPLD1可能与核受体信号通路和内质网形态调控存在交叉。

在TE调控方面，ZPLD1的核定位可能并非其主要功能，但其作为具有聚合倾向的胞外基质蛋白进入核质，可能对核内相分离凝聚体或核骨架产生影响。RARG作为核受体转录因子若与ZPLD1存在功能性互作，则ZPLD1可能通过调控视黄酸信号间接影响TE表达。前瞻性实验应通过共免疫沉淀验证核内互作伙伴，并利用CUT&Tag/ATAC-seq检测ZPLD1过表达或敲除时TE位点染色质可及性的变化。ZP模块的聚合倾向在核质中的角色是一个有前景但尚未探索的方向。

