---
type: protein-evaluation
gene: "SPMIP9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPMIP9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPMIP9 |
| 蛋白名称 | Protein SPMIP9 |
| 蛋白大小 | 180 aa / 20.6 kDa |
| UniProt ID | Q96LM6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 180 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=55.3; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | SPMIP9 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Supported)
- PubMed: strict=0, broad=0
- AF pLDDT: 55.3 / PDB: 0
- InterPro: SPMIP9
- Pfam: TSC21
- PPI degree=0 ChIP: None


### 4. 总体评价
★★★★  **68.9/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**精子微管结合蛋白的非经典核质分布**：SPMIP9（Protein SPMIP9, 180 aa, UniProt Q96LM6）被功能注释为精子鞭毛轴丝双联微管内部蛋白（Microtubule inner protein, MIP），是动力蛋白修饰的双联微管的结构组分（UniProt annotation: InterPro SPMIP9 IPR029361, Pfam TSC21 PF15217）。其唯一已知功能为参与精子鞭毛运动相关的微管结构组装——这是一个高度特化的细胞骨架功能，与核质转录调控完全无关。然而HPA标注该蛋白在Nucleoplasm中为Supported级别定位（核定位特异性8/10），这是令人困惑的亚细胞定位。

**低置信度三维结构的限制**：AlphaFold pLDDT=55.3的极低置信度（已与未知功能蛋白预期一致）和PDB=0的结构缺失，意味着该蛋白在溶液中的真实构象可能与AF2预测存在巨大偏差。TSC21结构域（Pfam PF15217）的功能尚未被结构解析，但一般认为其参与微管腔内侧的蛋白-蛋白互作。如果存在核内异构体（通过可变剪接或翻译后修饰产生），则可能在核内行使完全不同的功能。

**无PPI无文献的"双零"困境**：PPI degree=0（BioGRID和STRING均无互作数据）和PubMed=0（strict和broad均为0）使该蛋白成为完全无功能注释的"暗蛋白"。在已报道的~20,000个人类蛋白编码基因中，此类完全无文献记录的蛋白极少见。值得注意的是，精子鞭毛蛋白通常经历转录后调控以抑制其在体细胞中的异位表达——若SPMIP9在非生殖细胞中出现核质定位，这可能是HPA抗体的非特异性信号假阳性。

**TE调控的最低候选概率**：基于以下逻辑链推断TE调控潜力：(1) 微管结合蛋白与染色质调控之间不存在已知的分子交汇点；(2) SPMIP9缺乏任何DNA/RNA结合结构域；(3) 其核定位证据来源不确定（Supported而非Approved）；(4) 蛋白过小（20.6 kDa）可能通过被动扩散经过核孔。归一化评分68.9/100完全由新颖性满分（50/50）和核定位得分（32/40）驱动，实际TE调控的分子基础接近于零。建议在TE筛选中赋予最低优先级。

**微管-核质桥接假说**：唯一的理论可能性是通过微管动力学间接影响细胞核——核膜蛋白SUN-KASH复合物（LINC complex）通过微管-核骨架连接调控核质机械力传导，而机械力可能影响核孔通透性和染色质组织。然而，SPMIP9是鞭毛轴丝（非胞质微管）的专一性组分，这一间接假说基本不成立。


### 补充分析 (UniProt API)

**蛋白全称**: Protein SPMIP9

**功能**: Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in flagella axoneme

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029361 |
| Pfam | PF15217 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Protein SPMIP9

**功能**: Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in flagella axoneme

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029361 |
| Pfam | PF15217 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---