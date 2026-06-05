---
type: protein-evaluation
gene: "ERICH3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERICH3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERICH3 / C1orf173 |
| 蛋白名称 | Glutamate-rich protein 3 |
| 蛋白大小 | 1530 aa / 168.5 kDa |
| UniProt ID | Q5RHP9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane, Endoplasmic reticulum; 额外: Nucleoli, Prima; UniProt: Cell projection, cilium; Cytoplasm; Cytoplasm, cytoskeleton, |
| 蛋白大小 | 5/10 | ×1 | 5 | 1530 aa / 168.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR048257, IPR027962; Pfam: PF15257 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Endoplasmic reticulum; 额外: Nucleoli, Primary cilium | Uncertain |
| UniProt | Cell projection, cilium; Cytoplasm; Cytoplasm, cytoskeleton, cilium axoneme | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- non-motile cilium (GO:0097730)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf173 |

**关键文献**:
1. ERICH3: vesicular association and antidepressant treatment response.. *Molecular psychiatry*. PMID: 33230203
2. ERICH3 in Primary Cilia Regulates Cilium Formation and the Localisations of Ciliary Transport and Sonic Hedgehog Signaling Proteins.. *Scientific reports*. PMID: 31712586
3. Enterovirus 71 VP1 promotes 5-HT release by upregulating the expression of ERICH3 and methyltransferase ZC3H13.. *Virus research*. PMID: 35660571
4. Long non-coding RNA ERICH3-AS1 is an unfavorable prognostic factor for gastric cancer.. *PeerJ*. PMID: 32025363
5. Screening and identification of key biomarkers in nasopharyngeal carcinoma: Evidence from bioinformatic analysis.. *Medicine*. PMID: 31770211

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.6 |
| 高置信度残基 (pLDDT>90) 占比 | 7.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 82.9% |
| 有序区域 (pLDDT>70) 占比 | 13.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.6），有序残基占 13.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048257, IPR027962; Pfam: PF15257 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSPAN5 | 0.742 | 0.000 | — |
| CFAP44 | 0.625 | 0.094 | — |
| KLHL26 | 0.566 | 0.091 | — |
| ODF3L2 | 0.541 | 0.000 | — |
| SAXO2 | 0.514 | 0.079 | — |
| TAFA2 | 0.493 | 0.000 | — |
| TEKT1 | 0.483 | 0.000 | — |
| KLHL32 | 0.464 | 0.000 | — |
| CCDC173 | 0.457 | 0.079 | — |
| PLCD4 | 0.457 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDM2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HNRNPDL | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPCL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Bach1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Tuba3a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KLK6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.6 + PDB: 无 | pLDDT=43.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm; Cytoplasm, cyt / Nuclear membrane, Endoplasmic reticulum; 额外: Nucle | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ERICH3 — Glutamate-rich protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1530 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=43.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5RHP9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178965-ERICH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERICH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5RHP9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000178965-ERICH3/subcellular

![](https://images.proteinatlas.org/28655/2179_G1_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/28655/2179_G1_52_blue_red_green.jpg)
![](https://images.proteinatlas.org/28655/2234_F1_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/28655/2234_F1_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/28655/2243_B2_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/28655/2243_B2_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5RHP9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
