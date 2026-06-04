---
type: protein-evaluation
gene: "DERA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DERA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DERA |
| 蛋白名称 | Deoxyribose-phosphate aldolase |
| 蛋白大小 | 318 aa / 35.2 kDa |
| UniProt ID | Q9Y315 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Cytoplasmic granule; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 318 aa / 35.2 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=88 篇 (<=100->2) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=96.0; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR013785, IPR011343, IPR002915; Pfam: PF01791 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasmic granule; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleoplasm (GO:0005654)
- secretory granule lumen (GO:0034774)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 2379 |
| 别名(未计入scoring) |  |

**关键文献**:
1. 2-Deoxy-D-ribose-5-phosphate aldolase (DERA): applications and modifications.. *Applied microbiology and biotechnology*. PMID: 30284013
2. Genome-scale mapping of DNA damage suppressors through phenotypic CRISPR-Cas9 screens.. *Molecular cell*. PMID: 37478847
3. Stepwise genetic modification for efficient expression of heterologous proteins in Aspergillus nidulans.. *Applied microbiology and biotechnology*. PMID: 37698610
4. Characterization of a widespread sugar phosphate-processing bacterial microcompartment.. *Communications biology*. PMID: 39580597
5. Absence of GSTT1 and polymorphisms in GSTP1 and TP53 are associated with the incidence of acne vulgaris.. *Skin research and technology : official journal of International Society for Bioengineering and the Skin (ISBS) [and] International Society for Digital Imaging of Skin (ISDIS) [and] International Society for Skin Imaging (ISSI)*. PMID: 37113088

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.0 |
| 高置信度残基 (pLDDT>90) 占比 | 93.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 98.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.0，有序区 98.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013785, IPR011343, IPR002915; Pfam: PF01791 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGM2 | 0.987 | 0.000 | — |
| RBKS | 0.967 | 0.000 | — |
| TYMP | 0.959 | 0.272 | — |
| ALDH16A1 | 0.958 | 0.843 | — |
| TKT | 0.956 | 0.078 | — |
| TKTL2 | 0.956 | 0.078 | — |
| TALDO1 | 0.955 | 0.000 | — |
| TKTL1 | 0.955 | 0.078 | — |
| TPI1 | 0.929 | 0.091 | — |
| ALDOA | 0.924 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG2336 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PAAF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Dmel\CG15717 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| LANCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPIL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ALDH16A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ERP29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.0 + PDB: 无 | pLDDT=96.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic granule; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DERA -- Deoxyribose-phosphate aldolase，研究基础较多，新颖性有限。
2. 蛋白大小318 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y315
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023697-DERA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DERA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y315
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
