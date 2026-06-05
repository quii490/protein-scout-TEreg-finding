---
type: protein-evaluation
gene: "FBH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBH1 / FBX18, FBXO18 |
| 蛋白名称 | F-box DNA helicase 1 |
| 蛋白大小 | 1043 aa / 117.7 kDa |
| UniProt ID | Q8NFZ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1043 aa / 117.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.3; PDB: 8F5Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014017, IPR000212, IPR036047, IPR001810, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX18, FBXO18 |

**关键文献**:
1. Disparate requirements for RAD54L in replication fork reversal.. *Nucleic acids research*. PMID: 39315725
2. Disparate requirements for RAD54L in replication fork reversal.. *bioRxiv : the preprint server for biology*. PMID: 37546955
3. Identification, characterization, and In situ detection of a fruit-body-specific hydrophobin of Pleurotus ostreatus.. *Applied and environmental microbiology*. PMID: 9758836
4. Essential and distinct roles of the F-box and helicase domains of Fbh1 in DNA damage repair.. *BMC molecular biology*. PMID: 18312697
5. Bre1/RNF20 promotes Rad51-mediated strand exchange and antagonizes the Srs2/FBH1 helicases.. *Nature communications*. PMID: 37230987

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.3 |
| 高置信度残基 (pLDDT>90) 占比 | 47.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 8F5Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.3，有序区 75.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014017, IPR000212, IPR036047, IPR001810, IPR027417; Pfam: PF12937, PF00580, PF13361 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.995 | — |
| FANCM | 0.990 | 0.967 | — |
| CUL1 | 0.976 | 0.825 | — |
| RAD51 | 0.962 | 0.848 | — |
| RECQL5 | 0.938 | 0.608 | — |
| PCNA | 0.925 | 0.878 | — |
| WRN | 0.924 | 0.747 | — |
| RBX1 | 0.918 | 0.722 | — |
| RAD52 | 0.915 | 0.752 | — |
| XRCC3 | 0.912 | 0.803 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL13A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| skp1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15147268 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| Nedd1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SYNCRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Rock1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.3 + PDB: 8F5Q | pLDDT=76.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBH1 — F-box DNA helicase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1043 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFZ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134452-FBH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFZ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFZ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
