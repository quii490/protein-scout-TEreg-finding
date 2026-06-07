---
type: protein-evaluation
gene: "OGFOD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OGFOD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OGFOD1 / KIAA1612, TPA1 |
| 蛋白名称 | Prolyl 3-hydroxylase OGFOD1 |
| 蛋白大小 | 542 aa / 63.2 kDa |
| UniProt ID | Q8N543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 542 aa / 63.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.8; PDB: 4NHX, 4NHY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005123, IPR019601, IPR006620, IPR039558, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1612, TPA1 |

**关键文献**:
1. Identifying the target, mechanism, and agonist of α-ketoglutaric acid in delaying mesenchymal stem cell senescence.. *Cell reports*. PMID: 40570373
2. OGFOD1 enables AML chemo- and nutrient stress resistance by regulating protein synthesis.. *Cell metabolism*. PMID: 40961937
3. The ribosomal prolyl-hydroxylase OGFOD1 decreases during cardiac differentiation and modulates translation and splicing.. *JCI insight*. PMID: 31112528
4. OGFOD1 modulates the transcriptional and proteomic landscapes to alter isoproterenol-induced hypertrophy susceptibility.. *Journal of molecular and cellular cardiology*. PMID: 37084634
5. Ogfod1 deletion increases cardiac beta-alanine levels and protects mice against ischaemia- reperfusion injury.. *Cardiovascular research*. PMID: 34668514

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 75.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 4NHX, 4NHY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4NHX, 4NHY）+ AlphaFold高质量预测（pLDDT=86.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005123, IPR019601, IPR006620, IPR039558, IPR051842; Pfam: PF13661, PF10637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPS23 | 0.816 | 0.366 | — |
| TUFM | 0.809 | 0.797 | — |
| PABPC1 | 0.757 | 0.087 | — |
| CAPRIN1 | 0.706 | 0.000 | — |
| TRMT1 | 0.695 | 0.114 | — |
| JMJD4 | 0.685 | 0.000 | — |
| TSR1 | 0.683 | 0.000 | — |
| BMS1 | 0.680 | 0.000 | — |
| ABCF2 | 0.663 | 0.224 | — |
| LOC102724159 | 0.660 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FEM1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000457258.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RPS23 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FGL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPL42 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FNTA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TPRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SPATA46 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BUD13 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 4NHX, 4NHY | pLDDT=86.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

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
1. OGFOD1 — Prolyl 3-hydroxylase OGFOD1，非常新颖，仅有少数基础研究。
2. 蛋白大小542 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087263-OGFOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OGFOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000087263-OGFOD1/subcellular

![](https://images.proteinatlas.org/3215/4_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/3215/4_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/3215/5_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/3215/5_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/3215/6_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/3215/6_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N543 |
| SMART | SM00702; |
| UniProt Domain [FT] | DOMAIN 134..239; /note="Fe2OG dioxygenase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00805" |
| InterPro | IPR005123;IPR019601;IPR006620;IPR039558;IPR051842; |
| Pfam | PF13661;PF10637; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000087263-OGFOD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FEM1A | Intact | false |
| MRPL42 | Bioplex | false |
| RPS23 | Intact | false |
| SPATA46 | Bioplex | false |
| TPRN | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
