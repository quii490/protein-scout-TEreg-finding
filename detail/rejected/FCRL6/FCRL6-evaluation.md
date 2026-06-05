---
type: protein-evaluation
gene: "FCRL6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FCRL6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCRL6 / FCRH6 |
| 蛋白名称 | Fc receptor-like protein 6 |
| 蛋白大小 | 434 aa / 47.7 kDa |
| UniProt ID | Q6DN72 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 434 aa / 47.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- external side of plasma membrane (GO:0009897)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FCRH6 |

**关键文献**:
1. Roles for the FCRL6 Immunoreceptor in Tumor Immunology.. *Frontiers in immunology*. PMID: 33162991
2. Germline variants and mosaic chromosomal alterations affect COVID-19 vaccine immunogenicity.. *Cell genomics*. PMID: 40043710
3. FCRL6 receptor: expression and associated proteins.. *Immunology letters*. PMID: 20933011
4. The Identification of Blood Biomarkers of Chronic Neuropathic Pain by Comparative Transcriptomics.. *Neuromolecular medicine*. PMID: 34741226
5. T cell expressions of aberrant gene signatures and Co-inhibitory receptors (Co-IRs) as predictors of renal damage and lupus disease activity.. *Journal of biomedical science*. PMID: 38650001

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 55.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 28.3% |
| 有序区域 (pLDDT>70) 占比 | 67.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.2，有序区 67.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003599; Pfam: PF13895, PF13927 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLAMF8 | 0.525 | 0.000 | — |
| FAM167B | 0.481 | 0.000 | — |
| GZMH | 0.479 | 0.000 | — |
| GZMB | 0.471 | 0.000 | — |
| FGFBP2 | 0.464 | 0.000 | — |
| NKG7 | 0.461 | 0.000 | — |
| MFAP1 | 0.434 | 0.000 | — |
| PIGR | 0.406 | 0.000 | — |
| KIR2DL1 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GALNT15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 无 | pLDDT=76.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FCRL6 — Fc receptor-like protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小434 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6DN72
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181036-FCRL6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCRL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6DN72
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6DN72-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
