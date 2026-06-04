---
type: protein-evaluation
gene: "CNTNAP5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNTNAP5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNTNAP5 / CASPR5 |
| 蛋白名称 | Contactin-associated protein-like 5 |
| 蛋白大小 | 1306 aa / 145.6 kDa |
| UniProt ID | Q8WYK1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 1306 aa / 145.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.0; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR013320, IPR000742, IPR000421, IPR036056, IPR002 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm, Vesicles | Supported |
| UniProt | Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CASPR5 |

**关键文献**:
1. Single-nucleus RNA sequencing of human pancreatic islets identifies novel gene sets and distinguishes β-cell subpopulations with dynamic transcriptome profiles.. *Genome medicine*. PMID: 37127706
2. Characterization of a family with rare deletions in CNTNAP5 and DOCK4 suggests novel risk loci for autism and dyslexia.. *Biological psychiatry*. PMID: 20346443
3. Chromosome 2q14.3 microdeletion encompassing CNTNAP5 gene in a patient carrying a complex chromosomal rearrangement.. *Journal of genetics*. PMID: 34553698
4. Structure and function of the contactin-associated protein family in myelinated axons and their relationship with nerve diseases.. *Neural regeneration research*. PMID: 29090003
5. Post-GWAS functional analyses of CNTNAP5 suggests its role in glaucomatous neurodegeneration.. *bioRxiv : the preprint server for biology*. PMID: 38903068

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 56.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 9.3% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.0，有序区 86.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR000742, IPR000421, IPR036056, IPR002181; Pfam: PF00754, PF02210 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AASDHPPT | 0.629 | 0.000 | — |
| DSCAM | 0.607 | 0.069 | — |
| CNTN5 | 0.573 | 0.141 | — |
| CNTN4 | 0.551 | 0.141 | — |
| ANKS1B | 0.540 | 0.071 | — |
| NRXN1 | 0.504 | 0.000 | — |
| FREM3 | 0.475 | 0.000 | — |
| TMEM132C | 0.466 | 0.000 | — |
| CNTN3 | 0.441 | 0.141 | — |
| CCDC117 | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZNF620 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CACNA1C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 无 | pLDDT=84.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli fibrillar center; 额外: Nucleoplasm, Vesicl | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. CNTNAP5 -- Contactin-associated protein-like 5，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小1306 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYK1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155052-CNTNAP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNTNAP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYK1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
