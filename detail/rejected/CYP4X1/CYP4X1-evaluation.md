---
type: protein-evaluation
gene: "CYP4X1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP4X1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP4X1 |
| 蛋白名称 | Cytochrome P450 4X1 |
| 蛋白大小 | 509 aa / 58.9 kDa |
| UniProt ID | Q8N118 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 509 aa / 58.9 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.5/180** | |
| **归一化总分** | | | **55.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 40 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CYP4X1/sEH-Dependent Endocannabinoid Metabolism Drives Fibroblast-Mediated Immunosuppression to Limit Immunotherapy in Colon Cancer.. *Adv Sci (Weinh)*. PMID: 41276938
2. Investigating the role of oncogenic FAM83A as a prognostic biomarker in lung adenocarcinoma: Insights from smoker and non-smoker cohorts.. *J Genet Eng Biotechnol*. PMID: 41386847
3. Combination therapy with nisin, urolithin B, and vincristine exhibits synergistic antiproliferative and pro-apoptotic effects against human lymphoma cells: evidence from proteomics.. *Front Immunol*. PMID: 41063976
4. Orphan Cytochromes P450 as Possible Pharmacological Targets or Biomarkers in Breast Cancer.. *Curr Issues Mol Biol*. PMID: 41020804
5. CYP4X1 Expression Is Associated with Metastasis and Poor Prognosis in Patients with Colorectal Cancer.. *Int J Mol Sci*. PMID: 40076494

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 93.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q13136-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q13136 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 无 | pLDDT=89.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYP4X1 -- Cytochrome P450 4X1，非常新颖，仅有少数基础研究。
2. 蛋白大小509 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N118
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186377-CYP4X1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP4X1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N118
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
