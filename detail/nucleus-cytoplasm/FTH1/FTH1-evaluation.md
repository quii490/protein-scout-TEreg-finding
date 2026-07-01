---
type: protein-evaluation
gene: "FTH1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## FTH1 (Ferritin heavy chain) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FTH1 |
| 蛋白全称 | Ferritin heavy chain |
| UniProt ID | P02794 |
| 蛋白大小 | 183.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 4/10 | ×1 | 4.0 | 183 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR001519, IPR012347, IPR009040, IPR009078|
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=186 |
| **加权总分** | | | **89/180** | |
| **归一化总分 (÷1.83)** | | | **48/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: FTH1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

iron storage, nuclear under oxidative stress。

#### 3.3 PPI 网络

PPI degree=186。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

FTH1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR001519 |
| InterPro | IPR012347 |
| InterPro | IPR009040 |
| InterPro | IPR009078 |
| InterPro | IPR014034 |
| InterPro | IPR008331 |
| Pfam | PF00210 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000167996-FTH1

![](https://images.proteinatlas.org/80735/2274_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/80735/2274_B12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/80736/2274_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80736/2274_C12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/80737/2274_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/80737/2274_D12_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR001519;IPR012347;IPR009040;IPR009078;IPR014034;IPR008331; |
| Pfam | PF00210; |
| UniProt Domain | DOMAIN 11..160; /note="Ferritin-like diiron"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00085" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NCOA4 | STRING | 999 |
| SLC40A1 | STRING | 892 |
| FOSL1 | STRING | 784 |
| AHNAK | STRING | 783 |
| MARK2 | STRING | 776 |
| ROM1 | STRING | 775 |
| GPX4 | STRING | 774 |
| SF1 | STRING | 769 |


### PubMed

**Count: 1465**

| PMID | Title |
|---|---|
| 42371862 | Research Progress In Acupuncture For Parkinson's Disease: Insights Into The Mitochondrial Ferroptosis Pathway. |
| 42365862 | Harnessing natural herbaceous plants against ferroptosis: Implications for managing polycystic ovary syndrome. |
| 42364999 | Targeting macrophage ferritin heavy chain mitigates ferroptosis and lung injury in experimental acute respiratory distress syndrome. |
| 42364863 | SHC4 suppresses ferroptosis and promotes sorafenib resistance in hepatocellular carcinoma by disrupting the interaction between NCOA4 and FTH1. |
| 42361667 | Ferrostatin-1 inhibits ferroptosis and alleviates organophosphate nerve agent-induced cognitive deficits by regulating ACSL4/GPX4 and NCOA4/FTH1 pathw |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/FTH1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.89 |
| pLDDT > 0.9 占比 | 73.2% |
| pLDDT < 0.5 占比 | 3.8% |
| 建模残基数 | 183 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P02794
- HPA: https://www.proteinatlas.org/
