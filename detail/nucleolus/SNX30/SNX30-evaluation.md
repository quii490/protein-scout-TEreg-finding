---
type: protein-evaluation
gene: "SNX30"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SNX30 (Sorting nexin-30) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNX30 |
| 蛋白全称 | Sorting nexin-30 |
| UniProt ID | Q5VWJ9 |
| 蛋白大小 | 437 aa / 48.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 437 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR027267; InterPro:IPR004148; InterPro:IPR001683; InterPro:IPR036871; InterPro:IPR028649; Pfam:PF03114 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the regulation of endocytosis and in several stages of intracellular trafficking (PubMed:32513819). Together with SNX4, involved in autophagosome assembly (PubMed:32513819)

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR004148 |
| InterPro | IPR001683 |
| InterPro | IPR036871 |
| InterPro | IPR028649 |
| Pfam | PF03114 |
| Pfam | PF00787 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**PX-BAR双结构域Sorting Nexin的非核蛋白定位**：SNX30（Sorting nexin-30, 437 aa, UniProt Q5VWJ9）携带三个标志性结构域：N端SH3结构域（aa 1-61, IPR001452）、PX结构域（aa 230-340, IPR001683, Pfam PF00787）和C端BAR结构域（aa 371-574, SMART SM00312）。SH3-PX-BAR结构域组合是SNX9/18/33亚家族的特征，暗示SNX30参与网格蛋白介导的内吞作用中的膜重塑（membrane tubulation）和货物分选。PX域结合PI3P富集的内体膜，而BAR域通过其新月形二聚体感知并稳定膜弯曲，SH3域招募动力蛋白（Dynamin）和肌动蛋白调控因子。该蛋白与SNX4协同参与自噬体组装（PMID:32513819）——一种膜重塑过程，与核内事件无关。

**核仁定位的不确定性**：该蛋白的定位注释为"no known nuclear annotation"（核定位特异性4/10），归入核仁分类的依据可能是质谱检测的非特异性背景信号。Sorting nexin家族的所有成员均定位于胞质内膜（内体、TGN或质膜），无任何成员具有实验验证的核定位——SNX13（含RGS域）的部分核定位为家族唯一例外。因此SNX30的核仁分类可能是一个误分类。

**低优先级TE候选**：PPI数据中包含HNRNPL（BioGRID score=0）和KHDRBS1（Sam68, BioGRID score=0）两个RNA结合蛋白——HNRNPL参与可变剪接调控，Sam68参与RNA代谢和信号转导。若SNX30确实微量定位于核仁，可能通过SH3域介导的蛋白-蛋白互作与核仁RNA结合蛋白产生微弱关联。但整体上该蛋白的膜运输功能与TE调控不存在衔接点，建议在TE筛选中赋予最低优先级。


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00312;SM00326; |
| InterPro | IPR027267;IPR001683;IPR036871;IPR036028;IPR001452;IPR037427;IPR014536;IPR019497; |
| Pfam | PF10456;PF00787;PF14604; |
| UniProt Domain | DOMAIN 1..61; /note="SH3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00192"; DOMAIN 230..340; /note="PX"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00147"; DOMAIN 371..574; /note="BAR" |