---
type: protein-evaluation
gene: "Mycl"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Mycl 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Mycl / BHLHE38, LMYC, MYCL1 |
| 蛋白名称 | Protein L-Myc |
| 蛋白大小 | 364 aa / 40.3 kDa |
| UniProt ID | P12524 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Mitotic chromosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 364 aa / 40.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR050433, IPR002418, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 169 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE38, LMYC, MYCL1 |

**关键文献**:
1. Rlf-Mycl Gene Fusion Drives Tumorigenesis and Metastasis in a Mouse Model of Small Cell Lung Cancer.. *Cancer discovery*. PMID: 34344693
2. MAX Functions as a Tumor Suppressor and Rewires Metabolism in Small Cell Lung Cancer.. *Cancer cell*. PMID: 32470392
3. A Novel Synthetic Lethal Approach to Target MYC-Driven Cancers.. *Cancer research*. PMID: 35288735
4. MYCL promotes iPSC-like colony formation via MYC Box 0 and 2 domains.. *Scientific reports*. PMID: 34930932
5. Demystifying the Druggability of the MYC Family of Oncogenes.. *Journal of the American Chemical Society*. PMID: 36734615

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 39.3% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 28.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.7），有序残基占 28.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR050433, IPR002418, IPR012682; Pfam: PF00010, PF01056 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAX | 0.962 | 0.761 | — |
| EP400 | 0.960 | 0.776 | — |
| RLF | 0.805 | 0.045 | — |
| LIN28A | 0.770 | 0.000 | — |
| EPC1 | 0.764 | 0.761 | — |
| TRRAP | 0.750 | 0.622 | — |
| VPS72 | 0.735 | 0.717 | — |
| PPIE | 0.733 | 0.000 | — |
| KAT5 | 0.727 | 0.673 | — |
| JAZF1 | 0.725 | 0.718 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRKAA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCNK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CATSPER1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OTUD6A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CASK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AURKA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TAF5L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUPT7L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YEATS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.7 + PDB: 无 | pLDDT=63.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Mitotic chromosome | 一致 |
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
1. Mycl — Protein L-Myc，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小364 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P12524
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116990-MYCL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Mycl
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P12524
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000116990-MYCL/subcellular

![](https://images.proteinatlas.org/63132/1141_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/63132/1141_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/63132/1170_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/63132/1170_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/63132/1392_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/63132/1392_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P12524-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
