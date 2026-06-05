---
type: protein-evaluation
gene: "CAPN11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAPN11 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAPN11 |
| 蛋白名称 | Calpain-11 |
| 蛋白大小 | 739 aa / 84.4 kDa |
| UniProt ID | Q9UMQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mid piece, Principal piece, End piece; 额外: Acrosome, Equator; UniProt: Cytoplasmic vesicle, secretory vesicle, acrosome |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 739 aa / 84.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 6 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mid piece, Principal piece, End piece; 额外: Acrosome, Equatorial segment | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle, acrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 16 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Non-Mendelian inheritance of DNA methylation patterns in mice.. *Nat Genet*. PMID: 42162411
2. ZFP92, a KRAB domain zinc finger protein enriched in pancreatic islets, binds to B1/Alu SINE transposable elements and regulates retroelements and genes.. *PLoS Genet*. PMID: 37155670
3. Sex-Specific Whole-Transcriptome Analysis in the Cerebral Cortex of FAE Offspring.. *Cells*. PMID: 36672262
4. A genome-wide association study of obstructive heart defects among participants in the National Birth Defects Prevention Study.. *Am J Med Genet A*. PMID: 35451555
5. The gene regulatory network in different brain regions of neuropathic pain mouse models.. *Eur Rev Med Pharmacol Sci*. PMID: 32432769

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 58.3% |
| 置信残基 (pLDDT 70-90) 占比 | 31.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAPN11/CAPN11-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=86.8，有序区 90.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAST | 0.000 | 0.000 | — |
| CAPNS1 | 0.000 | 0.000 | — |
| CAPNS2 | 0.000 | 0.000 | — |
| SPATS1 | 0.000 | 0.000 | — |
| SPATA3 | 0.000 | 0.000 | — |
| SPACA4 | 0.000 | 0.000 | — |
| FAM71F1 | 0.000 | 0.000 | — |
| LRGUK | 0.000 | 0.000 | — |
| UBQLN3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9UMQ6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P13051 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P10644 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NYG5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O75821 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 6
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 无 | pLDDT=86.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, acrosome / Mid piece, Principal piece, End piece; 额外: Acrosom | 一致 |
| PPI | STRING + IntAct | 9 + 6 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CAPN11 — Calpain-11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小739 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137225-CAPN11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAPN11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CAPN11/CAPN11-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mid piece (approved)。来源: https://www.proteinatlas.org/ENSG00000137225-CAPN11/subcellular

![](https://images.proteinatlas.org/30955/2217_C10_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/30955/2217_C10_45_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
