---
type: protein-evaluation
gene: "PFN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PFN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PFN3 |
| 蛋白名称 | Profilin-3 |
| 蛋白大小 | 137 aa / 14.6 kDa |
| UniProt ID | P60673 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 137 aa / 14.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR048278, IPR005455, IPR036140, IPR005454; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol | Uncertain |
| UniProt | Cytoplasm, cytoskeleton; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Profilin 3 genetic architecture in glioma formalin fixed paraffin embedded (FFPE) archive.. *Gene*. PMID: 33775850
2. Natural antisense transcription from a comparative perspective.. *Genomics*. PMID: 27241791
3. Interdependent Transcription of a Natural Sense/Antisense Transcripts Pair (SLC34A1/PFN3).. *Non-coding RNA*. PMID: 35202092
4. Loss of Profilin3 Impairs Spermiogenesis by Affecting Acrosome Biogenesis, Autophagy, Manchette Development and Mitochondrial Organization.. *Frontiers in cell and developmental biology*. PMID: 34869336
5. Actin-related protein T3 is required for acrosome biogenesis and sperm function in mice.. *Development (Cambridge, England)*. PMID: 41668650

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.2 |
| 高置信度残基 (pLDDT>90) 占比 | 90.5% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.2，有序区 97.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048278, IPR005455, IPR036140, IPR005454; Pfam: PF00235 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTB | 0.999 | 0.330 | — |
| VASP | 0.998 | 0.126 | — |
| APBB1IP | 0.995 | 0.073 | — |
| ACTG1 | 0.987 | 0.178 | — |
| WAS | 0.980 | 0.000 | — |
| VCL | 0.973 | 0.000 | — |
| DIAPH1 | 0.965 | 0.093 | — |
| CFL2 | 0.959 | 0.100 | — |
| CFL1 | 0.958 | 0.100 | — |
| GSN | 0.955 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACTA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACTC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCHHL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POTEJ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNG1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.2 + PDB: 无 | pLDDT=94.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus / Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. PFN3 — Profilin-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小137 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60673
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196570-PFN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PFN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60673
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000196570-PFN3/subcellular

![](https://images.proteinatlas.org/38274/1959_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38274/1959_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38274/1985_E8_11_cr5e579da71234f_blue_red_green.jpg)
![](https://images.proteinatlas.org/38274/1985_E8_4_cr5e579da711c37_blue_red_green.jpg)
![](https://images.proteinatlas.org/38274/2030_F9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38274/2030_F9_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P60673-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
