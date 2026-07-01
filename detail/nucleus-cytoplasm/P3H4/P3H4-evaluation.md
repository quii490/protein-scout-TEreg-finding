---
type: protein-evaluation
gene: "P3H4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## P3H4 (ER protein SC65/Leprecan-like 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | P3H4 |
| 蛋白全称 | ER protein SC65/Leprecan-like 4 |
| UniProt ID | Q92791 |
| 蛋白大小 | 437.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 437 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR052284, IPR056585, IPR011990, PF23557|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=68 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | ER + Nucleolus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: P3H4 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为ER + Nucleolus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

collagen prolyl 3-hydroxylation, nuclear annotation contested。

#### 3.3 PPI 网络

PPI degree=68。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

P3H4 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR052284 |
| InterPro | IPR056585 |
| InterPro | IPR011990 |
| Pfam | PF23557 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000141696-P3H4

![](https://images.proteinatlas.org/22520/1139_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22520/1139_B5_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/22520/1971_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22520/1971_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22520/1132_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22520/1132_B5_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR052284;IPR056585;IPR011990; |
| Pfam | PF23557; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPIB | STRING | 839 |
| PLOD1 | STRING | 808 |
| PTEN | BioGRID | 1 |
| FASLG | BioGRID | 1 |
| FOXA3 | BioGRID | 1 |
| ALX3 | BioGRID | 1 |
| APEX1 | BioGRID | 1 |
| WWP2 | BioGRID | 1 |


### PubMed

**Count: 27**

| PMID | Title |
|---|---|
| 41787391 | Novel VSMC-associated biomarkers in intracranial aneurysm pathogenesis: a multi-omics and machine learning study. |
| 41220593 | P3H4 Enhances the Proliferation, Invasion, and Glycolysis of Hepatocellular Carcinoma Cells. |
| 40767885 | Collagen gene signature in the tumor microenvironment predicts survival and guides prognosis in bladder cancer. |
| 39693409 | Dextromethorphan inhibits collagen and collagen-like cargo secretion to ameliorate lung fibrosis. |
| 38706607 | The role of P3H family in cancer: implications for prognosis, tumor microenvironment and drug sensitivity. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q92791
- HPA: https://www.proteinatlas.org/
