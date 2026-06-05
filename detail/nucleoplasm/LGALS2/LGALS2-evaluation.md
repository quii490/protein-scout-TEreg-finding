---
type: protein-evaluation
gene: "LGALS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGALS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALS2 |
| 蛋白名称 | Galectin-2 |
| 蛋白大小 | 132 aa / 14.6 kDa |
| UniProt ID | P05162 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 132 aa / 14.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=96.6; PDB: 1HLC, 5DG1, 5DG2, 5EWS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- galectin complex (GO:1990724)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gene polymorphisms of LGALS2, LGALS3 and LGALS9 in patients with rheumatoid arthritis.. *Cellular immunology*. PMID: 34371260
2. Genetic association between inflammatory genes (IL-1α, CD14, LGALS2, PSMA6) and risk of ischemic stroke: A meta-analysis.. *Meta gene*. PMID: 27014587
3. PPARG, AGTR1, CXCL16 and LGALS2 polymorphisms are correlated with the risk for coronary heart disease.. *International journal of clinical and experimental pathology*. PMID: 26045830
4. Exploring the molecular mechanisms and shared gene signatures between rheumatoid arthritis and diffuse large B cell lymphoma.. *Frontiers in immunology*. PMID: 36389761
5. Overexpression of galectin2 (LGALS2) predicts a better prognosis in human breast cancer.. *American journal of translational research*. PMID: 35559406

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.6 |
| 高置信度残基 (pLDDT>90) 占比 | 96.2% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 1HLC, 5DG1, 5DG2, 5EWS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1HLC, 5DG1, 5DG2, 5EWS）+ AlphaFold高质量预测（pLDDT=96.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LTA | 0.807 | 0.292 | — |
| GAL | 0.784 | 0.000 | — |
| PAICS | 0.767 | 0.000 | — |
| CHD7 | 0.720 | 0.000 | — |
| CLC | 0.709 | 0.000 | — |
| SPX | 0.706 | 0.000 | — |
| LGALS1 | 0.674 | 0.000 | — |
| GALR2 | 0.603 | 0.000 | — |
| LGALS13 | 0.599 | 0.000 | — |
| LGALS9 | 0.581 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| Abcg3 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| Anxa5 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| Fabp6 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| SDCBP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SDCBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KDR | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| STAT3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UMOD | psi-mi:"MI:0008"(array technology) | imex:IM-28589|pubmed:32045104 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.6 + PDB: 1HLC, 5DG1, 5DG2, 5EWS | pLDDT=96.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LGALS2 — Galectin-2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小132 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05162
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100079-LGALS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05162
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05162-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
