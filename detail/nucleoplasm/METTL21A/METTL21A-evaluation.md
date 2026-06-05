---
type: protein-evaluation
gene: "METTL21A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL21A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL21A / FAM119A, HCA557B |
| 蛋白名称 | Protein N-lysine methyltransferase METTL21A |
| 蛋白大小 | 218 aa / 24.6 kDa |
| UniProt ID | Q8WXB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 218 aa / 24.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.9; PDB: 4LEC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019410, IPR029063; Pfam: PF10294 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM119A, HCA557B |

**关键文献**:
1. Exome sequencing identifies novel genetic variants associated with varicose veins.. *PLoS genetics*. PMID: 38980841
2. Weighted correlation network analysis revealed novel long non-coding RNAs for colorectal cancer.. *Scientific reports*. PMID: 35194111
3. Saccharomyces cerevisiae Eukaryotic Elongation Factor 1A (eEF1A) Is Methylated at Lys-390 by a METTL21-Like Methyltransferase.. *PloS one*. PMID: 26115316
4. METTL21A, a Non-Histone Methyltransferase, Is Dispensable for Spermatogenesis and Male Fertility in Mice.. *International journal of molecular sciences*. PMID: 35216057
5. Comprehensive Analysis of METTLs (METTL1/13/18/21A/23/25/2A/2B/5/6/9) and Associated mRNA Risk Signature in Hepatocellular Carcinoma.. *Analytical cellular pathology (Amsterdam)*. PMID: 38130905

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.9 |
| 高置信度残基 (pLDDT>90) 占比 | 85.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 91.3% |
| 可用 PDB 条目 | 4LEC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.9，有序区 91.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019410, IPR029063; Pfam: PF10294 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.931 | 0.629 | — |
| HSPA4 | 0.859 | 0.734 | — |
| METTL22 | 0.814 | 0.065 | — |
| EEF1AKMT2 | 0.761 | 0.000 | — |
| METTL18 | 0.743 | 0.000 | — |
| ZBED8 | 0.732 | 0.732 | — |
| HSPBP1 | 0.728 | 0.710 | — |
| ETFBKMT | 0.716 | 0.000 | — |
| KIN | 0.693 | 0.000 | — |
| EEF2KMT | 0.690 | 0.065 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| FAM200C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MSRB3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MEI4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LZTS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PFDN5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARPC4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF620 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF655 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BAG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.9 + PDB: 4LEC | pLDDT=91.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. METTL21A — Protein N-lysine methyltransferase METTL21A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小218 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144401-METTL21A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL21A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000144401-METTL21A/subcellular

![](https://images.proteinatlas.org/34712/381_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/34712/381_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/34712/389_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/34712/389_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/34712/398_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/34712/398_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WXB1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
