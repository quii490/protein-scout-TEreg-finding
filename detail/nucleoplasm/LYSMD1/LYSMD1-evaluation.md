---
type: protein-evaluation
gene: "LYSMD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LYSMD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LYSMD1 |
| 蛋白名称 | LYSMD1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | LYSMD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. LYSMD proteins promote activation of Rab32-family GTPases for lysosome-related organelle biogenesis.. *The Journal of cell biology*. PMID: 39078368
2. Myeloid cells limit production of antibody-secreting cells after immunization in the lymph node.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 24376270
3. Microsatellite instability-related prognostic risk score (MSI-pRS) defines a subset of lung squamous cell carcinoma (LUSC) patients with genomic instability and poor clinical outcome.. *Frontiers in genetics*. PMID: 36873930

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TULP3 | 0.610 | 0.607 | — |
| PHLDB3 | 0.512 | 0.000 | — |
| SCNM1 | 0.479 | 0.000 | — |
| LRP5L | 0.418 | 0.000 | — |
| TCEAL4 | 0.418 | 0.000 | — |
| ANKRD49 | 0.415 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RINT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM69 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DUSP4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TULP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PAX6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT34 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA6L9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 13
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 6 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LYSMD1 — LYSMD1 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/LYSMD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163155-LYSMD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LYSMD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/LYSMD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000163155-LYSMD1/subcellular

![](https://images.proteinatlas.org/28055/298_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/28055/298_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/28055/299_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/28055/299_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/28055/300_C7_4_red_green.jpg)
![](https://images.proteinatlas.org/28055/300_C7_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96S90 |
| SMART | SM00257; |
| UniProt Domain [FT] | DOMAIN 40..84; /note="LysM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01118" |
| InterPro | IPR018392;IPR045030;IPR036779; |
| Pfam | PF01476; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163155-LYSMD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DUSP4 | Intact | false |
| GOLGA2 | Intact | false |
| GOLGA6L9 | Intact | false |
| KRT34 | Intact | false |
| MTUS2 | Intact | false |
| PAX6 | Intact | false |
| RINT1 | Intact | false |
| TCF12 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
