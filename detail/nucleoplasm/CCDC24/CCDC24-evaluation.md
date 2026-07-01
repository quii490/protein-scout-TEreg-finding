---
type: protein-evaluation
gene: "CCDC24"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC24 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC24 |
| 蛋白名称 | Coiled-coil domain-containing protein 24 |
| 蛋白大小 | 307 aa / 34.3 kDa |
| UniProt ID | Q8N4L8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoli, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 307 aa / 34.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031367; Pfam: PF15669 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoli, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. An integrative analysis of transcriptome-wide association study and mRNA expression profile identified candidate genes for attention-deficit/hyperactivity disorder.. *Psychiatry research*. PMID: 31685286
2. Integrating single-cell and bulk RNA sequencing data establishes a cuproptosis-related gene predictive signature in breast cancer.. *Discover oncology*. PMID: 41021161

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 15.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 34.9% |
| 有序区域 (pLDDT>70) 占比 | 48.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 48.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031367; Pfam: PF15669 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERI3 | 0.526 | 0.000 | — |
| C5orf52 | 0.515 | 0.000 | — |
| ISCA1 | 0.503 | 0.000 | — |
| ZNF644 | 0.499 | 0.000 | — |
| WDR89 | 0.498 | 0.000 | — |
| RNF220 | 0.497 | 0.000 | — |
| TIGD5 | 0.487 | 0.000 | — |
| RABL2B | 0.484 | 0.000 | — |
| CFAP97D1 | 0.478 | 0.000 | — |
| B4GALT2 | 0.470 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 无 | pLDDT=66.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Nucleoli, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC24 — Coiled-coil domain-containing protein 24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小307 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DISC1 | BioGRID | 0 |
| GATA1 | BioGRID | 0 |
| CDC23 | BioGRID | 0 |
| RNF31 | BioGRID | 0 |
| USHBP1 | BioGRID | 0 |
| REN | BioGRID | 0 |
| BRCA2 | BioGRID | 0 |
| NDUFAB1 | BioGRID | 0 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### 深度机制分析

CCDC24（PF15669/IPR031367，DUF4595家族）是一个功能完全未知的coiled-coil蛋白，其结构域注释仍停留在DUF（Domain of Unknown Function）级别。AlphaFold v6预测的整体pLDDT仅为66.1，有序区域占比仅48.2%，提示该蛋白含有大量内在无序区域（IDR）。在真核蛋白中，IDR常介导液-液相分离（LLPS）及多价弱相互作用，CCDC24的低结构有序性暗示其可能通过IDR参与动态的无膜细胞器组装。其coiled-coil区域（CC结构域）已知介导蛋白-蛋白相互作用，可能在此作为二聚化或寡聚化的界面。

PPI网络分析显示，CCDC24的STRING预测互作伙伴中存在ZNF644（锌指转录因子，可能参与染色质调控）、RNF220（RING finger E3泛素连接酶）及TIGD5（piggyBac衍生转座酶结构域蛋白，具有DNA结合能力）。ZNF644与染色质修饰的潜在联系，RNF220的泛素化活性，以及TIGD5的DNA结合特性，共同指向CCDC24可能作为支架蛋白参与染色质附近的泛素化调控过程。此外，ERI3（外切核糖核酸酶）的互作提示其可能与RNA代谢存在交叉。

HPA免疫荧光定位显示CCDC24主要定位于质膜，但同时也在核仁和细胞质中被检出。这种质膜-核仁双重定位较为罕见，推测CCDC24可能通过某种信号依赖的穿梭机制在亚细胞区室间动态分布。核仁作为核糖体生物合成和多种应激反应的中枢，加上质膜定位，暗示CCDC24可能在细胞外信号到核内应答的传递中扮演接头角色。总体而言，CCDC24作为一个极度新颖（PubMed仅2篇）且含大量无序区域的coiled-coil蛋白，其机制研究应聚焦于IDR介导的分子凝聚体形成、coiled-coil介导的互作网络组装、以及亚细胞穿梭调控三个方面。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4L8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159214-CCDC24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4L8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000159214-CCDC24/subcellular

![](https://images.proteinatlas.org/35424/1840_A1_34_cr5b1530481772a_blue_red_green.jpg)
![](https://images.proteinatlas.org/35424/1840_A1_59_cr5b15304817a02_blue_red_green.jpg)
![](https://images.proteinatlas.org/35424/379_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35424/379_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35424/390_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35424/390_A2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N4L8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N4L8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031367; |
| Pfam | PF15669; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159214-CCDC24/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADRA2C | Intact | false |
| AKAP8L | Intact | false |
| ANTKMT | Intact | false |
| CDC23 | Intact | false |
| DISC1 | Intact | false |
| FNTB | Intact | false |
| GATA1 | Intact | false |
| IKZF3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
