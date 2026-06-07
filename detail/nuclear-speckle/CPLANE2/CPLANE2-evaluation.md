---
type: protein-evaluation
gene: "CPLANE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPLANE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPLANE2 / C1orf89, RSG1 |
| 蛋白名称 | Ciliogenesis and planar polarity effector 2 |
| 蛋白大小 | 258 aa / 28.5 kDa |
| UniProt ID | Q9BU20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytos |
| 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 28.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR039677, IPR001806; Pfam: PF00071 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- ciliary transition zone (GO:0035869)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf89, RSG1 |

**关键文献**:
1. The human ciliopathy protein RSG1 links the CPLANE complex to transition zone architecture.. *Nature communications*. PMID: 40593758
2. RSG1 is required for cilia-dependent neural tube closure.. *Genesis (New York, N.Y. : 2000)*. PMID: 38721990
3. Phenotypic Expansion and Molecular Implications in Recessive FUZ-Related Ciliopathy.. *Clinical genetics*. PMID: 41952398
4. The human ciliopathy protein RSG1 links the CPLANE complex to transition zone architecture.. *bioRxiv : the preprint server for biology*. PMID: 39386566

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 70.9% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.1，有序区 94.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR039677, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INTU | 0.985 | 0.829 | — |
| FUZ | 0.964 | 0.843 | — |
| WDPCP | 0.926 | 0.507 | — |
| ARL13B | 0.627 | 0.162 | — |
| RAB23 | 0.613 | 0.054 | — |
| IFT43 | 0.580 | 0.000 | — |
| IMPDH2 | 0.574 | 0.564 | — |
| IFT27 | 0.561 | 0.000 | — |
| IFT22 | 0.548 | 0.000 | — |
| ITSN2 | 0.540 | 0.497 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FUZ | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MSLN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TMEM14C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| IMPDH2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RND3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| INTU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 无 | pLDDT=90.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium basal body; Cytopl / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. CPLANE2 — Ciliogenesis and planar polarity effector 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BU20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132881-CPLANE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPLANE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BU20
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000132881-CPLANE2/subcellular

![](https://images.proteinatlas.org/28453/2147_D3_16_red_green.jpg)
![](https://images.proteinatlas.org/28453/2147_D3_38_red_green.jpg)
![](https://images.proteinatlas.org/28453/2165_G9_35_red_green.jpg)
![](https://images.proteinatlas.org/28453/2165_G9_47_red_green.jpg)
![](https://images.proteinatlas.org/28453/255_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/28453/255_H5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BU20-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BU20 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR039677;IPR001806; |
| Pfam | PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132881-CPLANE2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FUZ | Intact, Biogrid | true |
| HSPA2 | Bioplex | false |
| HSPA6 | Bioplex | false |
| HSPA8 | Bioplex | false |
| IMPDH2 | Intact | false |
| RND3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
