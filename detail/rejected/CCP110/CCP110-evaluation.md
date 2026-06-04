---
type: protein-evaluation
gene: "CCP110"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CCP110 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCP110 |
| 蛋白名称 | Centriolar coiled-coil protein of 110 kDa |
| 蛋白大小 | 1012 aa / 113.4 kDa |
| UniProt ID | O43303 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCP110/IF_images/REH_1.jpg|REH]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCP110/IF_images/U-251MG_1.jpg|U 251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centriolar satellite; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1012 aa / 113.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; C... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 77 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CDK1 and CEP97 cooperatively control centriole length to orchestrate ciliogenesis and developmental patterning.. *Genes Dev*. PMID: 42140673
2. Serum Proteomic Analysis Using Gel-Based Liquid Chromatography Tandem Mass Spectrometry Reveals Differences Between Canine Oral Malignancies and Non-Malignant Conditions.. *Vet Med Sci*. PMID: 42035449
3. Decoding the Molecular Landscape of Prepubertal Oocyte Maturation: GTPBP4 as a Key Driver of In Vitro Developmental Competence.. *Cell Prolif*. PMID: 40017443
4. CEP76 impairment at the centrosome-cilium interface contributes to a spectrum of ciliopathies.. *Sci Adv*. PMID: 41105778
5. Disrupted glucocorticoid receptor cell signalling causes a ciliogenesis defect in the fetal mouse renal tubule.. *EMBO Rep*. PMID: 40247090

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 16.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 62.4% |
| 有序区域 (pLDDT>70) 占比 | 28.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCP110/CCP110-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 28.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP97 | 0.000 | 0.000 | — |
| CEP290 | 0.000 | 0.000 | — |
| CCNF | 0.000 | 0.000 | — |
| CENPJ | 0.000 | 0.000 | — |
| RAB8A | 0.000 | 0.000 | — |
| CEP135 | 0.000 | 0.000 | — |
| PLK4 | 0.000 | 0.000 | — |
| SASS6 | 0.000 | 0.000 | — |
| KIF24 | 0.000 | 0.000 | — |
| CEP76 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q7TSH4 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q5NFW7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8IW35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:O43303 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P62158 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UBB9 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P25189 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P41208 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 无 | pLDDT=54.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centriolar satellite | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CCP110 — Centriolar coiled-coil protein of 110 kDa，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1012 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43303
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103540-CCP110/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCP110
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43303
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CCP110/CCP110-PAE.png]]




