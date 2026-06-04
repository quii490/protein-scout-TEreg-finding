---
type: protein-evaluation
gene: "GNPTAB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNPTAB — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNPTAB / GNPTA, KIAA1208 |
| 蛋白名称 | N-acetylglucosamine-1-phosphotransferase subunits alpha/beta |
| 蛋白大小 | 1256 aa / 143.6 kDa |
| UniProt ID | Q3T906 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane; Golgi apparatus membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1256 aa / 143.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.6; PDB: 2N6D, 7S05, 7S06, 9BGF, 9BGG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010506, IPR018247, IPR002048, IPR041536, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.0/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 178 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNPTA, KIAA1208 |

**关键文献**:
1. Mucolipidosis II and III alpha/beta in Brazil: analysis of the GNPTAB gene.. *Gene*. PMID: 23566849
2. Dilated cardiomyopathy in mucolipidosis type 2.. *Journal of biological regulators and homeostatic agents*. PMID: 33000604
3. Dysregulation of mannose-6-phosphate-dependent cholesterol homeostasis in acinar cells mediates pancreatitis.. *The Journal of clinical investigation*. PMID: 34128834
4. Quaternary diagnostics scheme for mucolipidosis II and detection of novel mutation in GNPTAB gene.. *Journal, genetic engineering & biotechnology*. PMID: 34342781
5. Pathogenic variants in GNPTAB and GNPTG encoding distinct subunits of GlcNAc-1-phosphotransferase differentially impact bone resorption in patients with mucolipidosis type II and III.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 34341521

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 23.2% |
| 置信残基 (pLDDT 70-90) 占比 | 43.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 23.4% |
| 有序区域 (pLDDT>70) 占比 | 66.2% |
| 可用 PDB 条目 | 2N6D, 7S05, 7S06, 9BGF, 9BGG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2N6D, 7S05, 7S06, 9BGF, 9BGG）+ AlphaFold极高置信度预测（pLDDT=71.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010506, IPR018247, IPR002048, IPR041536, IPR035993; Pfam: PF06464, PF18440, PF00066 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNPTG | 0.999 | 0.675 | — |
| NAGPA | 0.975 | 0.047 | — |
| PURA | 0.874 | 0.000 | — |
| ADK | 0.825 | 0.067 | — |
| MDH2 | 0.798 | 0.050 | — |
| SYCP3 | 0.783 | 0.000 | — |
| RAD51 | 0.707 | 0.069 | — |
| AP4E1 | 0.627 | 0.045 | — |
| RASSF7 | 0.625 | 0.625 | — |
| MBTPS1 | 0.601 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MAPK1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GNPTG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAP18 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPU | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PICK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RASSF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RETREG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGSF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PXYLP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 2N6D, 7S05, 7S06, 9BGF, 9BGG | pLDDT=71.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Golgi apparatus membrane / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNPTAB — N-acetylglucosamine-1-phosphotransferase subunits alpha/beta，研究基础较多，新颖性有限。
2. 蛋白大小1256 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3T906
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111670-GNPTAB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNPTAB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3T906
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
