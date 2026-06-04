---
type: protein-evaluation
gene: "EXOC3L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXOC3L — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC3L / EXOC3L |
| 蛋白名称 | Exocyst complex component 3-like protein |
| 蛋白大小 | 746 aa / 81.7 kDa |
| UniProt ID | Q86VI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles, Plasma membrane; UniProt: Cytoplasmic vesicle, secretory vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 746 aa / 81.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010326, IPR042532; Pfam: PF06046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- exocyst (GO:0000145)
- secretory granule (GO:0030141)
- transport vesicle (GO:0030133)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EXOC3L |

**关键文献**:
1. Genome-wide DNA methylation analysis of human pancreatic islets from type 2 diabetic and non-diabetic donors identifies candidate genes that influence insulin secretion.. *PLoS genetics*. PMID: 24603685
2. Involvement of Exoc3l, a protein structurally related to the exocyst subunit Sec6, in insulin secretion.. *Biomedical research (Tokyo, Japan)*. PMID: 18480549
3. Null mutation of exocyst complex component 3-like does not affect vascular development in mice.. *Experimental animals*. PMID: 37661429

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.3% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 90.9% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.0，有序区 90.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010326, IPR042532; Pfam: PF06046 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC2 | 0.980 | 0.869 | — |
| EXOC4 | 0.969 | 0.867 | — |
| EXOC1 | 0.968 | 0.903 | — |
| EXOC5 | 0.965 | 0.842 | — |
| EXOC8 | 0.921 | 0.594 | — |
| EXOC7 | 0.908 | 0.640 | — |
| EXOC6 | 0.879 | 0.615 | — |
| EXOC6B | 0.861 | 0.615 | — |
| EXOC1L | 0.794 | 0.491 | — |
| EXOC3L2 | 0.726 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOC3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LDB2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CEACAM6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HGS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYOD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT27 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 无 | pLDDT=87.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle / Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EXOC3L — Exocyst complex component 3-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小746 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179044-EXOC3L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
