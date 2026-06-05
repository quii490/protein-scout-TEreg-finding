---
type: protein-evaluation
gene: "GPR34"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR34 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR34 |
| 蛋白名称 | Probable G-protein coupled receptor 34 |
| 蛋白大小 | 381 aa / 43.9 kDa |
| UniProt ID | Q9UPC5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 43.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.5; PDB: 8IYX, 8IZ4, 8K4N, 8SAI, 8WRB, 8XBE, 8XBG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452, IPR048057; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
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
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 45.9% |
| 置信残基 (pLDDT 70-90) 占比 | 27.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 20.2% |
| 有序区域 (pLDDT>70) 占比 | 72.9% |
| 可用 PDB 条目 | 8IYX, 8IZ4, 8K4N, 8SAI, 8WRB, 8XBE, 8XBG, 8XBH, 8XBI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8IYX, 8IZ4, 8K4N, 8SAI, 8WRB, 8XBE, 8XBG, 8XBH, 8XBI）+ AlphaFold极高置信度预测（pLDDT=77.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR048057; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EFHC2 | 0.846 | 0.000 | — |
| TMEM119 | 0.737 | 0.000 | — |
| TREM2 | 0.689 | 0.000 | — |
| GPR82 | 0.688 | 0.000 | — |
| OLFML3 | 0.683 | 0.000 | — |
| ADORA3 | 0.675 | 0.000 | — |
| C1QA | 0.672 | 0.000 | — |
| CSF1R | 0.581 | 0.000 | — |
| TYROBP | 0.527 | 0.000 | — |
| AIF1 | 0.523 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498130.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| aspC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COX7A2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MT-ND5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 8IYX, 8IZ4, 8K4N, 8SAI, 8WRB,  | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Cytosol | 一致 |
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
1. GPR34 — Probable G-protein coupled receptor 34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPC5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171659-GPR34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPC5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000171659-GPR34/subcellular

![](https://images.proteinatlas.org/25490/665_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25490/665_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25490/668_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25490/668_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25490/674_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25490/674_B11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPC5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
