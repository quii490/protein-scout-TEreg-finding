---
type: protein-evaluation
gene: "NT5C1B"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NT5C1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NT5C1B / AIRP |
| 蛋白名称 | Cytosolic 5'-nucleotidase 1B |
| 蛋白大小 | 610 aa / 68.8 kDa |
| UniProt ID | Q96P26 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Catalyzes the hydrolysis of nucleotide monophosphates, releasing inorganic phosphate and the corresponding nucleoside, AMP is the major substrate

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Plasma membrane; 额外: Nucleoplasm, Connecting piece; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 610 aa / 68.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010394; Pfam: PF06189 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Plasma membrane; 额外: Nucleoplasm, Connecting piece, Mid piece | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像**: HPA 记录中该基因有可用 IF 图像（`if_display_images_available`），但未生成本地 IF 嵌入。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AIRP |

**关键文献**:
1. Transcriptome analysis of chicken fibroblast following transforming growth factor β1-mediated activation.. *Poultry science*. PMID: 40729813
2. Cancer-testis antigen expression in canine melanoma and healthy tissues.. *Veterinary immunology and immunopathology*. PMID: 40359694
3. NT5C1B and FH are closely associated with cryoprotectant tolerance in spermatozoa.. *Andrology*. PMID: 31168966
4. NT5C1B Improves Fertility of Boar Spermatozoa by Enhancing Quality and Cryotolerance During Cryopreservation.. *Animals : an open access journal from MDPI*. PMID: 41463814
5. Gene-deficient mouse model established by CRISPR/Cas9 system reveals 15 reproductive organ-enriched genes dispensable for male fertility.. *Frontiers in cell and developmental biology*. PMID: 38835510

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 30.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 42.1% |
| 有序区域 (pLDDT>70) 占比 | 49.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 49.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010394; Pfam: PF06189 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NT5M | 0.961 | 0.000 | — |
| NT5C | 0.958 | 0.000 | — |
| NT5C3B | 0.958 | 0.000 | — |
| NT5C2 | 0.950 | 0.000 | — |
| NT5C3A | 0.947 | 0.000 | — |
| DCK | 0.933 | 0.000 | — |
| ADSS1 | 0.932 | 0.071 | — |
| ITPA | 0.928 | 0.000 | — |
| ADSL | 0.925 | 0.000 | — |
| NT5E | 0.924 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 无 | pLDDT=63.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoli, Plasma membrane; 额外: Nucleoplasm, Connec | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NT5C1B — Cytosolic 5'-nucleotidase 1B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小610 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96P26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185013-NT5C1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NT5C1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96P26-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96P26 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010394; |
| Pfam | PF06189; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185013-NT5C1B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
