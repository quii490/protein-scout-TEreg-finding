---
type: protein-evaluation
gene: "CHRAC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CHRAC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHRAC1 / CHRAC15 |
| 蛋白名称 | Chromatin accessibility complex protein 1 |
| 蛋白大小 | 131 aa / 14.7 kDa |
| UniProt ID | Q9NRG0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 131 aa / 14.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.3; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR003958, IPR009072, IPR050568; Pfam: PF00808 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **174.5/180** | |
| **归一化总分 (÷1.83)** | | | **95.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | ECO:0000305

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- CHRAC (GO:0008623) [IBA:GO_Central]
- epsilon DNA polymerase complex (GO:0008622) [NAS:UniProtKB]
- nucleus (GO:0005634) [IBA:GO_Central]
- pericentric heterochromatin (GO:0005721) [ISO:ComplexPortal]

**结论**: HPA: Nucleoplasm; UniProt: Nucleus

#### 3.2 蛋白大小评估

**评价**: 131 aa / 14.7 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed 搜索链接 | [CHRAC1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CHRAC1) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 69.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 79.4% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003958, IPR009072, IPR050568; Pfam: PF00808 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: chromatin, nucleosome, remodeling

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLE3 | 0.999 | 0.989 | — |
| BAZ1A | 0.998 | 0.709 | — |
| SMARCA5 | 0.997 | 0.878 | — |
| SMARCA1 | 0.982 | 0.600 | — |
| POLE2 | 0.963 | 0.000 | — |
| POLE | 0.957 | 0.091 | — |
| NFYB | 0.924 | 0.745 | — |
| POLE4 | 0.921 | 0.000 | — |
| POLA2 | 0.920 | 0.000 | — |
| CRCP | 0.917 | 0.206 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| PJA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MCF2L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SLC35G2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ACTC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| CAPN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| FSD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| TAS2R41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| POLE3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=85.3, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 95.4/100

**核心优势**:
1. CHRAC1 — Chromatin accessibility complex protein 1，极度新颖，几乎未被系统研究（PubMed 9 篇）。
2. 蛋白大小131 aa，适合大部分生化实验。
3. AlphaFold pLDDT=85.3，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRG0
- Protein Atlas: https://www.proteinatlas.org/search/CHRAC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHRAC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRG0
- STRING: https://string-db.org/network/9606.CHRAC1
- Packet data timestamp: 2026-06-03 08:04:19

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104472-CHRAC1/subcellular

![](https://images.proteinatlas.org/59008/1020_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/59008/1020_H9_4_red_green.jpg)
![](https://images.proteinatlas.org/59008/993_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/59008/993_H9_3_red_green.jpg)
![](https://images.proteinatlas.org/59008/997_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/59008/997_A11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRG0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRG0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003958;IPR009072;IPR050568; |
| Pfam | PF00808; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104472-CHRAC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAZ1A | Biogrid, Opencell | true |
| POLE3 | Intact, Biogrid, Bioplex | true |
| SMARCA5 | Biogrid, Opencell | true |
| FAM9B | Intact | false |
| HMGA1 | Opencell | false |
| HMGN5 | Opencell | false |
| MECP2 | Opencell | false |
| NUCKS1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
