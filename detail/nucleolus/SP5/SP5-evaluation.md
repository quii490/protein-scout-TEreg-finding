---
type: protein-evaluation
gene: "SP5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SP5 — REJECTED (研究热度过高 (PubMed strict=168，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP5 |
| 蛋白名称 | Transcription factor Sp5 |
| 蛋白大小 | 398 aa / 42.0 kDa |
| UniProt ID | Q6BEB4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 398 aa / 42.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=168 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 168 |
| PubMed broad count | 472 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Directed Differentiation of Human Induced Pluripotent Stem Cells to Heart Valve Cells.. *Circulation*. PMID: 38357822
2. Transcription factors SP5 and SP8 drive primary cilia formation in mammalian embryos.. *Science (New York, N.Y.)*. PMID: 40875857
3. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
4. Base-pair resolution reveals clustered R-loops and DNA damage-susceptible R-loops.. *Molecular cell*. PMID: 40112807
5. Transcription factors SP5 and SP8 drive primary cilia formation.. *bioRxiv : the preprint server for biology*. PMID: 40501818

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 2.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 20.1% |
| 低置信 (pLDDT<50) 占比 | 54.3% |
| 有序区域 (pLDDT>70) 占比 | 25.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 25.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHAC2 | 0.585 | 0.000 | — |
| ASB3 | 0.569 | 0.091 | — |
| MYO3B | 0.512 | 0.000 | — |
| PEX11B | 0.498 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SFTPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HPN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CLDN5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BSCL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMPRSS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SEC22A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CXCL9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PpD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| N | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| TMEM79 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 12
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 4 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SP5 — Transcription factor Sp5，研究基础较多，新颖性有限。
2. 蛋白大小398 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 168 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 168 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6BEB4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204335-SP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6BEB4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000204335-SP5/subcellular

![](https://images.proteinatlas.org/74123/1526_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/74123/1526_G1_3_red_green.jpg)
![](https://images.proteinatlas.org/74123/1537_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/74123/1537_B7_3_red_green.jpg)
![](https://images.proteinatlas.org/74123/1548_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/74123/1548_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6BEB4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
