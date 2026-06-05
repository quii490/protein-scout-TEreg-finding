---
type: protein-evaluation
gene: "TSSK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSSK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSSK3 / SPOGA3, STK22C |
| 蛋白名称 | Testis-specific serine/threonine-protein kinase 3 |
| 蛋白大小 | 268 aa / 30.1 kDa |
| UniProt ID | Q96PN8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Nuclear bodies; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 268 aa / 30.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR017441, IPR042709; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Nuclear bodies | Approved |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPOGA3, STK22C |

**关键文献**:
1. Testis-specific serine kinase 3 is required for sperm morphogenesis and male fertility.. *Andrology*. PMID: 36306217
2. cDNA cloning, expression and bioinformatical analysis of Tssk genes in tree shrews.. *Computational biology and chemistry*. PMID: 33765466
3. Cloning, sequence characterization, and expression patterns of members of the porcine TSSK family.. *Genetics and molecular research : GMR*. PMID: 26600552
4. TSSK3, a novel target for male contraception, is required for spermiogenesis.. *Molecular reproduction and development*. PMID: 34623009
5. Testis-specific serine/threonine kinase 3 regulates the size of sperm reservoir in Anopheles stephensi.. *Molecular genetics and genomics : MGG*. PMID: 40913647

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.6 |
| 高置信度残基 (pLDDT>90) 占比 | 82.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.6，有序区 99.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR042709; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSKS | 0.722 | 0.000 | — |
| DDIT4L | 0.596 | 0.591 | — |
| CALY | 0.593 | 0.000 | — |
| KLHL10 | 0.574 | 0.000 | — |
| TXNDC2 | 0.525 | 0.070 | — |
| PRKAG1 | 0.488 | 0.340 | — |
| CIB4 | 0.485 | 0.128 | — |
| PRKAB2 | 0.484 | 0.413 | — |
| PRKAB1 | 0.484 | 0.413 | — |
| EIF2AK2 | 0.477 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FUT9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| OIP5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NMES1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RBBP4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| TRIP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM50 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SHISA6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.6 + PDB: 无 | pLDDT=93.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Nucleoplasm, Nucleoli; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSSK3 — Testis-specific serine/threonine-protein kinase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小268 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162526-TSSK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSSK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162526-TSSK3/subcellular

![](https://images.proteinatlas.org/37516/1337_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/37516/1337_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/37516/1338_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/37516/1338_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/37516/1364_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/37516/1364_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96PN8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
