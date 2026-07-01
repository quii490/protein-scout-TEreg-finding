---
type: protein-evaluation
gene: "LATS1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, nucleoplasm]
status: shortlisted
---

## LATS1 (Serine/threonine-protein kinase LATS1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LATS1 |
| 蛋白全称 | Serine/threonine-protein kinase LATS1 |
| UniProt ID | O95835 |
| 蛋白大小 | 1130.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare); GO-CC: Centrosome + Nucleus |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | GO-CC: Centrosome + Nucleus; 功能定义性核定位 |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1130.0 aa |
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | unclassified_bare; PubMed待验证 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF预测可用; 实验结构待验证 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | 功能性结构域存在; 非经典chromatin调控域 |
| 🔗 PPI | 9/10 | ×3 | 27.0 | PPI degree=446 |
| **加权总分** | | | **110/180** | |
| **归一化总分 (÷1.83)** | | | **60/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Centrosome + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |

**分析**: LATS1 的 GO-CC 注释明确支持Centrosome + Nucleus定位。功能为Hippo pathway core kinase, YAP1/TAZ regulation, tumor suppressor，核定位是其功能执行的必要条件。但缺乏 HPA IF 核定位图像验证。

#### 3.2 功能概述

Hippo pathway core kinase, YAP1/TAZ regulation, tumor suppressor。

#### 3.3 TE 调控相关性

LATS1 目前**无直接 TE 调控文献**。其核定位和功能机制提供了间接的调控可能性，但需实验验证。

#### 3.4 PPI 网络

PPI degree=446。核质互作网络规模较大。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**定位分类**: nucleoplasm

LATS1 具有明确的核定位和核功能，但缺乏与 TE 调控的直接实验关联。作为核蛋白靶标具有一定研究价值，TE 调控方向需从头建立假设和验证。

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
| InterPro | IPR000961 |
| InterPro | IPR011009 |
| InterPro | IPR049761 |
| InterPro | IPR042706 |
| InterPro | IPR017892 |
| InterPro | IPR000719 |
| InterPro | IPR008271 |
| InterPro | IPR050236 |
| InterPro | IPR015940 |
| InterPro | IPR009060 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SAV1 | STRING | 999 |
| MOB1A | STRING | 999 |
| MOB1B | STRING | 999 |
| YAP1 | STRING | 999 |
| WWTR1 | STRING | 997 |
| STK3 | STRING | 990 |
| LATS2 | STRING | 989 |
| AMOT | STRING | 982 |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/O95835
- HPA: https://www.proteinatlas.org/
