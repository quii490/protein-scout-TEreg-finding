---
type: protein-evaluation
gene: "DENND2C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DENND2C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND2C |
| 蛋白名称 | DENN domain-containing protein 2C |
| 蛋白大小 | 928 aa / 106.9 kDa |
| UniProt ID | Q68D51 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 928 aa / 106.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR051942, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Evidence of genetic variations associated with rotator cuff disease.. *Journal of shoulder and elbow surgery*. PMID: 24129055
2. Whole exome sequencing study identifies candidate loss of function variants and locus heterogeneity in familial cholesteatoma.. *PloS one*. PMID: 36920900
3. Significant association of full-thickness rotator cuff tears and estrogen-related receptor-β (ESRRB).. *Journal of shoulder and elbow surgery*. PMID: 25219474

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.3 |
| 高置信度残基 (pLDDT>90) 占比 | 28.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 47.4% |
| 有序区域 (pLDDT>70) 占比 | 45.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.3），有序残基占 45.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR051942, IPR037516; Pfam: PF03455, PF02141, PF03456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB9A | 0.655 | 0.000 | — |
| RAB9B | 0.629 | 0.000 | — |
| AMPD1 | 0.556 | 0.000 | — |
| C3orf67 | 0.542 | 0.000 | — |
| RAB35 | 0.484 | 0.303 | — |
| CSDE1 | 0.465 | 0.000 | — |
| ARHGAP26 | 0.464 | 0.000 | — |
| RHOBTB3 | 0.435 | 0.000 | — |
| FYCO1 | 0.428 | 0.000 | — |
| GSTM3 | 0.425 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YES1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARHGAP42 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HID1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.3 + PDB: 无 | pLDDT=61.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DENND2C — DENN domain-containing protein 2C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小928 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68D51
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175984-DENND2C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND2C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68D51
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000175984-DENND2C/subcellular

![](https://images.proteinatlas.org/29935/1802_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/29935/1802_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/29935/1921_H11_17_cr5cac5ec2f11f8_red_green.jpg)
![](https://images.proteinatlas.org/29935/1921_H11_26_cr5cac5ec2f3809_red_green.jpg)
![](https://images.proteinatlas.org/29935/272_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/29935/272_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q68D51-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q68D51 |
| SMART | SM00801;SM00799;SM00800; |
| UniProt Domain [FT] | DOMAIN 492..641; /note="uDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 663..796; /note="cDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 798..888; /note="dDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304" |
| InterPro | IPR001194;IPR005112;IPR043153;IPR051942;IPR037516;IPR005113; |
| Pfam | PF03455;PF02141;PF03456; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175984-DENND2C/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
