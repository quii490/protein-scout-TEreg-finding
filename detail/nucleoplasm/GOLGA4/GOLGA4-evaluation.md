---
type: protein-evaluation
gene: "GOLGA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GOLGA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA4 |
| 蛋白名称 | Golgin subfamily A member 4 |
| 蛋白大小 | 2230 aa / 261.1 kDa |
| UniProt ID | Q13439 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm; Golgi apparatus membrane; Golgi apparatus, trans- |
| 蛋白大小 | 2/10 | ×1 | 2 | 2230 aa / 261.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.6; PDB: 1R4A, 1UPT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000237; Pfam: PF01465 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Golgi apparatus membrane; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- trans-Golgi network (GO:0005802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

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
| AlphaFold 平均 pLDDT | 66.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 59.6% |
| 中等置信 (pLDDT 50-70) 占比 | 24.4% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 59.6% |
| 可用 PDB 条目 | 1R4A, 1UPT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.6），有序残基占 59.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000237; Pfam: PF01465 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL1 | 0.989 | 0.971 | — |
| GCC1 | 0.958 | 0.000 | — |
| GCC2 | 0.939 | 0.000 | — |
| MACF1 | 0.936 | 0.062 | — |
| GOLGA1 | 0.921 | 0.097 | — |
| GOLGB1 | 0.913 | 0.134 | — |
| ANKRD27 | 0.871 | 0.320 | — |
| TGOLN2 | 0.852 | 0.161 | — |
| GRIP1 | 0.825 | 0.066 | — |
| VTI1A | 0.821 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Arl1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:14718928 |
| NDN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EXOC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| BIRC6 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-11898|pubmed:18329369 |
| TP63 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20085233|imex:IM-20439 |
| ANKRD27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22705394|imex:IM-17311 |
| Wasf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| NECAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.6 + PDB: 1R4A, 1UPT | pLDDT=66.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus membrane; Golgi apparat / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GOLGA4 — Golgin subfamily A member 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2230 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13439
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144674-GOLGA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13439
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000144674-GOLGA4/subcellular

![](https://images.proteinatlas.org/40675/791_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/40675/791_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/40675/798_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/40675/798_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/40675/860_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/40675/860_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13439-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13439 |
| SMART | SM00755; |
| UniProt Domain [FT] | DOMAIN 2168..2215; /note="GRIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00250" |
| InterPro | IPR000237; |
| Pfam | PF01465; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144674-GOLGA4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EXOC1 | Intact, Biogrid | true |
| ANKRD27 | Intact | false |
| ARL1 | Biogrid | false |
| DNAJA1 | Biogrid | false |
| DNAJB1 | Opencell | false |
| HDAC2 | Biogrid | false |
| LIMD1 | Intact | false |
| RAB4A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
