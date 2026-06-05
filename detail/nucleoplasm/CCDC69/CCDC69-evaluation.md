---
type: protein-evaluation
gene: "CCDC69"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC69 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC69 |
| 蛋白名称 | Coiled-coil domain-containing protein 69 |
| 蛋白大小 | 296 aa / 34.8 kDa |
| UniProt ID | A6NI79 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Golgi apparatus, Actin filaments; UniProt: Cytoplasm, cytoskeleton, spindle; Midbody |
| 蛋白大小 | 10/10 | ×1 | 10 | 296 aa / 34.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051293 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus, Actin filaments | Approved |
| UniProt | Cytoplasm, cytoskeleton, spindle; Midbody | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- midbody (GO:0030496)
- nucleus (GO:0005634)
- spindle midzone (GO:0051233)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcriptomic analysis reveals the potential crosstalk genes and immune relationship between IgA nephropathy and periodontitis.. *Frontiers in immunology*. PMID: 36793719
2. RNA-Seq transcriptome profiling identifies CRISPLD2 as a glucocorticoid responsive gene that modulates cytokine function in airway smooth muscle cells.. *PloS one*. PMID: 24926665
3. Overexpression of CCDC69 activates p14(ARF)/MDM2/p53 pathway and confers cisplatin sensitivity.. *Journal of ovarian research*. PMID: 30651135
4. CCDC69 is a prognostic marker of breast cancer and correlates with tumor immune cell infiltration.. *Frontiers in surgery*. PMID: 35910470
5. Role of a novel coiled-coil domain-containing protein CCDC69 in regulating central spindle assembly.. *Cell cycle (Georgetown, Tex.)*. PMID: 20962590

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 13.2% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 75.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051293 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RMI2 | 0.706 | 0.656 | — |
| RMI1 | 0.605 | 0.605 | — |
| ARMCX2 | 0.490 | 0.000 | — |
| LRRC17 | 0.454 | 0.000 | — |
| RCSD1 | 0.442 | 0.000 | — |
| FAM219B | 0.428 | 0.000 | — |
| PAIP2 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACO1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2N | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| PMPCB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MTA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GGPS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LONP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, spindle; Midbody / Plasma membrane; 额外: Golgi apparatus, Actin filame | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

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
1. CCDC69 — Coiled-coil domain-containing protein 69，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小296 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NI79
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198624-CCDC69/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC69
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NI79
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NI79-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
