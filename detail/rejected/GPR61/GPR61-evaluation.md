---
type: protein-evaluation
gene: "GPR61"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR61 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR61 / BALGR, GPCR3 |
| 蛋白名称 | G-protein coupled receptor 61 |
| 蛋白大小 | 451 aa / 49.3 kDa |
| UniProt ID | Q9BZJ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 451 aa / 49.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 8KGK, 8TB0, 8TB7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endosome (GO:0005768)
- endosome membrane (GO:0010008)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BALGR, GPCR3 |

**关键文献**:
1. Weather and Birth Weight: Different Roles of Maternal and Neonatal GPR61 Promoter Methylation.. *Biomedical and environmental sciences : BES*. PMID: 35317898
2. Identification and molecular characterization of missense mutations in orphan G protein-coupled receptor GPR61 occurring in severe obesity.. *Molecular pharmacology*. PMID: 40133016
3. Discovery of Potent and Brain-Penetrant Inverse Agonists for GPR61, an Orphan G Protein-Coupled Receptor.. *Journal of medicinal chemistry*. PMID: 41834467
4. Orphan GPR61, GPR62 and GPR135 receptors and the melatonin MT(2) receptor reciprocally modulate their signaling functions.. *Scientific reports*. PMID: 28827538
5. Heifers express G-protein coupled receptor 61 in anterior pituitary gonadotrophs in stage-dependent manner.. *Animal reproduction science*. PMID: 28433506

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 53.4% |
| 可用 PDB 条目 | 8KGK, 8TB0, 8TB7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 53.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPER1 | 0.902 | 0.000 | — |
| GPR150 | 0.503 | 0.000 | — |
| GJB6 | 0.499 | 0.477 | — |
| RNF157 | 0.487 | 0.000 | — |
| GPR52 | 0.480 | 0.000 | — |
| GPR162 | 0.479 | 0.000 | — |
| GPR20 | 0.475 | 0.000 | — |
| GPR45 | 0.471 | 0.000 | — |
| GPR3 | 0.470 | 0.000 | — |
| GPR63 | 0.470 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000484797.1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SCN3B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PLP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TUSC5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM218 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KLRC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GJA8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATP6V0B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM147 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 8KGK, 8TB0, 8TB7 | pLDDT=69.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Endosome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR61 — G-protein coupled receptor 61，非常新颖，仅有少数基础研究。
2. 蛋白大小451 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZJ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156097-GPR61/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR61
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZJ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZJ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
