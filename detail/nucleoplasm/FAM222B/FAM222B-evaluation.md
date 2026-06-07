---
type: protein-evaluation
gene: "FAM222B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM222B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM222B / C17orf63 |
| 蛋白名称 | Protein FAM222B |
| 蛋白大小 | 562 aa / 59.7 kDa |
| UniProt ID | Q8WU58 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 562 aa / 59.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029340; Pfam: PF15258 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf63 |

**关键文献**:
1. Delphinidin upregulates microRNA-let-7b expression through family with sequence similarity 222 member B.. *Scientific reports*. PMID: 40789939
2. FAM222B Is Not a Likely Novel Candidate Gene for Cerebral Cavernous Malformations.. *Molecular syndromology*. PMID: 27587990
3. Exploration of signature-related FAM genes and correlation between FAM50A expression and the pathogenesis and prognosis of hepatocellular carcinoma.. *Translational cancer research*. PMID: 40950660
4. Evolutionary analysis through structural modeling of FAM222 proteins reveals a novel disordered conserved domain in vertebrates that interacts with NLK.. *Scientific reports*. PMID: 41365991

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.8 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.0% |
| 中等置信 (pLDDT 50-70) 占比 | 18.9% |
| 低置信 (pLDDT<50) 占比 | 73.3% |
| 有序区域 (pLDDT>70) 占比 | 7.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.8），有序残基占 7.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029340; Pfam: PF15258 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDZD9 | 0.641 | 0.000 | — |
| NLK | 0.538 | 0.532 | — |
| OR51D1 | 0.526 | 0.000 | — |
| ZNF572 | 0.488 | 0.000 | — |
| SSC4D | 0.484 | 0.000 | — |
| CEP152 | 0.474 | 0.000 | — |
| OR2K2 | 0.463 | 0.000 | — |
| ZNF789 | 0.452 | 0.000 | — |
| TRMT10B | 0.447 | 0.000 | — |
| ZNF695 | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0G2RPY1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ddhA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| aroF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NLK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TRIP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM168B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP11-1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BPIFA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RUNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| WWOX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.8 + PDB: 无 | pLDDT=47.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM222B — Protein FAM222B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小562 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WU58
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173065-FAM222B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM222B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WU58
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000173065-FAM222B/subcellular

![](https://images.proteinatlas.org/51840/1028_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/51840/1028_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/51840/802_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/51840/802_C5_5_red_green.jpg)
![](https://images.proteinatlas.org/51840/910_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/51840/910_G4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WU58-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WU58 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029340; |
| Pfam | PF15258; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173065-FAM222B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBQLN2 | Intact, Biogrid | true |
| AKAP8L | Intact | false |
| BAG4 | Intact | false |
| BPIFA1 | Intact | false |
| CDCA4 | Intact | false |
| CNFN | Intact | false |
| CYSRT1 | Intact | false |
| EIF3F | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
