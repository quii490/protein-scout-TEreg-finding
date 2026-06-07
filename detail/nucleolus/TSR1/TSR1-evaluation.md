---
type: protein-evaluation
gene: "TSR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSR1 / KIAA1401 |
| 蛋白名称 | Pre-rRNA-processing protein TSR1 homolog |
| 蛋白大小 | 804 aa / 91.8 kDa |
| UniProt ID | Q2NL82 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 804 aa / 91.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.2; PDB: 6G18, 6G4S, 6G4W, 6G51, 6G53, 6ZMT, 6ZN5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012948, IPR039761, IPR007034, IPR030387; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1401 |

**关键文献**:
1. Endothelial transferrin receptor 1 contributes to thrombogenesis through cascade ferroptosis.. *Redox biology*. PMID: 38241836
2. Isthmin-A Multifaceted Protein Family.. *Cells*. PMID: 36611811
3. Pathogenic TSR1 Gene Variants in Patients With Spontaneous Coronary Artery Dissection.. *Journal of the American College of Cardiology*. PMID: 31296288
4. Association of TSR1 Variants and Spontaneous Coronary Artery Dissection.. *Journal of the American College of Cardiology*. PMID: 31296287
5. Studies of congenital cataract-related TSR1 mutation and its expression in the lens.. *Yi chuan = Hereditas*. PMID: 32102773

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 30.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 76.3% |
| 可用 PDB 条目 | 6G18, 6G4S, 6G4W, 6G51, 6G53, 6ZMT, 6ZN5, 7WTS, 7WTT, 7WTU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6G18, 6G4S, 6G4W, 6G51, 6G53, 6ZMT, 6ZN5, 7WTS, 7WTT, 7WTU）+ AlphaFold极高置信度预测（pLDDT=80.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012948, IPR039761, IPR007034, IPR030387; Pfam: PF08142, PF04950, PF22298 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Aldh | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Drice | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17127 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13044 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| NetB | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| ENP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HRR25 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RIO2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| DIM1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 6G18, 6G4S, 6G4W, 6G51, 6G53,  | pLDDT=80.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSR1 — Pre-rRNA-processing protein TSR1 homolog，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小804 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2NL82
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167721-TSR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2NL82
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000167721-TSR1/subcellular

![](https://images.proteinatlas.org/53087/1050_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/53087/1050_F5_7_red_green.jpg)
![](https://images.proteinatlas.org/53087/861_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/53087/861_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/53087/880_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/53087/880_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2NL82-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2NL82 |
| SMART | SM00785;SM01362; |
| UniProt Domain [FT] | DOMAIN 81..242; /note="Bms1-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01051" |
| InterPro | IPR012948;IPR039761;IPR007034;IPR030387; |
| Pfam | PF08142;PF04950;PF22298; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167721-TSR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BYSL | Biogrid, Opencell, Bioplex | true |
| CSNK2A2 | Biogrid, Opencell | true |
| FAU | Biogrid, Opencell | true |
| FTSJ3 | Biogrid, Opencell | true |
| HNRNPU | Biogrid, Opencell | true |
| KPNB1 | Biogrid, Opencell, Bioplex | true |
| LTV1 | Biogrid, Opencell, Bioplex | true |
| NCL | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
