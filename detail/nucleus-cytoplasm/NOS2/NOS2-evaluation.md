---
type: protein-evaluation
gene: "NOS2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## NOS2 (Nitric oxide synthase, inducible) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | NOS2 |
| 蛋白全称 | Nitric oxide synthase, inducible |
| UniProt ID | P35228 |
| 蛋白大小 | 1153.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1153 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR003097, IPR017927, IPR001094, IPR008254|
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=205 |
| **加权总分** | | | **91/180** | |
| **归一化总分 (÷1.83)** | | | **49/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: NOS2 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

iNOS, NO production, immune response。

#### 3.3 PPI 网络

PPI degree=205。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

NOS2 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR003097 |
| InterPro | IPR017927 |
| InterPro | IPR001094 |
| InterPro | IPR008254 |
| InterPro | IPR001709 |
| InterPro | IPR029039 |
| InterPro | IPR039261 |
| InterPro | IPR023173 |
| InterPro | IPR050607 |
| InterPro | IPR044943 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR003097;IPR017927;IPR001094;IPR008254;IPR001709;IPR029039;IPR039261;IPR023173;IPR050607;IPR044943;IPR044940;IPR044944;IPR012144;IPR004030;IPR036119;IPR001433;IPR017938; |
| Pfam | PF00667;PF00258;PF00175;PF02898; |
| UniProt Domain | DOMAIN 539..677; /note="Flavodoxin-like"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00088"; DOMAIN 730..970; /note="FAD-binding FR-type"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00716" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CALM3 | STRING | 999 |
| HEL-S-72 | STRING | 999 |
| CALM1 | STRING | 999 |
| CALML6 | STRING | 993 |
| AKT1 | STRING | 976 |
| ASS1 | STRING | 973 |
| NOS1 | STRING | 939 |
| AKT3 | STRING | 904 |


### PubMed

**Count: 14879**

| PMID | Title |
|---|---|
| 42373507 | [Effects and mechanisms of broccoli-derived extracellular vesicles on wound healing of full-thickness skin defects in diabetic mice]. |
| 42364119 | ER stress amplifies inflammation via a dual mechanism involving IκBζ-XBP1s synergism and Regnase-1 degradation. |
| 42353825 | Integrative Network Toxicology Reveals Potential Molecular Targets Linking Plasticizer Exposure to Inflammatory Gastrointestinal Disorders. |
| 42347506 | Cyclopiazonic Acid Induces Mitochondrial Oxidative Stress in SH-SY5Y Cells: Protective Effects of Extra Virgin Olive Oil Phenolics. |
| 42342342 | Lactoferrin improves scopolamine-induced memory impairment in mice. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P35228
- HPA: https://www.proteinatlas.org/
