---
type: protein-evaluation
gene: "OBI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OBI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OBI1 / C13orf7, RNF219 |
| 蛋白名称 | ORC ubiquitin ligase 1 |
| 蛋白大小 | 726 aa / 81.1 kDa |
| UniProt ID | Q5W0B1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 726 aa / 81.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039209, IPR035691, IPR001841, IPR013083; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf7, RNF219 |

**关键文献**:
1. The ORC ubiquitin ligase OBI1 promotes DNA replication origin firing.. *Nature communications*. PMID: 31160578
2. Correlation research of susceptibility single nucleotide polymorphisms and the severity of clinical symptoms in attention deficit hyperactivity disorder.. *Frontiers in psychiatry*. PMID: 36213906
3. Long-read Sequencing Reveals Repeat Expansions and Large Structural Variants in Oral Squamous Cell Carcinoma.. *Genomics, proteomics & bioinformatics*. PMID: 41454621
4. Genetic Foundations of Nellore Traits: A Gene Prioritization and Functional Analyses of Genome-Wide Association Study Results.. *Genes*. PMID: 39336722
5. Alternative therapies for the management of inhibitors.. *Haemophilia : the official journal of the World Federation of Hemophilia*. PMID: 27405674

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 19.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 58.8% |
| 有序区域 (pLDDT>70) 占比 | 32.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 32.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039209, IPR035691, IPR001841, IPR013083; Pfam: PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT10 | 0.778 | 0.730 | — |
| CNOT11 | 0.771 | 0.692 | — |
| ORC3 | 0.697 | 0.362 | — |
| LRWD1 | 0.679 | 0.362 | — |
| ORC5 | 0.656 | 0.362 | — |
| TOB1 | 0.651 | 0.591 | — |
| CNOT1 | 0.647 | 0.618 | — |
| CNOT7 | 0.639 | 0.582 | — |
| CNOT3 | 0.626 | 0.626 | — |
| WRAP73 | 0.618 | 0.618 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTNNA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Cnot3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NLK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SNRNP70 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| STXBP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| UTRN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| FUBP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PDE2A | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 无 | pLDDT=57.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. OBI1 — ORC ubiquitin ligase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小726 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5W0B1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152193-OBI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OBI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5W0B1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000152193-OBI1/subcellular

![](https://images.proteinatlas.org/34785/389_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/34785/389_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/34785/398_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/34785/398_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5W0B1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
