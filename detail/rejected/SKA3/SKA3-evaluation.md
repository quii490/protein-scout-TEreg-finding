---
type: protein-evaluation
gene: "SKA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SKA3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKA3 / C13orf3, RAMA1 |
| 蛋白名称 | Spindle and kinetochore-associated protein 3 |
| 蛋白大小 | 412 aa / 46.4 kDa |
| UniProt ID | Q8IX90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitotic spindle, Centrosome; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton, spindle; Chromosome, centromere, ki |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 46.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.8; PDB: 4AJ5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033341 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitotic spindle, Centrosome; 额外: Cytosol | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, spindle; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- meiotic spindle (GO:0072687)
- mitotic spindle (GO:0072686)
- outer kinetochore (GO:0000940)
- SKA complex (GO:0170027)
- spindle microtubule (GO:0005876)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 138 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf3, RAMA1 |

**关键文献**:
1. Hypoxia-induced SKA3 promoted cholangiocarcinoma progression and chemoresistance by enhancing fatty acid synthesis via the regulation of PAR-dependent HIF-1a deubiquitylation.. *Journal of experimental & clinical cancer research : CR*. PMID: 37821935
2. SKA3-mediated hypoxia tolerance and metabolic reprogramming promote liver metastasis in lung adenocarcinoma.. *Cell death & disease*. PMID: 41298345
3. SKA3, negatively regulated by miR-128-3p, promotes the progression of non-small-cell lung cancer.. *Personalized medicine*. PMID: 34533066
4. Circular RNA circ_SKA3 enhances gastric cancer development by targeting miR-520h.. *Histology and histopathology*. PMID: 36134741
5. SKA3 is a prognostic biomarker and associated with immune infiltration in bladder cancer.. *Hereditas*. PMID: 35546682

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.8 |
| 高置信度残基 (pLDDT>90) 占比 | 24.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 23.5% |
| 低置信 (pLDDT<50) 占比 | 40.3% |
| 有序区域 (pLDDT>70) 占比 | 36.2% |
| 可用 PDB 条目 | 4AJ5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.8），有序残基占 36.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033341 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKA1 | 0.999 | 0.985 | — |
| SKA2 | 0.999 | 0.980 | — |
| BUB1B | 0.976 | 0.171 | — |
| CENPF | 0.968 | 0.000 | — |
| SPDL1 | 0.947 | 0.099 | — |
| NDC80 | 0.943 | 0.000 | — |
| PLK1 | 0.934 | 0.292 | — |
| BOD1 | 0.933 | 0.000 | — |
| CCNB1 | 0.911 | 0.000 | — |
| NUF2 | 0.893 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2R2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| SKA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| NOL4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCDC85C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC85B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SKA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOL4L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PYCR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.8 + PDB: 4AJ5 | pLDDT=63.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, spindle; Chromosome, cent / Mitotic spindle, Centrosome; 额外: Cytosol | 一致 |
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
1. SKA3 — Spindle and kinetochore-associated protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IX90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165480-SKA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IX90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitotic spindle (uncertain)。来源: https://www.proteinatlas.org/ENSG00000165480-SKA3/subcellular

![](https://images.proteinatlas.org/39356/1825_G7_37_cr5ac34600d8353_blue_red_green.jpg)
![](https://images.proteinatlas.org/39356/1825_G7_50_cr5bb4856a8a0f1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39356/2038_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39356/2038_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39356/2133_F8_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/39356/2133_F8_80_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IX90-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
