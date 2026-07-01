---
type: protein-evaluation
gene: "B3KNI3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KNI3 (cDNA FLJ14651 fis, clone NT2RP2002193, highly similar to Protein inhibitor of activated STAT protein 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KNI3 |
| 蛋白全称 | cDNA FLJ14651 fis, clone NT2RP2002193, highly similar to Protein inhibitor of activated STAT protein 3 |
| UniProt ID | B3KNI3 |
| 蛋白大小 | 628 aa / 69.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 628 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR023321; InterPro:IPR038654; InterPro:IPR003034; InterPro:IPR036361; InterPro:IPR004181; InterPro:IPR013083 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR023321 |
| InterPro | IPR038654 |
| InterPro | IPR003034 |
| InterPro | IPR036361 |
| InterPro | IPR004181 |
| InterPro | IPR013083 |
| Pfam | PF14324 |
| Pfam | PF02037 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KNI3编码PIAS3（Protein Inhibitor of Activated STAT 3）的同源蛋白，其结构域架构由四个功能模块串联而成：N端SAP结构域（IPR003034、Pfam PF02037）采用螺旋-伸展-螺旋折叠，识别AT-rich DNA序列和核基质附着区（MAR），赋予该蛋白直接的染色质结合能力；PINIT结构域（IPR038654、Pfam PF14324）介导核内滞留信号和转录抑制活性；C端SP-RING/MIZ型锌指结构域（IPR004181、IPR013083）是SUMO E3连接酶的催化核心，负责将SUMO蛋白转移至底物赖氨酸残基。IPR023321（SAP超家族折叠）和IPR036361（SP-RING锌指超家族）覆盖完整结构域折叠分类。

628 aa（69.1 kDa）的大分子量容纳了DNA结合与SUMO连接酶双重活性所需的全部结构域，与PIAS家族成员（PIAS1-4）的大小范围一致（约510-650 aa）。AlphaFold预测结构可用，SAP DNA结合域和SP-RING催化域的折叠预测可信度通常较高，但无实验PDB验证（归一化结构得分6/10）。作为TrEMBL未审阅条目（PubMed=0），PPI数据极度有限，但基于Swiss-Prot中PIAS3的已知互作组，其核心底物网络包括STAT3（JAK/STAT信号效应子）、NF-kB/p65、SMAD2/3/4（TGF-beta信号转导）、AR（雄激素受体）和MITF，此外与PIAS1/2/4形成同源/异源SUMO连接酶复合物。

TE调控相关性的机制推论基于SUMO化修饰在染色质沉默中的核心角色，属于候选列表中最直接的调控路径之一：（1）PIAS3通过SUMO化修饰KAP1/TRIM28——KRAB-ZFP辅抑制因子和TE沉默的核心执行枢纽——可增强KAP1对SETDB1/ESET（H3K9甲基转移酶）和HP1的招募效率，从而增加H3K9me3在TE启动子区域的沉积水平（PMID:17000779、19264966）；（2）PIAS3通过SUMO化修饰CTCF可影响绝缘子活性和染色质环的建立，进而改变TE-TAD边界的拓扑组织；（3）STAT3本身在IL-6/JAK信号激活条件下可直接结合并调控LINE-1启动子（PMID:28552788），PIAS3对STAT3的SUMO化修饰可同时抑制其转录活性和改变其DNA结合选择性。此外，PIAS3对SMAD2/3的SUMO化可影响TGF-beta诱导的上皮-间充质转化（EMT），而EMT过程中伴随大规模的TE表达重组。

然而，该TrEMBL变体缺乏GO-CC核定位注释（核定位特异性仅4/10），但鉴于SAP DNA结合域和PINIT核滞留域共同赋予的内在染色质锚定能力，PIAS3的实际核定位概率极高。归一化总分67.8/100，但因SUMO化-KAP1-TE沉默轴的高度特异性，其在候选排序中应获得机制加成的修正权重。建议优先进行a）核定位IF验证，b）PIAS3-KAP1 SUMO化-泛素化交叉调控的生化验证，c）敲除PIAS3后TE家族的RNA-seq分析。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KNI3

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KNI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KNI3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KNI3
