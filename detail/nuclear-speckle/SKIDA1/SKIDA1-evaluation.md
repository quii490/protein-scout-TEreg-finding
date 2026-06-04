---
type: protein-evaluation
gene: "SKIDA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKIDA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKIDA1 / C10orf140, DLN1 |
| 蛋白名称 | SKI/DACH domain-containing protein 1 |
| 蛋白大小 | 908 aa / 98.1 kDa |
| UniProt ID | Q1XH10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 908 aa / 98.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009061, IPR052119, IPR027971, IPR003380, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf140, DLN1 |

**关键文献**:
1. Novel Diagnostic and Therapeutic Options for KMT2A-Rearranged Acute Leukemias.. *Frontiers in pharmacology*. PMID: 35734412
2. SKIDA1 sustains MLL::ENL-expressing hematopoietic progenitors during neonatal stages and promotes B-lineage priming.. *Blood neoplasia*. PMID: 41574310
3. A characteristic gene expression profile regulated by ACIN1::NUTM1 fusion in a newly identified infant leukaemic cell line and an ACIN1::NUTM1-inducible model.. *British journal of haematology*. PMID: 40884014
4. Transcriptional Changes in Regulatory T Cells From Patients With Autoimmune Polyendocrine Syndrome Type 1 Suggest Functional Impairment of Lipid Metabolism and Gut Homing.. *Frontiers in immunology*. PMID: 34526996
5. Regulatory Potential of piRNAs Targeting Klotho and Other Genes.. *Genes*. PMID: 41751625

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.8% |
| 低置信 (pLDDT<50) 占比 | 72.4% |
| 有序区域 (pLDDT>70) 占比 | 12.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.4），有序残基占 12.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009061, IPR052119, IPR027971, IPR003380, IPR037000; Pfam: PF15223, PF02437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTF2 | 0.764 | 0.614 | — |
| PHF19 | 0.735 | 0.612 | — |
| EZH2 | 0.700 | 0.620 | — |
| SUZ12 | 0.698 | 0.623 | — |
| EED | 0.655 | 0.610 | — |
| MYSM1 | 0.588 | 0.507 | — |
| SMARCB1 | 0.541 | 0.465 | — |
| PBRM1 | 0.511 | 0.458 | — |
| FSTL3 | 0.489 | 0.000 | — |
| CEP44 | 0.483 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SUZ12 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| EZH1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| THAP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EED | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF445 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EZH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PHF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AGAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MTF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.4 + PDB: 无 | pLDDT=49.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies; 额外: Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SKIDA1 — SKI/DACH domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小908 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q1XH10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180592-SKIDA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKIDA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q1XH10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
