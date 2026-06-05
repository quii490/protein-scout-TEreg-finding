---
type: protein-evaluation
gene: "KBTBD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KBTBD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KBTBD4 / BKLHD4 |
| 蛋白名称 | Kelch repeat and BTB domain-containing protein 4 |
| 蛋白大小 | 534 aa / 59.9 kDa |
| UniProt ID | Q9NVX7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 534 aa / 59.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.7; PDB: 2EQX, 8VOJ, 8VPQ, 8VRT, 9DTG, 9DTQ, 9GGL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011705, IPR017096, IPR000210, IPR042884, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.5/180** | |
| **归一化总分** | | | **79.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BKLHD4 |

**关键文献**:
1. Disease-associated KBTBD4 mutations in medulloblastoma elicit neomorphic ubiquitylation activity to promote CoREST degradation.. *Cell death and differentiation*. PMID: 35379950
2. Histopathology and molecular pathology of pediatric pineal parenchymal tumors.. *Child's nervous system : ChNS : official journal of the International Society for Pediatric Neurosurgery*. PMID: 35972537
3. Molecular Stratification of Medulloblastoma: Clinical Outcomes and Therapeutic Interventions.. *Anticancer research*. PMID: 35489737
4. KBTBD4 Cancer Hotspot Mutations Drive Neomorphic Degradation of HDAC1/2 Corepressor Complexes.. *bioRxiv : the preprint server for biology*. PMID: 38798357
5. KBTBD4-mediated reduction of MYC is critical for hematopoietic stem cell expansion upon UM171 treatment.. *Blood*. PMID: 38207291

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 16.9% |
| 有序区域 (pLDDT>70) 占比 | 73.6% |
| 可用 PDB 条目 | 2EQX, 8VOJ, 8VPQ, 8VRT, 9DTG, 9DTQ, 9GGL, 9GGM, 9GGN, 9I2C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EQX, 8VOJ, 8VPQ, 8VRT, 9DTG, 9DTQ, 9GGL, 9GGM, 9GGN, 9I2C）+ AlphaFold极高置信度预测（pLDDT=77.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR042884, IPR042950; Pfam: PF07707, PF00651, PF07646 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.851 | 0.796 | — |
| KPNA6 | 0.629 | 0.628 | — |
| PRDM6 | 0.621 | 0.000 | — |
| CACUL1 | 0.616 | 0.589 | — |
| NUDCD3 | 0.599 | 0.599 | — |
| KDM1A | 0.533 | 0.512 | — |
| MPG | 0.530 | 0.527 | — |
| ZMYM3 | 0.517 | 0.000 | — |
| KPNA5 | 0.506 | 0.505 | — |
| SNCAIP | 0.466 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MPP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| KPNA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KPNA6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.7 + PDB: 2EQX, 8VOJ, 8VPQ, 8VRT, 9DTG,  | pLDDT=77.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KBTBD4 — Kelch repeat and BTB domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小534 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVX7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123444-KBTBD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KBTBD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVX7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123444-KBTBD4/subcellular

![](https://images.proteinatlas.org/37792/422_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/37792/422_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/37792/423_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/37792/423_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/37792/426_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/37792/426_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVX7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
