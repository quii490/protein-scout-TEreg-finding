---
type: protein-evaluation
gene: "NPHP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPHP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPHP4 / KIAA0673 |
| 蛋白名称 | Nephrocystin-4 |
| 蛋白大小 | 1426 aa / 157.6 kDa |
| UniProt ID | O75161 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Vesicles, Cytosol; UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytos |
| 蛋白大小 | 5/10 | ×1 | 5 | 1426 aa / 157.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=93 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR058687, IPR058688, IPR058686, IPR058685, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Vesicles, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923)
- cell-cell junction (GO:0005911)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- ciliary transition zone (GO:0035869)
- cytosol (GO:0005829)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 93 |
| PubMed broad count | 140 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0673 |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Variable phenotypes and penetrance between and within different zebrafish ciliary transition zone mutants.. *Disease models & mechanisms*. PMID: 36533556
3. Combining a prioritization strategy and functional studies nominates 5'UTR variants underlying inherited retinal disease.. *Genome medicine*. PMID: 38184646
4. NPHP4, a cilia-associated protein, negatively regulates the Hippo pathway.. *The Journal of cell biology*. PMID: 21555462
5. NPHP4 controls ciliary trafficking of membrane proteins and large soluble proteins at the transition zone.. *Journal of cell science*. PMID: 25150219

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.3 |
| 高置信度残基 (pLDDT>90) 占比 | 15.7% |
| 置信残基 (pLDDT 70-90) 占比 | 50.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 21.7% |
| 有序区域 (pLDDT>70) 占比 | 66.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.3，有序区 66.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR058687, IPR058688, IPR058686, IPR058685, IPR029775; Pfam: PF26015, PF26190, PF26189 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPGRIP1L | 0.999 | 0.767 | — |
| NPHP1 | 0.999 | 0.840 | — |
| RPGRIP1 | 0.997 | 0.687 | — |
| NPHP3 | 0.983 | 0.000 | — |
| CEP290 | 0.976 | 0.061 | — |
| TMEM67 | 0.969 | 0.000 | — |
| RPGR | 0.966 | 0.637 | — |
| INVS | 0.959 | 0.141 | — |
| IQCB1 | 0.953 | 0.095 | — |
| BCAR1 | 0.941 | 0.311 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000080128.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| ENSP00000367398.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |
| Nphp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Tuba1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Hspa1a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Hspa8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Thrap3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Rcn2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.3 + PDB: 无 | pLDDT=71.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium basal body; Cytopl / Nucleoplasm; 额外: Nuclear bodies, Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. NPHP4 — Nephrocystin-4，研究基础较多，新颖性有限。
2. 蛋白大小1426 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 93 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75161
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131697-NPHP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPHP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75161
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000131697-NPHP4/subcellular

![](https://images.proteinatlas.org/63852/1265_F2_4_red_green.jpg)
![](https://images.proteinatlas.org/63852/1265_F2_5_red_green.jpg)
![](https://images.proteinatlas.org/63852/1274_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/63852/1274_F2_4_red_green.jpg)
![](https://images.proteinatlas.org/63852/1282_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/63852/1282_G5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75161-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
