---
type: protein-evaluation
gene: "CNOT10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNOT10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNOT10 |
| 蛋白名称 | CCR4-NOT transcription complex subunit 10 |
| 蛋白大小 | 744 aa / 82.3 kDa |
| UniProt ID | Q9H9A5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Centrosome; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 744 aa / 82.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 18 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A natural product-hybridization approach toward anticancer drug discovery: synthesis and antitumor evaluation of CTBC6, designed from sulforaphane and magnolol.. *Bioorg Chem*. PMID: 41774989
2. CNOT10 is involved in TTP-mediated AU-rich element containing mRNA metabolism, independent of mRNA decay regulation.. *RNA*. PMID: 42049461
3. CNOT10 is involved in TTP-mediated AU-rich element containing mRNA metabolism, independent of mRNA decay regulation.. *bioRxiv*. PMID: 41542502
4. The CCR4-NOT deadenylase complex mediates tubulin autoregulation via specific adapters CNOT10 and CNOT11.. *MicroPubl Biol*. PMID: 41426964
5. GGNBP2 regulates MDA5 sensing triggered by self double-stranded RNA following loss of ADAR1 editing.. *Sci Immunol*. PMID: 39576872

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 59.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 73.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.2，有序区 73.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT9 | 0.000 | 0.000 | — |
| CNOT7 | 0.000 | 0.000 | — |
| CNOT2 | 0.000 | 0.000 | — |
| CNOT3 | 0.000 | 0.000 | — |
| CNOT6 | 0.000 | 0.000 | — |
| CNOT1 | 0.000 | 0.000 | — |
| CNOT11 | 0.000 | 0.000 | — |
| CNOT6L | 0.000 | 0.000 | — |
| CNOT8 | 0.000 | 0.000 | — |
| TNKS1BP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9UFF9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9H9A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:A0A5P8YLY5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BR39 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q9H9A5-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8BH15 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 无 | pLDDT=79.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Centrosome; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CNOT10 -- CCR4-NOT transcription complex subunit 10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小744 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9A5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182973-CNOT10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNOT10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9A5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9A5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9A5 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039740;IPR011990;IPR019734; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182973-CNOT10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CNOT2 | Intact, Biogrid | true |
| CNOT6 | Intact, Biogrid | true |
| CNOT6L | Intact, Biogrid | true |
| CNOT8 | Intact, Biogrid | true |
| TNRC6C | Intact, Biogrid | true |
| CAPZB | Biogrid | false |
| CNOT1 | Biogrid | false |
| CNOT11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
