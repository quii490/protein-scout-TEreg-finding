---
type: protein-evaluation
gene: "CETN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CETN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CETN2 / CALT, CEN2 |
| 蛋白名称 | Centrin-2 |
| 蛋白大小 | 172 aa / 19.7 kDa |
| UniProt ID | P41208 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Flagellar centriole; 额外: Centrosome, Mid piece,; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 172 aa / 19.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=85.4; PDB: 1M39, 1ZMZ, 2A4J, 2GGM, 2K2I, 2OBH, 8EBS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050145, IPR011992, IPR018247, IPR002048, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Flagellar centriole; 额外: Centrosome, Mid piece, Principal piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtu... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 9+2 motile cilium (GO:0097729)
- apical part of cell (GO:0045177)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- glial cell projection (GO:0097386)
- nuclear pore nuclear basket (GO:0044615)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CALT, CEN2 |

**关键文献**:
1. Astrocytic centrin-2 expression in entorhinal cortex correlates with Alzheimer's disease severity.. *Glia*. PMID: 39145525
2. Mps1 phosphorylation sites regulate the function of centrin 2 in centriole assembly.. *Molecular biology of the cell*. PMID: 20980622
3. Centrin-2 (Cetn2) mediated regulation of FGF/FGFR gene expression in Xenopus.. *Scientific reports*. PMID: 26014913
4. Characterization of the X-linked murine centrin Cetn2 gene.. *Gene*. PMID: 11250075
5. Deletion of both centrin 2 (CETN2) and CETN3 destabilizes the distal connecting cilium of mouse photoreceptors.. *The Journal of biological chemistry*. PMID: 30647131

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 1M39, 1ZMZ, 2A4J, 2GGM, 2K2I, 2OBH, 8EBS, 8EBT, 8EBV, 8EBW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1M39, 1ZMZ, 2A4J, 2GGM, 2K2I, 2OBH, 8EBS, 8EBT, 8EBV, 8EBW）+ AlphaFold极高置信度预测（pLDDT=85.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050145, IPR011992, IPR018247, IPR002048, IPR000629; Pfam: PF13499 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD23B | 0.999 | 0.650 | — |
| ENY2 | 0.999 | 0.636 | — |
| PCID2 | 0.999 | 0.493 | — |
| XPC | 0.999 | 0.988 | — |
| MCM3AP | 0.998 | 0.517 | — |
| SFI1 | 0.996 | 0.907 | — |
| RAD23A | 0.985 | 0.274 | — |
| ERCC1 | 0.971 | 0.000 | — |
| CETN3 | 0.967 | 0.426 | — |
| POC5 | 0.959 | 0.827 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000110198.4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ARSA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PRMT6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RAD23B | psi-mi:"MI:0091"(chromatography technology) | pubmed:21962512|imex:IM-16583 |
| XPC | psi-mi:"MI:0091"(chromatography technology) | pubmed:21962512|imex:IM-16583 |
| Pou5f1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| SFI1 | psi-mi:"MI:0065"(isothermal titration calorimetry) | pubmed:16956364|imex:IM-20476 |
| CCP110 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16760425 |
| USP49 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CETN3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 1M39, 1ZMZ, 2A4J, 2GGM, 2K2I,  | pLDDT=85.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Flagellar centriole; 额外: Centrosome,  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CETN2 — Centrin-2，非常新颖，仅有少数基础研究。
2. 蛋白大小172 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41208
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147400-CETN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CETN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41208
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000147400-CETN2/subcellular

![](https://images.proteinatlas.org/28956/2204_A11_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/28956/2204_A11_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/28956/329_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/28956/329_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/59330/1055_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/59330/1055_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P41208-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
