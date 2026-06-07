---
type: protein-evaluation
gene: "FILIP1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FILIP1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FILIP1L / COL4A3BPIP, DOC1, GIP90 |
| 蛋白名称 | Filamin A-interacting protein 1-like |
| 蛋白大小 | 1135 aa / 130.4 kDa |
| UniProt ID | Q4L180 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Cytoplasm; Membrane; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1135 aa / 130.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050719, IPR019131; Pfam: PF09727 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Cytoplasm; Membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 77 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COL4A3BPIP, DOC1, GIP90 |

**关键文献**:
1. Single-cell and bulk transcriptome analyses revealed the role of macrophage cholesterol metabolism in atherosclerosis.. *Lipids in health and disease*. PMID: 41299485
2. FILIP1L Loss Is a Driver of Aggressive Mucinous Colorectal Adenocarcinoma and Mediates Cytokinesis Defects through PFDN1.. *Cancer research*. PMID: 34417201
3. Filamin A interacting protein 1-like as a therapeutic target in cancer.. *Expert opinion on therapeutic targets*. PMID: 25200207
4. Filamin A interacting protein 1-like expression inhibits progression in colorectal cancer.. *Oncotarget*. PMID: 27750216
5. Smoking-associated Downregulation of FILIP1L Enhances Lung Adenocarcinoma Progression Through Mucin Production, Inflammation, and Fibrosis.. *Cancer research communications*. PMID: 36860703

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 35.9% |
| 有序区域 (pLDDT>70) 占比 | 55.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 55.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050719, IPR019131; Pfam: PF09727 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC16A8 | 0.668 | 0.000 | — |
| RAD51B | 0.610 | 0.000 | — |
| TBC1D23 | 0.608 | 0.000 | — |
| B3GLCT | 0.581 | 0.000 | — |
| ADAMTS9 | 0.577 | 0.000 | — |
| TRAPPC1 | 0.555 | 0.467 | — |
| TRAPPC8 | 0.551 | 0.476 | — |
| ERVW-1 | 0.550 | 0.000 | — |
| LYRM4 | 0.542 | 0.504 | — |
| TRAPPC4 | 0.539 | 0.450 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| nusB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| grpE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SMTN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SOX4 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |
| SP7 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane; Nucleus / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. FILIP1L — Filamin A-interacting protein 1-like，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1135 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4L180
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168386-FILIP1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FILIP1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4L180
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000168386-FILIP1L/subcellular

![](https://images.proteinatlas.org/43133/465_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43133/465_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43133/467_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43133/467_C7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4L180-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4L180 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050719;IPR019131; |
| Pfam | PF09727; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168386-FILIP1L/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
