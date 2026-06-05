---
type: protein-evaluation
gene: "RINL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RINL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RINL |
| 蛋白名称 | Ras and Rab interactor-like protein |
| 蛋白大小 | 566 aa / 62.5 kDa |
| UniProt ID | Q6ZS11 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cell projection, ruffle; Cytoplasmic vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 566 aa / 62.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036860, IPR003123, IPR045046, IPR037191; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cell projection, ruffle; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytosol (GO:0005829)
- endocytic vesicle (GO:0030139)
- ruffle (GO:0001726)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RINL, guanine nucleotide exchange factor Rab5-subfamily, is involved in the EphA8-degradation pathway with odin.. *PloS one*. PMID: 22291991
2. Molecular Atlas of PM(2.5) Chemical Constituents on Cardiac Conduction: A Multiomics Landscape in Older Adults.. *Environmental science & technology*. PMID: 41098063

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 24.4% |
| 置信残基 (pLDDT 70-90) 占比 | 32.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 56.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 56.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036860, IPR003123, IPR045046, IPR037191; Pfam: PF02204 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB5A | 0.818 | 0.098 | — |
| RABGEF1 | 0.707 | 0.000 | — |
| RIN3 | 0.632 | 0.292 | — |
| ALS2CL | 0.623 | 0.000 | — |
| ALS2 | 0.582 | 0.000 | — |
| GAPVD1 | 0.581 | 0.000 | — |
| RAB5C | 0.579 | 0.098 | — |
| RAB5B | 0.573 | 0.098 | — |
| EPHA8 | 0.536 | 0.064 | — |
| RIN1 | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1AKMT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32552912|imex:IM-28480 |
| SERPINB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RIPPLY3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NTHL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SUGP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MICAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FGFR1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| AATK | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| ANKRA2 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 无 | pLDDT=66.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, ruffle; Cytoplasmic vesicle / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RINL — Ras and Rab interactor-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小566 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZS11
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187994-RINL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RINL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZS11
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZS11-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
