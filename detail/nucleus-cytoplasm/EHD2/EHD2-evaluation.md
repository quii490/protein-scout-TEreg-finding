---
type: protein-evaluation
gene: "EHD2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## EHD2 (EH domain-containing protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | EHD2 |
| 蛋白全称 | EH domain-containing protein 2 |
| UniProt ID | Q9NZN4 |
| 蛋白大小 | 543.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 543 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR040990, IPR045063, IPR011992, IPR018247|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=76 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Caveola + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: EHD2 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Caveola + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

dynamin-like GTPase, caveolar endocytosis。

#### 3.3 PPI 网络

PPI degree=76。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

EHD2 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR040990 |
| InterPro | IPR045063 |
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| InterPro | IPR000261 |
| InterPro | IPR031692 |
| InterPro | IPR030381 |
| InterPro | IPR027417 |
| Pfam | PF18150 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00027; |
| InterPro | IPR040990;IPR045063;IPR011992;IPR018247;IPR002048;IPR000261;IPR031692;IPR030381;IPR027417; |
| Pfam | PF18150;PF00350;PF12763;PF16880; |
| UniProt Domain | DOMAIN 55..286; /note="Dynamin-type G"; /evidence="ECO:0000255|PROSITE-ProRule:PRU01055"; DOMAIN 449..537; /note="EH"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00077"; DOMAIN 481..516; /note="EF-hand"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00448" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000024422-EHD2

![](https://images.proteinatlas.org/66751/1667_E12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/66751/1667_E12_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/66751/1653_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66751/1653_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66751/1607_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66751/1607_E12_3_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EHBP1 | STRING | 996 |
| AP2A2 | STRING | 904 |
| CAVIN1 | STRING | 893 |
| PACSIN2 | STRING | 862 |
| DHX16 | BioGRID | 1 |
| BPGM | BioGRID | 1 |
| DDX56 | BioGRID | 1 |
| SPATA24 | BioGRID | 1 |


### PubMed

**Count: 176**

| PMID | Title |
|---|---|
| 42322139 | A Quarter Century of EHD Protein Research: From Endosomal Recycling to Ciliopathies. |
| 42308302 | An F-box protein OsFKF1 interacts with either OsGI or Hd1 and mediates the degradation of OsGI to control flowering time in rice. |
| 42213902 | A Phosphoproteomic Platform Identifies Erythrocyte Membrane Protein Band 4.1-Like 3-Mediated Lipid Droplet Remodeling Linked to Liver Cancer Invasion  |
| 42182235 | Orai1 is required for Ca(2+)-dependent plasma membrane repair and mechanoadaptation. |
| 42162066 | Gene expression profiling by RNA-sequencing reveals regulators of intramuscular fat in Black Slavonian pigs. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NZN4
- HPA: https://www.proteinatlas.org/
