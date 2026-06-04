---
type: protein-evaluation
gene: "DYNLT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYNLT1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLT1 |
| 蛋白名称 | Dynein light chain Tctex-type 1 |
| 蛋白大小 | 113 aa / 12.5 kDa |
| UniProt ID | P63172 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol, Acrosome; UniProt: Golgi apparatus; Cytoplasm; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 8/10 | ×1 | 8 | 113 aa / 12.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Acrosome | Approved |
| UniProt | Golgi apparatus; Cytoplasm; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 80 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Shared gene signatures between rheumatoid arthritis and Sjögren's syndrome.. *Am J Clin Exp Immunol*. PMID: 42179742
2. Autophagic molecular network in IS pathogenesis: A multi-omics Mendelian randomization study.. *Medicine (Baltimore)*. PMID: 41578456
3. Integrative multi-omics analysis reveals IFIT3⁺ macrophage-associated ISG20 as a prognostic biomarker and elucidates underlying tumor-suppressive mechanisms in ovarian cancer.. *J Ovarian Res*. PMID: 41514449
4. Generation and characterization of a DYNLT1-knockout mouse model reveals electrophysiological alterations and potential mechanistic contributors to atrial fibrillation.. *Biol Open*. PMID: 40457945
5. LINC02363: a potential biomarker for early diagnosis and treatment of sepsis.. *BMC Immunol*. PMID: 40089725

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.1 |
| 高置信度残基 (pLDDT>90) 占比 | 91.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 96.5% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.1，有序区 96.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1I2 | 0.000 | 0.000 | — |
| DYNLL1 | 0.000 | 0.000 | — |
| DYNLRB1 | 0.000 | 0.000 | — |
| TCTEX1D4 | 0.000 | 0.000 | — |
| DYNC1LI1 | 0.000 | 0.000 | — |
| DYNC1H1 | 0.000 | 0.000 | — |
| TCTEX1D2 | 0.000 | 0.000 | — |
| DYNC1I1 | 0.000 | 0.000 | — |
| WDR60 | 0.000 | 0.000 | — |
| DYNC1LI2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P63172 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P51807 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9BQS6 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q13748 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P10599 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q5NFC7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Z336 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P13423 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NP97 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.1 + PDB: 无 | pLDDT=95.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus; Cytoplasm; Cytoplasm, cytoskeleto / Cytosol, Acrosome | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DYNLT1 — Dynein light chain Tctex-type 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小113 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63172
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146425-DYNLT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63172
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
