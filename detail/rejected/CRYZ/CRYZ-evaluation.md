---
type: protein-evaluation
gene: "CRYZ"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRYZ — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYZ |
| 蛋白名称 | Zeta-crystallin |
| 蛋白大小 | 329 aa / 35.2 kDa |
| UniProt ID | Q08257 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | x1 | 10 | 329 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=96.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 29 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 198 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Comprehensive integrative analysis of Exosome-associated genes in major depressive disorder: Diagnostic biomarker discovery, immune modulation, and therapeutic implications.. *J Psychiatr Res*. PMID: 42061206
2. Multiomics analyses of human colorectal cancer reveal changes in mitochondrial metabolism associated with chemotherapy resistance.. *Front Oncol*. PMID: 41293266
3. Involvement of dysregulated RNA binding protein and alternative splicing regulatory networks in diabetic nephropathy from type 2 albuminuric cohorts.. *BMC Nephrol*. PMID: 40597902
4. Targeting z-Crystallin by aspirin restores the sensitivity to cisplatin in resistant A2780 ovarian cancer cells.. *Front Pharmacol*. PMID: 39021835
5. Tumor stromal nicotinamide N-methyltransferase overexpression as a prognostic biomarker for poor clinical outcome in early-stage colorectal cancer.. *Sci Rep*. PMID: 35177765

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.9 |
| 高置信度残基 (pLDDT>90) 占比 | 97.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 99.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.9，有序区 99.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NQO1 | 0.000 | 0.000 | — |
| HMOX1 | 0.000 | 0.000 | — |
| NFE2L2 | 0.000 | 0.000 | — |
| KEAP1 | 0.000 | 0.000 | — |
| GCLM | 0.000 | 0.000 | — |
| GCLC | 0.000 | 0.000 | — |
| GPX2 | 0.000 | 0.000 | — |
| GPX8 | 0.000 | 0.000 | — |
| GPX7 | 0.000 | 0.000 | — |
| GPX5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q08257 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P47199 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P22033 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15645 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q4J6C6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H4K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-54262888 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 29
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 29 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.9 + PDB: 无 | pLDDT=96.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 29 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRYZ -- Zeta-crystallin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小329 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08257
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116791-CRYZ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYZ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08257
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08257-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
