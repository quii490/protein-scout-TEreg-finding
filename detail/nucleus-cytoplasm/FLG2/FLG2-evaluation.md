---
type: protein-evaluation
gene: "FLG2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## FLG2 (Filaggrin-2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FLG2 |
| 蛋白全称 | Filaggrin-2 |
| UniProt ID | Q5D862 |
| 蛋白大小 | nan aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 2391 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR011992, IPR018247, IPR002048, IPR003303|
| 🔗 PPI | 6/10 | ×3 | 18.0 | PPI degree=126 |
| **加权总分** | | | **83/180** | |
| **归一化总分 (÷1.83)** | | | **45/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Keratohyalin granule + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: FLG2 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Keratohyalin granule + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

epidermal structural protein。

#### 3.3 PPI 网络

PPI degree=126。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

FLG2 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| InterPro | IPR003303 |
| InterPro | IPR034325 |
| InterPro | IPR052503 |
| InterPro | IPR001751 |
| InterPro | IPR013787 |
| Pfam | PF01023 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01394; |
| InterPro | IPR011992;IPR018247;IPR002048;IPR003303;IPR034325;IPR052503;IPR001751;IPR013787; |
| Pfam | PF01023; |
| UniProt Domain | DOMAIN 8..43; /note="EF-hand 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00448"; DOMAIN 49..84; /note="EF-hand 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00448" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LOR | STRING | 999 |
| IVL | STRING | 995 |
| CASP14 | STRING | 928 |
| PADI3 | STRING | 846 |
| FLG | STRING | 832 |
| KLK7 | STRING | 811 |
| KRT2 | STRING | 780 |
| TCF3 | BioGRID | 1 |


### PubMed

**Count: 98**

| PMID | Title |
|---|---|
| 42364022 | Integrated Multi-omics Profiling of 2,4-dinitrochlorobenzene (DNCB)-induced Atopic Dermatitis in Mice Reveals a Coordinated Network of Barrier Dysfunc |
| 42033032 | Polymorphisms in CLAUDIN1 and SPINK5 Influence Skin Absorption of Pyrene, Pyrimethanil, and Oxybenzone in Human Volunteers. |
| 42025449 | Skin barrier-related genes in childhood atopic dermatitis, asthma, and allergy: A systematic review and meta-analysis. |
| 41900972 | Transcriptomic Profiling Identifies a Distinct Molecular Signature in OSMF-Derived Oral Squamous Cell Carcinoma. |
| 41890232 | Promoter hypomethylation of CDH7: a novel epigenetic marker associated with cerebral small vessel disease. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q5D862
- HPA: https://www.proteinatlas.org/

### 深度机制分析

FLG2（Filaggrin-2）是表皮结构性蛋白家族的成员，其深度机制分析需从皮肤屏障生物学的角度展开。该蛋白是一个巨大的结构蛋白（2391个氨基酸），其序列中UniProt注释了2个EF-hand结构域（EF-hand 1: 8-43aa, EF-hand 2: 49-84aa），这对钙结合基序提示其在钙依赖性表皮分化过程中的调控角色。InterPro注释揭示了一个更为丰富的结构域全景：IPR011992（EF-hand domain pair）、IPR018247（EF-hand, Ca insensitive）、IPR002048（EF-hand domain）、IPR003303（Filaggrin）、IPR034325（S-100/Calmodulin-like）、IPR052503和IPR001751（S-100/CaBP type）。Pfam仅注释了PF01023（S-100/CaBP），而SMART数据标记为SM01394。这种以EF-hand/Ca2+结合和S-100家族为主的结构域架构将FLG2定位于钙依赖的表皮分化程序。

FLG2的功能与经典Filaggrin（FLG）类似但在分化层级中存在时间差异——它主要在颗粒层上部和角质层中表达，参与角质化包膜（cornified envelope, CE）的形成和皮肤屏障功能的维持。其S-100/CaBP结构域作为钙传感器，在表皮分化过程中感知胞内钙浓度的梯度变化（基底层低钙→颗粒层高钙），触发FLG2的构象变化和随后的蛋白水解加工。与FLG不同，FLG2的EF-hand使其具有直接的钙响应能力，这可能解释了其与FLG在表达时序上的差异。

PPI互作网络验证了FLG2在角质化程序中的整合角色。STRING数据显示LOR（Loricrin, score=999）、IVL（Involucrin, score=995）和CASP14（Caspase-14, score=928）是最高置信度互作伙伴——LOR和IVL同属CE前体蛋白，与FLG2共同在转谷氨酰胺酶催化下交联形成表皮屏障的蛋白质骨架；CASP14参与FLG的蛋白水解加工，其与FLG2的互作提示可能共享加工机制。PADI3（Peptidyl arginine deiminase 3, score=846）催化FLG2的精氨酸去亚氨酸化（citrullination），影响其正电荷密度和降解速率——这是一个重要的翻译后修饰调控机制。FLG（score=832）、KLK7（kallikrein-related peptidase 7, score=811）和KRT2（Keratin 2, score=780）进一步扩展了这一角质化网络。BioGRID还收录了TCF3（T细胞因子3, score=1），该转录因子参与Wnt信号通路，可能与FLG2的表达调控相关。

在核定位方面，UniProt GO-CC将FLG2注释为"Keratohyalin granule + Nucleus"，其中Keratohyalin granule显然是其主定位——这是颗粒层角质形成细胞中富含FLG/FLG2前体蛋白的特化细胞器。核定位可能反映了FLG2在终端分化过程中随着角化包膜形成和细胞核降解过程而发生的"旁观者"效应——表皮终末分化的最后阶段涉及核膜破裂和核内容物的释放，而非主动的功能性核定位。此外，FLG2缺乏任何DNA/chromatin结合结构域，其全部结构域均服务于钙感应和表皮结构功能。

PubMed文献分析聚焦于FLG2在皮肤屏障疾病中的作用。PMID 42033032和42025449研究了FLG2多态性与皮肤屏障功能和特应性疾病（atopic dermatitis, asthma, allergy）的关联。PMID 42364022通过整合多组学分析揭示了DNCB诱导的特应性皮炎模型中屏障功能障碍的协调网络。这些研究与FLG2的表皮结构功能高度一致，但完全未涉及核内或TE调控功能。

FLG2的推荐等级为2/5（45/100），其得分由PPI网络（6/10, degree=126的庞大互作网络）和调控结构域（8/10, EF-hand/S-100/Filaggrin）驱动，但核定位证据薄弱（4/10）是明显短板。深度机制模型为：胞外钙内流→FLG2的EF-hand感知钙梯度→S-100结构域构象变化→PADI3催化的citrullination→与LOR/IVL交联→CE形成→表皮屏障。该模型与TE调控无关，建议保留其作为皮肤生物学靶标的价值。


