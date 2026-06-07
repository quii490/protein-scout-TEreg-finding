---
type: protein-evaluation
gene: "FBXO33"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO33 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO33 / FBX33 |
| 蛋白名称 | F-box only protein 33 |
| 蛋白大小 | 555 aa / 62.6 kDa |
| UniProt ID | Q7Z6M2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 555 aa / 62.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX33 |

**关键文献**:
1. Lactylation-driven transcriptional activation of FBXO33 promotes gallbladder cancer metastasis by regulating p53 polyubiquitination.. *Cell death & disease*. PMID: 40021626
2. Identification of hypertrophy-modulating Cullin-RING ubiquitin ligases in primary cardiomyocytes.. *Frontiers in physiology*. PMID: 36969608
3. The Ubiquitin E3 Ligase FBXO33 Suppresses Stem Cell-Like Properties and Metastasis in Non-Small-Cell Lung Cancer by Promoting Ubiquitination and Degradation of Myc.. *Frontiers in bioscience (Landmark edition)*. PMID: 39206900
4. FipoQ/FBXO33, a Cullin-1-based ubiquitin ligase complex component modulates ubiquitination and solubility of polyglutamine disease protein.. *Journal of neurochemistry*. PMID: 30685895
5. [Analysis of genes related to hypothyroidism during pregnancy].. *Zhonghua yi xue za zhi*. PMID: 31715674

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.7 |
| 高置信度残基 (pLDDT>90) 占比 | 62.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.7，有序区 76.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.925 | 0.707 | — |
| RNH1 | 0.826 | 0.000 | — |
| SKP1 | 0.736 | 0.455 | — |
| TRIM75P | 0.614 | 0.000 | — |
| FBXO25 | 0.592 | 0.000 | — |
| YBX1 | 0.582 | 0.452 | — |
| LRFN5 | 0.557 | 0.000 | — |
| LRRC29 | 0.528 | 0.000 | — |
| WDR47 | 0.521 | 0.000 | — |
| AMN1 | 0.510 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARL4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SKP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| YBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CHCHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000298097 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.7 + PDB: 无 | pLDDT=81.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO33 — F-box only protein 33，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小555 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6M2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165355-FBXO33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6M2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165355-FBXO33/subcellular

![](https://images.proteinatlas.org/46657/696_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/46657/696_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/46657/713_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/46657/713_D4_4_red_green.jpg)
![](https://images.proteinatlas.org/46657/714_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/46657/714_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z6M2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z6M2 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 65..111; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR032675; |
| Pfam | PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165355-FBXO33/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL1 | Intact, Biogrid | true |
| SKP1 | Intact, Biogrid, Bioplex | true |
| YBX1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
