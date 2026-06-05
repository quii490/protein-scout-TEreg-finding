---
type: protein-evaluation
gene: "TCF21"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TCF21 — REJECTED (研究热度过高 (PubMed strict=196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF21 / BHLHA23, POD1 |
| 蛋白名称 | Transcription factor 21 |
| 蛋白大小 | 179 aa / 19.7 kDa |
| UniProt ID | O43680 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 179 aa / 19.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 196 |
| PubMed broad count | 363 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA23, POD1 |

**关键文献**:
1. Atheroprotective roles of smooth muscle cell phenotypic modulation and the TCF21 disease gene as revealed by single-cell analysis.. *Nature medicine*. PMID: 31359001
2. Cardiac Reprogramming and Gata4 Overexpression Reduce Fibrosis and Improve Diastolic Dysfunction in Heart Failure With Preserved Ejection Fraction.. *Circulation*. PMID: 39673349
3. Direct Reprogramming Improves Cardiac Function and Reverses Fibrosis in Chronic Myocardial Infarction.. *Circulation*. PMID: 36503256
4. Single-cell insights: pioneering an integrated atlas of chromatin accessibility and transcriptomic landscapes in diabetic cardiomyopathy.. *Cardiovascular diabetology*. PMID: 38664790
5. Transcription Factor 21 Regulates Cardiac Myofibroblast Formation and Fibrosis.. *Circulation research*. PMID: 39629593

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 24.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 31.8% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 36.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 36.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APLP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KLF15 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Q81U20 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| tolR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| y1093 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| poxB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MYOD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCF12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SDCBP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 无 | pLDDT=66.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TCF21 — Transcription factor 21，研究基础较多，新颖性有限。
2. 蛋白大小179 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 196 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 196 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43680
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118526-TCF21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43680
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000118526-TCF21/subcellular

![](https://images.proteinatlas.org/25769/2032_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/25769/2032_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/25769/2064_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/25769/2064_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/25769/2089_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/25769/2089_B3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43680-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
