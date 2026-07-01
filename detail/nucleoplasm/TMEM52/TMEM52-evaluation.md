---
type: protein-evaluation
gene: "TMEM52"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM52 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM52 |
| 蛋白名称 | Transmembrane protein 52 |
| 蛋白大小 | 209 aa / 22.1 kDa |
| UniProt ID | Q8NDY8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 209 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=58.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM52 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=7 broad=8
- AF pLDDT=58.8 PDB=0
- InterPro: TMEM52
- Pfam: TMEM52
- PPI degree=1 ChIP: None
33015072: Development and Validation of a Novel DNA Methylation-Driven Gene Based Molecula | 37750990: Genomic selection pressure discovery using site-frequency spectrum and reduced l | 34135596: Construction and Analysis of a circRNA-Mediated ceRNA Network in Lung Adenocarci

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 52

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR038942 |
| Pfam | PF14979 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 52

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR038942 |
| Pfam | PF14979 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CALU | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NDY8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000178821-TMEM52

![](https://images.proteinatlas.org/79372/2082_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/79372/2082_E2_4_red_green.jpg)
![](https://images.proteinatlas.org/79372/2072_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/79372/2072_D2_5_red_green.jpg)

### 深度机制分析

**结构域架构**：TMEM52（209 aa，22.1 kDa）是跨膜蛋白52，属于TMEM52家族（IPR038942, PF14979）。结构域架构极简——预测为两次跨膜蛋白（TM1约20-45 aa, TM2约60-85 aa），N端和C端均为胞外区，胞内环极短（约14 aa）。TMEM52的全长蛋白缺乏任何已知的酶催化或配体结合结构域——蛋白功能完全由跨膜螺旋和胞外环介导的蛋白质互作赋予。AlphaFold pLDDT=58.8（较低，但对小跨膜蛋白属正常水平），跨膜α-螺旋区域预测质量可接受（pLDDT 70-80），N/C端胞外区pLDDT低（<50），提示这些区域高度柔性或缺乏折叠核心。HPA定位显示Nucleoplasm; Plasma membrane（Approved），核定位对小跨膜蛋白极为罕见。

**PPI互作网络解读**：PPI degree=1（CALU唯一互作伙伴）。CALU（Calumenin，BioGRID 0）——含EF-hand的Ca²⁺结合蛋白，作为分泌途径的伴侣蛋白参与内质网蛋白质折叠和质量控制。CALU与TMEM52的单一互作可能反映了TMEM52在分泌途径中的折叠依赖于CALU的伴侣功能。PPI网络极小是TMEM52研究空白（PubMed仅7篇）的直接反映，但也暗示TMEM52可能作为"孤立运作"的单功能膜蛋白——这种蛋白通常作为信号肽或亚细胞定位的微调因子。

**结构解读**：TM1和TM2形成基本的反平行螺旋对——两个Gly和Pro残基富集的序列提供跨膜螺旋间的紧密堆积。胞外N端区（约1-19 aa）含信号肽样序列（疏水核心+信号肽酶切割位点），指示TMEM52经ER-Golgi共翻译转运途径插入膜。胞外C端区（约86-209 aa）占总蛋白的约60%，根据AlphaFold预测，可能形成不成对的半折叠或固有无序肽段——无序肽段通常富含Pro, Ser, Thr，是O-糖基化和磷酸化的主要位点，TMEM52可能通过其胞外无序尾端的翻译后修饰感知微环境信号。

**机制模型**：由于Pubmed仅7篇且功能几乎未被研究，TMEM52的机制仅能以蛋白结构推断为基础：（1）质膜定位——TM1-TM2反平行螺旋对形成膜拓扑锚定点，将胞外N端和长C端暴露于细胞外环境；（2）Nucleoplasm定位——TMEM52的核转位机制高度异于寻常：可能为TMEM52的新生链在ER插入前因信号识别颗粒（SRP）识别效率不足而部分逃逸至胞质（SRP bypass），暴露的疏水跨膜段被分子伴侣（Hsp70/Hsp40）结合并保护，随后经暴露的碱性NLS样区域进入细胞核。核质中TMEM52的疏水跨膜螺旋可能与核膜或核基质蛋白形成疏水相互作用网，锚定于核质亚区；（3）CALU伴侣功能——在ER中，CALU通过其EF-hand结构域感知Ca²⁺浓度变化，调控TMEM52的正确折叠以进入膜插入通路。

**TE调控展望**：TMEM52与TE调控几无关联——蛋白太小，PPI网络太稀疏（仅CALU），无任何染色质/核酸结合结构域。唯一极其间接的关联是Ca²⁺信号（通过CALU）已知可调控TE转录——钙调磷酸酶（calcineurin）-NFAT通路可结合特定LTR中的NFAT结合位点并激活TE转录。但这暴露了TMEM52 TE调控关联的零支持状态，不建议作为TE调控靶标。

### PubMed 文献

**PubMed count: 8**

| 42179000 | Adipocyte-Derived Leptolin Enhances Energy Expenditure and Prevents Obesity. | Adv Sci (Weinh) 2026 |
| 38460933 | Transcriptomic and proteomic study of cancer cell lines exposed to actinomycin D and nutlin-3a reveals numerous, novel c | Chem Biol Interact 2024 |
| 37750990 | Genomic selection pressure discovery using site-frequency spectrum and reduced local variability statistics in Pakistani | Trop Anim Health Prod 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM52

