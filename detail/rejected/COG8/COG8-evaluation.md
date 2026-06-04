---
type: protein-evaluation
gene: "COG8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COG8 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG8 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 8 |
| 蛋白大小 | 639 aa / 71.2 kDa |
| UniProt ID | B4DYU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 639 aa / 71.2 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=75.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 46 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Transcriptomic Signatures of the Foetal Liver and Late Prenatal Development in Vitrified Rabbit Embryos.. *Vet Sci*. PMID: 39195801
2. Alcohol drinking, DNA methylation and psychiatric disorders: A multi-omics Mendelian randomization study to investigate causal pathways.. *Addiction*. PMID: 38523595
3. A Rare Case of Cerebrotendinous Xanthomatosis Associated With a Mutation on COG8 Gene.. *J Investig Med High Impact Case Rep*. PMID: 37083278
4. Identification of Biomarkers Associated With CD4(+) T-Cell Infiltration With Gene Coexpression Network in Dermatomyositis.. *Front Immunol*. PMID: 35711463
5. Where all the Roads Meet? A Crossover Perspective on Host Factors Regulating SARS-CoV-2 infection.. *J Mol Biol*. PMID: 34914966

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 42.3% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 70.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.0，有序区 70.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG4 | 0.000 | 0.000 | — |
| COG2 | 0.000 | 0.000 | — |
| COG5 | 0.000 | 0.000 | — |
| COG6 | 0.000 | 0.000 | — |
| COG3 | 0.000 | 0.000 | — |
| COG1 | 0.000 | 0.000 | — |
| COG7 | 0.000 | 0.000 | — |
| STX16 | 0.000 | 0.000 | — |
| STX5 | 0.000 | 0.000 | — |
| RIC1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P49657 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VKH0 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96MW5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9VGC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q5NFN3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P42742 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q6NMI3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:C0SVM5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q84K25 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8LGS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 无 | pLDDT=75.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus | 一致 |
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
1. COG8 -- Conserved oligomeric Golgi complex subunit 8，非常新颖，仅有少数基础研究。
2. 蛋白大小639 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B4DYU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213380-COG8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B4DYU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
