---
type: protein-evaluation
gene: "WDR36"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR36 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR36 |
| 蛋白名称 | WD repeat-containing protein 36 |
| 蛋白大小 | 895 aa / 99.4 kDa |
| UniProt ID | Q8NI36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 895 aa / 99.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.4; PDB: 7MQ8, 7MQ9, 7MQA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR019775, IPR036322, IPR001680, IPR059 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- Pwp2p-containing subcomplex of 90S preribosome (GO:0034388)
- small-subunit processome (GO:0032040)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 98 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. WDR36 and P53 gene variants and susceptibility to primary open-angle glaucoma: analysis of gene-gene interactions.. *Investigative ophthalmology & visual science*. PMID: 21931130
2. Association of WDR36 polymorphisms with primary open angle glaucoma: A systematic review and meta-analysis.. *Medicine*. PMID: 28658128
3. WDR36 Regulates Trophectoderm Differentiation During Human Preimplantation Embryonic Development Through Glycolytic Metabolism.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39656902
4. Advances in glaucoma genetics.. *Progress in brain research*. PMID: 26497787
5. WDR36 Safeguards Self-Renewal and Pluripotency of Human Extended Pluripotent Stem Cells.. *Frontiers in genetics*. PMID: 35937980

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 65.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7MQ8, 7MQ9, 7MQA）+ AlphaFold高质量预测（pLDDT=87.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR019775, IPR036322, IPR001680, IPR059157; Pfam: PF25171, PF25168, PF04192 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP15 | 0.999 | 0.993 | — |
| WDR75 | 0.999 | 0.981 | — |
| UTP4 | 0.999 | 0.991 | — |
| HEATR1 | 0.999 | 0.991 | — |
| UTP6 | 0.999 | 0.992 | — |
| NOP56 | 0.999 | 0.993 | — |
| DCAF13 | 0.999 | 0.993 | — |
| BYSL | 0.999 | 0.991 | — |
| NGDN | 0.999 | 0.987 | — |
| KRR1 | 0.999 | 0.993 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| G3BP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| G3BP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SH3GLB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ESR1 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13780|pubmed:21182205 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=87.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WDR36 — WD repeat-containing protein 36，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小895 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NI36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134987-WDR36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NI36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000134987-WDR36/subcellular

![](https://images.proteinatlas.org/37796/565_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37796/565_C8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37796/570_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37796/584_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37796/584_C8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NI36-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NI36 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR019775;IPR036322;IPR001680;IPR059157;IPR007319; |
| Pfam | PF25171;PF25168;PF04192; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134987-WDR36/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AATF | Biogrid | false |
| ADARB1 | Biogrid | false |
| ANLN | Biogrid | false |
| BRD4 | Biogrid | false |
| CCNF | Biogrid | false |
| ESR1 | Biogrid | false |
| FBL | Biogrid | false |
| G3BP2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
