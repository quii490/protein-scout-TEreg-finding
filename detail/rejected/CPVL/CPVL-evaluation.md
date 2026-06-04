---
type: protein-evaluation
gene: "CPVL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPVL — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=124，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPVL |
| 蛋白名称 | Probable serine carboxypeptidase CPVL |
| 蛋白大小 | 476 aa / 54.2 kDa |
| UniProt ID | Q9H3G5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 476 aa / 54.2 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=124 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=93.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分** | | | **33.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 124 |
| PubMed broad count | 124 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Perinatal Neuroprotective Strategies and Intraventricular Hemorrhage in Preterm Infants ≤32 Weeks' Gestational Age: A Prospective Study With a Historical Control Cohort.. *Cureus*. PMID: 42211292
2. Identification of risk factors of cystic periventricular leukomalacia in preterm infants.. *Front Pediatr*. PMID: 42063437
3. Five-Minute Apgar Scores and Its Prognostic Value for Mortality and Severe Morbidity in Very Preterm Infants: A Multinational Cohort Study.. *BJOG*. PMID: 40661038
4. Association Between Glymphatic Dysfunction and Anxiety in Parkinson's Disease: Insights from DTI-ALPS and Choroid Plexus Volume.. *Neuropsychiatr Dis Treat*. PMID: 41867702
5. Analytical nuclear gradients for second-order Møller-Plesset perturbation theory using pair-natural orbitals based on localized virtual molecular orbitals.. *J Chem Phys*. PMID: 41404972

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 88.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 94.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.2，有序区 94.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H3G5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P00387-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q53S58 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8N2K0-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WUY8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H0P0-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NX40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 无 | pLDDT=93.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Endoplasmic reticulum | 待确认 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPVL -- Probable serine carboxypeptidase CPVL，研究基础较多，新颖性有限。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 124 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3G5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106066-CPVL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPVL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3G5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
