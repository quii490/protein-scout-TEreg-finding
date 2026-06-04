---
type: protein-evaluation
gene: "CRYGS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRYGS — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYGS |
| 蛋白名称 | Gamma-crystallin S |
| 蛋白大小 | 178 aa / 21.0 kDa |
| UniProt ID | P22914 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 178 aa / 21.0 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=95.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 87 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Evaluating gene-disease relationship strength in crystallin genes in association with pediatric cataracts.. *Ophthalmic Genet*. PMID: 42091610
2. Myodes rufocanus Cataract Identification and Transcriptome Analysis.. *Genes (Basel)*. PMID: 42194952
3. Genetic analysis and clinical characteristics of sporadic and familial congenital cataracts in southern Chinese families.. *Front Genet*. PMID: 41822754
4. Case report of a CRYGS gene mutation in a patient with congenital cataracts and secondary glaucoma.. *Am J Transl Res*. PMID: 40950277
5. Lens Cytoskeleton: An Update on the Etiopathogenesis of Human Cataracts.. *Cureus*. PMID: 38650819

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 94.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 97.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.3，有序区 97.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRYAA | 0.000 | 0.000 | — |
| BFSP2 | 0.000 | 0.000 | — |
| CRYAB | 0.000 | 0.000 | — |
| GJA8 | 0.000 | 0.000 | — |
| GJA3 | 0.000 | 0.000 | — |
| BFSP1 | 0.000 | 0.000 | — |
| PITX3 | 0.000 | 0.000 | — |
| MIP | 0.000 | 0.000 | — |
| HSF4 | 0.000 | 0.000 | — |
| LIM2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P22914 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 7
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 7 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 无 | pLDDT=95.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 待确认 |
| PPI | STRING + IntAct | 25 + 7 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRYGS -- Gamma-crystallin S，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小178 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22914
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213139-CRYGS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYGS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22914
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
