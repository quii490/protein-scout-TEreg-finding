---
type: protein-evaluation
gene: "AARD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AARD — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AARD / C8orf85 |
| 蛋白名称 | Alanine- and arginine-rich domain-containing protein |
| 蛋白大小 | 155 aa / 17.6 kDa |
| UniProt ID | Q4LEZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Lipid droplets; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 155 aa / 17.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051771 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Lipid droplets | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 303 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf85 |

**关键文献**:
1. Alanine and arginine rich domain containing protein, Aard, is directly regulated by androgen receptor in mouse Sertoli cells.. *Molecular medicine reports*. PMID: 27959439
2. Twenty years of research on the DFS70/LEDGF autoantibody-autoantigen system: many lessons learned but still many questions.. *Auto- immunity highlights*. PMID: 32127038
3. Genetic variation as a long-distance modulator of RAD21 expression in humans.. *Scientific reports*. PMID: 35906355
4. Aard is specifically up-regulated in Sertoli cells during mouse testis differentiation.. *The International journal of developmental biology*. PMID: 17486547
5. The Nuclear Dense Fine Speckled (DFS) Immunofluorescence Pattern: Not All Roads Lead to DFS70/LEDGFp75.. *Diagnostics (Basel, Switzerland)*. PMID: 36673033

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 53.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 23.9% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 59.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.6，有序区 59.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051771 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRT27 | 0.591 | 0.591 | — |
| IQUB | 0.505 | 0.000 | — |
| LRRC72 | 0.448 | 0.000 | — |
| CST9 | 0.431 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STX5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSGA10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KIAA0753 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT27 | psi-mi:"MI:0090"(protein complementation assay) | pubmed:32296183|imex:IM-25472 |
| CENPQ | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT24 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VPS37C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CEP57 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 15
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 无 | pLDDT=77.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Lipid droplets | 待确认 |
| PPI | STRING + IntAct | 4 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. AARD — Alanine- and arginine-rich domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小155 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4LEZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205002-AARD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AARD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4LEZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Lipid droplets (approved)。来源: https://www.proteinatlas.org/ENSG00000205002-AARD/subcellular

![](https://images.proteinatlas.org/68290/1331_E10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/68290/1331_E10_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/68290/1345_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68290/1345_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68290/1442_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68290/1442_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4LEZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
