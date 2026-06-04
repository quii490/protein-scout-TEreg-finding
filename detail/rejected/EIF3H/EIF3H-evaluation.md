---
type: protein-evaluation
gene: "EIF3H"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3H — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3H |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit H |
| 蛋白大小 | 366 aa / 41.6 kDa |
| UniProt ID | B3KS98 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 366 aa / 41.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 106 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Evaluation and Selection of Stable Reference Genes for qRT-PCR Analysis in Different Tissues of Mugilogobius chulae Under Pollutant Exposure.. *Animals (Basel)*. PMID: 42121831
2. Src promotes tumor cell invasion by hijacking the translation machineries.. *Cell Rep*. PMID: 41734063
3. AC005034.3/hsa-miR-126-5p/EIF3H axis: bioinformatics analysis, expression validation, and association with prognosis and immunosuppressive microenvironment in pancreatic adenocarcinoma.. *Front Cell Dev Biol*. PMID: 41822359
4. Deubiquitinating enzymes in breast cancer: in silico analysis of gene expression and metastatic correlation.. *J Biomol Struct Dyn*. PMID: 39671715
5. An integrative meta-analysis of SARS-CoV-2 RNA-protein interactomes identifies conserved host factors shared with other RNA viruses.. *Brief Funct Genomics*. PMID: 42149692

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 4.1% |
| 置信残基 (pLDDT 70-90) 占比 | 62.0% |
| 中等置信 (pLDDT 50-70) 占比 | 20.8% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 66.1% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=71.6，有序区 66.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3B | 0.000 | 0.000 | — |
| EIF3L | 0.000 | 0.000 | — |
| EIF3A | 0.000 | 0.000 | — |
| EIF3K | 0.000 | 0.000 | — |
| EIF3CL | 0.000 | 0.000 | — |
| EIF3G | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF3E | 0.000 | 0.000 | — |
| EIF3M | 0.000 | 0.000 | — |
| EIF3D | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O15372 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15834 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9P2A4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9U9Q4 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NRI5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NRI5-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P23508 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14240 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 无 | pLDDT=71.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF3H — Eukaryotic translation initiation factor 3 subunit H，研究基础较多，新颖性有限。
2. 蛋白大小366 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B3KS98
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147677-EIF3H/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3H
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KS98
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
