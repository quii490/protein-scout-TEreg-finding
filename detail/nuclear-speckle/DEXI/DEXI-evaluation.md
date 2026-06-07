---
type: protein-evaluation
gene: "DEXI"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEXI 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEXI / MYLE |
| 蛋白名称 | Dexamethasone-induced protein |
| 蛋白大小 | 95 aa / 10.4 kDa |
| UniProt ID | O95424 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 95 aa / 10.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023259; Pfam: PF15198 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MYLE |

**关键文献**:
1. Shared genetic architecture between leukocyte telomere length and Alzheimer's disease.. *Alzheimer's research & therapy*. PMID: 40382655
2. MiR-3960 inhibits bladder cancer progression via targeting of DEXI.. *Biochemical and biophysical research communications*. PMID: 37230046
3. Is DEXI a Multiple Sclerosis Susceptibility Gene?. *International journal of molecular sciences*. PMID: 39940946
4. DEXI, a candidate gene for type 1 diabetes, modulates rat and human pancreatic beta cell inflammation via regulation of the type I IFN/STAT signalling pathway.. *Diabetologia*. PMID: 30478640
5. Long-range DNA looping and gene expression analyses identify DEXI as an autoimmune disease candidate gene.. *Human molecular genetics*. PMID: 21989056

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 18.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 56.8% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 34.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 34.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023259; Pfam: PF15198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLEC16A | 0.808 | 0.000 | — |
| RMI2 | 0.674 | 0.000 | — |
| CIITA | 0.593 | 0.000 | — |
| ZC3H7A | 0.588 | 0.000 | — |
| MRPS28 | 0.578 | 0.000 | — |
| RD3L | 0.506 | 0.000 | — |
| RFXAP | 0.498 | 0.000 | — |
| MAP6D1 | 0.491 | 0.000 | — |
| LRRC1 | 0.444 | 0.000 | — |
| KCTD2 | 0.442 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBCD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GOLM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBQLN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PEX16 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TTMP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BMP10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SETDB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 无 | pLDDT=68.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DEXI — Dexamethasone-induced protein，非常新颖，仅有少数基础研究。
2. 蛋白大小95 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95424
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182108-DEXI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEXI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95424
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000182108-DEXI/subcellular

![](https://images.proteinatlas.org/41511/504_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/41511/504_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/41511/506_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/41511/506_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/41511/555_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/41511/555_F1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95424-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95424 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023259; |
| Pfam | PF15198; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182108-DEXI/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BMP10 | Intact | false |
| C3orf52 | Intact | false |
| KAT5 | Intact | false |
| PEX16 | Intact | false |
| PRKCA | Intact | false |
| SGTB | Intact | false |
| UBQLN1 | Intact | false |
| YWHAG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
