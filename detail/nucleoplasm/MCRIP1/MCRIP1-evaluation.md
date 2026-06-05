---
type: protein-evaluation
gene: "MCRIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MCRIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MCRIP1 / FAM195B, GRAN2 |
| 蛋白名称 | Mapk-regulated corepressor-interacting protein 1 |
| 蛋白大小 | 97 aa / 10.9 kDa |
| UniProt ID | C9JLW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm, Stress granule |
| 蛋白大小 | 5/10 | ×1 | 5 | 97 aa / 10.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029428; Pfam: PF14799 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM195B, GRAN2 |

**关键文献**:
1. MCRIP1 promotes the expression of lung-surfactant proteins in mice by disrupting CtBP-mediated epigenetic gene silencing.. *Communications biology*. PMID: 31240265
2. MCRIP1, an ERK substrate, mediates ERK-induced gene silencing during epithelial-mesenchymal transition by regulating the co-repressor CtBP.. *Molecular cell*. PMID: 25728771
3. Fecal microbiota transplantation alleviates experimental colitis through the Toll-like receptor 4 signaling pathway.. *World journal of gastroenterology*. PMID: 37662857
4. Shear Stress Markedly Alters the Proteomic Response to Hypoxia in Human Pulmonary Endothelial Cells.. *American journal of respiratory cell and molecular biology*. PMID: 36730645

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 32.0% |
| 中等置信 (pLDDT 50-70) 占比 | 40.2% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 55.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.4，有序区 55.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029428; Pfam: PF14799 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LSM12 | 0.720 | 0.616 | — |
| SAYSD1 | 0.616 | 0.000 | — |
| DHRS7C | 0.606 | 0.000 | — |
| NUTM2G | 0.514 | 0.000 | — |
| DDX6 | 0.490 | 0.374 | — |
| DNAH8 | 0.472 | 0.000 | — |
| UBAP2L | 0.464 | 0.410 | — |
| ILF2 | 0.453 | 0.000 | — |
| KHSRP | 0.443 | 0.000 | — |
| KRTAP9-1 | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ARHGAP27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PPP1R16B | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PTPRH | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| TNFRSF10A | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| LSM12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLF3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:36931259|imex:IM-29717 |
| CEP135 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:35709258|imex:IM-29848 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 1 / 14 = 7%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 无 | pLDDT=75.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, Stress granule / Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

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
1. MCRIP1 — Mapk-regulated corepressor-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小97 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9JLW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000225663-MCRIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MCRIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9JLW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000225663-MCRIP1/subcellular

![](https://images.proteinatlas.org/45542/742_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45542/742_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45542/765_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45542/765_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45542/771_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45542/771_B4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9JLW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
