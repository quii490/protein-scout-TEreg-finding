---
type: protein-evaluation
gene: "CTTNBP2NL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTTNBP2NL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTTNBP2NL / KIAA1433 |
| 蛋白名称 | CTTNBP2 N-terminal-like protein |
| 蛋白大小 | 639 aa / 70.2 kDa |
| UniProt ID | Q9P2B4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; UniProt: Cell projection, lamellipodium; Cytoplasm, cytoskeleton, str |
| 蛋白大小 | 10/10 | ×1 | 10 | 639 aa / 70.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050719, IPR019131; Pfam: PF09727 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | Cell projection, lamellipodium; Cytoplasm, cytoskeleton, stress fiber | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- FAR/SIN/STRIPAK complex (GO:0090443)
- lamellipodium (GO:0030027)
- stress fiber (GO:0001725)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1433 |

**关键文献**:
1. Recovering protein-protein and domain-domain interactions from aggregation of IP-MS proteomics of coregulator complexes.. *PLoS computational biology*. PMID: 22219718
2. The Drosophila protein, Nausicaa, regulates lamellipodial actin dynamics in a Cortactin-dependent manner.. *Biology open*. PMID: 31164339
3. Pan-Cancer Analysis on the Oncogenic Role of Programmed Cell Death 10.. *Journal of oncology*. PMID: 36276268
4. Tat-HSPE1 suppresses clear cell renal cell carcinoma growth through lysosome-dependent cell death.. *Frontiers in pharmacology*. PMID: 42147335
5. Transcriptional enhanced associate domain factor 1 regulates cortactin-binding protein 2 N-terminal-like to control cell apoptosis in thyroid cancer.. *CytoJournal*. PMID: 41216228

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.9 |
| 高置信度残基 (pLDDT>90) 占比 | 33.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 45.5% |
| 有序区域 (pLDDT>70) 占比 | 44.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.9），有序残基占 44.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050719, IPR019131; Pfam: PF09727 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRIP1 | 0.999 | 0.994 | — |
| STRN3 | 0.999 | 0.994 | — |
| STRN4 | 0.998 | 0.994 | — |
| MOB4 | 0.998 | 0.994 | — |
| PDCD10 | 0.998 | 0.994 | — |
| STRN | 0.997 | 0.994 | — |
| PPP2R1A | 0.997 | 0.994 | — |
| STRIP2 | 0.997 | 0.994 | — |
| STK24 | 0.997 | 0.994 | — |
| STK26 | 0.996 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZRANB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MOB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| STK26 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STRN3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STRIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| STK24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18782753|imex:IM-20360| |
| PPP2R1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18782753|imex:IM-20360| |
| PPP2CA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18782753|imex:IM-20360| |
| PPP2CB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18782753|imex:IM-20360| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.9 + PDB: 无 | pLDDT=65.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, lamellipodium; Cytoplasm, cytoske / Nucleoli fibrillar center, Cytosol | 一致 |
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
1. CTTNBP2NL — CTTNBP2 N-terminal-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小639 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2B4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143079-CTTNBP2NL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTTNBP2NL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2B4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000143079-CTTNBP2NL/subcellular

![](https://images.proteinatlas.org/7301/20_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7301/20_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/7301/21_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7301/21_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/7301/22_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7301/22_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2B4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2B4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050719;IPR019131; |
| Pfam | PF09727; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143079-CTTNBP2NL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| MAP4K4 | Biogrid, Opencell | true |
| MOB4 | Intact, Biogrid | true |
| PDCD10 | Biogrid, Bioplex | true |
| PPP2CA | Biogrid, Opencell | true |
| PPP2CB | Biogrid, Opencell, Bioplex | true |
| PPP2R1A | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
