---
type: protein-evaluation
gene: "WDR75"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR75 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR75 / UTP17 |
| 蛋白名称 | WD repeat-containing protein 75 |
| 蛋白大小 | 830 aa / 94.5 kDa |
| UniProt ID | Q8IWA0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 830 aa / 94.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.4; PDB: 7MQ8, 7MQ9, 7MQA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057644, IPR011047, IPR015943, IPR001680, IPR053 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **145.0/180** | |
| **归一化总分** | | | **80.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UTP17 |

**关键文献**:
1. Cardiac repair using regenerating neonatal heart tissue-derived extracellular vesicles.. *Nature communications*. PMID: 39900896
2. Transcriptome and microRNAome profiling of human skeletal muscle in pancreatic cancer cachexia.. *medRxiv : the preprint server for health sciences*. PMID: 40950454
3. Genome-wide DNA methylation analysis in schizophrenia with tardive dyskinesia: a preliminary study.. *Genes & genomics*. PMID: 37414911
4. Sequence-based GWAS meta-analyses for beef production traits.. *Genetics, selection, evolution : GSE*. PMID: 37828440
5. Hepatitis B virus X protein (HBx)-mediated immune modulation and prognostic model development in hepatocellular carcinoma.. *PloS one*. PMID: 40577282

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 49.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 12.9% |
| 有序区域 (pLDDT>70) 占比 | 78.6% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7MQ8, 7MQ9, 7MQA）+ AlphaFold高质量预测（pLDDT=80.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057644, IPR011047, IPR015943, IPR001680, IPR053826; Pfam: PF23869, PF23769 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP20 | 0.999 | 0.991 | — |
| WDR36 | 0.999 | 0.981 | — |
| TBL3 | 0.999 | 0.981 | — |
| BMS1 | 0.999 | 0.991 | — |
| RRP9 | 0.999 | 0.992 | — |
| WDR3 | 0.999 | 0.976 | — |
| UTP18 | 0.999 | 0.987 | — |
| NOL6 | 0.999 | 0.991 | — |
| WDR43 | 0.999 | 0.997 | — |
| MPHOSPH10 | 0.999 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PLEK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| FBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOL7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDFY3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=80.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDR75 — WD repeat-containing protein 75，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小830 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWA0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115368-WDR75/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR75
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWA0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
