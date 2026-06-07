---
type: protein-evaluation
gene: "SYTL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYTL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYTL3 / SLP3 |
| 蛋白名称 | Synaptotagmin-like protein 3 |
| 蛋白大小 | 610 aa / 68.6 kDa |
| UniProt ID | Q4VX76 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Vesicles; UniProt: Endomembrane system |
| 蛋白大小 | 10/10 | ×1 | 10 | 610 aa / 68.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR041282, IPR010911, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Vesicles | Approved |
| UniProt | Endomembrane system | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- exocytic vesicle (GO:0070382)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SLP3 |

**关键文献**:
1. Transcriptional and Immune Landscape of Cardiac Sarcoidosis.. *Circulation research*. PMID: 36111531
2. SYTL3-SLC22A3 Single-Nucleotide Polymorphisms and Gene-Gene/Environment Interactions on the Risk of Hyperlipidemia.. *Frontiers in genetics*. PMID: 34367243
3. Transcriptional networks identify synaptotagmin-like 3 as a regulator of cortical neuronal migration during early neurodevelopment.. *Cell reports*. PMID: 33657377
4. Assessment of gene signatures following the inhibition of IL-23: a study to evaluate the mechanistic effects behind the clinical efficacy of guselkumab in patients with psoriatic arthritis.. *Frontiers in immunology*. PMID: 40963613
5. Effect of SYTL3-SLC22A3 Variants, Their Haplotypes, and G × E Interactions on Serum Lipid Levels and the Risk of Coronary Artery Disease and Ischaemic Stroke.. *Frontiers in cardiovascular medicine*. PMID: 34458338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.1 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 62.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.1，有序区 62.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR041282, IPR010911, IPR043567; Pfam: PF00168, PF02318 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB27A | 0.957 | 0.809 | — |
| RAB27B | 0.848 | 0.701 | — |
| STXBP2 | 0.661 | 0.000 | — |
| RAB3A | 0.630 | 0.045 | — |
| STX3 | 0.628 | 0.091 | — |
| TMEM154 | 0.594 | 0.000 | — |
| VAMP8 | 0.586 | 0.073 | — |
| UNC13D | 0.547 | 0.000 | — |
| MYO5A | 0.513 | 0.000 | — |
| TMEM38A | 0.502 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rab27a | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11773082 |
| Nrxn1 | psi-mi:"MI:0096"(pull down) | pubmed:11243866 |
| barA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| OAZ2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ANKRD11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RAB27B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.1 + PDB: 无 | pLDDT=71.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endomembrane system / Nucleoli fibrillar center, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. SYTL3 — Synaptotagmin-like protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小610 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4VX76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164674-SYTL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYTL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4VX76
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000164674-SYTL3/subcellular

![](https://images.proteinatlas.org/30586/402_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30586/402_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30586/405_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30586/405_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30586/409_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30586/409_B8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4VX76-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4VX76 |
| SMART | SM00239; |
| UniProt Domain [FT] | DOMAIN 4..123; /note="RabBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00234"; DOMAIN 306..428; /note="C2 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 462..603; /note="C2 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041" |
| InterPro | IPR000008;IPR035892;IPR041282;IPR010911;IPR043567;IPR011011;IPR013083; |
| Pfam | PF00168;PF02318; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164674-SYTL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAB27A | Intact, Biogrid, Bioplex | true |
| OAZ2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
