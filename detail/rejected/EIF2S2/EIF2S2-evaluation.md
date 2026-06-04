---
type: protein-evaluation
gene: "EIF2S2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF2S2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2S2 |
| 蛋白名称 | Eukaryotic translation initiation factor 2 subunit 2 |
| 蛋白大小 | 333 aa / 38.4 kDa |
| UniProt ID | P20042 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum; 额外: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 333 aa / 38.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 51 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Exploring the key functions of T cells and the regulation of the immune microenvironment in prostate cancer using single-cell RNA sequencing and bulk RNA sequencing.. *Autoimmunity*. PMID: 41474172
2. Characterization of lactylation-related subtypes and diagnostic markers in myocardial ischemic reperfusion injury using weighted gene coexpression network analysis and machine learning.. *Front Immunol*. PMID: 42093976
3. EIF4A3-induced circEIF2S2 facilitates colorectal cancer growth, metastasis, and immune suppression via the miR-646/UHMK1 Axis.. *Int J Biol Macromol*. PMID: 41544785
4. Oocyte-specific knockout of eIF2 subunits causes apoptosis of mouse oocytes within the early growing follicles via mitochondrial dysfunctions and DNA damage.. *Cell Death Dis*. PMID: 41629280
5. A pilot study on DNA methylation changes for non-invasive molecular diagnostics in heart failure.. *ESC Heart Fail*. PMID: 40898655

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 42.0% |
| 有序区域 (pLDDT>70) 占比 | 46.2% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 46.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2S1 | 0.000 | 0.000 | — |
| EIF2B1 | 0.000 | 0.000 | — |
| EIF2S3 | 0.000 | 0.000 | — |
| EIF2B2 | 0.000 | 0.000 | — |
| EIF5 | 0.000 | 0.000 | — |
| EIF2B3 | 0.000 | 0.000 | — |
| EIF2B5 | 0.000 | 0.000 | — |
| EIF1 | 0.000 | 0.000 | — |
| EIF3C | 0.000 | 0.000 | — |
| EIF3B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q04724 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P04637 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q13432 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P51693 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9GZT6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q14194 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| intact:EBI-473810 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9P2H0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q05516 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y4G2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Endoplasmic reticulum; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF2S2 — Eukaryotic translation initiation factor 2 subunit 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小333 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20042
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125977-EIF2S2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2S2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20042
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
