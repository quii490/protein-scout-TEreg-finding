---
type: protein-evaluation
gene: "TGIF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TGIF1 — REJECTED (研究热度过高 (PubMed strict=141，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TGIF1 / TGIF |
| 蛋白名称 | Homeobox protein TGIF1 |
| 蛋白大小 | 401 aa / 43.0 kDa |
| UniProt ID | Q15583 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 401 aa / 43.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=141 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 2LK2, 6FQP, 6FQQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR008422, IPR050224; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 141 |
| PubMed broad count | 299 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TGIF |

**关键文献**:
1. Holoprosencephaly Overview.. **. PMID: 20301702
2. TGIF1 overexpression promotes glioma progression and worsens patient prognosis.. *Cancer medicine*. PMID: 35569122
3. Loss of TGFβ-Mediated Repression of Angiopoietin-2 in Pericytes Underlies Germinal Matrix Hemorrhage Pathogenesis.. *Stroke*. PMID: 39129597
4. Novel IgG and IgA autoantibodies validated in two independent cohorts are associated with disease activity and determine organ manifestations in systemic lupus erythematosus: implications for anti-LIN28A, anti-HMGN5, anti-IRF5, and anti-TGIF1.. *Annals of the rheumatic diseases*. PMID: 40348637
5. Molecular characterization and effects of the TGIF1 gene on proliferation and steroidogenesis in yak (Bos grunniens) granulosa cells.. *Theriogenology*. PMID: 37660474

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 18.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 51.6% |
| 有序区域 (pLDDT>70) 占比 | 26.0% |
| 可用 PDB 条目 | 2LK2, 6FQP, 6FQQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 26.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR008422, IPR050224; Pfam: PF05920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMAD2 | 0.991 | 0.525 | — |
| SMAD3 | 0.974 | 0.598 | — |
| TGIF2 | 0.911 | 0.000 | — |
| CTBP1 | 0.883 | 0.715 | — |
| HDAC1 | 0.831 | 0.628 | — |
| CTBP2 | 0.796 | 0.607 | — |
| SMAD4 | 0.789 | 0.081 | — |
| RARA | 0.701 | 0.095 | — |
| SMAD7 | 0.680 | 0.064 | — |
| SIX3 | 0.665 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MED31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STK16 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MKKS | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SDAD1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CTBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-25511|pubmed:25910212 |
| ENSP00000384133.2 | psi-mi:"MI:0432"(one hybrid) | imex:IM-25511|pubmed:25910212 |
| AXIN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:25873176|imex:IM-24341 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 2LK2, 6FQP, 6FQQ | pLDDT=58.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TGIF1 — Homeobox protein TGIF1，研究基础较多，新颖性有限。
2. 蛋白大小401 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 141 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 141 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15583
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177426-TGIF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TGIF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15583
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000177426-TGIF1/subcellular

![](https://images.proteinatlas.org/62160/1112_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/62160/1112_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/62160/1116_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/62160/1116_B11_4_red_green.jpg)
![](https://images.proteinatlas.org/62160/1169_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/62160/1169_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15583-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15583 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR009057;IPR008422;IPR050224; |
| Pfam | PF05920; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177426-TGIF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTBP1 | Intact, Biogrid | true |
| CTBP2 | Intact, Biogrid | true |
| PML | Intact, Biogrid | true |
| SMAD3 | Intact, Biogrid | true |
| APP | Intact | false |
| AXIN1 | Intact | false |
| AXIN2 | Intact | false |
| HDAC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
