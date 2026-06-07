---
type: protein-evaluation
gene: "STAT2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT2 — REJECTED (研究热度过高 (PubMed strict=1134，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT2 |
| 蛋白名称 | Signal transducer and activator of transcription 2 |
| 蛋白大小 | 851 aa / 97.9 kDa |
| UniProt ID | P52630 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Mid piece; 额外: Plasma membrane, Principal piece; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 851 aa / 97.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1134 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.8; PDB: 2KA4, 6UX2, 6WCZ, 8T12, 8T13 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR022 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Mid piece; 额外: Plasma membrane, Principal piece | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- ISGF3 complex (GO:0070721)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1134 |
| PubMed broad count | 1806 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pyruvate is a natural suppressor of interferon signaling by inducing STAT1 protein pyruvylation.. *Cell*. PMID: 41763198
2. LGR6 protects against myocardial ischemia-reperfusion injury via suppressing necroptosis.. *Redox biology*. PMID: 39471639
3. STAT dynamics.. *Cytokine & growth factor reviews*. PMID: 17683973
4. IL-20 controls resolution of experimental colitis by regulating epithelial IFN/STAT2 signalling.. *Gut*. PMID: 37884352
5. The Fibrillin-1/VEGFR2/STAT2 signaling axis promotes chemoresistance via modulating glycolysis and angiogenesis in ovarian cancer organoids and cells.. *Cancer communications (London, England)*. PMID: 35234370

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 47.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 20.0% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 2KA4, 6UX2, 6WCZ, 8T12, 8T13 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2KA4, 6UX2, 6WCZ, 8T12, 8T13）+ AlphaFold极高置信度预测（pLDDT=77.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR022756; Pfam: PF00017, PF12188, PF01017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IFNAR1 | 0.999 | 0.835 | — |
| IRF9 | 0.999 | 0.894 | — |
| STAT1 | 0.999 | 0.886 | — |
| TYK2 | 0.998 | 0.634 | — |
| IFNAR2 | 0.997 | 0.820 | — |
| CREBBP | 0.997 | 0.960 | — |
| JAK1 | 0.996 | 0.285 | — |
| STAT6 | 0.991 | 0.292 | — |
| JAK2 | 0.991 | 0.285 | — |
| JAK3 | 0.982 | 0.285 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32838362|imex:IM-27901| |
| PIAS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| P | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:20089657|imex:IM-28090 |
| Q82983 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15242592|imex:IM-28164 |
| DDX39B | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RUFY1 | psi-mi:"MI:0096"(pull down) | imex:IM-15364|pubmed:21988832 |
| SUMO1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ADA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| C1QA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 2KA4, 6UX2, 6WCZ, 8T12, 8T13 | pLDDT=77.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol, Mid piece; 额外: Plasma membrane, Principal | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STAT2 — Signal transducer and activator of transcription 2，研究基础较多，新颖性有限。
2. 蛋白大小851 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1134 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1134 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52630
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170581-STAT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52630
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000170581-STAT2/subcellular

![](https://images.proteinatlas.org/18888/155_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/155_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/199_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/199_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/2013_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/2013_A5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52630-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P52630 |
| SMART | SM00252;SM00964; |
| UniProt Domain [FT] | DOMAIN 572..667; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191" |
| InterPro | IPR008967;IPR000980;IPR036860;IPR001217;IPR022756;IPR035854;IPR048988;IPR036535;IPR013800;IPR015988;IPR013801;IPR012345;IPR013799; |
| Pfam | PF00017;PF12188;PF01017;PF02864;PF02865;PF21354; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170581-STAT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Intact, Biogrid | true |
| IFNAR2 | Intact, Biogrid | true |
| IRF9 | Intact, Biogrid, Bioplex | true |
| STAT1 | Intact, Biogrid | true |
| CREBBP | Biogrid | false |
| DCST1 | Biogrid | false |
| DOK4 | Intact | false |
| EP300 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
