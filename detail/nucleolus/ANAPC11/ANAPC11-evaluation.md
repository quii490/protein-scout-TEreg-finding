---
type: protein-evaluation
gene: "ANAPC11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANAPC11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC11 |
| 蛋白名称 | Anaphase-promoting complex subunit 11 |
| 蛋白大小 | 84 aa / 9.8 kDa |
| UniProt ID | Q9NYG5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 84 aa / 9.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.4; PDB: 2MT5, 4R2Y, 4UI9, 5A31, 5G04, 5G05, 5JG6 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051031, IPR024991, IPR001841, IPR013083; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分 (÷1.83)** | | | **75.4/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- anaphase-promoting complex (GO:0005680)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 36 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The APC/C E3 ligase subunit ANAPC11 mediates FOXO3 protein degradation to promote cell proliferation and lymph node metastasis in urothelial bladder cancer.. *Cell death & disease*. PMID: 37573356
2. Integrating machine learning for the identification of ubiquitination-associated genes in moyamoya disease.. *Frontiers in neurology*. PMID: 41036271
3. Zinc supplementation prevents mitotic accumulation in human keratinocyte cell lines upon environmentally relevant arsenic exposure.. *Toxicology and applied pharmacology*. PMID: 36162444
4. Molecular cloning and characterization of a RING-H2 finger protein, ANAPC11, the human homolog of yeast Apc11p.. *Journal of cellular biochemistry*. PMID: 11573242
5. Expression and prognostic value of cell-cycle-associated genes in lung squamous cell carcinoma.. *The journal of gene medicine*. PMID: 39171952

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 82.1% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 2MT5, 4R2Y, 4UI9, 5A31, 5G04, 5G05, 5JG6, 5KHR, 5KHU, 5L9T |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MT5, 4R2Y, 4UI9, 5A31, 5G04, 5G05, 5JG6, 5KHR, 5KHU, 5L9T）+ AlphaFold极高置信度预测（pLDDT=92.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051031, IPR024991, IPR001841, IPR013083; Pfam: PF12861 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANAPC5 | 0.999 | 0.966 | — |
| UBE2C | 0.999 | 0.996 | — |
| ANAPC4 | 0.999 | 0.998 | — |
| CDC20 | 0.999 | 0.851 | — |
| CDC16 | 0.999 | 0.991 | — |
| ANAPC10 | 0.999 | 0.997 | — |
| ANAPC1 | 0.999 | 0.966 | — |
| UBE2S | 0.999 | 0.971 | — |
| CDC23 | 0.999 | 0.973 | — |
| CDC27 | 0.999 | 0.997 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NKD2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CAPN11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MLKL | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZAP70 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| CDC16 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cdc23 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TRIM65 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| RNF111 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 2MT5, 4R2Y, 4UI9, 5A31, 5G04,  | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ANAPC11 — Anaphase-promoting complex subunit 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小84 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYG5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141552-ANAPC11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYG5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:48:35

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000141552-ANAPC11/subcellular

![](https://images.proteinatlas.org/21989/187_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/21989/187_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/21989/188_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/21989/188_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/21989/246_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/21989/246_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYG5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
