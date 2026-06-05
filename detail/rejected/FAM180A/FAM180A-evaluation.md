---
type: protein-evaluation
gene: "FAM180A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM180A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM180A |
| 蛋白名称 | Protein FAM180A |
| 蛋白大小 | 173 aa / 19.7 kDa |
| UniProt ID | Q6UWF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 173 aa / 19.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029170; Pfam: PF15173 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- extracellular region (GO:0005576)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Insights into growth retardation and dwarfism caused by goose parvovirus in goslings: a transcriptomic profiling study.. *Frontiers in veterinary science*. PMID: 40395806
2. Molecular analysis of the TGF-beta controlled gene expression program in chicken embryo dermal myofibroblasts.. *Gene*. PMID: 23127594
3. Integrative microRNA and transcriptome analysis reveals sex-specific molecular divergence in human bladder cancer.. *Biology of sex differences*. PMID: 41578372

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 64.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.6，有序区 85.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029170; Pfam: PF15173 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PI15 | 0.566 | 0.000 | — |
| SLC25A29 | 0.517 | 0.000 | — |
| ANKS1A | 0.514 | 0.000 | — |
| COL28A1 | 0.510 | 0.000 | — |
| GCC2 | 0.505 | 0.000 | — |
| KLHL35 | 0.485 | 0.000 | — |
| GLT6D1 | 0.479 | 0.000 | — |
| TCP11 | 0.473 | 0.000 | — |
| FANCE | 0.448 | 0.000 | — |
| C17orf67 | 0.437 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 14，IntAct interactions: 0
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 无 | pLDDT=86.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Vesicles | 一致 |
| PPI | STRING + IntAct | 14 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM180A — Protein FAM180A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小173 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189320-FAM180A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM180A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UWF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
