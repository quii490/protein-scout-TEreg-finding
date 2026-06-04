---
type: protein-evaluation
gene: "DDAH2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DDAH2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=157，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDAH2 / DDAH, G6A, NG30 |
| 蛋白名称 | Putative hydrolase DDAH2 |
| 蛋白大小 | 285 aa / 29.6 kDa |
| UniProt ID | O95865 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Cytoplasm; Mitochondrion; Mitochondrion |
| 蛋白大小 | 10/10 | x1 | 10 | 285 aa / 29.6 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=157 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR033199 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **66.0/180** | |
| **归一化总分** | | | **36.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Cytoplasm; Mitochondrion; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 157 |
| PubMed broad count | 231 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDAH, G6A, NG30 |

**关键文献**:
1. Early and late-onset preeclampsia: effects of DDAH2 polymorphisms on ADMA levels and association with DDAH2 haplotypes.. *Revista brasileira de ginecologia e obstetricia : revista da Federacao Brasileira das Sociedades de Ginecologia e Obstetricia*. PMID: 38765527
2. DDAH2 suppresses RLR-MAVS-mediated innate antiviral immunity by stimulating nitric oxide-activated, Drp1-induced mitochondrial fission.. *Science signaling*. PMID: 33850055
3. KLF3 aggravates renal fibrosis in chronic kidney disease through transcriptional activation of DDAH2.. *Biochemical pharmacology*. PMID: 40480524
4. DDAH1 and DDAH2 polymorphisms associate with asymmetrical dimethylarginine plasma levels in erectile dysfunction patients but not in healthy controls.. *Nitric oxide : biology and chemistry*. PMID: 31394201
5. Assessment of DDAH1 and DDAH2 Contributions to Psychiatric Disorders via In Silico Methods.. *International journal of molecular sciences*. PMID: 36233204

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 86.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=92.7，有序区 94.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033199 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AGXT2 | 0.795 | 0.000 | — |
| NOS3 | 0.786 | 0.000 | — |
| PRMT1 | 0.759 | 0.000 | — |
| EPB41L2 | 0.742 | 0.742 | — |
| SCGN | 0.723 | 0.370 | — |
| CLNS1A | 0.678 | 0.678 | — |
| DDAH1 | 0.660 | 0.628 | — |
| PRMT2 | 0.625 | 0.000 | — |
| EPB41L3 | 0.621 | 0.621 | — |
| EPB41L1 | 0.613 | 0.613 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 无 | pLDDT=92.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Mitochondrion; Mitochondrion / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DDAH2 -- Putative hydrolase DDAH2，研究基础较多，新颖性有限。
2. 蛋白大小285 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 157 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95865
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213722-DDAH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDAH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95865
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
