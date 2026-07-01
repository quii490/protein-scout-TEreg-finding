---
type: protein-evaluation
gene: "NECAB3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## NECAB3 (N-terminal EF-hand calcium-binding protein 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | NECAB3 |
| 蛋白全称 | N-terminal EF-hand calcium-binding protein 3 |
| UniProt ID | Q96P71 |
| 蛋白大小 | 396.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 396 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR007138, IPR011008, IPR011992, IPR018247|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=12 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Golgi + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: NECAB3 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Golgi + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

APP/amyloid-beta regulation, HIF1A glycolysis。

#### 3.3 PPI 网络

PPI degree=12。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

NECAB3 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR007138 |
| InterPro | IPR011008 |
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| InterPro | IPR039862 |
| Pfam | PF03992 |
| Pfam | PF13202 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00054; |
| InterPro | IPR007138;IPR011008;IPR011992;IPR018247;IPR002048;IPR039862; |
| Pfam | PF03992;PF13202; |
| UniProt Domain | DOMAIN 36..71; /note="EF-hand"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00448"; DOMAIN 296..385; /note="ABM" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000125967-NECAB3

![](https://images.proteinatlas.org/44785/1526_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44785/1526_G3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44785/1537_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44785/1537_D9_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NECAB1 | STRING | 798 |
| NEK2 | STRING | 738 |
| IKBKG | BioGRID | 1 |
| MYC | BioGRID | 1 |
| APP | BioGRID | 1 |
| APEX1 | BioGRID | 1 |
| FXR1 | BioGRID | 1 |
| DYRK1A | BioGRID | 1 |


### PubMed

**Count: 20**

| PMID | Title |
|---|---|
| 42106700 | Association between air pollution exposure and increased chronic kidney disease risk: the modifying effects of genetic susceptibility, transcriptomic, |
| 40121529 | AAT-MSC-EVs: Novel implications for suppressing ferroptosis, fibrosis and pain associated with chronic pancreatitis. |
| 39358554 | Sex differences in DNA methylation variations according to ART conception-evidence from the Norwegian mother, father, and child cohort study. |
| 39296922 | NECAB1-3, parvalbumin, calbindin, and calretinin in the hippocampus of the European mole. |
| 38934399 | NECAB family of neuronal calcium-binding proteins in health and disease. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/NECAB3_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.69 |
| pLDDT > 0.9 | 14.4% |
| pLDDT < 0.5 | 15.4% |
| 残基数 | 396 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96P71
- HPA: https://www.proteinatlas.org/
