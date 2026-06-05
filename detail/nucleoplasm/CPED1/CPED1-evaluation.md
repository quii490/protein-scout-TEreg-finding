---
type: protein-evaluation
gene: "CPED1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPED1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPED1 |
| 蛋白名称 | CPED1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | CPED1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | x1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (<=40->8) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | x3 | 9 | STRING 13 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 34 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Identification of Hypoxia and Mitochondrial-related Gene Signature and Prediction of Prognostic Model in Lung Adenocarcinoma.. *Journal of Cancer*. PMID: 39006078
2. Loss of cped1 does not affect bone and lean tissue in zebrafish.. *bioRxiv : the preprint server for biology*. PMID: 39026892
3. FOXP2 confers oncogenic effects in prostate cancer.. *eLife*. PMID: 37668356
4. Characterization of expression and alternative splicing of the gene cadherin-like and PC esterase domain containing 1 (Cped1).. *Gene*. PMID: 29935354
5. Cped1 promotes chicken SSCs formation with the aid of histone acetylation and transcription factor Sox2.. *Bioscience reports*. PMID: 30038055

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WNT16 | 0.702 | 0.000 | — |
| ING3 | 0.696 | 0.000 | — |
| FAM3C | 0.657 | 0.000 | — |
| TNFSF11 | 0.517 | 0.000 | — |
| FAM210A | 0.507 | 0.000 | — |
| EPDR1 | 0.495 | 0.000 | — |
| IZUMO3 | 0.480 | 0.000 | — |
| PPP6R3 | 0.447 | 0.000 | — |
| GALNT3 | 0.442 | 0.000 | — |
| MAMSTR | 0.441 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| gabP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENST00000310396 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 2
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 13 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CPED1 -- CPED1 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/CPED1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106034-CPED1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPED1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CPED1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106034-CPED1/subcellular

![](https://images.proteinatlas.org/12058/94_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/12058/94_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/12058/95_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/12058/95_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/12058/96_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/12058/96_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
