---
type: protein-evaluation
gene: "TRAIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAIP / RNF206, TRIP |
| 蛋白名称 | E3 ubiquitin-protein ligase TRAIP |
| 蛋白大小 | 469 aa / 53.3 kDa |
| UniProt ID | Q9BWF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus; Chromosome; Cytopl |
| 蛋白大小 | 10/10 | ×1 | 10 | 469 aa / 53.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.9; PDB: 4ZTD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052639, IPR001841, IPR013083; Pfam: PF13639 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus; Chromosome; Cytoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- site of DNA damage (GO:0090734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF206, TRIP |

**关键文献**:
1. Functional interrogation of DNA damage response variants with base editing screens.. *Cell*. PMID: 33606978
2. TRAIP suppresses bladder cancer progression by catalyzing K48-linked polyubiquitination of MYC.. *Oncogene*. PMID: 38123820
3. Silencing TRAIP suppresses cell proliferation and migration/invasion of triple negative breast cancer via RB-E2F signaling and EMT.. *Cancer gene therapy*. PMID: 36064576
4. Recognition of TRAIP with TRAFs: Current understanding and associated diseases.. *The international journal of biochemistry & cell biology*. PMID: 31442608
5. The Ubiquitin Ligase TRAIP: Double-Edged Sword at the Replisome.. *Trends in cell biology*. PMID: 33317933

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 23.5% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 4ZTD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.9，有序区 60.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052639, IPR001841, IPR013083; Pfam: PF13639 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAF1 | 0.896 | 0.527 | — |
| CYLD | 0.870 | 0.236 | — |
| TRAF2 | 0.841 | 0.744 | — |
| UIMC1 | 0.783 | 0.510 | — |
| FANCD2 | 0.753 | 0.292 | — |
| MAPRE2 | 0.723 | 0.723 | — |
| NEIL3 | 0.714 | 0.000 | — |
| CDC45 | 0.714 | 0.000 | — |
| MCM7 | 0.713 | 0.292 | — |
| LRR1 | 0.703 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-28986477 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| UBE2Z | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| TSG101 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| HIP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2H | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 4ZTD | pLDDT=74.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus; Chromoso / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRAIP — E3 ubiquitin-protein ligase TRAIP，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小469 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183763-TRAIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000183763-TRAIP/subcellular

![](https://images.proteinatlas.org/36261/434_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36261/434_D9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36261/450_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36261/450_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36261/453_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36261/453_D9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWF2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWF2 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052639;IPR001841;IPR013083; |
| Pfam | PF13639; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183763-TRAIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOX15B | Intact | false |
| CEP19 | Intact | false |
| CYLD | Biogrid | false |
| FLII | Biogrid | false |
| H2AX | Biogrid | false |
| JPH3 | Intact | false |
| LXN | Intact | false |
| MAPRE2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
