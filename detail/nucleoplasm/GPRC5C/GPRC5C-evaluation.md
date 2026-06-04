---
type: protein-evaluation
gene: "GPRC5C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPRC5C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRC5C / RAIG3 |
| 蛋白名称 | G-protein coupled receptor family C group 5 member C |
| 蛋白大小 | 441 aa / 48.2 kDa |
| UniProt ID | Q9NQ84 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles, Plasma membrane; 额外: Nucleoplasm, Primary cilium, ; UniProt: Cell membrane; Cytoplasmic vesicle membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 48.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR051753; Pfam: PF00003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nucleoplasm, Primary cilium, Primary cilium transition zone | Supported |
| UniProt | Cell membrane; Cytoplasmic vesicle membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- ciliary transition zone (GO:0035869)
- cilium (GO:0005929)
- cytoplasmic vesicle membrane (GO:0030659)
- extracellular exosome (GO:0070062)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)
- vesicle (GO:0031982)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAIG3 |

**关键文献**:
1. Vitamin A-Retinoic Acid Signaling Regulates Hematopoietic Stem Cell Dormancy.. *Cell*. PMID: 28479188
2. Orphan GPCR GPRC5C Facilitates Angiotensin II-Induced Smooth Muscle Contraction.. *Circulation research*. PMID: 38597112
3. Expression and prognostic significance of MLH1 and GPRC5C in resectable hepatocellular carcinoma.. *BMC cancer*. PMID: 40713584
4. GPRC5C drives branched-chain amino acid metabolism in leukemogenesis.. *Blood advances*. PMID: 37639313
5. The G protein-coupled receptor GPRC5C is a saccharide sensor with a novel 'off' response.. *FEBS letters*. PMID: 37418589

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 35.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 34.2% |
| 有序区域 (pLDDT>70) 占比 | 57.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 57.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR051753; Pfam: PF00003 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRM2 | 0.833 | 0.000 | — |
| GPR158 | 0.530 | 0.000 | — |
| GPR156 | 0.491 | 0.000 | — |
| ABHD16A | 0.460 | 0.421 | — |
| TMEM150C | 0.458 | 0.000 | — |
| GPR137 | 0.450 | 0.000 | — |
| GPR149 | 0.446 | 0.000 | — |
| GPR155 | 0.444 | 0.000 | — |
| GPR107 | 0.444 | 0.000 | — |
| ADGRG6 | 0.428 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ABHD16A | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| OLA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ZNF277 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM171 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APPBP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| TACR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasmic vesicle membrane / Vesicles, Plasma membrane; 额外: Nucleoplasm, Primar | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPRC5C — G-protein coupled receptor family C group 5 member C，非常新颖，仅有少数基础研究。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ84
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170412-GPRC5C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRC5C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ84
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
