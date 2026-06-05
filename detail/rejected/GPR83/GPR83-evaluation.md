---
type: protein-evaluation
gene: "GPR83"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR83 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR83 / GPR72, JP05, KIAA1540 |
| 蛋白名称 | G-protein coupled receptor 83 |
| 蛋白大小 | 423 aa / 48.3 kDa |
| UniProt ID | Q9NYM4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 48.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452, IPR000611; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- non-motile cilium (GO:0097730)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPR72, JP05, KIAA1540 |

**关键文献**:
1. Parallel ascending spinal pathways for affective touch and pain.. *Nature*. PMID: 33116307
2. Understanding the genetic complexity of puberty timing across the allele frequency spectrum.. *Nature genetics*. PMID: 38951643
3. Neuropeptide PEN and Its Receptor GPR83: Distribution, Signaling, and Regulation.. *ACS chemical neuroscience*. PMID: 30726666
4. Expression of Tacr1 and Gpr83 by spinal projection neurons.. *Molecular pain*. PMID: 40331673
5. Gpr83 Tunes Nociceptor Function, Controlling Pain.. *Neurotherapeutics : the journal of the American Society for Experimental NeuroTherapeutics*. PMID: 36352334

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 68.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR000611; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NPY | 0.970 | 0.000 | — |
| PYY | 0.909 | 0.000 | — |
| PPY | 0.901 | 0.000 | — |
| IRS4 | 0.900 | 0.049 | — |
| IRS2 | 0.900 | 0.049 | — |
| CHUK | 0.900 | 0.000 | — |
| IRS1 | 0.900 | 0.049 | — |
| IKBKB | 0.900 | 0.000 | — |
| GPR171 | 0.726 | 0.000 | — |
| ADCY3 | 0.714 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACVR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DDR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR83 — G-protein coupled receptor 83，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYM4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123901-GPR83/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYM4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYM4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
