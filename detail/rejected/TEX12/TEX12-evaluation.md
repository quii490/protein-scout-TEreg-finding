---
type: protein-evaluation
gene: "TEX12"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEX12 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX12 |
| 蛋白名称 | Testis-expressed protein 12 |
| 蛋白大小 | 123 aa / 14.1 kDa |
| UniProt ID | Q9BXU0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome, Basal body; UniProt: Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 123 aa / 14.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.7; PDB: 6HK8, 6HK9, 6R17, 6R2F, 6YQF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029193; Pfam: PF15219 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body | Supported |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- central element (GO:0000801)
- chromosome (GO:0005694)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Coiled-coil structure of meiosis protein TEX12 and conformational regulation by its C-terminal tip.. *Communications biology*. PMID: 36071143
2. Centrosome dysfunction associated with somatic expression of the synaptonemal complex protein TEX12.. *Communications biology*. PMID: 34880391
3. Progression of meiotic recombination requires structural maturation of the central element of the synaptonemal complex.. *Journal of cell science*. PMID: 18611960
4. A Novel Frameshift Microdeletion of the TEX12 Gene Caused Infertility in Two Brothers with Nonobstructive Azoospermia.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 37012491
5. Characterization of a novel meiosis-specific protein within the central element of the synaptonemal complex.. *Journal of cell science*. PMID: 16968740

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 57.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 20.3% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 61.8% |
| 可用 PDB 条目 | 6HK8, 6HK9, 6R17, 6R2F, 6YQF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6HK8, 6HK9, 6R17, 6R2F, 6YQF）+ AlphaFold极高置信度预测（pLDDT=79.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029193; Pfam: PF15219 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCE2 | 0.999 | 0.930 | — |
| SYCE1 | 0.997 | 0.000 | — |
| SYCE3 | 0.993 | 0.000 | — |
| SYCP1 | 0.983 | 0.000 | — |
| SYCP3 | 0.959 | 0.000 | — |
| SYCP2 | 0.900 | 0.000 | — |
| C14orf39 | 0.866 | 0.000 | — |
| SMC1B | 0.789 | 0.000 | — |
| REC8 | 0.783 | 0.000 | — |
| STAG3 | 0.782 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MSGN1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| COX5B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SUOX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SYCE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NUP54 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| INCA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGF29 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF835 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LENG1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 6HK8, 6HK9, 6R17, 6R2F, 6YQF | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Centrosome, Basal body | 一致 |
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
1. TEX12 — Testis-expressed protein 12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小123 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXU0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150783-TEX12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXU0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000150783-TEX12/subcellular

![](https://images.proteinatlas.org/38289/2175_G6_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/38289/2175_G6_92_blue_red_green.jpg)
![](https://images.proteinatlas.org/38289/2191_F4_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/38289/2191_F4_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/38289/2201_H2_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/38289/2201_H2_57_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXU0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
