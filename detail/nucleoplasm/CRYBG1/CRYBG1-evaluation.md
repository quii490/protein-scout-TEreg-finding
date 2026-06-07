---
type: protein-evaluation
gene: "CRYBG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRYBG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYBG1 / AIM1 |
| 蛋白名称 | Beta/gamma crystallin domain-containing protein 1 |
| 蛋白大小 | 2131 aa / 231.7 kDa |
| UniProt ID | Q9Y4K1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Microtubules, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 2/10 | x1 | 2 | 2131 aa / 231.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=48.9; PDB: 2DAD, 3CW3, 6VRO |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR050252, IPR001064, IPR011024, IPR035992, IPR000 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Microtubules, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AIM1 |

**关键文献**:
1. DHHC5 regulates lacteal function and intestinal lipid absorption by maintaining VEGFR2 localization in lipid rafts.. *Life metabolism*. PMID: 40589731
2. Multiomics profiles of genome-wide alterations in H3K27ac in different lung lobes after acute graft-versus-host disease with MSCs treatment.. *Frontiers in immunology*. PMID: 40443676
3. Establishment of ganglioside GD2-expressing extranodal NK/T-cell lymphoma cell line with scRNA-seq analysis.. *Experimental hematology*. PMID: 38029851
4. Deciphering hub genes and immune landscapes related to neutrophil extracellular traps in rheumatoid arthritis: insights from integrated bioinformatics analyses and experiments.. *Frontiers in immunology*. PMID: 39845946
5. Molecular Characterization and Subtyping of Breast Cancer Cell Lines Provide Novel Insights into Cancer Relevant Genes.. *Cells*. PMID: 38391914

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.9 |
| 高置信度残基 (pLDDT>90) 占比 | 18.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 67.9% |
| 有序区域 (pLDDT>70) 占比 | 29.9% |
| 可用 PDB 条目 | 2DAD, 3CW3, 6VRO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.9），有序残基占 29.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050252, IPR001064, IPR011024, IPR035992, IPR000772; Pfam: PF00030, PF00652 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP2R5C | 0.798 | 0.797 | — |
| MMP11 | 0.768 | 0.050 | — |
| SIRT2 | 0.630 | 0.000 | — |
| PPP2R5D | 0.602 | 0.602 | — |
| NEFM | 0.596 | 0.596 | — |
| SIRT1 | 0.496 | 0.000 | — |
| KRT18 | 0.480 | 0.480 | — |
| ZNF829 | 0.473 | 0.473 | — |
| VIM | 0.455 | 0.455 | — |
| PPP2R5B | 0.450 | 0.450 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.9 + PDB: 2DAD, 3CW3, 6VRO | pLDDT=48.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Microtubules, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CRYBG1 -- Beta/gamma crystallin domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2131 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4K1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112297-CRYBG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYBG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4K1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4K1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y4K1 |
| SMART | SM00458;SM00247; |
| UniProt Domain [FT] | DOMAIN 1430..1469; /note="Beta/gamma crystallin 'Greek key' 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1470..1525; /note="Beta/gamma crystallin 'Greek key' 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1531..1571; /note="Beta/gamma crystallin 'Greek key' 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1572..1614; /note="Beta/gamma crystallin 'Greek key' 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1626..1678; /note="Beta/gamma crystallin 'Greek key' 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1679..1721; /note="Beta/gamma crystallin 'Greek key' 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1727..1769; /note="Beta/gamma crystallin 'Greek key' 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1770..1812; /note="Beta/gamma crystallin 'Greek key' 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1823..1860; /note="Beta/gamma crystallin 'Greek key' 9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1861..1904; /note="Beta/gamma crystallin 'Greek key' 10"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1910..1950; /note="Beta/gamma crystallin 'Greek key' 11"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1951..1992; /note="Beta/gamma crystallin 'Greek key' 12"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1994..2127; /note="Ricin B-type lectin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00174" |
| InterPro | IPR050252;IPR001064;IPR011024;IPR035992;IPR000772; |
| Pfam | PF00030;PF00652; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112297-CRYBG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NEFM | Biogrid | false |
| STK4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
