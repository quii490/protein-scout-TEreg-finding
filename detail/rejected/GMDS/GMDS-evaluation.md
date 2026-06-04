---
type: protein-evaluation
gene: "GMDS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GMDS — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GMDS |
| 蛋白名称 | GDP-mannose 4,6 dehydratase |
| 蛋白大小 | 372 aa / 42.0 kDa |
| UniProt ID | O60547 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 372 aa / 42.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.1; PDB: 1T2A, 5IN4, 5IN5, 6GPJ, 6GPK, 6GPL, 6Q94 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006368, IPR016040, IPR036291; Pfam: PF16363 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 342 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Proteome-wide mapping of short-lived proteins in human cells.. *Molecular cell*. PMID: 34626566
2. The Indispensable Roles of GMDS and GMDS-AS1 in the Advancement of Cancer: Fucosylation, Signal Pathway and Molecular Pathogenesis.. *Mini reviews in medicinal chemistry*. PMID: 38591197
3. LncGMDS-AS1 promotes the tumorigenesis of colorectal cancer through HuR-STAT3/Wnt axis.. *Cell death & disease*. PMID: 36849492
4. Genomic analysis of glaucoma pathogenesis due to gmds mutation in zebrafish.. *Experimental eye research*. PMID: 40571142
5. lncRNA GMDS-AS1 restrains lung adenocarcinoma progression via recruiting TAF15 protein to stabilize SIRT1 mRNA.. *Epigenomics*. PMID: 37309595

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 89.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 94.1% |
| 可用 PDB 条目 | 1T2A, 5IN4, 5IN5, 6GPJ, 6GPK, 6GPL, 6Q94 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1T2A, 5IN4, 5IN5, 6GPJ, 6GPK, 6GPL, 6Q94）+ AlphaFold极高置信度预测（pLDDT=94.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006368, IPR016040, IPR036291; Pfam: PF16363 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSTA3 | 0.999 | 0.091 | — |
| GMPPA | 0.978 | 0.000 | — |
| TNKS | 0.897 | 0.813 | — |
| GMPPB | 0.892 | 0.000 | — |
| FOXC1 | 0.886 | 0.000 | — |
| ALG1 | 0.872 | 0.000 | — |
| TNKS2 | 0.845 | 0.734 | — |
| DPM2 | 0.844 | 0.000 | — |
| SLC35C1 | 0.812 | 0.000 | — |
| DPM3 | 0.801 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000370194.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| NPHP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNKS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNKS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNAB3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 1T2A, 5IN4, 5IN5, 6GPJ, 6GPK,  | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GMDS — GDP-mannose 4,6 dehydratase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小372 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60547
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112699-GMDS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GMDS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60547
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
