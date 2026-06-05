---
type: protein-evaluation
gene: "DCTN5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCTN5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTN5 |
| 蛋白名称 | Dynactin subunit 5 |
| 蛋白大小 | 182 aa / 20.1 kDa |
| UniProt ID | Q9BTE1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nuclear membrane; UniProt: Cytoplasm, cytoskeleton; Chromosome, centromere, kinetochore |
| 蛋白大小 | 8/10 | x1 | 8 | 182 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (<=20->10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=82.1; PDB: 5NW4, 9B7J, 9B85 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR047125, IPR011004; Pfam: PF21711 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane | Approved |
| UniProt | Cytoplasm, cytoskeleton; Chromosome, centromere, kinetochore | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- dynactin complex (GO:0005869)
- kinetochore (GO:0000776)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 8 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genomic analyses of intricate interaction of TE-lncRNA overlapping genes with miRNAs in human diseases.. *Genes & genomics*. PMID: 39215947
2. Prognostic Value of Dynactin mRNA Expression in Cutaneous Melanoma.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 29864111
3. Identification of Dysregulated Mechanisms and Potential Biomarkers in Ischemic Stroke Onset.. *International journal of general medicine*. PMID: 34456585
4. Glomerulocystic kidney disease in mice with a targeted inactivation of Wwtr1.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 17251353
5. Genome-Wide Genetic Analysis of Dropout in a Controlled Exercise Intervention in Sedentary Adults With Overweight or Obesity and Cardiometabolic Disease.. *Annals of behavioral medicine : a publication of the Society of Behavioral Medicine*. PMID: 38489667

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 33.0% |
| 置信残基 (pLDDT 70-90) 占比 | 51.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 84.1% |
| 可用 PDB 条目 | 5NW4, 9B7J, 9B85 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5NW4, 9B7J, 9B85）+ AlphaFold高质量预测（pLDDT=82.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047125, IPR011004; Pfam: PF21711 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTR1A | 0.999 | 0.975 | — |
| DCTN4 | 0.999 | 0.995 | — |
| DCTN6 | 0.999 | 0.989 | — |
| DCTN2 | 0.999 | 0.986 | — |
| DCTN1 | 0.999 | 0.958 | — |
| ACTR10 | 0.999 | 0.983 | — |
| DCTN3 | 0.997 | 0.889 | — |
| ACTR1B | 0.993 | 0.918 | — |
| DYNC1H1 | 0.991 | 0.825 | — |
| CAPZA1 | 0.985 | 0.889 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DCTN5-p25 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fadd | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ubc84D | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13081 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| DCTN6-p27 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17652 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpL17 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cnn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Gp150 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 5NW4, 9B7J, 9B85 | pLDDT=82.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Chromosome, centromere, k / Nucleoplasm, Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DCTN5 -- Dynactin subunit 5，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小182 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166847-DCTN5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTN5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTE1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166847-DCTN5/subcellular

![](https://images.proteinatlas.org/63710/1223_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/63710/1223_B5_3_red_green.jpg)
![](https://images.proteinatlas.org/63710/1231_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/63710/1231_B11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BTE1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
