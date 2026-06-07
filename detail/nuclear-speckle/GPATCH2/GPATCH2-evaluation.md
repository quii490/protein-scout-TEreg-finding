---
type: protein-evaluation
gene: "GPATCH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPATCH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPATCH2 / GPATC2 |
| 蛋白名称 | G patch domain-containing protein 2 |
| 蛋白大小 | 528 aa / 58.9 kDa |
| UniProt ID | Q9NW75 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus speckle; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 528 aa / 58.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000467, IPR051189; Pfam: PF01585 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus speckle; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPATC2 |

**关键文献**:
1. Deletion of Gpatch2 does not alter Tnf expression in mice.. *Cell death & disease*. PMID: 36973252
2. Genetic analysis of intracapillary glomerular lipoprotein deposits in aging mice.. *PloS one*. PMID: 25353171
3. Involvement of G-patch domain containing 2 overexpression in breast carcinogenesis.. *Cancer science*. PMID: 19432882
4. G-Patch Domain-Containing Protein 2, Transcriptionally Activated by YY1, Facilitates the Progression of Hepatocellular Carcinoma by Boosting SNAI2 Expression.. *IUBMB life*. PMID: 41236130

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 29.9% |
| 低置信 (pLDDT<50) 占比 | 50.8% |
| 有序区域 (pLDDT>70) 占比 | 19.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 19.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000467, IPR051189; Pfam: PF01585 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX15 | 0.991 | 0.840 | — |
| BYSL | 0.886 | 0.840 | — |
| NOL6 | 0.880 | 0.840 | — |
| DDX10 | 0.877 | 0.840 | — |
| UTP6 | 0.866 | 0.840 | — |
| PINX1 | 0.854 | 0.840 | — |
| UTP25 | 0.851 | 0.840 | — |
| KRR1 | 0.847 | 0.840 | — |
| NOM1 | 0.845 | 0.840 | — |
| UTP3 | 0.842 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CSNK2A2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| SMC3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGEB4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSNAX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CSNK2A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DPY30 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| FGF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 无 | pLDDT=55.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus speckle; Nucleus, nucleolus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPATCH2 — G patch domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小528 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NW75
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092978-GPATCH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPATCH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NW75
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000092978-GPATCH2/subcellular

![](https://images.proteinatlas.org/27181/212_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/27181/212_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/27181/213_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/27181/213_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/27181/214_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/27181/214_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NW75-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NW75 |
| SMART | SM00443; |
| UniProt Domain [FT] | DOMAIN 467..513; /note="G-patch"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00092" |
| InterPro | IPR000467;IPR051189; |
| Pfam | PF01585; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000092978-GPATCH2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| CSNK2B | Biogrid, Opencell | true |
| COMMD4 | Opencell | false |
| COPA | Opencell | false |
| COPE | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
