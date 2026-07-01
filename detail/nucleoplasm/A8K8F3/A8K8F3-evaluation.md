---
type: protein-evaluation
gene: "A8K8F3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K8F3 (cDNA FLJ76680, highly similar to Homo sapiens chromodomain protein, Y-linked, 1 (CDY1), transcript variant 2, mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K8F3 |
| 蛋白全称 | cDNA FLJ76680, highly similar to Homo sapiens chromodomain protein, Y-linked, 1 (CDY1), transcript variant 2, mRNA |
| UniProt ID | A8K8F3 |
| 蛋白大小 | 554 aa / 60.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 554 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR016197; InterPro:IPR000953; InterPro:IPR017984; InterPro:IPR023780; InterPro:IPR023779; InterPro:IPR029045 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR016197 |
| InterPro | IPR000953 |
| InterPro | IPR017984 |
| InterPro | IPR023780 |
| InterPro | IPR023779 |
| InterPro | IPR029045 |
| InterPro | IPR051053 |
| InterPro | IPR001753 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8K8F3编码CDY1（Chromodomain protein Y-linked 1）同源蛋白的TrEMBL变体，其结构域架构以染色质识别与修饰的双模块串联为特征：N端chromodomain（IPR016197、IPR000953、IPR023780、IPR023779）识别Lys9位甲基化的组蛋白H3（H3K9me2/me3）或H3K27me3，是HP1/chromo蛋白超家族的保守折叠；C端crotonase-like折叠域（IPR029045）与C端的组蛋白乙酰转移酶（HAT）活性相关——CDY1被Swiss-Prot注释为拥有HAT活性（IPR051053），催化组蛋白H4的Lys5/Lys8/Lys12位点乙酰化（Pfam MALAT1_like域 IPR001753可能参与RNA结合）。

554 aa（60.9 kDa）的含量构造赋予该蛋白在执行多步染色质修饰中所需的结构空间。AlphaFold预测结构可用。作为TrEMBL未审阅条目（PubMed=0），PPI数据有限，但基于Swiss-Prot中CDY1/CDY2家族已注释的角色，其互作伙伴可能包括H3K9甲基转移酶（如G9a/EHMT2、SUV39H1）、HP1异构体及转录共激活因子。

TE调控相关性从机制推论来看极为直接——CDY1通过chromodomain读取H3K9me3/H3K27me3标记后，利用其HAT催化模块对邻近组蛋白尾进行乙酰化，从而可能**转换**TE区域的染色质状态：从紧缩的异染色质（H3K9me3富集）转变为开放的常染色质（H4乙酰化富集）。这一"阅读-书写"（reader-writer）机制意味着CDY1可以是TE调控的动态开关——在特定发育窗口或应激条件下激活特定TE家族。此外，CDY1的Y染色体特异性和生殖细胞表达模式与TE在精子发生过程中的去抑制或激活窗高度吻合。

然而，GO-CC缺乏核定位注释（核定位特异性仅4/10）和PubMed=0的状态是主要限制。但基于chromodomain的H3K9me3结合能力和HAT催化模块的双重功能，该蛋白在TE调控候选列表中的潜力远高于当前归一化评分（67.8/100）所反映的水平。建议优先进行核定位IF验证和chromodomain甲基化结合实验。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K8F3

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K8F3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K8F3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K8F3
