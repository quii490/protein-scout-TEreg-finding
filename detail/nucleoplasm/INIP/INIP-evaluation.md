---
type: protein-evaluation
gene: "INIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INIP / C9orf80, SSBIP1 |
| 蛋白名称 | SOSS complex subunit C |
| 蛋白大小 | 104 aa / 11.4 kDa |
| UniProt ID | Q9NRY2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 104 aa / 11.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.1; PDB: 4OWT, 4OWW, 8RBZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031821; Pfam: PF15925 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **147.0/180** | |
| **归一化总分** | | | **81.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)
- SOSS complex (GO:0070876)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf80, SSBIP1 |

**关键文献**:
1. Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders.. *JAMA psychiatry*. PMID: 28097321
2. Genome-wide meta-analysis and omics integration identifies novel genes associated with diabetic kidney disease.. *Diabetologia*. PMID: 35763030
3. Tetrameric INTS6-SOSS1 complex facilitates DNA:RNA hybrid autoregulation at double-strand breaks.. *Nucleic acids research*. PMID: 39445827
4. Detailed gene dose analysis reveals recurrent focal gene deletions in pediatric B-cell precursor acute lymphoblastic leukemia.. *Leukemia & lymphoma*. PMID: 27090575
5. Design and synthesis of small semi-mimetic peptides with immunomodulatory activity based on myelin basic protein (MBP).. *Amino acids*. PMID: 9871477

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 29.8% |
| 置信残基 (pLDDT 70-90) 占比 | 35.6% |
| 中等置信 (pLDDT 50-70) 占比 | 21.2% |
| 低置信 (pLDDT<50) 占比 | 13.5% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 4OWT, 4OWW, 8RBZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4OWT, 4OWW, 8RBZ）+ AlphaFold高质量预测（pLDDT=76.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031821; Pfam: PF15925 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INTS3 | 0.999 | 0.999 | — |
| NABP2 | 0.999 | 0.998 | — |
| NABP1 | 0.985 | 0.421 | — |
| SSBP2 | 0.890 | 0.000 | — |
| SSBP1 | 0.876 | 0.000 | — |
| RBBP8 | 0.832 | 0.000 | — |
| RBBP5 | 0.781 | 0.000 | — |
| NBN | 0.766 | 0.000 | — |
| INTS11 | 0.736 | 0.000 | — |
| DGCR6L | 0.591 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| RBPMS | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| KRT34 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DGCR6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DGCR6L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARID5A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BPIFA1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NABP2 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| NABP1 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| INTS3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25484|pubmed:19683501 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 4OWT, 4OWW, 8RBZ | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. INIP — SOSS complex subunit C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小104 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRY2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148153-INIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRY2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000148153-INIP/subcellular

![](https://images.proteinatlas.org/20382/183_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/20382/183_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/20382/185_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/20382/185_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/20382/242_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/20382/242_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRY2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
