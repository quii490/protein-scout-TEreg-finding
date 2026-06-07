---
type: protein-evaluation
gene: "PHYHD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHYHD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHYHD1 |
| 蛋白名称 | Phytanoyl-CoA dioxygenase domain-containing protein 1 |
| 蛋白大小 | 291 aa / 32.4 kDa |
| UniProt ID | Q5SRE7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 32.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.5; PDB: 2OPW, 3OBZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008775; Pfam: PF05721 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Malignant epithelial cell marker-driven risk signature enables precise stratification in esophageal cancer.. *Frontiers in immunology*. PMID: 40496864
2. Genes associated with the progression of neurofibrillary tangles in Alzheimer's disease.. *Translational psychiatry*. PMID: 26126179
3. phytanoyl-CoA dioxygenase domain-containing protein 1 plays an important role in egg shell formation of silkworm (Bombyx mori).. *PloS one*. PMID: 34968397
4. Phyhd1, an XPhyH-like homologue, is induced in mouse T cells upon T cell stimulation.. *Biochemical and biophysical research communications*. PMID: 26970303
5. Identification and validation of methylation-driven genes prognostic signature for recurrence of laryngeal squamous cell carcinoma by integrated bioinformatics analysis.. *Cancer cell international*. PMID: 33005105

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 82.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 2OPW, 3OBZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2OPW, 3OBZ）+ AlphaFold高质量预测（pLDDT=93.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008775; Pfam: PF05721 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF705B | 0.420 | 0.044 | — |
| C16orf86 | 0.417 | 0.000 | — |
| AASDH | 0.417 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fer3HCH | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Q777E3 | psi-mi:"MI:0018"(two hybrid) | pubmed:17446270|imex:IM-20435| |
| HNRNPLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS9B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IPO7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRPS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 6
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 2OPW, 3OBZ | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 3 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PHYHD1 — Phytanoyl-CoA dioxygenase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5SRE7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175287-PHYHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHYHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5SRE7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000175287-PHYHD1/subcellular

![](https://images.proteinatlas.org/12115/1161_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/12115/1161_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/12115/1293_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/12115/1293_F4_4_red_green.jpg)
![](https://images.proteinatlas.org/12115/96_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/12115/96_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5SRE7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5SRE7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008775; |
| Pfam | PF05721; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175287-PHYHD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IPO7 | Bioplex | false |
| POT1 | Intact | false |
| PRPS1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
