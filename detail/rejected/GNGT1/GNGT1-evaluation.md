---
type: protein-evaluation
gene: "GNGT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNGT1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNGT1 |
| 蛋白名称 | Guanine nucleotide-binding protein G(T) subunit gamma-T1 |
| 蛋白大小 | 74 aa / 8.5 kDa |
| UniProt ID | P63211 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 74 aa / 8.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.4; PDB: 7L0P, 7L0Q, 7L0R, 7L0S |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- heterotrimeric G-protein complex (GO:0005834)
- photoreceptor disc membrane (GO:0097381)
- photoreceptor inner segment (GO:0001917)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 63.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 87.8% |
| 可用 PDB 条目 | 7L0P, 7L0Q, 7L0R, 7L0S |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7L0P, 7L0Q, 7L0R, 7L0S）+ AlphaFold高质量预测（pLDDT=88.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1 | 0.999 | 0.999 | — |
| GNB4 | 0.999 | 0.995 | — |
| GNB3 | 0.999 | 0.995 | — |
| GNB2 | 0.998 | 0.995 | — |
| GNAI1 | 0.984 | 0.939 | — |
| CCR5 | 0.981 | 0.816 | — |
| RHO | 0.980 | 0.429 | — |
| PDC | 0.975 | 0.900 | — |
| PDE6A | 0.974 | 0.000 | — |
| GNAT1 | 0.973 | 0.259 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| Kcnk2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23021213|imex:IM-18125 |
| ZNF277 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBXN4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MSANTD4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNAI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 7L0P, 7L0Q, 7L0R, 7L0S | pLDDT=88.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNGT1 — Guanine nucleotide-binding protein G(T) subunit gamma-T1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小74 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63211
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127928-GNGT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNGT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63211
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P63211-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
