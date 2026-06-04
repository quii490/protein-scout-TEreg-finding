---
type: protein-evaluation
gene: "COMMD9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD9 |
| 蛋白名称 | COMM domain-containing protein 9 |
| 蛋白大小 | 198 aa / 21.8 kDa |
| UniProt ID | Q9P000 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: Nucleus; Cytoplasmic vesicle |
| 蛋白大小 | 8/10 | ×1 | 8 | 198 aa / 21.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.8; PDB: 4NKN, 4OE9, 6BP6, 8ESD, 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017920, IPR037360, IPR048676; Pfam: PF07258, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- secretory granule lumen (GO:0034774)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Prognostic features of bladder cancer based on five neddylation-related genes.. *American journal of clinical and experimental urology*. PMID: 39584004
2. Functional interaction of COMMD3 and COMMD9 with the epithelial sodium channel.. *American journal of physiology. Renal physiology*. PMID: 23637203
3. COMMD9 promotes TFDP1/E2F1 transcriptional activity via interaction with TFDP1 in non-small cell lung cancer.. *Cellular signalling*. PMID: 27871936
4. Whole-exome sequencing and burden analysis identify six novel candidate risk genes and expand the genetic landscape of Parkinson's disease.. *NPJ Parkinson's disease*. PMID: 41339365
5. Regulation of murine copper homeostasis by members of the COMMD protein family.. *Disease models & mechanisms*. PMID: 33262129

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 35.9% |
| 置信残基 (pLDDT 70-90) 占比 | 52.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 4NKN, 4OE9, 6BP6, 8ESD, 8F2R, 8F2U, 8P0W |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4NKN, 4OE9, 6BP6, 8ESD, 8F2R, 8F2U, 8P0W）+ AlphaFold极高置信度预测（pLDDT=84.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037360, IPR048676; Pfam: PF07258, PF20923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD6 | 0.999 | 0.994 | — |
| COMMD1 | 0.977 | 0.828 | — |
| COMMD10 | 0.976 | 0.816 | — |
| COMMD4 | 0.976 | 0.837 | — |
| COMMD2 | 0.974 | 0.830 | — |
| CCDC22 | 0.973 | 0.846 | — |
| COMMD3 | 0.971 | 0.864 | — |
| CCDC93 | 0.964 | 0.781 | — |
| COMMD8 | 0.955 | 0.751 | — |
| COMMD5 | 0.950 | 0.623 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ARHGEF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| DCDC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COMMD6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COMMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DENND10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 4NKN, 4OE9, 6BP6, 8ESD, 8F2R,  | pLDDT=84.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasmic vesicle / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
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
1. COMMD9 — COMM domain-containing protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P000
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110442-COMMD9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P000
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
