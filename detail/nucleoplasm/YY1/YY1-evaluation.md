---
type: protein-evaluation
gene: "YY1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## YY1 — REJECTED (研究热度过高 (PubMed strict=1990，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YY1 / INO80S |
| 蛋白名称 | Transcriptional repressor protein YY1 |
| 蛋白大小 | 414 aa / 44.7 kDa |
| UniProt ID | P25490 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center, Nuclear bodies; UniProt: Nucleus matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 44.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1990 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.6; PDB: 1UBD, 1ZNM, 4C5I |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017114, IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center, Nuclear bodies | Supported |
| UniProt | Nucleus matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromatin silencing complex (GO:0005677)
- Ino80 complex (GO:0031011)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1990 |
| PubMed broad count | 2773 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: INO80S |

**关键文献**:
1. YY1 Is a Structural Regulator of Enhancer-Promoter Loops.. *Cell*. PMID: 29224777
2. Phosphorylation-dependent deubiquitinase OTUD3 regulates YY1 stability and promotes colorectal cancer progression.. *Cell death & disease*. PMID: 38351178
3. The role of USP7-YY1 interaction in promoting colorectal cancer growth and metastasis.. *Cell death & disease*. PMID: 38769122
4. YY1-controlled regulatory connectivity and transcription are influenced by the cell cycle.. *Nature genetics*. PMID: 39210046
5. A transcriptional regulatory mechanism of genes in the tricarboxylic acid cycle in the heart.. *The Journal of biological chemistry*. PMID: 39151728

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.6 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 63.8% |
| 有序区域 (pLDDT>70) 占比 | 28.7% |
| 可用 PDB 条目 | 1UBD, 1ZNM, 4C5I |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.6），有序残基占 28.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017114, IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.999 | 0.832 | — |
| HDAC1 | 0.999 | 0.785 | — |
| HDAC2 | 0.999 | 0.818 | — |
| EZH2 | 0.998 | 0.552 | — |
| RYBP | 0.998 | 0.532 | — |
| PPARGC1A | 0.995 | 0.091 | — |
| SUZ12 | 0.993 | 0.110 | — |
| INO80 | 0.992 | 0.855 | — |
| CTCF | 0.991 | 0.299 | — |
| UCHL5 | 0.990 | 0.835 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| esn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rybp | psi-mi:"MI:0096"(pull down) | pubmed:10369680|imex:IM-19615 |
| a6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| pho | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| Trl | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| NFKB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SPRY1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GRN | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RAF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.6 + PDB: 1UBD, 1ZNM, 4C5I | pLDDT=50.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix / Nucleoplasm; 额外: Nucleoli fibrillar center, Nuclea | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. YY1 — Transcriptional repressor protein YY1，研究基础较多，新颖性有限。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1990 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1990 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P25490
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100811-YY1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YY1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P25490
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100811-YY1/subcellular

![](https://images.proteinatlas.org/597/1935_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/597/1935_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/597/2055_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/597/2055_D8_4_red_green.jpg)
![](https://images.proteinatlas.org/597/2087_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/597/2087_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P25490-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
