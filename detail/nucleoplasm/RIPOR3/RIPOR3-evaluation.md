---
type: protein-evaluation
gene: "RIPOR3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIPOR3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIPOR3 / C20orf175, C20orf176, FAM65C |
| 蛋白名称 | RIPOR family member 3 |
| 蛋白大小 | 946 aa / 105.3 kDa |
| UniProt ID | Q96MK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 946 aa / 105.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031780, IPR026136; Pfam: PF15903 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf175, C20orf176, FAM65C |

**关键文献**:
1. Hypoxic stabilization of RIPOR3 mRNA via METTL3-mediated m(6)A methylation drives breast cancer progression and metastasis.. *Oncogene*. PMID: 39341989
2. Genome-Wide DNA Methylome and Transcriptome Analysis of Porcine Testicular Cells Infected With Transmissible Gastroenteritis Virus.. *Frontiers in veterinary science*. PMID: 35097042
3. Downregulated Expression of RIPOR3 Correlated with Immune Infiltrates Predicts Poor Prognosis in Oral Tongue Cancer.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 35277469
4. Integrated analysis of lncRNA-miRNA-mRNA ceRNA network in squamous cell carcinoma of tongue.. *BMC cancer*. PMID: 31391008
5. Identification of IPF specific genes expressed by lung tissue-derived fibroblasts using next generation sequencing.. *Sarcoidosis, vasculitis, and diffuse lung diseases : official journal of WASOG*. PMID: 41891414

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 37.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 59.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 59.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031780, IPR026136; Pfam: PF15903 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.806 | 0.789 | — |
| RHOA | 0.503 | 0.414 | — |
| HSD17B13 | 0.461 | 0.000 | — |
| SUSD1 | 0.452 | 0.091 | — |
| LTC4S | 0.419 | 0.000 | — |
| RHOC | 0.417 | 0.322 | — |
| RPS28 | 0.413 | 0.310 | — |
| EFCAB5 | 0.412 | 0.045 | — |
| ERICH6 | 0.406 | 0.045 | — |
| RPS24 | 0.403 | 0.309 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCML4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RHOA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RHOC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SHANK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCDC125 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NHERF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NHERF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SRPK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 10
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 无 | pLDDT=68.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 10 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RIPOR3 — RIPOR family member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小946 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000042062-RIPOR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIPOR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000042062-RIPOR3/subcellular

![](https://images.proteinatlas.org/51823/1353_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/51823/1353_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51823/1363_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/51823/1363_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51823/1848_A1_22_cr5abb7a69ac92a_red_green.jpg)
![](https://images.proteinatlas.org/51823/1848_A1_8_cr5abb7a69ab748_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
