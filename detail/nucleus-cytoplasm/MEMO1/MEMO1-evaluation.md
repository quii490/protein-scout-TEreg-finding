---
type: protein-evaluation
gene: "MEMO1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## MEMO1 (Protein MEMO1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MEMO1 |
| 蛋白全称 | Protein MEMO1 |
| UniProt ID | Q9Y316 |
| 蛋白大小 | 297.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 297 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | IPR002737, PF01875|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=63 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytosol + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: MEMO1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytosol + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

cell migration, ERBB2 signaling。

#### 3.3 PPI 网络

PPI degree=63。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

MEMO1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Protein MEMO1

**功能**: May control cell migration by relaying extracellular chemotactic signals to the microtubule cytoskeleton. Mediator of ERBB2 signaling. The MEMO1-RHOA-DIAPH1 signaling pathway plays an important role in ERBB2-dependent stabilization of microtubules at the cell cortex. It controls the localization of APC and CLASP2 to the cell membrane, via the regulation of GSK3B activity. In turn, membrane-bound APC allows the localization of the MACF1 to the cell membrane, which is required for microtubule capt

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002737 |
| Pfam | PF01875 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000162959-MEMO1

![](https://images.proteinatlas.org/57952/1766_G4_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/57952/1766_G4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/57952/1006_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57952/1006_F7_4_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR002737; |
| Pfam | PF01875; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ERBB2 | STRING | 797 |
| REL | BioGRID | 1 |
| TRIM27 | BioGRID | 1 |
| TACC1 | BioGRID | 1 |
| TCF4 | BioGRID | 1 |
| RBM45 | BioGRID | 1 |
| UBE3D | BioGRID | 1 |
| UPF1 | BioGRID | 1 |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/MEMO1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.97 |
| pLDDT > 0.9 占比 | 98.7% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 297 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9Y316
- HPA: https://www.proteinatlas.org/
