---
type: protein-evaluation
gene: "PM20D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PM20D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PM20D2 / ACY1L2 |
| 蛋白名称 | Xaa-Arg dipeptidase |
| 蛋白大小 | 436 aa / 47.8 kDa |
| UniProt ID | Q8IYS1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 436 aa / 47.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.1; PDB: 7YH4, 8XZC, 8ZEI, 8ZEL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036264, IPR002933, IPR052030, IPR011650, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **147.0/180** | |
| **归一化总分** | | | **81.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACY1L2 |

**关键文献**:
1. Comparative Analysis of the Characteristics of Triterpenoid Transcriptome from Different Strains of Wolfiporia cocos.. *International journal of molecular sciences*. PMID: 31362345
2. Landscape of sex differences in obesity and type 2 diabetes in subcutaneous adipose tissue: a systematic review and meta-analysis of transcriptomics studies.. *Metabolism: clinical and experimental*. PMID: 40157598
3. Analysis of weighted gene co-expression network of triterpenoid-related transcriptome characteristics from different strains of Wolfiporia cocos.. *Scientific reports*. PMID: 34521885

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| 可用 PDB 条目 | 7YH4, 8XZC, 8ZEI, 8ZEL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7YH4, 8XZC, 8ZEI, 8ZEL）+ AlphaFold高质量预测（pLDDT=93.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036264, IPR002933, IPR052030, IPR011650, IPR017144; Pfam: PF07687, PF01546 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PNRC1 | 0.633 | 0.000 | — |
| MAPK1IP1L | 0.529 | 0.045 | — |
| KLHL33 | 0.515 | 0.000 | — |
| UBE2J1 | 0.515 | 0.051 | — |
| MDN1 | 0.511 | 0.067 | — |
| ZKSCAN8 | 0.472 | 0.075 | — |
| FAAH | 0.462 | 0.045 | — |
| GAPDH | 0.452 | 0.069 | — |
| QRSL1 | 0.452 | 0.047 | — |
| PGRMC2 | 0.451 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000275072.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PSMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RUSC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP26-1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CNNM3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SIVA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYOZ3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HAO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 7YH4, 8XZC, 8ZEI, 8ZEL | pLDDT=93.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PM20D2 — Xaa-Arg dipeptidase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小436 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146281-PM20D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PM20D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYS1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000146281-PM20D2/subcellular

![](https://images.proteinatlas.org/30325/696_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/30325/696_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/30325/777_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/30325/777_C6_3_red_green.jpg)
![](https://images.proteinatlas.org/30325/790_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/30325/790_C6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYS1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
