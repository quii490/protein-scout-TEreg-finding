---
type: protein-evaluation
gene: "CPSF3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPSF3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPSF3L / INTS11 |
| 蛋白名称 | Integrator complex subunit 11 |
| 蛋白大小 | 600 aa / 67.7 kDa |
| UniProt ID | Q5TA45 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 600 aa / 67.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=90.7; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic and embryonic transcriptome analyses reveal the molecular and developmental basis of Mayer-Rokitansky-Küster-Hauser syndrome.. *J Med Genet*. PMID: 41233206
2. Bi-allelic variants in INTS11 are associated with a complex neurological disorder.. *Am J Hum Genet*. PMID: 37054711
3. Quantitative proteomic analysis of GnRH agonist treated GBM cell line LN229 revealed regulatory proteins inhibiting cancer cell proliferation.. *BMC Cancer*. PMID: 35109816
4. The Search for Molecular Markers in a Gene-Orphan Case Study of a Pediatric Spinal Cord Pilocytic Astrocytoma.. *Cancer Genomics Proteomics*. PMID: 32108034

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 66.5% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 0.2% |
| 有序区域 (pLDDT>70) 占比 | 96.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.7，有序区 96.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INTS5 | 0.000 | 0.000 | — |
| INTS1 | 0.000 | 0.000 | — |
| INTS4 | 0.000 | 0.000 | — |
| INTS9 | 0.000 | 0.000 | — |
| INTS6 | 0.000 | 0.000 | — |
| INTS3 | 0.000 | 0.000 | — |
| INTS7 | 0.000 | 0.000 | — |
| INTS2 | 0.000 | 0.000 | — |
| INTS10 | 0.000 | 0.000 | — |
| INTS8 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q5TA45 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9UL01 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5TA45-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WU58 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q99932-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q92734 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8N5J4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9ULV5-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 无 | pLDDT=90.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CPSF3L -- Integrator complex subunit 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小600 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TA45
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127054-CPSF3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPSF3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TA45
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
