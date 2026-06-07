---
type: protein-evaluation
gene: "GLTSCR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLTSCR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLTSCR1 / GLTSCR1 |
| 蛋白名称 | BRD4-interacting chromatin-remodeling complex-associated protein |
| 蛋白大小 | 1560 aa / 158.5 kDa |
| UniProt ID | Q9NZM4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1560 aa / 158.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052438, IPR015671; Pfam: PF15249 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- GBAF complex (GO:0140288)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SWI/SNF complex (GO:0016514)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLTSCR1 |

**关键文献**:
1. Large-scale discovery of novel neurodevelopmental disorder-related genes through a unified analysis of single-nucleotide and copy number variants.. *Genome medicine*. PMID: 35468861
2. BICRA, a SWI/SNF Complex Member, Is Associated with BAF-Disorder Related Phenotypes in Humans and Model Organisms.. *American journal of human genetics*. PMID: 33232675
3. Identification of assembly mode of non-canonical BAF (ncBAF) chromatin remodeling complex core module.. *Biochemical and biophysical research communications*. PMID: 39732119
4. GLTSCR1, ATM, PPP1R13L and CD3EAP Genetic Variants and Lung Cancer Risk in a Chinese Population.. *Current medical science*. PMID: 30128886
5. Loss of GLTSCR1 causes congenital heart defects by regulating NPPA transcription.. *Angiogenesis*. PMID: 36745292

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052438, IPR015671; Pfam: PF15249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRD9 | 0.999 | 0.691 | — |
| SMARCD1 | 0.995 | 0.841 | — |
| SMARCA4 | 0.990 | 0.631 | — |
| SS18 | 0.988 | 0.839 | — |
| BCL7A | 0.987 | 0.678 | — |
| SMARCA2 | 0.986 | 0.612 | — |
| BCL7C | 0.984 | 0.733 | — |
| SMARCB1 | 0.983 | 0.445 | — |
| SMARCC1 | 0.980 | 0.527 | — |
| ARID1A | 0.980 | 0.303 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| BICRA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SPATA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCL7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SS18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCL7C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMARCD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DYNC1H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLTSCR1 — BRD4-interacting chromatin-remodeling complex-associated protein，非常新颖，仅有少数基础研究。
2. 蛋白大小1560 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZM4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000063169-BICRA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLTSCR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZM4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000063169-BICRA/subcellular

![](https://images.proteinatlas.org/56211/1168_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/56211/1168_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/56211/1252_F1_4_red_green.jpg)
![](https://images.proteinatlas.org/56211/1252_F1_8_red_green.jpg)
![](https://images.proteinatlas.org/56211/1257_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/56211/1257_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZM4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZM4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052438;IPR015671; |
| Pfam | PF15249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000063169-BICRA/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
