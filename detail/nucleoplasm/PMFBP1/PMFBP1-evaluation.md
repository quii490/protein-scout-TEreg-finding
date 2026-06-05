---
type: protein-evaluation
gene: "PMFBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PMFBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PMFBP1 |
| 蛋白名称 | Polyamine-modulated factor 1-binding protein 1 |
| 蛋白大小 | 1007 aa / 117.5 kDa |
| UniProt ID | Q8TBY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Connecting piece; 额外: Cell Junctions, Acrosome,; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 8/10 | ×1 | 8 | 1007 aa / 117.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037391 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Connecting piece; 额外: Cell Junctions, Acrosome, Flagellar centriole, Mid piece, Principal piece | Uncertain |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- sperm flagellum (GO:0036126)
- sperm head (GO:0061827)
- sperm head-tail coupling apparatus (GO:0120212)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. Whole-genome sequencing identifies new candidate genes for nonobstructive azoospermia.. *Andrology*. PMID: 36017582
3. BmPMFBP1 regulates the development of eupyrene sperm in the silkworm, Bombyx mori.. *PLoS genetics*. PMID: 35312700
4. A homozygous loss-of-function mutation in CEP250 is associated with acephalic spermatozoa syndrome in humans.. *Andrology*. PMID: 39726222
5. Biallelic mutations in PMFBP1 cause acephalic spermatozoa.. *Clinical genetics*. PMID: 30298696

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 28.1% |
| 置信残基 (pLDDT 70-90) 占比 | 48.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 14.3% |
| 有序区域 (pLDDT>70) 占比 | 76.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.4，有序区 76.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037391 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUN5 | 0.804 | 0.079 | — |
| TSGA10 | 0.731 | 0.107 | — |
| SPATA6 | 0.655 | 0.000 | — |
| PMF1 | 0.626 | 0.000 | — |
| CEP112 | 0.623 | 0.000 | — |
| PMF1-BGLAP | 0.621 | 0.000 | — |
| SPATC1L | 0.580 | 0.000 | — |
| HOOK1 | 0.575 | 0.000 | — |
| MTUS1 | 0.570 | 0.090 | — |
| BRDT | 0.570 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| proV2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| recN | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RPL15 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLC25A5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| MKLN1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MMADHC | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| AAMP | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLTCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 无 | pLDDT=77.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Nucleoplasm, Connecting piece; 额外: Cell Junctions, | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. PMFBP1 — Polyamine-modulated factor 1-binding protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1007 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118557-PMFBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PMFBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000118557-PMFBP1/subcellular

![](https://images.proteinatlas.org/75825/2215_C7_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/75825/2215_C7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/75825/1835_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/75825/1835_C3_4_red_green.jpg)
![](https://images.proteinatlas.org/75825/1901_I14_1_red_green.jpg)
![](https://images.proteinatlas.org/75825/1901_I14_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TBY8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
