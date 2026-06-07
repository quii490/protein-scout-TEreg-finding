---
type: protein-evaluation
gene: "LMO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LMO2 — REJECTED (研究热度过高 (PubMed strict=450，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMO2 / RBTN2, RBTNL1, RHOM2, TTG2 |
| 蛋白名称 | Rhombotin-2 |
| 蛋白大小 | 158 aa / 18.4 kDa |
| UniProt ID | P25791 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 158 aa / 18.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=450 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.4; PDB: 2XJY, 2XJZ, 2YPA, 4KFZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050945, IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 450 |
| PubMed broad count | 734 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RBTN2, RBTNL1, RHOM2, TTG2 |

**关键文献**:
1. Follicular lymphoma comprises germinal center-like and memory-like molecular subtypes with prognostic significance.. *Blood*. PMID: 39374535
2. LDB1 establishes multi-enhancer networks to regulate gene expression.. *Molecular cell*. PMID: 39721581
3. Biologic and Clinical Analysis of Childhood Gamma Delta T-ALL Identifies LMO2/STAG2 Rearrangements as Extremely High Risk.. *Cancer discovery*. PMID: 38916500
4. HOXA9 Regulome and Pharmacological Interventions in Leukemia.. *Advances in experimental medicine and biology*. PMID: 39017854
5. Chromogenic LMO2 mRNA ISH Expression Correlates with LMO2 Protein and Gene Expression and Captures Their Survival Impact in Diffuse Large B-Cell Lymphoma, NOS.. *Cancers*. PMID: 39001439

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 75.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 1.9% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 2XJY, 2XJZ, 2YPA, 4KFZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XJY, 2XJZ, 2YPA, 4KFZ）+ AlphaFold高质量预测（pLDDT=90.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050945, IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LDB1 | 0.999 | 0.980 | — |
| GATA1 | 0.999 | 0.929 | — |
| TAL1 | 0.999 | 0.977 | — |
| LDB2 | 0.998 | 0.166 | — |
| LYL1 | 0.998 | 0.235 | — |
| GATA2 | 0.997 | 0.329 | — |
| TCF3 | 0.996 | 0.090 | — |
| RUNX1 | 0.988 | 0.000 | — |
| TCF12 | 0.978 | 0.902 | — |
| ZFPM1 | 0.973 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000257818.2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MAPRE3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STAT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EHMT2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAPRE2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RELA | psi-mi:"MI:0096"(pull down) | imex:IM-15364|pubmed:21988832 |
| AXIN1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| CDC25A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| STIP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 2XJY, 2XJZ, 2YPA, 4KFZ | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. LMO2 — Rhombotin-2，研究基础较多，新颖性有限。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 450 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 450 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P25791
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135363-LMO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P25791
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135363-LMO2/subcellular

![](https://images.proteinatlas.org/29285/1676_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/29285/1676_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/70901/1398_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/70901/1398_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/70901/1503_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/70901/1503_B4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P25791-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P25791 |
| SMART | SM00132; |
| UniProt Domain [FT] | DOMAIN 30..89; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 94..153; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR050945;IPR001781; |
| Pfam | PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135363-LMO2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABI2 | Intact, Biogrid | true |
| AFDN | Intact, Biogrid | true |
| HNRNPM | Intact, Biogrid | true |
| LDB1 | Intact, Biogrid | true |
| MAPRE2 | Intact, Biogrid | true |
| RELA | Intact, Biogrid | true |
| AGTRAP | Intact | false |
| AIMP2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
