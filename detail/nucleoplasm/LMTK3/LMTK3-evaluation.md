---
type: protein-evaluation
gene: "LMTK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LMTK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMTK3 / KIAA1883, TYKLM3 |
| 蛋白名称 | Serine/threonine-protein kinase LMTK3 |
| 蛋白大小 | 1460 aa / 153.7 kDa |
| UniProt ID | Q96Q04 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cell Junctions; UniProt: Membrane; Cell projection, axon; Cell projection, dendrite;  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1460 aa / 153.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.1; PDB: 6SEQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions | Uncertain |
| UniProt | Membrane; Cell projection, axon; Cell projection, dendrite; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- dendrite (GO:0030425)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1883, TYKLM3 |

**关键文献**:
1. Integrated multi-omics approach to distinct molecular characterization and classification of early-onset colorectal cancer.. *Cell reports. Medicine*. PMID: 36921601
2. LMTK3 regulation of EV biogenesis and cargo sorting promotes tumour growth by reducing monocyte infiltration and driving pro-tumourigenic macrophage polarisation in breast cancer.. *Molecular cancer*. PMID: 40405280
3. The structure-function relationship of oncogenic LMTK3.. *Science advances*. PMID: 33188023
4. LMTK3 confers chemo-resistance in breast cancer.. *Oncogene*. PMID: 29540829
5. LMTK3 knockdown retards cell growth and invasion and promotes apoptosis in thyroid cancer.. *Molecular medicine reports*. PMID: 28260052

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.1 |
| 高置信度残基 (pLDDT>90) 占比 | 13.5% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 76.6% |
| 有序区域 (pLDDT>70) 占比 | 20.1% |
| 可用 PDB 条目 | 6SEQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=46.1），有序残基占 20.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008266; Pfam: PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1CA | 0.609 | 0.294 | — |
| ESR1 | 0.566 | 0.294 | — |
| MAZ | 0.466 | 0.052 | — |
| C2CD4D | 0.444 | 0.000 | — |
| DACT3 | 0.417 | 0.000 | — |
| ELFN1 | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ESR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-26383|pubmed:21602804 |
| Shank3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Fmr1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Fxr1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| ABCE1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| IGF2R | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| PFKM | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| CKMT1A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 15
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.1 + PDB: 6SEQ | pLDDT=46.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Cell projection, axon; Cell projection,  / Nucleoplasm; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 6 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LMTK3 — Serine/threonine-protein kinase LMTK3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1460 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96Q04
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142235-LMTK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMTK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96Q04
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000142235-LMTK3/subcellular

![](https://images.proteinatlas.org/40203/1356_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/40203/1356_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/40203/411_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/40203/411_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/40203/415_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/40203/415_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96Q04-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
