---
type: protein-evaluation
gene: "FOXP4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXP4 — REJECTED (研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXP4 / FKHLA |
| 蛋白名称 | Forkhead box protein P4 |
| 蛋白大小 | 680 aa / 73.5 kDa |
| UniProt ID | Q8IVH2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 680 aa / 73.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 6XAT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047414, IPR001766, IPR050998, IPR032354, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 189 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHLA |

**关键文献**:
1. FOXP4 Is a Direct YAP1 Target That Promotes Gastric Cancer Stemness and Drives Metastasis.. *Cancer research*. PMID: 39047223
2. Spatiotemporal single-cell regulatory atlas reveals neural crest lineage diversification and cellular function during tooth morphogenesis.. *Nature communications*. PMID: 35974052
3. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844
4. FOXP4-mediated induction of PTK7 activates the Wnt/β-catenin pathway and promotes ovarian cancer development.. *Cell death & disease*. PMID: 38740744
5. FOXP4 Variants Are Associated With Plateau Iris and Angle Closure Glaucoma.. *Investigative ophthalmology & visual science*. PMID: 40637512

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 15.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 54.7% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 6XAT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047414, IPR001766, IPR050998, IPR032354, IPR030456; Pfam: PF00250, PF16159 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXP2 | 0.952 | 0.863 | — |
| HAND1 | 0.939 | 0.000 | — |
| FOXP1 | 0.867 | 0.625 | — |
| FOXP3 | 0.812 | 0.786 | — |
| FOXP1-2 | 0.794 | 0.422 | — |
| HAND2 | 0.764 | 0.000 | — |
| DHDDS | 0.568 | 0.568 | — |
| ZNF609 | 0.547 | 0.000 | — |
| CTBP1 | 0.502 | 0.000 | — |
| EZH2 | 0.485 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DEGS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ezrA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000516024.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2797100 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Pou5f1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| TBR1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | imex:IM-26315|pubmed:25232744 |
| DHDDS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPL12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FOXP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 6XAT | pLDDT=58.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXP4 — Forkhead box protein P4，研究基础较多，新颖性有限。
2. 蛋白大小680 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVH2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137166-FOXP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVH2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000137166-FOXP4/subcellular

![](https://images.proteinatlas.org/6538/2162_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/6538/2162_H9_3_red_green.jpg)
![](https://images.proteinatlas.org/6538/2192_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/6538/2192_E4_5_red_green.jpg)
![](https://images.proteinatlas.org/6538/2227_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/6538/2227_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IVH2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IVH2 |
| SMART | SM00339; |
| UniProt Domain [FT] | DOMAIN 333..373; /note="FoxP leucine zipper (ZIP)"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01424" |
| InterPro | IPR047414;IPR001766;IPR050998;IPR032354;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250;PF16159; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137166-FOXP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FOXP1 | Intact, Biogrid | true |
| FOXP2 | Intact, Biogrid | true |
| FOXP3 | Biogrid, Bioplex | true |
| EEF1AKMT3 | Bioplex | false |
| NFIA | Biogrid | false |
| NFIB | Biogrid | false |
| NFIC | Biogrid | false |
| NFIX | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
