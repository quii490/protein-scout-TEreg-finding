---
type: protein-evaluation
gene: "CNKSR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNKSR1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNKSR1 / CNK1 |
| 蛋白名称 | Connector enhancer of kinase suppressor of ras 1 |
| 蛋白大小 | 720 aa / 79.7 kDa |
| UniProt ID | Q969H4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm; Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 720 aa / 79.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 1WWV |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR049628, IPR051566, IPR017874, IPR001478, IPR036 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cell-cell junction (GO:0005911)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.8% |
| 置信残基 (pLDDT 70-90) 占比 | 42.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 29.9% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |
| 可用 PDB 条目 | 1WWV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 58.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049628, IPR051566, IPR017874, IPR001478, IPR036034; Pfam: PF10534, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KSR1 | 0.941 | 0.144 | — |
| RASSF1 | 0.915 | 0.292 | — |
| RHPN1 | 0.847 | 0.292 | — |
| RALGDS | 0.835 | 0.292 | — |
| CYTH3 | 0.817 | 0.789 | — |
| RHOA | 0.794 | 0.566 | — |
| RAF1 | 0.769 | 0.360 | — |
| MAP3K10 | 0.697 | 0.085 | — |
| CYTH2 | 0.683 | 0.636 | — |
| CYTH1 | 0.675 | 0.626 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 1WWV | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNKSR1 -- Connector enhancer of kinase suppressor of ras 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小720 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969H4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142675-CNKSR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNKSR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969H4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969H4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
