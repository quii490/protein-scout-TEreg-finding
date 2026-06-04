---
type: protein-evaluation
gene: "SERGEF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERGEF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERGEF / DELGEF, GNEFR |
| 蛋白名称 | Secretion-regulating guanine nucleotide exchange factor |
| 蛋白大小 | 458 aa / 49.0 kDa |
| UniProt ID | Q9UGK8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 458 aa / 49.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR058923, IPR009091, IPR000408, IPR051625; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DELGEF, GNEFR |

**关键文献**:
1. Aberrantly Methylated-Differentially Expressed Genes Identify Novel Atherosclerosis Risk Subtypes.. *Frontiers in genetics*. PMID: 33381146
2. Genome-Wide Association Study of First-Parity Reproductive Traits in Suzi Pig.. *Genes*. PMID: 41300787
3. A robust biomarker of differential correlations improves the diagnosis of cytologically indeterminate thyroid cancers.. *International journal of molecular medicine*. PMID: 27035928
4. Genome-wide admixture and association study of subclinical atherosclerosis in the Women's Interagency HIV Study (WIHS).. *PloS one*. PMID: 29206233
5. Admixture Mapping of Subclinical Atherosclerosis and Subsequent Clinical Events Among African Americans in 2 Large Cohort Studies.. *Circulation. Cardiovascular genetics*. PMID: 28408707

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 72.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 81.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.2，有序区 81.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR058923, IPR009091, IPR000408, IPR051625; Pfam: PF25390 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPH3 | 0.999 | 0.984 | — |
| EXOC2 | 0.912 | 0.510 | — |
| USH1C | 0.772 | 0.068 | — |
| EEF2 | 0.684 | 0.000 | — |
| PRMT6 | 0.587 | 0.292 | — |
| RABIF | 0.576 | 0.000 | — |
| HEATR9 | 0.571 | 0.000 | — |
| CCDC115 | 0.563 | 0.000 | — |
| DPH2 | 0.553 | 0.000 | — |
| SAAL1 | 0.543 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DPH3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14980502 |
| EXOC2 | psi-mi:"MI:0096"(pull down) | pubmed:14980502 |
| PITX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FOXH1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPAG8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HGS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NUDCD2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| BLOC1S5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BFAR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLXNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 无 | pLDDT=85.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. SERGEF — Secretion-regulating guanine nucleotide exchange factor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小458 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UGK8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129158-SERGEF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERGEF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UGK8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
