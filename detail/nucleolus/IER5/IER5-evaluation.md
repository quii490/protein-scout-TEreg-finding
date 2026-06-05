---
type: protein-evaluation
gene: "IER5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IER5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IER5 |
| 蛋白名称 | Immediate early response gene 5 protein |
| 蛋白大小 | 327 aa / 33.7 kDa |
| UniProt ID | Q5VY09 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 33.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.5; PDB: 8UO5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008653; Pfam: PF05760 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular mechanism of PP2A/B55α phosphatase inhibition by IER5.. *Cell chemical biology*. PMID: 40209703
2. PP2A and its adapter protein IER5 induce the DNA-binding ability and target gene expression of E2F1 via dephosphorylation at serine 375.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 37467925
3. Prediction of IER5 structure and function using a bioinformatics approach.. *Molecular medicine reports*. PMID: 31059029
4. PP2A adapter protein IER5 induces dephosphorylation and degradation of MDM2, thereby stabilizing p53.. *Cellular signalling*. PMID: 40081547
5. High IER5 Gene Expression Is Associated With Poor Prognosis in Glioma Patients.. *Frontiers in cell and developmental biology*. PMID: 34222249

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.5 |
| 高置信度残基 (pLDDT>90) 占比 | 6.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 30.3% |
| 低置信 (pLDDT<50) 占比 | 53.2% |
| 有序区域 (pLDDT>70) 占比 | 16.5% |
| 可用 PDB 条目 | 8UO5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.5），有序残基占 16.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008653; Pfam: PF05760 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MPDZ | 0.765 | 0.000 | — |
| PPP2R2C | 0.748 | 0.748 | — |
| PPP2R1A | 0.616 | 0.616 | — |
| PPP2R2D | 0.614 | 0.586 | — |
| MINK1 | 0.597 | 0.510 | — |
| PPP2R2B | 0.594 | 0.579 | — |
| PDZK1IP1 | 0.589 | 0.000 | — |
| MYCL | 0.549 | 0.000 | — |
| HSF1 | 0.542 | 0.510 | — |
| BTG2 | 0.534 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| Rabac1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:30925931|imex:IM-26645 |
| PPP2R2A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2C | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2D | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R1A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.5 + PDB: 8UO5 | pLDDT=53.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IER5 — Immediate early response gene 5 protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VY09
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162783-IER5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IER5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VY09
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162783-IER5/subcellular

![](https://images.proteinatlas.org/29894/321_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/29894/321_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/29894/323_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/29894/323_H2_4_red_green.jpg)
![](https://images.proteinatlas.org/29894/326_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/29894/326_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VY09-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
