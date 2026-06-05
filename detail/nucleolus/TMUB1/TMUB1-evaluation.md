---
type: protein-evaluation
gene: "TMUB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMUB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMUB1 / C7orf21, DULP, HOPS |
| 蛋白名称 | Transmembrane and ubiquitin-like domain-containing protein 1 |
| 蛋白大小 | 246 aa / 26.3 kDa |
| UniProt ID | Q9BVT8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane; Postsynaptic cell membrane; Recycling endosome; Cy |
| 蛋白大小 | 10/10 | ×1 | 10 | 246 aa / 26.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040352, IPR000626, IPR029071; Pfam: PF00240 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane; Postsynaptic cell membrane; Recycling endosome; Cytoplasm; Nucleus; Nucleus, nucleolus; Cy... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- nucleolus (GO:0005730)
- postsynaptic membrane (GO:0045211)
- recycling endosome (GO:0055037)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf21, DULP, HOPS |

**关键文献**:
1. Promoting anti-tumor immunity by targeting TMUB1 to modulate PD-L1 polyubiquitination and glycosylation.. *Nature communications*. PMID: 36376293
2. ERLIN1/2 scaffolds bridge TMUB1 and RNF170 and restrict cholesterol esterification to regulate the secretory pathway.. *Life science alliance*. PMID: 38782601
3. The Ins and Outs of HOPS/TMUB1 in biology and pathology.. *The FEBS journal*. PMID: 32860479
4. Nicotine-derived NNK promotes CRC progression through activating TMUB1/AKT pathway in METTL14/YTHDF2-mediated m6A manner.. *Journal of hazardous materials*. PMID: 38341886
5. Quality Control of ER Membrane Proteins by the RNF185/Membralin Ubiquitin Ligase Complex.. *Molecular cell*. PMID: 32738194

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.9 |
| 高置信度残基 (pLDDT>90) 占比 | 3.3% |
| 置信残基 (pLDDT 70-90) 占比 | 45.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 49.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.9），有序残基占 49.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040352, IPR000626, IPR029071; Pfam: PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERLIN2 | 0.919 | 0.695 | — |
| TMEM259 | 0.899 | 0.292 | — |
| RNF185 | 0.869 | 0.581 | — |
| ERLIN1 | 0.846 | 0.609 | — |
| TMUB2 | 0.844 | 0.707 | — |
| RNF170 | 0.798 | 0.564 | — |
| AMFR | 0.780 | 0.380 | — |
| ENSP00000493701 | 0.587 | 0.053 | — |
| CAMLG | 0.582 | 0.303 | — |
| FAM8A1 | 0.574 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GOLM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CHRNA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMBIM6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMUB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RIC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNK16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.9 + PDB: 无 | pLDDT=65.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Postsynaptic cell membrane; Recycling en / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. TMUB1 — Transmembrane and ubiquitin-like domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小246 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVT8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164897-TMUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVT8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164897-TMUB1/subcellular

![](https://images.proteinatlas.org/29429/273_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/29429/273_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/29429/274_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/29429/274_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/29429/275_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/29429/275_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BVT8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
