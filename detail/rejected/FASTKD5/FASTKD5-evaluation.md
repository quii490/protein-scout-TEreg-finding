---
type: protein-evaluation
gene: "FASTKD5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FASTKD5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FASTKD5 / KIAA1792 |
| 蛋白名称 | FAST kinase domain-containing protein 5, mitochondrial |
| 蛋白大小 | 764 aa / 86.6 kDa |
| UniProt ID | Q7L8L6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion matrix, mitochondrion nucleoid |
| 蛋白大小 | 10/10 | ×1 | 10 | 764 aa / 86.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion matrix, mitochondrion nucleoid | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrial nucleoid (GO:0042645)
- mitochondrion (GO:0005739)
- ribonucleoprotein granule (GO:0035770)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1792 |

**关键文献**:
1. A kinetic dichotomy between mitochondrial and nuclear gene expression processes.. *Molecular cell*. PMID: 38503286
2. The FASTK family proteins fine-tune mitochondrial RNA processing.. *PLoS genetics*. PMID: 34748562
3. Systematic Analysis of FASTK Gene Family Alterations in Cancer.. *International journal of molecular sciences*. PMID: 34768773
4. Bi-allelic mutations in FASTKD5 are associated with cytochrome c oxidase deficiency and early- to late-onset Leigh syndrome.. *American journal of human genetics*. PMID: 40499538
5. FASTKD5 processes mitochondrial pre-mRNAs at noncanonical cleavage sites.. *Nucleic acids research*. PMID: 40637235

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 73.1% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.3，有序区 73.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam: PF06743, PF08368, PF08373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NLRX1 | 0.825 | 0.195 | — |
| FASTKD2 | 0.753 | 0.088 | — |
| GRSF1 | 0.748 | 0.253 | — |
| TBRG4 | 0.673 | 0.088 | — |
| FASTK | 0.647 | 0.000 | — |
| TRMT10C | 0.589 | 0.088 | — |
| SUPV3L1 | 0.565 | 0.095 | — |
| ELAC2 | 0.538 | 0.088 | — |
| DDX28 | 0.533 | 0.000 | — |
| MTPAP | 0.501 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NLRX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| Unc93b1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| MAPK4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| MAPK6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| BCL2L14 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| SCRIB | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 无 | pLDDT=78.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion matrix, mitochondrion nucleoid / 暂无HPA定位数据 | 一致 |
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
1. FASTKD5 — FAST kinase domain-containing protein 5, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小764 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L8L6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000215251-FASTKD5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FASTKD5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L8L6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L8L6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
