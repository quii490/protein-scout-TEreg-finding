---
type: protein-evaluation
gene: "PACSIN1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PACSIN1 (Protein kinase C and casein kinase substrate in neurons protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PACSIN1 |
| 蛋白全称 | Protein kinase C and casein kinase substrate in neurons protein 1 |
| UniProt ID | Q9BY11 |
| 蛋白大小 | 444 aa / 48.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 444 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR027267; InterPro:IPR031160; InterPro:IPR001060; InterPro:IPR035743; InterPro:IPR037454; InterPro:IPR036028 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Plays a role in the reorganization of the microtubule cytoskeleton via its interaction with MAPT; this decreases microtubule stability and inhibits MAPT-induced microtubule polymerization. Plays a role in cellular transport processes by recruiting DNM1, DNM2 and DNM3 to membranes. Plays a role in the reorganization of the actin cytoskeleton and in neuron morphogenesis via its interaction with COBL

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR031160 |
| InterPro | IPR001060 |
| InterPro | IPR035743 |
| InterPro | IPR037454 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| Pfam | PF00611 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**F-BAR/SH3膜重塑蛋白的肌动蛋白-微管-核骨架桥接**：PACSIN1（Protein kinase C and casein kinase substrate in neurons protein 1, 444 aa, UniProt Q9BY11）属于PACSIN/Syndapin家族，拥有N端F-BAR（FCH-BAR）结构域（IPR027267, IPR001060, IPR035743; Pfam: FCH）和C端SH3结构域（IPR036028, IPR001452）。F-BAR域以新月形二聚体感知并稳定负弯曲度的膜（内吞小窝的凹曲面），而SH3域招募动力蛋白（DNM1/2/3）和WASP/WAVE复合物的PRD富集区以驱动肌动蛋白聚合——构成经典的内吞-肌动蛋白耦合机器。该蛋白还通过与MAPT/Tau蛋白的互作降低微管稳定性并抑制微管聚合。

**PACSIN1-Huntingtin互作与HD中的TE去抑制关联**：PPI中HTT/Huntingtin（STRING 917）的高互作评分提供了唯一TE相关线索。突变的Huntingtin蛋白（mHTT）在亨廷顿病（HD）中通过螯合转录因子（如CBP/p300, Sp1, TBP）导致全局转录失调，其中ERV和LINE-1的去抑制已被报道为HD纹状体神经元的早期分子事件。PACSIN1与HTT的互作可能在突触小泡内吞循环中发生，但HTT的核内片段（N-terminal fragments）可通过核孔进入核内，可能携带PACSIN1或影响其亚细胞分布。

**低优先级TE候选**：PACSIN1的神经突触特异性表达（脑组织富集）和膜重塑正典功能使其TE调控的可信度极低。F-BAR/SH3蛋白无任何染色质/DNA结合能力，核仁分类（67.8/100, 核定位特异性4/10）可能为低丰度污染信号。建议作为不推荐的最低优先级候选。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PACSIN2 | STRING | 938 |
| HTT | STRING | 917 |
| SOBP | STRING | 809 |
| TRIP10 | STRING | 746 |
| FCHO1 | STRING | 704 |
| PACSIN1 | BioGRID | 1 |
| KAT7 | BioGRID | 1 |
| CYFIP2 | BioGRID | 1 |