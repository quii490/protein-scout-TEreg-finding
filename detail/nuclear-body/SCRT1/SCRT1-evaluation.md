---
type: protein-evaluation
gene: "SCRT1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SCRT1 (Transcriptional repressor scratch 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SCRT1 |
| 蛋白全称 | Transcriptional repressor scratch 1 |
| UniProt ID | Q9BWW7 |
| 蛋白大小 | 348 aa / 38.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 348 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR050527; InterPro:IPR036236; InterPro:IPR013087; Pfam:PF00096; Pfam:PF13912 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Transcriptional repressor that binds E-box motif CAGGTG. Can modulate the action of basic helix-loop-helix (bHLH) transcription factors, critical for neuronal differentiation

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |
| Pfam | PF13912 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000261678-SCRT1

![](https://images.proteinatlas.org/45265/1652_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45265/1652_B5_3_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00355; |
| InterPro | IPR050527;IPR036236;IPR013087; |
| Pfam | PF00096;PF13912; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IMPDH1 | BioGRID | 1 |
| ZNF579 | BioGRID | 1 |
| WWP1 | BioGRID | 1 |
| PRMT9 | BioGRID | 1 |
| SORL1 | BioGRID | 1 |
| KLHDC10 | BioGRID | 1 |
| VRK3 | BioGRID | 1 |
| NES | BioGRID | 0 |


### PubMed 文献

**PubMed count: 17**

| 41724853 | Scrt1-iCreER: An Inducible Mouse Model for Genetic Access to Type I Spiral Ganglion and Cochlear Nucleus Neurons. | Mol Neurobiol 2026 |
| 41279603 | Quantifying the impact of genetic mutations on enhancer dynamics. | bioRxiv 2025 |
| 40409528 | Transcriptomic characterization of the synergy between human induced pluripotent stem cells-derived liver- and pancreas- | Mol Cell Endocrinol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SCRT1

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SCRT1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.66 |
| pLDDT > 0.9 占比 | 4.0% |
| pLDDT < 0.5 占比 | 29.0% |
| 建模残基数 | 348 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

**结构域架构**：SCRT1（UniProt Q9BWW7，348 aa，38.3 kDa）是Snail超家族的转录抑制因子。其域架构以C2H2型锌指DNA结合域为核心（InterPro:IPR036236 - zinc finger, C2H2-like，SMART:SM00355；Pfam:PF00096 and PF13912），串联多个锌指单元。IPR050527为Snail/Scratch家族转录因子的特异性家族标记，IPR013087指示锌指C2H2型保守折叠。N端预计包含SNAG（Snail/Gfi）抑制域，该短肽基序（约9 aa）通过与组蛋白去甲基化酶LSD1（KDM1A）和组蛋白去乙酰化酶HDAC1/2的协同作用实现转录抑制。

**PPI互作网络**：BioGRID互作数据显示IMPDH1（磷酸脱氢酶，评分1）、ZNF579（锌指蛋白，评分1）、WWP1（HECT E3泛素连接酶，评分1）、PRMT9（精氨酸甲基转移酶，评分1）、SORL1（分选受体，评分1）、KLHDC10（E3连接酶底物受体，评分1）、VRK3（非活性激酶，评分1）和NES（核输出信号相关蛋白，评分0）。PRMT9和WWP1的互作提示SCRT1活性可能受翻译后修饰调控——精氨酸甲基化和泛素化是已知的转录因子活性调控开关。

**结构-功能关系**：SCRT1的ESMFold结构预测（平均pLDDT=0.66，pLDDT>0.9仅占4.0%，pLDDT<0.5占29.0%）显示整体折叠置信度偏低，这与其锌指域外存在大量柔性/固有无序区段一致。SNAG抑制域通常以短β-发夹/延伸构象嵌入LSD1活性位点，竞争性地被HDAC1/2核酸受体复合体识别。锌指识别E-box基序（CAGGTG），通过位阻机制拮抗bHLH转录因子（如Neurogenin、Mash1）与E-box的结合，从而抑制神经分化相关基因转录。

**TE调控机制**：Snail/Scratch家族主要在神经分化和上皮-间质转化（EMT）中发挥转录抑制功能（PMID:41724853 - Scrt1-iCreER小鼠模型用于I型螺旋神经节神经元示踪）。在TE调控背景下，SCRT1可能通过SNAG域→LSD1→H3K4me2去甲基化的通路参与内源性逆转录病毒调控——LSD1是已知的ERV/LTR沉默因子，通过去除H3K4me2的活性标记使TE启动子进入抑制性染色质状态。ZNF579的C2H2锌指互作提示SCRT1可能作为KZFP-KAP1-TRIM28通路的协同因子。

**前沿意义**：SCRT1尽管有17篇PubMed文献，但在TE调控领域的研究为完全空白。PRMT9精氨酸甲基转移酶互作赋予了不对称二甲基精氨酸修饰调控SCRT1活性的可能性——精氨酸甲基化在染色质调控和TE沉默中日益受到关注。利用小鼠Scrt1条件性敲除模型结合TE-RNA-seq分析，将验证其转座子调控的生理相关性。

