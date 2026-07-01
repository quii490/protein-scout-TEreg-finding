---
type: protein-evaluation
gene: "PALD1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## PALD1 (Paladin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PALD1 |
| 蛋白全称 | Paladin |
| UniProt ID | Q9ULE6 |
| 蛋白大小 | 856.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 856 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR029021, IPR050561, IPR003595, PF14566|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=79 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: PALD1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

protein tyrosine phosphatase, vascular/immune。

#### 3.3 PPI 网络

PPI degree=79。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

PALD1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR029021 |
| InterPro | IPR050561 |
| InterPro | IPR003595 |
| Pfam | PF14566 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00404;SM01301; |
| InterPro | IPR029021;IPR050561;IPR003595; |
| Pfam | PF14566; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107719-PALD1

![](https://images.proteinatlas.org/17343/2197_B1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17343/2197_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/17343/166_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17343/166_D10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17343/2059_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17343/2059_B3_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZBP1 | BioGRID | 1 |
| IRF7 | BioGRID | 1 |
| CDK13 | BioGRID | 1 |
| SPDL1 | BioGRID | 1 |
| LMNA | BioGRID | 1 |
| ST7 | BioGRID | 1 |
| EMD | BioGRID | 1 |
| RAB9A | BioGRID | 1 |


### PubMed

**Count: 14**

| PMID | Title |
|---|---|
| 40413551 | Role of ZBED3 in PALD1/PIP2- dependent calcium homeostasis during oocyte maturation. |
| 37149695 | Entorhinal cortex epigenome-wide association study highlights four novel loci showing differential methylation in Alzheimer's disease. |
| 34313325 | Whole genome sequencing identifies rare germline variants enriched in cancer related genes in first degree relatives of familial pancreatic cancer pat |
| 33633342 | Admixture/fine-mapping in Brazilians reveals a West African associated potential regulatory variant (rs114066381) with a strong female-specific effect |
| 33369848 | Paladin is a phosphoinositide phosphatase regulating endosomal VEGFR2 signalling and angiogenesis. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9ULE6
- HPA: https://www.proteinatlas.org/
