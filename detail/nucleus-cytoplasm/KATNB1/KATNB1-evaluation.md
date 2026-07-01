---
type: protein-evaluation
gene: "KATNB1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## KATNB1 (Katanin p80 WD40 subunit B1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KATNB1 |
| 蛋白全称 | Katanin p80 WD40 subunit B1 |
| UniProt ID | Q9BVA0 |
| 蛋白大小 | 655.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 655 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR028021, IPR026962, IPR015943, IPR020472|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=65 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Centrosome + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: KATNB1 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Centrosome + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

microtubule severing, mitosis。

#### 3.3 PPI 网络

PPI degree=65。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

KATNB1 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR028021 |
| InterPro | IPR026962 |
| InterPro | IPR015943 |
| InterPro | IPR020472 |
| InterPro | IPR019775 |
| InterPro | IPR036322 |
| InterPro | IPR001680 |
| Pfam | PF13925 |
| Pfam | PF00400 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00320; |
| InterPro | IPR028021;IPR026962;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF13925;PF00400; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KATNA1 | STRING | 999 |
| KATNBL1 | STRING | 964 |
| KATNAL2 | STRING | 849 |
| ASPM | STRING | 780 |
| TUBB2A | STRING | 769 |
| TUBA1A | STRING | 765 |
| TUBG1 | STRING | 737 |
| TUBB5 | STRING | 735 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140854-KATNB1

![](https://images.proteinatlas.org/41165/489_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41165/489_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41165/484_E4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41165/484_E4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/41165/492_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41165/492_E4_3_blue_red_green.jpg)

### PubMed

**Count: 37**

| PMID | Title |
|---|---|
| 40586731 | Delta tubulin stabilizes male meiotic kinetochores and aids microtubule remodeling and fertility. |
| 39275889 | Katanin regulatory subunit B1 (KATNB1) regulates BTB dynamics through changes in cytoskeletal organization. |
| 38636565 | Mediterranean diet protects against a neuroinflammatory cortical transcriptome: Associations with brain volumetrics, peripheral inflammation, social i |
| 38193103 | The Challenge of Somatic Variants in Focal Cortical Dysplasia. |
| 37961556 | Mediterranean Diet Protects Against a Neuroinflammatory Cortical Transcriptome: Associations with Brain Volumetrics, Peripheral Inflammation, Social I |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9BVA0
- HPA: https://www.proteinatlas.org/
