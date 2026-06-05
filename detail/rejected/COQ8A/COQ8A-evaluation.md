---
type: protein-evaluation
gene: "COQ8A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ8A — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ8A / ADCK3, CABC1 |
| 蛋白名称 | Atypical kinase COQ8A, mitochondrial |
| 蛋白大小 | 647 aa / 72.0 kDa |
| UniProt ID | Q8NI60 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 647 aa / 72.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=69.6; PDB: 4PED, 5I35, 7UDP, 7UDQ |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR004147, IPR034646, IPR051409, IPR011009; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- extrinsic component of mitochondrial inner membrane (GO:0031314)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

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
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.9% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 30.0% |
| 有序区域 (pLDDT>70) 占比 | 62.1% |
| 可用 PDB 条目 | 4PED, 5I35, 7UDP, 7UDQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.6），有序残基占 62.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004147, IPR034646, IPR051409, IPR011009; Pfam: PF03109 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ9 | 0.991 | 0.427 | — |
| PDSS1 | 0.988 | 0.059 | — |
| COQ2 | 0.984 | 0.079 | — |
| COQ6 | 0.977 | 0.367 | — |
| PDSS2 | 0.970 | 0.059 | — |
| COQ3 | 0.969 | 0.509 | — |
| COQ5 | 0.962 | 0.678 | — |
| COQ4 | 0.927 | 0.125 | — |
| COQ7 | 0.919 | 0.301 | — |
| APTX | 0.885 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=69.6 + PDB: 4PED, 5I35, 7UDP, 7UDQ | pLDDT=69.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COQ8A -- Atypical kinase COQ8A, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小647 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NI60
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163050-COQ8A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ8A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NI60
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NI60-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
