---
type: protein-evaluation
gene: "FBXL8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXL8 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL8 / FBL8 |
| 蛋白名称 | F-box/LRR-repeat protein 8 |
| 蛋白大小 | 374 aa / 40.5 kDa |
| UniProt ID | Q96CD0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 40.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL8 |

**关键文献**:
1. Ubiquitylation of unphosphorylated c-myc by novel E3 ligase SCF(Fbxl8).. *Cancer biology & therapy*. PMID: 35438057
2. DNA methylation analysis of normal colon organoids from familial adenomatous polyposis patients reveals novel insight into colon cancer development.. *Clinical epigenetics*. PMID: 35999641
3. A Novel Signature of CCNF-Associated E3 Ligases Collaborate and Counter Each Other in Breast Cancer.. *Cancers*. PMID: 34201347
4. Human FBXL8 Is a Novel E3 Ligase Which Promotes BRCA Metastasis by Stimulating Pro-Tumorigenic Cytokines and Inhibiting Tumor Suppressors.. *Cancers*. PMID: 32784654
5. Profiling of a novel circadian clock-related prognostic signature and its role in immune function and response to molecular targeted therapy in pancreatic cancer.. *Aging*. PMID: 36626244

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 77.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORC4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SKP1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:19159283|imex:IM-20301 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| ALAS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNAI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Chmp6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ENST00000258200 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 9
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 0 + 9 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXL8 — F-box/LRR-repeat protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96CD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135722-FBXL8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96CD0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96CD0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
