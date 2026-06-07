---
type: protein-evaluation
gene: "ADAM33"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ADAM33 — REJECTED (研究热度过高 (PubMed strict=241，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADAM33 / C20orf153 |
| 蛋白名称 | Disintegrin and metalloproteinase domain-containing protein 33 |
| 蛋白大小 | 813 aa / 87.7 kDa |
| UniProt ID | Q9BZ11 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nuclear speckles; UniProt: Membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 813 aa / 87.7 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=241 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.3; PDB: 1R54, 1R55 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006586, IPR018358, IPR001762, IPR036436, IPR000 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.5/180** | |
| **归一化总分 (÷1.83)** | | | **44.3/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear speckles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 241 |
| PubMed broad count | 356 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf153 |

**关键文献**:
1. Polymorphisms of the ADAM33 gene and chronic obstructive pulmonary disease risk: a meta-analysis.. *The clinical respiratory journal*. PMID: 23902466
2. Association between ADAM33 S2 and V4 polymorphisms and susceptibility to allergic rhinitis: A meta-analysis.. *Allergologia et immunopathologia*. PMID: 26619918
3. Association between ADAM33 polymorphisms and asthma risk: a systematic review and meta-analysis.. *Respiratory research*. PMID: 30791911
4. A disintegrin and metalloprotease 33 (ADAM33) gene polymorphisms and the risk of asthma: a meta-analysis.. *Human immunology*. PMID: 23380143
5. ADAM33's Role in Asthma Pathogenesis: An Overview.. *International journal of molecular sciences*. PMID: 38396994

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 39.4% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 1R54, 1R55 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1R54, 1R55）+ AlphaFold高质量预测（pLDDT=75.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006586, IPR018358, IPR001762, IPR036436, IPR000742; Pfam: PF08516, PF00200, PF01562 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ATXN7 | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |
| SLC30A2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KIR3DL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VMA21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OPRM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM14B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BTNL9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MUC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC35E2A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 1R54, 1R55 | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ADAM33 — Disintegrin and metalloproteinase domain-containing protein 33，有一定研究基础，但仍存在niche空间。
2. 蛋白大小813 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 241 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 241 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZ11
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149451-ADAM33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ADAM33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZ11
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:50:52

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZ11-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZ11 |
| SMART | SM00608;SM00050; |
| UniProt Domain [FT] | DOMAIN 210..409; /note="Peptidase M12B"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00276"; DOMAIN 417..503; /note="Disintegrin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00068"; DOMAIN 649..681; /note="EGF-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR006586;IPR018358;IPR001762;IPR036436;IPR000742;IPR024079;IPR001590;IPR002870;IPR034027; |
| Pfam | PF08516;PF00200;PF01562;PF01421; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149451-ADAM33/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
