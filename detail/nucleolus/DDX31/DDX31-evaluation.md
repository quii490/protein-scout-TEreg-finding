---
type: protein-evaluation
gene: "DDX31"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX31 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX31 |
| 蛋白名称 | ATP-dependent DNA helicase DDX31 |
| 蛋白大小 | 851 aa / 94.1 kDa |
| UniProt ID | Q9H8H2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoli; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | x1 | 8 | 851 aa / 94.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=12 篇 (<=20->10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Golgi apparatus, Vesicles | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 12 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Novel examples of NMD escape through alternative intronic polyadenylation.. *NAR Genom Bioinform*. PMID: 42170191
2. TBC1D14 inhibits ribosome biogenesis to reduce lymph node metastasis in head and neck squamous cell carcinoma by mediating DDX31 ubiquitination.. *Int J Biol Macromol*. PMID: 40784392
3. Domain-specific p53 mutants activate EGFR by distinct mechanisms exposing tissue-independent therapeutic vulnerabilities.. *Nat Commun*. PMID: 36977662
4. VASA protein and gene expression analysis of human non-obstructive azoospermia and normal by immunohistochemistry, immunocytochemistry, and bioinformatics analysis.. *Sci Rep*. PMID: 36241908
5. Comprehensive development and validation of gene signature for predicting survival in patients with glioblastoma.. *Front Genet*. PMID: 36035145

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 39.7% |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 55.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FTSJ3 | 0.000 | 0.000 | — |
| PUM3 | 0.000 | 0.000 | — |
| NOC2L | 0.000 | 0.000 | — |
| RBM19 | 0.000 | 0.000 | — |
| DDX56 | 0.000 | 0.000 | — |
| DDX24 | 0.000 | 0.000 | — |
| RBM34 | 0.000 | 0.000 | — |
| DDX10 | 0.000 | 0.000 | — |
| BOP1 | 0.000 | 0.000 | — |
| DDX52 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H8H2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P37108 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 无 | pLDDT=66.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli; 额外: Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DDX31 -- ATP-dependent DNA helicase DDX31，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小851 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H8H2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125485-DDX31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8H2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H8H2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H8H2 |
| SMART | SM00487;SM01178;SM00490; |
| UniProt Domain [FT] | DOMAIN 262..443; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 480..659; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011545;IPR014001;IPR001650;IPR027417;IPR000629;IPR014014;IPR025313; |
| Pfam | PF13959;PF00270;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125485-DDX31/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPL31 | Biogrid, Bioplex | true |
| RPS6 | Biogrid, Bioplex | true |
| SRP14 | Intact, Biogrid, Bioplex | true |
| ABT1 | Bioplex | false |
| CBX6 | Bioplex | false |
| FBL | Biogrid | false |
| FGFBP1 | Bioplex | false |
| H1-1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
