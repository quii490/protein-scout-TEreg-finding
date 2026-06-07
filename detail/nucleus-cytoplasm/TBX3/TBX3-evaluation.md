---
type: protein-evaluation
gene: "TBX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX3 — REJECTED (研究热度过高 (PubMed strict=409，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX3 |
| 蛋白名称 | TBX3 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | TBX3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=409 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分** | | | **33.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
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
| PubMed strict count | 409 |
| PubMed broad count | 718 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Genomic Landscape of Endocrine-Resistant Advanced Breast Cancers.. *Cancer cell*. PMID: 30205045
2. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
3. Single-cell spatial multi-omics and deep learning dissect enhancer-driven gene regulatory networks in liver zonation.. *Nature cell biology*. PMID: 38182825
4. A single-cell atlas of the healthy breast tissues reveals clinically relevant clusters of breast epithelial cells.. *Cell reports. Medicine*. PMID: 33763657
5. Overexpression of TBX3 suppresses tumorigenesis in experimental and human cholangiocarcinoma.. *Cell death & disease*. PMID: 38909034

**评价**: 研究基础较多，新颖性有限。

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
| MAPK3 | 0.933 | 0.211 | — |
| MAPK1 | 0.911 | 0.067 | — |
| SOX2 | 0.907 | 0.308 | — |
| POU5F1 | 0.898 | 0.091 | — |
| NANOG | 0.882 | 0.098 | — |
| KLF4 | 0.878 | 0.054 | — |
| NKX2-5 | 0.873 | 0.075 | — |
| RBM19 | 0.870 | 0.000 | — |
| SALL4 | 0.829 | 0.060 | — |
| ESRRB | 0.827 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOLLIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| PRR20D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CSF3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| PFDN5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UFSP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000257566.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Smad3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBX3 — TBX3 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 409 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 409 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/TBX3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135111-TBX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/TBX3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000135111-TBX3/subcellular

![](https://images.proteinatlas.org/5799/1843_E3_31_red_green.jpg)
![](https://images.proteinatlas.org/5799/1843_E3_32_red_green.jpg)
![](https://images.proteinatlas.org/5799/1864_F6_13_cr5afd9ffd1623a_red_green.jpg)
![](https://images.proteinatlas.org/5799/1864_F6_29_cr5afd9ffd16412_red_green.jpg)
![](https://images.proteinatlas.org/5799/43_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/5799/43_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15119 |
| SMART | SM00425; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008967;IPR046360;IPR036960;IPR022582;IPR048387;IPR001699;IPR018186; |
| Pfam | PF00907;PF20627;PF12598; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135111-TBX3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CA8 | Intact | false |
| PFDN5 | Intact | false |
| PML | Biogrid | false |
| PRR20D | Intact | false |
| TLE5 | Intact | false |
| UFSP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
