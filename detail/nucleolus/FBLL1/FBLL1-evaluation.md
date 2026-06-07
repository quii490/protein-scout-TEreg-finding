---
type: protein-evaluation
gene: "FBLL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBLL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBLL1 |
| 蛋白名称 | RNA 2'-O-methyltransferase FBLL1 |
| 蛋白大小 | 334 aa / 34.8 kDa |
| UniProt ID | A6NHQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 34.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000692, IPR020813, IPR029063; Pfam: PF01269 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- box C/D methylation guide snoRNP complex (GO:0031428)
- Cajal body (GO:0015030)
- fibrillar center (GO:0001650)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of FBLL1 as a neuron-specific RNA 2'-O-methyltransferase mediating neuronal differentiation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39570315
2. Convolvulus arvensis Is a Novel Host of 'Candidatus Phytoplasma omanense'-Related Strains Causing Little Leaf Disease in Jordan.. *Plant disease*. PMID: 40198318
3. Extrachromosomal DNA drives molecular and clinical heterogeneity in hepatocellular carcinoma: a multi-omics analysis and prognostic model development.. *Human genomics*. PMID: 41634868
4. Integrated Multi-Omics and Spatial Transcriptomics Identify FBLL1 as a Malignant Transformation Driver in Hepatocellular Carcinoma.. *Cells*. PMID: 41677613
5. Fibrillarin and fibrillarin-like their role in cancer progression: new approaches and perspectives.. *Molecular biology reports*. PMID: 41524825

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 47.6% |
| 置信残基 (pLDDT 70-90) 占比 | 21.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 29.6% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.5，有序区 68.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000692, IPR020813, IPR029063; Pfam: PF01269 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOP58 | 0.994 | 0.838 | — |
| NOP56 | 0.994 | 0.838 | — |
| DKC1 | 0.992 | 0.841 | — |
| SNU13 | 0.984 | 0.840 | — |
| NOL6 | 0.976 | 0.841 | — |
| NHP2 | 0.974 | 0.507 | — |
| WDR36 | 0.972 | 0.840 | — |
| WDR46 | 0.972 | 0.841 | — |
| GAR1 | 0.969 | 0.293 | — |
| RRP9 | 0.968 | 0.839 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| LIN28A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SRSF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BMI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |
| CEP63 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:35709258|imex:IM-29848 |
| DDX6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 无 | pLDDT=75.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli fibrillar center; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBLL1 — RNA 2'-O-methyltransferase FBLL1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NHQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188573-FBLL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBLL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NHQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (supported)。来源: https://www.proteinatlas.org/ENSG00000188573-FBLL1/subcellular

![](https://images.proteinatlas.org/49546/756_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49546/756_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49546/760_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49546/760_G8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/49546/775_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49546/775_G8_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NHQ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NHQ2 |
| SMART | SM01206; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000692;IPR020813;IPR029063; |
| Pfam | PF01269; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188573-FBLL1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
