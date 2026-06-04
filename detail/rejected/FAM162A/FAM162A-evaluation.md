---
type: protein-evaluation
gene: "FAM162A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM162A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM162A / C3orf28, E2IG5 |
| 蛋白名称 | Protein FAM162A |
| 蛋白大小 | 154 aa / 17.3 kDa |
| UniProt ID | Q96A26 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 154 aa / 17.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009432; Pfam: PF06388 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.5/180** | |
| **归一化总分** | | | **58.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf28, E2IG5 |

**关键文献**:
1. Identification and verification of a polyamine metabolism-related gene signature for predicting prognosis and immune infiltration in osteosarcoma.. *Journal of orthopaedic surgery and research*. PMID: 40383808
2. Identification and validation of potential hypoxia-related genes associated with coronary artery disease.. *Frontiers in physiology*. PMID: 37637145
3. Identification of biomarkers associated with mitochondrial dysfunction and programmed cell death in chronic obstructive pulmonary disease via transcriptomics.. *Frontiers in genetics*. PMID: 40612794
4. A novel hypoxia- and lactate metabolism-related prognostic signature to characterize the immune landscape and predict immunotherapy response in osteosarcoma.. *Frontiers in immunology*. PMID: 39569192
5. Integrative Molecular Dynamics Simulations Untangle Cross-Linking Data to Unveil Mitochondrial Protein Distributions.. *Angewandte Chemie (International ed. in English)*. PMID: 39644219

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.4 |
| 高置信度残基 (pLDDT>90) 占比 | 7.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 54.5% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 31.8% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.4），有序残基占 31.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009432; Pfam: PF06388 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| Cbl | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |
| NDUFA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| NMES1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| RAB5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| STAP2 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| KSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| GHITM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.4 + PDB: 无 | pLDDT=64.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM162A — Protein FAM162A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114023-FAM162A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM162A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
