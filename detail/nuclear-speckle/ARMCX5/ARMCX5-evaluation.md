---
type: protein-evaluation
gene: "ARMCX5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARMCX5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARMCX5 / 无 |
| 蛋白名称 | Armadillo repeat-containing X-linked protein 5 |
| 蛋白大小 | 558 aa / 62.3 kDa |
| UniProt ID | Q6P1M9 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:33:23 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear speckles, Cytosol |
| 蛋白大小 | 10/10 | x1 | 10 | 558 aa / 62.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (<=20->10) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=54.1 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR011989, IPR006911... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **136.0/180** | |
| **归一化总分 (/1.83)** | | | **74.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles, Plasma membrane, Cytosol | Approved |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |

**关键文献**:
1. The Role of EZH2 Inhibitor, GSK-126, in Seizure Susceptibility.. *Journal of molecular neuroscience : MN*. PMID: 32772228
2. GPRASP/ARMCX Protein Family: Potential Involvement in Health and Diseases Revealed by their Novel Interacting Partners.. *Current topics in medicinal chemistry*. PMID: 33267763
3. Unveiling Novel Genetic Mutations and Prognostic Indicators in Breast Carcinoma: An Analysis of The Cancer Genome Atlas (TCGA) Data.. *Cureus*. PMID: 41503337
4. Identification of Immune Cells and Key Genes associated with Alzheimer's Disease.. *International journal of medical sciences*. PMID: 34975305

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 56.5% |
| 有序区域 (pLDDT>70) 占比 | 28.7% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=54.1），大部分区域无序。三维结构评分 3/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR006911, IPR016024; Pfam: PF04826 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC175 | 0.406 | 0.079 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CANX | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| M | anti tag coimmunoprecipitation | imex:IM-27674|pubmed:33208464 |
| GTF2IRD1 | two hybrid | pubmed:26275350|imex:IM-25509 |
| ALOX5 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| APPBP2 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| MAPK6 | anti tag coimmunoprecipitation | pubmed:26972000|imex:IM-22750 |
| RIPK4 | anti tag coimmunoprecipitation | pubmed:26972000|imex:IM-22750 |
| TNFRSF1B | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| INF2 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| FTL | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15

**评价**: 互作网络中等：STRING 12 预测 + IntAct 15 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=54.1 | 单一来源 |
| 定位 | HPA | Nuclear speckles | 单一来源 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 74.3/100

**核心优势**:
1. ARMCX5 -- Armadillo repeat-containing X-linked protein 5，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold pLDDT 较低（54.1），存在显著无序区
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q6P1M9
- Protein Atlas: https://www.proteinatlas.org/search/ARMCX5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARMCX5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1M9
- STRING: https://string-db.org/network/9606.ARMCX5
- Packet data timestamp: 2026-06-03 02:33:23

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000125962-ARMCX5/subcellular

![](https://images.proteinatlas.org/996/53_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/996/53_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/996/54_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/996/54_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/996/55_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/996/55_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1M9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
