---
type: protein-evaluation
gene: "DSCAML1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DSCAML1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSCAML1 |
| 蛋白名称 | Cell adhesion molecule DSCAML1 |
| 蛋白大小 | 2113 aa / 230.6 kDa |
| UniProt ID | A0A384DVL8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Synapse |
| 蛋白大小 | 2/10 | ×1 | 2 | 2113 aa / 230.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.5/180** | |
| **归一化总分** | | | **38.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell membrane; Synapse | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 46 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Assessing vision and autism spectrum disorder-relevant social interaction phenotypes in Dscam mice.. *Behav Brain Res*. PMID: 42119898
2. Pharmacological Correction of Aberrant DSCAML1 Localization by 4-Phenylbutyrate Ameliorates Epileptic Phenotypes in a Mouse Model Harboring the Patient-Specific A2105T Mutation.. *Genes Cells*. PMID: 42003794
3. Molecular insights into electroreceptor ribbon synapses from differential gene expression in sturgeon lateral line organs.. *J Anat*. PMID: 41271589
4. DSCAML1+ extracellular vesicles revealed by single-vesicle proteomics as a novel biomarker and therapeutic target in myocardial infarction.. *J Nanobiotechnology*. PMID: 41872860
5. RNA-Seq Analysis of Ruminal Methane Emissions in Beef-on-Dairy Cattle: Evidence for Immune, Nervous, and Endocrine Pathway Involvement.. *Animals (Basel)*. PMID: 41751050

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DSCAM | 0.000 | 0.000 | — |
| APOA5 | 0.000 | 0.000 | — |
| SDK2 | 0.000 | 0.000 | — |
| DLG4 | 0.000 | 0.000 | — |
| NTN1 | 0.000 | 0.000 | — |
| CPA1 | 0.000 | 0.000 | — |
| APOC3 | 0.000 | 0.000 | — |
| DLG2 | 0.000 | 0.000 | — |
| APOA4 | 0.000 | 0.000 | — |
| DOCK1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q5TCQ9 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9UPR0 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q86UL8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8TD84 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 4
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Synapse / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DSCAML1 — Cell adhesion molecule DSCAML1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小2113 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A384DVL8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177103-DSCAML1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSCAML1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A384DVL8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
