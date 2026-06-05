---
type: protein-evaluation
gene: "FAM222A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM222A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM222A / C12orf34 |
| 蛋白名称 | Protein FAM222A |
| 蛋白大小 | 452 aa / 46.8 kDa |
| UniProt ID | Q5U5X8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; 额外: Cell Junctions, Midbody ring; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 46.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029340; Pfam: PF15258 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Cell Junctions, Midbody ring | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf34 |

**关键文献**:
1. Ab initio and comparative 3D modeling of FAM222A-encoded protein and target-driven-based virtual screening for the identification of novel therapeutics against Alzheimer's disease.. *Journal of molecular graphics & modelling*. PMID: 37552909
2. FAM222A encodes a protein which accumulates in plaques in Alzheimer's disease.. *Nature communications*. PMID: 31964863
3. Gene Co-Expression Analysis of Multiple Brain Tissues Reveals Correlation of FAM222A Expression with Multiple Alzheimer's Disease-Related Genes.. *Journal of Alzheimer's disease : JAD*. PMID: 37092222
4. An integrative lipidomics and transcriptomics study revealing Bavachin and Icariin synergistically induce idiosyncratic liver injury.. *Immunopharmacology and immunotoxicology*. PMID: 39505304
5. Reactive astrocytes express Aggregatin (FAM222A) in the brains of Alzheimer's disease and Nasu-Hakola disease.. *Intractable & rare diseases research*. PMID: 33139980

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 25.7% |
| 低置信 (pLDDT<50) 占比 | 65.0% |
| 有序区域 (pLDDT>70) 占比 | 9.2% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.1），有序残基占 9.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029340; Pfam: PF15258 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEIS2 | 0.785 | 0.785 | — |
| MAB21L1 | 0.784 | 0.784 | — |
| PBX3 | 0.782 | 0.782 | — |
| MEIS1 | 0.780 | 0.780 | — |
| PBX1 | 0.780 | 0.780 | — |
| PBX2 | 0.676 | 0.676 | — |
| NLK | 0.602 | 0.602 | — |
| TBCCD1 | 0.477 | 0.000 | — |
| ANKRD13D | 0.464 | 0.000 | — |
| C7orf57 | 0.460 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NLK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| MEIS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEIS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PBX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PBX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAB21L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.1 + PDB: 无 | pLDDT=49.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Cell Junctions, Midbody ring | 待确认 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. FAM222A — Protein FAM222A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5U5X8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139438-FAM222A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM222A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5U5X8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5U5X8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
