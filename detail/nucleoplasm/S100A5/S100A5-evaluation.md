---
type: protein-evaluation
gene: "S100A5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## S100A5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | S100A5 |
| 蛋白名称 | Protein S100-A5 |
| 蛋白大小 | 92 aa / 10.7 kDa |
| UniProt ID | P33763 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 92 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=37 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=93.9; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | EF-hand-dom_pair; EF_Hand_1_Ca_BS; EF_hand_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=37 broad=52
- AF pLDDT=93.9 PDB=4
- InterPro: EF-hand-dom_pair; EF_Hand_1_Ca_BS; EF_hand_dom
- Pfam: S_100
- PPI degree=4 ChIP: None
15542977: Meningioma: an update. | 33528559: Were Ancestral Proteins Less Specific? | 29201357: Human S100A5 binds Ca(2+) and Cu(2+) independently.

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein S100-A5

**功能**: Binds calcium, zinc and copper. One subunit can simultaneously bind 2 calcium ions or 2 copper ions plus 1 zinc ion. Calcium and copper ions compete for the same binding sites

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| InterPro | IPR034325 |
| InterPro | IPR001751 |
| InterPro | IPR013787 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| S100A16 | STRING | 761 |
| HRNR | STRING | 732 |
| TNFRSF6B | BioGRID | 0 |
| CCDC170 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P33763-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196420-S100A5

![](https://images.proteinatlas.org/64184/1501_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/64184/1501_F3_3_red_green.jpg)
![](https://images.proteinatlas.org/64184/1529_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/64184/1529_E10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 52**

| 41027018 | Distinct odorant receptor response patterns to aliphatic odorants in freely behaving mice. | Chem Senses 2025 |
| 39128058 | Prognostic Value of S100 Family mRNA Expression in Hepatocellular Carcinoma. | Turk J Gastroenterol 2024 |
| 37611365 | A human identification system for hair shaft using RNA polymorphism. | Forensic Sci Int Genet 2023 |

### 深度机制分析

S100A5（92 aa, 10.7 kDa）属于S100钙结合蛋白家族，是该家族中神经系统中相对高表达的成员。其结构域架构为经典的EF-hand钙结合蛋白折叠——N端假EF-hand（S100特异性的S100_hand）和C端规范EF-hand（IPR002048），两者通过铰链区域连接，形成二聚体界面。EF-hand基序由螺旋-环-螺旋构象组成，环区含有保守的天冬氨酸和谷氨酸残基以配位钙离子。AlphaFold预测pLDDT高达93.9，并已有4个PDB条目提供高分辨率实验结构——这是25个候选蛋白中结构信息最优的之一。

S100A5以其多金属结合特性著称——一个亚基可同时结合两个钙离子或两个铜离子加一个锌离子，钙和铜竞争同一结合位点（PMID:29201357）。这种金属选择的多样性使S100A5成为细胞内金属离子的传感器和缓冲器。在钙结合状态下，S100A5经历构象变化，暴露出疏水裂隙以结合靶蛋白，激活下游信号通路。

HPA将S100A5定位为Nucleoplasm（Approved级别），这与S100家族蛋白钙依赖性核转位的已知范式一致。PPI网络（BioGRID degree=4, STRING扩展）中，S100A16（STRING 761，同一家族成员）是最强互作伙伴，可能形成异源二聚体；HRNR（STRING 732，皮屑蛋白）的互作提示上皮/屏障功能。

在TE调控语境下，S100A5的核定位通过两条主要通路产生潜在影响。其一，钙信号-转录偶联：核内钙浓度的波动（如通过核膜IP3受体释放）可激活S100A5，其构象变化可能暴露核定位信号或直接结合核内靶蛋白（如转录因子）来调控基因表达。其二，金属稳态：核内锌和铜是许多转录因子（如锌指蛋白）的结构辅助因子和染色质修饰酶（如组蛋白去乙酰化酶HDAC）的催化辅因子。S100A5通过缓冲核内游离锌/铜水平来间接调控这些蛋白的活性，从而影响TE位点的表观遗传状态。

S100家族在肿瘤中的预后价值已在肝细胞癌中获得验证（PMID:39128058），S100A5作为钙/金属信号的核内介体，其通过表观遗传修饰酶辅因子可用性调控来影响TE表达的假说值得进一步验证。pLDDT=93.9和4个PDB结构为结构导向的药物设计提供了极佳的起点——设计特异性阻断S100A5金属结合或靶蛋白互作的小分子可能成为调控TE表达的间接手段。

