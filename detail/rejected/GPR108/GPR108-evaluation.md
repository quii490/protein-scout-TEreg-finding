---
type: protein-evaluation
gene: "GPR108"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR108 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR108 / LUSTR2 |
| 蛋白名称 | Protein GPR108 |
| 蛋白大小 | 543 aa / 60.6 kDa |
| UniProt ID | Q9NPR9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; 额外: Vesicles; UniProt: Golgi apparatus, cis-Golgi network membrane; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 543 aa / 60.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR053937, IPR009637; Pfam: PF06814 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Vesicles | Approved |
| UniProt | Golgi apparatus, cis-Golgi network membrane; Golgi apparatus, trans-Golgi network membrane; Golgi ap... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network membrane (GO:0033106)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- trans-Golgi network (GO:0005802)

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
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 43.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.3，有序区 71.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053937, IPR009637; Pfam: PF06814 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCAMP2 | 0.766 | 0.000 | — |
| KIAA0319L | 0.659 | 0.000 | — |
| CNPPD1 | 0.636 | 0.000 | — |
| GPR152 | 0.631 | 0.000 | — |
| GPR137 | 0.556 | 0.000 | — |
| GPR137B | 0.555 | 0.000 | — |
| TPRA1 | 0.543 | 0.000 | — |
| GPR137C | 0.529 | 0.000 | — |
| GPR171 | 0.494 | 0.000 | — |
| TM9SF2 | 0.458 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRSAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FXYD6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GLRA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| yhjW | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CD53 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MTERF3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM209A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM243 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GJA8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 无 | pLDDT=75.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, cis-Golgi network membrane; Golgi / Golgi apparatus; 额外: Vesicles | 一致 |
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
1. GPR108 — Protein GPR108，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小543 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPR9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125734-GPR108/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR108
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPR9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000125734-GPR108/subcellular

![](https://images.proteinatlas.org/41924/484_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41924/484_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41924/489_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41924/489_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41924/492_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41924/492_F1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPR9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
