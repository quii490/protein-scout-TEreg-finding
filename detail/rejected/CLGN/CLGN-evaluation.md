---
type: protein-evaluation
gene: "CLGN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLGN — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLGN |
| 蛋白名称 | Calmegin |
| 蛋白大小 | 610 aa / 70.0 kDa |
| UniProt ID | O14967 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum; 额外: Equatorial segment, Mid piece; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 610 aa / 70.0 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=76.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Equatorial segment, Mid piece | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 43 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Design and Validation of a Predictive Model for Hepatocellular Carcinoma Based on Genes With Differential Expression Driven by DNA Methylation.. *Int J Genomics*. PMID: 41607685
2. Identifying Key Regulators in Odorant Receptor Trafficking.. *J Neurosci*. PMID: 41125435
3. Identification of novel differentiation trajectories and gene network associations with ectopic pregnancy in fallopian tube epithelium.. *Hum Reprod*. PMID: 41183511
4. Alterations of the gut commensal Akkermansia muciniphila in patients with COVID-19.. *Virulence*. PMID: 40360188
5. Targeting endoplasmic reticulum stress-induced CLGN resensitizes hepatocellular carcinoma to apoptosis: paeonol synergistically enhances efficacy by dual inhibition of CLGN and NF-κB.. *Front Oncol*. PMID: 41395613

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 24.6% |
| 有序区域 (pLDDT>70) 占比 | 71.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.2，有序区 71.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADAM2 | 0.000 | 0.000 | — |
| EFTUD2 | 0.000 | 0.000 | — |
| HSP90B1 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| PDILT | 0.000 | 0.000 | — |
| CALR3 | 0.000 | 0.000 | — |
| MOGS | 0.000 | 0.000 | — |
| ANKRD45 | 0.000 | 0.000 | — |
| CALR | 0.000 | 0.000 | — |
| PDIA3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NZC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P51811 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O14967 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O95864 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q96GX1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 无 | pLDDT=76.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum; 额外: Equatorial segment, Mid | 一致 |
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
1. CLGN -- Calmegin，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小610 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14967
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153132-CLGN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLGN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14967
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14967-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
