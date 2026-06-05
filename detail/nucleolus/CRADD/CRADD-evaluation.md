---
type: protein-evaluation
gene: "CRADD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRADD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRADD / RAIDD |
| 蛋白名称 | Death domain-containing protein CRADD |
| 蛋白大小 | 199 aa / 22.7 kDa |
| UniProt ID | P78560 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 199 aa / 22.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=47 篇 (<=60->6) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=79.4; PDB: 2O71, 2OF5, 3CRD |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001315, IPR042148, IPR037939, IPR037926, IPR011 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endopeptidase complex (GO:1905369)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 119 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAIDD |

**关键文献**:
1. Extra centrosomes delay DNA damage-driven tumorigenesis.. *Science advances*. PMID: 38552015
2. The adaptor CRADD/RAIDD controls activation of endothelial cells by proinflammatory stimuli.. *The Journal of biological chemistry*. PMID: 24958727
3. Cutting edge: the "death" adaptor CRADD/RAIDD targets BCL10 and suppresses agonist-induced cytokine expression in T lymphocytes.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 22323537
4. PIDD1 in cell cycle control, sterile inflammation and cell death.. *Biochemical Society transactions*. PMID: 35343572
5. CRADD and USP44 mutations in intellectual disability, mild lissencephaly, brain atrophy, developmental delay, strabismus, behavioural problems and skeletal anomalies.. *European journal of medical genetics*. PMID: 33647455

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 65.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 82.4% |
| 可用 PDB 条目 | 2O71, 2OF5, 3CRD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2O71, 2OF5, 3CRD）+ AlphaFold高质量预测（pLDDT=79.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001315, IPR042148, IPR037939, IPR037926, IPR011029; Pfam: PF00619, PF00531 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PIDD1 | 0.999 | 0.981 | — |
| CASP2 | 0.999 | 0.895 | — |
| TRADD | 0.980 | 0.000 | — |
| FADD | 0.967 | 0.000 | — |
| CYFIP2 | 0.934 | 0.000 | — |
| RIPK1 | 0.814 | 0.516 | — |
| APAF1 | 0.745 | 0.000 | — |
| MINDY3 | 0.728 | 0.000 | — |
| TNFRSF1A | 0.698 | 0.292 | — |
| RIPK2 | 0.692 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CASP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15073321 |
| PIDD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15073321 |
| ERG28 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CCSER2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DCXR | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IL9R | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KPNA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VTN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 2O71, 2OF5, 3CRD | pLDDT=79.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CRADD -- Death domain-containing protein CRADD，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78560
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169372-CRADD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRADD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78560
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78560-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
