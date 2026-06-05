---
type: protein-evaluation
gene: "AADAC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AADAC — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AADAC / DAC |
| 蛋白名称 | Arylacetamide deacetylase |
| 蛋白大小 | 399 aa / 45.7 kDa |
| UniProt ID | P22760 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 399 aa / 45.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=74 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013094, IPR029058, IPR017157, IPR050300, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 74 |
| PubMed broad count | 119 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAC |

**关键文献**:
1. Arylacetamide deacetylase regulates hepatic iron homeostasis to protect against carbon tetrachloride-induced ferroptosis.. *Archives of toxicology*. PMID: 39367970
2. Association of the AADAC gene and Tourette syndrome in a Han Chinese cohort.. *Neuroscience letters*. PMID: 29253601
3. Evaluation of gene expression of PLEKHS1, AADAC, and CDKN3 as novel genomic markers in gastric carcinoma.. *PloS one*. PMID: 35446856
4. Hydrolase activities of cynomolgus monkey liver microsomes and recombinant CES1, CES2, and AADAC.. *European journal of pharmaceutical sciences : official journal of the European Federation for Pharmaceutical Sciences*. PMID: 33722734
5. N-Glycosylation during translation is essential for human arylacetamide deacetylase enzyme activity.. *Biochemical pharmacology*. PMID: 24125761

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 91.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.6，有序区 99.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013094, IPR029058, IPR017157, IPR050300, IPR033140; Pfam: PF07859 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAT2 | 0.875 | 0.045 | — |
| NAT1 | 0.832 | 0.045 | — |
| CES1 | 0.693 | 0.000 | — |
| RGN | 0.621 | 0.000 | — |
| CES2 | 0.616 | 0.000 | — |
| KYNU | 0.610 | 0.000 | — |
| ABHD5 | 0.605 | 0.000 | — |
| TDO2 | 0.603 | 0.000 | — |
| NDUFS1 | 0.572 | 0.503 | — |
| UQCRFS1 | 0.535 | 0.461 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| APPBP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 无 | pLDDT=95.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AADAC — Arylacetamide deacetylase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 74 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22760
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114771-AADAC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AADAC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22760
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P22760-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
