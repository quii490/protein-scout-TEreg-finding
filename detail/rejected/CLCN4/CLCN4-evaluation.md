---
type: protein-evaluation
gene: "CLCN4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLCN4 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLCN4 |
| 蛋白名称 | Chloride channel protein |
| 蛋白大小 | 768 aa / 86.0 kDa |
| UniProt ID | A0A7I2Y1J6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Endosome membrane; Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 768 aa / 86.0 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=82.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Endosome membrane; Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 72 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrative transcriptomics and electrophysiological profiling of hiPSC-derived neurons identifies novel druggable pathways in Koolen-de Vries Syndrome.. *Mol Psychiatry*. PMID: 41680331
2. Population Genomics Provides Novel Insights Into Evolutionary Relationships and Local Adaptation of Two Ecotypes Coilia nasus.. *Ecol Evol*. PMID: 41446387
3. Dominant Action of CLCN4 Neurodevelopmental Disease Variants in Heteromeric Endosomal ClC-3/ClC-4 Transporters.. *Cells*. PMID: 41439993
4. Comorbidity of Attention Deficit Hyperactivity Disorder (ADHD) and Chung-Jansen Syndrome: Case Report and Review of Literature.. *Clin Case Rep*. PMID: 41383545
5. Endosomal 2Cl-/H+ exchangers regulate neuronal excitability by tuning Kv7/KCNQ channel density.. *Brain*. PMID: 40605603

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 41.7% |
| 置信残基 (pLDDT 70-90) 占比 | 43.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.8，有序区 84.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AMELX | 0.000 | 0.000 | — |
| CLIC4 | 0.000 | 0.000 | — |
| MID1 | 0.000 | 0.000 | — |
| CLIC1 | 0.000 | 0.000 | — |
| ASMT | 0.000 | 0.000 | — |
| CLCN5 | 0.000 | 0.000 | — |
| WWC3 | 0.000 | 0.000 | — |
| OSTM1 | 0.000 | 0.000 | — |
| SLC25A6 | 0.000 | 0.000 | — |
| EPRS1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8WTS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P51793 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 5
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 5 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 无 | pLDDT=82.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endosome membrane; Membrane / Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 5 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLCN4 -- Chloride channel protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小768 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A7I2Y1J6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000073464-CLCN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLCN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A7I2Y1J6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
