---
type: protein-evaluation
gene: "FBF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBF1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBF1 / ALB, KIAA1863 |
| 蛋白名称 | Fas-binding factor 1 |
| 蛋白大小 | 1133 aa / 125.4 kDa |
| UniProt ID | Q8TES7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome, Basal body; 额外: Primary cilium; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 1133 aa / 125.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033561, IPR049390; Pfam: PF21007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body; 额外: Primary cilium | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cytoplasm, cytoskelet... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- anchoring junction (GO:0070161)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary transition fiber (GO:0097539)
- ciliary transition zone (GO:0035869)
- cilium (GO:0005929)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALB, KIAA1863 |

**关键文献**:
1. A stress-induced cilium-to-PML-NB route drives senescence initiation.. *Nature communications*. PMID: 37019904
2. Transiently formed nucleus-to-cilium microtubule arrays mediate senescence initiation in a KIFC3-dependent manner.. *Nature communications*. PMID: 39266565
3. TALPID3 and ANKRD26 selectively orchestrate FBF1 localization and cilia gating.. *Nature communications*. PMID: 32366837
4. FBF1 maintains stem cell-like properties in breast cancer via PI3K/AKT/SOX2 axis.. *Stem cell research & therapy*. PMID: 39988656
5. Fbf1 regulates mouse oocyte meiosis by influencing Plk1.. *Theriogenology*. PMID: 33561696

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 49.1% |
| 有序区域 (pLDDT>70) 占比 | 42.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 42.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033561, IPR049390; Pfam: PF21007 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCLT1 | 0.997 | 0.136 | — |
| CEP83 | 0.994 | 0.000 | — |
| CEP164 | 0.990 | 0.046 | — |
| CEP89 | 0.983 | 0.000 | — |
| TRAF3IP1 | 0.886 | 0.091 | — |
| XRN2 | 0.844 | 0.782 | — |
| DXO | 0.843 | 0.782 | — |
| POLR2A | 0.820 | 0.783 | — |
| NIN | 0.807 | 0.000 | — |
| POLR2B | 0.801 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCEA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBGCP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| MAP3K5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ACCS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body; 额外: Primary cilium | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FBF1 — Fas-binding factor 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1133 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TES7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188878-FBF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TES7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
