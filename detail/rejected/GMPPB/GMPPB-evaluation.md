---
type: protein-evaluation
gene: "GMPPB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GMPPB — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GMPPB |
| 蛋白名称 | Mannose-1-phosphate guanylyltransferase catalytic subunit beta |
| 蛋白大小 | 360 aa / 39.8 kDa |
| UniProt ID | Q9Y5P6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 39.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=96.3; PDB: 7D72, 7D73, 7D74 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR056729, IPR045233, IPR018357, IPR050486, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- GDP-mannose pyrophosphorylase complex (GO:0120508)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Congenital Myasthenic Syndromes Overview.. **. PMID: 20301347
2. Clinical and genetic characterisation of a large Indian congenital myasthenic syndrome cohort.. *Brain : a journal of neurology*. PMID: 37721175
3. Neurogenetic fetal akinesia and arthrogryposis: genetics, expanding genotype-phenotypes and functional genomics.. *Journal of medical genetics*. PMID: 33060286
4. Integrative multi-omics analysis reveal novel therapeutic targets for glioblastoma.. *International journal of surgery (London, England)*. PMID: 40638267
5. Genetic variations and clinical spectrum of dystroglycanopathy in a large cohort of Chinese patients.. *Clinical genetics*. PMID: 33200426

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.3 |
| 高置信度残基 (pLDDT>90) 占比 | 95.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 7D72, 7D73, 7D74 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7D72, 7D73, 7D74）+ AlphaFold高质量预测（pLDDT=96.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056729, IPR045233, IPR018357, IPR050486, IPR005835; Pfam: PF25087, PF00483 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GMPPA | 0.999 | 0.997 | — |
| PMM2 | 0.945 | 0.000 | — |
| PMM1 | 0.924 | 0.000 | — |
| GMDS | 0.892 | 0.000 | — |
| POMT2 | 0.854 | 0.139 | — |
| TGDS | 0.845 | 0.000 | — |
| POMT1 | 0.825 | 0.139 | — |
| FKRP | 0.824 | 0.000 | — |
| POMGNT2 | 0.818 | 0.000 | — |
| RXYLT1 | 0.812 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ikbkb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| GMPPA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| heph | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| GOLPH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| TXNDC5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GLYCTK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DPPA4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POLR1C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.3 + PDB: 7D72, 7D73, 7D74 | pLDDT=96.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GMPPB — Mannose-1-phosphate guanylyltransferase catalytic subunit beta，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5P6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173540-GMPPB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GMPPB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5P6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
