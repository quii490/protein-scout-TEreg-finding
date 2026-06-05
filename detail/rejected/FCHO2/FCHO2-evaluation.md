---
type: protein-evaluation
gene: "FCHO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FCHO2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCHO2 |
| 蛋白名称 | F-BAR domain only protein 2 |
| 蛋白大小 | 810 aa / 88.9 kDa |
| UniProt ID | Q0JRZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome; 额外: Vesicles, Cytosol; UniProt: Membrane, clathrin-coated pit |
| 蛋白大小 | 8/10 | ×1 | 8 | 810 aa / 88.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.2; PDB: 2V0O, 7OG1, 7OHO, 7OHZ, 7OI5, 7OIQ, 7OIT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027267, IPR031160, IPR001060, IPR030122, IPR054 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Vesicles, Cytosol | Approved |
| UniProt | Membrane, clathrin-coated pit | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin-coated pit (GO:0005905)
- clathrin-coated vesicle (GO:0030136)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)
- presynapse (GO:0098793)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Nedd4L ubiquitin ligase is activated by FCHO2-generated membrane curvature.. *The EMBO journal*. PMID: 39402328
2. Intersectin1 promotes clathrin-mediated endocytosis by organizing and stabilizing endocytic protein interaction networks.. *Cell reports*. PMID: 39580802
3. Chrysin-Induced G Protein-Coupled Estrogen Receptor Activation Suppresses Pancreatic Cancer.. *International journal of molecular sciences*. PMID: 36077069
4. Identification and characterization of human FCHO2 and mouse Fcho2 genes in silico.. *International journal of molecular medicine*. PMID: 15254787
5. Mon1a and FCHO2 are required for maintenance of Golgi architecture.. *bioRxiv : the preprint server for biology*. PMID: 37461455

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 59.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 30.0% |
| 有序区域 (pLDDT>70) 占比 | 67.1% |
| 可用 PDB 条目 | 2V0O, 7OG1, 7OHO, 7OHZ, 7OI5, 7OIQ, 7OIT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2V0O, 7OG1, 7OHO, 7OHZ, 7OI5, 7OIQ, 7OIT）+ AlphaFold极高置信度预测（pLDDT=76.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR031160, IPR001060, IPR030122, IPR054713; Pfam: PF22699, PF10291 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS15 | 0.996 | 0.816 | — |
| ITSN1 | 0.985 | 0.330 | — |
| ITSN2 | 0.985 | 0.093 | — |
| DAB2 | 0.968 | 0.829 | — |
| TRIP10 | 0.964 | 0.062 | — |
| AP2S1 | 0.935 | 0.800 | — |
| AP2B1 | 0.931 | 0.752 | — |
| AP2M1 | 0.916 | 0.702 | — |
| EPS15L1 | 0.913 | 0.644 | — |
| EPN2 | 0.889 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| mutS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EPS15 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19380743|imex:IM-20432 |
| flaS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000393776.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dnaX | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A7M7D8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 2V0O, 7OG1, 7OHO, 7OHZ, 7OI5,  | pLDDT=76.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane, clathrin-coated pit / Centrosome; 额外: Vesicles, Cytosol | 一致 |
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
1. FCHO2 — F-BAR domain only protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小810 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0JRZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157107-FCHO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCHO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0JRZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000157107-FCHO2/subcellular

![](https://images.proteinatlas.org/77850/1611_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77850/1611_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77850/1740_C7_18_cr57fcfaded1733_blue_red_green.jpg)
![](https://images.proteinatlas.org/77850/1740_C7_23_cr57fcfae7a3863_blue_red_green.jpg)
![](https://images.proteinatlas.org/77850/1744_C7_12_cr580488e1f2732_blue_red_green.jpg)
![](https://images.proteinatlas.org/77850/1744_C7_21_cr580488f6aac97_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q0JRZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
