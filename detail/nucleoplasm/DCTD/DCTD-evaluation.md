---
type: protein-evaluation
gene: "DCTD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCTD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTD |
| 蛋白名称 | Deoxycytidylate deaminase |
| 蛋白大小 | 178 aa / 20.0 kDa |
| UniProt ID | P32321 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 178 aa / 20.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.5; PDB: 2W4L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016192, IPR002125, IPR016193, IPR016473, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 251 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Decitabine cytotoxicity is promoted by dCMP deaminase DCTD and mitigated by SUMO-dependent E3 ligase TOPORS.. *The EMBO journal*. PMID: 38760575
2. An integrated mechanism of G(q) regulation of PLCβ enzymes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40249783
3. Based on network pharmacology, molecular docking and experimental verification to reveal the mechanism of Andrographis paniculata against solar dermatitis.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 39326136
4. Transition of Dephospho-DctD to the Transcriptionally Active State via Interaction with Dephospho-IIA(Glc).. *mBio*. PMID: 35311533
5. Immune Characteristics of eQTL and Gene Risk Model and the Inhibitory Effect of DCTD and RRAS on Ferroptosis in Glioblastoma.. *Frontiers in bioscience (Landmark edition)*. PMID: 40917066

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 87.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 2W4L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.5，有序区 94.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016192, IPR002125, IPR016193, IPR016473, IPR015517; Pfam: PF00383 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYMS | 0.998 | 0.000 | — |
| DCK | 0.985 | 0.000 | — |
| DTYMK | 0.983 | 0.000 | — |
| DUT | 0.977 | 0.073 | — |
| TK2 | 0.970 | 0.000 | — |
| DCTPP1 | 0.959 | 0.000 | — |
| CMPK2 | 0.955 | 0.000 | — |
| NT5C2 | 0.949 | 0.000 | — |
| NT5C | 0.942 | 0.000 | — |
| NT5C1A | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000424017.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP76 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NUDT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| PSMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2I | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACOT7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 2W4L | pLDDT=94.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DCTD — Deoxycytidylate deaminase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小178 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P32321
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129187-DCTD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P32321
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000129187-DCTD/subcellular

![](https://images.proteinatlas.org/35894/404_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/35894/404_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/35894/410_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/35894/410_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P32321-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
