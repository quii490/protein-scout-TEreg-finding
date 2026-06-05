---
type: protein-evaluation
gene: "GPR52"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR52 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR52 |
| 蛋白名称 | G-protein coupled receptor 52 |
| 蛋白大小 | 361 aa / 41.4 kDa |
| UniProt ID | Q9Y2T5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 41.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.8; PDB: 6LI0, 6LI1, 6LI2, 6LI3, 8HMP, 9IJR, 9IJS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050125, IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The genetic architecture of fibromyalgia across 2.5 million individuals.. *medRxiv : the preprint server for health sciences*. PMID: 41001472
2. Structural basis of ligand recognition and self-activation of orphan GPR52.. *Nature*. PMID: 32076264
3. Orphan GPR52 as an emerging neurotherapeutic target.. *Drug discovery today*. PMID: 38387741
4. Research Progress of G Protein-coupled Receptor 52 on Central Nervous System Diseases.. *Medicinal chemistry (Shariqah (United Arab Emirates))*. PMID: 40444627
5. Orphan receptor-GPR52 inverse agonist efficacy in ameliorating chronic stress-related deficits in reward motivation and phasic accumbal dopamine activity in mice.. *Translational psychiatry*. PMID: 39242529

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 50.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 13.0% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 6LI0, 6LI1, 6LI2, 6LI3, 8HMP, 9IJR, 9IJS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6LI0, 6LI1, 6LI2, 6LI3, 8HMP, 9IJR, 9IJS）+ AlphaFold极高置信度预测（pLDDT=81.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050125, IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNAS | 0.921 | 0.910 | — |
| GNB1 | 0.909 | 0.909 | — |
| GNG2 | 0.816 | 0.816 | — |
| IGHV3-16 | 0.800 | 0.800 | — |
| GPR88 | 0.742 | 0.000 | — |
| RHO | 0.730 | 0.000 | — |
| GPR6 | 0.611 | 0.000 | — |
| GPR158 | 0.548 | 0.000 | — |
| GPR62 | 0.523 | 0.000 | — |
| GPR63 | 0.494 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SYNGR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FITM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RETREG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHPT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMBR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLCD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MBOAT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 6LI0, 6LI1, 6LI2, 6LI3, 8HMP,  | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR52 — G-protein coupled receptor 52，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2T5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203737-GPR52/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR52
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2T5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2T5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
