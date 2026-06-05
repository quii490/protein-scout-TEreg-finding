---
type: protein-evaluation
gene: "DAND5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAND5 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAND5 |
| 蛋白名称 | DAN domain family member 5 |
| 蛋白大小 | 189 aa / 20.2 kDa |
| UniProt ID | Q8N907 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Secreted |
| 蛋白大小 | 8/10 | x1 | 8 | 189 aa / 20.2 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=47 篇 (<=60->6) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Secreted | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 66 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Regulatory rewiring of Dand5 drove left-right organizer heterotopy and organ asymmetry evolution in chordates.. *Proc Natl Acad Sci U S A*. PMID: 42154548
2. Ccdc57 regulates cilia and left-right patterning in Xenopus.. *Biol Open*. PMID: 41758249
3. m(6)A methylation inhibits recruitment of the Dand5 3'UTR to the left-right determinant Bicc1.. *RNA*. PMID: 40634109
4. CIROZ is dispensable in ancestral vertebrates but essential for left-right patterning in humans.. *Am J Hum Genet*. PMID: 39753129
5. CACNA1G, A Heterotaxy Candidate Gene, Plays a Role in Ciliogenesis and Left-Right Patterning in Xenopus tropicalis.. *Genesis*. PMID: 40008628

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 32.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 19.6% |
| 低置信 (pLDDT<50) 占比 | 31.2% |
| 有序区域 (pLDDT>70) 占比 | 49.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 49.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CER1 | 0.000 | 0.000 | — |
| NODAL | 0.000 | 0.000 | — |
| GDF1 | 0.000 | 0.000 | — |
| PKD1L1 | 0.000 | 0.000 | — |
| LEFTY2 | 0.000 | 0.000 | — |
| GREM2 | 0.000 | 0.000 | — |
| TDGF1 | 0.000 | 0.000 | — |
| CERS6 | 0.000 | 0.000 | — |
| CFC1 | 0.000 | 0.000 | — |
| PITX2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N907 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 1
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 无 | pLDDT=69.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Mitochondria | 一致 |
| PPI | STRING + IntAct | 25 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DAND5 -- DAN domain family member 5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N907
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179284-DAND5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAND5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N907
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N907-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
