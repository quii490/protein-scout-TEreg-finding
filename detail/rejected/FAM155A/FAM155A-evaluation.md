---
type: protein-evaluation
gene: "FAM155A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM155A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM155A / FAM155A, NLF-1 |
| 蛋白名称 | NALCN channel auxiliary factor 1 |
| 蛋白大小 | 458 aa / 51.5 kDa |
| UniProt ID | B1AL88 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 458 aa / 51.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 6XIW, 7CM3, 7SX3, 7SX4, 7WJI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055288 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM155A, NLF-1 |

**关键文献**:
1. A new neurodevelopmental disorder linked to heterozygous variants in UNC79.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 37183800
2. Differential chromatin accessibility and transcriptional dynamics define breast cancer subtypes and their lineages.. *Nature cancer*. PMID: 39478117
3. Dysregulated synaptic gene expression in oligodendrocytes of spinal and bulbar muscular atrophy.. *JCI insight*. PMID: 40548375
4. COLQ and ARHGAP15 are Associated with Diverticular Disease and are Expressed in the Colon.. *The Journal of surgical research*. PMID: 34225052
5. Sequence variants in ARHGAP15, COLQ and FAM155A associate with diverticular disease and diverticulitis.. *Nature communications*. PMID: 28585551

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 7.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.4% |
| 低置信 (pLDDT<50) 占比 | 39.1% |
| 有序区域 (pLDDT>70) 占比 | 39.5% |
| 可用 PDB 条目 | 6XIW, 7CM3, 7SX3, 7SX4, 7WJI |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 39.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055288 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NALCN | 0.981 | 0.918 | — |
| UNC79 | 0.968 | 0.822 | — |
| UNC80 | 0.958 | 0.812 | — |
| CALM3 | 0.809 | 0.800 | — |
| CALM2 | 0.806 | 0.800 | — |
| ARHGAP15 | 0.583 | 0.000 | — |
| COLQ | 0.575 | 0.000 | — |
| PHGR1 | 0.544 | 0.000 | — |
| TAFA2 | 0.537 | 0.000 | — |
| LAMB4 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rabac1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:30925931|imex:IM-26645 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 1
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 6XIW, 7CM3, 7SX3, 7SX4, 7WJI | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM155A — NALCN channel auxiliary factor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小458 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B1AL88
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204442-NALF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM155A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B1AL88
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-B1AL88-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
