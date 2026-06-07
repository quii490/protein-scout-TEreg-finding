---
type: protein-evaluation
gene: "CCDC150"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC150 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC150 |
| 蛋白名称 | Coiled-coil domain-containing protein 150 |
| 蛋白大小 | 1101 aa / 128.8 kDa |
| UniProt ID | Q8NCX0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1101 aa / 128.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038807 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Enzalutamide-induced signatures revealed by epigenetic plasticity using single-cell multi-omics sequencing in prostate cancer.. *Molecular therapy. Nucleic acids*. PMID: 36910711
2. CCNB1 and AURKA are critical genes for prostate cancer progression and castration-resistant prostate cancer resistant to vinblastine.. *Frontiers in endocrinology*. PMID: 36601001
3. Gradient Rotating Magnetic Fields Impairing F-Actin-Related Gene CCDC150 to Inhibit Triple-Negative Breast Cancer Metastasis by Inactivating TGF-β1/SMAD3 Signaling Pathway.. *Research (Washington, D.C.)*. PMID: 38420580
4. A genome-wide association study on frequent exacerbation of asthma depending on smoking status.. *Respiratory medicine*. PMID: 35606283

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 12.6% |
| 置信残基 (pLDDT 70-90) 占比 | 56.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.2，有序区 69.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038807 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC77 | 0.616 | 0.000 | — |
| C18orf54 | 0.596 | 0.000 | — |
| ARMH2 | 0.581 | 0.000 | — |
| GTF3C3 | 0.571 | 0.000 | — |
| C9orf40 | 0.568 | 0.000 | — |
| C3orf14 | 0.559 | 0.000 | — |
| NEMP1 | 0.554 | 0.000 | — |
| CCDC34 | 0.549 | 0.000 | — |
| DEPDC1B | 0.548 | 0.000 | — |
| CEP85 | 0.536 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSMB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| NUP62 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| EFHC1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| RAD50 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CFAP161 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PRPF18 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NUTF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 无 | pLDDT=74.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC150 — Coiled-coil domain-containing protein 150，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCX0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144395-CCDC150/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC150
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCX0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000144395-CCDC150/subcellular

![](https://images.proteinatlas.org/48104/742_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/48104/742_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/48104/780_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/48104/780_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/48104/788_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/48104/788_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NCX0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NCX0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038807; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144395-CCDC150/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EFHC1 | Intact | false |
| GOLGA2 | Intact | false |
| NUP62 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
