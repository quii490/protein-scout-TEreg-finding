---
type: protein-evaluation
gene: "GOLM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLM1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLM1 / C9orf155, GOLPH2 |
| 蛋白名称 | Golgi membrane protein 1 |
| 蛋白大小 | 401 aa / 45.3 kDa |
| UniProt ID | Q8NBJ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus, cis-Golgi network membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 401 aa / 45.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 8YBC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026139 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Golgi apparatus, cis-Golgi network membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

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
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 39.4% |
| 有序区域 (pLDDT>70) 占比 | 43.9% |
| 可用 PDB 条目 | 8YBC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 43.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026139 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GOLPH3 | 0.808 | 0.108 | — |
| GPC3 | 0.736 | 0.000 | — |
| AFP | 0.717 | 0.000 | — |
| FAM20C | 0.633 | 0.292 | — |
| TRAF6 | 0.621 | 0.000 | — |
| NAA35 | 0.619 | 0.000 | — |
| KCNQ2 | 0.586 | 0.564 | — |
| SPINK1 | 0.581 | 0.000 | — |
| GET4 | 0.572 | 0.572 | — |
| GOLIM4 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RACK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FTH1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DCK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DCTN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF3J | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GEMIN7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| C1orf174 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL13A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MED22 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 8YBC | pLDDT=64.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, cis-Golgi network membrane / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLM1 — Golgi membrane protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小401 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBJ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135052-GOLM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBJ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (enhanced)。来源: https://www.proteinatlas.org/ENSG00000135052-GOLM1/subcellular

![](https://images.proteinatlas.org/10638/100_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10638/100_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10638/101_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10638/101_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10638/82_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10638/82_D12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NBJ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
