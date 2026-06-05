---
type: protein-evaluation
gene: "GLIPR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLIPR2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLIPR2 / C9orf19, GAPR1 |
| 蛋白名称 | Golgi-associated plant pathogenesis-related protein 1 |
| 蛋白大小 | 154 aa / 17.2 kDa |
| UniProt ID | Q9H4G4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; 额外: Microtubules; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 154 aa / 17.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.2; PDB: 1SMB, 4AIW, 5VHG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018244, IPR014044, IPR035940, IPR001283, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Microtubules | Uncertain |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- Golgi membrane (GO:0000139)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.2 |
| 高置信度残基 (pLDDT>90) 占比 | 90.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.0% |
| 可用 PDB 条目 | 1SMB, 4AIW, 5VHG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1SMB, 4AIW, 5VHG）+ AlphaFold高质量预测（pLDDT=95.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018244, IPR014044, IPR035940, IPR001283, IPR034113; Pfam: PF00188 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BECN1 | 0.894 | 0.292 | — |
| GART | 0.831 | 0.000 | — |
| GLIPR1 | 0.762 | 0.000 | — |
| TMEM37 | 0.540 | 0.000 | — |
| CRISP1 | 0.527 | 0.000 | — |
| UVRAG | 0.521 | 0.000 | — |
| RUBCN | 0.503 | 0.000 | — |
| TFEB | 0.498 | 0.000 | — |
| FAM90A7P | 0.474 | 0.000 | — |
| PI15 | 0.471 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cblb | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |
| VAMP5 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| Hmga2 | psi-mi:"MI:0096"(pull down) | imex:IM-23312|pubmed:26045162 |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| ZBTB18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-29234|pubmed:35800763 |
| HASPIN | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 7
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.2 + PDB: 1SMB, 4AIW, 5VHG | pLDDT=95.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Vesicles; 额外: Microtubules | 一致 |
| PPI | STRING + IntAct | 14 + 7 interactions | 数据充分 |

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
1. GLIPR2 — Golgi-associated plant pathogenesis-related protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4G4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122694-GLIPR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLIPR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4G4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000122694-GLIPR2/subcellular

![](https://images.proteinatlas.org/29478/281_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29478/281_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29478/282_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29478/282_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29478/283_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29478/283_G10_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4G4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
