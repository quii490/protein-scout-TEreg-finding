---
type: protein-evaluation
gene: "FAM187A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM187A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM187A |
| 蛋白名称 | Ig-like V-type domain-containing protein FAM187A |
| 蛋白大小 | 413 aa / 47.3 kDa |
| UniProt ID | A6NFU0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Acrosome; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 47.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039311, IPR007110, IPR036179, IPR013783, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Acrosome | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Genes for Improving Cold Sensitivity in Nerve-Damaged Rats Via Lumbar Sympathectomy Using Poly(A)-seq.. *Journal of integrative neuroscience*. PMID: 40613370
2. The SPARK complex forms the molecular basis of vertebrate fertilization.. *bioRxiv : the preprint server for biology*. PMID: 42182320

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.2% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 80.4% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.9，有序区 80.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039311, IPR007110, IPR036179, IPR013783, IPR013106; Pfam: PF07686 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INSYN1 | 0.600 | 0.000 | — |
| METTL21C | 0.516 | 0.000 | — |
| RHBG | 0.466 | 0.000 | — |
| FOXR1 | 0.454 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 4，IntAct interactions: 0
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 无 | pLDDT=82.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Acrosome | 一致 |
| PPI | STRING + IntAct | 4 + 0 interactions | 数据有限 |

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
1. FAM187A — Ig-like V-type domain-containing protein FAM187A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NFU0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214447-FAM187A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM187A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NFU0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NFU0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
