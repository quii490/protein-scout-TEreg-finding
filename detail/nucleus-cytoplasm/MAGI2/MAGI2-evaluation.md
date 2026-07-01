---
type: protein-evaluation
gene: "MAGI2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## MAGI2 (Membrane-associated guanylate kinase WW and PDZ 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MAGI2 |
| 蛋白全称 | Membrane-associated guanylate kinase WW and PDZ 2 |
| UniProt ID | Q86UL8 |
| 蛋白大小 | 1455.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1455 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR008145, IPR008144, IPR020590, IPR027417|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=46 |
| **加权总分** | | | **73/180** | |
| **归一化总分 (÷1.83)** | | | **39/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Tight junction + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: MAGI2 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Tight junction + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

synaptic scaffold, MAGUK family。

#### 3.3 PPI 网络

PPI degree=46。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

MAGI2 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR008145 |
| InterPro | IPR008144 |
| InterPro | IPR020590 |
| InterPro | IPR027417 |
| InterPro | IPR001478 |
| InterPro | IPR036034 |
| InterPro | IPR001202 |
| InterPro | IPR036020 |
| Pfam | PF00625 |
| Pfam | PF16663 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00072;SM00228;SM00456; |
| InterPro | IPR008145;IPR008144;IPR020590;IPR027417;IPR001478;IPR036034;IPR001202;IPR036020; |
| Pfam | PF00625;PF16663;PF00595;PF00397; |
| UniProt Domain | DOMAIN 17..101; /note="PDZ 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 109..283; /note="Guanylate kinase-like"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00100"; DOMAIN 302..335; /note="WW 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00224"; DOMAIN 348..381; /note="WW 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00224"; DOMAIN 426..510; /note="PDZ 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 605..683; /note="PDZ 3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 778..860; /note="PDZ 4"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 920..1010; /note="PDZ 5"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 1147..1229; /note="PDZ 6"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTEN | STRING | 998 |
| TEP1 | STRING | 998 |
| CTNNB1 | STRING | 986 |
| BAP1 | STRING | 922 |
| MAGI1 | STRING | 922 |
| NLGN1 | STRING | 893 |
| KIDINS220 | STRING | 808 |
| TAMALIN | STRING | 796 |


### PubMed

**Count: 344**

| PMID | Title |
|---|---|
| 42331551 | [cfDNA sequencing reveals response heterogeneity to first-line camrelizumab plus chemotherapy in esophageal squamous cell carcinoma]. |
| 42310233 | Pan-cancer and single-cell analysis identifies MAGI2-AS3 as an immune regulator and prognostic biomarker with a focus on colorectal cancer. |
| 42166848 | The association of non-alcoholic fatty liver index, plasma metal levels, and genetic susceptibility using genome-wide type analysis. |
| 41870210 | Extended motif recognition tunes WW domain affinity in MAGI-IQSEC complexes. |
| 41840107 | Genetic basis of immunity in Indian cattle as revealed by comparative analysis of Bos genome. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q86UL8
- HPA: https://www.proteinatlas.org/
