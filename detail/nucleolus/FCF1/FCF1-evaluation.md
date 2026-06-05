---
type: protein-evaluation
gene: "FCF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FCF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCF1 / C14orf111 |
| 蛋白名称 | rRNA-processing protein FCF1 homolog |
| 蛋白大小 | 198 aa / 23.4 kDa |
| UniProt ID | Q9Y324 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 198 aa / 23.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.7; PDB: 7MQ8, 7MQ9, 7MQA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006984, IPR037503, IPR029060, IPR002716; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **149.0/180** | |
| **归一化总分** | | | **82.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf111 |

**关键文献**:
1. Identification of prognostic RNA editing profiles for clear cell renal carcinoma.. *Frontiers in medicine*. PMID: 39091293
2. Structural and evolutionary relationships between two families of bacterial extracytoplasmic chaperone proteins which function cooperatively in fimbrial assembly.. *Research in microbiology*. PMID: 7906046
3. Gene signatures of circulating breast cancer cell models are a source of novel molecular determinants of metastasis and improve circulating tumor cell detection in patients.. *Journal of experimental & clinical cancer research : CR*. PMID: 35216615
4. The ribosome biogenesis factor yUtp23/hUTP23 coordinates key interactions in the yeast and human pre-40S particle and hUTP23 contains an essential PIN domain.. *Nucleic acids research*. PMID: 28082392
5. Genome-wide association study and accuracy of genomic prediction for teat number in Duroc pigs using genotyping-by-sequencing.. *Genetics, selection, evolution : GSE*. PMID: 28356075

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.5% |
| 置信残基 (pLDDT 70-90) 占比 | 35.9% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 2.0% |
| 有序区域 (pLDDT>70) 占比 | 84.4% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7MQ8, 7MQ9, 7MQA）+ AlphaFold高质量预测（pLDDT=83.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006984, IPR037503, IPR029060, IPR002716; Pfam: PF04900 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR46 | 0.999 | 0.988 | — |
| KRR1 | 0.999 | 0.987 | — |
| EMG1 | 0.999 | 0.976 | — |
| UTP11 | 0.999 | 0.986 | — |
| DNTTIP2 | 0.999 | 0.985 | — |
| UTP3 | 0.999 | 0.986 | — |
| NOP58 | 0.998 | 0.988 | — |
| IMP3 | 0.998 | 0.987 | — |
| UTP20 | 0.998 | 0.986 | — |
| BMS1 | 0.998 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| UTP22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29054886|imex:IM-25795| |
| CKB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29054886|imex:IM-25795| |
| KRR1 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |
| NOP14 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |
| NOP9 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |
| UTP30 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |
| ROK1 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |
| RRP7 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:29054886|imex:IM-25795| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=83.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm | 一致 |
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
1. FCF1 — rRNA-processing protein FCF1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y324
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119616-FCF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y324
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000119616-FCF1/subcellular

![](https://images.proteinatlas.org/46681/616_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/46681/616_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/46681/619_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/46681/619_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/46681/622_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/46681/622_D7_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y324-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
