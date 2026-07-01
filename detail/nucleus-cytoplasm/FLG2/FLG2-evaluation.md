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
