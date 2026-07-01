---
type: protein-evaluation
gene: "HENMT1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## HENMT1 (Small RNA 2-O-methyltransferase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | HENMT1 |
| 蛋白全称 | Small RNA 2-O-methyltransferase |
| UniProt ID | Q5T8I9 |
| 蛋白大小 | 393.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 393 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR026610, IPR060207, IPR029063, PF28339|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=23 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: HENMT1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

piRNA 2-O-methylation, germ cell。

#### 3.3 PPI 网络

PPI degree=23。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

HENMT1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR026610 |
| InterPro | IPR060207 |
| InterPro | IPR029063 |
| Pfam | PF28339 |
| Pfam | PF13489 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR026610;IPR060207;IPR029063; |
| Pfam | PF28339;PF13489; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162639-HENMT1

![](https://images.proteinatlas.org/28497/290_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28497/290_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28497/249_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28497/249_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28497/251_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28497/251_A9_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIWIL1 | STRING | 894 |
| PIWIL4 | STRING | 889 |
| TDRD9 | STRING | 796 |
| DICER1 | STRING | 787 |
| TARBP2 | STRING | 786 |
| PIWIL2 | STRING | 779 |
| AGO2 | STRING | 726 |
| MAEL | STRING | 714 |


### PubMed

**Count: 29**

| PMID | Title |
|---|---|
| 42343633 | HENMT1: an RNA methyltransferase in biology and disease. |
| 40645105 | Novel homozygous variants in piRNA pathway factors lead to male infertility in humans. |
| 40463248 | HENMT1 restricts endogenous retrovirus activity by methylation of 3'-tRNA fragments. |
| 39849452 | Development and validation of a novel artificial intelligence algorithm for precise prediction the postoperative prognosis of esophageal squamous cell |
| 39318356 | A homozygous nonsense variant in HENMT1 causes male infertility in humans and mice. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/HENMT1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.85 |
| pLDDT > 0.9 | 55.7% |
| pLDDT < 0.5 | 3.8% |
| 残基数 | 393 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q5T8I9
- HPA: https://www.proteinatlas.org/
