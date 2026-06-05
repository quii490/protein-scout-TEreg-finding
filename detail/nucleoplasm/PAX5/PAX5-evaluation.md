---
type: protein-evaluation
gene: "PAX5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX5 — REJECTED (研究热度过高 (PubMed strict=1218，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX5 |
| 蛋白名称 | Paired box protein Pax-5 |
| 蛋白大小 | 391 aa / 42.1 kDa |
| UniProt ID | Q02548 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1218 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 1K78, 1MDM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1218 |
| PubMed broad count | 2440 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PAX5-driven subtypes of B-progenitor acute lymphoblastic leukemia.. *Nature genetics*. PMID: 30643249
2. Disruption of the sorcin‒PAX5 protein‒protein interaction induces ferroptosis by promoting the FBXL12-mediated ubiquitination of ALDH1A1 in pancreatic cancer.. *Journal of hematology & oncology*. PMID: 40055736
3. Whole-transcriptome analysis in acute lymphoblastic leukemia: a report from the DFCI ALL Consortium Protocol 16-001.. *Blood advances*. PMID: 34933343
4. Transcriptional function of E2A, Ebf1, Pax5, Ikaros and Aiolos analyzed by in vivo acute protein degradation in early B cell development.. *Nature immunology*. PMID: 39179932
5. PAX5 alterations in B-cell acute lymphoblastic leukemia.. *Frontiers in oncology*. PMID: 36387144

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 46.5% |
| 有序区域 (pLDDT>70) 占比 | 37.9% |
| 可用 PDB 条目 | 1K78, 1MDM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 37.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043565; Pfam: PF00292, PF12403 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ETS1 | 0.996 | 0.922 | — |
| EBF1 | 0.985 | 0.000 | — |
| IKZF1 | 0.954 | 0.047 | — |
| IRF4 | 0.950 | 0.000 | — |
| CD79A | 0.946 | 0.000 | — |
| TLE4 | 0.936 | 0.510 | — |
| BCL6 | 0.931 | 0.047 | — |
| RUNX1 | 0.920 | 0.331 | — |
| CD19 | 0.918 | 0.000 | — |
| PRDM1 | 0.907 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DAXX | psi-mi:"MI:0018"(two hybrid) | pubmed:11799127 |
| lysU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE3A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:29426014|imex:IM-26302| |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000122367 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| KLHL38 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBXN7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OSGIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LARP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCNC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 1K78, 1MDM | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PAX5 — Paired box protein Pax-5，研究基础较多，新颖性有限。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1218 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1218 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02548
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196092-PAX5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02548
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196092-PAX5/subcellular

![](https://images.proteinatlas.org/56394/1354_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/56394/1354_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/56394/1362_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/56394/1362_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/56394/2055_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/56394/2055_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02548-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
