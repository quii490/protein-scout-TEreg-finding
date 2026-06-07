---
type: protein-evaluation
gene: "Nme2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Nme2 — REJECTED (研究热度过高 (PubMed strict=119，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Nme2 / NDK2, NM23B |
| 蛋白名称 | Nucleoside diphosphate kinase B |
| 蛋白大小 | 152 aa / 17.3 kDa |
| UniProt ID | P22392 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cell projection, lamellipodium; Cell pro |
| 蛋白大小 | 8/10 | ×1 | 8 | 152 aa / 17.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=119 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.7; PDB: 1NSK, 1NUE, 3BBB, 3BBC, 3BBF, 7KPF, 8PIE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR034907, IPR036850, IPR001564, IPR023005; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cell projection, lamellipodium; Cell projection, ruffle; Cytoplasm; Cytoplasm, p... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell periphery (GO:0071944)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- lamellipodium (GO:0030027)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 119 |
| PubMed broad count | 1087 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NDK2, NM23B |

**关键文献**:
1. Genetic Influence of the Brain on Muscle Structure: A Mendelian Randomization Study of Sarcopenia.. *Journal of cachexia, sarcopenia and muscle*. PMID: 39535371
2. Histidine Phosphorylation: Protein Kinases and Phosphatases.. *International journal of molecular sciences*. PMID: 39063217
3. NME proteins regulate class switch recombination.. *FEBS letters*. PMID: 30411342
4. The actions of NME1/NDPK-A and NME2/NDPK-B as protein kinases.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 29200201
5. Nuclear functions of NME proteins.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 29058704

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.7 |
| 高置信度残基 (pLDDT>90) 占比 | 98.7% |
| 置信残基 (pLDDT 70-90) 占比 | 0.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.4% |
| 可用 PDB 条目 | 1NSK, 1NUE, 3BBB, 3BBC, 3BBF, 7KPF, 8PIE, 8PYW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1NSK, 1NUE, 3BBB, 3BBC, 3BBF, 7KPF, 8PIE, 8PYW）+ AlphaFold极高置信度预测（pLDDT=97.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034907, IPR036850, IPR001564, IPR023005; Pfam: PF00334 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000426976.2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Ryr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Itgb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pik3r1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Mcf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Ikbkb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| NME3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| H2BC10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CACYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PGRMC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.7 + PDB: 1NSK, 1NUE, 3BBB, 3BBC, 3BBF,  | pLDDT=97.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell projection, lamellipodium / Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. Nme2 — Nucleoside diphosphate kinase B，研究基础较多，新颖性有限。
2. 蛋白大小152 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 119 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 119 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22392
- Protein Atlas: https://www.proteinatlas.org/ENSG00000243678-NME2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Nme2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22392
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000243678-NME2/subcellular

![](https://images.proteinatlas.org/36214/1894_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36214/1894_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36215/1894_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36215/1894_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/80057/2078_H6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/80057/2078_H6_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P22392-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P22392 |
| SMART | SM00562; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034907;IPR036850;IPR001564;IPR023005; |
| Pfam | PF00334; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000243678-NME2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NME1 | Intact, Biogrid | true |
| NME3 | Intact, Biogrid | true |
| NME4 | Intact, Biogrid | true |
| ACLY | Biogrid | false |
| DNM2 | Intact | false |
| DSTN | Biogrid | false |
| ESR1 | Biogrid | false |
| HERC5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
