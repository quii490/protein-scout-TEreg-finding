---
type: protein-evaluation
gene: "CWF19L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CWF19L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CWF19L2 |
| 蛋白名称 | CWF19-like protein 2 |
| 蛋白大小 | 894 aa / 103.8 kDa |
| UniProt ID | Q2TBE0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 894 aa / 103.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=3 篇 (<=20->10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=66.3; PDB: 6ID0, 6ID1, 8RO2 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR040194, IPR006768, IPR006767, IPR036265; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- post-mRNA release spliceosomal complex (GO:0071014)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Systematic identification of therapeutic targets for coronary artery calcification: an integrated transcriptomic and proteomic Mendelian randomization.. *Frontiers in cardiovascular medicine*. PMID: 39526184
2. Genome-wide analysis identifies 16q deletion associated with survival, molecular subtypes, mRNA expression, and germline haplotypes in breast cancer patients.. *Genes, chromosomes & cancer*. PMID: 18398821
3. NVL2-interacting protein CWF19L2 is required for debranching of intron-derived lariat RNAs.. *Biochemical and biophysical research communications*. PMID: 41422678

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.3 |
| 高置信度残基 (pLDDT>90) 占比 | 21.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 33.0% |
| 有序区域 (pLDDT>70) 占比 | 52.5% |
| 可用 PDB 条目 | 6ID0, 6ID1, 8RO2 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.3），有序残基占 52.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040194, IPR006768, IPR006767, IPR036265; Pfam: PF04677, PF04676 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC40 | 0.998 | 0.991 | — |
| PRPF19 | 0.995 | 0.995 | — |
| EFTUD2 | 0.994 | 0.993 | — |
| CDC5L | 0.992 | 0.992 | — |
| SYF2 | 0.988 | 0.936 | — |
| PPIL1 | 0.987 | 0.937 | — |
| SNRPA1 | 0.986 | 0.983 | — |
| PRPF8 | 0.985 | 0.977 | — |
| PLRG1 | 0.973 | 0.968 | — |
| BUD31 | 0.970 | 0.964 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| WDR83 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RINT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IKZF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZBTB8A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IKBKG | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DES | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CARD10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HOMER3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.3 + PDB: 6ID0, 6ID1, 8RO2 | pLDDT=66.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CWF19L2 -- CWF19-like protein 2，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小894 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2TBE0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152404-CWF19L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CWF19L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TBE0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
