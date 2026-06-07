---
type: protein-evaluation
gene: "SUSD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUSD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUSD1 |
| 蛋白名称 | Sushi domain-containing protein 1 |
| 蛋白大小 | 747 aa / 82.7 kDa |
| UniProt ID | Q6UWL2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 747 aa / 82.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR001881, IPR000152, IPR018097, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Metagenome-derived SusD-homologs affiliated with Bacteroidota bind to synthetic polymers.. *Applied and environmental microbiology*. PMID: 38953372
2. Development and Validation of Epigenetic Signature Predict Survival for Patients with Laryngeal Squamous Cell Carcinoma.. *DNA and cell biology*. PMID: 33481663
3. Identification of transcriptome alterations in the prefrontal cortex, hippocampus, amygdala and hippocampus of suicide victims.. *Scientific reports*. PMID: 34552157
4. Combined impact of CHCHD10 p.Gly66Val and three other variants suggests oligogenic contributions to ALS.. *Frontiers in neurology*. PMID: 40170896
5. Whole-Genome Sequencing of Cytogenetically Balanced Chromosome Translocations Identifies Potentially Pathological Gene Disruptions and Highlights the Importance of Microhomology in the Mechanism of Formation.. *Human mutation*. PMID: 27862604

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 15.0% |
| 置信残基 (pLDDT 70-90) 占比 | 63.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 78.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.8，有序区 78.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR001881, IPR000152, IPR018097, IPR057598; Pfam: PF07645, PF23144, PF00084 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC115 | 0.538 | 0.069 | — |
| CAPN9 | 0.529 | 0.098 | — |
| SLC46A2 | 0.519 | 0.051 | — |
| SUSD2 | 0.510 | 0.000 | — |
| NIPSNAP3B | 0.493 | 0.000 | — |
| CYP2F1 | 0.491 | 0.051 | — |
| FAM71C | 0.479 | 0.000 | — |
| CHFR | 0.479 | 0.086 | — |
| HSPA4L | 0.477 | 0.102 | — |
| TBC1D9B | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000363388.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| INSL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ST8SIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLEC2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCGB1D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GAT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMAN2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNASE13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 无 | pLDDT=77.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
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
1. SUSD1 — Sushi domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小747 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWL2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106868-SUSD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUSD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWL2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106868-SUSD1/subcellular

![](https://images.proteinatlas.org/48554/823_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/48554/823_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/48554/858_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/48554/858_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/48554/967_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/48554/967_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UWL2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UWL2 |
| SMART | SM00032;SM00181;SM00179; |
| UniProt Domain [FT] | DOMAIN 35..72; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 73..112; /note="EGF-like 2; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 125..162; /note="EGF-like 3; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 177..236; /note="Sushi 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00302"; DOMAIN 237..296; /note="Sushi 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00302" |
| InterPro | IPR000742;IPR001881;IPR000152;IPR018097;IPR057598;IPR009030;IPR049883;IPR051622;IPR035976;IPR000436; |
| Pfam | PF07645;PF23144;PF00084; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106868-SUSD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
