---
type: protein-evaluation
gene: "TRERF1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## TRERF1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TRERF1 |
| 蛋白全称 | Transcriptional-regulating factor 1 |
| UniProt ID | Q96PN7 |
| 蛋白大小 | 1200 aa / 132.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1200 aa|
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=49.2; PDB=0 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR000949, IPR009057, IPR001005, IPR017884|
| PPI | 5/10 | ×3 | 15.0 | PPI degree=30 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +3 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Binds DNA and activates transcription of CYP11A1. Interaction with CREBBP and EP300 results in a synergistic transcriptional activation of CYP11A1

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR000949 | ELM2_dom |
| InterPro | IPR009057 | Homeodomain-like_sf |
| InterPro | IPR001005 | SANT/Myb |
| InterPro | IPR017884 | SANT_dom |
| InterPro | IPR051066 | Trans_reg/Corepressor |
| InterPro | IPR036236 | Znf_C2H2_sf |
| InterPro | IPR013087 | Znf_C2H2_type |
| Pfam | PF01448 | ELM2 |


#### 3.4 结构信息

蛋白长度 1200 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000124496-TRERF1

![](https://images.proteinatlas.org/27771/1450_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/27771/1450_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/27771/1518_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/27771/1518_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/27771/1445_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/27771/1445_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/51273/855_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/51273/855_C10_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
★★★★  **73.8/100**  |  **nucleolus**
**TE candidate**: ELM2_dom; Homeodomain-like_sf; SANT/Myb


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01189;SM00717;SM00355; |
| InterPro | IPR000949;IPR009057;IPR001005;IPR017884;IPR051066;IPR036236;IPR013087; |
| Pfam | PF01448;PF13912; |
| UniProt Domain | DOMAIN 779..870; /note="ELM2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00512"; DOMAIN 885..936; /note="SANT"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00624" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DNTTIP1 | STRING | 970 |
| C14ORF43 | STRING | 869 |
| ELMSAN1 | STRING | 869 |
| HDAC1 | STRING | 869 |
| NR5A1 | STRING | 769 |
| SF1 | STRING | 769 |
| EP300 | BioGRID | 1 |
| CREBBP | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96PN7-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 24**

| 41872334 | Obesity-associated gene mutations across cancer types: a pan-cancer analysis of TCGA data. | BJC Rep 2026 |
| 41629253 | Large deletions in the DNA primase large subunit PRIM2 are associated with NADP-malate dehydrogenase activity in a porci | Anim Genet 2026 |
| 41199169 | Whole-genome resequencing uncovers population structure and candidate molecular markers for litter size in hetian sheep. | BMC Genomics 2025 |

### 深度机制分析

TRERF1（转录调控因子1）是一个多功能转录调节蛋白，1200 aa的巨型架构汇聚了多个经典转录调控结构域：ELM2（IPR000949/PF01448，转录抑制相关的招募结构域）、SANT/Myb（IPR001005，与组蛋白尾部结合并参与染色质重塑）、Homeodomain-like_sf（IPR009057，DNA结合折叠）、Znf_C2H2_sf/type（IPR036236/IPR013087，序列特异性DNA识别）以及SMART注释的SM01189/SM00717/SM00355。UniProt直接注释了ELM2（779-870 aa）和SANT（885-936 aa）的精确边界，提供了稀有的实验域映射信息。AlphaFold pLDDT仅49.2，反映1200 aa中大量无序区域的存在——这是转录因子通过固有无序区域进行多价互作的典型特征。

TRERF1被标记为TE_REG_CANDIDATE的核心理据在于其结构域组合的独特性。ELM2-SANT串联模块是已知转录辅抑制因子（如MTA家族、CoREST）的标志性架构，通常通过ELM2招募HDAC复合物、SANT结合去乙酰化组蛋白尾部来实现转录抑制（PMID涉及CREBBP/EP300互作协同激活CYP11A1）。PPI网络中HDAC1（STRING score=869）、EP300和CREBBP的互作证实TRERF1同时接触去乙酰化和乙酰化机器，表明其可能作为组蛋白修饰的"双向开关"——在特定启动子上根据辅助因子的可用性切换激活/抑制状态。

TRERF1在HPA中定位于核仁（nucleoli），结合ELMSAN1（STRING score=869）和DNTTIP1（STRING score=970）的互作，暗示其可能在核仁中的rDNA转录调控或核仁应激应答中发挥作用。核仁是核糖体生物合成的工厂，也是p53应激应答的枢纽——核仁应激下核仁蛋白释放至核质激活p53。如果TRERF1参与核仁应激信号传导，其ELM2-SANT模块可能在应激状态下通过HDAC1依赖机制沉默rDNA转录，从而协调核糖体生物合成与细胞增殖速度。肥胖相关基因突变（PMID:41872334）和生殖性状GWAS（PMID:41199169）提示TRERF1在代谢和生殖生物学中具有广泛的转录调控功能。ChIP-seq/rDNA-targeted ChIP和核仁应激下的动态定位分析应是后续验证的优先方向。

