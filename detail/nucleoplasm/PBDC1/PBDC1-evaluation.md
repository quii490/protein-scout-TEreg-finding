---
type: protein-evaluation
gene: "PBDC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PBDC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PBDC1 / CXorf26 |
| 蛋白名称 | Protein PBDC1 |
| 蛋白大小 | 233 aa / 26.1 kDa |
| UniProt ID | Q9BVG4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 233 aa / 26.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023139, IPR008476, IPR021148; Pfam: PF04669 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf26 |

**关键文献**:
1. ZDHHC15 as a candidate gene for autism spectrum disorder.. *American journal of medical genetics. Part A*. PMID: 36565021
2. Functional study on candidate regulators mediating the expression of CYP6B7 induced by fenvalerate in a susceptible strain of Helicoverpa armigera.. *Pesticide biochemistry and physiology*. PMID: 38879320

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 51.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 18.9% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 58.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.0，有序区 58.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023139, IPR008476, IPR021148; Pfam: PF04669 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTLL12 | 0.832 | 0.831 | — |
| EEF1A1 | 0.823 | 0.821 | — |
| EEF1A2 | 0.633 | 0.631 | — |
| SBNO1 | 0.618 | 0.220 | — |
| ZDHHC24 | 0.570 | 0.000 | — |
| PDCD5 | 0.544 | 0.000 | — |
| LRRC42 | 0.506 | 0.000 | — |
| MYSM1 | 0.492 | 0.091 | — |
| TIMM17B | 0.486 | 0.000 | — |
| SHROOM4 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STRN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1R16A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BABAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CTNNB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| PHB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SMAD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| EEF1A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EEF1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTLL12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 无 | pLDDT=75.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PBDC1 — Protein PBDC1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小233 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVG4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102390-PBDC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PBDC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVG4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000102390-PBDC1/subcellular

![](https://images.proteinatlas.org/3155/56_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/3155/56_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/3155/57_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/3155/57_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/3155/58_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/3155/58_A5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BVG4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BVG4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023139;IPR008476;IPR021148; |
| Pfam | PF04669; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102390-PBDC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EEF1A1 | Bioplex | false |
| EEF1A2 | Bioplex | false |
| POTEF | Bioplex | false |
| TTLL12 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
