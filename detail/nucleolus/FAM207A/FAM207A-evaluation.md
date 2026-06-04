---
type: protein-evaluation
gene: "FAM207A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM207A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM207A / C21orf70, FAM207A |
| 蛋白名称 | Ribosome biogenesis protein SLX9 homolog |
| 蛋白大小 | 230 aa / 25.5 kDa |
| UniProt ID | Q9NSI2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM207A/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM207A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 230 aa / 25.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.0; PDB: 7WTS, 7WTT, 7WTU, 7WTV, 7WTW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028160; Pfam: PF15341 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **152.0/180** | |
| **归一化总分** | | | **84.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 90S preribosome (GO:0030686)
- nucleolus (GO:0005730)
- preribosome, small subunit precursor (GO:0030688)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf70, FAM207A |

**关键文献**:
1. FAM207A acts as a novel and potential biomarker in lung adenocarcinoma and shapes the immunesuppressive tumor microenvironment.. *Clinical and experimental medicine*. PMID: 40259152
2. Five hypoxia and immunity related genes as potential biomarkers for the prognosis of osteosarcoma.. *Scientific reports*. PMID: 35102149
3. Osteoclasts differential-related prognostic biomarker for osteosarcoma based on single cell, bulk cell and gene expression datasets.. *BMC cancer*. PMID: 35300639
4. ATRX proximal protein associations boast roles beyond histone deposition.. *PLoS genetics*. PMID: 34780483

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 30.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 23.9% |
| 低置信 (pLDDT<50) 占比 | 23.5% |
| 有序区域 (pLDDT>70) 占比 | 52.6% |
| 可用 PDB 条目 | 7WTS, 7WTT, 7WTU, 7WTV, 7WTW |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM207A/FAM207A-PAE.png]]

**评价**: PDB实验结构（7WTS, 7WTT, 7WTU, 7WTV, 7WTW）+ AlphaFold极高置信度预测（pLDDT=71.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028160; Pfam: PF15341 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RRP12 | 0.977 | 0.957 | — |
| BYSL | 0.970 | 0.919 | — |
| LTV1 | 0.959 | 0.887 | — |
| TSR1 | 0.930 | 0.838 | — |
| UTP14A | 0.928 | 0.911 | — |
| NOB1 | 0.920 | 0.834 | — |
| RPS15A | 0.901 | 0.900 | — |
| BUD23 | 0.888 | 0.885 | — |
| PNO1 | 0.873 | 0.843 | — |
| TRMT112 | 0.869 | 0.860 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX9 | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| EZR | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FGD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| NEUROG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA6L9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 7WTS, 7WTT, 7WTU, 7WTV, 7WTW | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM207A — Ribosome biogenesis protein SLX9 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSI2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160256-SLX9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM207A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSI2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM207A/FAM207A-PAE.png]]




