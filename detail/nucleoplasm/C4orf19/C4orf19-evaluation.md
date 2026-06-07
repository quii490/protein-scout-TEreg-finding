---
type: protein-evaluation
gene: "C4orf19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C4orf19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C4orf19 / C4orf19 |
| 蛋白名称 | PDCD10 and GCKIII kinases-associated protein 1 |
| 蛋白大小 | 314 aa / 33.7 kDa |
| UniProt ID | Q8IY42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cell Junctions; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 33.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031528; Pfam: PF15770 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell periphery (GO:0071944)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C4orf19 |

**关键文献**:
1. Evolution of chromosome-arm aberrations in breast cancer through genetic network rewiring.. *Cell reports*. PMID: 38517886
2. Clear cell renal cell carcinoma: immunological significance of alternative splicing signatures.. *Frontiers in oncology*. PMID: 38288096
3. Alternative splicing events in tumor immune infiltration in renal clear cell carcinomas.. *Cancer gene therapy*. PMID: 35370291
4. The identification of multifocal breast cancer-associated long non-coding RNAs.. *European review for medical and pharmacological sciences*. PMID: 29271998
5. Molecular complex detection in protein interaction networks through reinforcement learning.. *BMC bioinformatics*. PMID: 37532987

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 43.0% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 12.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.4），有序残基占 12.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031528; Pfam: PF15770 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDCD10 | 0.861 | 0.861 | — |
| STK24 | 0.834 | 0.834 | — |
| STK25 | 0.832 | 0.832 | — |
| STK26 | 0.827 | 0.827 | — |
| EIF3E | 0.623 | 0.623 | — |
| FAM221A | 0.458 | 0.000 | — |
| KIAA0930 | 0.447 | 0.000 | — |
| LRRC66 | 0.436 | 0.000 | — |
| FAM219B | 0.432 | 0.000 | — |
| C3orf52 | 0.429 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PDCD10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EIF3E | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PGCKA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEP19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ABITRAM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 5
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.4 + PDB: 无 | pLDDT=54.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Nucleoplasm; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 12 + 5 interactions | 数据充分 |

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
1. C4orf19 — PDCD10 and GCKIII kinases-associated protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154274-C4orf19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C4orf19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000154274-C4orf19/subcellular

![](https://images.proteinatlas.org/52894/1396_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/52894/1396_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/52894/861_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/52894/861_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/52894/880_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/52894/880_H11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IY42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IY42 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031528; |
| Pfam | PF15770; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154274-C4orf19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PDCD10 | Intact, Biogrid, Bioplex | true |
| ABITRAM | Intact | false |
| CEP19 | Intact | false |
| EIF3E | Intact | false |
| STK25 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
