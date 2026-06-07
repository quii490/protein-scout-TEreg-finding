---
type: protein-evaluation
gene: "B4GALNT4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## B4GALNT4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | B4GALNT4 / 无 |
| 蛋白名称 | N-acetyl-beta-glucosaminyl-glycoprotein 4-beta-N-acetylgalactosaminyltransferase 1 |
| 蛋白大小 | 1039 aa / 116.5 kDa |
| UniProt ID | Q76KP1 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:28:24 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: G... |
| 蛋白大小 | 7/10 | x1 | 7 | 1039 aa / 116.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=69.8 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 5; Pfam: 1; IPR008428, IPR051227... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 14 partners; IntAct 9 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **147.5/180** | |
| **归一化总分 (/1.83)** | | | **80.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Vesicles, Cytosol | Uncertain |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- Golgi cisterna membrane (GO:0032580)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 1039 aa，蛋白偏大（> 800 aa），表达纯化有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 23 |

**关键文献**:
1. Expression and Malignant Potential of B4GALNT4 in Esophageal Squamous Cell Carcinoma.. *Annals of surgical oncology*. PMID: 32253672
2. Identification of novel molecular subtypes and a signature to predict prognosis and therapeutic response based on cuproptosis-related genes in prostate cancer.. *Frontiers in oncology*. PMID: 37205181
3. Accurate characterization of the IFITM locus using MiSeq and PacBio sequencing shows genetic variation in Galliformes.. *BMC genomics*. PMID: 28558694
4. A novel prognostic model for prostate cancer based on androgen biosynthetic and catabolic pathways.. *Frontiers in oncology*. PMID: 36439479
5. Glyco-engineered HEK 293-F cell lines for the production of therapeutic glycoproteins with human N-glycosylation and improved pharmacokinetics.. *Glycobiology*. PMID: 33403396

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.8 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 35.3% |
| 有序区域 (pLDDT>70) 占比 | 60.1% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=69.8），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008428, IPR051227, IPR029044, IPR037524, IPR011658; Pfam: PF05679 |

**染色质调控潜力分析**: 存在 6 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFV1 | 0.571 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | two hybrid fragment pooling approach | pubmed:31413325|imex:IM-26801 |
| INSL5 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PILRA | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| LYZL2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ANTXR1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CSN1S1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| HTRA1 | two hybrid | imex:IM-27784|pubmed:21622153 |
| C1orf54 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| CLEC12B | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9

**评价**: 互作网络中等：STRING 14 预测 + IntAct 9 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=69.8 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 80.6/100

**核心优势**:
1. B4GALNT4 -- N-acetyl-beta-glucosaminyl-glycoprotein 4-beta-N-acetylgalactosaminyltransferase 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 6 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q76KP1
- Protein Atlas: https://www.proteinatlas.org/search/B4GALNT4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B4GALNT4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q76KP1
- STRING: https://string-db.org/network/9606.B4GALNT4
- Packet data timestamp: 2026-06-03 03:28:24

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000182272-B4GALNT4/subcellular

![](https://images.proteinatlas.org/43276/1834_G12_4_red_green.jpg)
![](https://images.proteinatlas.org/43276/1834_G12_6_red_green.jpg)
![](https://images.proteinatlas.org/43276/1905_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/43276/1905_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/43276/1979_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/43276/1979_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q76KP1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q76KP1 |
| SMART | SM00758; |
| UniProt Domain [FT] | DOMAIN 108..278; /note="PA14"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01164" |
| InterPro | IPR008428;IPR051227;IPR029044;IPR037524;IPR011658; |
| Pfam | PF05679; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182272-B4GALNT4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
