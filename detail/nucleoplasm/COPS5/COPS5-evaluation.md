---
type: protein-evaluation
gene: "COPS5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COPS5 — REJECTED (研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPS5 |
| 蛋白名称 | COP9 signalosome complex subunit 5 |
| 蛋白大小 | 334 aa / 37.6 kDa |
| UniProt ID | Q92905 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytosol; Nucleus; Cytoplasm, perinuclear region;  |
| 蛋白大小 | 10/10 | x1 | 10 | 334 aa / 37.6 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=86.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm, cytosol; Nucleus; Cytoplasm, perinuclear region; Cytoplasmic vesicle, secretory vesicle, ... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 405 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrative Transcriptomics Identifies Ubiquitination-Related Genes BIRC2, COPS5, and TBK1 as Novel Biomarkers of T-Cell Dysregulation in Amyotrophic Lateral Sclerosis.. *J Inflamm Res*. PMID: 42117108
2. Nuclear export by COPS5/CSN5/JAB1 mediates vascular smooth muscle cell dedifferentiation in neointimal hyperplasia.. *Cardiovasc Res*. PMID: 41861053
3. Transcriptome Analysis Identifies Proteostasis and Cell Survival Pathway Disruption in Peripartum Cardiomyopathy, Leading to Heart Failure.. *Cells*. PMID: 42041565
4. Machine Learning Identifies TRAPPC13/COPS5 as Biomarkers and Vesicle Transport Subtypes in Parkinson's Disease.. *Can J Neurol Sci*. PMID: 41972297
5. Deubiquitinating enzymes in breast cancer: in silico analysis of gene expression and metastatic correlation.. *J Biomol Struct Dyn*. PMID: 39671715

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.3 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.3，有序区 87.1%），结构可靠。

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
| uniprotkb:P10599 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q92905 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P46527 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P09936 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P32119 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q99489 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NPY3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9P0P8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q7L5N1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P61201 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.3 + PDB: 无 | pLDDT=86.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Cytoplasm, perinuclea / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COPS5 -- COP9 signalosome complex subunit 5，研究基础较多，新颖性有限。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 107 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92905
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121022-COPS5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPS5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92905
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92905-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92905 |
| SMART | SM00232; |
| UniProt Domain [FT] | DOMAIN 55..192; /note="MPN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01182" |
| InterPro | IPR040961;IPR000555;IPR050242;IPR037518; |
| Pfam | PF18323;PF01398; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121022-COPS5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APP | Intact, Biogrid | true |
| ASB6 | Biogrid, Bioplex | true |
| BRSK2 | Intact, Biogrid | true |
| BRWD1 | Intact, Biogrid | true |
| BTBD1 | Biogrid, Bioplex | true |
| BTBD2 | Biogrid, Bioplex | true |
| CCNDBP1 | Intact, Biogrid | true |
| CDKN1B | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
