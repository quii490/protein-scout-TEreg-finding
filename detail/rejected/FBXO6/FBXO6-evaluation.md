---
type: protein-evaluation
gene: "FBXO6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO6 / FBG2, FBS2, FBX6 |
| 蛋白名称 | F-box only protein 6 |
| 蛋白大小 | 293 aa / 33.9 kDa |
| UniProt ID | Q9NRD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 293 aa / 33.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

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
- endoplasmic reticulum quality control compartment (GO:0044322)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBG2, FBS2, FBX6 |

**关键文献**:
1. Sugar-mediated non-canonical ubiquitination impairs Nrf1/NFE2L1 activation.. *Molecular cell*. PMID: 39116872
2. FBXO6-mediated RNASET2 ubiquitination and degradation governs the development of ovarian cancer.. *Cell death & disease*. PMID: 33767133
3. FBXO6 regulates colon cancer migration and invasion via ITGB1 ubiquitination and downstream signaling.. *Cell death & disease*. PMID: 41857001
4. FBXO6 regulates the antiviral immune responses via mediating alveolar macrophages survival.. *Journal of medical virology*. PMID: 36217277
5. The USP18-FBXO6 axis maintains the malignancy of ovarian cancer.. *Biochemical and biophysical research communications*. PMID: 35063764

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.1 |
| 高置信度残基 (pLDDT>90) 占比 | 80.9% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.1，有序区 86.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008979; Pfam: PF12937, PF04300 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.993 | 0.911 | — |
| CUL1 | 0.987 | 0.877 | — |
| FBXO2 | 0.962 | 0.000 | — |
| RBX1 | 0.852 | 0.678 | — |
| BTRC | 0.842 | 0.000 | — |
| CHEK1 | 0.725 | 0.292 | — |
| CAND1 | 0.699 | 0.000 | — |
| MAD2L2 | 0.693 | 0.000 | — |
| CCNF | 0.677 | 0.000 | — |
| PRKN | 0.670 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SkpB | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Dmel\CG6569 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fbxo42 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| GABPI | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ccdc85 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CG6911 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ORC4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.1 + PDB: 无 | pLDDT=88.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
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
1. FBXO6 — F-box only protein 6，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小293 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116663-FBXO6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
