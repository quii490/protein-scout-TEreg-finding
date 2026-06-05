---
type: protein-evaluation
gene: "DNAJC24"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC24 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC24 / DPH4, ZCSL3 |
| 蛋白名称 | DnaJ homolog subfamily C member 24 |
| 蛋白大小 | 149 aa / 17.1 kDa |
| UniProt ID | Q6P3W2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC24/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytoskeleton |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 149 aa / 17.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.5; PDB: 2L6L |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001623, IPR007872, IPR036671, IPR036869; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (1张)

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPH4, ZCSL3 |

**关键文献**:
1. DNAJC24 suppresses breast cancer malignancy and serves as a prognostic biomarker.. *Cancer cell international*. PMID: 40713574
2. DNAJC24 is a potential therapeutic target in hepatocellular carcinoma through affecting ammonia metabolism.. *Cell death & disease*. PMID: 35606363
3. Genetic Analysis of HSP40/DNAJ Family Genes in Parkinson's Disease: a Large Case-Control Study.. *Molecular neurobiology*. PMID: 35715682
4. Screening of reliable reference genes for the normalization of RT-qPCR in chicken gastrointestinal tract.. *Poultry science*. PMID: 37918133
5. Establishment of a pig CRISPR/Cas9 knockout library for functional gene screening in pig cells.. *Biotechnology journal*. PMID: 34705337

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 74.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.8% |
| 低置信 (pLDDT<50) 占比 | 4.7% |
| 有序区域 (pLDDT>70) 占比 | 74.5% |
| 可用 PDB 条目 | 2L6L |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.5，有序区 74.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR007872, IPR036671, IPR036869; Pfam: PF00226, PF05207 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF2 | 0.948 | 0.104 | — |
| ELP4 | 0.948 | 0.000 | — |
| IMMP1L | 0.933 | 0.070 | — |
| DCDC1 | 0.932 | 0.000 | — |
| DPH2 | 0.923 | 0.331 | — |
| DPH3 | 0.890 | 0.000 | — |
| MPPED2 | 0.888 | 0.000 | — |
| DPH1 | 0.871 | 0.186 | — |
| DPH5 | 0.818 | 0.000 | — |
| DPH7 | 0.809 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.5 + PDB: 2L6L | pLDDT=74.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC24 — DnaJ homolog subfamily C member 24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小149 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P3W2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170946-DNAJC24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P3W2
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:20

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P3W2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
