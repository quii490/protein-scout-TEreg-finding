---
type: protein-evaluation
gene: "SOX17"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOX17 — REJECTED (研究热度过高 (PubMed strict=662，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOX17 |
| 蛋白名称 | Transcription factor SOX-17 |
| 蛋白大小 | 414 aa / 44.1 kDa |
| UniProt ID | Q9H6I2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 44.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=662 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.4; PDB: 2YUL, 4A3N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR033392, IPR021934, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 662 |
| PubMed broad count | 1217 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of rare sequence variation underlying heritable pulmonary arterial hypertension.. *Nature communications*. PMID: 29650961
2. Defining the clinical validity of genes reported to cause pulmonary arterial hypertension.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 37422716
3. Genetic determinants of risk in pulmonary arterial hypertension: international genome-wide association studies and meta-analysis.. *The Lancet. Respiratory medicine*. PMID: 30527956
4. Rare variants in SOX17 are associated with pulmonary arterial hypertension with congenital heart disease.. *Genome medicine*. PMID: 30029678
5. Single-cell transcriptomics identifies gene expression networks driving differentiation and tumorigenesis in the human fallopian tube.. *Cell reports*. PMID: 33852846

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 1.9% |
| 中等置信 (pLDDT 50-70) 占比 | 26.6% |
| 低置信 (pLDDT<50) 占比 | 53.6% |
| 有序区域 (pLDDT>70) 占比 | 19.8% |
| 可用 PDB 条目 | 2YUL, 4A3N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.4），有序残基占 19.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR033392, IPR021934, IPR050140; Pfam: PF00505, PF12067 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POU5F1 | 0.988 | 0.345 | — |
| CTNNB1 | 0.967 | 0.301 | — |
| LEF1 | 0.953 | 0.095 | — |
| TCF7L1 | 0.948 | 0.093 | — |
| FOXA2 | 0.942 | 0.063 | — |
| TCF7L2 | 0.918 | 0.093 | — |
| TCF7 | 0.916 | 0.093 | — |
| GATA4 | 0.880 | 0.053 | — |
| NANOG | 0.871 | 0.124 | — |
| GATA6 | 0.854 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EZH2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:27728805|imex:IM-25628 |
| EBNA1BP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EEFSEC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HOMER3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RPL38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ercc8 | psi-mi:"MI:0096"(pull down) | pubmed:20211142|doi:10.1016/j. |
| NFIC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| NFIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| NFIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| KDM6A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.4 + PDB: 2YUL, 4A3N | pLDDT=57.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SOX17 — Transcription factor SOX-17，研究基础较多，新颖性有限。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 662 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 662 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6I2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164736-SOX17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOX17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6I2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164736-SOX17/subcellular

![](https://images.proteinatlas.org/58949/2257_D1_189_blue_red_green.jpg)
![](https://images.proteinatlas.org/58949/2257_D1_68_blue_red_green.jpg)
![](https://images.proteinatlas.org/25594/653_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/25594/653_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/25594/658_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/25594/658_B5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H6I2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
