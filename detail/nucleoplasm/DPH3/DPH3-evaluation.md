---
type: protein-evaluation
gene: "DPH3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPH3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPH3 |
| 蛋白名称 | Diphthamide biosynthesis protein 3 |
| 蛋白大小 | 82 aa / 9.2 kDa |
| UniProt ID | Q96FX2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 82 aa / 9.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 39 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Host immune constraints delineate the window of microbial colonization during early development of Larimichthys crocea.. *Zool Res*. PMID: 41493083
2. Shared pathogenesis in polycystic ovaries and rheumatoid arthritis: an analysis of key genes and pathways.. *Front Genet*. PMID: 40626180
3. miR-448-3p/miR-1264-3p Participates in Intermittent Hypoxic Response in Hippocampus by Regulating Fam76b/hnRNPA2B1.. *CNS Neurosci Ther*. PMID: 39912396
4. Integrative analysis of the role of the DPH gene family in hepatocellular carcinoma and expression validation.. *Transl Cancer Res*. PMID: 39262488
5. Diphthamide - a conserved modification of eEF2 with clinical relevance.. *Trends Mol Med*. PMID: 38097404

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 8.5% |
| 有序区域 (pLDDT>70) 占比 | 78.1% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=83.6，有序区 78.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SERGEF | 0.000 | 0.000 | — |
| DPH2 | 0.000 | 0.000 | — |
| DPH1 | 0.000 | 0.000 | — |
| EEF2 | 0.000 | 0.000 | — |
| ELP3 | 0.000 | 0.000 | — |
| DNAJC24 | 0.000 | 0.000 | — |
| DPH5 | 0.000 | 0.000 | — |
| DPH7 | 0.000 | 0.000 | — |
| DPH6 | 0.000 | 0.000 | — |
| KTI12 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96FX2 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9UGK8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q3E840 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P10591 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P39101 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P40150 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P25294 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P39987 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P0CS90 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P33416 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 无 | pLDDT=83.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DPH3 — Diphthamide biosynthesis protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小82 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154813-DPH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FX2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
