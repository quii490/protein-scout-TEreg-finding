---
type: protein-evaluation
gene: "B3KM90"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KM90 (cDNA FLJ10529 fis, clone NT2RP2000965, highly similar to Targeting protein for Xklp2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KM90 |
| 蛋白全称 | cDNA FLJ10529 fis, clone NT2RP2000965, highly similar to Targeting protein for Xklp2 |
| UniProt ID | B3KM90 |
| 蛋白大小 | 605 aa / 66.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 605 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR027329; InterPro:IPR027330; InterPro:IPR009675; Pfam:PF06886; Pfam:PF12214 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027329 |
| InterPro | IPR027330 |
| InterPro | IPR009675 |
| Pfam | PF06886 |
| Pfam | PF12214 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KM90编码TPX2（靶向Xklp2蛋白）的同源蛋白，其结构域架构以双模块特色为标志：N端的importin-alpha/aurora A结合域（IPR027329、IPR027330）和C端的纺锤体靶向域（IPR009675）。Pfam注释PF06886与PF12214分别对应这两个功能模块，共同负责在有丝分裂纺锤体组装过程中的微管成核调控和Aurora A激酶的定位激活。

605 aa（66.5 kDa）的分子量在微管相关蛋白中属中等大小。AlphaFold预测结构可用但缺乏实验PDB验证（归一化结构得分6/10）。作为TrEMBL未审阅条目（PubMed=0），其PPI数据极度匮乏，但基于TPX2在细胞周期调控中公认的角色，其潜在关键互作伙伴包括Aurora A（AURKA）、Importin-alpha（KPNA2）、Eg5（KIF11）及多种有丝分裂检查点蛋白。值得注意的是，TPX2被报道具有核定位信号（NLS）依赖的核转运机制，但该TrEMBL变体缺少GO-CC核定位注释。

TE调控相关性方面，TPX2主要定位于有丝分裂纺锤体而非染色质，其直接参与转录调控的证据薄弱。然而，有文献表明TPX2可间接影响基因表达——通过激活Aurora A激酶，下游的信号级联（如PLK1-CDC25或AKT-mTOR通路）可能改变转录因子活性和组蛋白修饰谱，进而影响TE区域的染色质可及性。这种间接机制赋予了该蛋白潜在的非经典TE调控角色。

从研究可行性看，该蛋白新颖性极高（10/10新颖性得分），属于未被探索的TrEMBL条目。但由于其功能集中在细胞质纺锤体组装而非核转录调控，作为TE调控研究靶标的优先级极低（归一化67.8/100）。若未来实验数据显示其在核质中有定位（可能通过NLS变异或输入蛋白相互作用异常），其与Aurora A的激酶调控关系可能成为连接细胞周期与TE表达的潜在桥梁。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KM90

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KM90
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KM90
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KM90
