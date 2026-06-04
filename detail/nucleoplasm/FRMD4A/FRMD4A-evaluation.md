---
type: protein-evaluation
gene: "FRMD4A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRMD4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRMD4A / FRMD4, KIAA1294 |
| 蛋白名称 | FERM domain-containing protein 4A |
| 蛋白大小 | 1039 aa / 115.5 kDa |
| UniProt ID | Q9P2Q2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton; Cell junction, adherens junction; C |
| 蛋白大小 | 8/10 | ×1 | 8 | 1039 aa / 115.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR021774, IPR014352, IPR035963, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cell junction, adherens junction; Cell junction, tight junction | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- bicellular tight junction (GO:0005923)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FRMD4, KIAA1294 |

**关键文献**:
1. p53 induces circFRMD4A to suppress cancer development through glycolytic reprogramming and cuproptosis.. *Molecular cell*. PMID: 39637854
2. Large-scale genome-wide association study of Asian population reveals genetic factors in FRMD4A and other loci influencing smoking initiation and nicotine dependence.. *Human genetics*. PMID: 22006218
3. Knocking Down FRMD4A, a Factor Associated with the Brain Development Disorder and a Risk Factor for Alzheimer's Disease, Using RNA-Targeting CRISPR/Cas13 Reveals Its Role in Cell Morphogenesis.. *International journal of molecular sciences*. PMID: 41155374
4. Integration of scRNA-Seq and scATAC-Seq Reveals Malignant Characteristics of Sarcomatoid Clear Cell Renal Cell Carcinoma.. *Cancer science*. PMID: 41082386
5. FRMD4A-cytohesin signaling modulates the cellular release of tau.. *Journal of cell science*. PMID: 27044754

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 30.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 49.3% |
| 有序区域 (pLDDT>70) 占比 | 43.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 43.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR021774, IPR014352, IPR035963, IPR019748; Pfam: PF11819, PF09380, PF00373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYTH1 | 0.919 | 0.521 | — |
| CYTH4 | 0.720 | 0.236 | — |
| CYTH2 | 0.683 | 0.114 | — |
| CYTH3 | 0.681 | 0.114 | — |
| RUFY2 | 0.586 | 0.000 | — |
| MYO1G | 0.511 | 0.000 | — |
| REEP3 | 0.498 | 0.000 | — |
| MYO5C | 0.476 | 0.000 | — |
| C11orf52 | 0.471 | 0.000 | — |
| PICALM | 0.471 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF3IP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| prfB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| cutC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| metG1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| WDR83 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TAX1BP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 无 | pLDDT=61.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell junction, adherens j / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FRMD4A — FERM domain-containing protein 4A，非常新颖，仅有少数基础研究。
2. 蛋白大小1039 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2Q2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151474-FRMD4A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRMD4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2Q2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
