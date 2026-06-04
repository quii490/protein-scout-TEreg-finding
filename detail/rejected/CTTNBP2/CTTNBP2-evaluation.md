---
type: protein-evaluation
gene: "CTTNBP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTTNBP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTTNBP2 / C7orf8, CORTBP2, KIAA1758 |
| 蛋白名称 | Cortactin-binding protein 2 |
| 蛋白大小 | 1663 aa / 181.1 kDa |
| UniProt ID | Q8WZ74 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Midbody ring; 额外: Cytosol; UniProt: Cytoplasm, cell cortex; Cell projection, dendritic spine |
| 蛋白大小 | 5/10 | ×1 | 5 | 1663 aa / 181.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR050719, IPR019131, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Midbody ring; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cell cortex; Cell projection, dendritic spine | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- dendritic spine (GO:0043197)
- FAR/SIN/STRIPAK complex (GO:0090443)
- glutamatergic synapse (GO:0098978)
- postsynaptic actin cytoskeleton (GO:0098871)
- synaptic vesicle (GO:0008021)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf8, CORTBP2, KIAA1758 |

**关键文献**:
1. Phase separation and zinc-induced transition modulate synaptic distribution and association of autism-linked CTTNBP2 and SHANK3.. *Nature communications*. PMID: 35562389
2. STRIPAK complexes: structure, biological function, and involvement in human diseases.. *The international journal of biochemistry & cell biology*. PMID: 24333164
3. CTTNBP2 Controls Synaptic Expression of Zinc-Related Autism-Associated Proteins and Regulates Synapse Formation and Autism-like Behaviors.. *Cell reports*. PMID: 32492416
4. Autism-linked mutations of CTTNBP2 reduce social interaction and impair dendritic spine formation via diverse mechanisms.. *Acta neuropathologica communications*. PMID: 33168105
5. Sex bias in social deficits, neural circuits and nutrient demand in Cttnbp2 autism models.. *Brain : a journal of neurology*. PMID: 36385662

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.0 |
| 高置信度残基 (pLDDT>90) 占比 | 6.5% |
| 置信残基 (pLDDT 70-90) 占比 | 39.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 46.0% |
| 有序区域 (pLDDT>70) 占比 | 45.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.0），有序残基占 45.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR050719, IPR019131, IPR057568; Pfam: PF25408, PF00023, PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRIP1 | 0.998 | 0.994 | — |
| STRN3 | 0.998 | 0.994 | — |
| STRIP2 | 0.997 | 0.994 | — |
| MOB4 | 0.997 | 0.994 | — |
| STRN | 0.997 | 0.994 | — |
| STK26 | 0.996 | 0.994 | — |
| STRN4 | 0.996 | 0.994 | — |
| PPP2CB | 0.995 | 0.994 | — |
| STK24 | 0.995 | 0.994 | — |
| PDCD10 | 0.995 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APPL1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ZRANB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MOB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| STK26 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| PPP2CB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18782753|imex:IM-20360| |
| PPP2CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| Strn | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STRN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| CCT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STRIP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.0 + PDB: 无 | pLDDT=58.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cell cortex; Cell projection, dendritic / Midbody ring; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTTNBP2 — Cortactin-binding protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小1663 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WZ74
- Protein Atlas: https://www.proteinatlas.org/ENSG00000077063-CTTNBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTTNBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WZ74
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
