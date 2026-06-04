---
type: protein-evaluation
gene: "DYNLT2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYNLT2B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLT2B |
| 蛋白名称 | Dynein light chain Tctex-type protein 2B |
| 蛋白大小 | 142 aa / 16.1 kDa |
| UniProt ID | Q8WW35 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules, Primary cilium; 额外: Mitotic spindle, Basal bod; UniProt: Dynein axonemal particle |
| 蛋白大小 | 8/10 | ×1 | 8 | 142 aa / 16.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Primary cilium; 额外: Mitotic spindle, Basal body, Cytosol | Approved |
| UniProt | Dynein axonemal particle | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 8 |
| 别名(未计入scoring) |  |

**关键文献**:
1. TUB-like protein 2, a substrate of CCT8, is essential for the intraflagellar transport during spermiogenesis in mice†.. *Biol Reprod*. PMID: 40613306
2. Reanalysis of Whole-Exome Sequencing Data of an Infant with Suspected Diagnosis of Jeune Syndrome Revealed a Likely Pathogenic Variant in GRK2: A Newly Associated Gene for Jeune Syndrome Phenotype.. *Mol Syndromol*. PMID: 38585547

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 70.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 13.4% |
| 有序区域 (pLDDT>70) 占比 | 83.1% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.8，有序区 83.1%），结构可靠。

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
| uniprotkb:Q8WW35 | psi-mi:"MI:0034"(display technology) | pubmed:- |
| uniprotkb:Q8N961 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O60749 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5VST6-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WVS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96EX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96JQ2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UNH7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P55273 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P63172 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 无 | pLDDT=85.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Dynein axonemal particle / Microtubules, Primary cilium; 额外: Mitotic spindle, | 一致 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DYNLT2B — Dynein light chain Tctex-type protein 2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小142 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WW35
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213123-DYNLT2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLT2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WW35
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
