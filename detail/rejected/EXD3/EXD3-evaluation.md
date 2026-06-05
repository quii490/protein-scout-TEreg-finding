---
type: protein-evaluation
gene: "EXD3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXD3 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXD3 |
| 蛋白名称 | Exonuclease mut-7 homolog |
| 蛋白大小 | 876 aa / 96.6 kDa |
| UniProt ID | Q8N9H8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Focal adhesion sites; 额外: Actin filaments; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 876 aa / 96.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002562, IPR052408, IPR037432, IPR002782, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites; 额外: Actin filaments | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Modelling G protein-biased agonism using GLP-1 receptor C-terminal mutations.. *Molecular metabolism*. PMID: 41570980
2. Identification of Novel, Replicable Genetic Risk Loci for Suicidal Thoughts and Behaviors Among US Military Veterans.. *JAMA psychiatry*. PMID: 36515925
3. A new Caenorhabditis elegans apurinic/apyrimidinic (AP) endonuclease engaged in rescue from replication stress-induced arrest.. *Genetics and molecular biology*. PMID: 41183359
4. [Bioinformatics analysis of expression and function of EXD3 gene in gastric cancer].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 30890511
5. Genome-wide association study identifies four pan-ancestry loci for suicidal ideation in the Million Veteran Program.. *PLoS genetics*. PMID: 36940203

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 39.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 79.8% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 79.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002562, IPR052408, IPR037432, IPR002782, IPR012337; Pfam: PF01612, PF01927 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZFYVE28 | 0.705 | 0.000 | — |
| ZNF678 | 0.687 | 0.091 | — |
| RBM46 | 0.645 | 0.000 | — |
| RECQL | 0.593 | 0.000 | — |
| EXO1 | 0.582 | 0.042 | — |
| POLD2 | 0.581 | 0.000 | — |
| EXD1 | 0.569 | 0.000 | — |
| DNA2 | 0.556 | 0.057 | — |
| POLD1 | 0.543 | 0.047 | — |
| DAZAP2 | 0.533 | 0.420 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9NX53 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| GASK1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMBIM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PSME4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Focal adhesion sites; 额外: Actin filaments | 待确认 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EXD3 — Exonuclease mut-7 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小876 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9H8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187609-EXD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9H8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N9H8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
