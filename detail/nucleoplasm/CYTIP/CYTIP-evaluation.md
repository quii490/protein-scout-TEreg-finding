---
type: protein-evaluation
gene: "CYTIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYTIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYTIP / PSCDBP |
| 蛋白名称 | Cytohesin-interacting protein |
| 蛋白大小 | 359 aa / 40.0 kDa |
| UniProt ID | O60759 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Early endosome |
| 蛋白大小 | 10/10 | x1 | 10 | 359 aa / 40.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=18 篇 (<=20->10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 2Z17 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052122, IPR001478, IPR036034; Pfam: PF00595 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Early endosome | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PSCDBP |

**关键文献**:
1. Genome-wide identification of differentially methylated promoters and enhancers associated with response to anti-PD-1 therapy in non-small cell lung cancer.. *Experimental & molecular medicine*. PMID: 32879421
2. Identification of characteristic genes ofanddeficiency constitutions: an integrated analysis based on bioinformatics and machine learning.. *Journal of traditional Chinese medicine = Chung i tsa chih ying wen pan*. PMID: 40810238
3. Identification of aneuploidy-related gene signature to predict survival in head and neck squamous cell carcinomas.. *Aging*. PMID: 37988195
4. Proteomic analysis in primary T cells reveals IL-7 alters T cell receptor thresholding via CYTIP/cytohesin/LFA-1 localisation and activation.. *The Biochemical journal*. PMID: 35015072
5. Cytip regulates dendritic-cell function in contact hypersensitivity.. *European journal of immunology*. PMID: 22488362

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 26.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 23.4% |
| 低置信 (pLDDT<50) 占比 | 42.6% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 2Z17 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052122, IPR001478, IPR036034; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYTH1 | 0.988 | 0.809 | — |
| SNX27 | 0.957 | 0.046 | — |
| CYTH3 | 0.905 | 0.616 | — |
| CD48 | 0.789 | 0.045 | — |
| EVI2B | 0.762 | 0.000 | — |
| SERPINB3 | 0.746 | 0.000 | — |
| DGKZ | 0.718 | 0.051 | — |
| CYTH2 | 0.717 | 0.623 | — |
| CD53 | 0.657 | 0.000 | — |
| CXCR4 | 0.559 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rne | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ftsI | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| manA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| KIF9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MCRS1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SCNM1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CYTH1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CYTH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABRAXAS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 2Z17 | pLDDT=62.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Early endosome / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CYTIP -- Cytohesin-interacting protein，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60759
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115165-CYTIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYTIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60759
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60759-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
