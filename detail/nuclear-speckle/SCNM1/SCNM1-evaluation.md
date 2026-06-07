---
type: protein-evaluation
gene: "SCNM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SCNM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SCNM1 |
| 蛋白名称 | Sodium channel modifier 1 |
| 蛋白大小 | 230 aa / 25.9 kDa |
| UniProt ID | Q9BWG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 230 aa / 25.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 7DVQ, 8Y7E |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033570, IPR031625, IPR031622; Pfam: PF15805, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleoplasm; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structure of the activated human minor spliceosome.. *Science (New York, N.Y.)*. PMID: 33509932
2. Mutations in SCNM1 cause orofaciodigital syndrome due to minor intron splicing defects affecting primary cilia.. *American journal of human genetics*. PMID: 36084634
3. Clinical and Biological Significance of Sodium Channel Modifier 1 as a Component of the Minor Spliceosome in Hepatocellular Carcinoma.. *Annals of surgical oncology*. PMID: 40172715
4. Evidence for a direct role of the disease modifier SCNM1 in splicing.. *Human molecular genetics*. PMID: 17656373
5. Expanding the phenotype associated with biallelic SCNM1 variants.. *Human genomics*. PMID: 41291844

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 14.8% |
| 置信残基 (pLDDT 70-90) 占比 | 38.3% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 7DVQ, 8Y7E |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 53.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033570, IPR031625, IPR031622; Pfam: PF15805, PF15803 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARMC7 | 0.949 | 0.922 | — |
| LUC7L2 | 0.926 | 0.000 | — |
| FMC1-LUC7L2 | 0.926 | 0.000 | — |
| SF3B3 | 0.920 | 0.920 | — |
| SF3B1 | 0.917 | 0.915 | — |
| SNRPD2 | 0.909 | 0.800 | — |
| RNF113A | 0.908 | 0.900 | — |
| SF3B2 | 0.902 | 0.900 | — |
| PRPF8 | 0.900 | 0.900 | — |
| CDC5L | 0.900 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCM6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRNP | psi-mi:"MI:0089"(protein array) | pubmed:18482256|imex:IM-19010 |
| RSAD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HMG20A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PLSCR1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRT38 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HOMER3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 7DVQ, 8Y7E | pLDDT=69.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus speckle / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SCNM1 — Sodium channel modifier 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163156-SCNM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCNM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000163156-SCNM1/subcellular

![](https://images.proteinatlas.org/54324/867_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/54324/867_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/54324/870_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/54324/870_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/54324/872_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/54324/872_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWG6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033570;IPR031625;IPR031622; |
| Pfam | PF15805;PF15803; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163156-SCNM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FHL5 | Intact, Biogrid | true |
| GOLGA2 | Intact, Biogrid | true |
| AVPI1 | Intact | false |
| AXIN2 | Intact | false |
| BACH2 | Intact | false |
| BLZF1 | Intact | false |
| CALCOCO2 | Intact | false |
| CARD10 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
