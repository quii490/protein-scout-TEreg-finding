---
type: protein-evaluation
gene: "TATDN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TATDN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TATDN2 / KIAA0218 |
| 蛋白名称 | 3'-5' RNA nuclease TATDN2 |
| 蛋白大小 | 761 aa / 85.0 kDa |
| UniProt ID | Q93075 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 761 aa / 85.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018228, IPR032466, IPR001130; Pfam: PF01026 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0218 |

**关键文献**:
1. Linkage analysis using whole exome sequencing data implicates SLC17A1, SLC17A3, TATDN2 and TMEM131L in type 1 diabetes in Kuwaiti families.. *Scientific reports*. PMID: 37696853
2. Complex organisation and structure of the ghrelin antisense strand gene GHRLOS, a candidate non-coding RNA gene.. *BMC molecular biology*. PMID: 18954468
3. Evolutionary analysis of ghrelin in Actinopterygii.. *Comparative biochemistry and physiology. Part D, Genomics & proteomics*. PMID: 40784251
4. Establishment of a Genomic-Clinicopathologic Nomogram for Predicting Early Recurrence of Hepatocellular Carcinoma After R0 Resection.. *Journal of gastrointestinal surgery : official journal of the Society for Surgery of the Alimentary Tract*. PMID: 32128678

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 61.2% |
| 有序区域 (pLDDT>70) 占比 | 35.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 35.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018228, IPR032466, IPR001130; Pfam: PF01026 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XBP1 | 0.750 | 0.000 | — |
| CCDC174 | 0.624 | 0.000 | — |
| PRRT3 | 0.579 | 0.000 | — |
| MTFR1L | 0.570 | 0.000 | — |
| ADO | 0.533 | 0.000 | — |
| ENSP00000481571 | 0.509 | 0.000 | — |
| BAHD1 | 0.508 | 0.000 | — |
| IRAK2 | 0.492 | 0.000 | — |
| VWA5B1 | 0.483 | 0.000 | — |
| UBE2L5 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000408736.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SPACA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLAUR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAGK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCNJL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ISCA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IL13RA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AFG2B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 无 | pLDDT=59.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

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
1. TATDN2 — 3'-5' RNA nuclease TATDN2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小761 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q93075
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157014-TATDN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TATDN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q93075
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000157014-TATDN2/subcellular

![](https://images.proteinatlas.org/36822/436_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36822/436_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36822/442_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36822/442_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36822/521_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/36822/521_A3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q93075-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
