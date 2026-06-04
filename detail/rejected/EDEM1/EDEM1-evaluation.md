---
type: protein-evaluation
gene: "EDEM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EDEM1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=135，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EDEM1 |
| 蛋白名称 | ER degradation-enhancing alpha-mannosidase-like protein 1 |
| 蛋白大小 | 657 aa / 73.8 kDa |
| UniProt ID | Q92611 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum; 额外: Aggresome; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 657 aa / 73.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=135 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Aggresome | Enhanced |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 135 |
| PubMed broad count | 170 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Deep learning-based precision phenotyping of spine curvature identifies novel genetic risk loci for scoliosis in the UK Biobank.. *NPJ Digit Med*. PMID: 41882318
2. The synthetic cannabinoid CUMYL-4CN-BINACA induces hepatic injury in rats via oxidative stress, NF-κB activation, Nrf2 suppression, EDEM-1, ER stress-mediated apoptotic pathways.. *Food Chem Toxicol*. PMID: 41109593
3. Integration of autophagy-related genes and immune dysregulation reveals a prognostic landscape in multiple myeloma.. *Front Oncol*. PMID: 41040512
4. EDEM1 Inhibits Endoplasmic Reticulum Stress to Induce Doxorubicin Resistance through Accelerating ERAD and Activating Keap1/Nrf2 Antioxidant Pathway in Triple-Negative Breast Cancer.. *Research (Wash D C)*. PMID: 40735463
5. Alzheimer's disease genetic risk: Top African American risk allele frequencies and genetic architecture among Mexican-, African-, and non-Hispanic White Americans.. *Alzheimers Dement (N Y)*. PMID: 40539127

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 73.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 80.3% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=83.9，有序区 80.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC10 | 0.000 | 0.000 | — |
| SEL1L | 0.000 | 0.000 | — |
| CANX | 0.000 | 0.000 | — |
| XBP1 | 0.000 | 0.000 | — |
| DERL2 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| OS9 | 0.000 | 0.000 | — |
| MAN2C1 | 0.000 | 0.000 | — |
| EDEM3 | 0.000 | 0.000 | — |
| DERL3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q7JUF8 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q0E938 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9V393 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q92611 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P27797 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P30101 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P13667 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15084 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P14625 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P07237 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 无 | pLDDT=83.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum; 额外: Aggresome | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EDEM1 — ER degradation-enhancing alpha-mannosidase-like protein 1，研究基础较多，新颖性有限。
2. 蛋白大小657 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 135 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92611
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134109-EDEM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EDEM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92611
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
