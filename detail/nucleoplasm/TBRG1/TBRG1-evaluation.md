---
type: protein-evaluation
gene: "TBRG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBRG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBRG1 / NIAM |
| 蛋白名称 | Transforming growth factor beta regulator 1 |
| 蛋白大小 | 411 aa / 44.9 kDa |
| UniProt ID | Q3YBR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 411 aa / 44.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.8; PDB: 2WZO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003889, IPR003888, IPR040092; Pfam: PF05965, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **145.0/180** | |
| **归一化总分** | | | **80.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NIAM |

**关键文献**:
1. Development of a Risk Score Model for Osteosarcoma Based on DNA Methylation-Driven Differentially Expressed Genes.. *Journal of oncology*. PMID: 35602303
2. The structure of the FYR domain of transforming growth factor beta regulator 1.. *Protein science : a publication of the Protein Society*. PMID: 20506279
3. Identification of Hub Genes in High-Grade Serous Ovarian Cancer Using Weighted Gene Co-Expression Network Analysis.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 32180586
4. Structural and functional analysis of transforming growth factor beta regulator 1 (TBRG1) in the red swamp crayfish Procambarus clarkii: The initial insight into TBRG1's role in invertebrate immunity.. *Fish & shellfish immunology*. PMID: 38168633
5. NIAM-deficient mice are predisposed to the development of proliferative lesions including B-cell lymphomas.. *PloS one*. PMID: 25393878

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 43.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 56.2% |
| 可用 PDB 条目 | 2WZO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=71.8，有序区 56.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003889, IPR003888, IPR040092; Pfam: PF05965, PF05964 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABL6 | 0.774 | 0.000 | — |
| REEP5 | 0.641 | 0.000 | — |
| ZNF740 | 0.634 | 0.055 | — |
| ADAMTSL2 | 0.604 | 0.000 | — |
| INO80E | 0.589 | 0.233 | — |
| FBN1 | 0.586 | 0.066 | — |
| TMSB10 | 0.578 | 0.000 | — |
| CDKN2A | 0.542 | 0.070 | — |
| ADAMTS10 | 0.513 | 0.000 | — |
| GARNL3 | 0.493 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000409016.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0G2RNT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fadB/acbP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RDJ6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RIX9 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RKM4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| hpt | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| b4154 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| yscH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SNRPB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 2WZO | pLDDT=71.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TBRG1 — Transforming growth factor beta regulator 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小411 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3YBR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154144-TBRG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBRG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3YBR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000154144-TBRG1/subcellular

![](https://images.proteinatlas.org/55645/883_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/55645/883_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/55645/886_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/55645/886_H11_4_red_green.jpg)
![](https://images.proteinatlas.org/68022/1250_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/68022/1250_E3_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3YBR2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
