---
type: protein-evaluation
gene: "COMMD10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD10 |
| 蛋白名称 | COMM domain-containing protein 10 |
| 蛋白大小 | 202 aa / 23.0 kDa |
| UniProt ID | Q9Y6G5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 202 aa / 23.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.7; PDB: 8ESD, 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017920, IPR037361; Pfam: PF07258, PF21672 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Copper metabolism in cell death and autophagy.. *Autophagy*. PMID: 37055935
2. Expression profile and bioinformatics analysis of COMMD10 in BALB/C mice and human.. *Cancer gene therapy*. PMID: 30787448
3. A Contemporary Review of the Genomic Associations of Coronary Artery Myocardial Bridging.. *Genes*. PMID: 38136997
4. COMMD10 inhibits tumor progression and induces apoptosis by blocking NF-κB signal and values up BCLC staging in predicting overall survival in hepatocellular carcinoma.. *Clinical and translational medicine*. PMID: 34047468
5. COMMD10 Regulates Angiogenesis and Bone Formation via Rap1 Signaling Pathway.. *FASEB bioAdvances*. PMID: 40496352

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 47.5% |
| 置信残基 (pLDDT 70-90) 占比 | 35.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 2.0% |
| 有序区域 (pLDDT>70) 占比 | 83.1% |
| 可用 PDB 条目 | 8ESD, 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8ESD, 8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=83.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037361; Pfam: PF07258, PF21672 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD2 | 0.987 | 0.916 | — |
| COMMD1 | 0.980 | 0.853 | — |
| CCDC22 | 0.979 | 0.903 | — |
| COMMD5 | 0.979 | 0.866 | — |
| COMMD6 | 0.978 | 0.836 | — |
| COMMD9 | 0.976 | 0.816 | — |
| COMMD7 | 0.976 | 0.854 | — |
| COMMD3 | 0.971 | 0.868 | — |
| CCDC93 | 0.971 | 0.906 | — |
| COMMD8 | 0.970 | 0.839 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vlet | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Setd3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| COMMD1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELA | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB2 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| COMMD5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 8ESD, 8F2R, 8F2U, 8P0W | pLDDT=83.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD10 — COMM domain-containing protein 10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小202 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6G5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145781-COMMD10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6G5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000145781-COMMD10/subcellular

![](https://images.proteinatlas.org/54156/834_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/54156/834_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/54156/867_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/54156/867_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/54156/877_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/54156/877_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6G5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
