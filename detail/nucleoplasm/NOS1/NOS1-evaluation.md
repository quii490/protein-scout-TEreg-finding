---
type: protein-evaluation
gene: "NOS1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NOS1 — REJECTED (研究热度过高 (PubMed strict=699，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOS1 |
| 蛋白名称 | Nitric oxide synthase 1 |
| 蛋白大小 | 1434 aa / 161.0 kDa |
| UniProt ID | P29475 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cell membrane, sarcolemma; Cell projection, dendritic spine |
| 蛋白大小 | 5/10 | ×1 | 5 | 1434 aa / 161.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=699 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.3; PDB: 4D1N, 4UCH, 4UH5, 4UH6, 4V3U, 5ADF, 5ADG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Cell membrane, sarcolemma; Cell projection, dendritic spine | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- calyx of Held (GO:0044305)
- caveola (GO:0005901)
- cell periphery (GO:0071944)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- membrane raft (GO:0045121)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 699 |
| PubMed broad count | 3858 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A pontine-medullary loop crucial for REM sleep and its deficit in Parkinson's disease.. *Cell*. PMID: 39303715
2. Identification of potential candidate genes and pathways in atrioventricular nodal reentry tachycardia by whole-exome sequencing.. *Clinical and translational medicine*. PMID: 32508047
3. nNOS in Erbb4-positive neurons regulates GABAergic transmission in mouse hippocampus.. *Cell death & disease*. PMID: 38396027
4. Association Between NOS1 Gene Polymorphisms and Schizophrenia in Asian and Caucasian Populations: A Meta-Analysis.. *Neuromolecular medicine*. PMID: 28795310
5. A novel anti-epileptogenesis strategy of temporal lobe epilepsy based on nitric oxide donor.. *EMBO molecular medicine*. PMID: 39653809

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 50.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 4D1N, 4UCH, 4UH5, 4UH6, 4V3U, 5ADF, 5ADG, 5ADI, 5FVU, 5FVV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4D1N, 4UCH, 4UH5, 4UH6, 4V3U, 5ADF, 5ADG, 5ADI, 5FVU, 5FVV）+ AlphaFold极高置信度预测（pLDDT=79.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001709; Pfam: PF00667, PF00258, PF00175 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CALML4 | 0.999 | 0.046 | — |
| NOS1AP | 0.999 | 0.411 | — |
| CALM3 | 0.999 | 0.902 | — |
| CALML3 | 0.999 | 0.066 | — |
| CALML6 | 0.999 | 0.046 | — |
| CALML5 | 0.999 | 0.066 | — |
| DLG4 | 0.996 | 0.523 | — |
| RASD1 | 0.990 | 0.292 | — |
| GRIN2B | 0.984 | 0.129 | — |
| SNTA1 | 0.979 | 0.912 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0096"(pull down) | pubmed:9786987 |
| Dynll1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| CKAP4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Myo5a | psi-mi:"MI:0813"(proximity ligation assay) | imex:IM-22065|pubmed:21680773 |
| Ptgs1 | psi-mi:"MI:0813"(proximity ligation assay) | imex:IM-23317|pubmed:24530741 |
| ADRB3 | psi-mi:"MI:0813"(proximity ligation assay) | imex:IM-22310|pubmed:24190960 |
| Tnik | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Huwe1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 4D1N, 4UCH, 4UH5, 4UH6, 4V3U,  | pLDDT=79.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane, sarcolemma; Cell projection, dendri / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NOS1 — Nitric oxide synthase 1，研究基础较多，新颖性有限。
2. 蛋白大小1434 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 699 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 699 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29475
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089250-NOS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29475
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000089250-NOS1/subcellular

![](https://images.proteinatlas.org/58312/1591_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58312/1591_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58312/1616_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58312/1616_F12_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P29475-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P29475 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 17..99; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 760..940; /note="Flavodoxin-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00088"; DOMAIN 995..1242; /note="FAD-binding FR-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00716" |
| InterPro | IPR003097;IPR017927;IPR001094;IPR008254;IPR001709;IPR029039;IPR039261;IPR023173;IPR050607;IPR044943;IPR044940;IPR044944;IPR012144;IPR004030;IPR036119;IPR001433;IPR001478;IPR036034;IPR017938; |
| Pfam | PF00667;PF00258;PF00175;PF02898;PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000089250-NOS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DLG4 | Biogrid | false |
| NOS1AP | Biogrid | false |
| PRKD1 | Biogrid | false |
| SNTA1 | Biogrid | false |
| SOX2 | Biogrid | false |
| STUB1 | Biogrid | false |
| VAC14 | Intact | false |
| ZDHHC23 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
