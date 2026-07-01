---
type: protein-evaluation
gene: "FCHSD2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## FCHSD2 (F-BAR and double SH3 domains protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FCHSD2 |
| 蛋白全称 | F-BAR and double SH3 domains protein 2 |
| UniProt ID | O94868 |
| 蛋白大小 | 740 aa / 81.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 740 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR027267; InterPro:IPR031160; InterPro:IPR001060; InterPro:IPR034934; InterPro:IPR035556; InterPro:IPR035460 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Adapter protein that plays a role in endocytosis via clathrin-coated pits. Contributes to the internalization of cell surface receptors, such as integrin ITGB1 and transferrin receptor (PubMed:29887380). Promotes endocytosis of EGFR in cancer cells, and thereby contributes to the down-regulation of EGFR signaling (PubMed:30249660). Recruited to clathrin-coated pits during a mid-to-late stage of as

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR031160 |
| InterPro | IPR001060 |
| InterPro | IPR034934 |
| InterPro | IPR035556 |
| InterPro | IPR035460 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CCDC158 | BioGRID | 0 |
| CCDC85B | BioGRID | 0 |
| MAGI1 | BioGRID | 0 |
| CASK | BioGRID | 0 |
| VCP | BioGRID | 0 |
| VCPIP1 | BioGRID | 0 |
| HSPA5 | BioGRID | 0 |
| SRP72 | BioGRID | 0 |


### PubMed 文献

**PubMed count: 37**

| 42192936 | A Ten-Gene Transcriptomic Biomarker Panel for Glioma Classification and Prognosis Identified via Integrative Hypergraph  | Cancers (Basel) 2026 |
| 41021661 | Identifying genetic determinants of outer retinal function in mice using a large-scale gene-targeted screen. | PLoS Genet 2025 |
| 39382837 | Endosomal actin branching, fission, and receptor recycling require FCHSD2 recruitment by MICAL-L1. | Mol Biol Cell 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FCHSD2

### 深度机制分析

**结构域架构**：FCHSD2（UniProt O94868，740 aa，81.4 kDa）属于F-BAR蛋白家族（FCH/SHD双SH3域蛋白）。其域架构包含三个功能模块沿N→C排列：N端的F-BAR域（IPR027267 - F-BAR domain, Pfam位置；IPR031160 - FCHSD2-type F-BAR domain；IPR001060 - FCH domain）采用新月形同源二聚体结构——每个单体含三个延伸α-螺旋的卷曲螺旋捆——通过正电荷凹面的基本残基识别含PI(4,5)P₂和PI(3,4,5)P₃的弯曲膜；串联的两个C端SH3域——第一SH3（IPR034934, SH3_FCHSD1_2_1；IPR035556, SH3_FCHSD2_1）和第二SH3（IPR035460, SH3_FCHSD1_2_2）——均采用五股β-桶折叠，识别PXXP配体基序；短中心连接子连接F-BAR和SH3域。IPR036028（SH3-like domain superfamily）和IPR001452（Src homology-3 domain）提供SH3超家族标记。

**PPI互作网络**：BioGRID互作数据展示了一个围绕细胞骨架和内质网应激的PPI网络：CCDC158（coiled-coil蛋白，评分0）和CCDC85B（coiled-coil蛋白，评分0）为未表征的卷曲螺旋蛋白——推测通过coiled-coil-二聚体与FCHSD2的F-BAR同源二聚体界面的coiled-coil协同；MAGI1（膜相关鸟苷酸激酶1，评分0）和CASK（钙/钙调蛋白依赖性丝氨酸激酶，评分0）构成膜结合支架信号复合体；VCP（valosin-containing protein/p97，评分0）和VCPIP1（VCP/p97互作蛋白，评分0）为AAA+ ATPase——在ERAD和有丝分裂高尔基/ER/核膜重塑中协同去膜蛋白复合体；HSPA5（BiP/Grp78，评分0）为ER分子伴侣；SRP72（信号识别颗粒72，评分0）参与共翻译靶向。

**结构-功能关系**：FCHSD2作为内吞衔接蛋白，通过F-BAR域感知/诱导细胞膜弯曲并富集于网格蛋白包被的窝（clathrin-coated pits），通过SH3域招募下游效应子介导内吞机械的组装。以MICAL-L1依赖的方式参与内体肌动蛋白分枝、裂变和受体回收（PMID:39382837）。在癌症细胞中通过促进EGFR内吞下调EGFR信号（PMID:30249660）。

**TE调控机制**：FCHSD2与TE调控的连接最令人兴奋地通过MICAL-L1→肌动蛋白重构→DDR（DNA损伤应答）信号轴。MICAL-L1是F-actin去聚合酶和SRF/MRTF-A转录通路的调控因子——MRTF-A/G-actin→核转位→SRF复合体激活已知结合ERV/LTR启动子中的血清响应元件（SRE/CArG box）。因此FCHSD2通过内吞→肌动蛋白动力学→MRTF-A核转位→SRF→TE转录通路的调控。此外，VCP/p97是多个TE限制通路的核心ATP酶——VCP驱动的去膜可释放被膜包埋的TE DNA，并且VCP与泛素化组蛋白和DNA损伤位点的清理相关。SRP72（共翻译靶向因子）的PPI暗示FCHSD2可能在TE编码的膜蛋白（如Syncytin-ERV包膜蛋白）共翻译插入ER中发挥作用。

**前沿意义**：FCHSD2的37篇PubMed文献聚焦于内吞和癌症信号，但EGFR内吞下调活性恰好连接膜运输与细胞增殖信号——EGFR信号是ERV/LTR启动子活性的重要正调控因子。FCHSD2→EGFR内吞→MAPK信号减弱→LTR转录抑制构成一条多步骤但逻辑一致的负调控通路。F-BAR域代表了一种进化保守的膜重塑工具，逆转录病毒Gag蛋白出芽同样使用类似的PIP₂依赖性膜弯曲机制——FCHSD2是否通过竞争PIP₂或膜弯曲中间体干扰TE/病毒出芽是极具原创性的假说。

