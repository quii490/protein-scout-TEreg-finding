---
type: protein-evaluation
gene: "EIF2B1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF2B1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2B1 |
| 蛋白名称 | Translation initiation factor eIF2B subunit alpha |
| 蛋白大小 | 305 aa / 33.7 kDa |
| UniProt ID | Q14232 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 305 aa / 33.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=74 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 74 |
| PubMed broad count | 591 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic screening of EIF2B genes reveals mutation spectrum and predicted prevalence of vanishing white matter disease in Chinese population.. *Clin Chim Acta*. PMID: 41791694
2. Adult-onset vanishing white matter disease caused by the EIF2B5 c.185A>T (p.Asp62Val) variant.. *Front Genet*. PMID: 41700296
3. Consensus-Based Expert Recommendations for Diagnosis and Clinical Management of Vanishing White Matter.. *Neurology*. PMID: 41232062
4. "Case report": Whole-exome sequencing reveals compound heterozygous variants in the EIF2B5 gene in a familial case of vanishing white matter.. *Front Genet*. PMID: 41244982
5. Bioinformatic analysis of brucellosis and construction of a diagnostic model based on key genes.. *Sci Rep*. PMID: 41053229

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2B3 | 0.000 | 0.000 | — |
| EIF2B4 | 0.000 | 0.000 | — |
| EIF2B5 | 0.000 | 0.000 | — |
| EIF2B2 | 0.000 | 0.000 | — |
| EIF2S3 | 0.000 | 0.000 | — |
| EIF2S2 | 0.000 | 0.000 | — |
| EIF2S1 | 0.000 | 0.000 | — |
| EIF2S3B | 0.000 | 0.000 | — |
| EIF2AK4 | 0.000 | 0.000 | — |
| TYMP | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q14232 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q01338 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P30545 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q01337 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P18762 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P07550 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| intact:EBI-1059069 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P52565 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P14866 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9NR50 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol | 一致 |
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
1. EIF2B1 — Translation initiation factor eIF2B subunit alpha，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小305 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 74 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14232
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111361-EIF2B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14232
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
