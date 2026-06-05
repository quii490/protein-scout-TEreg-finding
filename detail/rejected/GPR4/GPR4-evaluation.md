---
type: protein-evaluation
gene: "GPR4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR4 |
| 蛋白名称 | G-protein coupled receptor 4 |
| 蛋白大小 | 362 aa / 41.0 kDa |
| UniProt ID | P46093 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 362 aa / 41.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.7; PDB: 8Z3M, 8Z3Q, 8Z3Y, 8Z65, 8Z66, 8Z67, 8ZCE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR002276; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 51.4% |
| 置信残基 (pLDDT 70-90) 占比 | 26.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 15.7% |
| 有序区域 (pLDDT>70) 占比 | 77.6% |
| 可用 PDB 条目 | 8Z3M, 8Z3Q, 8Z3Y, 8Z65, 8Z66, 8Z67, 8ZCE, 8ZCF, 9BIP, 9JFV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8Z3M, 8Z3Q, 8Z3Y, 8Z65, 8Z66, 8Z67, 8ZCE, 8ZCF, 9BIP, 9JFV）+ AlphaFold极高置信度预测（pLDDT=80.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR002276; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAP3K4 | 0.761 | 0.045 | — |
| LPAR1 | 0.691 | 0.000 | — |
| CGA | 0.674 | 0.000 | — |
| GPR132 | 0.654 | 0.000 | — |
| KCNK5 | 0.578 | 0.045 | — |
| GRK2 | 0.570 | 0.097 | — |
| GPR3 | 0.555 | 0.000 | — |
| GPR39 | 0.553 | 0.000 | — |
| RAMP3 | 0.544 | 0.000 | — |
| GRK5 | 0.541 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 8Z3M, 8Z3Q, 8Z3Y, 8Z65, 8Z66,  | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR4 — G-protein coupled receptor 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小362 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46093
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177464-GPR4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46093
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46093-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
