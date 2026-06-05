---
type: protein-evaluation
gene: "UMAD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UMAD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UMAD1 / RPA3-AS1, RPA3OS |
| 蛋白名称 | UBAP1-MVB12-associated (UMA)-domain containing protein 1 |
| 蛋白大小 | 137 aa / 15.2 kDa |
| UniProt ID | C9J7I0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 137 aa / 15.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR053292, IPR023340 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RPA3-AS1, RPA3OS |

**关键文献**:
1. Genome-wide haplotype association analysis of primary biliary cholangitis risk in Japanese.. *Scientific reports*. PMID: 29773854
2. The Evf2 Ultraconserved Enhancer lncRNA Functionally and Spatially Organizes Megabase Distant Genes in the Developing Forebrain.. *Molecular cell*. PMID: 30146317
3. Association of the RPA3-UMAD1 locus with interstitial lung diseases complicated with rheumatoid arthritis in Japanese.. *Annals of the rheumatic diseases*. PMID: 32737115
4. Genome-wide placental DNA methylations in fetal overgrowth and associations with leptin, adiponectin and fetal growth factors.. *Clinical epigenetics*. PMID: 36585686

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.8% |
| 低置信 (pLDDT<50) 占比 | 31.4% |
| 有序区域 (pLDDT>70) 占比 | 32.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 32.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053292, IPR023340 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS37B | 0.603 | 0.603 | — |
| TSG101 | 0.565 | 0.562 | — |
| GLCCI1 | 0.479 | 0.000 | — |
| ANO2 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BIRC2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| SHARPIN | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TRAF2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RBCK1 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TNIP1 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TH | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GABARAPL1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Cep55 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ptpn23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TFG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 11
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 无 | pLDDT=61.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 4 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. UMAD1 — UBAP1-MVB12-associated (UMA)-domain containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小137 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9J7I0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000219545-UMAD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UMAD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9J7I0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000219545-UMAD1/subcellular

![](https://images.proteinatlas.org/44806/522_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/44806/522_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/44806/527_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/44806/527_A6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9J7I0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
