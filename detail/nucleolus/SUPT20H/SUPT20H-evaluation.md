---
type: protein-evaluation
gene: "SUPT20H"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT20H 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUPT20H / C13orf19, FAM48A |
| 蛋白名称 | Transcription factor SPT20 homolog |
| 蛋白大小 | 779 aa / 85.8 kDa |
| UniProt ID | Q8NEM7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 779 aa / 85.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.8; PDB: 7KTR, 7KTS, 8H7G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021950, IPR046468; Pfam: PF12090 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- SAGA complex (GO:0000124)
- SAGA-type complex (GO:0070461)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf19, FAM48A |

**关键文献**:
1. Genome-scale CRISPR-Cas9 screen reveals novel regulators of B7-H3 in tumor cells.. *Journal for immunotherapy of cancer*. PMID: 35768165
2. A novel nonsense variant in SUPT20H gene associated with Rheumatoid Arthritis identified by Whole Exome Sequencing of multiplex families.. *PloS one*. PMID: 30845214
3. An Autophagy-Related Gene Signature Associated With Clinical Prognosis and Immune Microenvironment in Gliomas.. *Frontiers in oncology*. PMID: 33194668
4. A predicted risk score based on the expression of 16 autophagy-related genes for multiple myeloma survival.. *Oncology letters*. PMID: 31612041
5. Genomic and Socioeconomic Determinants of Racial Disparities in Breast Cancer Survival: Insights from the All of Us Program.. *Cancers*. PMID: 39409914

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.8 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 28.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 45.4% |
| 有序区域 (pLDDT>70) 占比 | 40.7% |
| 可用 PDB 条目 | 7KTR, 7KTS, 8H7G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.8），有序残基占 40.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021950, IPR046468; Pfam: PF12090 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SGF29 | 0.999 | 0.992 | — |
| TRRAP | 0.999 | 0.997 | — |
| TAF9 | 0.999 | 0.992 | — |
| TADA3 | 0.999 | 0.972 | — |
| TADA1 | 0.999 | 0.991 | — |
| SUPT3H | 0.999 | 0.993 | — |
| ATXN7 | 0.999 | 0.989 | — |
| SUPT7L | 0.999 | 0.940 | — |
| TAF5L | 0.999 | 0.989 | — |
| TAF12 | 0.999 | 0.997 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16751104|imex:IM-11828 |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| STAT3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MAPK1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| USP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| A0A384LQH9 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Fla FV | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.8 + PDB: 7KTR, 7KTS, 8H7G | pLDDT=58.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SUPT20H — Transcription factor SPT20 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小779 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEM7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102710-SUPT20H/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUPT20H
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEM7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000102710-SUPT20H/subcellular

![](https://images.proteinatlas.org/38906/412_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38906/412_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38906/419_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38906/419_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38906/471_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38906/471_G12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEM7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
