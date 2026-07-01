---
type: protein-evaluation
gene: "ODF1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## ODF1 (Outer dense fiber protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ODF1 |
| 蛋白全称 | Outer dense fiber protein 1 |
| UniProt ID | Q14990 |
| 蛋白大小 | 250.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 250 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR002068, IPR008978, IPR037552, IPR037389|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=40 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Centrosome + Nucleus + Flagellum | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: ODF1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Centrosome + Nucleus + Flagellum。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

sperm outer dense fiber, HspB10。

#### 3.3 PPI 网络

PPI degree=40。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

ODF1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR002068 |
| InterPro | IPR008978 |
| InterPro | IPR037552 |
| InterPro | IPR037389 |
| Pfam | PF00011 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000155087-ODF1

![](https://images.proteinatlas.org/64295/2205_A8_24_blue_red_green.jpg)
![](https://images.proteinatlas.org/64295/2205_A8_28_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR002068;IPR008978;IPR037552;IPR037389; |
| Pfam | PF00011; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ODF2 | STRING | 900 |
| SPATC1 | STRING | 885 |
| AKAP3 | STRING | 788 |
| OAZ3 | STRING | 771 |
| CEP128 | STRING | 735 |
| SPAG5 | STRING | 712 |
| CDK5 | BioGRID | 1 |
| CDK5R1 | BioGRID | 1 |


### PubMed

**Count: 110**

| PMID | Title |
|---|---|
| 42009655 | TENT5C extends Odf1 poly(A) tail to sustain sperm morphogenesis and fertility. |
| 40211238 | LncRNA-mRNA co-expression network in the mechanism of butylphthalide treatment for ischemic stroke. |
| 40196629 | TENT5C extends Odf1 poly(A) tail to sustain sperm morphogenesis and fertility. |
| 39506588 | Identification of Potential Biomarkers Associated with Spermatogenesis in Azoospermia. |
| 39386799 | WDR64, a testis-specific protein, is involved in the manchette and flagellum formation by interacting with ODF1. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/ODF1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.65 |
| pLDDT > 0.9 占比 | 8.8% |
| pLDDT < 0.5 占比 | 40.0% |
| 建模残基数 | 250 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q14990
- HPA: https://www.proteinatlas.org/
