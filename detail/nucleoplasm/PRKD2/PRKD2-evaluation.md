---
type: protein-evaluation
gene: "PRKD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRKD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRKD2 / PKD2 |
| 蛋白名称 | Serine/threonine-protein kinase D2 |
| 蛋白大小 | 878 aa / 96.7 kDa |
| UniProt ID | Q9BZL6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Cell membrane; Nucleus; Golgi apparatus, trans-Go |
| 蛋白大小 | 8/10 | ×1 | 8 | 878 aa / 96.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 2COA, 3BGM, 4NNX, 4NNY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046349, IPR020454, IPR011009, IPR011993, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Cell membrane; Nucleus; Golgi apparatus, trans-Golgi network | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PKD2 |

**关键文献**:
1. Identification of novel mutational drivers reveals oncogene dependencies in multiple myeloma.. *Blood*. PMID: 29884741
2. Proteome-Wide Mendelian Randomization Identifies Therapeutic Targets for Abdominal Aortic Aneurysm.. *Journal of the American Heart Association*. PMID: 39895541
3. Single-cell and bulk transcriptomics uncovers PRKD2-driven tumor stemness and progression in multiple myeloma.. *Scientific reports*. PMID: 41120632
4. HSP90 supports tumor growth and angiogenesis through PRKD2 protein stabilization.. *Cancer research*. PMID: 25297628
5. Mutual inhibition between Prkd2 and Bcl6 controls T follicular helper cell differentiation.. *Science immunology*. PMID: 31980486

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.8% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 57.8% |
| 可用 PDB 条目 | 2COA, 3BGM, 4NNX, 4NNY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 57.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046349, IPR020454, IPR011009, IPR011993, IPR001849; Pfam: PF00130, PF00169, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRKD1 | 0.979 | 0.793 | — |
| PRKD3 | 0.976 | 0.767 | — |
| PRKCA | 0.911 | 0.000 | — |
| ITGB1 | 0.909 | 0.072 | — |
| ITGAM | 0.907 | 0.000 | — |
| PRKCB | 0.907 | 0.000 | — |
| ITGB2 | 0.905 | 0.072 | — |
| RAP1A | 0.905 | 0.000 | — |
| RAP1B | 0.904 | 0.000 | — |
| ITGAL | 0.903 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380984 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| CHM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHYHIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| ST8SIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLA2G10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 2COA, 3BGM, 4NNX, 4NNY | pLDDT=68.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Nucleus; Golgi apparatus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRKD2 — Serine/threonine-protein kinase D2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小878 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZL6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105287-PRKD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRKD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZL6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
