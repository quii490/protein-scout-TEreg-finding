---
type: protein-evaluation
gene: "CMBL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMBL — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMBL |
| 蛋白名称 | Carboxymethylenebutenolidase homolog |
| 蛋白大小 | 245 aa / 28.0 kDa |
| UniProt ID | Q96DG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | x1 | 10 | 245 aa / 28.0 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR029058, IPR042946, IPR002925; Pfam: PF01738 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 1979 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Human carboxymethylenebutenolidase as a bioactivating hydrolase of olmesartan medoxomil in liver and intestine.. *The Journal of biological chemistry*. PMID: 20177059
2. Editorial focus: entering into the non-coding RNA era.. *Cellular & molecular biology letters*. PMID: 30250489
3. Further exploitation of metabolic potential for catechol biodegradation of Klebsiella sp. CD33.. *Chemosphere*. PMID: 39542372
4. Clinical monoclonal B lymphocytosis versus Rai 0 chronic lymphocytic leukemia: A comparison of cellular, cytogenetic, molecular, and clinical features.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 24036852
5. Different hydrolases involved in bioactivation of prodrug-type angiotensin receptor blockers: carboxymethylenebutenolidase and carboxylesterase 1.. *Drug metabolism and disposition: the biological fate of chemicals*. PMID: 23946449

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 82.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 92.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 92.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR042946, IPR002925; Pfam: PF01738 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATPSCKMT | 0.884 | 0.000 | — |
| ENSP00000428055 | 0.862 | 0.000 | — |
| ADHFE1 | 0.862 | 0.000 | — |
| HADH | 0.795 | 0.000 | — |
| CRYL1 | 0.787 | 0.000 | — |
| BTC | 0.640 | 0.000 | — |
| AREG | 0.632 | 0.000 | — |
| TRAPPC11 | 0.610 | 0.610 | — |
| TRAPPC12 | 0.610 | 0.610 | — |
| TRAPPC13 | 0.609 | 0.609 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARRB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF4A2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CD2BP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PUF60 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMYD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRIP6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATIC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20000738|imex:IM-19572 |
| EBI-6095751 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CMBL -- Carboxymethylenebutenolidase homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164237-CMBL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMBL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
