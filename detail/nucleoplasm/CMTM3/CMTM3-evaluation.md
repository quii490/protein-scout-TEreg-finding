---
type: protein-evaluation
gene: "CMTM3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CMTM3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMTM3 |
| 蛋白名称 | CKLF-like MARVEL transmembrane domain-containing protein 3 |
| 蛋白大小 | 182 aa / 19.7 kDa |
| UniProt ID | Q96MX0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 182 aa / 19.7 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 23 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 68 |
| 别名(未计入scoring) |  |

**关键文献**:
1. MiR-218-5p inhibits glioma progression by targeting CKLF-like MARVEL transmembrane domain-containing 3.. *BMC Cancer*. PMID: 41527058
2. The Bioinformatics Analysis of Publicly Available Datasets and Validation in a Mouse Model of Myocardial Infarction Through Coronary Artery Ligation.. *J Inflamm Res*. PMID: 41847429
3. CMTM3 promotes adipocyte differentiation by regulating PPARγ in 3T3-L1 cells.. *Genes Dis*. PMID: 40697995
4. HECTD3 E3 ligase mediates ubiquitination of AKT-phosphorylated CMTM3 in HER2-overexpressed breast cancer cells.. *Carcinogenesis*. PMID: 40836897
5. Differences in the expression of CMTM3 and SSTR2 genes in right and left colon tumors: A molecular insight into colorectal cancer.. *Med Oncol*. PMID: 40720052

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 44.5% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 26.9% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 68.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.8，有序区 68.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CMTM1 | 0.000 | 0.000 | — |
| CMTM2 | 0.000 | 0.000 | — |
| CKLF | 0.000 | 0.000 | — |
| CMTM4 | 0.000 | 0.000 | — |
| CMTM7 | 0.000 | 0.000 | — |
| CMTM8 | 0.000 | 0.000 | — |
| CMTM6 | 0.000 | 0.000 | — |
| SF3B3 | 0.000 | 0.000 | — |
| KYNU | 0.000 | 0.000 | — |
| MOB3C | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q6IN84 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96AG4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9GZR5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96MX0 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P08034 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:A8MZ59 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H6H4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9H169-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q70UQ0-4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5SR56 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 23，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 23 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 无 | pLDDT=79.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 23 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CMTM3 -- CKLF-like MARVEL transmembrane domain-containing protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小182 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MX0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140931-CMTM3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMTM3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MX0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
