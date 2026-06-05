---
type: protein-evaluation
gene: "BEX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEX1 |
| 蛋白名称 | Protein BEX1 |
| 蛋白大小 | 125 aa / 14.9 kDa |
| UniProt ID | Q9HBH7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 125 aa / 14.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007623, IPR021156; Pfam: PF04538 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DNMT1-mediated methylation of BEX1 regulates stemness and tumorigenicity in liver cancer.. *Journal of hepatology*. PMID: 34217777
2. BEX1 supports the stemness of hepatoblastoma by facilitating Warburg effect in a PPARγ/PDK1 dependent manner.. *British journal of cancer*. PMID: 37715024
3. Bex1 is essential for ciliogenesis and harbours biomolecular condensate-forming capacity.. *BMC biology*. PMID: 35144600
4. BEX1 is an RNA-dependent mediator of cardiomyopathy.. *Nature communications*. PMID: 29192139
5. BEX1 is a critical determinant of viral myocarditis.. *PLoS pathogens*. PMID: 35192678

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.6% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 62.4% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 31.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 31.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007623, IPR021156; Pfam: PF04538 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMO2 | 0.895 | 0.000 | — |
| LDB2 | 0.880 | 0.000 | — |
| LDB1 | 0.868 | 0.000 | — |
| NHLH2 | 0.840 | 0.000 | — |
| CALML4 | 0.748 | 0.000 | — |
| CALML5 | 0.748 | 0.000 | — |
| CALML6 | 0.748 | 0.000 | — |
| CALML3 | 0.748 | 0.000 | — |
| OMP | 0.701 | 0.314 | — |
| TCEAL5 | 0.692 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT31 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTAG1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CNOT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGEA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KLHL20 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OTP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MDFI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT34 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BEX1 — Protein BEX1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小125 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBH7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133169-BEX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBH7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000133169-BEX1/subcellular

![](https://images.proteinatlas.org/78630/1776_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/78630/1776_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78630/1823_D7_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/78630/1823_D7_33_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HBH7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
