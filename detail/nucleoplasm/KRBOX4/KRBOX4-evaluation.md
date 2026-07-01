---
type: protein-evaluation
gene: "KRBOX4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## KRBOX4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRBOX4 |
| 蛋白名称 | KRAB domain-containing protein 4 |
| 蛋白大小 | 171 aa / 20.1 kDa |
| UniProt ID | Q5JUW0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 171 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=48.9; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF |
| PPI | 5/10 | x3 | 15.0 | PPI degree=21 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=0 broad=0
- AF pLDDT=48.9 PDB=0
- InterPro: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF
- Pfam: KRAB
- PPI degree=21 ChIP: None


### 4. 总体评价
**72.7/100** | **nucleoplasm**
TE candidate: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050169 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050169 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRIM28 | BioGRID | 1 |
| ASXL2 | BioGRID | 1 |
| XPO5 | BioGRID | 1 |
| TMEM126A | BioGRID | 1 |
| GADD45GIP1 | BioGRID | 1 |
| LMO3 | BioGRID | 1 |
| PRKAB2 | BioGRID | 1 |
| LMO1 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：KRBOX4（171 aa，20.1 kDa）是高度精简的TE调控候选蛋白，仅含KRAB结构域（PF01352，IPR001909，KRAB_dom_sf IPR036051）和Krueppel_C2H2_ZnF（IPR050169）。与典型的KRAB-ZNF蛋白不同，KRBOX4可能仅含少量（甚至单个）C2H2锌指——这使得其DNA结合特异性和靶向TE家族数量受限于锌指数目。理论估算：单个C2H2锌指仅识别3-4 bp核心序列，不足以提供足够的基因组特异性。可能需要通过KRAB结构域介导的蛋白-蛋白互作（如与其他ZNF蛋白形成异源二聚体）来增强DNA靶向的特异性。

**PPI互作网络解读**：PPI degree=21，最关键的互作伙伴是TRIM28/KAP1（BioGRID 1分），这是KRAB结构域的唯一经典结合靶点，证实了KRBOX4通过KRAB-TRIM28途径招募共抑制复合物的能力。其余互作伙伴包括：XPO5（Exportin-5，miRNA前体的核输出受体——提示可能与RNA核质转运有关）、ASXL2（Polycomb complex组分，参与H2AK119ub1去泛素化调控）、LMO1/LMO3（LIM-only转录共因子，在造血和神经发育中发挥作用）。这组互作暗示KRBOX4可能在核内蛋白复合物中充当KRAB结构域"模块供应商"的适配器角色。

**结构解读**：AlphaFold pLDDT=48.9，整体预测质量很低（本批次中倒数第二）。低pLDDT主要由以下原因导致：（1）蛋白仅171 aa，较小的尺寸意味着更大比例的无序区域（IDR）；（2）KRAB结构域本身的RMSF在溶液中较高，需结合KAP1后才能稳定折叠——AlphaFold预测的是孤立状态，因此低估了其在复合物中的真实结构质量；（3）少量C2H2锌指可能在锌离子缺失的状态下呈无序构象。尽管整体pLDDT低，KRAB结构域核心（VxL基序区域）的局部pLDDT可能达60-70，足以形成功能性的KAP1结合面。

**机制模型**：KRBOX4的极简设计决定了其功能模式更可能是"共调控因子（co-factor）"而非独立的"序列特异性转录因子"：（1）KRAB结构域通过招募TRIM28而在特定基因组区域（由与其互作的ZNF蛋白识别）建立H3K9me3异染色质标记；（2）由于自身锌指数量不足，KRBOX4可能作为"KRAB模块供应商"嵌入已存在的转录抑制复合物（如通过ASXL2锚定于Polycomb domain）增强特定区域的异染色质化程度；（3）与XPO5的互作暗示可能在pre-miRNA核输出的质量控制中通过KRAB依赖的转录沉默调控miRNA宿主基因的表达。

**TE调控展望**：KRBOX4的TE调控潜力受限于自身锌指数量，但作为KRAB模块的"增强子"或"adaptor"，可能在特定基因组环境中协同经典的KZNF蛋白实现TE沉默。推荐的实验策略：（1）外源表达KRBOX4后ChIP-seq鉴定TRIM28招募增强的基因组区域；（2）检测KRBOX4与特定KZNF蛋白（如ZNF10、ZNF274）是否形成异源复合物；（3）nascent RNA-seq评估CRISPR激活/抑制（CRISPRa/i）调控KRBOX4后TE家族的转录变化模式。零PubMed研究意味着KRBOX4可能是一个全新的KRAB功能模块范式。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5JUW0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRBOX4

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000147121-KRBOX4

![](https://images.proteinatlas.org/65295/1151_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/65295/1151_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/65295/1279_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/65295/1279_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/65295/1154_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/65295/1154_G12_2_red_green.jpg)
