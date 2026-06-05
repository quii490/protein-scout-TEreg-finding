---
type: protein-evaluation
gene: "DBX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DBX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DBX1 |
| 蛋白名称 | Homeobox protein DBX1 |
| 蛋白大小 | 343 aa / 37.3 kDa |
| UniProt ID | A6NMT0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 37.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051662, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular and behavioral profiling of Dbx1-derived neurons in the arcuate, lateral and ventromedial hypothalamic nuclei.. *Neural development*. PMID: 27209204
2. Dbx1 is a dorsal midbrain-specific determinant of GABAergic neuron fate and regulates differentiation of the dorsal midbrain into the inferior and superior colliculi.. *Frontiers in cell and developmental biology*. PMID: 38344749
3. Diversity within olfactory sensory derivatives revealed by the contribution of Dbx1 lineages.. *The Journal of comparative neurology*. PMID: 37125418
4. The embryonic patterning gene Dbx1 governs the survival of the auditory midbrain via Tcf7l2-Ap2δ transcriptional cascade.. *Cell death and differentiation*. PMID: 37081114
5. Fate mapping neurons and glia derived from Dbx1-expressing progenitors in mouse preBötzinger complex.. *Physiological reports*. PMID: 28611151

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 49.9% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 23.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 23.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051662, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OLIG2 | 0.646 | 0.000 | — |
| LHX6 | 0.641 | 0.104 | — |
| LHX2 | 0.622 | 0.104 | — |
| OLIG3 | 0.609 | 0.000 | — |
| LHX5 | 0.599 | 0.104 | — |
| NEUROG2 | 0.596 | 0.000 | — |
| SHH | 0.593 | 0.000 | — |
| IRX3 | 0.590 | 0.065 | — |
| TBR1 | 0.560 | 0.071 | — |
| LHX9 | 0.551 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| EBI-9975278 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| TNFSF14 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 无 | pLDDT=61.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DBX1 — Homeobox protein DBX1，非常新颖，仅有少数基础研究。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NMT0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109851-DBX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DBX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NMT0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NMT0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
