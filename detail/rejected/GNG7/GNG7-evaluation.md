---
type: protein-evaluation
gene: "GNG7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNG7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNG7 / GNGT7 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-7 |
| 蛋白大小 | 68 aa / 7.5 kDa |
| UniProt ID | O60262 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 68 aa / 7.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 97 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNGT7 |

**关键文献**:
1. GNG7 as a tumor-suppressor gene in lung adenocarcinoma: implications for prognosis and immune-based therapies.. *Frontiers in oncology*. PMID: 40496619
2. GNG7 and ADCY1 as diagnostic and prognostic biomarkers for pancreatic adenocarcinoma through bioinformatic-based analyses.. *Scientific reports*. PMID: 34650124
3. The Prognostic Value of GNG7 in Colorectal Cancer and Its Relationship With Immune Infiltration.. *Frontiers in genetics*. PMID: 35281820
4. Loss of protein expression and recurrent DNA hypermethylation of the GNG7 gene in squamous cell carcinoma of the head and neck.. *Journal of applied genetics*. PMID: 22183866
5. Identification of GNG7 as a novel biomarker and potential therapeutic target for gastric cancer via bioinformatic analysis and in vitro experiments.. *Aging*. PMID: 36863706

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.9 |
| 高置信度残基 (pLDDT>90) 占比 | 69.1% |
| 置信残基 (pLDDT 70-90) 占比 | 27.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.9，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB3 | 0.999 | 0.995 | — |
| GNB1 | 0.999 | 0.995 | — |
| GNB2 | 0.999 | 0.995 | — |
| GNB4 | 0.999 | 0.995 | — |
| GNB5 | 0.999 | 0.995 | — |
| GNAI1 | 0.973 | 0.830 | — |
| GNAS | 0.964 | 0.400 | — |
| GNAL | 0.959 | 0.400 | — |
| GNAI3 | 0.952 | 0.834 | — |
| GNAI2 | 0.947 | 0.811 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MPP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GNB5 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| Kcnk2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23021213|imex:IM-18125 |
| GNAI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GORASP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GNAI3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNAI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.9 + PDB: 无 | pLDDT=90.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNG7 — Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-7，研究基础较多，新颖性有限。
2. 蛋白大小68 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60262
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176533-GNG7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNG7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60262
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60262-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
