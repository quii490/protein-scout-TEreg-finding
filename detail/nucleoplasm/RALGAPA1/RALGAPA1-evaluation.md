---
type: protein-evaluation
gene: "RALGAPA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RALGAPA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RALGAPA1 / GARNL1, KIAA0884, TULIP1 |
| 蛋白名称 | Ral GTPase-activating protein subunit alpha-1 |
| 蛋白大小 | 2036 aa / 229.8 kDa |
| UniProt ID | Q6GYQ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Mitochondria, Mid piece, Principal piece; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2036 aa / 229.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR035974, IPR000331, IPR046859, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Mitochondria, Mid piece, Principal piece | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GARNL1, KIAA0884, TULIP1 |

**关键文献**:
1. Identification of SURF4 and RALGAPA1 as promising therapeutic targets in glioblastoma and pan-cancer through integrative multi-omics, CRISPR-Cas9 screening and prognostic meta-analysis.. *Cancer immunology, immunotherapy : CII*. PMID: 40249536
2. Whole‑exome sequencing insights into synchronous bilateral breast cancer with discordant molecular subtypes.. *Oncology letters*. PMID: 39430730
3. RALGAPA1 Deletion in Belgian Shepherd Dogs with Cerebellar Ataxia.. *Genes*. PMID: 37628572
4. Bi-allelic Variants in RALGAPA1 Cause Profound Neurodevelopmental Disability, Muscular Hypotonia, Infantile Spasms, and Feeding Abnormalities.. *American journal of human genetics*. PMID: 32004447
5. Genome-Wide Association Study for Test-Day Milk Yield, Proteins, and Composition Traits of Crossbred Dairy Cattle in Ethiopia.. *International journal of genomics*. PMID: 39473539

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 28.6% |
| 置信残基 (pLDDT 70-90) 占比 | 35.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 28.6% |
| 有序区域 (pLDDT>70) 占比 | 64.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 64.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR035974, IPR000331, IPR046859, IPR027107; Pfam: PF20412, PF02145 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RALGAPB | 0.825 | 0.292 | — |
| NKIRAS2 | 0.825 | 0.774 | — |
| LRPAP1 | 0.813 | 0.000 | — |
| GFOD1 | 0.646 | 0.646 | — |
| ARHGAP4 | 0.622 | 0.000 | — |
| MEA1 | 0.608 | 0.608 | — |
| AP2B1 | 0.606 | 0.598 | — |
| FAM91A1 | 0.595 | 0.000 | — |
| RHOH | 0.586 | 0.195 | — |
| AP2M1 | 0.563 | 0.557 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| RRP1B | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-26334|pubmed:19710015 |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| RAB11A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDIA4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CLU | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| AP2M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GFOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 无 | pLDDT=69.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Mitochondria, Mid piece, Principal pi | 一致 |
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
1. RALGAPA1 — Ral GTPase-activating protein subunit alpha-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2036 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6GYQ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174373-RALGAPA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RALGAPA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6GYQ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000174373-RALGAPA1/subcellular

![](https://images.proteinatlas.org/851/10_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/851/10_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/851/11_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/851/11_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/851/15_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/851/15_C11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6GYQ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6GYQ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1796..2004; /note="Rap-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00165" |
| InterPro | IPR016024;IPR035974;IPR000331;IPR046859;IPR027107; |
| Pfam | PF20412;PF02145; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174373-RALGAPA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAZ | Biogrid, Opencell | true |
| AP2B1 | Biogrid | false |
| LAMP1 | Biogrid | false |
| RAB11A | Biogrid | false |
| RHOB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
