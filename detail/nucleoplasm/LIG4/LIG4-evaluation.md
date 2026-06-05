---
type: protein-evaluation
gene: "LIG4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LIG4 — REJECTED (研究热度过高 (PubMed strict=315，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIG4 |
| 蛋白名称 | DNA ligase 4 |
| 蛋白大小 | 911 aa / 104.0 kDa |
| UniProt ID | P49917 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 911 aa / 104.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=315 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.2; PDB: 1IK9, 2E2W, 3II6, 3VNN, 3W1B, 3W1G, 3W5O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR044125, IPR001357, IPR036420, IPR000977, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- condensed chromosome (GO:0000793)
- DNA ligase IV complex (GO:0032807)
- DNA-dependent protein kinase-DNA ligase 4 complex (GO:0005958)
- nonhomologous end joining complex (GO:0070419)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 315 |
| PubMed broad count | 718 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DNA damage response signaling pathways and targets for radiotherapy sensitization in cancer.. *Signal transduction and targeted therapy*. PMID: 32355263
2. Dynamic assemblies and coordinated reactions of non-homologous end joining.. *Nature*. PMID: 40500445
3. Chromosome end protection by RAP1-mediated inhibition of DNA-PK.. *Nature*. PMID: 40240611
4. A landscape of germ line mutations in a cohort of inherited bone marrow failure patients.. *Blood*. PMID: 29146883
5. Ligase IV syndrome.. *Advances in experimental medicine and biology*. PMID: 20687505

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 62.7% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 1IK9, 2E2W, 3II6, 3VNN, 3W1B, 3W1G, 3W5O, 4HTO, 4HTP, 6BKF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1IK9, 2E2W, 3II6, 3VNN, 3W1B, 3W1G, 3W5O, 4HTO, 4HTP, 6BKF）+ AlphaFold极高置信度预测（pLDDT=88.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044125, IPR001357, IPR036420, IPR000977, IPR012309; Pfam: PF00533, PF04679, PF01068 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NHEJ1 | 0.999 | 0.964 | — |
| PRKDC | 0.999 | 0.897 | — |
| XRCC5 | 0.999 | 0.974 | — |
| XRCC6 | 0.999 | 0.967 | — |
| XRCC4 | 0.999 | 0.997 | — |
| DCLRE1C | 0.997 | 0.626 | — |
| PAXX | 0.988 | 0.292 | — |
| ATM | 0.987 | 0.142 | — |
| ERCC1 | 0.966 | 0.000 | — |
| ERCC4 | 0.965 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DNAlig4 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| sgg | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| XRCC4 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:11702069 |
| PNKP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GZMK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TSFM | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PHF10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZSCAN18 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NHEJ1 | psi-mi:"MI:0096"(pull down) | pubmed:16439205|imex:IM-11818 |
| LIF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 1IK9, 2E2W, 3II6, 3VNN, 3W1B,  | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. LIG4 — DNA ligase 4，研究基础较多，新颖性有限。
2. 蛋白大小911 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 315 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 315 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49917
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174405-LIG4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIG4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49917
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000174405-LIG4/subcellular

![](https://images.proteinatlas.org/57325/1006_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/57325/1006_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/57325/1011_A6_6_red_green.jpg)
![](https://images.proteinatlas.org/57325/1011_A6_8_red_green.jpg)
![](https://images.proteinatlas.org/57325/1683_F7_14_cr5805392412353_red_green.jpg)
![](https://images.proteinatlas.org/57325/1683_F7_18_cr5805392cdad36_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49917-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
