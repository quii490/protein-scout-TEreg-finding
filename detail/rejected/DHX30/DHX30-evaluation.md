---
type: protein-evaluation
gene: "DHX30"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHX30 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX30 |
| 蛋白名称 | ATP-dependent RNA helicase DHX30 |
| 蛋白大小 | 1194 aa / 133.9 kDa |
| UniProt ID | Q7L2E3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; 额外: Cytosol; UniProt: Cytoplasm; Mitochondrion; Mitochondrion matrix, mitochondrio |
| 蛋白大小 | 8/10 | x1 | 8 | 1194 aa / 133.9 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (<=60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=81.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Mitochondrion; Mitochondrion matrix, mitochondrion nucleoid | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 43 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Neurodevelopmental disorder with variable motor and language impairment (NEDMIAL): first case reported in Argentina.. *Arch Argent Pediatr*. PMID: 40591572
2. Bioinformatics analysis and polyclonal antibody preparation of Mesocricetus auratus DHX30.. *Protein Expr Purif*. PMID: 40199434
3. Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA(Thr) production.. *Proc Natl Acad Sci U S A*. PMID: 39752519
4. A subcellular selective APEX2-based proximity labeling used for identifying mitochondrial G-quadruplex DNA binding proteins.. *Nucleic Acids Res*. PMID: 39718986
5. Proteome Dynamics in iPSC-Derived Human Dopaminergic Neurons.. *Mol Cell Proteomics*. PMID: 39251023

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.1 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 82.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.1，有序区 82.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLRMT | 0.000 | 0.000 | — |
| GRSF1 | 0.000 | 0.000 | — |
| DDX28 | 0.000 | 0.000 | — |
| FASTKD3 | 0.000 | 0.000 | — |
| PTCD3 | 0.000 | 0.000 | — |
| SSBP1 | 0.000 | 0.000 | — |
| FASTKD2 | 0.000 | 0.000 | — |
| YBX1 | 0.000 | 0.000 | — |
| ILF3 | 0.000 | 0.000 | — |
| NCBP2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q7L2E3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y6K5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.1 + PDB: 无 | pLDDT=81.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Mitochondrion; Mitochondrion matrix, mi / Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DHX30 -- ATP-dependent RNA helicase DHX30，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1194 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L2E3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132153-DHX30/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX30
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L2E3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L2E3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
