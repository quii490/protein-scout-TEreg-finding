---
type: protein-evaluation
gene: "DKFZp666C237"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp666C237 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp666C237 |
| 蛋白名称 | Uncharacterized protein DKFZp666C237 |
| 蛋白大小 | 219 aa / 25.2 kDa |
| UniProt ID | Q658L7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 219 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=88.3; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Znf_C2H2-type; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=88.3 PDB=0
- InterPro: Znf_C2H2-type; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.9/100** | **nucleoplasm**
TE candidate: Znf_C2H2-type; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**结构域架构与DNA结合潜力**：DKFZp666C237（219 aa, UniProt Q658L7）携带三个C2H2锌指结构域（InterPro: Znf_C2H2-type IPR013087, Znf_C2H2_sf IPR036236; Pfam: zf-C2H2 PF00096），属于经典Kruppel型锌指蛋白超家族。C2H2锌指是高等真核生物中最丰富的DNA结合结构域，以ββα折叠方式识别特定DNA序列的大沟。该蛋白的pLDDT值为88.3（AlphaFold），表明整体折叠质量高，锌指区域在三维空间中形成可预测的DNA识别面。关键问题在于缺乏实验核定位信号（NLS）注释——尽管C2H2锌指蛋白通常通过被动扩散或非经典核孔通道进入核质，但缺乏明确的核输入机制降低了其作为TE调控因子的可信度。

**PPI网络与辅因子招募**：该蛋白当前PPI degree=0（BioGRID及STRING均未检出互作伙伴），属于完全未表征的"孤儿"蛋白。对于C2H2锌指蛋白而言，其功能发挥通常依赖于与辅阻遏物（如TRIM28/KAP1）或辅激活物的互作。以KRAB-ZNF家族为参考，典型的TE沉默锌指蛋白（如ZNF91/93）通过N端KRAB结构域招募TRIM28-SETDB1复合物，在逆转座子位点沉积H3K9me3沉默标记。DKFZp666C237缺乏KRAB结构域，提示其若具有锌指介导的DNA识别能力，则可能通过非经典机制（如直接竞争TF结合位点或招募其他染色质修饰因子）影响TE调控。

**结构预测与TE识别假说**：基于AlphaFold pLDDT=88.3的高置信度三维结构，该蛋白的锌指串联排列（Znf_C2H2_type × 3）可能形成连续的DNA识别界面。C2H2锌指蛋白中，每个锌指模块通常识别3-4 bp DNA序列，该蛋白的3个串联锌指理论识别能力为9-12 bp，足以对TE末端重复序列（LTR或ITR）产生序列特异性。然而，PDB结构数据缺失（PDB=0），锌指-DNA共晶结构不存在，意味着DNA靶标尚无法预测。其InterPro归属IPR050758（C2H2 ZF蛋白家族）指向转录调控功能。

**新颖性驱动的TE调控机会**：PubMed=0的完全"暗物质"状态既是挑战也是机遇。在人类基因组中，~700个C2H2锌指蛋白中约三分之一的KRAB-ZNF亚家族已被证明参与逆转座子沉默，但非KRAB型C2H2蛋白在TE调控中的角色几乎完全未知。DKFZp666C237作为小型（25.2 kDa）非KRAB型多锌指蛋白，可能代表了一类尚未被发现的TE调控模式——通过锌指直接识别TE序列而不依赖经典的KRAB-TRIM28通路。

**机制假说与实验验证方向**：若该蛋白具有TE结合能力，最可能的机制是：(1) 直接结合TE启动子区域的特定DNA基序，竞争内源性转录因子或RNA Pol II的结合；(2) 作为结构蛋白改变TE区域局部染色质构型。鉴于归一化评分68.9/100（新颖性满分50/50），ChIP-seq或CUT&RUN是验证其TE结合的首选实验手段。总体而言，该蛋白在结构域层面具备TE调控的分子基础（C2H2锌指），但缺乏实验证据（无PPI、无核定位验证），属高风险高回报候选靶标。


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp666C237

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050758 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp666C237

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050758 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---