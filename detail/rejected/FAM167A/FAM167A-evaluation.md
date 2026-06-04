---
type: protein-evaluation
gene: "FAM167A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM167A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM167A / C8orf13 |
| 蛋白名称 | Protein FAM167A |
| 蛋白大小 | 214 aa / 24.2 kDa |
| UniProt ID | Q96KS9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 214 aa / 24.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024280, IPR051771; Pfam: PF11652 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
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
| PubMed strict count | 25 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf13 |

**关键文献**:
1. Association of EBF1, FAM167A(C8orf13)-BLK and TNFSF4 gene variants with primary Sjögren's syndrome.. *Genes and immunity*. PMID: 20861858
2. Single-cell transcriptome-wide Mendelian randomization and colocalization reveal cell-specific mechanisms in systemic lupus erythematosus.. *Rheumatology (Oxford, England)*. PMID: 41233983
3. Post-genome-wide association study dissects genetic vulnerability and risk gene expression of Sjögren's disease for cardiovascular disease.. *Journal of translational medicine*. PMID: 40350475
4. Association studies of TNFSF4, TNFAIP3 and FAM167A-BLK polymorphisms with primary Sjogren's syndrome in Han Chinese.. *Journal of human genetics*. PMID: 23635951
5. The rheumatic disease-associated FAM167A-BLK locus encodes DIORA-1, a novel disordered protein expressed highly in bronchial epithelium and alveolar macrophages.. *Clinical and experimental immunology*. PMID: 29663334

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 34.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 30.8% |
| 有序区域 (pLDDT>70) 占比 | 54.7% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.1，有序区 54.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024280, IPR051771; Pfam: PF11652 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BLK | 0.978 | 0.000 | — |
| MTMR9 | 0.871 | 0.000 | — |
| XKR6 | 0.744 | 0.000 | — |
| MTMR7 | 0.714 | 0.000 | — |
| BANK1 | 0.664 | 0.000 | — |
| PPP1R3B | 0.661 | 0.000 | — |
| PXK | 0.608 | 0.000 | — |
| IRF5 | 0.583 | 0.000 | — |
| PHRF1 | 0.578 | 0.000 | — |
| GMCL1 | 0.572 | 0.572 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GMCL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TXLNB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PPP3CA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SHTN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MID1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCAS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZWINT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEFM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 无 | pLDDT=70.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM167A — Protein FAM167A，非常新颖，仅有少数基础研究。
2. 蛋白大小214 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KS9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154319-FAM167A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM167A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KS9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
