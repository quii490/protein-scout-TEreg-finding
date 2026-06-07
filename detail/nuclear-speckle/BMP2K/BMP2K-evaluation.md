---
type: protein-evaluation
gene: "BMP2K"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BMP2K 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMP2K / BIKE |
| 蛋白名称 | BMP-2-inducible protein kinase |
| 蛋白大小 | 1161 aa / 129.2 kDa |
| UniProt ID | Q9NSY1 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:40:25 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 7/10 | x1 | 7 | 1161 aa / 129.2 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=32 篇 (21-40->8) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=55.0; PDB: 4W9W, 4W9X, ... |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 5; Pfam: 2; IPR051744, IPR028182... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **150.5/180** | |
| **归一化总分 (/1.83)** | | | **82.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 1161 aa，蛋白偏大（> 800 aa），表达纯化有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BIKE |

**关键文献**:
1. ZNF384-Related Fusion Genes in Acute Lymphoblastic Leukemia.. *Cancer control : journal of the Moffitt Cancer Center*. PMID: 37306722
2. BMP2K phosphorylates AP-2 and regulates clathrin-mediated endocytosis.. *Traffic (Copenhagen, Denmark)*. PMID: 34480404
3. Subcellular distribution of bone morphogenetic protein 2-inducible kinase (BMP2K): Regulation by liquid-liquid phase separation and nucleocytoplasmic shuttling.. *Biochemical and biophysical research communications*. PMID: 36739695
4. Splicing variation of BMP2K balances abundance of COPII assemblies and autophagic degradation in erythroid cells.. *eLife*. PMID: 32795391
5. BMP2K dysregulation promotes abnormal megakaryopoiesis in acute megakaryoblastic leukemia.. *Cell & bioscience*. PMID: 32322386

**评价**: 较高新颖性，研究尚处早期阶段（PubMed 21-40篇）。新颖性评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 64.5% |
| 有序区域 (pLDDT>70) 占比 | 30.5% |
| 可用 PDB 条目 | 4W9W, 4W9X, 5I3O, 5I3R, 5IKW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=55.0），大部分区域无序。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051744, IPR028182, IPR011009, IPR000719, IPR008271; Pfam: PF15282, PF00069 |

**染色质调控潜力分析**: 存在 7 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REPS1 | 0.877 | 0.829 | -- |
| PICALM | 0.850 | 0.802 | -- |
| NUMB | 0.824 | 0.499 | -- |
| AP2S1 | 0.822 | 0.812 | -- |
| AP2M1 | 0.818 | 0.749 | -- |
| AP2B1 | 0.789 | 0.777 | -- |
| NUMBL | 0.750 | 0.322 | -- |
| CLINT1 | 0.732 | 0.726 | -- |
| RALBP1 | 0.731 | 0.713 | -- |
| RUNDC3A | 0.684 | 0.665 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1380999 | pull down | pubmed:17721511|imex:IM-19952 |
| EBI-1380405 | pull down | pubmed:17721511|imex:IM-19952 |
| EBI-1380972 | pull down | pubmed:17721511|imex:IM-19952 |
| 38943" | pull down | pubmed:17721511|imex:IM-19952 |
| 38918" | pull down | pubmed:17721511|imex:IM-19952 |
| BCR/ABL fusion | anti bait coimmunoprecipitation | pubmed:19380743|imex:IM-20432 |
| EPS15 | tandem affinity purification | pubmed:19380743|imex:IM-20432 |
| FN1 | cross-linking study | imex:IM-14135|pubmed:19738201 |
| TGOLN2 | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| OXCT1 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 4W9W, 4W9X, 5I3O | pLDDT=55.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nuclear speckles / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 82.2/100

**核心优势**:
1. BMP2K -- BMP-2-inducible protein kinase，较高新颖性，研究尚处早期阶段。
2. 已有PDB实验结构：4W9W, 4W9X, 5I3O。
3. 存在 7 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. AlphaFold pLDDT 较低（55.0），存在显著无序区

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NSY1
- Protein Atlas: https://www.proteinatlas.org/search/BMP2K
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMP2K
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSY1
- STRING: https://string-db.org/network/9606.BMP2K
- Packet data timestamp: 2026-06-03 03:40:25

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000138756-BMP2K/subcellular

![](https://images.proteinatlas.org/26451/604_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/26451/604_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/26451/607_H1_4_red_green.jpg)
![](https://images.proteinatlas.org/26451/607_H1_5_red_green.jpg)
![](https://images.proteinatlas.org/26451/609_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/26451/609_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NSY1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NSY1 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 51..316; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR051744;IPR028182;IPR011009;IPR000719;IPR008271; |
| Pfam | PF15282;PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138756-BMP2K/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP2B1 | Biogrid, Opencell | true |
| AP2S1 | Biogrid, Opencell | true |
| CLTA | Biogrid, Opencell | true |
| RALBP1 | Biogrid, Bioplex | true |
| RUNDC3A | Intact, Biogrid | true |
| ACAA1 | Intact | false |
| AP1B1 | Biogrid | false |
| AP2A2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
