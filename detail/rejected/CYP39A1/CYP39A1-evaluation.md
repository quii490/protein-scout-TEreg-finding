---
type: protein-evaluation
gene: "CYP39A1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP39A1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP39A1 |
| 蛋白名称 | 24-hydroxycholesterol 7-alpha-hydroxylase |
| 蛋白大小 | 469 aa / 54.1 kDa |
| UniProt ID | Q9NYL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 469 aa / 54.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 56 |
| 别名(未计入scoring) |  |

**关键文献**:
1. How cytochrome P450 enzymes in humans are involved in Parkinson's disease: a literature review.. *Neuroscience*. PMID: 41730497
2. Multi-omics analysis reveals gut microbiota remodeling and lipid metabolism regulation during the treatment of nonalcoholic fatty liver disease with Yindan Pinggan capsule.. *Chin Med*. PMID: 41877256
3. Inosine alleviates colorectal cancer liver metastasis by promoting M1 macrophage polarization and modulating the PI3K/AKT signaling pathway.. *Front Immunol*. PMID: 41890717
4. Advances in molecular genetics and multi-omics of exfoliation syndrome.. *Exp Eye Res*. PMID: 41548831
5. Ingenol-Mediated SIRT1-LXRα Signaling Reduces Lipid Accumulation and Alleviates Postmenopausal Liver Damage.. *Phytother Res*. PMID: 41531169

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.9 |
| 高置信度残基 (pLDDT>90) 占比 | 77.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 0.2% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.9，有序区 96.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP46A1 | 0.000 | 0.000 | — |
| HSD3B7 | 0.000 | 0.000 | — |
| CH25H | 0.000 | 0.000 | — |
| NR1H4 | 0.000 | 0.000 | — |
| LSS | 0.000 | 0.000 | — |
| SQLE | 0.000 | 0.000 | — |
| MSMO1 | 0.000 | 0.000 | — |
| FDFT1 | 0.000 | 0.000 | — |
| HSD17B7 | 0.000 | 0.000 | — |
| FAXDC2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NRX5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H7B4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P15104 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P19652 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q15034 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 7
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.9 + PDB: 无 | pLDDT=91.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 7 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYP39A1 -- 24-hydroxycholesterol 7-alpha-hydroxylase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小469 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146233-CYP39A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP39A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYL5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
