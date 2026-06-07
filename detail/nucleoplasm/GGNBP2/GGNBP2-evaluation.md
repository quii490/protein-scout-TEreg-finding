---
type: protein-evaluation
gene: "GGNBP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GGNBP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GGNBP2 / LCRG1, LZK1, ZNF403 |
| 蛋白名称 | Gametogenetin-binding protein 2 |
| 蛋白大小 | 697 aa / 79.1 kDa |
| UniProt ID | Q9H3C7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Endoplasmic reticulum; UniProt: Cytoplasmic vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 697 aa / 79.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 8BFJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026073 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 37.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 36.7% |
| 有序区域 (pLDDT>70) 占比 | 55.8% |
| 可用 PDB 条目 | 8BFJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 55.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026073 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT11 | 0.920 | 0.919 | — |
| PIGW | 0.796 | 0.000 | — |
| OAZ3 | 0.778 | 0.000 | — |
| DHRS11 | 0.715 | 0.091 | — |
| SDHB | 0.674 | 0.145 | — |
| ZNHIT3 | 0.669 | 0.000 | — |
| GGN | 0.667 | 0.095 | — |
| MRM1 | 0.647 | 0.000 | — |
| MYO19 | 0.643 | 0.000 | — |
| ETFB | 0.634 | 0.412 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CNOT11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF331 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PAK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DTX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 8BFJ | pLDDT=68.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GGNBP2 — Gametogenetin-binding protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小697 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3C7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000278311-GGNBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GGNBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3C7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000278311-GGNBP2/subcellular

![](https://images.proteinatlas.org/73392/1541_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73392/1541_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73392/1542_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73392/1542_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73392/1638_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73392/1638_H3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3C7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H3C7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026073; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000278311-GGNBP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTRC | Biogrid | false |
| FBXW11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
