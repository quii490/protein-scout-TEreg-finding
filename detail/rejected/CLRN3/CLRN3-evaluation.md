---
type: protein-evaluation
gene: "CLRN3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLRN3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLRN3 / TMEM12, USH3AL1 |
| 蛋白名称 | Clarin-3 |
| 蛋白大小 | 226 aa / 25.3 kDa |
| UniProt ID | Q8NCR9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 226 aa / 25.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026748; Pfam: PF25807 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM12, USH3AL1 |

**关键文献**:
1. A CLRN3-Based CD8(+) T-Related Gene Signature Predicts Prognosis and Immunotherapy Response in Colorectal Cancer.. *Biomolecules*. PMID: 39199281
2. Differential Membrane Protein Profile in Bovine X- and Y-Sperm.. *Journal of proteome research*. PMID: 34009990
3. Deciphering aptamer-protein interactions for bovine sperm sorting through in silico and in vitro studies.. *Molecular biology reports*. PMID: 40085160
4. Mapping the Cell-Surface N-Glycoproteome of Human Hepatocytes Reveals Markers for Selecting a Homogeneous Population of iPSC-Derived Hepatocytes.. *Stem cell reports*. PMID: 27569060
5. A 14-Methylation-Driven Differentially Expressed RNA as a Signature for Overall Survival Prediction in Patients with Uterine Corpus Endometrial Carcinoma.. *DNA and cell biology*. PMID: 32397815

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 52.7% |
| 置信残基 (pLDDT 70-90) 占比 | 35.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 87.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.6，有序区 87.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026748; Pfam: PF25807 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMIGD1 | 0.728 | 0.000 | — |
| CACNG2 | 0.717 | 0.000 | — |
| MEP1A | 0.572 | 0.000 | — |
| SLC6A19 | 0.565 | 0.000 | — |
| SLC10A2 | 0.557 | 0.000 | — |
| ZNF614 | 0.537 | 0.000 | — |
| USH1C | 0.528 | 0.000 | — |
| SLC5A1 | 0.520 | 0.000 | — |
| CCNYL1 | 0.491 | 0.000 | — |
| CBARP | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NME2P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| TXNDC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCDC43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HCCS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 无 | pLDDT=86.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. CLRN3 — Clarin-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小226 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCR9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180745-CLRN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLRN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCR9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NCR9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
