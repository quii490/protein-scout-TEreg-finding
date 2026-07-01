---
type: protein-evaluation
gene: "OLFM1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## OLFM1 (Noelin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | OLFM1 |
| 蛋白全称 | Noelin |
| UniProt ID | Q99784 |
| 蛋白大小 | 485 aa / 53.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 485 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR022082; InterPro:IPR003112; InterPro:IPR050605; InterPro:IPR011044; Pfam:PF12308; Pfam:PF02191 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Contributes to the regulation of axonal growth in the embryonic and adult central nervous system by inhibiting interactions between RTN4R and LINGO1. Inhibits RTN4R-mediated axon growth cone collapse (By similarity). May play an important role in regulating the production of neural crest cells by the neural tube (By similarity). May be required for normal responses to olfactory stimuli (By similar

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR022082 |
| InterPro | IPR003112 |
| InterPro | IPR050605 |
| InterPro | IPR011044 |
| Pfam | PF12308 |
| Pfam | PF02191 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**Olfactomedin结构域蛋白的分泌/细胞外天然功能**：OLFM1（Noelin, 485 aa, UniProt Q99784）以C端Olfactomedin样结构域（aa 226-478, IPR003112, Pfam PF02191）为特征，该结构域属于富含半胱氨酸的分泌蛋白模块（约250 aa），在脊椎动物神经发育中高度保守。OLFM1作为RTN4R（Nogo-66受体）拮抗剂，抑制RTN4R与LINGO1的互作，从而调控成年中枢神经系统中的轴突生长（By similarity）。此外，该蛋白在神经管来源的神经嵴细胞生成和嗅觉刺激的正常应答中发挥作用。Olfactomedin家族的已知功能均局限于分泌蛋白的胞外信号功能。

**核仁定位的来源质疑**：HPA标注该蛋白"无已知核定位注释"（核定位特异性4/10），归入核仁分类的依据可能为质谱检测中的胞质/核仁交叉污染。Olfactomedin域的保守二硫键网络和糖基化修饰（N-糖基化）使其通过内质网-高尔基体分泌途径被分泌至胞外基质——这一生物合成通路与核仁完全不兼容。无任何Olfactomedin家族成员已被证实在核仁或核质中发挥功能。

**PPI中的微弱染色质连接**：PPI数据中EHMT1（STRING 817, G9a样蛋白）的高互作评分提供了唯一的染色质调控线索。EHMT1是H3K9me1/2甲基转移酶GLP，与G9a（EHMT2）形成异二聚体在常染色质区域催化H3K9me1/2，对ERV和LINE-1元件的沉默有直接贡献。若OLFM1与EHMT1的互作是真实的（attention: STRING推断），则可能通过秘密蛋白-trans受体间接影响EHMT1活性。EGFR（BioGRID score=1）和MYCN（BioGRID score=1）的互作暗示RTK信号和发育转录调控的潜在关联。然而，OLFM1的分泌蛋白天然功能与该互作网络之间存在不兼容性——EHMT1和MYCN为核蛋白，需OLFM1进入核内才能产生互作，这在Olfactomedin家族中从未被报道。

**不推荐的TE候选**：PubMed=54的非零文献量和OLFM1-胶质母细胞瘤肿瘤抑制功能（PMID:41831591）暗示存在非分泌性细胞自主功能，但与TE调控的距离过远。建议作为不推荐的最低优先级候选。


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00284; |
| InterPro | IPR022082;IPR003112;IPR050605;IPR011044; |
| Pfam | PF12308;PF02191; |
| UniProt Domain | DOMAIN 226..478; /note="Olfactomedin-like"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00446" |