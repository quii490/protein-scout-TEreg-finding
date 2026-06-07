---
type: protein-evaluation
gene: "GTSF1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GTSF1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GTSF1L |
| 蛋白名称 | GTSF1L (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | GTSF1L |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoli; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Uncertain |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gtsf1l and Gtsf2 Are Specifically Expressed in Gonocytes and Spermatids but Are Not Essential for Spermatogenesis.. *PloS one*. PMID: 26930067
2. The two Gtsf paralogs in silkworms orthogonally activate their partner PIWI proteins for target cleavage.. *RNA (New York, N.Y.)*. PMID: 36319089
3. Comparative gene expression profiling of fertility related transcripts in bull sperm of different genetic backgrounds.. *Tropical animal health and production*. PMID: 39951048
4. Development of a Novel Immune Infiltration-Based Gene Signature to Predict Prognosis and Immunotherapy Response of Patients With Cervical Cancer.. *Frontiers in immunology*. PMID: 34539641
5. An extended Tudor domain within Vreteno interconnects Gtsf1L and Ago3 for piRNA biogenesis in Bombyx mori.. *The EMBO journal*. PMID: 37984437

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
| TMEM225 | 0.649 | 0.000 | — |
| TMEM270 | 0.573 | 0.000 | — |
| FAM71F1 | 0.512 | 0.000 | — |
| C5orf58 | 0.503 | 0.000 | — |
| HEATR9 | 0.498 | 0.000 | — |
| FAM151B | 0.490 | 0.000 | — |
| SPATS1 | 0.482 | 0.000 | — |
| FAM25C | 0.480 | 0.000 | — |
| FSCN3 | 0.479 | 0.000 | — |
| HSF5 | 0.476 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HELLS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GSC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VPS26B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRUNE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| THUMPD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WDR54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. GTSF1L — GTSF1L (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/GTSF1L
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124196-GTSF1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GTSF1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/GTSF1L
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000124196-GTSF1L/subcellular

![](https://images.proteinatlas.org/54694/1779_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/54694/1779_B3_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H1H1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022776;IPR051591;IPR036236; |
| Pfam | PF05253; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124196-GTSF1L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSC2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
