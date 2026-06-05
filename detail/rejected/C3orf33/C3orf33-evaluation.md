---
type: protein-evaluation
gene: "C3orf33"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C3orf33 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C3orf33 |
| 蛋白名称 | Protein C3orf33 |
| 蛋白大小 | 294 aa / 33.8 kDa |
| UniProt ID | Q6P1S2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 33.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042421, IPR035437 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane; Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular space (GO:0005615)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. C3orf33/MISO regulates mitochondrial homeostasis via mitophagy.. *Autophagy*. PMID: 41568773
2. AC3-33, a novel secretory protein, inhibits Elk1 transcriptional activity via ERK pathway.. *Molecular biology reports*. PMID: 20680465
3. Integrative Analysis of Proteome-wide Association Studies and Functional Enrichment Analysis to Identify Genes and Chemicals Associated with Alcohol Dependence.. *Journal of addiction medicine*. PMID: 37267176
4. Prokaryotic expression and characterization of human AC3-33 protein.. *Frontiers in bioscience (Elite edition)*. PMID: 20515784

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 8.5% |
| 置信残基 (pLDDT 70-90) 占比 | 46.9% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 55.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042421, IPR035437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C15orf61 | 0.701 | 0.000 | — |
| C15orf62 | 0.626 | 0.000 | — |
| SLC33A1 | 0.619 | 0.071 | — |
| MRPS18A | 0.501 | 0.114 | — |
| MRPL53 | 0.467 | 0.108 | — |
| MTERF4 | 0.449 | 0.000 | — |
| GFM2 | 0.444 | 0.045 | — |
| DNAJC4 | 0.443 | 0.045 | — |
| DNAJC11 | 0.409 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC39A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEX44 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PCDHGB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EDEM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BSG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RANBP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NKAIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC39A12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAMDC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 2 / 9 = 22%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 22%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 无 | pLDDT=68.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C3orf33 — Protein C3orf33，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P1S2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174928-C3orf33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C3orf33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1S2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1S2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
