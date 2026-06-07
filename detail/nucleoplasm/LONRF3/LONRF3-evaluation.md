---
type: protein-evaluation
gene: "LONRF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LONRF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LONRF3 / RNF127 |
| 蛋白名称 | LON peptidase N-terminal domain and RING finger protein 3 |
| 蛋白大小 | 759 aa / 84.5 kDa |
| UniProt ID | Q496Y0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 759 aa / 84.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003111, IPR046336, IPR015947, IPR011990, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF127 |

**关键文献**:
1. Construction of an E3 Ubiquitin Ligase Gene Model to Predict the Prognosis of Idiopathic Pulmonary Fibrosis Patients Using Integrated Bioinformatics Analysis.. *Current medicinal chemistry*. PMID: 41088915
2. Comprehensive Analysis of E3 Ubiquitin Ligases Reveals Ring Finger Protein 223 as a Novel Oncogene Activated by KLF4 in Pancreatic Cancer.. *Frontiers in cell and developmental biology*. PMID: 34722520

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 50.1% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 27.7% |
| 有序区域 (pLDDT>70) 占比 | 68.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 68.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003111, IPR046336, IPR015947, IPR011990, IPR019734; Pfam: PF02190, PF00097, PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NPAS2 | 0.525 | 0.000 | — |
| PER3 | 0.521 | 0.000 | — |
| PER2 | 0.496 | 0.000 | — |
| ZCCHC18 | 0.488 | 0.000 | — |
| ARNTL | 0.484 | 0.000 | — |
| AGO3 | 0.472 | 0.467 | — |
| NFIL3 | 0.470 | 0.000 | — |
| C22orf31 | 0.447 | 0.000 | — |
| MTMR8 | 0.440 | 0.000 | — |
| RFPL4B | 0.420 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENO1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| PHB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20195357|imex:IM-20475 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CTAG1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DMD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AGO3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DES | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NOTCH2NLA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 13
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 12 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LONRF3 — LON peptidase N-terminal domain and RING finger protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小759 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q496Y0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175556-LONRF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LONRF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q496Y0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000175556-LONRF3/subcellular

![](https://images.proteinatlas.org/50422/742_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/50422/742_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/50422/830_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/50422/830_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/50422/852_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/50422/852_C2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q496Y0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q496Y0 |
| SMART | SM00464;SM00184;SM00028; |
| UniProt Domain [FT] | DOMAIN 546..755; /note="Lon N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01123" |
| InterPro | IPR003111;IPR046336;IPR015947;IPR011990;IPR019734;IPR018957;IPR001841;IPR013083;IPR017907; |
| Pfam | PF02190;PF00097;PF13923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175556-LONRF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPBP2 | Intact | false |
| CTAG1A | Intact | false |
| CTAG1B | Intact | false |
| CYSRT1 | Intact | false |
| DES | Intact | false |
| NOTCH2NLA | Intact | false |
| PHB1 | Intact | false |
| TRAF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
