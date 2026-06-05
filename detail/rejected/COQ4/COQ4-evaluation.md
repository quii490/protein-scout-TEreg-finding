---
type: protein-evaluation
gene: "COQ4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ4 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ4 |
| 蛋白名称 | Ubiquinone biosynthesis protein COQ4 homolog, mitochondrial |
| 蛋白大小 | 265 aa / 29.7 kDa |
| UniProt ID | Q9Y3A0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 265 aa / 29.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=88.1; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR007715, IPR027540; Pfam: PF05019 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- extrinsic component of mitochondrial inner membrane (GO:0031314)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- protein-containing complex (GO:0032991)
- ubiquinone biosynthesis complex (GO:0110142)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 95 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. Hereditary Ataxia Overview.. **. PMID: 20301317
3. Biallelic COQ4 Variants in Hereditary Spastic Paraplegia: Clinical and Molecular Characterization.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 38014483
4. Primary Coenzyme Q10 Deficiency-7 and Pathogenic COQ4 Variants: Clinical Presentation, Biochemical Analyses, and Treatment.. *Frontiers in genetics*. PMID: 35154243
5. Comprehensive analysis of lactate-related gene profiles and immune characteristics in lupus nephritis.. *Frontiers in immunology*. PMID: 38455045

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.1 |
| 高置信度残基 (pLDDT>90) 占比 | 82.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 11.7% |
| 有序区域 (pLDDT>70) 占比 | 86.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.1，有序区 86.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007715, IPR027540; Pfam: PF05019 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ6 | 0.991 | 0.292 | — |
| COQ5 | 0.990 | 0.510 | — |
| COQ3 | 0.988 | 0.508 | — |
| COQ7 | 0.987 | 0.328 | — |
| COQ9 | 0.986 | 0.466 | — |
| COQ8B | 0.927 | 0.125 | — |
| COQ8A | 0.927 | 0.125 | — |
| PDSS1 | 0.916 | 0.000 | — |
| COQ2 | 0.912 | 0.000 | — |
| SLC35D1 | 0.882 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDC19 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HHF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HSL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HTA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| IMD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL20A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL27A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL8B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPP0 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.1 + PDB: 无 | pLDDT=88.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COQ4 -- Ubiquinone biosynthesis protein COQ4 homolog, mitochondrial，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小265 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3A0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167113-COQ4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3A0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3A0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
