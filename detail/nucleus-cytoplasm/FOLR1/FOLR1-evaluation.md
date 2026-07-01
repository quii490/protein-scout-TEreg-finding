---
type: protein-evaluation
gene: "FOLR1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## FOLR1 (Folate receptor alpha) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FOLR1 |
| 蛋白全称 | Folate receptor alpha |
| UniProt ID | P15328 |
| 蛋白大小 | 257.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 257 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR004269, IPR018143, PF03024|
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=231 |
| **加权总分** | | | **94/180** | |
| **归一化总分 (÷1.83)** | | | **51/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Plasma membrane + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: FOLR1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Plasma membrane + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

folate uptake, cancer therapeutic target。

#### 3.3 PPI 网络

PPI degree=231。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

FOLR1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR004269 |
| InterPro | IPR018143 |
| Pfam | PF03024 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR004269;IPR018143; |
| Pfam | PF03024; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCBP1 | STRING | 759 |
| EGFR | STRING | 721 |
| IMPDH2 | BioGRID | 1 |
| CUL3 | BioGRID | 1 |
| NCAPH2 | BioGRID | 1 |
| AGO2 | BioGRID | 1 |
| FANCD2 | BioGRID | 1 |
| LTB4R2 | BioGRID | 1 |


### PubMed

**Count: 526**

| PMID | Title |
|---|---|
| 42346396 | Immunometabolic Stratification of Autism Spectrum Disorder by CD4(+) T-Cell Phenotype Reveals Subtype-Specific Energetic Deficit and Coordinated Suppr |
| 42346230 | Consensus Statement from the Society of Gynecologic Oncology of Canada on Folate Receptor α Testing in Ovarian Cancer. |
| 42341116 | FOLR1-targeted actinium-225-based alpha-particle therapy eliminates ovarian cancer. |
| 42322854 | Folate receptor-α targeted therapies in ovarian cancer: recent advances and emerging therapeutic strategies. |
| 42293194 | Excess folic acid disrupts placental endocrine function in vitro: a potential mechanism linking elevated folic acid exposure with gestational diabetes |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/FOLR1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.9 |
| pLDDT > 0.9 | 65.0% |
| pLDDT < 0.5 | 0.0% |
| 残基数 | 257 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P15328
- HPA: https://www.proteinatlas.org/
