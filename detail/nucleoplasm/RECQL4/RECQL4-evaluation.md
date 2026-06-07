---
type: protein-evaluation
gene: "RECQL4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RECQL4 — REJECTED (研究热度过高 (PubMed strict=239，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RECQL4 / RECQ4 |
| 蛋白名称 | ATP-dependent DNA helicase Q4 |
| 蛋白大小 | 1208 aa / 133.1 kDa |
| UniProt ID | O94761 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1208 aa / 133.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=239 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.4; PDB: 2KMU, 5LST |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011545, IPR004589, IPR021110, IPR014001, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 239 |
| PubMed broad count | 423 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RECQ4 |

**关键文献**:
1. Rothmund-Thomson syndrome.. *Orphanet journal of rare diseases*. PMID: 20113479
2. USP50 suppresses alternative RecQ helicase use and deleterious DNA2 activity during replication.. *Nature communications*. PMID: 39284827
3. Rothmund-Thomson syndrome and RECQL4 defect: splitting and lumping.. *Cancer letters*. PMID: 16271439
4. Shared and non-overlapping functions of RECQL4 and BLM helicases in chemotherapeutics-induced glioma cell responses.. *BMC cancer*. PMID: 41023983
5. An overview of RecQ helicases and related diseases.. *Aging*. PMID: 40728512

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 35.4% |
| 有序区域 (pLDDT>70) 占比 | 59.0% |
| 可用 PDB 条目 | 2KMU, 5LST |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.4），有序残基占 59.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR004589, IPR021110, IPR014001, IPR001650; Pfam: PF00270, PF11719, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCM | 0.991 | 0.967 | — |
| MCM10 | 0.989 | 0.526 | — |
| CDC45 | 0.982 | 0.510 | — |
| RAD51 | 0.982 | 0.844 | — |
| EXO1 | 0.981 | 0.763 | — |
| FEN1 | 0.981 | 0.469 | — |
| TICRR | 0.972 | 0.000 | — |
| TOP3A | 0.962 | 0.832 | — |
| CHTF18 | 0.951 | 0.094 | — |
| TOPBP1 | 0.948 | 0.107 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q99PV9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PRSS23 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| Fas2 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| GNAI2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CHCHD3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HNRNPA1L2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HNRNPA1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ATAD3A | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| STOM | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 2KMU, 5LST | pLDDT=67.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RECQL4 — ATP-dependent DNA helicase Q4，研究基础较多，新颖性有限。
2. 蛋白大小1208 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 239 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 239 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94761
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160957-RECQL4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RECQL4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94761
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/RECQL4/IF_images/RECQL4_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000160957-RECQL4/subcellular

![](https://images.proteinatlas.org/25821/604_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/25821/604_C6_3_red_green.jpg)
![](https://images.proteinatlas.org/25821/607_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/25821/607_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/25821/609_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/25821/609_C6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94761-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94761 |
| SMART | SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 489..662; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 683..850; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011545;IPR004589;IPR021110;IPR014001;IPR001650;IPR027417; |
| Pfam | PF00270;PF11719;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160957-RECQL4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAG2 | Biogrid, Bioplex | true |
| PNMA2 | Biogrid, Bioplex | true |
| PTGES3 | Biogrid, Bioplex | true |
| SF3B3 | Biogrid, Bioplex | true |
| TUBB | Biogrid, Bioplex | true |
| ACTL6B | Bioplex | false |
| AHCYL1 | Biogrid | false |
| AMZ1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
