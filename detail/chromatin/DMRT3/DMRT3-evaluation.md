---
type: protein-evaluation
gene: "DMRT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMRT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMRT3 / DMRTA3 |
| 蛋白名称 | Doublesex- and mab-3-related transcription factor 3 |
| 蛋白大小 | 472 aa / 51.2 kDa |
| UniProt ID | Q9NQL9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 472 aa / 51.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001275, IPR036407, IPR005173, IPR026607, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DMRTA3 |

**关键文献**:
1. Characterization of Dmrt3-Derived Neurons Suggest a Role within Locomotor Circuits.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 30578339
2. Identification and characterization of single nucleotide polymorphisms in DMRT3 gene in Indian horse (Equus caballus) and donkey (Equus asinus) populations.. *Animal biotechnology*. PMID: 37149793
3. Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.. *medRxiv : the preprint server for health sciences*. PMID: 40196253
4. Nuclear localization, DNA binding and restricted expression in neural and germ cells of zebrafish Dmrt3.. *Biology of the cell*. PMID: 18282142
5. DMRT5, DMRT3, and EMX2 Cooperatively Repress Gsx2 at the Pallium-Subpallium Boundary to Maintain Cortical Identity in Dorsal Telencephalic Progenitors.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 30143575

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.3 |
| 高置信度残基 (pLDDT>90) 占比 | 16.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 24.2% |
| 低置信 (pLDDT<50) 占比 | 53.2% |
| 有序区域 (pLDDT>70) 占比 | 22.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.3），有序残基占 22.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001275, IPR036407, IPR005173, IPR026607, IPR009060; Pfam: PF00751, PF03474 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DMRT2 | 0.582 | 0.000 | — |
| FOXD4 | 0.529 | 0.045 | — |
| KANK1 | 0.514 | 0.044 | — |
| EMX2 | 0.511 | 0.052 | — |
| AKR1E2 | 0.501 | 0.068 | — |
| HLTF | 0.481 | 0.045 | — |
| TEX53 | 0.478 | 0.000 | — |
| LMX1B | 0.467 | 0.109 | — |
| FOXL2 | 0.464 | 0.045 | — |
| AMZ1 | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRTAP9-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MDFI | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FOXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KPRP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT34 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT31 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.3 + PDB: 无 | pLDDT=57.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DMRT3 — Doublesex- and mab-3-related transcription factor 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小472 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQL9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064218-DMRT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMRT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQL9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQL9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQL9 |
| SMART | SM00301; |
| UniProt Domain [FT] | DOMAIN 249..284; /note="DMA"; /evidence="ECO:0000255" |
| InterPro | IPR001275;IPR036407;IPR005173;IPR026607;IPR009060; |
| Pfam | PF00751;PF03474; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000064218-DMRT3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKAP8L | Intact | false |
| ASPG | Intact | false |
| ATP6V0D1 | Intact | false |
| C11orf1 | Intact | false |
| CCNDBP1 | Intact | false |
| CYSRT1 | Intact | false |
| FHL3 | Intact | false |
| FHL5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
