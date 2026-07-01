---
type: protein-evaluation
gene: "FBP1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## FBP1 (Fructose-1,6-bisphosphatase 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FBP1 |
| 蛋白全称 | Fructose-1,6-bisphosphatase 1 |
| UniProt ID | P09467 |
| 蛋白大小 | 338.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 338 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR044015, IPR000146, IPR033391, IPR028343|
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=386 |
| **加权总分** | | | **94/180** | |
| **归一化总分 (÷1.83)** | | | **51/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: FBP1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

gluconeogenesis, nuclear moonlighting in ccRCC。

#### 3.3 PPI 网络

PPI degree=386。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

FBP1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR044015 |
| InterPro | IPR000146 |
| InterPro | IPR033391 |
| InterPro | IPR028343 |
| InterPro | IPR020548 |
| Pfam | PF00316 |
| Pfam | PF18913 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000165140-FBP1

![](https://images.proteinatlas.org/5857/1081_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/5857/1081_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/5857/71_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/5857/71_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/5857/73_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/5857/73_E9_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR044015;IPR000146;IPR033391;IPR028343;IPR020548; |
| Pfam | PF00316;PF18913; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TALDO1 | STRING | 992 |
| NLK | STRING | 992 |
| GPI | STRING | 992 |
| TKT | STRING | 981 |
| PFKFB3 | STRING | 967 |
| PFKFB4 | STRING | 965 |
| PFKFB2 | STRING | 964 |
| FUBP3 | STRING | 889 |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/FBP1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.87 |
| pLDDT > 0.9 占比 | 47.6% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 338 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P09467
- HPA: https://www.proteinatlas.org/
