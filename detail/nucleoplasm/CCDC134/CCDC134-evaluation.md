---
type: protein-evaluation
gene: "CCDC134"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCDC134 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCDC134 |
| 蛋白名称 | Coiled-coil domain-containing protein 134 |
| 蛋白大小 | 229 aa / 26.6 kDa |
| UniProt ID | Q9H6E4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 229 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=22 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=83.0; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CC134 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=27 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Supported)
- PubMed: strict=22, broad=31
- AF pLDDT: 83.0 / PDB: 2
- InterPro: CC134
- Pfam: ERK-JNK_inhib
- PPI degree=27 ChIP: None
39509507: Regulated N-glycosylation controls chaperone function and receptor trafficking. | 39127989: Update on the Genetics of Osteogenesis Imperfecta. | 41261126: Structural basis of regulated N-glycosylation at the secretory translocon.

### 4. 总体评价
★★★★  **71.0/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Coiled-coil domain-containing protein 134

**功能**: Molecular adapter required to prevent protein hyperglycosylation of HSP90B1: during translation, associates with nascent HSP90B1 and the STT3A catalytic component of the OST-A complex and tethers them to a specialized translocon that forms a microenvironment for HSP90B1 folding (PubMed:38670073, PubMed:39509507). In the CCDC134-containing translocon, STT3A associates with the SRT pseudosubstrate motif of HSP90B1, preventing access to facultative glycosylation sites until folding is completed, pr

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026321 |
| Pfam | PF15002 |

### 深度机制分析

CCDC134（PF15002/IPR026321，ERK-JNK_inhib家族）是一个含coiled-coil结构域的适配蛋白，其功能注释指向N-糖基化质量控制和分泌通道的调节。UniProt功能描述明确指出CCDC134通过与HSP90B1（GRP94，内质网分子伴侣）新生链和OST-A复合体的STT3A催化亚基结合，桥接翻译中蛋白与特化的转位子微环境。这一"翻译共翻译"（co-translational）N-糖基化门控机制由结构生物学验证（PubMed: 38670073, 39509507），其中CCDC134作为分子适配器限制STT3A对HSP90B1上非必需糖基化位点的预访问，直到折叠完成——实质上是利用空间位阻实现糖基化保真度控制。

结构层面，AlphaFold v6预测的整体pLDDT为83.0，有序区域比例适中，PDB数据库中已有2个条目，说明已有确定的实验结构信息。Pfam将其归属为ERK-JNK_inhib家族，但CCDC134中该结构域与经典MAPK通路抑制的关系尚不清楚。coiled-coil区域的构建提示其可能通过CC结构域形成同源/异源二聚体以实现功能。

PPI网络方面，BioGRID数据显示CCDC134与泛素-蛋白酶体系统组分（UBC、UBQLN4、VCP）及染色质修饰因子（TADA2A、KAT2B）存在互作。VCP/p97是内质网相关降解（ERAD）的核心ATP酶，UBQLN4为穿梭因子——这些互作将CCDC134与内质网蛋白质质量控制通路联系起来，提示其不仅参与共翻译糖基化调控，还可能在错误折叠蛋白的分选和降解中扮演角色。KAT2B/PCAF作为组蛋白乙酰转移酶的互作则暗示CCDC134可能通过未知机制触及染色质层面的调控。

HPA定位为nucleoplasm且获得Supported级可信度，但同时存在分泌通道功能——这种"核-分泌双定位"的矛盾性值得深思。可能CCDC134的功能并不局限于分泌通道：其与TADA2A、KAT2B染色质调控因子的互作提示核内功能的可能性；或者其在细胞质/内质网中行使主要功能，核定位为次要或条件依赖性的。该蛋白作为N-糖基化保真度的分子守门人，其对HSP90B1客户端蛋白成熟的影响可能间接波及多种信号通路——HSP90B1的客户蛋白涵盖整合素、Toll样受体及Wnt共受体，因此CCDC134的功能失调可能产生广泛的下游效应。

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBC | BioGRID | 0 |
| UBQLN4 | BioGRID | 0 |
| VCP | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| TCTN1 | BioGRID | 0 |
| TRIM25 | BioGRID | 0 |
| TADA2A | BioGRID | 0 |
| KAT2B | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H6E4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100147-CCDC134

![](https://images.proteinatlas.org/75348/2075_A5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2075_A5_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100147-CCDC134

![](https://images.proteinatlas.org/75348/2075_A5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2075_A5_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100147-CCDC134

![](https://images.proteinatlas.org/75348/2075_A5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2075_A5_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2207_E8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75348/2035_H10_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 31**

| 42182752 | Identification and validation of prognostic genes related to mitochondrial dynamics and mitochondrial autophagy in esoph | J Thorac Dis 2026 |
| 41940328 | Genetic evidence for causal roles of circulating proteins on breast cancer susceptibility. | iScience 2026 |
| 41673675 | Decreased expression of circ-CCDC134 mediated by TNF-α in patients with rheumatoid arthritis affects T cell function via | Arthritis Res Ther 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCDC134

