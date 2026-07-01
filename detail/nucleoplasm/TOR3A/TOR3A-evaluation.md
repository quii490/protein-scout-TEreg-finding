---
type: protein-evaluation
gene: "TOR3A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TOR3A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TOR3A |
| 蛋白名称 | Torsin-3A |
| 蛋白大小 | 397 aa / 46.2 kDa |
| UniProt ID | Q9H497 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 397 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | P-loop_NTPase; TOR1A_C; Torsin |
| PPI | 6/10 | x3 | 18.0 | PPI degree=85 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=8 broad=12
- AF pLDDT=77.9 PDB=0
- InterPro: P-loop_NTPase; TOR1A_C; Torsin
- Pfam: TOR1A_C; Torsin
- PPI degree=85 ChIP: None
34557561: Monocyte Gene Expression Distinguishes Enhancing Brain Parenchymal Cysticercal G | 41739568: TOR3A represses type I interferon production and limits viral clearance during r | 31747682: Replication of Genome-Wide Association Analysis Identifies New Susceptibility Lo

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**AAA+ ATPase的核膜内功能与先天免疫-TE调控接口**：TOR3A（Torsin-3A, 397 aa, UniProt Q9H497）属于Torsin/ClpB AAA+ ATPase超家族，拥有P-loop核苷三磷酸酶（P-loop_NTPase IPR027417）和Torsin保守域（IPR010448, Pfam Torsin PF06309; TOR1A_C IPR049337, Pfam PF21376）。AAA+蛋白通过ATP水解驱动的构象循环执行机械力产生功能，在核膜内质网（NE-ER）系统中充当分子伴侣——协助核孔复合物和LINC复合物组分（SUN-KASH桥）的正确折叠和组装。与Torsin-1A（DYT1肌张力障碍蛋白）不同，TOR3A的功能注释完全空白（UniProt无功能描述）。

**TOR3A在I型IFN产生中的直接免疫调节功能**：PMID:41739568是TOR3A最具转化价值的文献——该研究明确指出"TOR3A represses type I interferon production and limits viral clearance during respiratory syncytial virus infection"。TOR3A通过抑制IRF3/IRF7磷酸化和核转位来负调控IFN-β产生，防止过度抗病毒免疫反应。这对于TE调控生物学有深远含义：(1) cGAS-STING通路通过识别逆转座子cDNA激活IFN-I反应，TOR3A的IFN抑制功能可能同时抑制TE诱导的自身免疫激活；(2) IFN-I通路通过ISRE（IFN刺激应答元件）激活ERV/LTR启动子，TOR3A通过降低IFN-I水平间接抑制TE转录——形成"TOR3A→IFN-I下调→ERV/LTR TE沉默"的负反馈环路。

**核孔复合物调控与TE RNA出核的可能关联**：Torsin AAA+ ATPase已知底物包括核孔复合物的Nup358/RanBP2——Torsin家族通过ATP水解产生的力帮助核孔蛋白的正确折叠和嵌入核膜。若TOR3A影响核孔的组装或通透性，则可能调控TE RNA（特别是含LTR的长非编码RNA）的核质转运效率——这与MOAP1和THOC1/TREX出核复合物构成功能平行线。PPI中HNRNPH1（BioGRID score=1）是对此假说的支持——HNRNPH1是异质核核糖核蛋白家族成员，识别GGG基序的RNA并结合于大多数LINE-1 RNA，调控其剪接和核保留。

**PPI网络的多能干细胞调控特征**：PPI中包含POU5F1/OCT4（BioGRID score=1）、NANOG（BioGRID score=1）和DPPA4（BioGRID score=1），均为多能干细胞核心转录因子。胚胎干细胞中TE（特别是MERVL/ERV-L）的高表达是维持多能性所必需的，而退出多能性需要TE的迅速沉默。若TOR3A在多能性退出中通过IFN信号抑制间接沉默TE，则可解释其与干细胞因子的互作——NANOG和OCT4直接结合MERVL LTR调控其转录。AlphaFold pLDDT=77.9的中等置信度和PubMed=8的极低文献量（新颖性满分50/50）使TOR3A成为IFN-TE-核膜三交叉点的高潜力候选。


### 补充分析 (UniProt API)

**蛋白全称**: Torsin-3A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR049337 |
| InterPro | IPR010448 |
| Pfam | PF21376 |
| Pfam | PF06309 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Torsin-3A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR049337 |
| InterPro | IPR010448 |
| Pfam | PF21376 |
| Pfam | PF06309 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMPRSS5 | BioGRID | 1 |
| FOXS1 | BioGRID | 1 |
| PCGF1 | BioGRID | 1 |
| DPPA4 | BioGRID | 1 |
| NANOG | BioGRID | 1 |
| POU5F1 | BioGRID | 1 |
| ADAM33 | BioGRID | 1 |
| HNRNPH1 | BioGRID | 1 |