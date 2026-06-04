---
type: protein-evaluation
gene: "CDKN2AIPNL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDKN2AIPNL — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDKN2AIPNL |
| 蛋白名称 | CDKN2AIP N-terminal-like protein |
| 蛋白大小 | 116 aa / 13.2 kDa |
| UniProt ID | Q96HQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 116 aa / 13.2 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.5; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 28 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CDKN2AIPNL: a potential pan-cancer biomarker.. *Front Genet*. PMID: 41640880
2. Extreme temperatures modulate gene expression in the airway epithelium of the lungs in mice and asthma patients.. *Front Med (Lausanne)*. PMID: 40313552
3. Weighted correlation network analysis revealed novel long non-coding RNAs for colorectal cancer.. *Sci Rep*. PMID: 35194111
4. Functional characterization of Copy Number Variations regions in Djallonké sheep.. *J Anim Breed Genet*. PMID: 33682236
5. Full-length NF-κB repressing factor contains an XRN2 binding domain.. *Biochem J*. PMID: 32011671

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 67.2% |
| 置信残基 (pLDDT 70-90) 占比 | 30.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 97.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDKN2AIPNL/CDKN2AIPNL-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=90.5，有序区 97.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRN2 | 0.000 | 0.000 | — |
| EID2B | 0.000 | 0.000 | — |
| ARL16 | 0.000 | 0.000 | — |
| EPB41L5 | 0.000 | 0.000 | — |
| MIGA1 | 0.000 | 0.000 | — |
| IQCF6 | 0.000 | 0.000 | — |
| METTL21A | 0.000 | 0.000 | — |
| DTWD2 | 0.000 | 0.000 | — |
| MFSD5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96HQ2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O95994 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q16514 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96JM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BTA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9HCH0-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96JA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O15027-5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NYF8-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6PGN9-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 28
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 28 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 无 | pLDDT=90.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 9 + 28 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CDKN2AIPNL — CDKN2AIP N-terminal-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小116 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000237190-CDKN2AIPNL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDKN2AIPNL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CDKN2AIPNL/CDKN2AIPNL-PAE.png]]
