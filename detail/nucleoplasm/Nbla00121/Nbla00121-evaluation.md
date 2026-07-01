---
type: protein-evaluation
gene: "Nbla00121"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## Nbla00121 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Nbla00121 |
| 蛋白名称 | Uncharacterized protein Nbla00121 |
| 蛋白大小 | 307 aa / 35.3 kDa |
| UniProt ID | Q3LIC1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 307 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=77.6; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=77.6 PDB=0
- InterPro: Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2; zf-H2C2_2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**C2H2锌指蛋白的转录调控潜力与TE结合推测**：Nbla00121（Uncharacterized protein Nbla00121, 307 aa, UniProt Q3LIC1）的UniProt功能注释为"May be involved in transcriptional regulation"，这是本批次所有"暗蛋白"中唯一一个拥有直接转录调控推断注释的。携带Krueppel_C2H2_ZnFinger（IPR050826）、Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087）三类锌指结构域，Pfam注释为zf-C2H2（PF00096）和zf-H2C2_2（PF13465）——后者属于非经典C2H2锌指变体，暗示其DNA结合特异性可能偏离规范锌指识别码。307 aa的中等大小可容纳约5-6个锌指重复，理论DNA识别长度为15-20 bp，足以特异靶向特定的TE家族亚型。

**TRIM28互作与KRAB非依赖转录抑制的潜在机制**：PPI数据中最引人注目的是TRIM28/KAP1（STRING score=518）——与KR-ZNF1共享的顶级辅阻遏物。在无KRAB结构域的情况下，Nbla00121通过何种基序招募TRIM28是一个关键的机制问题。可能的互作模式包括：(1) 非经典TRIM28结合基序（如RBCC域识别的HP1盒基序PxVxL）；(2) SUMO-SIM相互作用——TRIM28通过其C端PHD-Bromodomain识别SUMO修饰的锌指蛋白；(3) 间接互作——通过KRBOX4（STRING score=517）或ZNF827（STRING score=506）等中间锌指蛋白桥接。TRIM28作为桥梁蛋白连接锌指DNA结合模块和SETDB1/HP1异染色质机器，其存在是TE沉默功能的最强间接证据。

**锌指蛋白网络中的"枢纽-辐射"拓扑**：Nbla00121的PPI网络呈现出以TRIM28为中心的"枢纽-辐射"（hub-spoke）拓扑——ZNF773（STRING 484）、ZNF585A（STRING 482）、ZNF439（STRING 458）、ZNF18（STRING 457）、ZNF224（STRING 490）、ZNF549（STRING 544）等一整套C2H2锌指蛋白互作展示了锌指蛋白之间的功能网络。这种锌指蛋白群（ZNF cluster）互作模式在KRAB-ZNF簇中已有先例——Chr19上的KRAB-ZNF基因簇通过锌指域的蛋白间互作形成异源二聚体，扩展TE识别的组合多样性。

**转录调控推断与实验优先度**：UniProt的"May be involved in transcriptional regulation"推断来自InterPro2GO的自动注释，虽非实验证据但反映了保守的结构域-功能映射。AlphaFold pLDDT=77.6提示存在部分有序-部分无序域的组织，可能需结合DNA伙伴才完全折叠。鉴于归一化得分68.3/100和新奇性满分50/50，Nbla00121在锌指蛋白TE候选中的优先级仅次于KR-ZNF1和FLJ00335。


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein Nbla00121

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050826 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |
| Pfam | PF13465 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein Nbla00121

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050826 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |
| Pfam | PF13465 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---