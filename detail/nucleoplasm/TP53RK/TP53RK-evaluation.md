---
type: protein-evaluation
gene: "TP53RK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TP53RK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TP53RK / C20orf64, PRPK |
| 蛋白名称 | EKC/KEOPS complex subunit TP53RK |
| 蛋白大小 | 253 aa / 28.2 kDa |
| UniProt ID | Q96S44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 253 aa / 28.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.0; PDB: 6WQX, 7SZA, 7SZB, 7SZC, 7SZD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR022495, IPR011009, IPR000719, IPR008266; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- EKC/KEOPS complex (GO:0000408)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf64, PRPK |

**关键文献**:
1. Mutations in KEOPS-complex genes cause nephrotic syndrome with primary microcephaly.. *Nature genetics*. PMID: 28805828
2. TP53RK Drives the Progression of Chronic Kidney Disease by Phosphorylating Birc5.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37382161
3. Identifying TP53RK as a key regulator of colorectal cancer survival and a potential therapeutic target.. *Scientific reports*. PMID: 41102525
4. Identification of TP53RK-Binding Protein (TPRKB) Dependency in TP53-Deficient Cancers.. *Molecular cancer research : MCR*. PMID: 31110156
5. p53-related protein kinase confers poor prognosis and represents a novel therapeutic target in multiple myeloma.. *Blood*. PMID: 28082445

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 77.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 6WQX, 7SZA, 7SZB, 7SZC, 7SZD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6WQX, 7SZA, 7SZB, 7SZC, 7SZD）+ AlphaFold极高置信度预测（pLDDT=91.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022495, IPR011009, IPR000719, IPR008266; Pfam: PF06293 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TPRKB | 0.999 | 0.997 | — |
| GON7 | 0.999 | 0.873 | — |
| LAGE3 | 0.999 | 0.736 | — |
| OSGEP | 0.999 | 0.993 | — |
| TP53 | 0.982 | 0.510 | — |
| OSGEPL1 | 0.958 | 0.744 | — |
| YRDC | 0.847 | 0.000 | — |
| NUP43 | 0.819 | 0.812 | — |
| PDXK | 0.803 | 0.000 | — |
| WDR73 | 0.712 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TPRKB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DCTN1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| LRRC2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| OSGEP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SYNE1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SMS | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| PATJ | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| NUP43 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 6WQX, 7SZA, 7SZB, 7SZC, 7SZD | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TP53RK — EKC/KEOPS complex subunit TP53RK，非常新颖，仅有少数基础研究。
2. 蛋白大小253 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96S44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172315-TP53RK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TP53RK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96S44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96S44-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96S44 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 33..253; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR022495;IPR011009;IPR000719;IPR008266; |
| Pfam | PF06293; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172315-TP53RK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CALCOCO2 | Intact, Biogrid | true |
| GON7 | Intact, Biogrid, Bioplex | true |
| LAGE3 | Biogrid, Bioplex | true |
| OSGEP | Intact, Biogrid, Bioplex | true |
| TPRKB | Intact, Biogrid, Bioplex | true |
| GORASP2 | Intact | false |
| MTUS2 | Intact | false |
| NUP43 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
