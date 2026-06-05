---
type: protein-evaluation
gene: "FAM160A1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM160A1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM160A1 / FAM160A1 |
| 蛋白名称 | FHF complex subunit HOOK-interacting protein 1A |
| 蛋白大小 | 1040 aa / 116.6 kDa |
| UniProt ID | Q05DH4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1040 aa / 116.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019384, IPR045669, IPR045668; Pfam: PF19314, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.5/180** | |
| **归一化总分** | | | **59.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM160A1 |

**关键文献**:
1. Coexistence of Rheumatoid Arthritis, Cerebrovascular Disease, and Alzheimer's Disease: A Case Study With Genetic Insights.. *Cureus*. PMID: 41913828
2. Identifying genes and pathways in familial lymphoid cancers using whole exome sequencing.. *Leukemia & lymphoma*. PMID: 41652927

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 40.1% |
| 有序区域 (pLDDT>70) 占比 | 52.7% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 52.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019384, IPR045669, IPR045668; Pfam: PF19314, PF19311, PF10257 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKTIP | 0.930 | 0.830 | — |
| HOOK3 | 0.897 | 0.786 | — |
| HOOK1 | 0.697 | 0.420 | — |
| LZTS2 | 0.596 | 0.000 | — |
| HOOK2 | 0.588 | 0.292 | — |
| AP4E1 | 0.557 | 0.420 | — |
| SIPA1L1 | 0.521 | 0.000 | — |
| FAM160B1 | 0.511 | 0.000 | — |
| GULP1 | 0.511 | 0.000 | — |
| GPR26 | 0.497 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HOOK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AKTIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM160A1 — FHF complex subunit HOOK-interacting protein 1A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1040 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05DH4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164142-FHIP1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM160A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05DH4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q05DH4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
