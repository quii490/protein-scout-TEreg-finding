---
type: protein-evaluation
gene: "DOCK3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK3 |
| 蛋白名称 | DOCK3 |
| 蛋白大小 | 2032 aa / 233.3 kDa |
| UniProt ID | A0A2X0SFH6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 2/10 | ×1 | 2 | 2032 aa / 233.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.0/180** | |
| **归一化总分** | | | **33.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 88 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CB-Dock3: an enhanced web server for protein-ligand blind docking.. *Nucleic Acids Res*. PMID: 42087554
2. Composite selection signal analysis: Uncovering candidate genes and quantitative trait loci in Indian sheep breeds.. *PLoS One*. PMID: 41880302
3. The DOCK3-HAUS7 axis: A new paradigm in optic nerve regeneration.. *Neural Regen Res*. PMID: 41777040
4. Large scale prospective evaluation of co-folding across 557 Mac1-ligand complexes and three virtual screens.. *bioRxiv*. PMID: 41509292
5. DOCK3 orchestrates metastasis and immune microenvironment in prostate cancer.. *Front Urol*. PMID: 41200217

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELMO1 | 0.000 | 0.000 | — |
| NEDD9 | 0.000 | 0.000 | — |
| ELMO3 | 0.000 | 0.000 | — |
| SLC9A9 | 0.000 | 0.000 | — |
| ELMO2 | 0.000 | 0.000 | — |
| RAC1 | 0.000 | 0.000 | — |
| RHOG | 0.000 | 0.000 | — |
| RAC2 | 0.000 | 0.000 | — |
| CRK | 0.000 | 0.000 | — |
| FYN | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P16333 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:Q8IZD9 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P62993 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:Q14511 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8CIQ7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P00519 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P46108 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P27986 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:Q9NR30 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:P13667 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DOCK3 — DOCK3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2032 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A2X0SFH6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088538-DOCK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A2X0SFH6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
