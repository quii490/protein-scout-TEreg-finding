---
type: protein-evaluation
gene: "DKFZp666M039"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp666M039 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp666M039 |
| 蛋白名称 | Uncharacterized protein DKFZp666M039 |
| 蛋白大小 | 289 aa / 32.7 kDa |
| UniProt ID | Q658Q3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 289 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=85.0; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=85.0 PDB=0
- InterPro: Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.9/100** | **nucleoplasm**
TE candidate: Krueppel_C2H2_ZnFinger; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**多锌指架构与DNA结合潜力**：DKFZp666M039（289 aa, UniProt Q658Q3）的InterPro注释为Krueppel_C2H2_ZnFinger（IPR050826）、Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087），共计三类C2H2锌指相关结构域。Kruppel型C2H2锌指得名于果蝇Kruppel基因，其典型特征是在锌指间存在保守的TGEKP连接序列，形成串联排列的指状DNA结合模块。该蛋白含289 aa，在已知C2H2锌指蛋白中属于中等大小，理论上可容纳4-6个锌指重复单元。AlphaFold pLDDT=85.0表明整体折叠高置信度，Znf_C2H2_sf超折叠（全β结构）在三维空间中将形成指状突起，每个指状单元插入DNA大沟。然而PDB=0意味着缺乏锌指-DNA共晶结构，DNA识别特异性完全未知。

**KRAB结构域缺失的功能含义**：与DKFZp666C237类似，DKFZp666M039同样不携带KRAB抑制结构域，这使其归类于非KRAB型C2H2锌指蛋白。值得注意的是，所有已知的高置信度TE沉默锌指蛋白（ZNF91、ZNF93、ZNF100、ZNF675等）均为KRAB-ZNF型。非KRAB型C2H2蛋白在TE调控中的潜在机制仍是领域空白——可能通过以下方式：(1) 作为竞争性抑制剂，结合TE启动子区域阻止内源转录因子激活；(2) 通过非KRAB的转录抑制域（如BTB/POZ结构域，但该蛋白也缺乏）实现转录沉默；(3) 作为结构蛋白通过多聚化形成空间位阻。该蛋白的IPR050826分类指出了一个庞大的多成员亚家族，可能反映了基因扩增驱动的TE防御功能演化。

**完全新颖的"暗物质"蛋白**：PubMed=0（strict和broad均为0）、PPI degree=0（与DKFZp666C237完全一致），表明该蛋白处于功能注释的绝对空白区。此类蛋白在蛋白质组学研究中通常属于"已检测但无功能关联"类别。TE调控候选蛋白需要满足的至少一个支持条件是锌指介导的核酸结合——这一点技术上可通过电泳迁移率实验（EMSA）或SELEX进行体外验证。AlphaFold结构提供了锌指域的三维坐标，可用作分子对接计算的基础，预测其对特定TE衍生DNA序列（如Alu、L1 5'UTR、LTR启动子）的结合偏好。

**机制假说与实验优先级**：考虑到该蛋白缺乏核定位证据（核定位特异性5/10）、无PPI搭档、无文献支持，其TE调控候选资格完全依赖锌指结构域的DNA结合潜力和新颖性优势（50/50）。若推进实验验证，优先级应为：(1) 重组表达并验证锌指域的Zn2+配位和DNA结合活性；(2) 通过ChIP-exo或HT-SELEX确定DNA结合基序；(3) 比对所得基序与人类TE序列数据库（Repbase/Dfam）。鉴于归一化评分68.9/100，这是一项高风险高回报的"盲探"候选。


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp666M039

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050826 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp666M039

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050826 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---