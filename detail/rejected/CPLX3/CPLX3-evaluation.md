---
type: protein-evaluation
gene: "CPLX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPLX3 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPLX3 |
| 蛋白名称 | Complexin-3 |
| 蛋白大小 | 158 aa / 17.6 kDa |
| UniProt ID | Q8WVH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Synapse; Cell membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 158 aa / 17.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=74.6; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR008849; Pfam: PF05835 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Synapse; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytosol (GO:0005829)
- photoreceptor ribbon synapse (GO:0098684)
- presynaptic active zone membrane (GO:0048787)
- SNARE complex (GO:0031201)
- synaptic vesicle membrane (GO:0030672)
- terminal bouton (GO:0043195)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 39 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The SNARE regulator Complexin3 is a target of the cone circadian clock.. *The Journal of comparative neurology*. PMID: 32783205
2. Molecular diversity of early-born subplate neurons.. *Cerebral cortex (New York, N.Y. : 1991)*. PMID: 22628460
3. A multifaceted architectural framework of the mouse claustrum complex.. *The Journal of comparative neurology*. PMID: 37782702
4. Global Gene Knockout of Kcnip3 Enhances Pain Sensitivity and Exacerbates Negative Emotions in Rats.. *Frontiers in molecular neuroscience*. PMID: 30740043
5. Epigenome-wide association analysis of daytime sleepiness in the Multi-Ethnic Study of Atherosclerosis reveals African-American-specific associations.. *Sleep*. PMID: 31139831

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 48.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 69.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.6，有序区 69.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008849; Pfam: PF05835 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPLX1 | 0.972 | 0.104 | — |
| VAMP1 | 0.941 | 0.094 | — |
| SNAP25 | 0.931 | 0.099 | — |
| CPLX2 | 0.929 | 0.096 | — |
| STX1A | 0.915 | 0.094 | — |
| CPLX4 | 0.904 | 0.000 | — |
| STX3 | 0.852 | 0.091 | — |
| VAMP2 | 0.701 | 0.096 | — |
| LMAN1L | 0.659 | 0.000 | — |
| STX1B | 0.643 | 0.094 | — |

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
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 无 | pLDDT=74.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Synapse; Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CPLX3 -- Complexin-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213578-CPLX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPLX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WVH0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
