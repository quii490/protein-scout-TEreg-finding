---
type: protein-evaluation
gene: "DNAJC5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC5 |
| 蛋白名称 | DnaJ homolog subfamily C member 5 |
| 蛋白大小 | 198 aa / 22.1 kDa |
| UniProt ID | Q9H3Z4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Vesicles; 额外: Golgi apparatus, Perinuclear theca, Principal ; UniProt: Cytoplasm, cytosol; Membrane; Cytoplasmic vesicle, secretory |
| 蛋白大小 | 8/10 | x1 | 8 | 198 aa / 22.1 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=82 篇 (<=100->2) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **77.5/180** | |
| **归一化总分** | | | **43.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Golgi apparatus, Perinuclear theca, Principal piece, End piece | Supported |
| UniProt | Cytoplasm, cytosol; Membrane; Cytoplasmic vesicle, secretory vesicle, chromaffin granule membrane; M... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 82 |
| 别名(未计入scoring) |  |

**关键文献**:
1. TDP43 and hnRNP K Regulate Alternative Splicing of DNAJC5.. *Cell Biol Int*. PMID: 41983529
2. Palmitoyl Acyltransferases Control the Membrane Localization of DNAJC5 to Regulate Unconventional Protein Secretion.. *Traffic*. PMID: 41657026
3. Genome-wide characterization of the Hsp40 gene family in Clarias fuscus reveals their roles in thermal stress adaptation and immune modulation.. *Comp Biochem Physiol Part D Genomics Proteomics*. PMID: 41151232
4. From machine learning to causal insight: a robust 12-gene signature to distinguish sepsis risk from systemic inflammatory response syndrome.. *Eur J Med Res*. PMID: 41723546
5. Correction: DNAJC5 promotes cisplatin resistance in epithelial ovarian cancer by autophagy induced by the BiP/IRE1α/XBP1 endoplasmic reticulum stress pathway.. *Sci Rep*. PMID: 41605986

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.6 |
| 高置信度残基 (pLDDT>90) 占比 | 22.7% |
| 置信残基 (pLDDT 70-90) 占比 | 36.4% |
| 中等置信 (pLDDT 50-70) 占比 | 30.3% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.6，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| SYT1 | 0.000 | 0.000 | — |
| VAMP2 | 0.000 | 0.000 | — |
| RAB3A | 0.000 | 0.000 | — |
| PPT1 | 0.000 | 0.000 | — |
| CLN3 | 0.000 | 0.000 | — |
| SLC32A1 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| SYN1 | 0.000 | 0.000 | — |
| SYP | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A0A0G2JX56 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H3Z4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O95782 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:P53680 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q9P2U7 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q16572 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q9H598 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q8NDX2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q8IUH5 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:P60904 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.6 + PDB: 无 | pLDDT=73.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Membrane; Cytoplasmic vesicle, / Vesicles; 额外: Golgi apparatus, Perinuclear theca,  | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: **

**核心优势**:
1. DNAJC5 -- DnaJ homolog subfamily C member 5，研究基础较多，新颖性有限。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3Z4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101152-DNAJC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3Z4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
