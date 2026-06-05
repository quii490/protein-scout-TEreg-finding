---
type: protein-evaluation
gene: "PLAAT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLAAT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLAAT1 / HRASLS |
| 蛋白名称 | Phospholipase A and acyltransferase 1 |
| 蛋白大小 | 168 aa / 18.8 kDa |
| UniProt ID | Q9HDD0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Focal adhesion sites; 额外: Cytosol; UniProt: Membrane; Cytoplasm; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 168 aa / 18.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051496, IPR007053; Pfam: PF04970 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites; 额外: Cytosol | Approved |
| UniProt | Membrane; Cytoplasm; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- lysosome (GO:0005764)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- nuclear envelope lumen (GO:0005641)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HRASLS |

**关键文献**:
1. The PLAAT family as phospholipid-related enzymes.. *Progress in lipid research*. PMID: 40074088
2. PLAAT1 Exhibits Phosphatidylcholine:Monolysocardiolipin Transacylase Activity.. *International journal of molecular sciences*. PMID: 35743156
3. Gene loss and relaxed selection of plaat1 in vertebrates adapted to low-light environments.. *Proceedings. Biological sciences*. PMID: 38864338
4. Gene loss and relaxed selection of plaat1 in vertebrates adapted to low-light environments.. *bioRxiv : the preprint server for biology*. PMID: 38168154
5. Plaat1 deficiency reduces cardiac cardiolipin content and impairs exercise tolerance.. *Journal of lipid research*. PMID: 40345663

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 29.2% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.9，有序区 55.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051496, IPR007053; Pfam: PF04970 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC5 | 0.757 | 0.641 | — |
| CRABP2 | 0.717 | 0.000 | — |
| CLPB | 0.679 | 0.402 | — |
| RARG | 0.668 | 0.129 | — |
| RARB | 0.628 | 0.129 | — |
| ALKBH7 | 0.614 | 0.610 | — |
| LRATD2 | 0.595 | 0.000 | — |
| HRAS | 0.591 | 0.053 | — |
| GRPEL2 | 0.588 | 0.306 | — |
| GRPEL1 | 0.588 | 0.306 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TLX3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HGS | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZIC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPANK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DNAAF19 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBQLN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HIDE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ALKBH7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DNAJC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 无 | pLDDT=71.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Nucleus; Cytoplasm / Focal adhesion sites; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLAAT1 — Phospholipase A and acyltransferase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小168 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HDD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127252-PLAAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLAAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HDD0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (approved)。来源: https://www.proteinatlas.org/ENSG00000127252-PLAAT1/subcellular

![](https://images.proteinatlas.org/51179/821_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51179/821_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51179/831_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51179/831_F6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51179/882_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51179/882_F6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HDD0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
