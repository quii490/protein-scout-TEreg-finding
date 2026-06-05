---
type: protein-evaluation
gene: "COX8A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX8A — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX8A / COX8, COX8L |
| 蛋白名称 | Cytochrome c oxidase subunit 8A, mitochondrial |
| 蛋白大小 | 69 aa / 7.6 kDa |
| UniProt ID | P10176 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 69 aa / 7.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=85.8; PDB: 5Z62, 8D4T |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR003205, IPR036548; Pfam: PF02285 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)
- respiratory chain complex IV (GO:0045277)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COX8, COX8L |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. Icaritin induces paraptosis in hepatocellular carcinoma cells by targeting BHLHE40 via endoplasmic reticulum stress and mitochondrial dysfunction.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 40424981
3. Interrogating mediators of single-cell transcriptional changes in the acute damaged cerebral cortex: Insights into endothelial-astrocyte interactions.. *Molecular and cellular neurosciences*. PMID: 40090391
4. MRPL17 is a critical regulator of mitochondrial function and a novel therapeutic target in non-small cell lung cancer.. *Cell death & disease*. PMID: 41422086
5. Transcription- and phosphorylation-dependent control of a functional interplay between XBP1s and PINK1 governs mitophagy and potentially impacts Parkinson disease pathophysiology.. *Autophagy*. PMID: 34030589

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 56.5% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 5Z62, 8D4T |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=85.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003205, IPR036548; Pfam: PF02285 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COX5B | 0.999 | 0.800 | — |
| COX6A1 | 0.998 | 0.800 | — |
| COX6C | 0.998 | 0.825 | — |
| COX6B1 | 0.998 | 0.800 | — |
| COX7B | 0.997 | 0.825 | — |
| COX7C | 0.997 | 0.912 | — |
| COX5A | 0.996 | 0.825 | — |
| COX4I1 | 0.996 | 0.913 | — |
| MT-CO1 | 0.990 | 0.900 | — |
| NDUFA4 | 0.989 | 0.860 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 5Z62, 8D4T | pLDDT=85.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COX8A -- Cytochrome c oxidase subunit 8A, mitochondrial，非常新颖，仅有少数基础研究。
2. 蛋白大小69 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10176
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176340-COX8A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX8A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10176
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P10176-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
