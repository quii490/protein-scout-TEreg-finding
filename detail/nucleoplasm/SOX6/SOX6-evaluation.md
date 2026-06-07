---
type: protein-evaluation
gene: "SOX6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOX6 — REJECTED (研究热度过高 (PubMed strict=447，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOX6 |
| 蛋白名称 | Transcription factor SOX-6 |
| 蛋白大小 | 828 aa / 91.9 kDa |
| UniProt ID | P35712 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 828 aa / 91.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=447 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR051356; Pfam: PF00505 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 447 |
| PubMed broad count | 666 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ScRNA-Seq Reveals a Distinct Osteogenic Progenitor of Alveolar Bone.. *Journal of dental research*. PMID: 37148259
2. Differential chromatin accessibility and transcriptional dynamics define breast cancer subtypes and their lineages.. *Nature cancer*. PMID: 39478117
3. Large-scale genomic and transcriptomic analyses elucidate the genetic basis of high meat yield in chickens.. *Journal of advanced research*. PMID: 36871617
4. Robust gene expression programs underlie recurrent cell states and phenotype switching in melanoma.. *Nature cell biology*. PMID: 32753671
5. Transient gene melting governs the timing of oligodendrocyte maturation.. *Cell*. PMID: 40858115

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.3 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 61.1% |
| 有序区域 (pLDDT>70) 占比 | 27.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.3），有序残基占 27.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR051356; Pfam: PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOX5 | 0.980 | 0.661 | — |
| SOX9 | 0.953 | 0.000 | — |
| HDAC1 | 0.952 | 0.303 | — |
| BCL11A | 0.942 | 0.059 | — |
| GATA1 | 0.923 | 0.086 | — |
| CTNNB1 | 0.918 | 0.301 | — |
| PURB | 0.870 | 0.000 | — |
| MYH7B | 0.853 | 0.046 | — |
| COL2A1 | 0.828 | 0.000 | — |
| KLF1 | 0.754 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POMGNT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF184 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SHOX | psi-mi:"MI:0018"(two hybrid) | pubmed:21262861|imex:IM-16923 |
| HMGA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SOX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SOX13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Tox3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Irf9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NFIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| NFIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.3 + PDB: 无 | pLDDT=55.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SOX6 — Transcription factor SOX-6，研究基础较多，新颖性有限。
2. 蛋白大小828 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 447 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 447 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35712
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110693-SOX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35712
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000110693-SOX6/subcellular

![](https://images.proteinatlas.org/1923/1032_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/1923/1032_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/1923/35_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/1923/35_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/1923/36_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/1923/36_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35712-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P35712 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR051356; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110693-SOX6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFIC | Intact, Biogrid | true |
| CENPK | Biogrid | false |
| CTBP2 | Biogrid | false |
| CTNNB1 | Biogrid | false |
| HDAC1 | Biogrid | false |
| NFIA | Intact, Biogrid | false |
| NFIB | Intact, Biogrid | false |
| NFIX | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
