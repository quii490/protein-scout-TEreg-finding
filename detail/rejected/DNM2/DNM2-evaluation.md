---
type: protein-evaluation
gene: "DNM2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNM2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=341，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNM2 |
| 蛋白名称 | Dynamin-2 |
| 蛋白大小 | 870 aa / 98.1 kDa |
| UniProt ID | P50570 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus, Cytosol; UniProt: Cytoplasm, cytoskeleton; Cytoplasmic vesicle, clathrin-coate |
| 蛋白大小 | 8/10 | ×1 | 8 | 870 aa / 98.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=341 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.5/180** | |
| **归一化总分** | | | **33.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasmic vesicle, clathrin-coated vesicle; Cell projection, uropodium; E... | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 341 |
| PubMed broad count | 383 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dynamin 2 Regulates Mitochondrial Mitotic Fission in Pulmonary Hypertension.. *Circ Res*. PMID: 42047020
2. Placental dysregulation of mitochondrial morphology and dynamics as a hallmark of maternal age-related adaptation.. *Life Sci*. PMID: 41861604
3. Beyond Membrane Remodeling: Organelle Crosstalk and Convergent Pathology in Centronuclear Myopathy.. *Muscles*. PMID: 42201138
4. DNM2 lipid binding drives centronuclear myopathy and represents a potential therapeutic target.. *JCI Insight*. PMID: 42100875
5. Integrated miRNA-proteomic profiling identifies chronic vesicle-trafficking and proteostasis disruptions after mild traumatic brain injury.. *Exp Neurol*. PMID: 41605412

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 39.9% |
| 置信残基 (pLDDT 70-90) 占比 | 35.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 17.1% |
| 有序区域 (pLDDT>70) 占比 | 75.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=77.6，有序区 75.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HCLS1 | 0.000 | 0.000 | — |
| CTTN | 0.000 | 0.000 | — |
| BIN1 | 0.000 | 0.000 | — |
| AMPH | 0.000 | 0.000 | — |
| DNM3 | 0.000 | 0.000 | — |
| DNM1 | 0.000 | 0.000 | — |
| WASL | 0.000 | 0.000 | — |
| ARC | 0.000 | 0.000 | — |
| CAV1 | 0.000 | 0.000 | — |
| SH3GL2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P50570 | psi-mi:"MI:2215"(barcode fusion genetics two hybri | pubmed:- |
| uniprotkb:P39054-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P39052 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13838 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q6FIF0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y262 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9UBV8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P23284 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P01106 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P62993 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 无 | pLDDT=77.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasmic vesicle, clat / Golgi apparatus, Cytosol | 一致 |
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
1. DNM2 — Dynamin-2，研究基础较多，新颖性有限。
2. 蛋白大小870 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 341 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50570
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079805-DNM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50570
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
