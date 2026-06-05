---
type: protein-evaluation
gene: "MNT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MNT — REJECTED (研究热度过高 (PubMed strict=372，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MNT / BHLHD3, ROX |
| 蛋白名称 | Max-binding protein MNT |
| 蛋白大小 | 582 aa / 62.3 kDa |
| UniProt ID | Q99583 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 582 aa / 62.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=372 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 372 |
| PubMed broad count | 2155 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHD3, ROX |

**关键文献**:
1. KDOQI Clinical Practice Guideline for Nutrition in CKD: 2020 Update.. *American journal of kidney diseases : the official journal of the National Kidney Foundation*. PMID: 32829751
2. Nutrition in Kidney Disease: Core Curriculum 2022.. *American journal of kidney diseases : the official journal of the National Kidney Foundation*. PMID: 34862042
3. Nutrition in the Intensive Care Unit-A Narrative Review.. *Nutrients*. PMID: 34445010
4. Alterations of DNA damage response pathway: Biomarker and therapeutic strategy for cancer immunotherapy.. *Acta pharmaceutica Sinica. B*. PMID: 34729299
5. The MYCN oncoprotein is an RNA-binding accessory factor of the nuclear exosome targeting complex.. *Molecular cell*. PMID: 38703770

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 21.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 51.4% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MLX | 0.949 | 0.620 | — |
| MAX | 0.943 | 0.872 | — |
| MXD4 | 0.897 | 0.000 | — |
| MYC | 0.834 | 0.292 | — |
| SIN3A | 0.817 | 0.354 | — |
| MXD3 | 0.739 | 0.621 | — |
| MLXIPL | 0.729 | 0.000 | — |
| MXD1 | 0.727 | 0.292 | — |
| MYCN | 0.702 | 0.060 | — |
| NIF3L1 | 0.666 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| N | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| toy | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Mer | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| beat-IIa | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG1607 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Octbeta2R | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Not1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3085 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pgant6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 无 | pLDDT=59.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. MNT — Max-binding protein MNT，研究基础较多，新颖性有限。
2. 蛋白大小582 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 372 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 372 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99583
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070444-MNT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MNT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99583
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000070444-MNT/subcellular

![](https://images.proteinatlas.org/59532/1045_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/59532/1045_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/59532/1049_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/59532/1049_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/59532/1117_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/59532/1117_A12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99583-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
