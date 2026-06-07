---
type: protein-evaluation
gene: "RAI14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RAI14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAI14 / KIAA1334, NORPEG |
| 蛋白名称 | Ankycorbin |
| 蛋白大小 | 980 aa / 110.0 kDa |
| UniProt ID | Q9P0K7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Actin filaments, Cytosol; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, stress fib |
| 蛋白大小 | 8/10 | ×1 | 8 | 980 aa / 110.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR042420; Pfam: PF00023, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Actin filaments, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, stress fiber; Cytoplasm, cell cortex; Cell junctio... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- anchoring junction (GO:0070161)
- cell cortex (GO:0005938)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- stress fiber (GO:0001725)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1334, NORPEG |

**关键文献**:
1. Retinoic acid-induced protein 14 links mechanical forces to Hippo signaling.. *EMBO reports*. PMID: 39160347
2. Retinoic acid-induced protein 14 controls dendritic spine dynamics associated with depressive-like behaviors.. *eLife*. PMID: 35467532
3. Unveiling the role of RAI14 in cancer: Biological significance and translational perspectives.. *Seminars in oncology*. PMID: 40902302
4. RAI14 Regulated by circNFATC3/miR-23b-3p axis Facilitates Cell Growth and Invasion in Gastric Cancer.. *Cell transplantation*. PMID: 33840258
5. Rai14 is a novel interactor of Invariant chain that regulates macropinocytosis.. *Frontiers in immunology*. PMID: 37545539

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 24.6% |
| 置信残基 (pLDDT 70-90) 占比 | 42.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 21.4% |
| 有序区域 (pLDDT>70) 占比 | 67.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.6，有序区 67.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR042420; Pfam: PF00023, PF12796, PF13857 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PACSIN1 | 0.695 | 0.616 | — |
| PACSIN3 | 0.643 | 0.605 | — |
| PACSIN2 | 0.624 | 0.602 | — |
| TRIOBP | 0.602 | 0.598 | — |
| PPP1CB | 0.597 | 0.591 | — |
| TTC23L | 0.559 | 0.000 | — |
| RPGRIP1L | 0.486 | 0.450 | — |
| PPP1CC | 0.481 | 0.473 | — |
| PLK1 | 0.467 | 0.448 | — |
| DHRS13 | 0.463 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAZ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| ENSP00000422942.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 无 | pLDDT=72.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / Nucleoplasm; 额外: Actin filaments, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. RAI14 — Ankycorbin，非常新颖，仅有少数基础研究。
2. 蛋白大小980 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0K7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000039560-RAI14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAI14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0K7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000039560-RAI14/subcellular

![](https://images.proteinatlas.org/36949/565_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/36949/565_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/36949/570_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/36949/570_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/36949/584_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/36949/584_B5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0K7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P0K7 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR042420; |
| Pfam | PF00023;PF12796;PF13857; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000039560-RAI14/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PACSIN2 | Biogrid, Opencell | true |
| PACSIN3 | Biogrid, Opencell | true |
| PSMD9 | Biogrid, Opencell | true |
| RPGRIP1L | Intact, Biogrid | true |
| YWHAB | Intact, Biogrid, Opencell | true |
| YWHAG | Intact, Biogrid, Opencell | true |
| YWHAH | Biogrid, Opencell | true |
| YWHAQ | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
