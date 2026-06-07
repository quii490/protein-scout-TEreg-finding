---
type: protein-evaluation
gene: "LACTBL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LACTBL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LACTBL1 |
| 蛋白名称 | Beta-lactamase-like protein 1 |
| 蛋白大小 | 579 aa / 63.5 kDa |
| UniProt ID | A8MY62 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 579 aa / 63.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001466, IPR012338, IPR051478; Pfam: PF00144 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genome-Wide Association Analysis to Search for New Loci Associated with Lifelong Premature Ejaculation Risk in Chinese Male Han Population.. *The world journal of men's health*. PMID: 35021295

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.3 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.3，有序区 97.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001466, IPR012338, IPR051478; Pfam: PF00144 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHST7 | 0.561 | 0.000 | — |
| SNRPB2 | 0.530 | 0.000 | — |
| RS1 | 0.514 | 0.000 | — |
| KLHL24 | 0.499 | 0.000 | — |
| TMEM154 | 0.480 | 0.000 | — |
| NME5 | 0.462 | 0.000 | — |
| LEMD3 | 0.437 | 0.000 | — |
| SSBP3 | 0.432 | 0.000 | — |
| PLA2G4D | 0.418 | 0.000 | — |
| PLA2G4E | 0.415 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ITM2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-29868|pubmed:34446781 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 1
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.3 + PDB: 无 | pLDDT=92.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 11 + 1 interactions | 数据充分 |

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
1. LACTBL1 — Beta-lactamase-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小579 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MY62
- Protein Atlas: https://www.proteinatlas.org/ENSG00000215906-LACTBL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LACTBL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MY62
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000215906-LACTBL1/subcellular

![](https://images.proteinatlas.org/66810/1956_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66810/1956_E1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66810/1976_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66810/1976_C5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66810/2043_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66810/2043_G3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MY62-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A8MY62 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001466;IPR012338;IPR051478; |
| Pfam | PF00144; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000215906-LACTBL1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
