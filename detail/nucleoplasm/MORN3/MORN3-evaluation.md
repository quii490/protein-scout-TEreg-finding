---
type: protein-evaluation
gene: "MORN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MORN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MORN3 |
| 蛋白名称 | MORN repeat-containing protein 3 |
| 蛋白大小 | 240 aa / 27.6 kDa |
| UniProt ID | Q6PF18 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Cytoplasmic vesicle, secretory vesicle, acrosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 240 aa / 27.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.4; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003409, IPR052472; Pfam: PF02493 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle, acrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The plasma peptides of ovarian cancer.. *Clinical proteomics*. PMID: 30598658
2. A Designed Peptide Targets Two Types of Modifications of p53 with Anti-cancer Activity.. *Cell chemical biology*. PMID: 29681526
3. Membrane occupation and recognition nexus (MORN) motif controls protein localization and function.. *FEBS letters*. PMID: 35568981
4. Identification and validation of a novel 16-gene prognostic signature for patients with breast cancer.. *Scientific reports*. PMID: 35853971
5. Characterization of membrane occupation and recognition nexus repeat containing 3, meiosis expressed gene 1 binding partner, in mouse male germ cells.. *Asian journal of andrology*. PMID: 25248657

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 78.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.4，有序区 94.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003409, IPR052472; Pfam: PF02493 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MORN5 | 0.781 | 0.000 | — |
| RSPH1 | 0.713 | 0.620 | — |
| LRGUK | 0.629 | 0.301 | — |
| PACRG | 0.611 | 0.000 | — |
| RIMBP3 | 0.574 | 0.000 | — |
| HOOK1 | 0.569 | 0.104 | — |
| RSPH3 | 0.546 | 0.139 | — |
| HOOK2 | 0.499 | 0.154 | — |
| KIF3B | 0.492 | 0.000 | — |
| CCDC148 | 0.472 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ALOXE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNASE7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RSPH1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| DYNLL2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| IKZF3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PAX6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EIF3D | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LHX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 8J07 | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, acrosome / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MORN3 — MORN repeat-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小240 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PF18
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139714-MORN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MORN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PF18
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000139714-MORN3/subcellular

![](https://images.proteinatlas.org/38710/2183_A12_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/38710/2183_A12_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/38710/2199_C12_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/38710/2199_C12_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/38710/1240_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/38710/1240_C5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PF18-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PF18 |
| SMART | SM00698; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003409;IPR052472; |
| Pfam | PF02493; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139714-MORN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOXE3 | Intact | false |
| ARID5A | Intact | false |
| BEX2 | Intact | false |
| BLZF1 | Intact | false |
| C14orf119 | Intact | false |
| CDCA7L | Intact | false |
| CTDSP1 | Intact | false |
| DYNLL1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
