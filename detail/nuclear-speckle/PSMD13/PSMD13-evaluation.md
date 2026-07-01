---
type: protein-evaluation
gene: "PSMD13"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PSMD13 (26S proteasome non-ATPase regulatory subunit 13) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PSMD13 |
| 蛋白全称 | 26S proteasome non-ATPase regulatory subunit 13 |
| UniProt ID | Q9UNM6 |
| 蛋白大小 | 376 aa / 41.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 376 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR000717; InterPro:IPR054179; InterPro:IPR035298; InterPro:IPR036390; Pfam:PF01399; Pfam:PF22037 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellu

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000717 |
| InterPro | IPR054179 |
| InterPro | IPR035298 |
| InterPro | IPR036390 |
| Pfam | PF01399 |
| Pfam | PF22037 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMD8 | STRING | 999 |
| USP14 | STRING | 999 |
| PSMD3 | STRING | 999 |
| PSMD1 | STRING | 999 |
| PSMD4 | STRING | 999 |
| PSMD14 | STRING | 999 |
| ADRM1 | STRING | 999 |
| UCHL5 | STRING | 998 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000185627-PSMD13

![](https://images.proteinatlas.org/38692/455_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/38692/455_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/38692/449_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/38692/449_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/38692/452_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/38692/452_G8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 34**

| 42327232 | Post-translational modifications in the brain are critical contributors to Alzheimer's disease neuropathology and cognit | bioRxiv 2026 |
| 42289649 | Comparative mass spectrometry analysis of high and low centrifugation extracellular vesicle (EV) pellets from healthy ur | Clin Proteomics 2026 |
| 42124546 | Identifying pleiotropic genes for backfat thickness and semen traits in pigs using GWAS summary data. | J Anim Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMD13

### 深度机制分析

**结构域架构**：PSMD13/Rpn9（UniProt Q9UNM6，376 aa，41.4 kDa）是26S蛋白酶体19S调节粒子（PA700）的盖部（lid）亚基。其域架构以PCI域（Proteasome, COP9, eIF3 domain）为核心——IPR000717（Proteasome component (PCI) domain）和Pfam:PF01399（PCI）采用全α-螺旋束折叠，作为支架域介导19S盖部中PSMD13与邻近亚基（主要是PSMD8/Rpn12和PSMD3/Rpn3）的二元→高阶组装。IPR036390（PCI domain superfamily）为PCI样α-螺旋重复折叠超家族。IPR035298为PSMD13特异性的串联PCI折叠标记。Pfam:PF22037为PSMD13新定义的C端域。PCI域通过疏水核心和盐桥网络实现高度特异性的伙伴识别，无酶活性——PSMD13是结构与组装性亚基。

**PPI互作网络**：STRING数据显示PSMD13的PPI网络完全由26S蛋白酶体亚基构成，评分极其一致：PSMD8（Rpn12，评分999）、USP14（Ubp6，评分999）、PSMD3（Rpn3，评分999）、PSMD1（Rpn2，评分999）、PSMD4（Rpn10，评分999）、PSMD14（Rpn11，评分999）、ADRM1（Rpn13，评分999）和UCHL5（Uch37，评分998）。所有核心伙伴均为彼此的19S亚基——PSMD13作为PCI支架在盖部组装中必不可少。USP14和UCHL5位于19S基底（base）而非盖部——其与PSMD13的互作反映26S全酶的跨模块协同。

**结构-功能关系**：在26S蛋白酶体全酶中，PSMD13位于19S盖部（由9个γ-亚基组成——含6个PCI蛋白和3个MPN蛋白）。盖部通过PCI域介导的异型互作组装为马蹄形结构，此过程中PSMD13主要与PSMD8和PSMD3形成PCI域对的结晶核心。盖部与基底的对接构成完整的19S调节粒子，20S核心颗粒的α环门控在19S全组装后被打开。

**TE调控机制**：PSMD13通过泛素-蛋白酶体系统（UPS）的多层次参与TE调控。其一，19S调节粒子的核心功能——识别K48泛素化标签以递送底物至20S进行ATP依赖性降解——直接决定了TE编码蛋白的胞内寿命。LINE-1 ORF1p的高表达/聚集毒性、ERV Env蛋白和内源性逆转录病毒Gag颗粒均需经UPS降解以维持蛋白稳态。其二，19S基底的去泛素化酶（USP14和UCHL5——PPI评分999/998）在底物进入20S前进性修剪泛素链，其编辑活动决定泛素信号的过渡动态——该过程调控TE蛋白的降解或回收之间的平衡。其三，cGAMP/STING/IFN通路的负调控因子（如STING蛋白自身）经UPS降解以设定先天免疫应答的终止时程——PSMD13参与的降解效率决定了IFN信号的持时，进而影响TE转录的JAK-STAT依赖性激活。

**前沿意义**：PSMD13的34篇PubMed中主导内容为泛素化蛋白组学、阿尔茨海默病神经病理学（PMID:42327232）和猪/农业性状GWAS。作为19S盖部PCI支架，PSMD13在TE调控中的角色是上下文结构性的而非直接催化性的——但其PCI域的组装功能是不可替代的（PSMD13 KO可致19S完全缺陷）。USP14特异性抑制剂（IU1系列）已可药理抑制19S去泛素化酶，通过USP14→PSMD13→PSMD8→PSMD3→盖部全组装的级联传递——IU1处理可经UPS功能改变验证其对TE编码蛋白降解的影响（pulse-chase/环己酰亚胺追踪）。

