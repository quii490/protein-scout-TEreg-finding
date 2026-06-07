---
type: protein-evaluation
gene: "GLB1L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLB1L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLB1L2 |
| 蛋白名称 | Beta-galactosidase-1-like protein 2 |
| 蛋白大小 | 636 aa / 72.1 kDa |
| UniProt ID | Q8IW92 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 636 aa / 72.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026283, IPR048912, IPR048913, IPR008979, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- vacuole (GO:0005773)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcriptome-wide map of N6-methyladenosine (m6A) profiling in coronary artery disease (CAD) with clopidogrel resistance.. *Clinical epigenetics*. PMID: 38098098
2. Sequencing Analysis Demonstrates That a Complex Genetic Architecture Contributes to Risk for Spina Bifida.. *Birth defects research*. PMID: 41013918
3. Nine genes abundantly expressed in the epididymis are not essential for male fecundity in mice.. *Andrology*. PMID: 30927342
4. Integrative analyses of ferroptosis and immune related biomarkers and the osteosarcoma associated mechanisms.. *Scientific reports*. PMID: 37031292
5. Molecular Expression of Some Oncogenes and Predisposing Behaviors Contributing to the Aggressiveness of Prostate Cancer.. *Reports of biochemistry & molecular biology*. PMID: 34277869

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.0 |
| 高置信度残基 (pLDDT>90) 占比 | 89.9% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.0，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026283, IPR048912, IPR048913, IPR008979, IPR017853; Pfam: PF21317, PF21467, PF01301 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PATE3 | 0.595 | 0.000 | — |
| PATE2 | 0.560 | 0.000 | — |
| PATE1 | 0.543 | 0.000 | — |
| PRR32 | 0.502 | 0.000 | — |
| DEFB115 | 0.481 | 0.000 | — |
| CLPSL2 | 0.447 | 0.000 | — |
| GOLPH3L | 0.433 | 0.433 | — |
| LRRC23 | 0.427 | 0.000 | — |
| ZNF431 | 0.425 | 0.000 | — |
| AFAP1L1 | 0.424 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAMK2A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC39A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FUT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASIC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FUT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PNLDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.0 + PDB: 无 | pLDDT=94.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

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
1. GLB1L2 — Beta-galactosidase-1-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小636 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IW92
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149328-GLB1L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLB1L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IW92
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149328-GLB1L2/subcellular

![](https://images.proteinatlas.org/54808/1036_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/54808/1036_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/54808/893_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/54808/893_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/54808/895_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/54808/895_D5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IW92-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IW92 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026283;IPR048912;IPR048913;IPR008979;IPR017853;IPR031330;IPR019801;IPR001944; |
| Pfam | PF21317;PF21467;PF01301; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149328-GLB1L2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAMK2A | Intact | false |
| CYSRT1 | Intact | false |
| DKKL1 | Bioplex | false |
| GP9 | Bioplex | false |
| HTR1B | Bioplex | false |
| KCNK1 | Bioplex | false |
| KLK15 | Bioplex | false |
| SFTPC | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
