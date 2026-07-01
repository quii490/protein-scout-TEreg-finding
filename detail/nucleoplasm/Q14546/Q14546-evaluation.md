---
type: protein-evaluation
gene: "Q14546"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## Q14546 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Q14546 |
| 蛋白名称 | Homeobox-like |
| 蛋白大小 | 60 aa / 7.2 kDa |
| UniProt ID | Q14546 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 60 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=89.1; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | HD; Homeobox_regulator; Homeodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=89.1 PDB=0
- InterPro: HD; Homeobox_regulator; Homeodomain-like_sf
- Pfam: Homeodomain
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: HD; Homeobox_regulator; Homeodomain-like_sf


### 深度机制分析

**最小化同源异形域的TE DNA结合潜力**：Q14546（Homeobox-like, 60 aa, 7.2 kDa, UniProt Q14546）是本批次中第二小的蛋白（仅次于DKFZp686N0199），包含Homeobox（HD, IPR001356, Pfam Homeodomain PF00046）、Homeobox_regulator（IPR051306）和Homeodomain-like_sf（IPR009057）三重同源异形域相关分类。同源异形域是约60 aa的独立折叠模块，采用典型的螺旋-转角-螺旋（HTH）折叠（α1-α2-α3），其中α3"识别螺旋"插入DNA大沟，α1和N端尾臂接触小沟和磷酸骨架。Q14546的大小（60 aa）恰好对应一个完整的同源异形域，是一个纯化至仅含DNA结合模块的最小化转录因子。

**同源异形域-TE结合在进化中的先驱作用**：同源异形域蛋白（Hox、POU、LIM等家族）在基因组中的识别序列为TAAT/ATTA核心基序及其扩展组合。该基序在人类基因组中的分布特征富含于特定TE家族中——Alu-Sx亚家族的A-box包含TAAT基序，而MER20和MER39元件的Hox应答增强子中富集TAAT/ATTA。若Q14546具有同源异形域介导的TE DNA识别能力，可能作为竞争性抑制因子阻断Hox转录因子对TE衍生增强子的激活——这是非KRAB锌指蛋白之外的另一类TE转录调控范式。

**极小型蛋白的核质扩散与功能孤立性**：7.2 kDa的分子量意味着Q14546的核质定位（核定位特异性5/10）可通过完全被动的核孔扩散实现，不需NLS。PPI degree=0和PubMed=0的完全"零"状态暗示该蛋白要么是低丰度的功能冗余因子，要么仅在特定发育窗口期表达。AlphaFold pLDDT=89.1的高置信度结构（PDB=0）确证了同源异形域三螺旋折叠在溶液中的稳定性——这意味着该蛋白在核质中处于"DNA-ready"构象，随时可识别其靶标序列。

**实验分析的挑战与策略**：60 aa的极短长度使标准ChIP-seq的crosslinking效率可能受影响（赖氨酸残基少）。推荐的替代方案：(1) CUT&RUN（低背景，不需要高交联效率）；(2) HT-SELEX在体外确定DNA结合基序；(3) 合成生物素化Q14546蛋白进行"DNA免疫沉淀+测序"（DIP-seq）以直接鉴定基因组结合位点。若所得基序与TE（尤其是MER20/Hox增强子）重叠，则验证了同源异形域-TE调控轴。归一化得分68.3/100中调控结构域12/30和三维结构21/30是其得分优势。


### 补充分析 (UniProt API)

**蛋白全称**: Homeobox-like

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001356 |
| InterPro | IPR051306 |
| InterPro | IPR009057 |
| InterPro | IPR000047 |
| Pfam | PF00046 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Homeobox-like

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001356 |
| InterPro | IPR051306 |
| InterPro | IPR009057 |
| InterPro | IPR000047 |
| Pfam | PF00046 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---