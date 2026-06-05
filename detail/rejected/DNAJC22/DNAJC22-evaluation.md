---
type: protein-evaluation
gene: "DNAJC22"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC22 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC22 |
| 蛋白名称 | DnaJ homolog subfamily C member 22 |
| 蛋白大小 | 341 aa / 38.1 kDa |
| UniProt ID | Q8N4W6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 341 aa / 38.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.7; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR036869, IPR007829; Pfam: PF00226, PF |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: Protein Atlas 中未找到该基因条目（无ENSG匹配），无法获取IF原图。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic Analysis of HSP40/DNAJ Family Genes in Parkinson's Disease: a Large Case-Control Study.. *Molecular neurobiology*. PMID: 35715682
2. Melocular Evolution on Cold Temperature Adaptation of Chinese Rhesus Macaques.. *Current genomics*. PMID: 39911280
3. Computational genome-wide identification of heat shock protein genes in the bovine genome.. *F1000Research*. PMID: 30542619
4. A cross-species approach to identify transcriptional regulators exemplified for Dnajc22 and Hnf4a.. *Scientific reports*. PMID: 28642491
5. Comprehensive Analysis of GDF10 Methylation Site-Associated Genes as Prognostic Markers for Endometrial Cancer.. *Journal of oncology*. PMID: 36262352

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.7 |
| 高置信度残基 (pLDDT>90) 占比 | 39.3% |
| 置信残基 (pLDDT 70-90) 占比 | 37.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.5% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.7，有序区 76.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR036869, IPR007829; Pfam: PF00226, PF05154 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC27 | 0.583 | 0.113 | — |
| HSPA4L | 0.574 | 0.142 | — |
| DNAJC24 | 0.571 | 0.000 | — |
| DNAJC18 | 0.559 | 0.000 | — |
| DNAJC28 | 0.557 | 0.000 | — |
| HSPA14-2 | 0.556 | 0.142 | — |
| DNAJC9 | 0.551 | 0.000 | — |
| HSPA12B | 0.550 | 0.142 | — |
| HSPA14 | 0.545 | 0.142 | — |
| LBX1 | 0.512 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 7 / 15 = 47%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 47%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.7 + PDB: 无 | pLDDT=81.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC22 — DnaJ homolog subfamily C member 22，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小341 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4W6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178401-DNAJC22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4W6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:06

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N4W6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
