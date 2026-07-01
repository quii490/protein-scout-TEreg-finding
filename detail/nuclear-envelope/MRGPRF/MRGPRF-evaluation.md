---
type: protein-evaluation
gene: "MRGPRF"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## MRGPRF (Mas-related G protein-coupled receptor member F) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MRGPRF |
| 蛋白全称 | Mas-related G protein-coupled receptor member F |
| UniProt ID | Q96AM1 |
| 蛋白大小 | 343 aa / 37.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 343 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR000276; InterPro:IPR017452; InterPro:IPR026228; InterPro:IPR026234; Pfam:PF00001 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Orphan receptor. May bind to a neuropeptide and may regulate nociceptor function and/or development, including the sensation or modulation of pain (By similarity)

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR026228 |
| InterPro | IPR026234 |
| Pfam | PF00001 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRIM67 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000172935-MRGPRF

![](https://images.proteinatlas.org/28811/2275_A12_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/28811/2275_A12_138_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 23**

| 42269381 | International Union of Basic and Clinical Pharmacology. CXXII. Applying an objective evaluation to the status of class A | Pharmacol Rev 2026 |
| 40788071 | USP45 Represses Melanoma Development by Deubiquitinating and Stabilizing Tumor Suppressor MRGPRF. | Adv Sci (Weinh) 2025 |
| 40289281 | Gut microbes-spinal connection is required for itch sensation. | Gut Microbes 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MRGPRF

### 深度机制分析

**结构域架构**：MRGPRF（UniProt Q96AM1，343 aa，37.7 kDa）属于Mas相关G蛋白偶联受体（MRGPR）家族——A类GPCR超家族成员。其域架构遵循经典的7次跨膜螺旋（TM1-TM7）拓扑：胞外N端→TM1→胞内环1→TM2→胞外环1→TM3→胞内环2→TM4→胞外环2→TM5→胞内环3→TM6→胞外环3→TM7→胞内C端。IPR000276（G protein-coupled receptor, rhodopsin-like）和Pfam:PF00001（7 transmembrane receptor）定义该7TM折叠。IPR017452（GPCR, rhodopsin-like, 7TM）为超家族注释。IPR026228（Mas-related G protein-coupled receptor F）和IPR026234（Mas-related G protein-coupled receptor, MRF/F/G type）为家族/亚型特异性标记。作为孤儿受体——即内源配体尚未鉴定——MRGPRF的功能注释主要基于序列相似性和体外异源表达系统。

**PPI互作网络**：MRGPRF的PPI数据极度贫乏——BioGRID仅记录TRIM67（三重基序蛋白67，评分0）一个潜在互作伙伴。TRIM67为神经元特异性E3泛素连接酶，参与发育轴突导向。该单一互作数据的贫困反映了孤儿GPCR的功能研究困难——缺乏明确的内源配体，传统的膜蛋白互作组学（膜蛋白溶解和稳定困难）也难以拓展PPI图谱。只有一个互作记录意味着现有PPI信息不足以支撑任何稳健的网络分析。

**结构-功能关系**：MRGPRF是孤儿受体，May bind a neuropeptide（UniProt By similarity注释），推测功能为感受或调控伤害性信号传导和/或发育过程，包括痛觉的感知或调制。作为GPCR，其信号机制通过G蛋白偶联（Gαi/o或Gαq/11亚型未确定）实现胞外信号→胞内second messenger的转导。USP45（去泛素化酶）去泛素化并稳定MRGPRF（PMID:40788071），将该受体的蛋白质稳定性与泛素化体调控联系起来。

**TE调控机制**：在核蛋白评估背景下，MRGPRF的神经元伤害感受受体身份与TE调控的关联极为间接。但有两个细微连接值得提出。其一，GPCR信号经Gαq→PLC→PIP₂→IP₃/DAG通路激活PKC和钙信号，已知可增强CREB介导的转录——而CREB结合位点（CRE/TRE元件）在ERV-LTR启动子中富集。其二，TRIM67（唯一的互作伙伴）属于TRIM蛋白超家族——许多TRIM家族成员（TRIM28/KAP1最为突出）是经典的TE沉默因子。TRIM67虽然主要在神经元轴突中发挥作用，但若其与MRGPRF的互作在内体-溶酶体或核周区室中发生，可能调控受体降解和下游信号时程。肠道菌群-脊髓连接在瘙痒感觉中的作用（PMID:40289281）提示MRGPRF信号可能受环境微生物代谢产物调控。

**前沿意义**：MRGPRF仅23篇PubMed文献和极度贫乏的PPI数据使其成为功能研究最不充分的GPCR之一。核蛋白定位证据缺失使其在TE调控中的直接价值极低，但GPCR→钙信号→CREB→ERV转录轴的间接通路提供了低置信但概念上可行的连接。TRIM67的单一互作因其所属的超家族背景而有被深入研究的价值。现有USP45去泛素化酶调控（PMID:40788071）和MOR激动剂领域进展为将来的功能化学遗传学验证提供了工具。

