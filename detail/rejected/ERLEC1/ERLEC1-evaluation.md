---
type: protein-evaluation
gene: "ERLEC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERLEC1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERLEC1 / C2orf30, XTP3TPB |
| 蛋白名称 | Endoplasmic reticulum lectin 1 |
| 蛋白大小 | 483 aa / 54.9 kDa |
| UniProt ID | Q96DZ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 483 aa / 54.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.0; PDB: 8KES, 8KET, 8KEV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009011, IPR044865, IPR045149, IPR012913; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum quality control compartment (GO:0044322)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf30, XTP3TPB |

**关键文献**:
1. Circulating Proteins Influencing Psychiatric Disease: A Mendelian Randomization Study.. *Biological psychiatry*. PMID: 36280454
2. Identification of Endoplasmic Reticulum Stress-Related Biomarkers of Periodontitis Based on Machine Learning: A Bioinformatics Analysis.. *Disease markers*. PMID: 36072904
3. Gut microbiota and interstitial cystitis: exploring the gut-bladder axis through mendelian randomization, biological annotation and bulk RNA sequencing.. *Frontiers in immunology*. PMID: 39399486
4. The Distant Molecular Effects on the Brain by Cancer Treatment.. *Brain sciences*. PMID: 38248237
5. Identification of a novel endoplasmic reticulum stress response element regulated by XBP1.. *The Journal of biological chemistry*. PMID: 23737521

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.3% |
| 置信残基 (pLDDT 70-90) 占比 | 42.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 19.3% |
| 有序区域 (pLDDT>70) 占比 | 67.7% |
| 可用 PDB 条目 | 8KES, 8KET, 8KEV |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8KES, 8KET, 8KEV）+ AlphaFold高质量预测（pLDDT=73.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009011, IPR044865, IPR045149, IPR012913; Pfam: PF07915 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEL1L | 0.998 | 0.916 | — |
| SYVN1 | 0.992 | 0.927 | — |
| DERL2 | 0.990 | 0.898 | — |
| DERL1 | 0.985 | 0.840 | — |
| DERL3 | 0.966 | 0.746 | — |
| CANX | 0.947 | 0.000 | — |
| OS9 | 0.936 | 0.705 | — |
| AMFR | 0.935 | 0.746 | — |
| HSP90B1 | 0.925 | 0.300 | — |
| UBE2J1 | 0.922 | 0.616 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| SLC15A3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MICA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATF6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNTNAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 8KES, 8KET, 8KEV | pLDDT=73.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERLEC1 — Endoplasmic reticulum lectin 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小483 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DZ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068912-ERLEC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERLEC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DZ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DZ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
