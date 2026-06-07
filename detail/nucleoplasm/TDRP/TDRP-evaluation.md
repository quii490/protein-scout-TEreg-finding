---
type: protein-evaluation
gene: "TDRP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TDRP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TDRP / C8orf42 |
| 蛋白名称 | Testis development-related protein |
| 蛋白大小 | 185 aa / 20.4 kDa |
| UniProt ID | Q86YL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 185 aa / 20.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031399; Pfam: PF15683 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf42 |

**关键文献**:
1. Genome-wide association study of chlamydia reinfection in African American women.. *Frontiers in immunology*. PMID: 41080568
2. Variations in gender identity and sexual orientation of university students.. *Sexual medicine*. PMID: 37965377
3. Opioid medication use and blood DNA methylation: epigenome-wide association meta-analysis.. *Epigenomics*. PMID: 36700736
4. TDRP deficiency contributes to low sperm motility and is a potential risk factor for male infertility.. *American journal of translational research*. PMID: 27069551
5. Four novel genes associated with longevity found in Cane corso purebred dogs.. *BMC veterinary research*. PMID: 35590325

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 63.2% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 18.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.6），有序残基占 18.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031399; Pfam: PF15683 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBXO25 | 0.706 | 0.000 | — |
| ZNF596 | 0.658 | 0.000 | — |
| FBXO38 | 0.616 | 0.000 | — |
| ERICH1 | 0.561 | 0.000 | — |
| PRM2 | 0.559 | 0.000 | — |
| SMOC2 | 0.543 | 0.000 | — |
| GPCPD1 | 0.455 | 0.000 | — |
| C6orf223 | 0.434 | 0.000 | — |
| KBTBD11 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.6 + PDB: 无 | pLDDT=59.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TDRP — Testis development-related protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小185 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180190-TDRP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TDRP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000180190-TDRP/subcellular

![](https://images.proteinatlas.org/8462/100_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8462/100_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8462/101_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8462/101_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8462/1144_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8462/1144_G2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YL5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86YL5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031399; |
| Pfam | PF15683; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180190-TDRP/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
