---
type: protein-evaluation
gene: "COMMD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COMMD2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD2 |
| 蛋白名称 | COMM domain-containing protein 2 |
| 蛋白大小 | 199 aa / 22.7 kDa |
| UniProt ID | Q86X83 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | x1 | 8 | 199 aa / 22.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=89.0; PDB: 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR017920, IPR037354; Pfam: PF07258, PF21672 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 56.8% |
| 置信残基 (pLDDT 70-90) 占比 | 40.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 8F2R, 8F2U, 8P0W |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=89.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037354; Pfam: PF07258, PF21672 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD3 | 0.989 | 0.873 | — |
| COMMD4 | 0.987 | 0.873 | — |
| COMMD10 | 0.987 | 0.916 | — |
| CCDC22 | 0.984 | 0.886 | — |
| COMMD5 | 0.980 | 0.891 | — |
| COMMD1 | 0.974 | 0.872 | — |
| COMMD9 | 0.974 | 0.830 | — |
| COMMD6 | 0.972 | 0.831 | — |
| COMMD8 | 0.972 | 0.835 | — |
| COMMD7 | 0.967 | 0.832 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.0 + PDB: 8F2R, 8F2U, 8P0W | pLDDT=89.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COMMD2 -- COMM domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86X83
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114744-COMMD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X83
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
