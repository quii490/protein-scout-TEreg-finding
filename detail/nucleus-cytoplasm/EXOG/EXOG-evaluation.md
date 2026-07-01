---
type: protein-evaluation
gene: "EXOG"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## EXOG (Nuclease EXOG, mitochondrial) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | EXOG |
| 蛋白全称 | Nuclease EXOG, mitochondrial |
| UniProt ID | Q9Y2C4 |
| 蛋白大小 | 368.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 368 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR044929, IPR001604, IPR020821, IPR041003|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=51 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Mitochondrion + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: EXOG 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Mitochondrion + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

mitochondrial endonuclease, apoptotic nuclear translocation。

#### 3.3 PPI 网络

PPI degree=51。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

EXOG 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR044929 |
| InterPro | IPR001604 |
| InterPro | IPR020821 |
| InterPro | IPR041003 |
| InterPro | IPR044925 |
| InterPro | IPR040255 |
| Pfam | PF01223 |
| Pfam | PF18026 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000157036-EXOG

![](https://images.proteinatlas.org/71050/1332_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/71050/1332_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/71050/1411_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/71050/1411_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/71050/1358_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/71050/1358_H1_4_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00892;SM00477; |
| InterPro | IPR044929;IPR001604;IPR020821;IPR041003;IPR044925;IPR040255; |
| Pfam | PF01223;PF18026; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FEN1 | STRING | 741 |
| EIF2B2 | BioGRID | 1 |
| CDH5 | BioGRID | 1 |
| RANBP6 | BioGRID | 1 |
| TRDN | BioGRID | 1 |
| RIPPLY2 | BioGRID | 1 |
| RBM4 | BioGRID | 1 |
| MEPCE | BioGRID | 1 |


### PubMed

**Count: 48**

| PMID | Title |
|---|---|
| 42278383 | Single-Nucleotide Polymorphisms in Genes Associated with Mitochondrial and DNA Damage Response Modulate the Risk of Non-Alcoholic Fatty Liver Disease  |
| 41760790 | Machine learning-based identification of potential diagnostic signatures in spinal cord injury. |
| 41680859 | Forecasting malaria incidence in a resource-limited urban setting with climate variables as exogenous regressors: time series analysis using a SARIMAX |
| 40042814 | Mitochondrial exonuclease EXOG supports DNA integrity by the removal of single-stranded DNA flaps. |
| 38918595 | Artificial intelligence-enhanced electrocardiography derived body mass index as a predictor of future cardiometabolic disease. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/EXOG_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.91 |
| pLDDT > 0.9 占比 | 79.1% |
| pLDDT < 0.5 占比 | 1.6% |
| 建模残基数 | 368 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2C4
- HPA: https://www.proteinatlas.org/
