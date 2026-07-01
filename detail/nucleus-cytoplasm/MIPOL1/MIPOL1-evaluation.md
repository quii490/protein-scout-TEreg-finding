---
type: protein-evaluation
gene: "MIPOL1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## MIPOL1 (Mirror-image polydactyly gene 1 protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MIPOL1 |
| 蛋白全称 | Mirror-image polydactyly gene 1 protein |
| UniProt ID | Q8TD10 |
| 蛋白大小 | 442.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 442 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR026175, PF27921, PF27918|
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=111 |
| **加权总分** | | | **85/180** | |
| **归一化总分 (÷1.83)** | | | **46/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytosol + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: MIPOL1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytosol + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

coiled-coil, uncharacterized function。

#### 3.3 PPI 网络

PPI degree=111。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

MIPOL1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR026175 |
| Pfam | PF27921 |
| Pfam | PF27918 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR026175; |
| Pfam | PF27921;PF27918; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151338-MIPOL1

![](https://images.proteinatlas.org/50179/764_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50179/764_G7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/50179/716_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50179/716_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50179/719_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50179/719_G7_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KIAA1328 | STRING | 999 |
| ASTN2 | STRING | 999 |
| FRK | STRING | 999 |
| RPAP2 | STRING | 999 |
| KPNA5 | STRING | 782 |
| LATS2 | BioGRID | 1 |
| ARNT2 | BioGRID | 1 |
| DGCR6 | BioGRID | 1 |


### PubMed

**Count: 27**

| PMID | Title |
|---|---|
| 39726856 | A multi-trait approach identified 7 novel genes for back pain. |
| 38853702 | A novel homozygous FAM92A gene (CIBAR1) variant further confirms its association with non-syndromic postaxial polydactyly type A9 (PAPA9). |
| 38612805 | Proteomic Analyses Reveal the Role of Alpha-2-Macroglobulin in Canine Osteosarcoma Cell Migration. |
| 36067927 | A novel homozygous variant in the GLI1 underlies postaxial polydactyly in a large consanguineous family with intra familial variable phenotypes. |
| 35965362 | Laurin-Sandrow Syndrome: A Case Report and Review of Literature. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8TD10
- HPA: https://www.proteinatlas.org/
