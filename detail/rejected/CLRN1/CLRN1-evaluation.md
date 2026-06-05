---
type: protein-evaluation
gene: "CLRN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLRN1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLRN1 |
| 蛋白名称 | Clarin-1 |
| 蛋白大小 | 232 aa / 25.7 kDa |
| UniProt ID | P58418 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Centrosome; 额外: Vesicles, Basal body; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 232 aa / 25.7 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=90.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Vesicles, Basal body | Uncertain |
| UniProt | Cell membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 103 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Compensatory Interplay Between Clarin-1 and Clarin-2 Deafness-Associated Proteins Governs Phenotypic Variability in Hearing.. *Adv Sci (Weinh)*. PMID: 41572507
2. Genes linked to hearing and vestibular phenotypes in humans and mice: an interspecies systematic review.. *Hum Genomics*. PMID: 41430327
3. Identification of novel ceRNA networks associated with system hemostasis and their prognostic implication in lung squamous cell carcinoma.. *J Thromb Thrombolysis*. PMID: 41405758
4. Identification of a variant in the USH1G gene in a family with Usher syndrome.. *Biomedica*. PMID: 41060164
5. Clinical and genetic characterisation of childhood-onset sensorineural hearing loss reveal associated phenotypes and enrichment of pathogenic founder mutations in the Finnish population.. *Int J Audiol*. PMID: 39422539

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 77.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 88.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 88.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYO7A | 0.000 | 0.000 | — |
| USH1C | 0.000 | 0.000 | — |
| USH1G | 0.000 | 0.000 | — |
| WHRN | 0.000 | 0.000 | — |
| USH2A | 0.000 | 0.000 | — |
| PCDH15 | 0.000 | 0.000 | — |
| ADGRV1 | 0.000 | 0.000 | — |
| CDH23 | 0.000 | 0.000 | — |
| CIB2 | 0.000 | 0.000 | — |
| CACNG2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P58418 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q8NHW4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9NRS4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9NV12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q6PL45-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9H0R3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IXM6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q96MV8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q53HI1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BVK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 无 | pLDDT=90.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Centrosome; 额外: Vesicles, Basal body | 一致 |
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
1. CLRN1 -- Clarin-1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小232 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58418
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163646-CLRN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLRN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58418
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (uncertain)。来源: https://www.proteinatlas.org/ENSG00000163646-CLRN1/subcellular

![](https://images.proteinatlas.org/54031/1453_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54031/1453_E4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/54031/1484_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54031/1484_E4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/54031/2145_G4_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/54031/2145_G4_29_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58418-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
