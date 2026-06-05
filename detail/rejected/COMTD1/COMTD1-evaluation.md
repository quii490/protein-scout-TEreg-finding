---
type: protein-evaluation
gene: "COMTD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COMTD1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMTD1 |
| 蛋白名称 | Catechol O-methyltransferase domain-containing protein 1 |
| 蛋白大小 | 262 aa / 28.8 kDa |
| UniProt ID | Q86VU5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; 额外: Plasma membrane, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 262 aa / 28.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.3; PDB: 2AVD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050362, IPR029063, IPR002935; Pfam: PF01596 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mitochondrial-related genes as prognostic and metastatic markers in breast cancer: insights from comprehensive analysis and clinical models.. *Frontiers in immunology*. PMID: 39380996
2. Identification of a novel transcriptome signature for predicting the response to anti-TNF-α treatment in patients with rheumatoid arthritis.. *Annals of the rheumatic diseases*. PMID: 40908203
3. A frame-shift mutation in COMTD1 is associated with impaired pheomelanin pigmentation in chicken.. *PLoS genetics*. PMID: 37068079
4. A risk prognostic model for patients with esophageal squamous cell carcinoma basing on cuproptosis and ferroptosis.. *Journal of cancer research and clinical oncology*. PMID: 37405477
5. Genomic Binding Patterns of Forkhead Box Protein O1 Reveal Its Unique Role in Cardiac Hypertrophy.. *Circulation*. PMID: 32640834

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.3 |
| 高置信度残基 (pLDDT>90) 占比 | 82.8% |
| 置信残基 (pLDDT 70-90) 占比 | 0.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 13.4% |
| 有序区域 (pLDDT>70) 占比 | 83.6% |
| 可用 PDB 条目 | 2AVD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.3，有序区 83.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050362, IPR029063, IPR002935; Pfam: PF01596 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TK1 | 0.651 | 0.000 | — |
| TYMP | 0.585 | 0.000 | — |
| DUS2 | 0.551 | 0.000 | — |
| MCRIP2 | 0.541 | 0.000 | — |
| MAT1A | 0.516 | 0.000 | — |
| MAT2A | 0.515 | 0.000 | — |
| MAP6D1 | 0.514 | 0.066 | — |
| DNAJC1 | 0.513 | 0.000 | — |
| PAXBP1 | 0.489 | 0.000 | — |
| TMC4 | 0.487 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000361616.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PNO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| UBQLN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| EIF4G3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IFRD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GEMIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPAG9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.3 + PDB: 2AVD | pLDDT=89.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COMTD1 — Catechol O-methyltransferase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小262 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VU5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165644-COMTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VU5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VU5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
