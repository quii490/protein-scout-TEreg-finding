---
type: protein-evaluation
gene: "COTL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COTL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COTL1 / CLP |
| 蛋白名称 | Coactosin-like protein |
| 蛋白大小 | 142 aa / 15.9 kDa |
| UniProt ID | Q14019 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 142 aa / 15.9 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=90.4; PDB: 1T2L, 1T3X, 1T3Y, 1TMW, 1VFQ, 1WNJ |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR002108, IPR029006; Pfam: PF00241 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cortical actin cytoskeleton (GO:0030864)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleus (GO:0005634)
- secretory granule lumen (GO:0034774)
- site of polarized growth (GO:0030427)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLP |

**关键文献**:
1. Machine learning algorithms integrate bulk and single-cell RNA data to unveil oxidative stress following intracerebral hemorrhage.. *International immunopharmacology*. PMID: 38865753
2. Coactosin-like F-actin binding protein (Cotl1) plays a key role in adipocyte differentiation and obesity.. *Communications biology*. PMID: 40246959
3. Coactosin-like 1 integrates signaling critical for shear-dependent thrombus formation in mouse platelets.. *Haematologica*. PMID: 31582545
4. Coactosin-Like Protein (COTL1) Promotes Glioblastoma (GBM) Growth in vitro and in vivo.. *Cancer management and research*. PMID: 33154670
5. Coactosin-Like Protein in Breast Carcinoma: Friend or Foe?. *Journal of inflammation research*. PMID: 35873386

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 81.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 1T2L, 1T3X, 1T3Y, 1TMW, 1VFQ, 1WNJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=90.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002108, IPR029006; Pfam: PF00241 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALOX5 | 0.989 | 0.816 | — |
| ALOX5AP | 0.796 | 0.000 | — |
| LTA4H | 0.682 | 0.000 | — |
| ACTB | 0.645 | 0.359 | — |
| CAP1 | 0.634 | 0.495 | — |
| CFL1 | 0.582 | 0.204 | — |
| ACTG1 | 0.567 | 0.359 | — |
| MEAK7 | 0.564 | 0.000 | — |
| TAGLN2 | 0.562 | 0.283 | — |
| CAP2 | 0.561 | 0.495 | — |

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
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 1T2L, 1T3X, 1T3Y, 1TMW, 1VFQ,  | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COTL1 -- Coactosin-like protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小142 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14019
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103187-COTL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COTL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14019
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14019-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14019 |
| SMART | SM00102; |
| UniProt Domain [FT] | DOMAIN 2..130; /note="ADF-H"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00599" |
| InterPro | IPR002108;IPR029006; |
| Pfam | PF00241; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103187-COTL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOX5 | Intact, Biogrid | true |
| PDE6H | Intact | false |
| TERF2IP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
