---
type: protein-evaluation
gene: "WDR17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR17 |
| 蛋白名称 | WD repeat-containing protein 17 |
| 蛋白大小 | 1322 aa / 147.7 kDa |
| UniProt ID | Q8IZU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1322 aa / 147.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011047, IPR015943, IPR020472, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cloning and characterization of WDR17, a novel WD repeat-containing gene on chromosome 4q34.. *Biochimica et biophysica acta*. PMID: 12401215
2. Wdr17 Regulates Cell Proliferation, Cell Cycle Progression and Apoptosis in Mouse Spermatocyte Cell Line.. *Animals : an open access journal from MDPI*. PMID: 38791636
3. Evaluating of Gene Expression Alteration after Garlic Consumption, Analyzing through Bioinformatics Approach.. *Iranian journal of pharmaceutical research : IJPR*. PMID: 34400942
4. Methylation of CpG island promoters at ZNF625, LONRF2, SDC2 and WDR17 in a patient with numerous non-granular type laterally spreading tumors and colorectal cancer: A case report.. *Oncology letters*. PMID: 36478906
5. Concurrent Mutations in ATM and Genes Associated with Common γ Chain Signaling in Peripheral T Cell Lymphoma.. *PloS one*. PMID: 26536348

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 36.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 89.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.4，有序区 89.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011047, IPR015943, IPR020472, IPR019775, IPR036322; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRWD1 | 0.867 | 0.000 | — |
| NOC2L | 0.853 | 0.189 | — |
| RPF2 | 0.845 | 0.240 | — |
| GTPBP4 | 0.843 | 0.093 | — |
| BRIX1 | 0.836 | 0.415 | — |
| WDR3 | 0.815 | 0.000 | — |
| SDAD1 | 0.801 | 0.000 | — |
| EBNA1BP2 | 0.792 | 0.234 | — |
| MRTO4 | 0.763 | 0.071 | — |
| TSR1 | 0.761 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| WHAMMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RSPH1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| MET | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35384245|imex:IM-29494 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 无 | pLDDT=85.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDR17 — WD repeat-containing protein 17，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1322 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150627-WDR17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
