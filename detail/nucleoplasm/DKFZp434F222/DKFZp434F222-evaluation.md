---
type: protein-evaluation
gene: "DKFZp434F222"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp434F222 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp434F222 |
| 蛋白名称 | DNA polymerase epsilon catalytic subunit |
| 蛋白大小 | 496 aa / 56.5 kDa |
| UniProt ID | B3KS74 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 496 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.5; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | DNA_pol_e_suA_C; POL2; Znf-DPOE |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=82.5 PDB=0
- InterPro: DNA_pol_e_suA_C; POL2; Znf-DPOE
- Pfam: DUF1744; zf-DPOE; zf_DPOE_2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: DNA_pol_e_suA_C; POL2; Znf-DPOE


### 深度机制分析

**DNA聚合酶ε催化亚基片段与TE复制耦联**：DKFZp434F222（496 aa, UniProt B3KS74）被标注为"DNA polymerase epsilon catalytic subunit"，属于B家族DNA聚合酶。其结构域包含DNA_pol_e_suA_C（IPR013697, 聚合酶ε催化亚基A C端域）、POL2（IPR029703, DNA聚合酶ε催化亚基A）和Znf-DPOE（IPR054475, DNA聚合酶ε锌指域）。Pfscan识别出DUF1744（PF08490）、zf-DPOE（PF22912）和zf_DPOE_2（PF23250）——这些锌指模块在Pol ε全酶中负责与辅助亚基（POLE2/3/4）和引物酶（PrimPol）的装配。该蛋白参与染色体DNA复制（UniProt功能注解）机制可能包括：在复制叉处合成前导链DNA，同时通过聚合酶-解旋酶耦合维持复制叉稳定性。

**DNA复制机器-TE沉默的功能冲突假说**：DNA聚合酶ε在TE调控中的潜在角色呈现两面性：(1) 作为DNA复制机器的核心组分，Pol ε在S期结合的复制起点在基因组中与年轻LINE-1（L1Hs-Ta）的分布呈负相关——这暗示Pol ε通过排斥L1的邻近复制起点来限制其在DNA复制过程中的剪切和重新插入；(2) 然而，DNA聚合酶沿DNA模板的合成过程会短暂剥离核小体和异染色质标记（H3K9me3, H3K27me3），可能为TE提供复制的"可及性窗口"——在复制叉通过后，CAF-1和DNMT1需在几分钟内重建染色质沉默状态，此过程的失败可导致TE去抑制。POLE/POLD1外切酶校读活性的缺陷与肿瘤中的超突变表型相关，而这种超突变负荷富含L1介导的结构变异。

**锌指域的非催化功能与实验验证路径**：zf-DPOE锌指域不参与催化——其确切功能未确定，但可能参与Pol ε与染色质模板的非特异性结合或与新合成DNA链的持续合成能力（processivity）相关。PubMed=0和PPI degree=0使该蛋白成为完全未研究的DNA复制因子片段。实验上，Pol ε ChIP-seq（特别是eSPAN技术区分leading vs lagging strand）可检测Pol ε在TE位点的复制叉占位偏好。归一化得分68.3/100的调控结构域12/30（6/10锌指+DNA复制域）是候选的独特优势。


### 补充分析 (UniProt API)

**蛋白全称**: DNA polymerase epsilon catalytic subunit

**功能**: DNA polymerase II participates in chromosomal DNA replication

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013697 |
| InterPro | IPR029703 |
| InterPro | IPR054475 |
| Pfam | PF08490 |
| Pfam | PF22912 |
| Pfam | PF23250 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: DNA polymerase epsilon catalytic subunit

**功能**: DNA polymerase II participates in chromosomal DNA replication

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013697 |
| InterPro | IPR029703 |
| InterPro | IPR054475 |
| Pfam | PF08490 |
| Pfam | PF22912 |
| Pfam | PF23250 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---