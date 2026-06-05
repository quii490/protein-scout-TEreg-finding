---
type: protein-evaluation
gene: "TLE5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TLE5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLE5 / AES, GRG, GRG5 |
| 蛋白名称 | TLE family member 5 |
| 蛋白大小 | 197 aa / 22.0 kDa |
| UniProt ID | Q08117 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 197 aa / 22.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005617, IPR009146; Pfam: PF03920 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AES, GRG, GRG5 |

**关键文献**:
1. Aggregatibacteraphrophilus T6SS Effectors in Host-Bacterial Interactions.. *Journal of dental research*. PMID: 40574274
2. Cloning, purification, crystallization and preliminary X-ray studies of the putative type VI secretion immunity protein Tli5 (PA5088) from Pseudomonas aeruginosa.. *Acta crystallographica. Section F, Structural biology communications*. PMID: 25005085
3. Structure of the type VI secretion phospholipase effector Tle1 provides insight into its hydrolysis and membrane targeting.. *Acta crystallographica. Section D, Biological crystallography*. PMID: 25084336
4. Structural and SAXS analysis of Tle5-Tli5 complex reveals a novel inhibition mechanism of H2-T6SS in Pseudomonas aeruginosa.. *Protein science : a publication of the Protein Society*. PMID: 28758353

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 51.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 31.5% |
| 有序区域 (pLDDT>70) 占比 | 55.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 55.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005617, IPR009146; Pfam: PF03920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLE3 | 0.932 | 0.773 | — |
| TLE1 | 0.919 | 0.742 | — |
| TLE4 | 0.913 | 0.825 | — |
| PTRH2 | 0.893 | 0.510 | — |
| TLE2 | 0.858 | 0.677 | — |
| RIPPLY1 | 0.825 | 0.791 | — |
| TLE7 | 0.803 | 0.000 | — |
| VENTX | 0.796 | 0.791 | — |
| TLE6 | 0.781 | 0.050 | — |
| SIX6 | 0.772 | 0.713 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000221561.7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000317537.4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MED31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SH3GL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SNCAIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CCL7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GABARAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL18A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TLE5 — TLE family member 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小197 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08117
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104964-TLE5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLE5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08117
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104964-TLE5/subcellular

![](https://images.proteinatlas.org/49499/751_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/49499/751_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/49499/858_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/49499/858_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/49499/967_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/49499/967_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08117-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
