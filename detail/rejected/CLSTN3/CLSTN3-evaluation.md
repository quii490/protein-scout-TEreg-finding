---
type: protein-evaluation
gene: "CLSTN3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLSTN3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLSTN3 / CS3, KIAA0726 |
| 蛋白名称 | Calsyntenin-3 |
| 蛋白大小 | 956 aa / 106.1 kDa |
| UniProt ID | Q9BQT9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Postsynaptic cell membrane; Endoplasmic reticulum membrane;  |
| 蛋白大小 | 8/10 | ×1 | 8 | 956 aa / 106.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002126, IPR015919, IPR045588, IPR013320; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Postsynaptic cell membrane; Endoplasmic reticulum membrane; Golgi apparatus membrane; Cell projectio... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- dendrite (GO:0030425)
- endoplasmic reticulum membrane (GO:0005789)
- GABA-ergic synapse (GO:0098982)
- glutamatergic synapse (GO:0098978)
- Golgi membrane (GO:0000139)
- lipid droplet (GO:0005811)
- organelle membrane contact site (GO:0044232)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CS3, KIAA0726 |

**关键文献**:
1. Identification of novel protein biomarkers and drug targets for colorectal cancer by integrating human plasma proteome with genome.. *Genome medicine*. PMID: 37726845
2. CLSTN3β enforces adipocyte multilocularity to facilitate lipid utilization.. *Nature*. PMID: 36477540
3. CLSTN3 gene variant associates with obesity risk and contributes to dysfunction in white adipose tissue.. *Molecular metabolism*. PMID: 35753632
4. An integrated multi-omics analysis identifies protein biomarkers and potential drug targets for psoriatic arthritis.. *Communications biology*. PMID: 39953266
5. Calsyntenin-3 interacts with both α- and β-neurexins in the regulation of excitatory synaptic innervation in specific Schaffer collateral pathways.. *The Journal of biological chemistry*. PMID: 32434929

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 44.9% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 73.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.3，有序区 73.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002126, IPR015919, IPR045588, IPR013320; Pfam: PF19699 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NRXN1 | 0.734 | 0.000 | — |
| NRXN2 | 0.705 | 0.000 | — |
| CDH17 | 0.690 | 0.000 | — |
| NXN | 0.643 | 0.000 | — |
| LRRTM1 | 0.634 | 0.000 | — |
| GABBR1 | 0.509 | 0.000 | — |
| PEX5 | 0.495 | 0.000 | — |
| ERP27 | 0.495 | 0.000 | — |
| IGSF21 | 0.485 | 0.000 | — |
| SH3BP5L | 0.484 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| App | psi-mi:"MI:0030"(cross-linking study) | pubmed:17934213|imex:IM-19287 |
| ST8SIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM97 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CMTM7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZDHHC22 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAM1L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NKG7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM54 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM107 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PGAP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 无 | pLDDT=77.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynaptic cell membrane; Endoplasmic reticulum  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLSTN3 — Calsyntenin-3，非常新颖，仅有少数基础研究。
2. 蛋白大小956 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQT9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139182-CLSTN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLSTN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQT9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQT9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
