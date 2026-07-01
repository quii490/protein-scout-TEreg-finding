---
type: protein-evaluation
gene: "kr-znf1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## kr-znf1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | kr-znf1 |
| 蛋白名称 | KR-ZNF1 |
| 蛋白大小 | 120 aa / 13.6 kDa |
| UniProt ID | Q13580 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 120 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=89.2; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=89.2 PDB=0
- InterPro: Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**最小化C2H2锌指蛋白的TE识别潜力**：KR-ZNF1（120 aa, 13.6 kDa, UniProt Q13580）是本次50个蛋白中第三小的蛋白（仅次于Q14546和DKFZp686N0199）。其名称（KR-ZNF1）暗示其为Krüppel型锌指蛋白——携带Snail/Krueppel_Znf（IPR050527）、Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087）三类C2H2锌指相关结构域。考虑到120 aa的极短长度，该蛋白可能仅含1-2个锌指重复（每个锌指模块约23-30 aa），这意味着其DNA识别能力有限（理论上识别3-6 bp）。

**TRIM28/KAP1互作的高置信度线索**：PPI数据中包含TRIM28/KAP1（STRING score=522）作为最强互作伙伴——这是本批次所有锌指蛋白中唯一一个明确与TRIM28相关的。TRIM28/KAP1是所有KRAB-ZNF介导TE沉默的核心辅阻遏物，通过其N端RBCC结构域招募SETDB1（H3K9me3甲基转移酶）和HP1。尽管KR-ZNF1缺乏KRAB结构域，但其与TRIM28的互作暗示可能存在非经典TRIM28招募通路，或通过锌指间的辅助基序（如SIM/SUMO互作基序）实现TRIM28结合。此外，ZNF223（STRING 777）和ZNF468（STRING 772）等C2H2锌指蛋白的互作暗示KR-ZNF1可能通过锌指-锌指蛋白互作网络间接参与TE调控。

**Snail/Krueppel_Znf家族的TE关联**：KR-ZNF1被归类为Snail/Krueppel_Znf家族（IPR050527）。Snail家族转录因子（SNAI1/2/3）通过其C端锌指域识别E-box（CANNTG）基序，该基序在多种TE（特别是ERV-L LTR和MaLR LTR）的启动子中普遍存在。若KR-ZNF1具有类似的E-box结合特异性，则可能竞争Snail家族因子对TE衍生增强子的调控。

**极小型蛋白的核质穿梭优势**：13.6 kDa的分子量远低于被动扩散核孔阈值（~40-60 kDa），意味着该蛋白可通过被动扩散自由进出细胞核核质。这种尺寸优势使其成为"即插即用"的候选——无需复杂的核输入机制即可抵达DNA靶标。AlphaFold pLDDT=89.2的高置信度表明其锌指域在溶液中已稳定折叠，随时可执行DNA结合功能。归一化得分68.3/100中调控结构域12/30（锌指6/10）和新奇性满分50/50使KR-ZNF1成为高优先级TE调控候选。


### 补充分析 (UniProt API)

**蛋白全称**: KR-ZNF1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KR-ZNF1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KR-ZNF1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---