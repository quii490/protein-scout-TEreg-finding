---
type: protein-evaluation
gene: "OSBPL7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL7 / ORP7 |
| 蛋白名称 | Oxysterol-binding protein-related protein 7 |
| 蛋白大小 | 842 aa / 95.4 kDa |
| UniProt ID | Q9BZF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm, cytosol; Endoplasmic reticulum membrane; Cell mem |
| 蛋白大小 | 8/10 | ×1 | 8 | 842 aa / 95.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasm, cytosol; Endoplasmic reticulum membrane; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- perinuclear endoplasmic reticulum (GO:0097038)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORP7 |

**关键文献**:
1. Functional omics of ORP7 in primary endothelial cells.. *BMC biology*. PMID: 39695567
2. Hypercholesterolemia in the Malaysian Cohort Participants: Genetic and Non-Genetic Risk Factors.. *Genes*. PMID: 36980993
3. Oxysterol-binding protein-like 7 deficiency leads to ER stress-mediated apoptosis in podocytes and proteinuria.. *American journal of physiology. Renal physiology*. PMID: 38961844
4. Clinical effects of novel susceptibility genes for beta-amyloid: a gene-based association study in the Korean population.. *Frontiers in aging neuroscience*. PMID: 37901794
5. Compounds targeting OSBPL7 increase ABCA1-dependent cholesterol efflux preserving kidney function in two models of kidney disease.. *Nature communications*. PMID: 34341345

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 20.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 32.2% |
| 有序区域 (pLDDT>70) 占比 | 60.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 60.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041680; Pfam: PF01237, PF15409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAPA | 0.759 | 0.431 | — |
| PLEK2 | 0.666 | 0.000 | — |
| PLEK | 0.663 | 0.000 | — |
| RRAS | 0.590 | 0.069 | — |
| TYW1B | 0.576 | 0.000 | — |
| OSBPL9 | 0.534 | 0.091 | — |
| OSBPL6 | 0.525 | 0.482 | — |
| OSBPL3 | 0.486 | 0.435 | — |
| VAPB | 0.481 | 0.297 | — |
| PRR15L | 0.474 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCDC85C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OSBPL6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OSBPL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VAPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:34524948|imex:IM-30012 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Endoplasmic reticulum membrane / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. OSBPL7 — Oxysterol-binding protein-related protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小842 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006025-OSBPL7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000006025-OSBPL7/subcellular

![](https://images.proteinatlas.org/53083/849_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/53083/849_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/53083/869_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/53083/869_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/53083/885_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/53083/885_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZF2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
