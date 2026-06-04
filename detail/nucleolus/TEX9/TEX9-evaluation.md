---
type: protein-evaluation
gene: "TEX9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX9 |
| 蛋白名称 | Testis-expressed protein 9 |
| 蛋白大小 | 391 aa / 44.8 kDa |
| UniProt ID | Q8N6V9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Primary cilium, Centrosome, Cytosol; 额外: Nucleoplasm, Nucleo; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 44.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Primary cilium, Centrosome, Cytosol; 额外: Nucleoplasm, Nucleoli fibrillar center, Vesicles, Basal body | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Scrutinizing the human TEX genes in the context of human male infertility.. *Andrology*. PMID: 37594251
2. Insights into Ciliary Genes and Evolution from Multi-Level Phylogenetic Profiling.. *Molecular biology and evolution*. PMID: 28460059
3. An unbiased in vivo functional genomics screening approach in mice identifies novel tumor cell-based regulators of immune rejection.. *Cancer immunology, immunotherapy : CII*. PMID: 28770278
4. Insights into Human Ciliopathies: Gene Silencing of ropn1l and tex9 in Schmidtea mediterranea Indicate Association with Ciliary Structure and Motility.. *microPublication biology*. PMID: 42079374
5. The Functionally Unannotated Proteome of Human Male Tissues: A Shared Resource to Uncover New Protein Functions Associated with Reproductive Biology.. *Journal of proteome research*. PMID: 33064489

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.2% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 23.8% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.8，有序区 64.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC112 | 0.869 | 0.698 | — |
| NOL4L | 0.738 | 0.738 | — |
| CCDC14 | 0.692 | 0.421 | — |
| NOL4 | 0.669 | 0.669 | — |
| CCDC148 | 0.631 | 0.545 | — |
| C10orf88 | 0.556 | 0.000 | — |
| FAXC | 0.542 | 0.000 | — |
| CCDC60 | 0.542 | 0.000 | — |
| SPAG17 | 0.507 | 0.000 | — |
| CCDC13 | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC112 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Srp68 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| anon-WO0140519.45 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| NimC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pka-R1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "BcDNA:RE67729" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sinah | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TXNDC9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GSTA5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NOL4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 无 | pLDDT=77.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Primary cilium, Centrosome, Cytosol; 额外: Nucleopla | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TEX9 — Testis-expressed protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6V9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151575-TEX9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6V9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
