---
type: protein-evaluation
gene: "NHSL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NHSL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHSL2 |
| 蛋白名称 | NHS-like protein 2 |
| 蛋白大小 | 1225 aa / 133.3 kDa |
| UniProt ID | Q5HYW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cell Junctions; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1225 aa / 133.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024845; Pfam: PF15273 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Comprehensive analysis of dysregulated circular RNAs and construction of a ceRNA network involved in the pathology of Alzheimer's disease in a 5 × FAD mouse model.. *Frontiers in aging neuroscience*. PMID: 36466608
2. The Nance-Horan syndrome protein encodes a functional WAVE homology domain (WHD) and is important for co-ordinating actin remodelling and maintaining cell morphology.. *Human molecular genetics*. PMID: 20332100
3. Real-world-data for phenotypes and genotypes of rare monogenic genetic epilepsies and genes of uncertain significance for epilepsy.. *Epilepsia open*. PMID: 42220229

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.9 |
| 高置信度残基 (pLDDT>90) 占比 | 5.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 74.8% |
| 有序区域 (pLDDT>70) 占比 | 13.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.9），有序残基占 13.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024845; Pfam: PF15273 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| purT | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cyfip2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| SORBS3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PPP1R13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFCP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAPK9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARID4B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLIC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PIH1D2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.9 + PDB: 无 | pLDDT=47.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cell Junctions; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NHSL2 — NHS-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1225 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5HYW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204131-NHSL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHSL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5HYW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000204131-NHSL2/subcellular

![](https://images.proteinatlas.org/49771/1830_F7_63_blue_red_green.jpg)
![](https://images.proteinatlas.org/49771/1830_F7_64_blue_red_green.jpg)
![](https://images.proteinatlas.org/75115/1830_F8_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/75115/1830_F8_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/75115/1901_H16_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75115/1901_H16_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5HYW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5HYW2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024845; |
| Pfam | PF15273; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204131-NHSL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NCK1 | Intact, Biogrid | true |
| NCK2 | Intact, Biogrid | true |
| NCKAP1 | Biogrid, Opencell | true |
| WASF2 | Biogrid, Opencell | true |
| ABI1 | Biogrid | false |
| ABI2 | Biogrid | false |
| ABI3 | Intact | false |
| ATXN1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
