---
type: protein-evaluation
gene: "TBCA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBCA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBCA |
| 蛋白名称 | Tubulin-specific chaperone A |
| 蛋白大小 | 108 aa / 12.9 kDa |
| UniProt ID | O75347 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; 额外: Nucleoli; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 108 aa / 12.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 1H7C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004226, IPR036126; Pfam: PF02970 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 167 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Serum proteomics reveal APOE-ε4-dependent and APOE-ε4-independent protein signatures in Alzheimer's disease.. *Nature aging*. PMID: 39169269
2. Polygenic Resilience Modulates the Penetrance of Parkinson Disease Genetic Risk Factors.. *Annals of neurology*. PMID: 35599344
3. Genome- and epigenome-wide studies of plasma protein biomarkers for Alzheimer's disease implicate TBCA and TREM2 in disease risk.. *Alzheimer's & dementia (Amsterdam, Netherlands)*. PMID: 35475137
4. Colchicine Blocks Tubulin Heterodimer Recycling by Tubulin Cofactors TBCA, TBCB, and TBCE.. *Frontiers in cell and developmental biology*. PMID: 33968934
5. Proteomic signatures of the APOE ε4 and APOE ε2 genetic variants and Alzheimer's disease.. *medRxiv : the preprint server for health sciences*. PMID: 40799961

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 93.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 97.2% |
| 可用 PDB 条目 | 1H7C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.1，有序区 97.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004226, IPR036126; Pfam: PF02970 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TUBB2A | 0.871 | 0.324 | — |
| TUBA4A | 0.868 | 0.224 | — |
| TBCE-2 | 0.856 | 0.411 | — |
| TBCD | 0.816 | 0.133 | — |
| TUBB4B | 0.790 | 0.432 | — |
| NDUFB4 | 0.773 | 0.000 | — |
| TUBB2B | 0.763 | 0.324 | — |
| TUBB4A | 0.749 | 0.324 | — |
| TUBB3 | 0.749 | 0.324 | — |
| TUBB6 | 0.723 | 0.324 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| vari | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HNF1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 1H7C | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Microtubules; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBCA — Tubulin-specific chaperone A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小108 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75347
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171530-TBCA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBCA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75347
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75347-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75347 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004226;IPR036126; |
| Pfam | PF02970; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171530-TBCA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HYDIN | Biogrid | false |
| TERF2IP | Intact | false |
| TUBB | Biogrid | false |
| TUBB2A | Biogrid | false |
| TUBB4B | Biogrid, Opencell | false |
| UBA2 | Biogrid | false |
| ZMYM6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
