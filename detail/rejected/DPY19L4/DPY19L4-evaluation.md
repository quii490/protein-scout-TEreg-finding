---
type: protein-evaluation
gene: "DPY19L4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPY19L4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPY19L4 |
| 蛋白名称 | Probable C-mannosyltransferase DPY19L4 |
| 蛋白大小 | 723 aa / 83.8 kDa |
| UniProt ID | Q7Z388 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPY19L4/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPY19L4/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 723 aa / 83.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018732, IPR047464; Pfam: PF10034 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Potential Protective Effect of Carotid Endarterectomy: Inducing Ischemic Tolerance in Brain Tissue after Stroke.. *Journal of molecular neuroscience : MN*. PMID: 41632392
2. Identifying Key Epigenetic Modification-Related Genes for Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma and Cellular Validation.. *Current gene therapy*. PMID: 41293945

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 59.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 86.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018732, IPR047464; Pfam: PF10034 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMTC3 | 0.581 | 0.000 | — |
| GK5 | 0.546 | 0.000 | — |
| TMEM9B | 0.543 | 0.000 | — |
| FAM131A | 0.540 | 0.000 | — |
| FKTN | 0.536 | 0.000 | — |
| CCNQ | 0.535 | 0.000 | — |
| NOC4L | 0.531 | 0.000 | — |
| VWA7 | 0.528 | 0.000 | — |
| TMTC4 | 0.520 | 0.000 | — |
| SLC45A1 | 0.507 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
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
1. DPY19L4 — Probable C-mannosyltransferase DPY19L4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小723 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z388
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156162-DPY19L4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPY19L4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z388
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:19:40

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z388-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
