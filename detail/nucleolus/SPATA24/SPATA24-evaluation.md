---
type: protein-evaluation
gene: "SPATA24"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA24 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA24 |
| 蛋白名称 | Spermatogenesis-associated protein 24 |
| 蛋白大小 | 205 aa / 23.6 kDa |
| UniProt ID | Q86W54 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 23.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029176; Pfam: PF15175 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- male germ cell nucleus (GO:0001673)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Potential role of 4-hydroxyisoleucine in enhancing fertility in male mice with diet-induced obesity.. *Frontiers in endocrinology*. PMID: 40917356
2. Mixed model-based eQTL analysis reveals lncRNAs associated with regulation of genes involved in sex determination and spermatogenesis: The key to understanding human gender imbalance.. *Computational biology and chemistry*. PMID: 35709667

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.4，有序区 85.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029176; Pfam: PF15175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC18 | 0.672 | 0.000 | — |
| SMIM33 | 0.664 | 0.000 | — |
| LRCOL1 | 0.581 | 0.000 | — |
| PROB1 | 0.561 | 0.000 | — |
| FAM229B | 0.554 | 0.000 | — |
| ZSCAN2 | 0.541 | 0.000 | — |
| FAM13B | 0.513 | 0.000 | — |
| SPATA21 | 0.503 | 0.000 | — |
| CTNNBIP1 | 0.502 | 0.502 | — |
| SPATA3 | 0.502 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| FLOT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PTAFR | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EHD2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CAMK2D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MDFI | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EFEMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTNNBIP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OIP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 无 | pLDDT=88.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplas / Nucleoplasm, Cytosol | 一致 |
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
1. SPATA24 — Spermatogenesis-associated protein 24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86W54
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170469-SPATA24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86W54
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170469-SPATA24/subcellular

![](https://images.proteinatlas.org/44000/498_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/44000/498_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/44000/501_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/44000/501_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/44000/512_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/44000/512_B6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86W54-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86W54 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029176; |
| Pfam | PF15175; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170469-SPATA24/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP72 | Intact, Biogrid | true |
| CALCOCO2 | Intact | false |
| KRT31 | Intact | false |
| KRT40 | Intact | false |
| KRTAP4-2 | Intact | false |
| LZTS2 | Intact | false |
| PCM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
