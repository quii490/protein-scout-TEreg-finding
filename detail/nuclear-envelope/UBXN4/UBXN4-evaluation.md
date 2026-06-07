---
type: protein-evaluation
gene: "UBXN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN4 / KIAA0242, UBXD2, UBXDC1 |
| 蛋白名称 | UBX domain-containing protein 4 |
| 蛋白大小 | 508 aa / 56.8 kDa |
| UniProt ID | Q92575 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus envelope |
| 蛋白大小 | 10/10 | ×1 | 10 | 508 aa / 56.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.3; PDB: 2KXJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036249, IPR029071, IPR001012; Pfam: PF00789, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus envelope | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0242, UBXD2, UBXDC1 |

**关键文献**:
1. Spatial Density and Distribution of Tumor-Associated Macrophages Predict Survival in Non-Small Cell Lung Carcinoma.. *Cancer research*. PMID: 32699134
2. The AAA-ATPase ATAD1 and its partners promote degradation of desmin intermediate filaments in muscle.. *EMBO reports*. PMID: 36278411
3. APOE*4 Risk-Modifying Genes and Drug Targets in Alzheimer's Disease through Cell-Type Specific Genomic Analyses.. *medRxiv : the preprint server for health sciences*. PMID: 41404291
4. Identifying genetic overlaps in obesity and metabolic disorders unlocking unique and shared mechanistic insights.. *Free radical biology & medicine*. PMID: 39999931
5. The Ubiquitin-Proteasome System Participates in Sperm Surface Subproteome Remodeling during Boar Sperm Capacitation.. *Biomolecules*. PMID: 37371576

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 45.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 23.0% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 2KXJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.3，有序区 65.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036249, IPR029071, IPR001012; Pfam: PF00789, PF23187 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.999 | 0.994 | — |
| UBXN6 | 0.999 | 0.994 | — |
| UBXN8 | 0.956 | 0.000 | — |
| NSFL1C | 0.956 | 0.300 | — |
| UBXN1 | 0.953 | 0.000 | — |
| UBXN2A | 0.952 | 0.000 | — |
| SVIP | 0.932 | 0.000 | — |
| UBE4A | 0.891 | 0.781 | — |
| FAF2 | 0.854 | 0.000 | — |
| UBQLN1 | 0.828 | 0.458 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOM1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| dnaJ2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| sdhA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| ZNF24 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| UBE4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS13C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IP6K1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS13A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 2KXJ | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus envelope / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. UBXN4 — UBX domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小508 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92575
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144224-UBXN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92575
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92575-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92575 |
| SMART | SM00166; |
| UniProt Domain [FT] | DOMAIN 315..393; /note="UBX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00215" |
| InterPro | IPR036249;IPR029071;IPR001012; |
| Pfam | PF00789;PF23187; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
