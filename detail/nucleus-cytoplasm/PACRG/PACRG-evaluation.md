---
type: protein-evaluation
gene: "PACRG"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## PACRG (Parkin coregulated gene protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PACRG |
| 蛋白全称 | Parkin coregulated gene protein |
| UniProt ID | Q96M98 |
| 蛋白大小 | 296.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 296 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | IPR019399, PF10274|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=63 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Axoneme + Nucleus + Manchette | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: PACRG 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Axoneme + Nucleus + Manchette。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

ciliary microtubule inner protein, Parkinson disease。

#### 3.3 PPI 网络

PPI degree=63。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

PACRG 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR019399 |
| Pfam | PF10274 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR019399; |
| Pfam | PF10274; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000112530-PACRG

![](https://images.proteinatlas.org/66293/1376_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/1376_F8_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2148_D5_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2148_D5_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2160_F4_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2160_F4_43_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MEIG1 | STRING | 990 |
| CFAP20 | STRING | 915 |
| PRKN | STRING | 914 |
| TUBA1A | STRING | 895 |
| TEKT2 | STRING | 876 |
| TUBB4B | STRING | 868 |
| NME7 | STRING | 858 |
| PIERCE1 | STRING | 844 |


### PubMed

**Count: 101**

| PMID | Title |
|---|---|
| 41911957 | Transcriptome and alternative splicing analyses uncover immune-centric pathogenesis in periodontitis versus barrier-dysfunction-driven pathogenesis in |
| 41677459 | Correction: DNAH10 interacts with UCHL3-PACRG complex to coordinate sperm head and flagella development during spermiogenesis. |
| 41153639 | Tumour SNPs Associated with Immune-Related Hepatitis in Patients with Melanoma Receiving Immune Checkpoint Inhibitors. |
| 41058558 | DNAH10 interacts with UCHL3-PACRG complex to coordinate sperm head and flagella development during spermiogenesis. |
| 40265567 | In Silico Discovery of Potential Inhibitors Targeting the MEIG1-PACRG Complex for Male Contraceptive Development. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/PACRG_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.78 |
| pLDDT > 0.9 | 42.9% |
| pLDDT < 0.5 | 12.2% |
| 残基数 | 296 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96M98
- HPA: https://www.proteinatlas.org/
