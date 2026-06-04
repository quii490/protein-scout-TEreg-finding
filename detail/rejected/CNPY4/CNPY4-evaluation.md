---
type: protein-evaluation
gene: "CNPY4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNPY4 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNPY4 |
| 蛋白名称 | Protein canopy homolog 4 |
| 蛋白大小 | 248 aa / 28.3 kDa |
| UniProt ID | Q8N129 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Secreted |
| 蛋白大小 | 10/10 | x1 | 10 | 248 aa / 28.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 13 partners; IntAct 29 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Secreted | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Secretory kinase FAM20C triggers adipocyte dysfunction, inciting insulin resistance and inflammation in obesity.. *J Clin Invest*. PMID: 41148235
2. CNPY4 is a Lipid-Binding Regulator of Sphingolipid Homeostasis.. *bioRxiv*. PMID: 41279395
3. Biomarker Discovery for Metabolic Dysfunction-associated Steatotic Liver Disease Utilizing Mendelian Randomization, Machine Learning, and External Validation.. *J Clin Transl Hepatol*. PMID: 40951528
4. The role of canopy family proteins: biological mechanism and disease function.. *Mol Biol Rep*. PMID: 39869231
5. Progress in Research on CNPY2 in Diseases.. *Mini Rev Med Chem*. PMID: 37259932

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 49.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 12.5% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.8，有序区 69.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LY96 | 0.000 | 0.000 | — |
| TLR4 | 0.000 | 0.000 | — |
| CNPY2 | 0.000 | 0.000 | — |
| CHAD | 0.000 | 0.000 | — |
| CNPY1 | 0.000 | 0.000 | — |
| GML | 0.000 | 0.000 | — |
| HSP90B1 | 0.000 | 0.000 | — |
| TLR2 | 0.000 | 0.000 | — |
| LRIG3 | 0.000 | 0.000 | — |
| ERGIC3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N129 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BRQ8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 29
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 29 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 无 | pLDDT=79.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Vesicles | 一致 |
| PPI | STRING + IntAct | 13 + 29 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNPY4 -- Protein canopy homolog 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N129
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166997-CNPY4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNPY4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N129
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
