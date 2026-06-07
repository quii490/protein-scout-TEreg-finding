---
type: protein-evaluation
gene: "UACA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UACA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UACA / KIAA1561 |
| 蛋白名称 | Uveal autoantigen with coiled-coil domains and ankyrin repeats |
| 蛋白大小 | 1416 aa / 162.5 kDa |
| UniProt ID | Q9BZF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton |
| 蛋白大小 | 5/10 | ×1 | 5 | 1416 aa / 162.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR042420, IPR000727; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1561 |

**关键文献**:
1. UACA locus is associated with breast cancer chemoresistance and survival.. *NPJ breast cancer*. PMID: 35322040
2. PFKP Mediates Breast Cancer Metastasis Through Altered Glycolysis.. *Cureus*. PMID: 40821334
3. Identification of UACA, EXOSC9, and ΤΜX2 in bovine periosteal cells by mass spectrometry and immunohistochemistry.. *Analytical and bioanalytical chemistry*. PMID: 24696107
4. SUV39H1-dependent methyl-degron is a critical regulator of skeletal homeostasis.. *Cell reports*. PMID: 40581930
5. Roles of PANoptosis and related genes in acute liver failure: neoteric insight from bioinformatics analysis and animal experiment verification.. *Journal of Zhejiang University. Science. B*. PMID: 40274384

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 9.6% |
| 置信残基 (pLDDT 70-90) 占比 | 65.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 10.2% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.0，有序区 74.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR042420, IPR000727; Pfam: PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APAF1 | 0.903 | 0.091 | — |
| LGALS3 | 0.784 | 0.095 | — |
| CYCS | 0.744 | 0.049 | — |
| CASP9 | 0.742 | 0.076 | — |
| PAWR | 0.607 | 0.000 | — |
| FLII | 0.604 | 0.093 | — |
| RHOH | 0.587 | 0.197 | — |
| IMMT | 0.583 | 0.000 | — |
| PRADC1 | 0.582 | 0.000 | — |
| EFHD2 | 0.572 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIE | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| REL | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| CELSR3 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| JPH1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ANKRD28 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TP63 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20085233|imex:IM-20439 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 无 | pLDDT=74.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. UACA — Uveal autoantigen with coiled-coil domains and ankyrin repeats，非常新颖，仅有少数基础研究。
2. 蛋白大小1416 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137831-UACA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UACA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137831-UACA/subcellular

![](https://images.proteinatlas.org/43503/1607_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/43503/1607_B4_6_red_green.jpg)
![](https://images.proteinatlas.org/43503/1610_G5_5_red_green.jpg)
![](https://images.proteinatlas.org/43503/1610_G5_6_red_green.jpg)
![](https://images.proteinatlas.org/43503/1667_B4_23_cr57ea4ca01eefd_red_green.jpg)
![](https://images.proteinatlas.org/43503/1667_B4_8_cr57ea4c983518f_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZF9 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR042420;IPR000727; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137831-UACA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BORCS6 | Biogrid, Bioplex | true |
| AHCYL1 | Intact | false |
| ANLN | Biogrid | false |
| CCDC125 | Intact | false |
| HIF1AN | Intact | false |
| KRAS | Biogrid | false |
| KRT31 | Intact | false |
| KRT40 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
