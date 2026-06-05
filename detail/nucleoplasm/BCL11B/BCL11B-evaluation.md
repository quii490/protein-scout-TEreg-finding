---
type: protein-evaluation
gene: "BCL11B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCL11B — REJECTED (研究热度过高 (PubMed strict=310，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL11B / CTIP2, RIT1 |
| 蛋白名称 | B-cell lymphoma/leukemia 11B |
| 蛋白大小 | 894 aa / 95.5 kDa |
| UniProt ID | Q9C0K0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 894 aa / 95.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=310 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057448, IPR051497, IPR056438, IPR036236, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- neuron projection (GO:0043005)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SWI/SNF complex (GO:0016514)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 310 |
| PubMed broad count | 613 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTIP2, RIT1 |

**关键文献**:
1. International Consensus Classification of acute lymphoblastic leukemia/lymphoma.. *Virchows Archiv : an international journal of pathology*. PMID: 36422706
2. Emerging molecular subtypes and therapies in acute lymphoblastic leukemia.. *Seminars in diagnostic pathology*. PMID: 37120350
3. T-Cell Acute Lymphoblastic Leukemia: Biomarkers and Their Clinical Usefulness.. *Genes*. PMID: 34440292
4. The role of transcription factors in shaping regulatory T cell identity.. *Nature reviews. Immunology*. PMID: 37336954
5. Enhancer Hijacking Drives Oncogenic BCL11B Expression in Lineage-Ambiguous Stem Cell Leukemia.. *Cancer discovery*. PMID: 34103329

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 68.0% |
| 有序区域 (pLDDT>70) 占比 | 20.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.8），有序残基占 20.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057448, IPR051497, IPR056438, IPR036236, IPR013087; Pfam: PF25491, PF00096, PF23611 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NR2F1 | 0.991 | 0.523 | — |
| BCL11A | 0.989 | 0.624 | — |
| SMARCA4 | 0.967 | 0.317 | — |
| ARID1B | 0.966 | 0.053 | — |
| BCL7A | 0.954 | 0.045 | — |
| SMARCA2 | 0.951 | 0.076 | — |
| BRD9 | 0.950 | 0.000 | — |
| SUV39H1 | 0.948 | 0.331 | — |
| HDAC1 | 0.947 | 0.690 | — |
| ACTL6A | 0.947 | 0.073 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| HDAC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| HDAC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| Pag1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:26512138|imex:IM-25616 |
| AIM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23523|pubmed:25665578 |
| Foxp3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24578|pubmed:21875956 |
| ENSMUSP00000068258.5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24578|pubmed:21875956 |
| Tnik | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Fmr1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| RBBP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.8 + PDB: 无 | pLDDT=50.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BCL11B — B-cell lymphoma/leukemia 11B，研究基础较多，新颖性有限。
2. 蛋白大小894 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 310 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 310 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0K0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127152-BCL11B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL11B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0K0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000127152-BCL11B/subcellular

![](https://images.proteinatlas.org/49117/1353_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/49117/1353_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/49117/1363_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/49117/1363_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/49117/1421_G3_5_red_green.jpg)
![](https://images.proteinatlas.org/49117/1421_G3_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C0K0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
