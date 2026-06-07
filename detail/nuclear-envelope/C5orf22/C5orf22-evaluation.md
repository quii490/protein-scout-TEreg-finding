---
type: protein-evaluation
gene: "C5orf22"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C5orf22 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C5orf22 |
| 蛋白名称 | UPF0489 protein C5orf22 |
| 蛋白大小 | 442 aa / 50.0 kDa |
| UniProt ID | Q49AR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 50.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR024131; Pfam: PF12640 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic contributions to female gout and hyperuricaemia using genome-wide association study and polygenic risk score analyses.. *Rheumatology (Oxford, England)*. PMID: 35758599
2. Integrating Whole-Genome Resequencing and RNA Sequencing Data Reveals Selective Sweeps and Differentially Expressed Genes Related to Nervous System Changes in Luxi Gamecocks.. *Genes*. PMID: 36980855
3. Development and verification of a comprehensive diagnostic model for osteosarcoma using random forest and artificial neural network.. *Discover oncology*. PMID: 41731213
4. A Proteomic Connectivity Map for Characterizing the Tumor Adaptive Response to Small Molecule Chemical Perturbagens.. *ACS chemical biology*. PMID: 31846293

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 73.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 80.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.0，有序区 80.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024131; Pfam: PF12640 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WBP11 | 0.708 | 0.613 | — |
| ELOF1 | 0.599 | 0.596 | — |
| SAYSD1 | 0.594 | 0.000 | — |
| TRMT13 | 0.579 | 0.000 | — |
| C5orf51 | 0.577 | 0.000 | — |
| TPGS2 | 0.574 | 0.000 | — |
| PQBP1 | 0.568 | 0.472 | — |
| OSM | 0.544 | 0.544 | — |
| RGS3 | 0.539 | 0.000 | — |
| KLHL12 | 0.535 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 无 | pLDDT=84.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. C5orf22 — UPF0489 protein C5orf22，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49AR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082213-C5orf22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C5orf22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49AR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000082213-C5orf22/subcellular

![](https://images.proteinatlas.org/43062/460_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43062/460_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43062/465_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43062/465_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43062/467_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43062/467_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49AR2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q49AR2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024131; |
| Pfam | PF12640; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000082213-C5orf22/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| WBP11 | Intact, Biogrid | true |
| DDIT4L | Intact | false |
| ELOF1 | Intact | false |
| NOL9 | Bioplex | false |
| OSM | Bioplex | false |
| SURF2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
