---
type: protein-evaluation
gene: "EPHA10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EPHA10 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPHA10 |
| 蛋白名称 | Ephrin type-A receptor 10 |
| 蛋白大小 | 1008 aa / 109.7 kDa |
| UniProt ID | Q5JZY3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell membrane; Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 1008 aa / 109.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027936, IPR001090, IPR050449, IPR003961, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell membrane; Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- dendrite (GO:0030425)
- extracellular region (GO:0005576)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Eph receptor A10 has a potential as a target for a prostate cancer therapy.. *Biochemical and biophysical research communications*. PMID: 24924629
2. Characterization of a novel Eph receptor tyrosine kinase, EphA10, expressed in testis.. *Biochimica et biophysica acta*. PMID: 15777695
3. Isoform expression patterns of EPHA10 protein mediate breast cancer progression by regulating the E-Cadherin and β-catenin complex.. *Oncotarget*. PMID: 28427223
4. A new serological autoantibody signature associated with multiple sclerosis.. *Neurobiology of disease*. PMID: 41038542
5. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 39.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 78.0% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.2，有序区 78.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027936, IPR001090, IPR050449, IPR003961, IPR036116; Pfam: PF14575, PF25599, PF01404 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EFNA1 | 0.996 | 0.098 | — |
| EFNA4 | 0.985 | 0.098 | — |
| EFNA3 | 0.981 | 0.098 | — |
| EFNB1 | 0.967 | 0.241 | — |
| EFNA5 | 0.962 | 0.098 | — |
| EFNA2 | 0.962 | 0.098 | — |
| EFNB2 | 0.954 | 0.241 | — |
| EFNB3 | 0.912 | 0.241 | — |
| EPHA7 | 0.857 | 0.330 | — |
| EPHB6 | 0.710 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPHA7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFCP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CAMK2D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| BANP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| ERO1B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| ZNF326 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| CCDC86 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| CRELD2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 无 | pLDDT=79.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell membrane; Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EPHA10 — Ephrin type-A receptor 10，非常新颖，仅有少数基础研究。
2. 蛋白大小1008 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JZY3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183317-EPHA10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPHA10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JZY3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
