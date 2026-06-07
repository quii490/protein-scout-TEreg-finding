---
type: protein-evaluation
gene: "MYRIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYRIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYRIP / SLAC2C |
| 蛋白名称 | Rab effector MyRIP |
| 蛋白大小 | 859 aa / 95.7 kDa |
| UniProt ID | Q8NFW9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center, Golgi apparatus; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cytoplasmic vesicl |
| 蛋白大小 | 8/10 | ×1 | 8 | 859 aa / 95.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041282, IPR051745, IPR006788, IPR010911, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center, Golgi apparatus | Approved |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cytoplasmic vesicle, secretory vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cortical actin cytoskeleton (GO:0030864)
- cytosol (GO:0005829)
- dense core granule (GO:0031045)
- exocyst (GO:0000145)
- melanosome (GO:0042470)
- perinuclear region of cytoplasm (GO:0048471)
- photoreceptor outer segment (GO:0001750)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SLAC2C |

**关键文献**:
1. MyRIP anchors protein kinase A to the exocyst complex.. *The Journal of biological chemistry*. PMID: 17827149
2. Rab27a and MyRIP regulate the amount and multimeric state of VWF released from endothelial cells.. *Blood*. PMID: 19270261
3. Involvement of the Rab27 binding protein Slac2c/MyRIP in insulin exocytosis.. *Molecular biology of the cell*. PMID: 14517322
4. Cargo binding activates myosin VIIA motor function in cells.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 21482763
5. MyRIP, a novel Rab effector, enables myosin VIIa recruitment to retinal melanosomes.. *EMBO reports*. PMID: 11964381

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 52.0% |
| 有序区域 (pLDDT>70) 占比 | 39.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.7），有序残基占 39.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041282, IPR051745, IPR006788, IPR010911, IPR011011; Pfam: PF02318, PF04698 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB27A | 0.999 | 0.479 | — |
| MYO5A | 0.997 | 0.000 | — |
| MYO7A | 0.978 | 0.000 | — |
| RAB27B | 0.968 | 0.287 | — |
| EXOC3 | 0.933 | 0.000 | — |
| EXOC4 | 0.926 | 0.000 | — |
| SYTL1 | 0.903 | 0.000 | — |
| SYTL2 | 0.661 | 0.000 | — |
| PRKACB | 0.607 | 0.000 | — |
| CAV1 | 0.599 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| OIP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C1orf216 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RAB27A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RAB27B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VPS26C | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.7 + PDB: 无 | pLDDT=57.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cytoplas / Nucleoplasm, Nucleoli fibrillar center, Golgi appa | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MYRIP — Rab effector MyRIP，非常新颖，仅有少数基础研究。
2. 蛋白大小859 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFW9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170011-MYRIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYRIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFW9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170011-MYRIP/subcellular

![](https://images.proteinatlas.org/6433/1370_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6433/1370_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6433/1372_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6433/1372_D4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/6433/1421_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6433/1421_B3_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFW9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFW9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 4..124; /note="RabBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00234" |
| InterPro | IPR041282;IPR051745;IPR006788;IPR010911;IPR011011;IPR013083; |
| Pfam | PF02318;PF04698; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170011-MYRIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAB27A | Intact, Biogrid | true |
| C1orf216 | Intact | false |
| OIP5 | Intact | false |
| RAB27B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
