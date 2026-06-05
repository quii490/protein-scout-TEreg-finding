---
type: protein-evaluation
gene: "SYCE3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYCE3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYCE3 / C22orf41, THEG2 |
| 蛋白名称 | Synaptonemal complex central element protein 3 |
| 蛋白大小 | 88 aa / 10.6 kDa |
| UniProt ID | A1L190 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Golgi apparatus; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 88 aa / 10.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.6; PDB: 6H86 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028145; Pfam: PF15191 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Golgi apparatus | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- central element (GO:0000801)
- chromosome (GO:0005694)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf41, THEG2 |

**关键文献**:
1. HSF5 Deficiency Causes Male Infertility Involving Spermatogenic Arrest at Meiotic Prophase I in Humans and Mice.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38958533
2. Structural maturation of SYCP1-mediated meiotic chromosome synapsis by SYCE3.. *Nature structural & molecular biology*. PMID: 36635604
3. Molecular structure of human synaptonemal complex protein SYCE1.. *Chromosoma*. PMID: 30607510
4. A molecular model for self-assembly of the synaptonemal complex protein SYCE3.. *The Journal of biological chemistry*. PMID: 31023827
5. Structural insight into the central element assembly of the synaptonemal complex.. *Scientific reports*. PMID: 25394919

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.6 |
| 高置信度残基 (pLDDT>90) 占比 | 85.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 6H86 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.6，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028145; Pfam: PF15191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCE2 | 0.996 | 0.095 | — |
| SYCE1 | 0.994 | 0.095 | — |
| TEX12 | 0.993 | 0.000 | — |
| SYCP1 | 0.967 | 0.000 | — |
| SYCP3 | 0.948 | 0.000 | — |
| SYCP2 | 0.893 | 0.000 | — |
| C14orf39 | 0.822 | 0.000 | — |
| STAG3 | 0.804 | 0.000 | — |
| SMC1B | 0.773 | 0.000 | — |
| REC8 | 0.758 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HAUS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRT79 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGF29 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAUS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZWINT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HBZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.6 + PDB: 6H86 | pLDDT=93.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Nucleoli, Golgi apparatus | 一致 |
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
1. SYCE3 — Synaptonemal complex central element protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小88 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1L190
- Protein Atlas: https://www.proteinatlas.org/ENSG00000217442-SYCE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYCE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1L190
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000217442-SYCE3/subcellular

![](https://images.proteinatlas.org/47813/1353_F5_5_red_green.jpg)
![](https://images.proteinatlas.org/47813/1353_F5_6_red_green.jpg)
![](https://images.proteinatlas.org/47813/1363_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/47813/1363_F5_3_red_green.jpg)
![](https://images.proteinatlas.org/47813/1381_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/47813/1381_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A1L190-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
