---
type: protein-evaluation
gene: "CCDC87"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CCDC87 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC87 |
| 蛋白名称 | Coiled-coil domain-containing protein 87 |
| 蛋白大小 | 849 aa / 96.4 kDa |
| UniProt ID | Q9NVE4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 849 aa / 96.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037383; Pfam: PF03999 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Ccdc87 is critical for sperm function and male fertility.. *Biology of reproduction*. PMID: 29733332

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 8.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.7% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 34.4% |
| 有序区域 (pLDDT>70) 占比 | 41.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 41.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037383; Pfam: PF03999 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCDC2B | 0.562 | 0.000 | — |
| CCDC58 | 0.513 | 0.000 | — |
| PRR14L | 0.480 | 0.000 | — |
| CCDC97 | 0.479 | 0.000 | — |
| FAM184B | 0.451 | 0.000 | — |
| SUN2 | 0.447 | 0.292 | — |
| RTL5 | 0.442 | 0.000 | — |
| CCDC155 | 0.431 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KASH5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CDR2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| USHBP1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SUN2 | psi-mi:"MI:0096"(pull down) | pubmed:22555292|imex:IM-24042 |
| STAT3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| ESR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:25604459|imex:IM-23333 |
| TRIM54 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| TRIM27 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| KRT15 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 13
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 8 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CCDC87 — Coiled-coil domain-containing protein 87，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小849 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVE4
- Protein Atlas: https://www.proteinatlas.org/search/CCDC87
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC87
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVE4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000182791-CCDC87/subcellular

![](https://images.proteinatlas.org/79508/2064_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/79508/2064_A3_5_red_green.jpg)
![](https://images.proteinatlas.org/79508/2089_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/79508/2089_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/79508/2180_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/79508/2180_F1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVE4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
