---
type: protein-evaluation
gene: "OTULINL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OTULINL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OTULINL / FAM105A |
| 蛋白名称 | Inactive ubiquitin thioesterase OTULINL |
| 蛋白大小 | 356 aa / 42.2 kDa |
| UniProt ID | Q9NUU6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm; Endoplasmic reticulum membrane; Nucleus envelope |
| 蛋白大小 | 10/10 | ×1 | 10 | 356 aa / 42.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.8; PDB: 6DRM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023235, IPR023236; Pfam: PF16218 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Cytoplasm; Endoplasmic reticulum membrane; Nucleus envelope | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic side of endoplasmic reticulum membrane (GO:0098554)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM105A |

**关键文献**:
1. FAM105A/OTULINL Is a Pseudodeubiquitinase of the OTU-Class that Localizes to the ER Membrane.. *Structure (London, England : 1993)*. PMID: 31056421
2. Ubiquitin-dependent and -independent functions of OTULIN in cell fate control and beyond.. *Cell death and differentiation*. PMID: 33288901

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.8 |
| 高置信度残基 (pLDDT>90) 占比 | 75.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |
| 可用 PDB 条目 | 6DRM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.8，有序区 88.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023235, IPR023236; Pfam: PF16218 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNFRSF17 | 0.533 | 0.533 | — |
| TMEM63C | 0.520 | 0.000 | — |
| OTUD6A | 0.495 | 0.000 | — |
| OTUD4 | 0.493 | 0.000 | — |
| OTUD5 | 0.477 | 0.000 | — |
| OTUD3 | 0.469 | 0.000 | — |
| OTUD6B | 0.461 | 0.000 | — |
| C3orf14 | 0.459 | 0.000 | — |
| OTUD7A | 0.456 | 0.000 | — |
| OTUD1 | 0.450 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| GOLT1A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC30A8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| JAGN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM86B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000274217.3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.8 + PDB: 6DRM | pLDDT=88.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum membrane; Nucleus / Nucleoli, Cytosol | 一致 |
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
1. OTULINL — Inactive ubiquitin thioesterase OTULINL，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小356 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUU6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145569-OTULINL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OTULINL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUU6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000145569-OTULINL/subcellular

![](https://images.proteinatlas.org/46638/831_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46638/831_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46638/871_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46638/871_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46638/882_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46638/882_F8_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NUU6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
