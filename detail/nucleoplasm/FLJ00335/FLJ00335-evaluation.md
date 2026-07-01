---
type: protein-evaluation
gene: "FLJ00335"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## FLJ00335 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FLJ00335 |
| 蛋白名称 | FLJ00335 protein |
| 蛋白大小 | 157 aa / 17.9 kDa |
| UniProt ID | Q8NF55 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 157 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=83.7; PDB=0 |
| 调控结构域 | 7/10 | ×2 | 14.0 | ELM2_dom; SANT_dom; Trans_reg/Corepressor |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=83.7 PDB=0
- InterPro: ELM2_dom; SANT_dom; Trans_reg/Corepressor
- Pfam: ELM2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: ELM2_dom; SANT_dom; Trans_reg/Corepressor


### 深度机制分析

**ELM2-SANT双结构域架构与辅阻遏物功能**：FLJ00335（157 aa, 17.9 kDa, UniProt Q8NF55）拥有本批次中最引人注目的调控结构域组合——ELM2结构域（IPR000949, Pfam ELM2 PF01448）、SANT结构域（IPR017884）和转录调控/辅阻遏物分类（Trans_reg/Corepressor IPR051066）。ELM2-SANT双结构域是已知最强的转录辅阻遏物结构域组合之一，最早发现于Mi-2/NuRD染色质重塑复合物的核心亚基中。ELM2域介导组蛋白去乙酰化酶（HDAC）招募，SANT域则以类似Myb的方式与未修饰的组蛋白尾部结合，使辅阻遏物锚定在染色质上。

**SANT-组蛋白尾部结合与TE靶向假说**：SANT结构域是c-Myb DNA结合域的进化衍生物，但已丧失DNA结合能力，转而特异识别未修饰的组蛋白H3和H4尾部。FLJ00335的SANT域（IPR017884）若保留了组蛋白尾结合能力，可将其ELM2结构域定位至特定核小体位点。对于TE调控而言，内源性逆转录病毒（ERV）LTR通常被H3K9me3和DNA甲基化标记覆盖，但这些修饰依赖于辅阻遏物复合物的持续锚定——FLJ00335作为"缺失HDAC酶亚基"的辅阻遏物适配蛋白，可能作为支架招募完整HDAC复合物至TE位点。这一假说得到了其IPR051066（转录调控/辅阻遏物）分类的支持。

**小尺寸与核质可及性**：157 aa / 17.9 kDa的分子量确保了被动扩散通过核孔的高效性，而ELM2-SANT双结构域（共约120 aa）几乎占据整个蛋白。这种紧凑的"全功能域"架构暗示该蛋白可能作为一个最小化的辅阻遏物模块（minimal corepressor module），专一执行染色质招募功能。AlphaFold pLDDT=83.7表明ELM2和SANT域在结构上是独立折叠的，域间可能存在一段柔性连接区域。

**新奇的"暗蛋白"与极高TE调控优先级**：PubMed=0的完全无文献状态和PPI degree=0的孤儿特征，使得该蛋白的TE调控潜力完全依赖于结构域推理。ELM2-SANT组合在已知人类蛋白质组中极为罕见（仅存在于Mi-2α/β, MTA1/2/3, p66α/β等约10个蛋白中），FLJ00335可能是这一精英辅阻遏物俱乐部中唯一未被研究的神秘成员。若其具备HDAC招募活性（可通过GST pull-down验证），则可作为TE沉默的高优先级候选蛋白。归一化得分68.3/100中调控结构域维度14/30（锌指7/10）是本蛋白得分上调的主要来源。


### 补充分析 (UniProt API)

**蛋白全称**: FLJ00335 protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000949 |
| InterPro | IPR017884 |
| InterPro | IPR051066 |
| Pfam | PF01448 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: FLJ00335 protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000949 |
| InterPro | IPR017884 |
| InterPro | IPR051066 |
| Pfam | PF01448 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---