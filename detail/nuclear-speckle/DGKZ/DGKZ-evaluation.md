---
type: protein-evaluation
gene: "DGKZ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DGKZ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGKZ / DAGK6 |
| 蛋白名称 | Diacylglycerol kinase zeta |
| 蛋白大小 | 928 aa / 104.0 kDa |
| UniProt ID | Q13574 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm, cytosol; Cell membrane; Cell projection, |
| 蛋白大小 | 8/10 | ×1 | 8 | 928 aa / 104.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.4; PDB: 5ELQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR017438, IPR047485, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol; Cell membrane; Cell projection, lamellipodium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- lamellipodium (GO:0030027)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAGK6 |

**关键文献**:
1. Base-editing mutagenesis maps alleles to tune human T cell functions.. *Nature*. PMID: 38093011
2. Whole Exome Sequencing Identifies Epithelial and Immune Dysfunction-Related Biomarkers in Food Protein-Induced Enterocolitis Syndrome.. *Clinical and experimental allergy : journal of the British Society for Allergy and Clinical Immunology*. PMID: 39348862
3. Expression analysis and genotyping of DGKZ: a GWAS-derived risk gene for schizophrenia.. *Molecular biology reports*. PMID: 31087244
4. Whole-genome sequencing identifies novel genes for autism in Chinese trios.. *Science China. Life sciences*. PMID: 39126614
5. Comparative Analysis of Transcriptome Profiles in Patients with Thromboangiitis Obliterans.. *Genes*. PMID: 38275601

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 44.0% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| 可用 PDB 条目 | 5ELQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=77.4，有序区 72.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR017438, IPR047485, IPR047484; Pfam: PF12796, PF00130, PF00609 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNX27 | 0.987 | 0.512 | — |
| LPL | 0.900 | 0.000 | — |
| MARCKS | 0.845 | 0.000 | — |
| PLCG1 | 0.842 | 0.292 | — |
| GNPAT | 0.821 | 0.000 | — |
| DLG4 | 0.818 | 0.095 | — |
| GPD2 | 0.809 | 0.000 | — |
| PLD2 | 0.801 | 0.073 | — |
| ARRB1 | 0.789 | 0.000 | — |
| PPP6R1 | 0.766 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8IVW9 | psi-mi:"MI:0053"(fluorescence polarization spectro | doi:10.1038/s41467-022-33018-0 |
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| MYZAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SAT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RB1 | psi-mi:"MI:0019"(coimmunoprecipitation) | imex:IM-14473|pubmed:16286473 |
| RBL1 | psi-mi:"MI:0096"(pull down) | imex:IM-14473|pubmed:16286473 |
| RBL2 | psi-mi:"MI:0096"(pull down) | imex:IM-14473|pubmed:16286473 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| ARRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| Q8CLY1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 5ELQ | pLDDT=77.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Cell membrane; Cell p / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DGKZ — Diacylglycerol kinase zeta，非常新颖，仅有少数基础研究。
2. 蛋白大小928 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13574
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149091-DGKZ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGKZ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13574
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000149091-DGKZ/subcellular

![](https://images.proteinatlas.org/51336/791_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/51336/791_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/51336/798_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/51336/798_A10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13574-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13574 |
| SMART | SM00248;SM00109;SM00045;SM00046; |
| UniProt Domain [FT] | DOMAIN 291..425; /note="DAGKc"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00783" |
| InterPro | IPR002110;IPR036770;IPR017438;IPR047485;IPR047484;IPR037607;IPR056383;IPR000756;IPR001206;IPR016064;IPR002219; |
| Pfam | PF12796;PF00130;PF00609;PF00781;PF23578; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149091-DGKZ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PIK3CA | Biogrid | false |
| SNX27 | Biogrid | false |
| TP53 | Biogrid | false |
| VHL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
