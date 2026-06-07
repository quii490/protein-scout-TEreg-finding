---
type: protein-evaluation
gene: "REXO5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## REXO5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REXO5 |
| 蛋白名称 | RNA exonuclease 5 |
| 蛋白大小 | 774 aa / 86.9 kDa |
| UniProt ID | Q96IC2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Nucleoli, Endoplasmic reticulum; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 774 aa / 86.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR034922, IPR047021, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoli, Endoplasmic reticulum | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. REXO5 promotes genomic integrity through regulating R-loop using its exonuclease activity.. *Leukemia*. PMID: 39080354
2. Characterization of the mammalian RNA exonuclease 5/NEF-sp as a testis-specific nuclear 3' → 5' exoribonuclease.. *RNA (New York, N.Y.)*. PMID: 28539487
3. The Conserved RNA Exonuclease Rexo5 Is Required for 3' End Maturation of 28S rRNA, 5S rRNA, and snoRNAs.. *Cell reports*. PMID: 29045842
4. Conserved domains and structural motifs that differentiate closely related Rex1 and Rex3 DEDDh exoribonucleases are required for their function in yeast.. *PloS one*. PMID: 40455837

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 39.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 76.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.0，有序区 76.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR034922, IPR047021, IPR013520; Pfam: PF00929, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REXO2 | 0.953 | 0.106 | — |
| REXO1 | 0.916 | 0.000 | — |
| PCNA | 0.667 | 0.416 | — |
| PAN3 | 0.574 | 0.498 | — |
| EXOSC10 | 0.555 | 0.156 | — |
| DIS3 | 0.521 | 0.068 | — |
| TTC31 | 0.480 | 0.047 | — |
| GMPS | 0.442 | 0.000 | — |
| RPF2 | 0.433 | 0.073 | — |
| LRRC29 | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Elp1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-108965 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CycB | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| dx | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cyp4g1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Wnk | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| chrb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG7656 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pxt | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 无 | pLDDT=78.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane; 额外: Nucleoli, Endoplasmic reticu | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. REXO5 — RNA exonuclease 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小774 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96IC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005189-REXO5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REXO5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IC2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000005189-REXO5/subcellular

![](https://images.proteinatlas.org/40755/504_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/40755/504_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/40755/555_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/40755/555_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/40755/840_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/40755/840_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IC2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96IC2 |
| SMART | SM00479;SM00360; |
| UniProt Domain [FT] | DOMAIN 228..376; /note="Exonuclease"; DOMAIN 505..579; /note="RRM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 600..679; /note="RRM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR012677;IPR035979;IPR034922;IPR047021;IPR013520;IPR012337;IPR036397;IPR000504; |
| Pfam | PF00929;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005189-REXO5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAX | Biogrid | false |
| PTGES3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
