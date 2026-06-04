---
type: protein-evaluation
gene: "CXCL14"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CXCL14 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=625，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CXCL14 |
| 蛋白名称 | C-X-C motif chemokine 14 |
| 蛋白大小 | 111 aa / 13.1 kDa |
| UniProt ID | O95715 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 8/10 | x1 | 8 | 111 aa / 13.1 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=625 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 22 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **62.0/180** | |
| **归一化总分** | | | **34.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Secreted | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 625 |
| PubMed broad count | 645 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Multi-omics analysis reveals CXCL14(+) inhibitory neuron dysfunction in major depressive disorder.. *J Affect Disord*. PMID: 41796773
2. Spatial metabolomics and transcriptomics reveal the metabolic-immune niche associated with renal fibrosis in hyperuricemia.. *Free Radic Biol Med*. PMID: 41951016
3. Integrated Bioinformatics and Structural Assessment Suggest Doxycycline as a Potential Candidate Targeting MMP7 in Lung Cancer and SSc-Associated ILD.. *OMICS*. PMID: 42201688
4. Multi-Omics Reveals Dysregulation of the Endosome-Lysosome-Autophagy Axis and Immune-Inflammatory Imbalance in Elderly Sepsis.. *Clin Interv Aging*. PMID: 42226934
5. A Stromal-Centered Single-Cell Landscape Identifies POSTN(+) Fibroblasts as a High-Risk Stromal Subset in Hepatocellular Carcinoma.. *Biomarkers*. PMID: 42172061

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 51.4% |
| 置信残基 (pLDDT 70-90) 占比 | 36.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 2.7% |
| 有序区域 (pLDDT>70) 占比 | 88.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.2，有序区 88.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CXCL12 | 0.000 | 0.000 | — |
| CXCL5 | 0.000 | 0.000 | — |
| CCL11 | 0.000 | 0.000 | — |
| CCL21 | 0.000 | 0.000 | — |
| CXCL17 | 0.000 | 0.000 | — |
| CXCL11 | 0.000 | 0.000 | — |
| CXCL9 | 0.000 | 0.000 | — |
| CCL13 | 0.000 | 0.000 | — |
| CCL5 | 0.000 | 0.000 | — |
| CCL17 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q04864 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:A0A6L8PL26 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O95715 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P36406 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q8IYF3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O00399 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75935 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P50452 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q14651 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WYA6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 22
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 22 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 无 | pLDDT=85.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 22 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CXCL14 -- C-X-C motif chemokine 14，研究基础较多，新颖性有限。
2. 蛋白大小111 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 625 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95715
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145824-CXCL14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CXCL14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95715
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
