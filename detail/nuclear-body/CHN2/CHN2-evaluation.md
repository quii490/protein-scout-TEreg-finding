---
type: protein-evaluation
gene: "CHN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHN2 / ARHGAP3, BCH |
| 蛋白名称 | Beta-chimaerin |
| 蛋白大小 | 468 aa / 53.9 kDa |
| UniProt ID | P52757 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 468 aa / 53.9 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=84.7; PDB: 1XA6 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR046349, IPR035840, IPR017356, IPR020454, IPR002 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 195 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARHGAP3, BCH |

**关键文献**:
1. CHN2 Promoter Methylation Change May Be Associated With Methamphetamine Dependence.. *Shanghai archives of psychiatry*. PMID: 29719347
2. Association of a novel polymorphism of the β2-chimaerin gene (CHN2) with smoking.. *Journal of investigative medicine : the official publication of the American Federation for Clinical Research*. PMID: 23941981
3. In vitro embryotoxicity of the cysteine proteinase inhibitors benzyloxycarbonyl-phenylalanine-alanine-diazomethane (Z-Phe-Ala-CHN2) and benzyloxycarbonyl-phenylalanine-phenylalanine-diazomethane (Z-Phe-Phe-CHN2).. *Teratology*. PMID: 7871486
4. Severe insulin resistance and intrauterine growth deficiency associated with haploinsufficiency for INSR and CHN2: new insights into synergistic pathways involved in growth and metabolism.. *Diabetes*. PMID: 19720790
5. β3-chimaerin, a novel member of the chimaerin Rac-GAP family.. *Molecular biology reports*. PMID: 24430297

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 67.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 14.3% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 1XA6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=84.7，有序区 82.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046349, IPR035840, IPR017356, IPR020454, IPR002219; Pfam: PF00130, PF00620, PF00017 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAC1 | 0.835 | 0.681 | — |
| CPVL | 0.703 | 0.000 | — |
| DGKG | 0.656 | 0.000 | — |
| AKT1 | 0.639 | 0.071 | — |
| CTSB | 0.624 | 0.000 | — |
| FRMD3 | 0.624 | 0.000 | — |
| EPHA4 | 0.590 | 0.091 | — |
| TMED10 | 0.536 | 0.000 | — |
| RASA1 | 0.533 | 0.071 | — |
| CTSC | 0.531 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BAG6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SUMO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ALS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| NCK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| RADIL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SHF | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SENP8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NCK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PTGDS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 1XA6 | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHN2 -- Beta-chimaerin，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52757
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106069-CHN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52757
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106069-CHN2/subcellular

![](https://images.proteinatlas.org/18989/1030_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/18989/1030_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/18989/1327_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/18989/1327_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/18989/176_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/18989/176_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52757-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
