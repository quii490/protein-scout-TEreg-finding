---
type: protein-evaluation
gene: "TRAPPC13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAPPC13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAPPC13 / C5orf44 |
| 蛋白名称 | Trafficking protein particle complex subunit 13 |
| 蛋白大小 | 417 aa / 46.5 kDa |
| UniProt ID | A5PLN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 417 aa / 46.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010378, IPR055428, IPR055429, IPR055427; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- TRAPPII protein complex (GO:1990071)
- TRAPPIII protein complex (GO:1990072)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C5orf44 |

**关键文献**:
1. TRAPPC13 modulates autophagy and the response to Golgi stress.. *Journal of cell science*. PMID: 28536105
2. Biochemical Insight into Novel Rab-GEF Activity of the Mammalian TRAPPIII Complex.. *Journal of molecular biology*. PMID: 34229011
3. TRAPPC13 Is a Novel Target of Mesorhizobium amorphae Type III Secretion System Effector NopP.. *Molecular plant-microbe interactions : MPMI*. PMID: 33630651
4. Machine Learning Identifies TRAPPC13/COPS5 as Biomarkers and Vesicle Transport Subtypes in Parkinson's Disease.. *The Canadian journal of neurological sciences. Le journal canadien des sciences neurologiques*. PMID: 41972297
5. Characterization of Aspergillus nidulans TRAPPs uncovers unprecedented similarities between fungi and metazoans and reveals the modular assembly of TRAPPII.. *PLoS genetics*. PMID: 31869332

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.7 |
| 高置信度残基 (pLDDT>90) 占比 | 58.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 89.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.7，有序区 89.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010378, IPR055428, IPR055429, IPR055427; Pfam: PF23643, PF23647, PF06159 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAPPC12 | 0.998 | 0.811 | — |
| TRAPPC8 | 0.996 | 0.292 | — |
| TRAPPC11 | 0.996 | 0.496 | — |
| TRAPPC1 | 0.992 | 0.819 | — |
| TRAPPC2L | 0.987 | 0.684 | — |
| TRAPPC5 | 0.985 | 0.705 | — |
| TRAPPC2 | 0.983 | 0.692 | — |
| TRAPPC6B | 0.983 | 0.610 | — |
| TRAPPC9 | 0.977 | 0.124 | — |
| TRAPPC3 | 0.974 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PP2AA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| EBI-2845318 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TRAPPC2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18685|pubmed:21453443 |
| TRAPPC8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18685|pubmed:21453443 |
| TRAPPC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18685|pubmed:21453443 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| - | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TBC1D14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.7 + PDB: 无 | pLDDT=86.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRAPPC13 — Trafficking protein particle complex subunit 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小417 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A5PLN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113597-TRAPPC13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAPPC13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A5PLN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
