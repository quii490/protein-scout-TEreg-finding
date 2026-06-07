---
type: protein-evaluation
gene: "MACROD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MACROD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MACROD1 / LRP16 |
| 蛋白名称 | ADP-ribose glycohydrolase MACROD1 |
| 蛋白大小 | 325 aa / 35.5 kDa |
| UniProt ID | Q9BQ69 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 325 aa / 35.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.3; PDB: 2X47, 6LH4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002589, IPR043472; Pfam: PF01661 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LRP16 |

**关键文献**:
1. Are PARPs promiscuous?. *Bioscience reports*. PMID: 35380161
2. Cardiomyocyte mitochondrial mono-ADP-ribosylation dictates cardiac tolerance to sepsis by configuring bioenergetic reserve in male mice.. *Nature communications*. PMID: 40885706
3. Comparative analysis of MACROD1, MACROD2 and TARG1 expression, localisation and interactome.. *Scientific reports*. PMID: 32427867
4. The Controversial Roles of ADP-Ribosyl Hydrolases MACROD1, MACROD2 and TARG1 in Carcinogenesis.. *Cancers*. PMID: 32151005
5. Behavioural Characterisation of Macrod1 and Macrod2 Knockout Mice.. *Cells*. PMID: 33578760

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 19.7% |
| 有序区域 (pLDDT>70) 占比 | 72.3% |
| 可用 PDB 条目 | 2X47, 6LH4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2X47, 6LH4）+ AlphaFold高质量预测（pLDDT=82.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002589, IPR043472; Pfam: PF01661 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARP1 | 0.868 | 0.757 | — |
| OARD1 | 0.850 | 0.000 | — |
| ADPRHL2 | 0.839 | 0.000 | — |
| PARG | 0.822 | 0.000 | — |
| ESR1 | 0.818 | 0.510 | — |
| MACROH2A2 | 0.728 | 0.000 | — |
| UXT | 0.723 | 0.292 | — |
| NUDT16 | 0.691 | 0.000 | — |
| PARP2 | 0.689 | 0.363 | — |
| PARP10 | 0.672 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| KRT18 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26365|pubmed:20035625 |
| ESR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-26365|pubmed:20035625 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| EXOC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HBE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PARP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 2X47, 6LH4 | pLDDT=82.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MACROD1 — ADP-ribose glycohydrolase MACROD1，非常新颖，仅有少数基础研究。
2. 蛋白大小325 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ69
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133315-MACROD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MACROD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ69
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MACROD1/IF_images/MACROD1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000133315-MACROD1/subcellular

![](https://images.proteinatlas.org/71075/1409_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/71075/1409_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/71075/1411_E4_4_red_green.jpg)
![](https://images.proteinatlas.org/71075/1411_E4_6_red_green.jpg)
![](https://images.proteinatlas.org/71075/1412_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/71075/1412_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ69-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ69 |
| SMART | SM00506; |
| UniProt Domain [FT] | DOMAIN 141..322; /note="Macro"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00490" |
| InterPro | IPR002589;IPR043472; |
| Pfam | PF01661; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133315-MACROD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PARP1 | Intact, Biogrid, Bioplex | true |
| RELA | Intact, Biogrid | true |
| ESR1 | Intact | false |
| IKBKG | Biogrid | false |
| KPNA1 | Intact | false |
| KRT18 | Intact | false |
| MTHFD2 | Bioplex | false |
| RPA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
