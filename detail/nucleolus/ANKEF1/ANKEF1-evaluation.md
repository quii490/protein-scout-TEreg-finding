---
type: protein-evaluation
gene: "ANKEF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKEF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKEF1 / ANKRD5 |
| 蛋白名称 | Ankyrin repeat and EF-hand domain-containing protein 1 |
| 蛋白大小 | 776 aa / 86.7 kDa |
| UniProt ID | Q9NU02 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Plasma membrane, Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 776 aa / 86.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052801, IPR002110, IPR036770, IPR011992, IPR002 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Plasma membrane, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANKRD5 |

**关键文献**:
1. ANKEF1 is a key axonemal component essential for murine sperm motility and male fertility.. *eLife*. PMID: 41460250
2. Spatiotemporal expression profile of embryonic and adult ankyrin repeat and EF-hand domain containing protein 1-encoding genes ankef1a and ankef1b in zebrafish.. *Gene expression patterns : GEP*. PMID: 31520739
3. Genome-Wide Scan for Parent-of-Origin Effects in a sub-Saharan African Cohort With Nonsyndromic Cleft Lip and/or Cleft Palate (CL/P).. *The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association*. PMID: 34382870
4. Regionalized Protein Localization Domains in the Zebrafish Hair Cell Kinocilium.. *Journal of developmental biology*. PMID: 37367482
5. NOVEL GENETIC FINDINGS IN A CHINESE FAMILY WITH EARLY-ONSET FEMALE-RELATED TYPE 2 DIABETES.. *Acta endocrinologica (Bucharest, Romania : 2005)*. PMID: 31149201

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 43.0% |
| 置信残基 (pLDDT 70-90) 占比 | 38.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 8.5% |
| 有序区域 (pLDDT>70) 占比 | 81.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 81.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052801, IPR002110, IPR036770, IPR011992, IPR002048; Pfam: PF12796 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSPH14 | 0.634 | 0.121 | — |
| WDR38 | 0.619 | 0.099 | — |
| CFAP99 | 0.618 | 0.098 | — |
| TSNAXIP1 | 0.618 | 0.099 | — |
| TEKT3 | 0.616 | 0.093 | — |
| CCDC65 | 0.607 | 0.000 | — |
| DNAH10 | 0.606 | 0.055 | — |
| FBXO36 | 0.602 | 0.000 | — |
| CLBA1 | 0.561 | 0.000 | — |
| RSPH4A | 0.547 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| NRDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| USP46 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NXN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UTP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EPB41L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLASRP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SH3GLB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PRPF40A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center, Plasma membrane, Cytoso | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0 (仅1源)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. ANKEF1 — Ankyrin repeat and EF-hand domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小776 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NU02
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132623-ANKEF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKEF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NU02
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:52:02

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000132623-ANKEF1/subcellular

![](https://images.proteinatlas.org/41151/484_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41151/484_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41151/492_B4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41151/492_B4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/41151/836_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41151/836_B12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NU02-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NU02 |
| SMART | SM00248; |
| UniProt Domain [FT] | DOMAIN 335..369; /note="EF-hand"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR052801;IPR002110;IPR036770;IPR011992;IPR002048; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132623-ANKEF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HIF1AN | Biogrid, Bioplex | true |
| CALCB | Bioplex | false |
| CASP6 | Intact | false |
| CCK | Intact | false |
| CLASRP | Intact | false |
| COQ8A | Intact | false |
| P4HB | Intact | false |
| SH3GLB1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
