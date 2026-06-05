---
type: protein-evaluation
gene: "SPANXN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPANXN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPANXN4 |
| 蛋白名称 | Sperm protein associated with the nucleus on the X chromosome N4 |
| 蛋白大小 | 99 aa / 11.2 kDa |
| UniProt ID | Q5MJ08 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles, Plasma membrane; 额外: Nuclear membrane; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 99 aa / 11.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010007; Pfam: PF07458 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nuclear membrane | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Auto-immunoproteomics analysis of COVID-19 ICU patients revealed increased levels of autoantibodies related to the male reproductive system.. *Frontiers in physiology*. PMID: 37520825
2. Mutational analysis of SPANX genes in families with X-linked prostate cancer.. *The Prostate*. PMID: 17373721

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 39.4% |
| 中等置信 (pLDDT 50-70) 占比 | 59.6% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 39.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 39.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010007; Pfam: PF07458 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPANXA2 | 0.917 | 0.000 | — |
| SPANXA1 | 0.846 | 0.000 | — |
| SPANXD | 0.655 | 0.000 | — |
| CXorf40B | 0.574 | 0.000 | — |
| XAGE3 | 0.571 | 0.000 | — |
| CXorf51A | 0.571 | 0.000 | — |
| TENT5D | 0.544 | 0.000 | — |
| FAM133A | 0.541 | 0.000 | — |
| CSAG3 | 0.501 | 0.292 | — |
| MAGEC3 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| UBA6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TXNL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CAPNS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CAPN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLCG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKCI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 无 | pLDDT=69.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles, Plasma membrane; 额外: Nuclear membrane | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPANXN4 — Sperm protein associated with the nucleus on the X chromosome N4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小99 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5MJ08
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189326-SPANXN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5MJ08
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000189326-SPANXN4/subcellular

![](https://images.proteinatlas.org/59094/1916_F7_23_cr5c9a12ac86cb4_blue_red_green.jpg)
![](https://images.proteinatlas.org/59094/1916_F7_2_cr5c9a12ac86805_blue_red_green.jpg)
![](https://images.proteinatlas.org/59094/1929_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/59094/1929_D1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/59094/1961_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/59094/1961_G11_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5MJ08-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
