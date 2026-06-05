---
type: protein-evaluation
gene: "HAUS7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HAUS7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAUS7 / UCHL5IP, UIP1 |
| 蛋白名称 | HAUS augmin-like complex subunit 7 |
| 蛋白大小 | 358 aa / 39.8 kDa |
| UniProt ID | Q99871 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Centrosome; 额外: Nucleoli, Basal body, Mid p; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 39.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=78.0; PDB: 7SQK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029711 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Centrosome; 额外: Nucleoli, Basal body, Mid piece, Principal piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- HAUS complex (GO:0070652)
- mitotic spindle microtubule (GO:1990498)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)
- sperm midpiece (GO:0097225)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UCHL5IP, UIP1 |

**关键文献**:
1. A prognostic model based on the Augmin family genes for LGG patients.. *Scientific reports*. PMID: 37161065
2. Chromosomal instability in women with primary ovarian insufficiency.. *Human reproduction (Oxford, England)*. PMID: 29425284
3. The dynamics of gene expression during and post meiosis sets the sperm agenda.. *Molecular reproduction and development*. PMID: 31589365
4. Current updates and future perspectives in the evaluation of azoospermia: A systematic review.. *Arab journal of urology*. PMID: 34552771
5. Identifying Biomarkers and Therapeutic Targets by Multiomic Analysis for HNSCC: Precision Medicine and Healthcare Management.. *ACS omega*. PMID: 38524437

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.3% |
| 置信残基 (pLDDT 70-90) 占比 | 38.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 69.8% |
| 可用 PDB 条目 | 7SQK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=78.0，有序区 69.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029711 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HAUS6 | 0.999 | 0.986 | — |
| HAUS5 | 0.999 | 0.967 | — |
| HAUS1 | 0.999 | 0.973 | — |
| HAUS2 | 0.999 | 0.988 | — |
| HAUS8 | 0.999 | 0.972 | — |
| HAUS4 | 0.998 | 0.965 | — |
| HAUS3 | 0.998 | 0.954 | — |
| UCHL5 | 0.859 | 0.292 | — |
| PSMD8 | 0.833 | 0.000 | — |
| TUBG1 | 0.816 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATF4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| Haus4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HAUS1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| BSG | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Vav1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ACOX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 7SQK | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Plasma membrane, Centrosome; 额外: Nucleoli, Basal b | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HAUS7 — HAUS augmin-like complex subunit 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99871
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213397-HAUS7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAUS7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99871
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000213397-HAUS7/subcellular

![](https://images.proteinatlas.org/3614/2120_D2_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/3614/2120_D2_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/3614/2128_G10_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/3614/2128_G10_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/3614/2167_H7_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/3614/2167_H7_52_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99871-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
