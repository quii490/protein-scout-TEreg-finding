---
type: protein-evaluation
gene: "KLHL35"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL35 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL35 |
| 蛋白名称 | KLHL35 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | KLHL35 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome; 额外: Nucleoli fibrillar center; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Nucleoli fibrillar center | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The potential role of DNA methylation in abdominal aortic aneurysms.. *International journal of molecular sciences*. PMID: 25993294
2. Developing a pyroptosis-related gene signature to better predict the prognosis and immune status of patients with head and neck squamous cell carcinoma.. *Frontiers in genetics*. PMID: 36685979
3. Comprehensive analysis of KLHL35 expression and its prognostic value in cancer: implications for colorectal cancer diagnosis and therapy.. *Discover oncology*. PMID: 41114922
4. scBPGRN: Integrating single-cell multi-omics data to construct gene regulatory networks based on BP neural network.. *Computers in biology and medicine*. PMID: 36335815
5. Tissue-Specific Gene Expression during Productive Human Papillomavirus 16 Infection of Cervical, Foreskin, and Tonsil Epithelium.. *Journal of virology*. PMID: 31189705

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CORO6 | 0.537 | 0.000 | — |
| TCP11 | 0.527 | 0.000 | — |
| ZSCAN18 | 0.516 | 0.059 | — |
| ANKS1A | 0.516 | 0.053 | — |
| PI15 | 0.500 | 0.000 | — |
| GCC2 | 0.495 | 0.000 | — |
| FAM180A | 0.485 | 0.000 | — |
| CCDC8 | 0.483 | 0.000 | — |
| SCUBE3 | 0.478 | 0.000 | — |
| DLEU7 | 0.470 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APPBP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM25C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UBTD2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NCK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CALCOCO2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA6L9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ALAS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NUDCD3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Centrosome; 额外: Nucleoli fibrillar ce | 待确认 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KLHL35 — KLHL35 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/KLHL35
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149243-KLHL35/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL35
- AlphaFold: https://alphafold.ebi.ac.uk/entry/KLHL35
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149243-KLHL35/subcellular

![](https://images.proteinatlas.org/39864/1179_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/39864/1179_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/39864/517_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/39864/517_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/39864/520_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/39864/520_H6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PF15 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 41..119; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037"; DOMAIN 146..248; /note="BACK" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR015915;IPR006652;IPR030601;IPR011333; |
| Pfam | PF07707;PF00651;PF01344;PF24681; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149243-KLHL35/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALAS1 | Intact | false |
| APPBP2 | Intact | false |
| CALCOCO2 | Intact | false |
| FAM25A | Intact | false |
| GOLGA6L9 | Intact | false |
| NCK2 | Intact | false |
| UBTD2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
