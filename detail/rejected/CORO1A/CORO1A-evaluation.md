---
type: protein-evaluation
gene: "CORO1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CORO1A — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=147，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CORO1A |
| 蛋白名称 | Coronin-1A |
| 蛋白大小 | 461 aa / 51.0 kDa |
| UniProt ID | P31146 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Cytoplasmic |
| 蛋白大小 | 10/10 | x1 | 10 | 461 aa / 51.0 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=147 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=93.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Cytoplasmic vesicle, phagosome membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 147 |
| PubMed broad count | 147 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The cytoskeletal regulator Coronin-1A plays a multidirectional role in glioblastoma stemness.. *Sci Rep*. PMID: 42209665
2. Integrated analysis of programmed cell death-related genes identifies CORO1A as an apoptosis-associated gene in acute myeloid leukemia.. *PeerJ*. PMID: 42153148
3. CORO1C (coronin 1C) promotes autophagosome formation by coordinating branched actin network dynamics.. *Autophagy*. PMID: 41968673
4. PCSK9 promotes prostate cancer via facilitating intratumoral cholesterol accumulation and enhancing immunosuppressive tumor microenvironment.. *J Adv Res*. PMID: 41951051
5. Dual regulation of coronin-1 expression by the core promoter and intronic regions.. *J Immunol*. PMID: 41456103

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.1，有序区 94.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFL1 | 0.000 | 0.000 | — |
| CFL2 | 0.000 | 0.000 | — |
| CORO1B | 0.000 | 0.000 | — |
| FGD3 | 0.000 | 0.000 | — |
| WAS | 0.000 | 0.000 | — |
| ITGB2 | 0.000 | 0.000 | — |
| IFT80 | 0.000 | 0.000 | — |
| LAPTM5 | 0.000 | 0.000 | — |
| NCF4 | 0.000 | 0.000 | — |
| ACTR2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P31146 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q15750 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P84022 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P25791 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O15160 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96GM5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P40763 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q13643 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8TB22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5NIE3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 无 | pLDDT=93.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; C / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CORO1A -- Coronin-1A，研究基础较多，新颖性有限。
2. 蛋白大小461 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 147 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P31146
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102879-CORO1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CORO1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P31146
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
