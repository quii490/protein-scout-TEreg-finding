---
type: protein-evaluation
gene: "ERP44"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERP44 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=115，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERP44 / KIAA0573, TXNDC4 |
| 蛋白名称 | Endoplasmic reticulum resident protein 44 |
| 蛋白大小 | 406 aa / 47.0 kDa |
| UniProt ID | Q9BS26 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 406 aa / 47.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=115 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.9; PDB: 2R2J, 5GU6, 5GU7, 5HQP, 5XWM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052643, IPR041870, IPR041862, IPR036249, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- specific granule lumen (GO:0035580)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 115 |
| PubMed broad count | 141 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0573, TXNDC4 |

**关键文献**:
1. Adiponectin, a Therapeutic Target for Obesity, Diabetes, and Endothelial Dysfunction.. *International journal of molecular sciences*. PMID: 28635626
2. Ero1α-Dependent ERp44 Dissociation From RyR2 Contributes to Cardiac Arrhythmia.. *Circulation research*. PMID: 35086342
3. Opposing regulation of endoplasmic reticulum retention under stress by ERp44 and PDIA6.. *The Biochemical journal*. PMID: 39621446
4. The pivotal role of ERp44 in patrolling protein secretion.. *Journal of cell science*. PMID: 33173013
5. The role of ERp44 in glucose and lipid metabolism.. *Archives of biochemistry and biophysics*. PMID: 31283909

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.9 |
| 高置信度残基 (pLDDT>90) 占比 | 80.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 89.6% |
| 可用 PDB 条目 | 2R2J, 5GU6, 5GU7, 5HQP, 5XWM |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2R2J, 5GU6, 5GU7, 5HQP, 5XWM）+ AlphaFold极高置信度预测（pLDDT=89.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052643, IPR041870, IPR041862, IPR036249, IPR013766; Pfam: PF00085, PF13848 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERO1A | 0.997 | 0.475 | — |
| ITPR1 | 0.988 | 0.334 | — |
| PRDX4 | 0.982 | 0.913 | — |
| ERO1B | 0.977 | 0.506 | — |
| LMAN1 | 0.903 | 0.303 | — |
| TXN | 0.895 | 0.000 | — |
| SUMF1 | 0.873 | 0.206 | — |
| ZNF385A | 0.872 | 0.091 | — |
| JCHAIN | 0.871 | 0.000 | — |
| DNAJB11 | 0.855 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Itpr1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15652484 |
| Catsup | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3420 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Nmd3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3557 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ND-19 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Invadolysin | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Act5C | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sstn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| slow | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.9 + PDB: 2R2J, 5GU6, 5GU7, 5HQP, 5XWM | pLDDT=89.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERP44 — Endoplasmic reticulum resident protein 44，研究基础较多，新颖性有限。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 115 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BS26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023318-ERP44/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERP44
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BS26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
