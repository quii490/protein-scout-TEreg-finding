---
type: protein-evaluation
gene: "R3HCC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## R3HCC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | R3HCC1 |
| 蛋白名称 | R3H and coiled-coil domain-containing protein 1 |
| 蛋白大小 | 440 aa / 49.1 kDa |
| UniProt ID | Q9Y3T6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 440 aa / 49.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR001374, IPR036867, IPR039884; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A novel diabetic foot ulcer diagnostic model: identification and analysis of genes related to glutamine metabolism and immune infiltration.. *BMC genomics*. PMID: 38287255
2. Identification of disulfidptosis-related genes in immunity and immunotherapy in diabetic foot ulcer.. *Annals of medicine and surgery (2012)*. PMID: 41675755
3. Genetic profile and biological implication of PIN2/TRF1-interacting telomerase inhibitor 1 (PinX1) in human cancers: an analysis using The Cancer Genome Atlas.. *Oncotarget*. PMID: 28978030
4. Association between a single nucleotide polymorphism in the R3HCC1 gene and irinotecan toxicity.. *Cancer medicine*. PMID: 36308049

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 26.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.3% |
| 低置信 (pLDDT<50) 占比 | 37.0% |
| 有序区域 (pLDDT>70) 占比 | 48.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 48.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR001374, IPR036867, IPR039884; Pfam: PF01424 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHMP7 | 0.678 | 0.000 | — |
| SVOPL | 0.509 | 0.000 | — |
| DMAP1 | 0.468 | 0.000 | — |
| SNAP47 | 0.459 | 0.000 | — |
| GPKOW | 0.441 | 0.000 | — |
| FAM149A | 0.440 | 0.000 | — |
| MOCS1 | 0.434 | 0.000 | — |
| YIPF3 | 0.432 | 0.000 | — |
| TMEM63C | 0.428 | 0.000 | — |
| ZNF414 | 0.420 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2R2B | psi-mi:"MI:0096"(pull down) | imex:IM-9155|pubmed:19156129 |
| SLITRK6 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SHC2 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PIK3R1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Rcc1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SAMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 6
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 无 | pLDDT=66.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 13 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. R3HCC1 — R3H and coiled-coil domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小440 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3T6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104679-R3HCC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=R3HCC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3T6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000104679-R3HCC1/subcellular

![](https://images.proteinatlas.org/23153/215_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23153/215_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23153/216_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23153/216_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23153/217_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23153/217_D2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3T6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3T6 |
| SMART | SM00393; |
| UniProt Domain [FT] | DOMAIN 16..81; /note="R3H"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00382" |
| InterPro | IPR012677;IPR001374;IPR036867;IPR039884; |
| Pfam | PF01424; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104679-R3HCC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NUMA1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
