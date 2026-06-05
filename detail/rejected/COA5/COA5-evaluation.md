---
type: protein-evaluation
gene: "COA5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COA5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COA5 / C2orf64, PET191 |
| 蛋白名称 | Cytochrome c oxidase assembly factor 5 |
| 蛋白大小 | 74 aa / 8.4 kDa |
| UniProt ID | Q86WW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion intermembrane space |
| 蛋白大小 | 5/10 | ×1 | 5 | 74 aa / 8.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018793; Pfam: PF10203 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion intermembrane space | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf64, PET191 |

**关键文献**:
1. Association of Predicted Expression and Multimodel Association Analysis of Substance Abuse Traits.. *Complex psychiatry*. PMID: 36407771
2. Development and Evaluation of the Protective Efficacy of Novel Marek's Disease Virus Rispens Vector Vaccines Against Infectious Bursal Disease.. *Avian diseases*. PMID: 27610721
3. Characterization of the liver proteome in dairy cows experiencing negative energy balance at early lactation.. *Journal of proteomics*. PMID: 34153542
4. Quantitative Proteomics Analysis of Ischemia/Reperfusion Injury-Modulated Proteins in Cardiac Microvascular Endothelial Cells and the Protective Role of Tongxinluo.. *Cellular physiology and biochemistry : international journal of experimental cellular physiology, biochemistry, and pharmacology*. PMID: 28334711
5. COA5 has an essential role in the early stage of mitochondrial complex IV assembly.. *Life science alliance*. PMID: 39779219

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 54.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 18.9% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 79.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.1，有序区 79.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018793; Pfam: PF10203 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COX17 | 0.842 | 0.000 | — |
| CHCHD7 | 0.786 | 0.000 | — |
| CHCHD4 | 0.778 | 0.199 | — |
| COX19 | 0.774 | 0.000 | — |
| PET117 | 0.772 | 0.000 | — |
| SCO1 | 0.763 | 0.000 | — |
| COA6 | 0.754 | 0.000 | — |
| TIMM9 | 0.730 | 0.000 | — |
| COX11 | 0.725 | 0.000 | — |
| COX14 | 0.710 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP1-3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT31 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CHCHD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GAPDHS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GFAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TYMP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 无 | pLDDT=83.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion intermembrane space / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COA5 — Cytochrome c oxidase assembly factor 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小74 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183513-COA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000183513-COA5/subcellular

![](https://images.proteinatlas.org/57768/1231_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57768/1231_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57768/1301_C7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57768/1301_C7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/57768/994_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57768/994_C7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86WW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
