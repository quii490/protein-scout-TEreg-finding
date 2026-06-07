---
type: protein-evaluation
gene: "COPRS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COPRS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPRS / C17orf79, COPR5 |
| 蛋白名称 | Coordinator of PRMT5 and differentiation stimulator |
| 蛋白大小 | 184 aa / 20.1 kDa |
| UniProt ID | Q9NQ92 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 184 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=18 篇 (<=20->10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR029289; Pfam: PF15340 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf79, COPR5 |

**关键文献**:
1. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate Pseudomonas copper resistance.. *PLoS genetics*. PMID: 38861577
2. Coprs inactivation leads to a derepression of LINE1 transposons in spermatocytes.. *FEBS open bio*. PMID: 30652083
3. Essential Gene Clusters Involved in Copper Tolerance Identified in Acinetobacter baumannii Clinical and Environmental Isolates.. *Pathogens (Basel, Switzerland)*. PMID: 31952222
4. The two-component signal transduction system CopRS of Corynebacterium glutamicum is required for adaptation to copper-excess stress.. *PloS one*. PMID: 21799779
5. A Copper-Responsive Two-Component System Governs Lipoprotein Remodeling in Listeria monocytogenes.. *Journal of bacteriology*. PMID: 36622228

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 59.2% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 27.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 27.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029289; Pfam: PF15340 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRMT5 | 0.989 | 0.779 | — |
| WDR77 | 0.925 | 0.622 | — |
| RIOK1 | 0.854 | 0.615 | — |
| H4C6 | 0.837 | 0.292 | — |
| UTP6 | 0.797 | 0.000 | — |
| CLNS1A | 0.750 | 0.626 | — |
| CRLF3 | 0.693 | 0.000 | — |
| RAB11FIP4 | 0.673 | 0.000 | — |
| ATAD5 | 0.667 | 0.000 | — |
| ADAP2 | 0.637 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MEMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LACTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| RAB5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| FBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBFOX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 无 | pLDDT=62.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. COPRS -- Coordinator of PRMT5 and differentiation stimulator，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ92
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172301-COPRS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPRS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ92
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172301-COPRS/subcellular

![](https://images.proteinatlas.org/52552/783_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/52552/783_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/52552/785_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/52552/785_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/52552/868_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/52552/868_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ92-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQ92 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029289; |
| Pfam | PF15340; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172301-COPRS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLNS1A | Biogrid, Opencell | true |
| HNRNPH1 | Biogrid, Opencell | true |
| PRMT5 | Intact, Biogrid | true |
| SNRPB | Biogrid, Opencell | true |
| H3C6 | Biogrid | false |
| H4C1 | Intact | false |
| H4C11 | Intact | false |
| H4C12 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
