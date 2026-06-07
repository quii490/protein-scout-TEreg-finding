---
type: protein-evaluation
gene: "TRIM51"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM51 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM51 / SPRYD5 |
| 蛋白名称 | Tripartite motif-containing protein 51 |
| 蛋白大小 | 452 aa / 52.3 kDa |
| UniProt ID | Q9BSJ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 52.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPRYD5 |

**关键文献**:
1. Polygenic risk scores and risk stratification in deep vein thrombosis.. *Thrombosis research*. PMID: 37331118
2. Whole exome sequencing and rare variant association study to identify genetic modifiers, KLF1 mutations, and a novel double mutation in Thai patients with hemoglobin E/beta-thalassemia.. *Hematology (Amsterdam, Netherlands)*. PMID: 36939018
3. The role of TRIM51 as a multipurpose biomarker in melanoma.. *Translational cancer research*. PMID: 35116291
4. Intrinsic Disorder in Human Proteins Encoded by Core Duplicon Gene Families.. *The journal of physical chemistry. B*. PMID: 32880174

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 63.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 87.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.6，有序区 87.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR003877; Pfam: PF00622, PF15227 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC45A3 | 0.666 | 0.000 | — |
| MS4A2 | 0.587 | 0.000 | — |
| GATA2 | 0.573 | 0.053 | — |
| PRAMEF11 | 0.555 | 0.105 | — |
| PRAMEF13 | 0.520 | 0.105 | — |
| PRAMEF1 | 0.517 | 0.105 | — |
| TRIM56 | 0.478 | 0.000 | — |
| OR8J3 | 0.476 | 0.000 | — |
| TRIM52 | 0.458 | 0.000 | — |
| TRIM54 | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RNF40 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPRY2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 无 | pLDDT=86.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRIM51 — Tripartite motif-containing protein 51，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSJ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124900-TRIM51/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM51
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSJ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000124900-TRIM51/subcellular

![](https://images.proteinatlas.org/77883/1692_F9_18_cr57d15e8ea1e8a_blue_red_green.jpg)
![](https://images.proteinatlas.org/77883/1692_F9_23_cr57d15e94dfaf7_blue_red_green.jpg)
![](https://images.proteinatlas.org/77883/1757_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77883/1757_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77883/1769_C8_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/77883/1769_C8_35_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSJ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BSJ1 |
| SMART | SM00336;SM00184; |
| UniProt Domain [FT] | DOMAIN 269..452; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR003877;IPR050143;IPR000315;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00622;PF15227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124900-TRIM51/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
