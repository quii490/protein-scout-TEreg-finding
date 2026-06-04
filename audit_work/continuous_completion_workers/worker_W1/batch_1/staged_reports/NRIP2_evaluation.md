---
type: protein-evaluation
gene: "NRIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NRIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRIP2 |
| 蛋白名称 | Nuclear receptor-interacting protein 2 |
| 蛋白大小 | 281 aa / 31.3 kDa |
| UniProt ID | Q9BQI9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 281 aa / 31.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033821, IPR019103, IPR021109; Pfam: PF09668 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear bodies | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of prognostic stemness biomarkers in colon adenocarcinoma drug resistance.. *BMC genomic data*. PMID: 35794546
2. Leptin Aggravates Thoracic Aortic Dissection Through Impairment of Energy Metabolism in Nrip2(+) Smooth Muscle Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40667784
3. Transcriptome Signatures for Cognitive Resilience Among Individuals with Pathologically Confirmed Alzheimer Disease.. *medRxiv : the preprint server for health sciences*. PMID: 39606402
4. Nuclear Receptor Interacting Protein-2 Mediates the Stabilization and Activation of β-Catenin During Podocyte Injury.. *Frontiers in cell and developmental biology*. PMID: 35004680
5. Global analysis of FSH-regulated gene expression and histone modification in mouse granulosa cells.. *Molecular reproduction and development*. PMID: 32892476

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 25.6% |
| 低置信 (pLDDT<50) 占比 | 27.8% |
| 有序区域 (pLDDT>70) 占比 | 46.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 46.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033821, IPR019103, IPR021109; Pfam: PF09668 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPS27A | 0.655 | 0.619 | — |
| SF3A2 | 0.602 | 0.591 | — |
| HDAC7 | 0.593 | 0.591 | — |
| SUSD5 | 0.536 | 0.000 | — |
| GRIP2 | 0.528 | 0.000 | — |
| RAD23A | 0.512 | 0.398 | — |
| RAD23B | 0.512 | 0.398 | — |
| IQSEC3 | 0.509 | 0.000 | — |
| PSMD2 | 0.508 | 0.296 | — |
| TEX52 | 0.505 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCNG2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ELF5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HDAC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLF16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Q3UYH0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ENST00000337508 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 无 | pLDDT=66.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NRIP2 — Nuclear receptor-interacting protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小281 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQI9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000053702-NRIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQI9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
