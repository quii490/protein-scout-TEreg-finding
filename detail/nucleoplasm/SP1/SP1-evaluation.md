---
type: protein-evaluation
gene: "SP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SP1 — REJECTED (研究热度过高 (PubMed strict=11333，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP1 / TSFP1 |
| 蛋白名称 | Transcription factor Sp1 |
| 蛋白大小 | 785 aa / 80.7 kDa |
| UniProt ID | P08047 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 785 aa / 80.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=11333 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=39.1; PDB: 1SP1, 1SP2, 1VA1, 1VA2, 1VA3, 6PV0, 6PV1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- euchromatin (GO:0000791)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11333 |
| PubMed broad count | 15060 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TSFP1 |

**关键文献**:
1. SP1 undergoes phase separation and activates RGS20 expression through super-enhancers to promote lung adenocarcinoma progression.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38976739
2. Role of Specificity Protein 1 (SP1) in Cardiovascular Diseases: Pathological Mechanisms and Therapeutic Potentials.. *Biomolecules*. PMID: 39062521
3. Role of Sp1 in atherosclerosis.. *Molecular biology reports*. PMID: 35715606
4. SP1 and NFY Regulate the Expression of PNPT1, a Gene Encoding a Mitochondrial Protein Involved in Cancer.. *International journal of molecular sciences*. PMID: 36232701
5. Sp1 facilitates continued HSV-1 gene expression in the absence of key viral transactivators.. *mBio*. PMID: 38349188

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 39.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 87.3% |
| 有序区域 (pLDDT>70) 占比 | 10.8% |
| 可用 PDB 条目 | 1SP1, 1SP2, 1VA1, 1VA2, 1VA3, 6PV0, 6PV1, 6PV2, 6PV3, 6UCO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=39.1），有序残基占 10.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.999 | 0.892 | — |
| EP300 | 0.999 | 0.926 | — |
| JUN | 0.996 | 0.794 | — |
| TP53 | 0.994 | 0.923 | — |
| TBP | 0.994 | 0.501 | — |
| CREBBP | 0.992 | 0.749 | — |
| HDAC1 | 0.991 | 0.962 | — |
| ESR2 | 0.988 | 0.523 | — |
| E2F1 | 0.983 | 0.745 | — |
| SMAD3 | 0.978 | 0.825 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MED17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24882805|imex:IM-23033 |
| MED27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24882805|imex:IM-23033 |
| MED14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24882805|imex:IM-23033 |
| MED23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24882805|imex:IM-23033 |
| MED24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Taf4 | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| TOC33 | psi-mi:"MI:0096"(pull down) | pubmed:23118188|imex:IM-18721 |
| TOC34 | psi-mi:"MI:0096"(pull down) | pubmed:23118188|imex:IM-18721 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=39.1 + PDB: 1SP1, 1SP2, 1VA1, 1VA2, 1VA3,  | pLDDT=39.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SP1 — Transcription factor Sp1，研究基础较多，新颖性有限。
2. 蛋白大小785 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11333 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=39.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 11333 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P08047
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185591-SP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P08047
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000185591-SP1/subcellular

![](https://images.proteinatlas.org/12292/94_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/12292/94_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/12292/95_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/12292/95_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/12292/96_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/12292/96_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P08047-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
