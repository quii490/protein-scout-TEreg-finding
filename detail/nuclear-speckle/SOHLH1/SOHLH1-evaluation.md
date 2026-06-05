---
type: protein-evaluation
gene: "SOHLH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SOHLH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOHLH1 / C9orf157, NOHLH, TEB2 |
| 蛋白名称 | Spermatogenesis- and oogenesis-specific basic helix-loop-helix-containing protein 1 |
| 蛋白大小 | 328 aa / 34.5 kDa |
| UniProt ID | Q5JUK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 328 aa / 34.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR039583; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 86 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf157, NOHLH, TEB2 |

**关键文献**:
1. FIGLA, LHX8 and SOHLH1 transcription factor networks regulate mouse oocyte growth and differentiation.. *Nucleic acids research*. PMID: 32086523
2. Sohlh1 and Lhx8 are prominent biomarkers to estimate the primordial follicle pool in mice.. *Reproductive biology and endocrinology : RB&E*. PMID: 37194006
3. Auto-regulation of the Sohlh1 gene by the SOHLH2/SOHLH1/SP1 complex: implications for early spermatogenesis and oogenesis.. *PloS one*. PMID: 25003626
4. SOHLH1 and SOHLH2 coordinate spermatogonial differentiation.. *Developmental biology*. PMID: 22056784
5. SOHLH1 and SOHLH2 directly down-regulate STIMULATED BY RETINOIC ACID 8 (STRA8) expression.. *Cell cycle (Georgetown, Tex.)*. PMID: 25603532

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.8 |
| 高置信度残基 (pLDDT>90) 占比 | 11.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 37.8% |
| 低置信 (pLDDT<50) 占比 | 42.1% |
| 有序区域 (pLDDT>70) 占比 | 20.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.8），有序残基占 20.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR039583; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LHX8 | 0.962 | 0.000 | — |
| FIGLA | 0.947 | 0.000 | — |
| NOBOX | 0.942 | 0.000 | — |
| SOHLH2 | 0.919 | 0.000 | — |
| CCDC169-SOHLH2 | 0.918 | 0.000 | — |
| YBX2 | 0.897 | 0.000 | — |
| GBX1 | 0.827 | 0.000 | — |
| STRA8 | 0.736 | 0.000 | — |
| ZBTB16 | 0.697 | 0.000 | — |
| NANOS2 | 0.688 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OIP5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| USHBP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HEMK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ACTN3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CASP3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PEF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RUSC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C10orf55 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| IL16 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.8 + PDB: 无 | pLDDT=57.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles | 一致 |
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
1. SOHLH1 — Spermatogenesis- and oogenesis-specific basic helix-loop-helix-containing protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小328 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JUK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165643-SOHLH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOHLH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JUK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000165643-SOHLH1/subcellular

![](https://images.proteinatlas.org/59439/1500_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/59439/1500_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/59439/1505_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/59439/1505_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/59439/1519_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/59439/1519_H5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JUK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
