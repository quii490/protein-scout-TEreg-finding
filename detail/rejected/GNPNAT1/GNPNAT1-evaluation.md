---
type: protein-evaluation
gene: "GNPNAT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNPNAT1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNPNAT1 / GNA1 |
| 蛋白名称 | Glucosamine 6-phosphate N-acetyltransferase |
| 蛋白大小 | 184 aa / 20.7 kDa |
| UniProt ID | Q96EK6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane; Endosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 20.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.5; PDB: 2HUZ, 2O28, 3CXP, 3CXQ, 3CXS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR000182, IPR039143; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi apparatus membrane; Endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- endosome membrane (GO:0010008)
- Golgi membrane (GO:0000139)
- late endosome (GO:0005770)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNA1 |

**关键文献**:
1. GNPNAT1 is a potential biomarker correlated with immune infiltration and immunotherapy outcome in breast cancer.. *Frontiers in immunology*. PMID: 37215111
2. GNPNAT1 promotes the stemness of breast cancer and serves as a potential prognostic biomarker.. *Oncology reports*. PMID: 37387422
3. Potential role of glucosamine-phosphate N-acetyltransferase 1 in the development of lung adenocarcinoma.. *Aging*. PMID: 33686019
4. A novel variant in GNPNAT1 gene causing a spondylo-epi-metaphyseal dysplasia resembling PGM3-Desbuquois like dysplasia.. *American journal of medical genetics. Part A*. PMID: 36097642
5. GNPNAT1 is a Biomarker That Predicts a Poor Prognosis of Breast Cancer.. *Breast cancer (Dove Medical Press)*. PMID: 38476642

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.5 |
| 高置信度残基 (pLDDT>90) 占比 | 97.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 2HUZ, 2O28, 3CXP, 3CXQ, 3CXS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2HUZ, 2O28, 3CXP, 3CXQ, 3CXS）+ AlphaFold极高置信度预测（pLDDT=97.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR000182, IPR039143; Pfam: PF00583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGM3 | 0.997 | 0.000 | — |
| GFPT1 | 0.994 | 0.071 | — |
| GFPT2 | 0.993 | 0.071 | — |
| NAGK | 0.980 | 0.079 | — |
| GNPDA1 | 0.971 | 0.000 | — |
| GNPDA2 | 0.961 | 0.000 | — |
| HK1 | 0.939 | 0.067 | — |
| AMDHD2-2 | 0.934 | 0.000 | — |
| HK3 | 0.932 | 0.067 | — |
| HKDC1 | 0.932 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000496934.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Ryr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| C1QA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NAGK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FABP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OR5F1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFKBIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSD17B6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.5 + PDB: 2HUZ, 2O28, 3CXP, 3CXQ, 3CXS | pLDDT=97.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Endosome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNPNAT1 — Glucosamine 6-phosphate N-acetyltransferase，非常新颖，仅有少数基础研究。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EK6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100522-GNPNAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNPNAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EK6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
