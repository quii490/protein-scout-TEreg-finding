---
type: protein-evaluation
gene: "ERI3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERI3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERI3 / PINT1, PRNPIP, PRNPIP1 |
| 蛋白名称 | ERI1 exoribonuclease 3 |
| 蛋白大小 | 337 aa / 37.2 kDa |
| UniProt ID | O43414 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI3/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI3/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 337 aa / 37.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.8; PDB: 2XRI, 7K05, 7K06, 7K07, 7LPY, 7LPZ, 7LQ0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051274, IPR047201, IPR013520, IPR012337, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PINT1, PRNPIP, PRNPIP1 |

**关键文献**:
1. Identification of ribosome biogenesis genes and subgroups in ischaemic stroke.. *Frontiers in immunology*. PMID: 39290696
2. Analysis of LINE-1 Elements in DNA from Postmortem Brains of Individuals with Schizophrenia.. *Neuropsychopharmacology : official publication of the American College of Neuropsychopharmacology*. PMID: 28585566
3. [ERI3 expression is elevated in hepatocellular carcinoma and correlates with poor patient prognosis].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 41540704
4. Regulation of cyclic adenosine 3',5'- monophosphate signaling and pulsatile neurosecretion by Gi-coupled plasma membrane estrogen receptors in immortalized gonadotrophin-releasing hormone neurons.. *Molecular endocrinology (Baltimore, Md.)*. PMID: 14680004
5. Identification of Caenorhabditis elegans genes regulating longevity using enhanced RNAi-sensitive strains.. *Cold Spring Harbor symposia on quantitative biology*. PMID: 18419309

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 59.1% |
| 置信残基 (pLDDT 70-90) 占比 | 0.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 38.6% |
| 有序区域 (pLDDT>70) 占比 | 60.0% |
| 可用 PDB 条目 | 2XRI, 7K05, 7K06, 7K07, 7LPY, 7LPZ, 7LQ0 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI3/ERI3-PAE.png]]

**评价**: PDB实验结构（2XRI, 7K05, 7K06, 7K07, 7LPY, 7LPZ, 7LQ0）+ AlphaFold极高置信度预测（pLDDT=73.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051274, IPR047201, IPR013520, IPR012337, IPR036397; Pfam: PF00929 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRNP | 0.786 | 0.132 | — |
| SYN3 | 0.704 | 0.000 | — |
| GRB2 | 0.703 | 0.000 | — |
| SYN2 | 0.672 | 0.000 | — |
| DUS3L | 0.626 | 0.000 | — |
| SYN1 | 0.580 | 0.000 | — |
| ERI1 | 0.568 | 0.000 | — |
| RNF220 | 0.545 | 0.000 | — |
| TRAPPC1 | 0.534 | 0.000 | — |
| TMEM53 | 0.534 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| menB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7R9Q0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TFAP2A | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| PSMD9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNJ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CELF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| nleF | psi-mi:"MI:0018"(two hybrid) | pubmed:25519916|imex:IM-23549 |
| RAPGEF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Stmn1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cenpf | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 2XRI, 7K05, 7K06, 7K07, 7LPY,  | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ERI3 — ERI1 exoribonuclease 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小337 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43414
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117419-ERI3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43414
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI3/ERI3-PAE.png]]




