---
type: protein-evaluation
gene: "GNPDA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNPDA1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNPDA1 / GNPI, HLN, KIAA0060 |
| 蛋白名称 | Glucosamine-6-phosphate deaminase 1 |
| 蛋白大小 | 289 aa / 32.7 kDa |
| UniProt ID | P46926 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; 额外: Golgi apparatus; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 289 aa / 32.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.9; PDB: 1NE7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006148, IPR004547, IPR018321, IPR037171; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Golgi apparatus | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNPI, HLN, KIAA0060 |

**关键文献**:
1. The Possible Roles of Glucosamine-6-Phosphate Deaminases in Ammonium Metabolism in Cancer.. *International journal of molecular sciences*. PMID: 39596123
2. Identification of differential proteins in colorectal cancer cells treated with caffeic acid phenethyl ester.. *World journal of gastroenterology*. PMID: 25206290
3. Activating miRNA-mRNA network in gemcitabine-resistant pancreatic cancer cell associates with alteration of memory CD4(+) T cells.. *Annals of translational medicine*. PMID: 32355723
4. Phlegm-dampness constitution: genomics, susceptibility, adjustment and treatment with traditional Chinese medicine.. *The American journal of Chinese medicine*. PMID: 23548117
5. Development and Validation of a Novel Prognosis Model Based on a Panel of Three Immunogenic Cell Death-Related Genes for Non-Cirrhotic Hepatocellular Carcinoma.. *Journal of hepatocellular carcinoma*. PMID: 37781718

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 90.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| 可用 PDB 条目 | 1NE7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.9，有序区 93.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006148, IPR004547, IPR018321, IPR037171; Pfam: PF01182 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AMDHD2-2 | 0.995 | 0.071 | — |
| AMDHD2 | 0.994 | 0.790 | — |
| GNPNAT1 | 0.971 | 0.000 | — |
| GNPDA2 | 0.970 | 0.701 | — |
| GFPT2 | 0.969 | 0.000 | — |
| GFPT1 | 0.969 | 0.000 | — |
| GPI | 0.962 | 0.000 | — |
| H6PD | 0.949 | 0.000 | — |
| HK1 | 0.944 | 0.000 | — |
| MPI | 0.943 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Gnpda | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9552|pubmed:19079254 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| GNPDA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEC31A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACCS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AMDHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA11 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 1NE7 | pLDDT=93.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Vesicles; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNPDA1 — Glucosamine-6-phosphate deaminase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小289 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46926
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113552-GNPDA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNPDA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46926
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46926-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
