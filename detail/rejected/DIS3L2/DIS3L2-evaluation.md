---
type: protein-evaluation
gene: "DIS3L2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DIS3L2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=126，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIS3L2 |
| 蛋白名称 | DIS3-like exonuclease 2 |
| 蛋白大小 | 885 aa / 99.3 kDa |
| UniProt ID | Q8IYB7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm, P-body |
| 蛋白大小 | 8/10 | ×1 | 8 | 885 aa / 99.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=126 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 19 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.0/180** | |
| **归一化总分** | | | **32.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm; Cytoplasm, P-body | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 126 |
| PubMed broad count | 127 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The long isoform of ZAP coordinates multiple enzymes to mediate complete decay of target transcripts.. *Cell Rep*. PMID: 42054207
2. Systematic Review: Prognostic Molecular Biomarkers in Wilms Tumors.. *JCO Precis Oncol*. PMID: 42150146
3. Mechanism of nucleolytic degradation of human ribosomes.. *bioRxiv*. PMID: 42094531
4. Prolonged Survival With Homozygous Deletion of Exon 9 in Perlman Syndrome: A Case Report.. *Case Rep Genet*. PMID: 42040973
5. MiRNA Stability and Degradation: Dynamic Regulators of Cellular Regulatory Networks.. *Wiley Interdiscip Rev RNA*. PMID: 41608885

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 71.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 80.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DIS3L2/DIS3L2-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 80.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC10 | 0.000 | 0.000 | — |
| EXOSC4 | 0.000 | 0.000 | — |
| EXOSC5 | 0.000 | 0.000 | — |
| EXOSC3 | 0.000 | 0.000 | — |
| EXOSC1 | 0.000 | 0.000 | — |
| EXOSC9 | 0.000 | 0.000 | — |
| EXOSC8 | 0.000 | 0.000 | — |
| C1D | 0.000 | 0.000 | — |
| EXOSC7 | 0.000 | 0.000 | — |
| EXOSC2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9W0T7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IYB7 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P30101 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q7L5N1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q99689 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P08670 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 19
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 19 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, P-body / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 19 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DIS3L2 — DIS3-like exonuclease 2，研究基础较多，新颖性有限。
2. 蛋白大小885 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 126 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYB7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144535-DIS3L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIS3L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYB7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DIS3L2/DIS3L2-PAE.png]]
