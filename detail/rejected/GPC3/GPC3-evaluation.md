---
type: protein-evaluation
gene: "GPC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPC3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=659，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPC3 / OCI5 |
| 蛋白名称 | Glypican-3 |
| 蛋白大小 | 580 aa / 65.6 kDa |
| UniProt ID | P51654 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 580 aa / 65.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=659 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.1; PDB: 7ZA1, 7ZAW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001863, IPR019803; Pfam: PF01153 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.0/180** | |
| **归一化总分** | | | **38.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- endoplasmic reticulum lumen (GO:0005788)
- Golgi lumen (GO:0005796)
- lysosomal lumen (GO:0043202)
- plasma membrane (GO:0005886)
- side of membrane (GO:0098552)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 659 |
| PubMed broad count | 1487 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OCI5 |

**关键文献**:
1. Peptide Binder to Glypican-3 as a Theranostic Agent for Hepatocellular Carcinoma.. *Journal of nuclear medicine : official publication, Society of Nuclear Medicine*. PMID: 38423788
2. Simpson-Golabi-Behmel syndrome.. *American journal of medical genetics. Part C, Seminars in medical genetics*. PMID: 38766979
3. Glypican-3: A promising biomarker for hepatocellular carcinoma diagnosis and treatment.. *Medicinal research reviews*. PMID: 28621802
4. GPC3-targeted immunoPET imaging of hepatocellular carcinomas.. *European journal of nuclear medicine and molecular imaging*. PMID: 35147737
5. Glypican-3-Specific CAR T Cells Coexpressing IL15 and IL21 Have Superior Expansion and Antitumor Activity against Hepatocellular Carcinoma.. *Cancer immunology research*. PMID: 31953246

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 52.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 28.4% |
| 有序区域 (pLDDT>70) 占比 | 66.0% |
| 可用 PDB 条目 | 7ZA1, 7ZAW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7ZA1, 7ZAW）+ AlphaFold高质量预测（pLDDT=75.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001863, IPR019803; Pfam: PF01153 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IGF2 | 0.993 | 0.000 | — |
| WNT3A | 0.986 | 0.143 | — |
| IHH | 0.964 | 0.114 | — |
| WNT5A | 0.960 | 0.143 | — |
| SHH | 0.959 | 0.114 | — |
| AFP | 0.927 | 0.000 | — |
| WNT2 | 0.927 | 0.143 | — |
| WNT4 | 0.926 | 0.143 | — |
| WNT1 | 0.922 | 0.143 | — |
| WNT3 | 0.921 | 0.143 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APPL1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| GPR183 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIP5K1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LIPG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ISLR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ODAPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIGLECL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 7ZA1, 7ZAW | pLDDT=75.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPC3 — Glypican-3，研究基础较多，新颖性有限。
2. 蛋白大小580 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 659 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51654
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147257-GPC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51654
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
