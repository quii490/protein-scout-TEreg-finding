---
type: protein-evaluation
gene: "NIPAL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NIPAL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NIPAL3 / NPAL3 |
| 蛋白名称 | NIPA-like protein 3 |
| 蛋白大小 | 406 aa / 44.7 kDa |
| UniProt ID | Q6P499 |
| 数据采集时间 | 2026-06-03 23:46:27 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 406 aa / 44.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=2 篇 (<= 20 -> 10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=75.1; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR008521; Pfam: PF05653 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 11 interactions |
| 互证加分 | -- | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NPAL3 |

**关键文献**:
1. Construction of a HOXA11-AS-Interact Ed Network in Keloid Fibroblasts Using Integrated Bioinformatic Analysis and in Vitro Validation.. *Frontiers in genetics*. PMID: 35432479
2. Artificial neural network inference analysis identified novel genes and gene interactions associated with skeletal muscle aging.. *Journal of cachexia, sarcopenia and muscle*. PMID: 39210538

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 37.4% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 71.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.1，有序区 71.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008521; Pfam: PF05653 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VPS45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EDA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GJA5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MANBAL | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPX8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATP6V0C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VMA21 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CD79A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 11
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 无 | pLDDT=75.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 11 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NIPAL3 -- NIPA-like protein 3，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P499
- Protein Atlas: https://www.proteinatlas.org/ENSG00000001461-NIPAL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NIPAL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P499
- STRING: https://string-db.org/network/9606.NIPAL3
- Packet data timestamp: 2026-06-03 23:46:27

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000001461-NIPAL3/subcellular

![](https://images.proteinatlas.org/39978/411_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/39978/411_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/39978/415_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/39978/415_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/39978/416_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/39978/416_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P499-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P499 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008521; |
| Pfam | PF05653; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000001461-NIPAL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP6V0C | Intact | false |
| CD79A | Intact | false |
| EDA | Intact, Biogrid | false |
| GJA5 | Intact | false |
| GPX8 | Intact | false |
| MANBAL | Intact | false |
| TMEM14B | Intact | false |
| VMA21 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
