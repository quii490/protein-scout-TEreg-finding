---
type: protein-evaluation
gene: "CYSRT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYSRT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYSRT1 / C9orf169 |
| 蛋白名称 | Cysteine-rich tail protein 1 |
| 蛋白大小 | 144 aa / 15.3 kDa |
| UniProt ID | A8MQ03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; 额外: Vesicles, Midbody; UniProt: Cornified envelope |
| 蛋白大小 | 8/10 | ×1 | 8 | 144 aa / 15.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018904; Pfam: PF10631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Vesicles, Midbody | Approved |
| UniProt | Cornified envelope | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf169 |

**关键文献**:
1. CYSRT1: An Antimicrobial Epidermal Protein that Can Interact with Late Cornified Envelope Proteins.. *The Journal of investigative dermatology*. PMID: 36804407
2. Application of weighted gene co-expression network analysis to identify key modules and hub genes in oral squamous cell carcinoma tumorigenesis.. *OncoTargets and therapy*. PMID: 30275705

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 53.5% |
| 低置信 (pLDDT<50) 占比 | 35.4% |
| 有序区域 (pLDDT>70) 占比 | 11.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 11.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018904; Pfam: PF10631 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPRP | 0.657 | 0.591 | — |
| KRT78 | 0.642 | 0.046 | — |
| KRTAP1-3 | 0.624 | 0.624 | — |
| LCE3A | 0.617 | 0.591 | — |
| ZNF587 | 0.603 | 0.074 | — |
| SMIM5 | 0.593 | 0.000 | — |
| KRTAP9-8 | 0.592 | 0.591 | — |
| PLLP | 0.591 | 0.591 | — |
| ZNF786 | 0.591 | 0.591 | — |
| LCE2C | 0.591 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498316.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CACNA1A | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| SMOC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCEANC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDKL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RGL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYP21A2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MED25 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PKD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cornified envelope / Nuclear speckles; 额外: Vesicles, Midbody | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CYSRT1 — Cysteine-rich tail protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小144 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MQ03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYSRT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MQ03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/subcellular

![](https://images.proteinatlas.org/21886/1207_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/1207_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/21886/237_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/237_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/21886/268_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/268_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MQ03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A8MQ03 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018904; |
| Pfam | PF10631; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A1CF | Intact | false |
| ACY3 | Intact | false |
| ADAMTSL3 | Intact | false |
| AGXT | Intact | false |
| ALDH3B1 | Intact | false |
| ALPP | Intact | false |
| AQP1 | Intact | false |
| AREG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
