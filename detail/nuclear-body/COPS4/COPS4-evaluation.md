---
type: protein-evaluation
gene: "COPS4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COPS4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPS4 |
| 蛋白名称 | COP9 signalosome complex subunit 4 |
| 蛋白大小 | 438 aa / 49.7 kDa |
| UniProt ID | D6RFN0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear speckles; UniProt: Cytoplasmic vesicle, secretory vesicle, synaptic vesicle; Nu |
| 蛋白大小 | 10/10 | x1 | 10 | 438 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=88.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Cytoplasmic vesicle, secretory vesicle, synaptic vesicle; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 13 |
| 别名(未计入scoring) |  |

**关键文献**:
1. COPS4 is a novel prognostic biomarker and potential therapeutic target involved in regulation of immune microenvironment in numerous cancers.. *Comput Biol Med*. PMID: 40424765
2. Ensemble Learning for Higher Diagnostic Precision in Schizophrenia Using Peripheral Blood Gene Expression Profile.. *Neuropsychiatr Dis Treat*. PMID: 38716091
3. Identification of crucial lncRNAs and mRNAs in liver regeneration after portal vein ligation through weighted gene correlation network analysis.. *BMC Genomics*. PMID: 36131263
4. mRNA Capture Sequencing and RT-qPCR for the Detection of Pathognomonic, Novel, and Secondary Fusion Transcripts in FFPE Tissue: A Sarcoma Showcase.. *Int J Mol Sci*. PMID: 36232302
5. Shared Blood Transcriptomic Signatures between Alzheimer's Disease and Diabetes Mellitus.. *Biomedicines*. PMID: 33406707

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 78.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 90.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.9，有序区 90.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COPS8 | 0.000 | 0.000 | — |
| COPS5 | 0.000 | 0.000 | — |
| COPS7B | 0.000 | 0.000 | — |
| GPS1 | 0.000 | 0.000 | — |
| COPS2 | 0.000 | 0.000 | — |
| COPS7A | 0.000 | 0.000 | — |
| COPS6 | 0.000 | 0.000 | — |
| COPS3 | 0.000 | 0.000 | — |
| RBX1 | 0.000 | 0.000 | — |
| NEDD8 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O88544 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NS73 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8N6Y0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BT78 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q0VDD7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P01100 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 无 | pLDDT=88.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, synaptic v / Nuclear speckles | 一致 |
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
1. COPS4 -- COP9 signalosome complex subunit 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小438 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/D6RFN0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138663-COPS4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPS4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/D6RFN0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-D6RFN0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BT78 |
| SMART | SM00088; |
| UniProt Domain [FT] | DOMAIN 197..366; /note="PCI"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01185" |
| InterPro | IPR041406;IPR000717;IPR054559;IPR040134;IPR036388;IPR036390; |
| Pfam | PF18420;PF01399;PF22241; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138663-COPS4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRME1 | Intact, Biogrid | true |
| BTBD1 | Biogrid, Bioplex | true |
| COPS2 | Intact, Biogrid | true |
| COPS3 | Biogrid, Bioplex | true |
| COPS5 | Intact, Biogrid, Bioplex | true |
| COPS6 | Intact, Biogrid, Bioplex | true |
| COPS7B | Intact, Biogrid, Bioplex | true |
| COPS8 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
