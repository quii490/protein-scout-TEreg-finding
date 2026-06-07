---
type: protein-evaluation
gene: "OLIG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## OLIG2 — REJECTED (研究热度过高 (PubMed strict=1022，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OLIG2 / BHLHB1, BHLHE19, PRKCBP2, RACK17 |
| 蛋白名称 | Oligodendrocyte transcription factor 2 |
| 蛋白大小 | 323 aa / 32.4 kDa |
| UniProt ID | Q13516 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 323 aa / 32.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1022 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050359, IPR036638, IPR032658; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Uncertain |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

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
| PubMed strict count | 1022 |
| PubMed broad count | 2079 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB1, BHLHE19, PRKCBP2, RACK17 |

**关键文献**:
1. Single-cell RNA-sequencing of human eosinophils in allergic inflammation in the esophagus.. *The Journal of allergy and clinical immunology*. PMID: 38871184
2. Transcription factors ASCL1 and OLIG2 drive glioblastoma initiation and co-regulate tumor cell types and migration.. *Nature communications*. PMID: 39609428
3. Generation and isolation of oligodendrocyte progenitor cells from human pluripotent stem cells.. *Nature protocols*. PMID: 26134954
4. A conserved molecular logic for neurogenesis to gliogenesis switch in the cerebral cortex.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38713624
5. Reconstructing and reprogramming the tumor-propagating potential of glioblastoma stem-like cells.. *Cell*. PMID: 24726434

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 19.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 26.0% |
| 低置信 (pLDDT<50) 占比 | 49.8% |
| 有序区域 (pLDDT>70) 占比 | 24.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 24.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050359, IPR036638, IPR032658; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ID4 | 0.952 | 0.311 | — |
| GFAP | 0.919 | 0.000 | — |
| OLIG1 | 0.909 | 0.000 | — |
| CSPG4 | 0.898 | 0.000 | — |
| ID2 | 0.896 | 0.311 | — |
| SOX10 | 0.892 | 0.073 | — |
| NKX2-2 | 0.885 | 0.091 | — |
| PAX6 | 0.877 | 0.045 | — |
| MBP | 0.843 | 0.000 | — |
| NES | 0.836 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Id4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15280210 |
| Tcf3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15280210 |
| Id2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15280210 |
| Smarca4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23332759|imex:IM-20830 |
| TXLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP12-4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LRRFIP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| SMAD4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| HEY1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 无 | pLDDT=59.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. OLIG2 — Oligodendrocyte transcription factor 2，研究基础较多，新颖性有限。
2. 蛋白大小323 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1022 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1022 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13516
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205927-OLIG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OLIG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13516
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000205927-OLIG2/subcellular

![](https://images.proteinatlas.org/3254/118_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/3254/118_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/3254/119_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/3254/119_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/3254/120_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/3254/120_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13516-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13516 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 108..162; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050359;IPR036638;IPR032658; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205927-OLIG2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KRTAP12-4 | Intact | false |
| TXLNA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
