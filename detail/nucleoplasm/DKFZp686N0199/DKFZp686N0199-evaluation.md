---
type: protein-evaluation
gene: "DKFZp686N0199"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp686N0199 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp686N0199 |
| 蛋白名称 | Uncharacterized protein DKFZp686N0199 |
| 蛋白大小 | 58 aa / 7.0 kDa |
| UniProt ID | Q7Z3W8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 58 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=95.8; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=95.8 PDB=0
- InterPro: Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**极微型单锌指蛋白的DNA结合"探针"功能**：DKFZp686N0199（58 aa, 7.0 kDa, UniProt Q7Z3W8）是本批次中最小的蛋白（甚至小于Q14546的60 aa），仅包含Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087）两个锌指分类，Pfam注释为zf-C2H2（PF00096）。58 aa的长度仅足以容纳单个C2H2锌指模块（~23-25 aa）及两端短连接区——一个单锌指理论上只能识别3-4 bp DNA，不具备任何序列特异性，因此该蛋白的DNA结合能力可以忽略不计。AlphaFold pLDDT=95.8是本批次所有50个蛋白中的最高置信度值——这在单域小蛋白中非常典型，因为AF2对单结构域、无长loop的小蛋白预测精度极高。

**核质"漂流"与微弱的转录干扰假说**：7.0 kDa的分子量甚至是足以通过核孔自由被动扩散的——任何大于5 kDa的分子都可穿越核孔，但效率随尺寸增加而降低。DKFZp686N0199的超小尺寸使它在胞质-核质间快速平衡——可能作为一个"锌指探针"在核质中扫描DNA大沟的非特异性电接触。若该单锌指具有微弱的序列偏好（如富G/C三联体），可能在极高水平表达时（如基因扩增或启动子去抑制）通过竞争占据染色质结合蛋白的DNA位点而干扰TE启动子的转录。这种"惰性DNA占位"机制类似于原核生物中的DNA结合蛋白（如HU, IHF）的转录调控模式。

**最低优先级推荐**：PPI degree=0、PubMed=0、仅含单锌指的结构域限制和缺乏核定位证据（5/10），使该蛋白成为TE调控候选中的最弱候选之一。任何TE调控的生物学功能需通过单锌指的非特异性DNA结合来解释，这在分子水平上缺乏说服力。归一化得分68.3/100几乎全部由新颖性满分（50/50）和三维结构21/30驱动。建议赋予"暗蛋白"中的最低优先级。


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686N0199

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686N0199

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---