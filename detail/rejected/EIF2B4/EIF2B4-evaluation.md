---
type: protein-evaluation
gene: "EIF2B4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF2B4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2B4 |
| 蛋白名称 | Translation initiation factor eIF2B subunit delta |
| 蛋白大小 | 544 aa / 59.7 kDa |
| UniProt ID | E7ERK9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 544 aa / 59.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 44 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A set of downregulated pleiotropic genes are possible multi-omics biomarkers underlying the irritable bowel syndrome-non-alcoholic fatty liver disease comorbidity.. *Am J Transl Res*. PMID: 41552323
2. EIF2B4 promotes hepatocellular carcinoma progression and immune evasion by driving STAT3 translation via a GEF-dependent mechanism.. *Cell Oncol (Dordr)*. PMID: 41144132
3. Novel Stemness-Associated Scores: Enhancing Predictions of Hepatocellular Carcinoma Prognosis and Tumor Immune Microenvironment.. *Oncol Res*. PMID: 40746880
4. Effects of the Small-Molecule ISRIB on the Rapid and Efficient Myelination of Oligodendrocytes in Human Stem Cell-Derived Cerebral Organoids in Patients With Leukoencephalopathy With Vanishing White Matter.. *CNS Neurosci Ther*. PMID: 40296303
5. Exploring the Causal Relationship and Molecular Mechanisms Between Fasting Insulin and Androgenetic Alopecia: A Mendelian Randomization Study with Bioinformatics Analysis.. *Clin Cosmet Investig Dermatol*. PMID: 39935957

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 59.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 25.9% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=75.6，有序区 68.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2B3 | 0.000 | 0.000 | — |
| EIF2B5 | 0.000 | 0.000 | — |
| EIF2B1 | 0.000 | 0.000 | — |
| EIF2B2 | 0.000 | 0.000 | — |
| EIF2S1 | 0.000 | 0.000 | — |
| EIF2S3 | 0.000 | 0.000 | — |
| EIF2S2 | 0.000 | 0.000 | — |
| EIF2S3B | 0.000 | 0.000 | — |
| RABIF | 0.000 | 0.000 | — |
| TYMP | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9UI10 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UI10-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:E7ERK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P49770 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q63186 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13144 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 无 | pLDDT=75.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EIF2B4 — Translation initiation factor eIF2B subunit delta，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小544 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/E7ERK9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115211-EIF2B4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2B4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/E7ERK9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
