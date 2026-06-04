---
type: protein-evaluation
gene: "GLT1D1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLT1D1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLT1D1 |
| 蛋白名称 | Glycosyltransferase 1 domain-containing protein 1 |
| 蛋白大小 | 346 aa / 38.5 kDa |
| UniProt ID | Q96MS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 346 aa / 38.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001296, IPR052622; Pfam: PF00534 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Customized Chromosomal Microarrays for Neurodevelopmental Disorders.. *Genes*. PMID: 40869915
2. Genetic susceptibility to patient-reported xerostomia among long-term oropharyngeal cancer survivors.. *Scientific reports*. PMID: 35459784
3. Promoting keratinocyte psoriasiform changes and IL-17RE expression: Potential role of GLT1D1 in linear psoriasis.. *Molecular immunology*. PMID: 42090972
4. Squalene through Its Post-Squalene Metabolites Is a Modulator of Hepatic Transcriptome in Rabbits.. *International journal of molecular sciences*. PMID: 35456988
5. Genetic Association Analysis of Fasting and 1- and 2-Hour Glucose Tolerance Test Data Using a Generalized Index of Dissimilarity Measure for the Korean Population.. *Genomics & informatics*. PMID: 28154509

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.7 |
| 高置信度残基 (pLDDT>90) 占比 | 94.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.7，有序区 98.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001296, IPR052622; Pfam: PF00534 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM132D | 0.469 | 0.000 | — |
| PRORP | 0.453 | 0.000 | — |
| SLC15A4 | 0.450 | 0.000 | — |
| MEGF11 | 0.428 | 0.000 | — |
| LRMDA | 0.420 | 0.000 | — |
| FAM153B | 0.418 | 0.000 | — |
| TMEM132C | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASAH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RUFY3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 4
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.7 + PDB: 无 | pLDDT=95.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Cytosol | 一致 |
| PPI | STRING + IntAct | 7 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLT1D1 — Glycosyltransferase 1 domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小346 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151948-GLT1D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLT1D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
