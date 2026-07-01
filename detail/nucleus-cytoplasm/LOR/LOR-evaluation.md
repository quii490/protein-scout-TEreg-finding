---
type: protein-evaluation
gene: "LOR"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## LOR (Loricrin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LOR |
| 蛋白全称 | Loricrin |
| UniProt ID | P23490 |
| 蛋白大小 | 312.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 312 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | IPR031700, PF15847|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=35 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cornified envelope + Nucleoplasm | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: LOR 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cornified envelope + Nucleoplasm。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

keratinocyte envelope structural。

#### 3.3 PPI 网络

PPI degree=35。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

LOR 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Loricrin

**功能**: Major keratinocyte cell envelope protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031700 |
| Pfam | PF15847 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR031700; |
| Pfam | PF15847; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IVL | STRING | 999 |
| FLG2 | STRING | 999 |
| FLG | STRING | 998 |
| SNAI1 | STRING | 973 |
| GATA6 | STRING | 915 |
| KRT2 | STRING | 800 |
| CASP14 | STRING | 795 |
| KRT14 | STRING | 782 |


### PubMed

**Count: 2150**

| PMID | Title |
|---|---|
| 42361834 | Feasibility study of image reconstruction for a forceps-type positron emission counter: a simulation-based algorithm comparison. |
| 42353332 | High-Level Secretory Expression of Recombinant Type XVII Human-like Collagen in Komagataella phaffii. |
| 42334954 | Glyphosate in Queensland Waterways: An Ecological Risk Assessment. |
| 42321046 | Activating valence oscillations in reconstructed high-entropy selenide for self-stabilized seawater oxidation through localized lattice oxygen redox. |
| 42298090 | Protective effects of extracellular vesicle-like nanoparticles derived from Cannabis sativa adventitious roots against UVB-induced damage in human ker |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/LOR_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.33 |
| pLDDT > 0.9 | 0.0% |
| pLDDT < 0.5 | 92.0% |
| 残基数 | 312 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P23490
- HPA: https://www.proteinatlas.org/
