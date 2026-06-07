---
type: protein-evaluation
gene: "SIVA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SIVA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIVA1 / SIVA |
| 蛋白名称 | Apoptosis regulatory protein Siva |
| 蛋白大小 | 175 aa / 18.7 kDa |
| UniProt ID | O15304 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 175 aa / 18.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=67 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022773; Pfam: PF05458 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 67 |
| PubMed broad count | 98 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIVA |

**关键文献**:
1. Siva1 is a XIAP-interacting protein that balances NFkappaB and JNK signalling to promote apoptosis.. *Journal of cell science*. PMID: 19584092
2. Exploring the dual role of SIVA1 in cancer biology.. *Gene*. PMID: 40024298
3. Anticancer activity of recombinant Siva1 protein in human nasopharyngeal carcinoma cell line CNE-2.. *Cancer biomarkers : section A of Disease markers*. PMID: 26406409
4. Siva1 suppresses epithelial-mesenchymal transition and metastasis of tumor cells by inhibiting stathmin and stabilizing microtubules.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 21768358
5. Helicobacter pylori pathogen inhibits cellular responses to oncogenic stress and apoptosis.. *PLoS pathogens*. PMID: 35767594

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 19.4% |
| 置信残基 (pLDDT 70-90) 占比 | 49.7% |
| 中等置信 (pLDDT 50-70) 占比 | 19.4% |
| 低置信 (pLDDT<50) 占比 | 11.4% |
| 有序区域 (pLDDT>70) 占比 | 69.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.9，有序区 69.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022773; Pfam: PF05458 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCL2L1 | 0.990 | 0.516 | — |
| CD27 | 0.972 | 0.474 | — |
| BCL2 | 0.938 | 0.294 | — |
| RAD18 | 0.783 | 0.619 | — |
| PCNA | 0.740 | 0.733 | — |
| TNFRSF18 | 0.730 | 0.301 | — |
| XIAP | 0.700 | 0.625 | — |
| STMN1 | 0.687 | 0.510 | — |
| TP53 | 0.658 | 0.510 | — |
| SLC9A3R2 | 0.646 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CD27 | psi-mi:"MI:0018"(two hybrid) | pubmed:9177220 |
| MYZAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BEX3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PCNA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| erpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pyrE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NTAQ1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C2orf68 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP26-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CREB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 无 | pLDDT=75.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SIVA1 — Apoptosis regulatory protein Siva，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 67 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15304
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184990-SIVA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIVA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15304
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000184990-SIVA1/subcellular

![](https://images.proteinatlas.org/65398/1230_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/65398/1230_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/66693/1211_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/66693/1211_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/66693/1217_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/66693/1217_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15304-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15304 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022773; |
| Pfam | PF05458; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184990-SIVA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CD27 | Intact, Biogrid | true |
| PXMP2 | Intact, Biogrid | true |
| ABL2 | Biogrid | false |
| BCL2L1 | Biogrid | false |
| CD4 | Biogrid | false |
| CDKN2A | Biogrid | false |
| FOXP3 | Biogrid | false |
| LPAR2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
