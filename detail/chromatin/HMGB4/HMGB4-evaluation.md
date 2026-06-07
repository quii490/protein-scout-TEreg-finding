---
type: protein-evaluation
gene: "HMGB4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMGB4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMGB4 |
| 蛋白名称 | High mobility group protein B4 |
| 蛋白大小 | 186 aa / 22.5 kDa |
| UniProt ID | Q8WW32 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 186 aa / 22.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009071, IPR036910, IPR050342; Pfam: PF00505, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Age-Associated Proteomic Changes in Human Spermatozoa.. *International journal of molecular sciences*. PMID: 40649876
2. Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.. *Life (Basel, Switzerland)*. PMID: 35207567
3. HMGB4 is expressed by neuronal cells and affects the expression of genes involved in neural differentiation.. *Scientific reports*. PMID: 27608812
4. Nucleocytoplasmic distribution of the Arabidopsis chromatin-associated HMGB2/3 and HMGB4 proteins.. *Plant physiology*. PMID: 20940346
5. HMGB proteins: interactions with DNA and chromatin.. *Biochimica et biophysica acta*. PMID: 20123072

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 60.2% |
| 置信残基 (pLDDT 70-90) 占比 | 33.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 93.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 93.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR050342; Pfam: PF00505, PF09011 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOX4 | 0.636 | 0.052 | — |
| SRY | 0.625 | 0.052 | — |
| FNDC8 | 0.447 | 0.000 | — |
| RAG1 | 0.405 | 0.400 | — |
| IQCF1 | 0.401 | 0.000 | — |
| SMARCE1 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCF5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CEP70 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SCL30 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| GT-1 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MYB56 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| Q94K96 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| KRTAP12-4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KINB1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:36376753|imex:IM-29283 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 8
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 6 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HMGB4 — High mobility group protein B4，非常新颖，仅有少数基础研究。
2. 蛋白大小186 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WW32
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176256-HMGB4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMGB4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WW32
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WW32-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WW32 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR050342; |
| Pfam | PF00505;PF09011; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176256-HMGB4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP70 | Intact | false |
| KRTAP12-4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
