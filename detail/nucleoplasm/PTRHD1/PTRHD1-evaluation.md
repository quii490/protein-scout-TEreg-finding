---
type: protein-evaluation
gene: "PTRHD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTRHD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTRHD1 / C2orf79 |
| 蛋白名称 | Putative peptidyl-tRNA hydrolase PTRHD1 |
| 蛋白大小 | 140 aa / 15.8 kDa |
| UniProt ID | Q6GMV3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 140 aa / 15.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023476, IPR002833, IPR042237; Pfam: PF01981 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf79 |

**关键文献**:
1. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
2. Clinical Variability of SYNJ1-Associated Early-Onset Parkinsonism.. *Frontiers in neurology*. PMID: 33841314
3. The genetic landscape of Parkinson's disease.. *Revue neurologique*. PMID: 30245141
4. Analysis of PTRHD1 common and rare variants in European patients with Parkinson's disease.. *Neurobiology of aging*. PMID: 34246528
5. New Genes Causing Hereditary Parkinson's Disease or Parkinsonism.. *Current neurology and neuroscience reports*. PMID: 28733970

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 83.6% |
| 置信残基 (pLDDT 70-90) 占比 | 0.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 84.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 84.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023476, IPR002833, IPR042237; Pfam: PF01981 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS13C | 0.629 | 0.000 | — |
| C6orf89 | 0.627 | 0.627 | — |
| DNAJC6 | 0.620 | 0.000 | — |
| TMEM230 | 0.619 | 0.000 | — |
| RAB39B | 0.592 | 0.000 | — |
| CHCHD2 | 0.583 | 0.000 | — |
| FBXO7 | 0.578 | 0.000 | — |
| DNAJC13 | 0.578 | 0.000 | — |
| RIC3 | 0.572 | 0.000 | — |
| SYNJ1 | 0.527 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| C6orf89 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RY12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPA4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TSR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| S100A6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NFKBIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SUMO1P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FSD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GSX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 无 | pLDDT=90.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PTRHD1 — Putative peptidyl-tRNA hydrolase PTRHD1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小140 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6GMV3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184924-PTRHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTRHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6GMV3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184924-PTRHD1/subcellular

![](https://images.proteinatlas.org/19951/221_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/19951/221_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/19951/222_B8_3_red_green.jpg)
![](https://images.proteinatlas.org/19951/222_B8_4_red_green.jpg)
![](https://images.proteinatlas.org/19951/248_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6GMV3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
