---
type: protein-evaluation
gene: "RHBG"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RHBG 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RHBG |
| 蛋白名称 | Ammonium transporter Rh type B |
| 蛋白大小 | 458 aa / 49.5 kDa |
| UniProt ID | Q9H310 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 458 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=92 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=93.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ammonium/urea_transptr; NH4_transpt_AmtB-like_dom; RhesusRHD |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=92 broad=153
- AF pLDDT=93.7 PDB=0
- InterPro: Ammonium/urea_transptr; NH4_transpt_AmtB-like_dom; RhesusRHD
- Pfam: Ammonium_transp
- PPI degree=4 ChIP: None
39052834: Ammonia transporter RhBG initiates downstream signaling and functional responses | 19953292: The Rh protein family: gene evolution, membrane biology, and disease association | 26471760: Expression of ammonia transporters Rhbg and Rhcg in mouse skeletal muscle and th

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**氨转运蛋白的核质定位悖论**：RHBG（Ammonium transporter Rh type B, UniProt Q9H310）属于Rhesus血型氨转运蛋白家族（InterPro: RhesusRHD IPR002229, Ammonium/urea_transptr IPR029020），是位于基底侧质膜的12次跨膜转运蛋白。其氨/甲胺电中性转运功能已在爪蟾卵母细胞和肾上皮细胞中被充分验证（PMIDs:15284342, 15929723, 24077989），负责酸碱稳态维持和肾脏酸分泌。然而HPA数据明确显示该蛋白在Nucleoplasm中为Approved级别定位（核定位特异性9/10），这与12次跨膜蛋白的拓扑特征形成强烈矛盾。一个可能的解释是：RHBG的N端或C端可溶性片段经蛋白酶解后释放入核行使信号功能，类似于Notch的RIP（regulated intramembrane proteolysis）机制。

**高置信度三维结构与功能洞察**：AlphaFold pLDDT=93.7为本次50个蛋白中的顶级结构质量指标，表明AlphaFold对RHBG跨膜螺旋束的建模非常自信。该蛋白包含NH4_transpt_AmtB-like_dom（IPR024041），采用Amt/MEP/Rh氨通道家族保守的伪二重对称折叠，中央为疏水性氨传递通道。跨膜通道蛋白在核质中的潜在非经典功能包括：(1) 作为核膜氨通道调节核内pH——核内pH波动直接影响组蛋白修饰酶（如HDAC和HAT）的活性，从而间接调控染色质状态；(2) 蛋白片段作为转录辅因子发挥功能。

**低PPI度与信号通路关联**：PPI degree=4（BioGRID, 包含SH2B1和CYSRT1, score=1），互作网络极其稀疏。然而，SH2B1作为JAK-STAT信号调控接头蛋白（JAK2激酶的适配蛋白），暗示RHBG可能通过微弱的信号连接间接参与细胞因子信号——而IFN信号的STAT1激活已知影响LINE-1逆转座子表达。这是RHBG与TE调控之间较为牵强的关联线索。

**酸-碱微环境与表观遗传调控的新概念**：氨转运影响细胞内外NH3/NH4+平衡，直接调控局部pH。核内pH是染色质构型的关键物理参数——酸性pH促进组蛋白-组蛋白和组蛋白-DNA的静电互作增强，提高染色质压缩度；碱性pH削弱核小体稳定性。若RHBG或其片段影响核仁/核质pH梯度，则可通过物理化学机制影响富含AT的TE区域（Alu, L1）的可及性。然而，这种pH-TE关联假说目前纯属理论推测。

**新颖性与风险**：PubMed=92的文献量不算低，但所有文献集中于肾酸碱生理学（PMIDs:42192833, 42055369），无一篇涉及核功能。归一化得分68.9/100中核定位特异性36/40和新奇性35/50是主要支撑。这是一个需要多学科交叉验证（膜蛋白生物化学 + 核生物学 + TE基因组学）的低可行性候选，不建议作为首要靶标。


### 补充分析 (UniProt API)

**蛋白全称**: Ammonium transporter Rh type B

**功能**: Ammonium transporter involved in the maintenance of acid-base homeostasis. Transports ammonium and its related derivative methylammonium across the basolateral plasma membrane of epithelial cells likely contributing to renal transepithelial ammonia transport and ammonia metabolism. May transport either NH4(+) or NH3 ammonia species predominantly mediating an electrogenic NH4(+) transport (PubMed:15284342, PubMed:15929723, PubMed:24077989). May act as a CO2 channel providing for renal acid secret

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029020 |
| InterPro | IPR024041 |
| InterPro | IPR002229 |
| Pfam | PF00909 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SH2B1 | BioGRID | 1 |
| CYSRT1 | BioGRID | 1 |
| KRTAP19-1 | BioGRID | 0 |
| KRTAP19-2 | BioGRID | 0 |