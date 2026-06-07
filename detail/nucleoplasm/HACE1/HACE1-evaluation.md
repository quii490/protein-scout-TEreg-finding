---
type: protein-evaluation
gene: "HACE1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HACE1 — REJECTED (研究热度过高 (PubMed strict=111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HACE1 / KIAA1320 |
| 蛋白名称 | E3 ubiquitin-protein ligase HACE1 |
| 蛋白大小 | 909 aa / 102.3 kDa |
| UniProt ID | Q8IYU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nuclear bodies; UniProt: Golgi apparatus, Golgi stack membrane; Cytoplasm; Endoplasmi |
| 蛋白大小 | 8/10 | ×1 | 8 | 909 aa / 102.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=111 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.5; PDB: 8H8X, 8HAE, 8PWL, 8Q0N |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR050409, IPR000569, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nuclear bodies | Supported |
| UniProt | Golgi apparatus, Golgi stack membrane; Cytoplasm; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 111 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1320 |

**关键文献**:
1. HMBOX1 reverses autophagy mediated 5-fluorouracil resistance through promoting HACE1-induced ubiquitination and degradation of ATG5 in colorectal cancer.. *Autophagy*. PMID: 40126194
2. CircRNA-CREIT inhibits stress granule assembly and overcomes doxorubicin resistance in TNBC by destabilizing PKR.. *Journal of hematology & oncology*. PMID: 36038948
3. ZDHHC3-mediated SCAP S-acylation promotes cholesterol biosynthesis and tumor immune escape in hepatocellular carcinoma.. *Cell reports*. PMID: 39522165
4. HACE1 as a bridge between oxidative stress and autophagy.. *Frontiers in immunology*. PMID: 40948788
5. Loss of the Tumor Suppressor HACE1 Contributes to Cancer Progression.. *Current drug targets*. PMID: 30827236

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 84.3% |
| 可用 PDB 条目 | 8H8X, 8HAE, 8PWL, 8Q0N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8H8X, 8HAE, 8PWL, 8Q0N）+ AlphaFold高质量预测（pLDDT=83.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR050409, IPR000569, IPR035983; Pfam: PF12796, PF13637, PF00632 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KIAA1324 | 0.942 | 0.058 | — |
| UBE2L3 | 0.935 | 0.832 | — |
| RAC1 | 0.866 | 0.833 | — |
| PRNP | 0.607 | 0.058 | — |
| TRRAP | 0.575 | 0.094 | — |
| RAB4A | 0.559 | 0.544 | — |
| OPTN | 0.523 | 0.292 | — |
| ALYREF | 0.519 | 0.414 | — |
| HTT | 0.478 | 0.089 | — |
| TBC1D32 | 0.463 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLXNA2 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| IRF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| RAB4A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OPTN | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-22995|pubmed:25026213 |
| UBE2L3 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22995|pubmed:25026213 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22995|pubmed:25026213 |
| ENSP00000262903.4 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22995|pubmed:25026213 |
| USP2 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22995|pubmed:25026213 |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| POTEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 8H8X, 8HAE, 8PWL, 8Q0N | pLDDT=83.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane; Cytoplasm;  / Endoplasmic reticulum; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. HACE1 — E3 ubiquitin-protein ligase HACE1，研究基础较多，新颖性有限。
2. 蛋白大小909 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 111 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000085382-HACE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HACE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000085382-HACE1/subcellular

![](https://images.proteinatlas.org/46071/1609_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/46071/1609_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/46071/1634_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/46071/1634_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/46071/1697_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/46071/1697_H10_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYU2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IYU2 |
| SMART | SM00248;SM00119; |
| UniProt Domain [FT] | DOMAIN 574..909; /note="HECT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00104" |
| InterPro | IPR002110;IPR036770;IPR050409;IPR000569;IPR035983; |
| Pfam | PF12796;PF13637;PF00632; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000085382-HACE1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| OPTN | Intact, Biogrid | true |
| RAB4A | Intact, Biogrid | true |
| RAC1 | Intact, Biogrid | true |
| CASR | Biogrid | false |
| CCNC | Biogrid | false |
| SNTG2 | Biogrid | false |
| SPIDR | Biogrid | false |
| UBE2L3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
