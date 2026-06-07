---
type: protein-evaluation
gene: "C9orf85"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C9orf85 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C9orf85 |
| 蛋白名称 | Uncharacterized protein C9orf85 |
| 蛋白大小 | 179 aa / 20.2 kDa |
| UniProt ID | Q96MD7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 179 aa / 20.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019351; Pfam: PF10217 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-gene knockout-coupled omics analysis identifies C9orf85 and CXorf38 as two uncharacterized human proteins associated with ZIP8 malfunction.. *Frontiers in molecular biosciences*. PMID: 36330220

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 30.7% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 58.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.8，有序区 58.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019351; Pfam: PF10217 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GVQW2 | 0.717 | 0.000 | — |
| C9orf57 | 0.716 | 0.000 | — |
| BRCC3 | 0.622 | 0.610 | — |
| BABAM1 | 0.611 | 0.608 | — |
| ZFAND5 | 0.610 | 0.000 | — |
| BABAM2 | 0.608 | 0.608 | — |
| CEMIP2 | 0.527 | 0.000 | — |
| TRNAU1AP | 0.514 | 0.000 | — |
| HIGD2B | 0.500 | 0.000 | — |
| C16orf89 | 0.474 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 1 / 12 = 8%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 无 | pLDDT=74.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C9orf85 — Uncharacterized protein C9orf85，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小179 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MD7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155621-C9orf85/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C9orf85
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MD7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000155621-C9orf85/subcellular

![](https://images.proteinatlas.org/50767/712_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/50767/712_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/50767/804_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50767/804_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/50767/964_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50767/964_F10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MD7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96MD7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019351; |
| Pfam | PF10217; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155621-C9orf85/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
