---
type: protein-evaluation
gene: "NACC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NACC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NACC1 / BTBD14B, NAC1 |
| 蛋白名称 | Nucleus accumbens-associated protein 1 |
| 蛋白大小 | 527 aa / 57.3 kDa |
| UniProt ID | Q96RE7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 527 aa / 57.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 3GA1, 4U2N, 7BV9, 8YZS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018379, IPR000210, IPR011333, IPR050457; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTBD14B, NAC1 |

**关键文献**:
1. An overview of the co-transcription factor NACC1: Beyond its pro-tumor effects.. *Life sciences*. PMID: 38030057
2. Dynamic BTB-domain filaments promote clustering of ZBTB proteins.. *Molecular cell*. PMID: 38996459
3. An intellectual-disability-associated mutation of the transcriptional regulator NACC1 impairs glutamatergic neurotransmission.. *Frontiers in molecular neuroscience*. PMID: 37533751
4. Nucleus Accumbens Associated Protein 1 in Cancers-The Real Value.. *International journal of molecular sciences*. PMID: 39769395
5. Nacc1 Mutation in Mice Models Rare Neurodevelopmental Disorder with Underlying Synaptic Dysfunction.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 38388424

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 27.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 47.8% |
| 有序区域 (pLDDT>70) 占比 | 43.6% |
| 可用 PDB 条目 | 3GA1, 4U2N, 7BV9, 8YZS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 43.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018379, IPR000210, IPR011333, IPR050457; Pfam: PF10523, PF00651 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GADD45GIP1 | 0.913 | 0.125 | — |
| HDAC4 | 0.874 | 0.535 | — |
| SCAF1 | 0.787 | 0.000 | — |
| FBXL19 | 0.778 | 0.068 | — |
| NANOG | 0.777 | 0.489 | — |
| POU5F1 | 0.743 | 0.190 | — |
| SOX2 | 0.702 | 0.094 | — |
| U2AF2 | 0.649 | 0.000 | — |
| PSMD7 | 0.633 | 0.309 | — |
| KLF16 | 0.627 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Sox2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Pou5f1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ZBTB9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKCI | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LSM3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LGALS8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ITLN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPL43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 3GA1, 4U2N, 7BV9, 8YZS | pLDDT=63.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NACC1 — Nucleus accumbens-associated protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小527 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RE7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160877-NACC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NACC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RE7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000160877-NACC1/subcellular

![](https://images.proteinatlas.org/21238/146_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/21238/146_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/21238/147_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/21238/147_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/21238/148_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/21238/148_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RE7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
