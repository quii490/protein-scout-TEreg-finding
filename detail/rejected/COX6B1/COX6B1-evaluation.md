---
type: protein-evaluation
gene: "COX6B1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX6B1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX6B1 / COX6B |
| 蛋白名称 | Cytochrome c oxidase subunit 6B1 |
| 蛋白大小 | 86 aa / 10.2 kDa |
| UniProt ID | P14854 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; 额外: Principal piece; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 86 aa / 10.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=95.0; PDB: 5Z62 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR048280, IPR036549, IPR003213; Pfam: PF02297 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Principal piece | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)
- respiratory chain complex IV (GO:0045277)
- sperm principal piece (GO:0097228)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

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
| AlphaFold 平均 pLDDT | 95.0 |
| 高置信度残基 (pLDDT>90) 占比 | 89.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 5Z62 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=95.0，有序区 100.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048280, IPR036549, IPR003213; Pfam: PF02297 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFA4 | 0.999 | 0.919 | — |
| UQCRQ | 0.999 | 0.978 | — |
| COX5A | 0.999 | 0.974 | — |
| COX6A2 | 0.999 | 0.951 | — |
| UQCRB | 0.999 | 0.980 | — |
| COX5B | 0.999 | 0.974 | — |
| COX6A1 | 0.999 | 0.982 | — |
| COX4I1 | 0.999 | 0.969 | — |
| COX6C | 0.999 | 0.963 | — |
| MT-CO2 | 0.999 | 0.999 | — |

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
| 三维结构 | AlphaFold pLDDT=95.0 + PDB: 5Z62 | pLDDT=95.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Mitochondria; 额外: Principal piece | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COX6B1 -- Cytochrome c oxidase subunit 6B1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小86 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P14854
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126267-COX6B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX6B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P14854
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
