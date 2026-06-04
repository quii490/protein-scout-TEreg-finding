---
type: protein-evaluation
gene: "CLEC18B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLEC18B — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLEC18B |
| 蛋白名称 | C-type lectin domain family 18 member B |
| 蛋白大小 | 455 aa / 50.5 kDa |
| UniProt ID | Q6UXF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted; Endoplasmic reticulum; Golgi apparatus; Endosome |
| 蛋白大小 | 10/10 | x1 | 10 | 455 aa / 50.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 4 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Secreted; Endoplasmic reticulum; Golgi apparatus; Endosome | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) |  |

**关键文献**:
1. SP1-Mediated upregulation of CLEC18B promotes the proliferation and metastasis of glioma through regulation of the Wnt/β-Catenin/EMT Pathway.. *Transl Oncol*. PMID: 40885170
2. Decoding EGFR A289 Mutation in Glioblastoma: A Predictive Biomarker Framework and Targeted Therapeutic Insights.. *J Mol Neurosci*. PMID: 40650675
3. Gene Expression Profiling Regulated by lncRNA H19 Using Bioinformatic Analyses in Glioma Cell Lines.. *Cancer Genomics Proteomics*. PMID: 39467632
4. Identification of seven-gene signature for prediction of lung squamous cell carcinoma.. *Onco Targets Ther*. PMID: 31440059
5. Overexpression of CLEC18B Associates With the Proliferation, Migration, and Prognosis of Glioblastoma.. *ASN Neuro*. PMID: 29914265

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 36.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 75.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区 75.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GART | 0.000 | 0.000 | — |
| ARL14EPL | 0.000 | 0.000 | — |
| OR4F17 | 0.000 | 0.000 | — |
| OR4F5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 4，IntAct interactions: 0
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 无 | pLDDT=79.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted; Endoplasmic reticulum; Golgi apparatus;  / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 4 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLEC18B -- C-type lectin domain family 18 member B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小455 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UXF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140839-CLEC18B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLEC18B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
