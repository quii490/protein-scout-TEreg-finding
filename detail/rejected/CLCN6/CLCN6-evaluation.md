---
type: protein-evaluation
gene: "CLCN6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLCN6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLCN6 / KIAA0046 |
| 蛋白名称 | H(+)/Cl(-) exchange transporter 6 |
| 蛋白大小 | 869 aa / 97.3 kDa |
| UniProt ID | P51797 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Late endosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 869 aa / 97.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.8; PDB: 8JPJ, 8JPO, 8JPR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000644, IPR046342, IPR051280, IPR014743, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Uncertain |
| UniProt | Late endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endosome membrane (GO:0010008)
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0046 |

**关键文献**:
1. Genome-wide association analysis and fine mapping of NT-proBNP level provide novel insight into the role of the MTHFR-CLCN6-NPPA-NPPB gene cluster.. *Human molecular genetics*. PMID: 21273288
2. Rare Exome Sequence Variants in CLCN6 Reduce Blood Pressure Levels and Hypertension Risk.. *Circulation. Cardiovascular genetics*. PMID: 26658788
3. Identification and validation of a signature involving voltage-gated chloride ion channel genes for prediction of prostate cancer recurrence.. *Frontiers in endocrinology*. PMID: 36246902
4. Genetic polymorphism in Methylenetetrahydrofolate Reductase chloride transport protein 6 (MTHFR CLCN6) gene is associated with keratinocyte skin cancer in a cohort of renal transplant recipients.. *Skin health and disease*. PMID: 35677930
5. Single nucleotide variations in CLCN6 identified in patients with benign partial epilepsies in infancy and/or febrile seizures.. *PloS one*. PMID: 25794116

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 35.2% |
| 置信残基 (pLDDT 70-90) 占比 | 40.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 8JPJ, 8JPO, 8JPR |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8JPJ, 8JPO, 8JPR）+ AlphaFold高质量预测（pLDDT=77.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000644, IPR046342, IPR051280, IPR014743, IPR002248; Pfam: PF00571, PF00654 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM131B | 0.856 | 0.000 | — |
| MTHFR | 0.818 | 0.000 | — |
| OSTM1 | 0.817 | 0.071 | — |
| AGTRAP | 0.776 | 0.000 | — |
| KIAA1549 | 0.767 | 0.000 | — |
| PPT1 | 0.762 | 0.000 | — |
| BRAF | 0.745 | 0.000 | — |
| TRAK1 | 0.744 | 0.000 | — |
| RNF130 | 0.698 | 0.000 | — |
| KSR1 | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP6V0A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITM2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-29868|pubmed:34446781 |
| ENST00000346436 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 8JPJ, 8JPO, 8JPR | pLDDT=77.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. CLCN6 — H(+)/Cl(-) exchange transporter 6，非常新颖，仅有少数基础研究。
2. 蛋白大小869 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51797
- Protein Atlas: https://www.proteinatlas.org/ENSG00000011021-CLCN6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLCN6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51797
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
