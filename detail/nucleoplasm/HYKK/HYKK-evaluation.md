---
type: protein-evaluation
gene: "HYKK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HYKK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HYKK / AGPHD1 |
| 蛋白名称 | Hydroxylysine kinase |
| 蛋白大小 | 373 aa / 41.9 kDa |
| UniProt ID | A2RU49 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles, Aggresome, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 41.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002575, IPR011009, IPR050249; Pfam: PF01636 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles, Aggresome, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AGPHD1 |

**关键文献**:
1. Systematic druggable genome-wide Mendelian randomization identifies therapeutic targets for lung cancer.. *BMC cancer*. PMID: 38834983
2. Effect of smoking cessation medications on intracranial aneurysm risk: A Mendelian randomization study.. *Tobacco induced diseases*. PMID: 38690207
3. Transcriptomic profiles of the ruminal wall in Italian Mediterranean dairy buffaloes fed green forage.. *BMC genomics*. PMID: 36941576
4. Polymorphism of prion protein gene (PRNP) in Nigerian sheep.. *Prion*. PMID: 36892181
5. Multiomic Mendelian randomization analysis of metabolic gene methylation expression and protein levels in lung adenocarcinoma.. *Discover oncology*. PMID: 41021077

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 88.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.5，有序区 94.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002575, IPR011009, IPR050249; Pfam: PF01636 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PHYKPL | 0.995 | 0.074 | — |
| ETNPPL | 0.932 | 0.074 | — |
| PSMA4 | 0.889 | 0.000 | — |
| CHRNA3 | 0.784 | 0.000 | — |
| AGXT2 | 0.780 | 0.074 | — |
| IREB2 | 0.771 | 0.080 | — |
| CHRNA5 | 0.758 | 0.000 | — |
| CHRNB4 | 0.702 | 0.000 | — |
| OSGEP | 0.637 | 0.628 | — |
| CLPTM1L | 0.611 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DDB2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EIF3B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LAGE3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GMCL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OSGEP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLJ13057 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MTA1-like | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| TRIP6 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| Syn2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| CG17159 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 无 | pLDDT=93.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Vesicles, Aggresome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HYKK — Hydroxylysine kinase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A2RU49
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188266-HYKK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HYKK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2RU49
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
