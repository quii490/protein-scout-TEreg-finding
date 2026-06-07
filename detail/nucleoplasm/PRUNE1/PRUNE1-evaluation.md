---
type: protein-evaluation
gene: "PRUNE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRUNE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRUNE1 / PRUNE |
| 蛋白名称 | Exopolyphosphatase PRUNE1 |
| 蛋白大小 | 453 aa / 50.2 kDa |
| UniProt ID | Q86TP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cell junction, focal adhesion |
| 蛋白大小 | 10/10 | ×1 | 10 | 453 aa / 50.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001667, IPR038763, IPR004097, IPR038222; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cell junction, focal adhesion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRUNE |

**关键文献**:
1. Generation of Conditional Knockout Alleles for PRUNE-1.. *Cells*. PMID: 36831191
2. PRUNE1 c.933G>A synonymous variant induces exon 7 skipping, disrupts the DHHA2 domain, and leads to an atypical NMIHBA syndrome presentation: Case report and review of the literature.. *American journal of medical genetics. Part A*. PMID: 35194938
3. PAD2-Mediated Histone Citrullination Drives Tumor Progression by Enhancing Cell Proliferation and Modifying the Microenvironment in Pancreatic Cancer.. *Molecular cancer research : MCR*. PMID: 40506250
4. Neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies in a consanguineous Iranian family is associated with a homozygous start loss variant in the PRUNE1 gene.. *BMC medical genomics*. PMID: 35379233
5. An Overview of Drug-Resistant Epilepsies Based on Advances in Genetics: A Cohort Study.. *Neurology India*. PMID: 41510857

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 74.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 82.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.2，有序区 82.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001667, IPR038763, IPR004097, IPR038222; Pfam: PF01368, PF02833 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NME1 | 0.942 | 0.295 | — |
| HDDC3 | 0.900 | 0.000 | — |
| GSK3B | 0.878 | 0.749 | — |
| APRT | 0.819 | 0.000 | — |
| BNIP2 | 0.743 | 0.000 | — |
| GSK3A | 0.668 | 0.621 | — |
| BNIPL | 0.603 | 0.000 | — |
| GMPPB | 0.601 | 0.545 | — |
| DHH | 0.542 | 0.000 | — |
| PPP4C | 0.542 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000271620.3 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |
| NME1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10602478|imex:IM-20207 |
| GSK3A | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| GSK3B | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| GMFG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INSYN2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIANP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GMPPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 无 | pLDDT=85.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell junction, focal adhesion / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PRUNE1 — Exopolyphosphatase PRUNE1，非常新颖，仅有少数基础研究。
2. 蛋白大小453 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86TP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143363-PRUNE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRUNE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86TP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PRUNE1/IF_images/PRUNE1_IF_291_D8_2_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000143363-PRUNE1/subcellular

![](https://images.proteinatlas.org/28411/254_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28411/254_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28411/291_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28411/291_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28411/546_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28411/546_D8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86TP1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86TP1 |
| SMART | SM01131; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001667;IPR038763;IPR004097;IPR038222; |
| Pfam | PF01368;PF02833; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143363-PRUNE1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSK3A | Biogrid, Opencell | true |
| GSK3B | Biogrid, Opencell | true |
| NME1 | Intact, Biogrid | true |
| CXorf66 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
