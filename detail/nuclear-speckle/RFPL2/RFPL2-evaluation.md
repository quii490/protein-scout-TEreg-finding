---
type: protein-evaluation
gene: "RFPL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RFPL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RFPL2 / RNF79 |
| 蛋白名称 | Ret finger protein-like 2 |
| 蛋白大小 | 378 aa / 42.1 kDa |
| UniProt ID | O75678 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 378 aa / 42.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF79 |

**关键文献**:
1. Duplications on human chromosome 22 reveal a novel Ret Finger Protein-like gene family with sense and endogenous antisense transcripts.. *Genome research*. PMID: 10508838

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.7% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.4，有序区 67.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF11002, PF00622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFPL3 | 0.742 | 0.465 | — |
| PAX6 | 0.648 | 0.045 | — |
| PRAMEF1 | 0.640 | 0.105 | — |
| PRAMEF13 | 0.569 | 0.105 | — |
| PRAMEF11 | 0.551 | 0.105 | — |
| PRAMEF12 | 0.546 | 0.105 | — |
| PRAMEF2 | 0.546 | 0.105 | — |
| ZSCAN4 | 0.539 | 0.065 | — |
| MBD3L2 | 0.518 | 0.000 | — |
| PRAMEF25 | 0.518 | 0.105 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BACH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHLPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DMWD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AHNAK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DYRK1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR73 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF507 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNG1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MIOS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.4 + PDB: 无 | pLDDT=73.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RFPL2 — Ret finger protein-like 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小378 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75678
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128253-RFPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RFPL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75678
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000128253-RFPL2/subcellular

![](https://images.proteinatlas.org/48320/1711_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/48320/1711_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/48320/1712_B12_14_cr5804a7b6268fd_red_green.jpg)
![](https://images.proteinatlas.org/48320/1712_B12_24_cr5804a7c7dcdc9_red_green.jpg)
![](https://images.proteinatlas.org/48320/1737_C3_13_cr58063ebd153c9_red_green.jpg)
![](https://images.proteinatlas.org/48320/1737_C3_2_cr58063eb3ccd17_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75678-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75678 |
| SMART | SM00589;SM00449; |
| UniProt Domain [FT] | DOMAIN 168..362; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR006574;IPR022723;IPR037960;IPR003877;IPR050143;IPR013083; |
| Pfam | PF13765;PF11002;PF00622;PF15227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128253-RFPL2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
