---
type: protein-evaluation
gene: "CRPPA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRPPA — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRPPA / ISPD |
| 蛋白名称 | D-ribitol-5-phosphate cytidylyltransferase |
| 蛋白大小 | 451 aa / 49.9 kDa |
| UniProt ID | A4D126 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 451 aa / 49.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.9; PDB: 4CVH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR034683, IPR040635, IPR018294, IPR029044; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ISPD |

**关键文献**:
1. Involvement of abnormal dystroglycan expression and matriglycan levels in cancer pathogenesis.. *Cancer cell international*. PMID: 36494657
2. Cytidine Diphosphate-Ribitol Analysis for Diagnostics and Treatment Monitoring of Cytidine Diphosphate-l-Ribitol Pyrophosphorylase A Muscular Dystrophy.. *Clinical chemistry*. PMID: 31375477
3. Whole-genome sequencing unravels novel genetic determinants and regulatory pathways associated with triamcinolone acetonide-induced ocular hypertension.. *Molecular genetics and genomics : MGG*. PMID: 36222912
4. Analysis of genotype-phenotype correlation in Walker-Warburg syndrome with a novel CRPPA mutation in different clinical manifestations.. *European journal of ophthalmology*. PMID: 33977792
5. The role of ratio markers based on prealbumin in the diagnosis of periprosthetic joint infection.. *Frontiers in cellular and infection microbiology*. PMID: 40697817

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 72.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 87.8% |
| 可用 PDB 条目 | 4CVH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.9，有序区 87.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034683, IPR040635, IPR018294, IPR029044; Pfam: PF01128, PF18706 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FKTN | 0.978 | 0.000 | — |
| RXYLT1 | 0.801 | 0.000 | — |
| FKRP | 0.776 | 0.104 | — |
| POMT1 | 0.763 | 0.070 | — |
| POMT2 | 0.758 | 0.070 | — |
| B4GAT1 | 0.746 | 0.000 | — |
| POMGNT2 | 0.744 | 0.000 | — |
| ENY2 | 0.726 | 0.636 | — |
| POMK | 0.706 | 0.000 | — |
| DAG1 | 0.700 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCT2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 4CVH | pLDDT=87.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRPPA — D-ribitol-5-phosphate cytidylyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小451 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4D126
- Protein Atlas: https://www.proteinatlas.org/search/CRPPA
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRPPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4D126
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000214960-CRPPA/subcellular

![](https://images.proteinatlas.org/53554/1343_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/53554/1343_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/53554/1347_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/53554/1347_H5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A4D126-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
