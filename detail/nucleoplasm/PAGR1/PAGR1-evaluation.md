---
type: protein-evaluation
gene: "PAGR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAGR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAGR1 / C16orf53, PA1 |
| 蛋白名称 | PAXIP1-associated glutamate-rich protein 1 |
| 蛋白大小 | 254 aa / 27.7 kDa |
| UniProt ID | Q9BTK6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 254 aa / 27.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028213; Pfam: PF15364 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- histone methyltransferase complex (GO:0035097)
- MLL3/4 complex (GO:0044666)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf53, PA1 |

**关键文献**:
1. Glucose-Responsive PAGR1-Regulated Skeletal Muscle Gene Program Controls Systemic Glucose Homeostasis and Hepatic Metabolism.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40703063
2. CRISPR screens in sister chromatid cohesion defective cells reveal PAXIP1-PAGR1 as regulator of chromatin association of cohesin.. *Nucleic acids research*. PMID: 37702151
3. A STAG2-PAXIP1/PAGR1 axis suppresses lung tumorigenesis.. *The Journal of experimental medicine*. PMID: 39652422
4. Overlapping and Distinct Functions of the Paralogous PagR Regulators of Bacillus anthracis.. *Journal of bacteriology*. PMID: 36005808
5. A STAG2-PAXIP1/PAGR1 axis suppresses lung tumorigenesis.. *bioRxiv : the preprint server for biology*. PMID: 39345539

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 37.4% |
| 低置信 (pLDDT<50) 占比 | 31.1% |
| 有序区域 (pLDDT>70) 占比 | 31.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 31.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028213; Pfam: PF15364 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAXIP1 | 0.999 | 0.824 | — |
| KDM6A | 0.997 | 0.757 | — |
| WDR5 | 0.996 | 0.667 | — |
| DPY30 | 0.996 | 0.503 | — |
| KMT2C | 0.995 | 0.603 | — |
| ASH2L | 0.994 | 0.540 | — |
| RBBP5 | 0.994 | 0.596 | — |
| NCOA6 | 0.987 | 0.592 | — |
| KMT2D | 0.985 | 0.739 | — |
| SETD1A | 0.746 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| SLX1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| WDR5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| KDM6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| QDPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAXIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TP53RK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NXT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PAGR1 — PAXIP1-associated glutamate-rich protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小254 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTK6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000280789-PAGR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAGR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTK6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BTK6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
