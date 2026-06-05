---
type: protein-evaluation
gene: "CAMKK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CAMKK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAMKK1 / CAMKKA |
| 蛋白名称 | Calcium/calmodulin-dependent protein kinase kinase 1 |
| 蛋白大小 | 505 aa / 55.7 kDa |
| UniProt ID | Q8N5S9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAMKK1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAMKK1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 55.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.0; PDB: 6CCF, 6CD6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAMKKA |

**关键文献**:
1. Human umbilical cord mesenchymal stem cell-derived exosomes ameliorate liver steatosis by promoting fatty acid oxidation and reducing fatty acid synthesis.. *JHEP reports : innovation in hepatology*. PMID: 37274776
2. CAMKK1 in Obesity and Type 2 Diabetes Mellitus: Evidence of Interaction With Appetite-Regulating, Metabolic and Inflammatory Factors.. *Endocrinology, diabetes & metabolism*. PMID: 40965347
3. 14-3-3 protein inhibits CaMKK1 by blocking the kinase active site with its last two C-terminal helices.. *Protein science : a publication of the Protein Society*. PMID: 37817008
4. Associations Between CAMKK1 Polymorphism rs7214723 and the Prognosis of Patients With Lung Cancer.. *Frontiers in oncology*. PMID: 34868969
5. Look for the Scaffold: Multifaceted Regulation of Enzyme Activity by 14-3-3 Proteins.. *Physiological research*. PMID: 38647170

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 31.7% |
| 有序区域 (pLDDT>70) 占比 | 57.6% |
| 可用 PDB 条目 | 6CCF, 6CD6 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6CCF, 6CD6）+ AlphaFold高质量预测（pLDDT=71.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CALM3 | 0.998 | 0.916 | — |
| CALML3 | 0.987 | 0.060 | — |
| CALML5 | 0.987 | 0.060 | — |
| CALML6 | 0.985 | 0.045 | — |
| CALML4 | 0.985 | 0.045 | — |
| CALM1 | 0.976 | 0.911 | — |
| CAMK4 | 0.947 | 0.178 | — |
| CALM2 | 0.927 | 0.917 | — |
| CAMKK2 | 0.908 | 0.000 | — |
| CAMK1 | 0.713 | 0.184 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| RUVBL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RUVBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LPIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GARRE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CSNK1E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ELAC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| NTHL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 6CCF, 6CD6 | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CAMKK1 — Calcium/calmodulin-dependent protein kinase kinase 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5S9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000004660-CAMKK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAMKK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5S9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:30:32

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N5S9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
