---
type: protein-evaluation
gene: "CUEDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CUEDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CUEDC2 / C10orf66 |
| 蛋白名称 | CUE domain-containing protein 2 |
| 蛋白大小 | 287 aa / 32.0 kDa |
| UniProt ID | Q9H467 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear membrane, Plasma membrane,; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 287 aa / 32.0 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=39 篇 (<=40->8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=72.5; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR003892, IPR039805; Pfam: PF02845 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear membrane, Plasma membrane, Primary cilium tip | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf66 |

**关键文献**:
1. CUEDC2: multifunctional roles in carcinogenesis.. *Frontiers in bioscience (Landmark edition)*. PMID: 30844721
2. Comparison of ADAM19 and CUEDC2 expression in EHCC and their clinicopathological significance.. *Biomarkers in medicine*. PMID: 32960074
3. CUEDC2 controls osteoblast differentiation and bone formation via SOCS3-STAT3 pathway.. *Cell death & disease*. PMID: 32393737
4. CUEDC2 Drives β-Catenin Nuclear Translocation and Promotes Triple-Negative Breast Cancer Tumorigenesis.. *Cells*. PMID: 36231027
5. CUEDC2: an emerging key player in inflammation and tumorigenesis.. *Protein & cell*. PMID: 21976060

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 28.9% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 20.2% |
| 有序区域 (pLDDT>70) 占比 | 64.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.5，有序区 64.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003892, IPR039805; Pfam: PF02845 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGR | 0.834 | 0.292 | — |
| TBP | 0.788 | 0.781 | — |
| ESR1 | 0.756 | 0.510 | — |
| IKBKB | 0.661 | 0.292 | — |
| CHUK | 0.660 | 0.292 | — |
| FZR1 | 0.619 | 0.612 | — |
| CDC27 | 0.608 | 0.510 | — |
| GTF2A1 | 0.591 | 0.591 | — |
| FBXL15 | 0.587 | 0.000 | — |
| ELOC | 0.580 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RNF26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KHK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FZR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GTF2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CTLA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| hspa1a_hspa1b_human-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 无 | pLDDT=72.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Nuclear membrane, Plasma | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CUEDC2 -- CUE domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H467
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107874-CUEDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CUEDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H467
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H467-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
