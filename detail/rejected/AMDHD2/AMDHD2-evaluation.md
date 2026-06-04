---
type: protein-evaluation
gene: "AMDHD2"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AMDHD2 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AMDHD2 |
| 蛋白大小 | 409 aa / 43.7 kDa |
| UniProt ID | Q9Y303 |
| 蛋白全名 | N-acetylglucosamine-6-phosphate deacetylase |
| HPA IF 主定位 | Nucleoli, Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Nucleoli+Cytosol双主定位；核仁定位明确但胞质也有 |
| 蛋白大小 | 9/10 | ×1 | 9 | 409aa/43.7kDa，理想实验范围 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | pLDDT=94.5；PDB 7NUT/7NUU (X-ray 1.84-1.90A, 全长二聚体) |
| 调控结构域 | 4/10 | ×2 | 8 | IPR006680 Amidohydrolase；氨基糖代谢酶，无调控域 |
| PPI网络 | 4/10 | ×3 | 12 | GNPDA1(0.994实验), GNPDA2(0.994实验); 己糖胺通路 |
| **加权总分** | | | **121/180** | |
| **归一化总分 (÷1.8)** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoli (main), Cytosol (main) | Approved |
| UniProt | 无亚细胞定位注释 | |
| GO-CC | GO:0005829 (cytosol, TAS), GO:0005634 (nucleus, HDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved IF 将 Nucleoli 和 Cytosol 并列为主定位，核仁信号明确。GO-CC 也含 nucleus (HDA)。**评分: 3/10**。

#### 3.2 蛋白大小评估

409 aa / 43.7 kDa。理想实验范围。PDB 显示为同源二聚体。**评分: 9/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 6 |
| PubMed symbol_only | 7 |
| 主要方向 | 己糖胺途径、氨基糖代谢、COPD |

**评价**: PubMed 仅 6 篇，极端新颖。AMDHD2 催化 GlcNGc-6-P 脱乙酰化，关键文献为 2022 eLife 论文。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Kroef V et al. (2022). "GFPT2/GFAT2 and AMDHD2 act in tandem to control the hexosamine pathway." *eLife*. PMID: 35229715 — 核心功能文献，eLife
2. Xiao X et al. (2025). "Identifying KL-6-Associated Immune Cell Signatures and Key Genes in Emphysematous COPD." *J Inflamm Res*. PMID: 40416710
3. Ding H et al. (2022). "Differentially expressed mRNAs and their upstream miR-491-5p in patients with coronary atherosclerosis." *Korean J Physiol Pharmacol*. PMID: 35477546
4. Pan B et al. (2022). "Identification of Body Size Determination Related Candidate Genes in Domestic Pig." *Animals*. PMID: 35883386
5. Selionova M et al. (2024). "Genome-Wide Association Study of Milk Composition in Karachai Goats." *Animals*. PMID: 38275787

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.5 |
| pLDDT > 90 (Very High) | 86.6% |
| pLDDT 70-90 (High) | 11.0% |
| pLDDT 50-70 (Medium) | 0.7% |
| pLDDT < 50 (Low) | 1.7% |
| 有序区域 (pLDDT>70) | 97.6% |
| 实验结构 (PDB) | 7NUT (X-ray 1.90A), 7NUU (X-ray 1.84A, 全长1-409, 同源二聚体) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 含两个高分辨率 X-ray 结构 (1.84-1.90 A)，为全长同源二聚体。预测与实验高度一致。**评分: 10/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR006680 (Amidohydrolase-related); IPR003764 (N-acetylglucosamine-6-phosphate deacetylase); IPR011059 (Metal-dependent hydrolase); IPR032466 (Metal-dependent hydrolase) |
| Pfam | PF01979 (Amidohydro_1) |

AMDHD2 为 N-乙酰葡萄糖胺-6-磷酸脱乙酰酶，水解 Neu5Gc 降解途径中的 GlcNGc-6-P。含 TIM 桶状折叠，形成同源二聚体。功能纯代谢，无已知调控域。**评分: 4/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| GNPDA1 | 0.994 | 0.79 (强实验) |
| GNPDA2 | 0.994 | 0.835 (强实验) |
| GNE | 0.898 | 0 |
| GFPT2 | 0.819 | 0 |

GNPDA1/GNPDA2 有强实验互作，与己糖胺途径功能一致。IntAct: GNPDA2 (Y2H array), GNPDA1 (co-IP), TRIP13 (validated Y2H), RAN/HIP1/LAMP2/CASP6 (Y2H array)。PPI 集中于氨基糖代谢。**评分: 4/10**。

### 4. 拒绝理由

AMDHD2 nuclear_score=3 (≤3 阈值)，核心原因：
- 核定位双主定位 (Nucleoli+Cytosol)，核特异性不足
- 功能为氨基糖代谢酶
- 无核调控结构域

**结论**: 虽极度新颖 (6篇) 且结构优质 (PDB 1.84A全长二聚体)，但代谢酶功能与核调控无关，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y303
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y303
- PDB: https://www.rcsb.org/structure/7NUT
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AMDHD2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000162066-AMDHD2
