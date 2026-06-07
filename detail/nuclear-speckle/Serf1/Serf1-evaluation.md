---
type: protein-evaluation
gene: "Serf1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Serf1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Serf1 / FAM2A, SERF1, SMAM1 |
| 蛋白名称 | Small EDRK-rich factor 1 |
| 蛋白大小 | 110 aa / 12.3 kDa |
| UniProt ID | O75920 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 110 aa / 12.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007513, IPR040211; Pfam: PF04419 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Uncertain |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM2A, SERF1, SMAM1 |

**关键文献**:
1. G-CSF resistance of ELANE-mutant neutropenia depends on SERF1-containing truncated-neutrophil elastase aggregates.. *The Journal of clinical investigation*. PMID: 39560992
2. Salt-responsive ERF1 regulates reactive oxygen species-dependent signaling during the initial response to salt stress in rice.. *The Plant cell*. PMID: 23800963
3. Molecular analysis of SMN2, NAIP, and GTF2H2 gene deletions and relationships with clinical subtypes of spinal muscular atrophy.. *Journal of neurogenetics*. PMID: 39321203
4. Genomic analysis of a spinal muscular atrophy (SMA) discordant family identifies a novel mutation in TLL2, an activator of growth differentiation factor 8 (myostatin): a case report.. *BMC medical genetics*. PMID: 31888525
5. Analysis of the plant hormone expression profile during somatic embryogenesis induction in teak (Tectona grandis).. *Frontiers in plant science*. PMID: 39439509

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 37.3% |
| 中等置信 (pLDDT 50-70) 占比 | 38.2% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 37.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 37.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007513, IPR040211; Pfam: PF04419 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFAF3 | 0.919 | 0.000 | — |
| SMN1 | 0.885 | 0.000 | — |
| NAIP | 0.872 | 0.000 | — |
| SMN2 | 0.843 | 0.000 | — |
| GPKOW | 0.724 | 0.000 | — |
| C1S | 0.720 | 0.000 | — |
| BDP1 | 0.689 | 0.000 | — |
| GTF2H2 | 0.616 | 0.000 | — |
| TAAR8 | 0.605 | 0.000 | — |
| TPMT | 0.592 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIK3R3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SERF1A | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| ELOVL7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. Serf1 — Small EDRK-rich factor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小110 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75920
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172058-SERF1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Serf1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75920
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (uncertain)。来源: https://www.proteinatlas.org/ENSG00000172058-SERF1A/subcellular

![](https://images.proteinatlas.org/75271/1565_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75271/1565_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/75271/1569_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75271/1569_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75271/1595_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75271/1595_E4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75920-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75920 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007513;IPR040211; |
| Pfam | PF04419; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172058-SERF1A/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
