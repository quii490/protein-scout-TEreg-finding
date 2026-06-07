---
type: protein-evaluation
gene: "MAGIX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGIX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGIX |
| 蛋白名称 | PDZ domain-containing protein MAGIX |
| 蛋白大小 | 334 aa / 35.3 kDa |
| UniProt ID | Q9H6Y5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic chromosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 35.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 2DJT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030031, IPR001478, IPR036034; Pfam: PF00595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GHT-SELEX demonstrates unexpectedly high intrinsic sequence specificity and complex DNA binding of many human transcription factors.. *bioRxiv : the preprint server for biology*. PMID: 39605368
2. Construction and Analysis of a circRNA-Mediated ceRNA Network in Lung Adenocarcinoma.. *OncoTargets and therapy*. PMID: 34135596

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.3% |
| 低置信 (pLDDT<50) 占比 | 36.8% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 2DJT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030031, IPR001478, IPR036034; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC26 | 0.763 | 0.763 | — |
| ANAPC16 | 0.707 | 0.707 | — |
| ANAPC7 | 0.699 | 0.699 | — |
| ANAPC2 | 0.690 | 0.690 | — |
| ANAPC4 | 0.646 | 0.646 | — |
| ANAPC5 | 0.622 | 0.622 | — |
| CDC23 | 0.604 | 0.604 | — |
| ANAPC1 | 0.601 | 0.601 | — |
| CDC27 | 0.594 | 0.594 | — |
| CDC16 | 0.540 | 0.540 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBA52 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC13 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ERCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TJP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PMPCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 2DJT | pLDDT=61.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Mitotic chromosome | 待确认 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAGIX — PDZ domain-containing protein MAGIX，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6Y5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000269313-MAGIX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGIX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6Y5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000269313-MAGIX/subcellular

![](https://images.proteinatlas.org/7390/1843_E2_19_cr5b07c7dd3ce0b_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1843_E2_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1868_C2_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1868_C2_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1925_B8_16_cr5cd568559d2a6_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1925_B8_29_cr5cd568559f340_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H6Y5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H6Y5 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 125..209; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR030031;IPR001478;IPR036034; |
| Pfam | PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000269313-MAGIX/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
