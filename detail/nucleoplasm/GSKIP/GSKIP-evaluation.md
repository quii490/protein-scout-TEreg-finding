---
type: protein-evaluation
gene: "GSKIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GSKIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GSKIP / C14orf129 |
| 蛋白名称 | GSK3B-interacting protein |
| 蛋白大小 | 139 aa / 15.6 kDa |
| UniProt ID | Q9P0R6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 139 aa / 15.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.9; PDB: 1SGO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037395, IPR007967, IPR023231; Pfam: PF05303 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 56 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf129 |

**关键文献**:
1. Many faces and functions of GSKIP: a temporospatial regulation view.. *Cellular signalling*. PMID: 35728705
2. The A-kinase Anchoring Protein GSKIP Regulates GSK3β Activity and Controls Palatal Shelf Fusion in Mice.. *The Journal of biological chemistry*. PMID: 26582204
3. Variation in the Ovine Glycogen Synthase Kinase 3 Beta-Interaction Protein Gene (GSKIP) Affects Carcass and Growth Traits in Romney Sheep.. *Animals : an open access journal from MDPI*. PMID: 34573656
4. High expression of GSKIP is associated with poor prognosis in meningioma.. *Medicine*. PMID: 36550871
5. The origin of GSKIP, a multifaceted regulatory factor in the mammalian Wnt pathway.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 29694914

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 69.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 76.3% |
| 可用 PDB 条目 | 1SGO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.9，有序区 76.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037395, IPR007967, IPR023231; Pfam: PF05303 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSK3B | 0.985 | 0.843 | — |
| GSK3A | 0.848 | 0.809 | — |
| ATG2B | 0.788 | 0.000 | — |
| PRKACB | 0.773 | 0.071 | — |
| PRKACA | 0.771 | 0.071 | — |
| PRKACG | 0.771 | 0.071 | — |
| PRKAR2B | 0.492 | 0.091 | — |
| PRKAR2A | 0.461 | 0.098 | — |
| BCORL1 | 0.439 | 0.000 | — |
| PIN1 | 0.405 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMYD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSK3B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PEX19 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EXT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GSK3A | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-11703|pubmed:20368287 |
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GM2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LORICRIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PMEL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 1SGO | pLDDT=83.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Golgi apparatus, Vesicles; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GSKIP — GSK3B-interacting protein，非常新颖，仅有少数基础研究。
2. 蛋白大小139 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0R6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100744-GSKIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GSKIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0R6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000100744-GSKIP/subcellular

![](https://images.proteinatlas.org/43054/460_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43054/460_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43054/465_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43054/465_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43054/467_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43054/467_H6_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0R6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P0R6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037395;IPR007967;IPR023231; |
| Pfam | PF05303; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100744-GSKIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSK3A | Intact, Biogrid, Opencell, Bioplex | true |
| GSK3B | Intact, Biogrid, Opencell | true |
| RP2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
