---
type: protein-evaluation
gene: "C6orf136"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C6orf136 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C6orf136 |
| 蛋白名称 | Uncharacterized protein C6orf136 |
| 蛋白大小 | 315 aa / 35.8 kDa |
| UniProt ID | Q5SQH8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 35.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018790; Pfam: PF10184 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A novel cuproptosis-related gene model predicts outcomes and treatment responses in pancreatic adenocarcinoma.. *BMC cancer*. PMID: 36894917
2. Identification of FOXM1-induced epigenetic markers for head and neck squamous cell carcinomas.. *Cancer*. PMID: 24114764
3. Single-cell and bulk transcriptomic analyses uncover immune subtypes associated with programmed cell death features in intrahepatic cholangiocarcinoma.. *Scientific reports*. PMID: 41840103
4. Identification of immune-related mitochondrial metabolic disorder genes in septic shock using bioinformatics and machine learning.. *Hereditas*. PMID: 39609718
5. Identification of key genes in cuproptosis during acute kidney injury through weighted gene co-expression network analysis.. *Medicine*. PMID: 41137350

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 25.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 45.1% |
| 有序区域 (pLDDT>70) 占比 | 40.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 40.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018790; Pfam: PF10184 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C11orf16 | 0.542 | 0.000 | — |
| GLT8D1 | 0.539 | 0.000 | — |
| NRM | 0.529 | 0.000 | — |
| GNL1 | 0.521 | 0.000 | — |
| PAFAH1B3 | 0.516 | 0.000 | — |
| ABCF1 | 0.514 | 0.000 | — |
| C12orf56 | 0.477 | 0.000 | — |
| TCF19 | 0.470 | 0.000 | — |
| GTF2H4 | 0.463 | 0.000 | — |
| SPCS1 | 0.435 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rbm8a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KIF21A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MPZL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAP1S | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KIAA0232 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RNF126 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 6
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 无 | pLDDT=61.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 14 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C6orf136 — Uncharacterized protein C6orf136，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5SQH8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204564-C6orf136/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C6orf136
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5SQH8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5SQH8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
