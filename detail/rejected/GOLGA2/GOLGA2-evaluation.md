---
type: protein-evaluation
gene: "GOLGA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLGA2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA2 |
| 蛋白名称 | Golgin subfamily A member 2 |
| 蛋白大小 | 1002 aa / 113.1 kDa |
| UniProt ID | Q08379 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus, cis-Golgi network membrane; Endoplasmic ret |
| 蛋白大小 | 8/10 | ×1 | 8 | 1002 aa / 113.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.9; PDB: 4REY, 6IW8, 6IWA, 6K06 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024858, IPR043937, IPR043976; Pfam: PF19046, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Golgi apparatus, cis-Golgi network membrane; Endoplasmic reticulum-Golgi intermediate compartment me... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- Golgi apparatus (GO:0005794)
- Golgi cis cisterna (GO:0000137)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- microtubule (GO:0005874)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 44.3% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 23.7% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 4REY, 6IW8, 6IWA, 6K06 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4REY, 6IW8, 6IWA, 6K06）+ AlphaFold高质量预测（pLDDT=74.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024858, IPR043937, IPR043976; Pfam: PF19046, PF15070 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GORASP1 | 0.999 | 0.981 | — |
| USO1 | 0.997 | 0.787 | — |
| GORASP2 | 0.994 | 0.836 | — |
| STK25 | 0.987 | 0.787 | — |
| RAB1B | 0.979 | 0.637 | — |
| AKAP9 | 0.968 | 0.394 | — |
| GOLGB1 | 0.958 | 0.495 | — |
| RAB1A | 0.947 | 0.795 | — |
| GOLGA3 | 0.943 | 0.239 | — |
| STX5 | 0.943 | 0.494 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000416097.4 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| POM121 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TUBGCP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ABLIM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF250 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Prkce | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11139474 |
| Uso1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12634853|imex:IM-23685 |
| TRIM29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAB2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STK25 | psi-mi:"MI:0018"(two hybrid) | pubmed:15037601 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 4REY, 6IW8, 6IWA, 6K06 | pLDDT=74.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, cis-Golgi network membrane; Endop / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLGA2 — Golgin subfamily A member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1002 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08379
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167110-GOLGA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08379
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (enhanced)。来源: https://www.proteinatlas.org/ENSG00000167110-GOLGA2/subcellular

![](https://images.proteinatlas.org/21178/1772_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21178/1772_C6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/21178/189_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21178/189_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21178/190_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21178/190_B5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08379-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
