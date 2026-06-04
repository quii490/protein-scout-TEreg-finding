---
type: protein-evaluation
gene: "CARHSP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARHSP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARHSP1 |
| 蛋白名称 | Calcium-regulated heat-stable protein 1 |
| 蛋白大小 | 147 aa / 15.9 kDa |
| UniProt ID | Q9Y2V2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm, P-body; Cytoplasmic granule |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 147 aa / 15.9 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm; Cytoplasm, P-body; Cytoplasmic granule | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 29 |
| 别名(未计入scoring) |  |

**关键文献**:
1. RNA-binding proteins in the mouse lens: Functional classifications, expression profiling, and interaction studies of Carhsp1 with crystallin mRNAs.. *Dev Biol*. PMID: 42061735
2. Modulation of the Stress Granule Component Carhsp1 Mitigates Disease-Associated Deficits in Spinocerebellar Ataxia Type 3 Mouse Models.. *Mov Disord*. PMID: 41853947
3. The Combined Expression Profiles of Epigenetic Biomarkers Reveal Heterogeneity in Normospermic Human Sperm Samples.. *Genes (Basel)*. PMID: 41300766
4. A chemical epigenetic tool to probe site-specific DNA-binding protein complexes.. *Proc Natl Acad Sci U S A*. PMID: 41037631
5. A Chemical Epigenetic Probe to Capture the Site-Specific DNA-Binding Protein Complex.. *Res Sq*. PMID: 40162224

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 78.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CARHSP1/CARHSP1-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 78.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITFG2 | 0.000 | 0.000 | — |
| KPTN | 0.000 | 0.000 | — |
| LITAFD | 0.000 | 0.000 | — |
| SPNS3 | 0.000 | 0.000 | — |
| DIS3L2 | 0.000 | 0.000 | — |
| RAB3IL1 | 0.000 | 0.000 | — |
| DIS3L | 0.000 | 0.000 | — |
| DIS3 | 0.000 | 0.000 | — |
| PNPT1 | 0.000 | 0.000 | — |
| SLC38A7 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O76061 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y2V2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9ULX6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H8Y8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P0DPK4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q9UJV3-2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P60410 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:A8MQ03 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q3LI67 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q8ND90 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, P-body; Cytoplasmic granule / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CARHSP1 — Calcium-regulated heat-stable protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小147 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2V2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153048-CARHSP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARHSP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2V2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CARHSP1/CARHSP1-PAE.png]]
