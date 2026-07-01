---
type: protein-evaluation
gene: "OTUB1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, nucleoplasm]
status: shortlisted
---

## OTUB1 (Ubiquitin thioesterase OTUB1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | OTUB1 |
| 蛋白全称 | Ubiquitin thioesterase OTUB1 |
| UniProt ID | Q96FW1 |
| 蛋白大小 | 271.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare); GO-CC: Cytosol + Nucleoplasm |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | GO-CC: Cytosol + Nucleoplasm; 功能定义性核定位 |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 271.0 aa |
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | unclassified_bare; PubMed待验证 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF预测可用; 实验结构待验证 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | 功能性结构域存在; 非经典chromatin调控域 |
| 🔗 PPI | 9/10 | ×3 | 27.0 | PPI degree=357 |
| **加权总分** | | | **112/180** | |
| **归一化总分 (÷1.83)** | | | **61/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytosol + Nucleoplasm | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |

**分析**: OTUB1 的 GO-CC 注释明确支持Cytosol + Nucleoplasm定位。功能为deubiquitinase, DNA repair regulation, inhibits RNF168，核定位是其功能执行的必要条件。但缺乏 HPA IF 核定位图像验证。

#### 3.2 功能概述

deubiquitinase, DNA repair regulation, inhibits RNF168。

#### 3.3 TE 调控相关性

OTUB1 目前**无直接 TE 调控文献**。其核定位和功能机制提供了间接的调控可能性，但需实验验证。

#### 3.4 PPI 网络

PPI degree=357。核质互作网络规模较大。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**定位分类**: nucleoplasm

OTUB1 具有明确的核定位和核功能，但缺乏与 TE 调控的直接实验关联。作为核蛋白靶标具有一定研究价值，TE 调控方向需从头建立假设和验证。

**核心优势**:
- 明确的 GO-CC 核定位注释
- 功能定义性核蛋白

**风险**:
- 无 HPA IF 核定位图像
- 无 TE 调控文献
- 无 ChIP-Seq 实验数据

### ESM 结构预测补充 (ESMFold Analysis)

**方法**: 使用 Meta ESM Metagenomic Atlas API 对全长蛋白序列进行 ab initio 折叠预测。
**PDB 文件**: `detail/_esm_structures/OTUB1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.94 |
| pLDDT > 0.9 占比 | 81.9% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 271 |

**与 AlphaFold 对比**:

无 AlphaFold 数据可对比。ESMFold 提供独立的从头折叠验证。

ESMFold 基于进化规模语言模型，对序列空间进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证和补充。


### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR003323 |
| InterPro | IPR016615 |
| InterPro | IPR038765 |
| InterPro | IPR019400 |
| InterPro | IPR042468 |
| InterPro | IPR042467 |
| Pfam | PF10275 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBE2N | STRING | 999 |
| UBE2D1 | STRING | 987 |
| UBA52 | STRING | 978 |
| UBE2D2 | STRING | 976 |
| RPS27A | STRING | 975 |
| UBE2V2 | STRING | 949 |
| TRAF6 | STRING | 948 |
| UBE2D3 | STRING | 945 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167770-OTUB1

![](https://images.proteinatlas.org/80075/2079_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2079_C6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_5_blue_red_green.jpg)

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96FW1
- HPA: https://www.proteinatlas.org/

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167770-OTUB1

![](https://images.proteinatlas.org/80075/2079_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2079_C6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_5_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167770-OTUB1

![](https://images.proteinatlas.org/80075/2079_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2079_C6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2080_C6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80075/2078_C6_5_blue_red_green.jpg)
