---
type: protein-evaluation
gene: "LRRC40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC40 |
| 蛋白名称 | Leucine-rich repeat-containing protein 40 |
| 蛋白大小 | 602 aa / 68.2 kDa |
| UniProt ID | Q9H9A6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 602 aa / 68.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050333; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Injury-induced immune responses in Hydra.. *Seminars in immunology*. PMID: 25086685
2. PLXNA2 and LRRC40 as candidate genes in autism spectrum disorder.. *Autism research : official journal of the International Society for Autism Research*. PMID: 33749153
3. A protein interaction network centered on leucine-rich repeats and immunoglobulin-like domains 1 (LRIG1) regulates growth factor receptors.. *The Journal of biological chemistry*. PMID: 29317492
4. Identification of a 12-Gene Signature and Hub Genes Involved in Kidney Wilms Tumor via Integrated Bioinformatics Analysis.. *Frontiers in oncology*. PMID: 35480093

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 45.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.9，有序区 87.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050333; Pfam: PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNPY3 | 0.818 | 0.734 | — |
| KCTD3 | 0.741 | 0.729 | — |
| MRI1 | 0.682 | 0.680 | — |
| LUM | 0.630 | 0.305 | — |
| GML | 0.609 | 0.000 | — |
| SMIM12 | 0.600 | 0.094 | — |
| TUBB8 | 0.558 | 0.099 | — |
| MYL4 | 0.521 | 0.104 | — |
| ISLR | 0.515 | 0.473 | — |
| ADGRL1 | 0.514 | 0.514 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 无 | pLDDT=82.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRC40 — Leucine-rich repeat-containing protein 40，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小602 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9A6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066557-LRRC40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9A6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000066557-LRRC40/subcellular

![](https://images.proteinatlas.org/26564/604_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26564/604_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/26564/607_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26564/607_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/26564/609_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26564/609_G1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9A6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9A6 |
| SMART | SM00364;SM00365;SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR003591;IPR032675;IPR050333; |
| Pfam | PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000066557-LRRC40/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSPA8 | Biogrid, Opencell | true |
| DNAL1 | Intact | false |
| FKBP5 | Biogrid | false |
| MEPCE | Biogrid | false |
| PGK2 | Intact | false |
| PRKN | Biogrid | false |
| SUGT1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
