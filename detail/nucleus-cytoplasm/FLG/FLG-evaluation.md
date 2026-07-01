---
type: protein-evaluation
gene: "FLG"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## FLG (Filaggrin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FLG |
| 蛋白全称 | Filaggrin |
| UniProt ID | P20930 |
| 蛋白大小 | 4061.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 4061 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR011992, IPR018247, IPR002048, IPR003303|
| 🔗 PPI | 6/10 | ×3 | 18.0 | PPI degree=128 |
| **加权总分** | | | **85/180** | |
| **归一化总分 (÷1.83)** | | | **46/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Keratohyalin granule + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: FLG 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Keratohyalin granule + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

epidermal structural protein, 4061 aa。

#### 3.3 PPI 网络

PPI degree=128。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

FLG 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

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
| Pfam | PF03516 |
| Pfam | PF01023 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00409;SM00408;SM00219; |
| InterPro | IPR028174;IPR016248;IPR007110;IPR036179;IPR013783;IPR013098;IPR003599;IPR003598;IPR013151;IPR011009;IPR000719;IPR017441;IPR050122;IPR001245;IPR008266;IPR020635; |
| Pfam | PF07679;PF00047;PF07714; |
| UniProt Domain | DOMAIN 25..119; /note="Ig-like C2-type 1"; DOMAIN 158..246; /note="Ig-like C2-type 2"; DOMAIN 255..357; /note="Ig-like C2-type 3"; DOMAIN 478..767; /note="Protein kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00159" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000143631-FLG

![](https://images.proteinatlas.org/27505/1320_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27505/1320_B11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/30188/1320_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/30188/1320_F10_5_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LOR | STRING | 998 |
| IVL | STRING | 997 |
| PIK3R1 | STRING | 992 |
| HRAS | STRING | 962 |
| GRB2 | STRING | 961 |
| ZMYM2 | STRING | 957 |
| PIK3R2 | STRING | 948 |
| CTNNB1 | STRING | 947 |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P20930
- HPA: https://www.proteinatlas.org/
