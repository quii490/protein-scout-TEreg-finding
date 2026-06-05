---
type: protein-evaluation
gene: "GOLGA5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLGA5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA5 / RETII, RFG5 |
| 蛋白名称 | Golgin subfamily A member 5 |
| 蛋白大小 | 731 aa / 83.0 kDa |
| UniProt ID | Q8TBA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 731 aa / 83.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019177; Pfam: PF09787 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- Golgi apparatus (GO:0005794)
- Golgi cisterna (GO:0031985)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- transport vesicle (GO:0030133)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RETII, RFG5 |

**关键文献**:
1. Golgin Subfamily A Member 5 Is Essential for Production of Extracellular Matrix Proteins during TGF-β1-Induced Periodontal Ligament-Fibroblastic Differentiation.. *Stem cells international*. PMID: 35879965
2. Gene rearrangements in radiation-induced thyroid carcinogenesis.. *Medical and pediatric oncology*. PMID: 11340615
3. Novel Genetic Variants Distinguishing Myelin Oligodendrocyte Glycoprotein-IgG-Positive From Myelin Oligodendrocyte Glycoprotein-IgG-Negative Pediatric Acute Disseminated Encephalomyelitis in Northern China.. *Pediatric neurology*. PMID: 38781724
4. Persistent and acute chlamydial infections induce different structural changes in the Golgi apparatus.. *International journal of medical microbiology : IJMM*. PMID: 24780199
5. CHD6 eviction of promoter nucleosomes maintains housekeeping transcriptional program in prostate cancer.. *Molecular therapy. Nucleic acids*. PMID: 39717618

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 45.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 31.6% |
| 有序区域 (pLDDT>70) 占比 | 62.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.6，有序区 62.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019177; Pfam: PF09787 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG7 | 0.964 | 0.000 | — |
| GOLGB1 | 0.923 | 0.000 | — |
| COG3 | 0.892 | 0.000 | — |
| CUX1 | 0.885 | 0.000 | — |
| RAB1A | 0.883 | 0.625 | — |
| COG6 | 0.876 | 0.000 | — |
| COG8 | 0.849 | 0.000 | — |
| COG5 | 0.841 | 0.000 | — |
| GOSR1 | 0.827 | 0.000 | — |
| OCRL | 0.824 | 0.230 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mcf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| AOC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| GOLGA2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC6A15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC6A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 无 | pLDDT=71.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLGA5 — Golgin subfamily A member 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小731 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066455-GOLGA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000066455-GOLGA5/subcellular

![](https://images.proteinatlas.org/992/1834_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/992/1834_F4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/992/1899_F4_3_cr5ba2041001d67_blue_red_green.jpg)
![](https://images.proteinatlas.org/992/1899_F4_8_cr5ba20410021ab_blue_red_green.jpg)
![](https://images.proteinatlas.org/992/1_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/992/1_A1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TBA6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
