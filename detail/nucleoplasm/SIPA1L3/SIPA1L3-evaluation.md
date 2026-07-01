---
type: protein-evaluation
gene: "SIPA1L3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SIPA1L3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SIPA1L3 |
| 蛋白名称 | Signal-induced proliferation-associated 1-like protein 3 |
| 蛋白大小 | 1781 aa / 194.6 kDa |
| UniProt ID | O60292 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Golgi apparatus; Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 1781 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=17 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=55.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PDZ; PDZ_sf; Rap/Ran-GAP_sf |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=110 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=17 broad=24
- AF pLDDT=55.5 PDB=0
- InterPro: PDZ; PDZ_sf; Rap/Ran-GAP_sf
- Pfam: PDZ; Rap-GAP_dimer; Rap_GAP
- PPI degree=110 ChIP: None
39651118: Uncovering the electrical synapse proteome in retinal neurons via in vivo proxim | 27993984: An Epha4/Sipa1l3/Wnt pathway regulates eye development and lens maturation. | 33130294: Host genetics influences the relationship between the gut microbiome and psychia

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**多结构域信号支架蛋白与核质功能的张力**：SIPA1L3（Signal-induced proliferation-associated 1-like protein 3, 1781 aa, UniProt O60292）是本研究批次中分子量最大的蛋白（194.6 kDa）。其结构域架构包含PDZ结构域（IPR001478, Pfam PDZ）、Rap/Ran-GAP超折叠（IPR035974）和Rap-GAP二聚化域（Pfam Rap-GAP_dimer），构成了经典的信号支架蛋白拓扑。PDZ结构域通常通过识别靶蛋白C端PDZ结合基序（class I: X-S/T-X-Φ-COOH）介导蛋白-蛋白互作，在细胞极性、细胞连接组装中发挥核心功能。该蛋白的已知生理功能集中在晶状体上皮细胞形态发生和极性维持（PMID:26231217），PDZ介导的与AMOT-Patj紧密连接复合物的相互作用抑制是其分子机制的核心（PMID:41088697）。

**核质定位的矛盾与TE调控窗口**：HPA数据显示该蛋白定位于Golgi apparatus、Nucleoplasm和Plasma membrane（核定位特异性8/10, Approved evidence）。一个194.6 kDa的蛋白出现在核质中是反直觉的——其分子量远超被动扩散的核孔阈值（~40-60 kDa），因此必然存在主动核输入机制。可能的核定位信号（NLS）尚未被实验鉴定。PPI数据中出现了ELAVL1（HuR, STRING）——一种经典的RNA结合蛋白，穿梭于核质与胞质之间并参与mRNA稳定性和翻译调控。若SIPA1L3通过ELAVL1介导的核质穿梭进入核内，则可能在核内执行与胞质不同的信号功能。

**Rap-GAP信号与染色质调控的潜在交汇**：Rap/Ran-GAP超折叠赋予该蛋白GTPase激活蛋白功能，可能调控Rap或Ran小G蛋白家族。Ran GTPase是核质转运的核心调控因子，Ran-GTP梯度驱动importin-α/β介导的核输入和exportin介导的核输出。若SIPA1L3具有Ran-GAP活性，它可能直接参与核质转运机器的门控，甚至可能调控染色质修饰酶（如HDAC、SUV39H1）的核定位。此外，PPI中DYRK1B（双特异性酪氨酸磷酸化调控激酶1B, BioGRID）的存在值得关注——DYRK1B磷酸化HP1γ和H3，影响异染色质组装。这一间接的染色质连接是SIPA1L3-TE调控假说的唯一分子线索。

**大尺寸蛋白的结构限制**：AlphaFold pLDDT=55.5的极低置信度（蛋白大小1781 aa超出AF2可靠预测范围）和PDB=0的结构缺失严重阻碍了机制研究。1781 aa的蛋白大小为实验提供了空间——可设计截短体进行结构域功能映射。PDZ域和Rap-GAP域可作为独立模块进行体外生化分析。考虑到PPI degree=110（STRING/BioGRID）的中等互作复杂度和PubMed=17的低文献量，该蛋白属于信号蛋白的"核内月光功能"探索型候选。

**风险收益评估**：主要风险在于核定位可能为HPA抗体交叉反应的假阳性，且已知功能（上皮极性）与核质/TE调控之间存在巨大概念跳跃。归一化得分68.9/100中新奇性维度45/50、PPI 21/30是两大亮点，但三维结构得分12/30是显著短板。若推进，建议首先通过免疫荧光结合亚细胞分级确认核定位的真实性，随后通过BioID临近标记鉴定核内互作组。


### 补充分析 (UniProt API)

**蛋白全称**: Signal-induced proliferation-associated 1-like protein 3

**功能**: Plays a critical role in epithelial cell morphogenesis, polarity, adhesion and cytoskeletal organization in the lens (PubMed:26231217)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001478 |
| InterPro | IPR036034 |
| InterPro | IPR035974 |
| InterPro | IPR000331 |
| InterPro | IPR050989 |
| InterPro | IPR021818 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 1 |
| DYRK1B | BioGRID | 1 |
| LATS2 | BioGRID | 1 |
| YWHAB | BioGRID | 1 |
| WDR83 | BioGRID | 1 |
| SRPK2 | BioGRID | 1 |
| CEP152 | BioGRID | 1 |
| ODF2 | BioGRID | 1 |