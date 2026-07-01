---
type: protein-evaluation
gene: "LAP3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## LAP3 (Cytosol aminopeptidase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LAP3 |
| 蛋白全称 | Cytosol aminopeptidase |
| UniProt ID | P28838 |
| 蛋白大小 | 519.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 519 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR011356, IPR043472, IPR000819, IPR023042|
| 🔗 PPI | 6/10 | ×3 | 18.0 | PPI degree=137 |
| **加权总分** | | | **88/180** | |
| **归一化总分 (÷1.83)** | | | **48/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: LAP3 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

leucine aminopeptidase, glutathione metabolism。

#### 3.3 PPI 网络

PPI degree=137。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

LAP3 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR011356 |
| InterPro | IPR043472 |
| InterPro | IPR000819 |
| InterPro | IPR023042 |
| InterPro | IPR008283 |
| Pfam | PF00883 |
| Pfam | PF02789 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR011356;IPR043472;IPR000819;IPR023042;IPR008283; |
| Pfam | PF00883;PF02789; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000002549-LAP3

![](https://images.proteinatlas.org/29606/299_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29606/299_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29606/298_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29606/298_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29606/300_D2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29606/300_D2_4_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GGT5 | STRING | 932 |
| GGT7 | STRING | 930 |
| SNRPD3 | STRING | 924 |
| PRODH2 | STRING | 912 |
| PRODH | STRING | 912 |
| GSS | STRING | 911 |
| GCLC | STRING | 900 |
| GOT1 | STRING | 888 |


### PubMed

**Count: 761**

| PMID | Title |
|---|---|
| 42302622 | Integrating genomics and transcriptomics to dissect genetic variants associated with feed efficiency and growth traits in chicken. |
| 42296527 | Improving Molecular-Level Understanding of Atmospheric Oxygenated Organic Molecules Using Online High-Resolution Orbitrap Mass Spectrometry. |
| 42133534 | CRISPR-Cas12a2-Based Multiplexed Diagnostic for Rapid and Highly Sensitive Detection of Respiratory Viruses. |
| 42113057 | Widespread Occurrence of Tire Wear p-Phenylenediamines and Their Quinones in Cloud Water. |
| 42092672 | A health-oriented strategy for identifying and controlling high-risk PM(2.5) sources: Case study of Heze. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P28838
- HPA: https://www.proteinatlas.org/
