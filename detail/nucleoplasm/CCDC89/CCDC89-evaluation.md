---
type: protein-evaluation
gene: "CCDC89"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC89 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC89 / BOIP |
| 蛋白名称 | Coiled-coil domain-containing protein 89 |
| 蛋白大小 | 374 aa / 43.8 kDa |
| UniProt ID | Q8N998 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 43.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.1; PDB: 8WQA, 8WQB, 8WQD, 8WQH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043450 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BOIP |

**关键文献**:
1. CCDC89 is required for optimal sperm motility and male fertility in mammals.. *Human reproduction (Oxford, England)*. PMID: 40591933
2. The Cilia-Associated Protein CCDC89 Is Dispensable for Male Fertility in Mice.. *Cytoskeleton (Hoboken, N.J.)*. PMID: 41074672

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 76.0% |
| 可用 PDB 条目 | 8WQA, 8WQB, 8WQD, 8WQH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8WQA, 8WQB, 8WQD, 8WQH）+ AlphaFold高质量预测（pLDDT=83.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043450 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EFCAB12 | 0.600 | 0.000 | — |
| SPACA7 | 0.559 | 0.000 | — |
| CCDC182 | 0.543 | 0.000 | — |
| HEY1 | 0.517 | 0.092 | — |
| FRG2B | 0.507 | 0.000 | — |
| KRTAP10-1 | 0.507 | 0.000 | — |
| TSPY4 | 0.476 | 0.000 | — |
| C1orf194 | 0.458 | 0.000 | — |
| KRTAP4-3 | 0.445 | 0.000 | — |
| MFSD6L | 0.438 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TSFM | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PIK3R3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LRRC45 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM50B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZMYM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBLN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS27A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 8WQA, 8WQB, 8WQD, 8WQH | pLDDT=83.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

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
1. CCDC89 — Coiled-coil domain-containing protein 89，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N998
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179071-CCDC89/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC89
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N998
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000179071-CCDC89/subcellular

![](https://images.proteinatlas.org/40628/1296_A8_4_red_green.jpg)
![](https://images.proteinatlas.org/40628/1296_A8_5_red_green.jpg)
![](https://images.proteinatlas.org/40628/1336_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/40628/1336_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/40628/1413_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/40628/1413_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N998-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N998 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043450; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179071-CCDC89/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM50B | Intact | false |
| LRRC45 | Intact | false |
| PIK3R3 | Intact | false |
| TSFM | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
