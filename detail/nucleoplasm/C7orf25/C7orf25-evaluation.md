---
type: protein-evaluation
gene: "C7orf25"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C7orf25 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C7orf25 |
| 蛋白名称 | UPF0415 protein C7orf25 |
| 蛋白大小 | 421 aa / 46.5 kDa |
| UniProt ID | Q9BPX7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 421 aa / 46.5 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010733, IPR041076; Pfam: PF07000, PF18474 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 13 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrated analysis of the prognostic and oncogenic roles of OPN3 in human cancers.. *BMC cancer*. PMID: 35180853
2. Functionathon: a manual data mining workflow to generate functional hypotheses for uncharacterized human proteins and its application by undergraduate students.. *Database : the journal of biological databases and curation*. PMID: 34318869
3. Genome-Wide Association Study and Phenotype Prediction of Reproductive Traits in Large White Pigs.. *Animals : an open access journal from MDPI*. PMID: 39682314

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 78.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 91.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010733, IPR041076; Pfam: PF07000, PF18474 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSMA2 | 0.705 | 0.000 | — |
| CXorf58 | 0.666 | 0.000 | — |
| SMLR1 | 0.580 | 0.000 | — |
| WDR83 | 0.551 | 0.000 | — |
| VOPP1 | 0.499 | 0.000 | — |
| SEC61G | 0.490 | 0.000 | — |
| FAM204A | 0.478 | 0.000 | — |
| BLVRA | 0.437 | 0.000 | — |
| FAM220A | 0.433 | 0.053 | — |
| LANCL2 | 0.422 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FRA10AC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HEXD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBB2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BRD4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FZR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MUC5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GTPBP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000396597.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| TARS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| EBI-10173104 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 13
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 无 | pLDDT=89.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 14 + 13 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C7orf25 — UPF0415 protein C7orf25，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPX7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136197-C7orf25/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C7orf25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPX7
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:26:38

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000136197-C7orf25/subcellular

![](https://images.proteinatlas.org/20120/177_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/20120/177_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/20120/178_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/20120/178_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/20120/247_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/20120/247_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BPX7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BPX7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010733;IPR041076; |
| Pfam | PF07000;PF18474; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136197-C7orf25/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GTPBP1 | Intact | false |
| RANBP2 | Intact | false |
| TARS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
