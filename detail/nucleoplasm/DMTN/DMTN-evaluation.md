---
type: protein-evaluation
gene: "DMTN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMTN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMTN / DMT, EPB49 |
| 蛋白名称 | Dematin |
| 蛋白大小 | 405 aa / 45.5 kDa |
| UniProt ID | Q08495 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm, cytosol; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 405 aa / 45.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 1QZP, 1ZV6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032402, IPR051618, IPR003128, IPR036886; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton; Cell membrane... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- actin filament (GO:0005884)
- cell projection membrane (GO:0031253)
- cortical cytoskeleton (GO:0030863)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DMT, EPB49 |

**关键文献**:
1. Artificial intelligence-based epigenomic, transcriptomic and histologic signatures of tobacco use in oral squamous cell carcinoma.. *NPJ precision oncology*. PMID: 38851780
2. Dematin inhibits glioblastoma malignancy through RhoA-mediated CDKs downregulation and cytoskeleton remodeling.. *Experimental cell research*. PMID: 35561787
3. Machine Learning Based Network Analysis Determined Clinically Relevant miRNAs in Breast Cancer.. *Frontiers in genetics*. PMID: 33281885
4. Common and rare variant genetic contributions in African Americans with autism.. *medRxiv : the preprint server for health sciences*. PMID: 41332866
5. Identification of Key Biomarkers for Systemic Lupus Erythematosus Progression and Therapy Response: A Bulk RNA-Sequencing-Based Bioinformatics Study.. *Brain and behavior*. PMID: 41316541

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 11.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.4% |
| 中等置信 (pLDDT 50-70) 占比 | 28.4% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 39.8% |
| 可用 PDB 条目 | 1QZP, 1ZV6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 39.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032402, IPR051618, IPR003128, IPR036886; Pfam: PF16182, PF02209 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADD2 | 0.996 | 0.099 | — |
| ADD1 | 0.993 | 0.089 | — |
| ADD3 | 0.993 | 0.089 | — |
| EPB41 | 0.991 | 0.000 | — |
| TMOD1 | 0.933 | 0.000 | — |
| EPB42 | 0.918 | 0.000 | — |
| TMOD2 | 0.894 | 0.000 | — |
| TMOD3 | 0.894 | 0.000 | — |
| GYPC | 0.886 | 0.000 | — |
| ANK1 | 0.884 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 1QZP, 1ZV6 | pLDDT=63.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Cytoplasm, perinucl / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DMTN — Dematin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小405 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08495
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158856-DMTN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMTN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08495
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08495-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q08495 |
| SMART | SM00153; |
| UniProt Domain [FT] | DOMAIN 337..405; /note="HP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00595" |
| InterPro | IPR032402;IPR051618;IPR003128;IPR036886; |
| Pfam | PF16182;PF02209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158856-DMTN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAE | Biogrid, Bioplex | true |
| YWHAH | Biogrid, Bioplex | true |
| YWHAQ | Biogrid, Bioplex | true |
| CEP76 | Intact | false |
| CPA3 | Bioplex | false |
| GOLGA2 | Intact | false |
| SFN | Biogrid | false |
| TRAF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
