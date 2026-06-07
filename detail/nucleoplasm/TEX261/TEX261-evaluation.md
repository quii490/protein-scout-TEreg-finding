---
type: protein-evaluation
gene: "TEX261"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX261 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX261 |
| 蛋白名称 | Protein TEX261 |
| 蛋白大小 | 196 aa / 22.5 kDa |
| UniProt ID | Q6UWH6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 196 aa / 22.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007277; Pfam: PF04148 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Scrutinizing the human TEX genes in the context of human male infertility.. *Andrology*. PMID: 37594251
2. Tex261, a novel gene presumably related but distinct from steroidogenic acute regulatory (StAR) gene, is regulated during the development of germ cells.. *Biochemical and biophysical research communications*. PMID: 9464256
3. Supplementation with Tex261 provides a possible preventive treatment for hypoxic pulmonary artery hypertension.. *Frontiers in pharmacology*. PMID: 36408272
4. Tex261 modulates the excitotoxic cell death induced by N-methyl-D-aspartate (NMDA) receptor activation.. *Biochemical and biophysical research communications*. PMID: 17803966
5. The miRNA Pull Out Assay as a Method to Validate the miR-28-5p Targets Identified in Other Tumor Contexts in Prostate Cancer.. *International journal of genomics*. PMID: 29085832

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.3% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 77.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.4，有序区 77.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007277; Pfam: PF04148 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTC16 | 0.536 | 0.000 | — |
| TEX26 | 0.506 | 0.000 | — |
| SIGLEC12 | 0.469 | 0.469 | — |
| BPIFB3 | 0.449 | 0.000 | — |
| SLC25A52 | 0.447 | 0.000 | — |
| CXorf58 | 0.445 | 0.000 | — |
| TM4SF20 | 0.445 | 0.000 | — |
| SPAG7 | 0.439 | 0.000 | — |
| HECTD3 | 0.438 | 0.000 | — |
| SNAPC5 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIGLEC12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENST00000272438 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 2
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 无 | pLDDT=82.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TEX261 — Protein TEX261，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小196 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWH6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144043-TEX261/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX261
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWH6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000144043-TEX261/subcellular

![](https://images.proteinatlas.org/16631/131_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/16631/131_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/16631/132_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/16631/132_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/16631/164_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/16631/164_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UWH6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UWH6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007277; |
| Pfam | PF04148; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144043-TEX261/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
