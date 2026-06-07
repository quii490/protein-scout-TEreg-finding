---
type: protein-evaluation
gene: "LPIN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LPIN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LPIN2 / KIAA0249 |
| 蛋白名称 | Phosphatidate phosphatase LPIN2 |
| 蛋白大小 | 896 aa / 99.4 kDa |
| UniProt ID | Q92539 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Plasma membrane, Actin filaments; UniProt: Nucleus; Cytoplasm, cytosol; Endoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 896 aa / 99.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036412, IPR026058, IPR031703, IPR007651, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane, Actin filaments | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 125 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0249 |

**关键文献**:
1. Promoting axon regeneration by inhibiting RNA N6-methyladenosine demethylase ALKBH5.. *eLife*. PMID: 37535403
2. Gene structure and spatio-temporal expression of chicken LPIN2.. *Molecular biology reports*. PMID: 24562627
3. Ontogenetic Expression of Lpin2 and Lpin3 Genes and Their Associations with Traits in Two Breeds of Chinese Fat-tailed Sheep.. *Asian-Australasian journal of animal sciences*. PMID: 26950863
4. Variation in the chicken LPIN2 gene and association with performance traits.. *British poultry science*. PMID: 25668704
5. Inborn errors of cytoplasmic triglyceride metabolism.. *Journal of inherited metabolic disease*. PMID: 25300978

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 48.8% |
| 有序区域 (pLDDT>70) 占比 | 40.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 40.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036412, IPR026058, IPR031703, IPR007651, IPR013209; Pfam: PF16876, PF04571, PF08235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLPP2 | 0.975 | 0.087 | — |
| PLPP3 | 0.974 | 0.087 | — |
| LPIN3 | 0.963 | 0.617 | — |
| LPIN1 | 0.963 | 0.610 | — |
| CEPT1 | 0.934 | 0.000 | — |
| CHPT1 | 0.928 | 0.000 | — |
| SELENOI | 0.921 | 0.000 | — |
| CDS2 | 0.920 | 0.000 | — |
| PLPP5 | 0.920 | 0.091 | — |
| PLPP4 | 0.920 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| gcvT | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| LPIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| NRDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FNTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DYRK1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LPIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Endoplasmic reticulum / Cytosol; 额外: Plasma membrane, Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. LPIN2 — Phosphatidate phosphatase LPIN2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小896 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92539
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101577-LPIN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LPIN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92539
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000101577-LPIN2/subcellular

![](https://images.proteinatlas.org/17857/149_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17857/149_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17857/150_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17857/150_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17857/151_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17857/151_D2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92539-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92539 |
| SMART | SM00775; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036412;IPR026058;IPR031703;IPR007651;IPR013209;IPR031315; |
| Pfam | PF16876;PF04571;PF08235; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101577-LPIN2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYRK1B | Biogrid | false |
| FBXW11 | Biogrid | false |
| YWHAE | Opencell | false |
| YWHAZ | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
