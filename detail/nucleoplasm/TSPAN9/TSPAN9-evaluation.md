---
type: protein-evaluation
gene: "TSPAN9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSPAN9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSPAN9 / NET5 |
| 蛋白名称 | Tetraspanin-9 |
| 蛋白大小 | 239 aa / 26.8 kDa |
| UniProt ID | O75954 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 239 aa / 26.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018499, IPR000301, IPR018503, IPR008952; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular matrix (GO:0031012)
- focal adhesion (GO:0005925)
- migrasome (GO:0140494)
- plasma membrane (GO:0005886)
- tetraspanin-enriched microdomain (GO:0097197)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NET5 |

**关键文献**:
1. The role of tetraspanins pan-cancer.. *iScience*. PMID: 35992081
2. Tspan9 Exacerbates Cardiac Hypertrophy by Impairing Cardiac Autophagy.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40406987
3. Screening scaffold proteins for improved functional delivery of luminal proteins using engineered extracellular vesicles.. *Journal of controlled release : official journal of the Controlled Release Society*. PMID: 40425092
4. TSPAN9 inhibits malignant progression of hepatocellular carcinoma.. *Translational cancer research*. PMID: 40792132
5. Tspan9 Induces EMT and Promotes Osteosarcoma Metastasis via Activating FAK-Ras-ERK1/2 Pathway.. *Frontiers in oncology*. PMID: 35280793

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 66.9% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 93.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018499, IPR000301, IPR018503, IPR008952; Pfam: PF00335 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD9 | 0.761 | 0.510 | — |
| TSPAN32 | 0.715 | 0.000 | — |
| GP6 | 0.614 | 0.126 | — |
| ITGB1 | 0.603 | 0.000 | — |
| CD151 | 0.527 | 0.000 | — |
| CD63 | 0.515 | 0.000 | — |
| TSPAN15 | 0.493 | 0.292 | — |
| CTDSPL | 0.466 | 0.000 | — |
| SAMD14 | 0.446 | 0.000 | — |
| VWCE | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EVA1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000011898 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |
| TSC22D3 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 无 | pLDDT=89.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Golgi apparatus; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSPAN9 — Tetraspanin-9，非常新颖，仅有少数基础研究。
2. 蛋白大小239 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75954
- Protein Atlas: https://www.proteinatlas.org/ENSG00000011105-TSPAN9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPAN9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75954
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000011105-TSPAN9/subcellular

![](https://images.proteinatlas.org/14002/105_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/14002/105_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/14002/107_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/14002/107_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/14002/1587_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/14002/1587_D2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75954-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
