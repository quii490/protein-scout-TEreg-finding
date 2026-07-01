---
type: protein-evaluation
gene: "HLCS"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, nucleoplasm]
status: shortlisted
---

## HLCS (Biotin--protein ligase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | HLCS |
| 蛋白全称 | Biotin--protein ligase |
| UniProt ID | P50747 |
| 蛋白大小 | 726.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare); GO-CC: Chromatin + Nuclear lamina + Nuclear matrix |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | GO-CC: Chromatin + Nuclear lamina + Nuclear matrix; 功能定义性核定位 |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 726.0 aa |
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | unclassified_bare; PubMed待验证 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF预测可用; 实验结构待验证 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | 功能性结构域存在; 非经典chromatin调控域 |
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=44 |
| **加权总分** | | | **94/180** | |
| **归一化总分 (÷1.83)** | | | **51/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Chromatin + Nuclear lamina + Nuclear matrix | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |

**分析**: HLCS 的 GO-CC 注释明确支持Chromatin + Nuclear lamina + Nuclear matrix定位。功能为holocarboxylase synthetase, chromatin biotinylation，核定位是其功能执行的必要条件。但缺乏 HPA IF 核定位图像验证。

#### 3.2 功能概述

holocarboxylase synthetase, chromatin biotinylation。

#### 3.3 TE 调控相关性

HLCS 目前**无直接 TE 调控文献**。其核定位和功能机制提供了间接的调控可能性，但需实验验证。

#### 3.4 PPI 网络

PPI degree=44。核质互作网络规模较小。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**定位分类**: nucleoplasm

HLCS 具有明确的核定位和核功能，但缺乏与 TE 调控的直接实验关联。作为核蛋白靶标具有一定研究价值，TE 调控方向需从头建立假设和验证。

**核心优势**:
- 明确的 GO-CC 核定位注释
- 功能定义性核蛋白

**风险**:
- 无 HPA IF 核定位图像
- 无 TE 调控文献
- 无 ChIP-Seq 实验数据

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR045864 |
| InterPro | IPR004408 |
| InterPro | IPR003142 |
| InterPro | IPR004143 |
| Pfam | PF02237 |
| Pfam | PF03099 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BTD | STRING | 996 |
| POT1 | BioGRID | 1 |
| HLCS | BioGRID | 1 |
| DDX52 | BioGRID | 1 |
| TBC1D20 | BioGRID | 1 |
| CDKN3 | BioGRID | 1 |
| PTP4A1 | BioGRID | 1 |
| RAB9A | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159267-HLCS

![](https://images.proteinatlas.org/17379/173_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/173_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_2_blue_red_green.jpg)

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P50747
- HPA: https://www.proteinatlas.org/

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159267-HLCS

![](https://images.proteinatlas.org/17379/173_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/173_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159267-HLCS

![](https://images.proteinatlas.org/17379/173_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/173_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/140_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17379/168_C2_2_blue_red_green.jpg)
