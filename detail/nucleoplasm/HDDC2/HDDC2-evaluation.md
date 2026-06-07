---
type: protein-evaluation
gene: "HDDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDDC2 / C6orf74, NS5ATP2 |
| 蛋白名称 | 5'-deoxynucleotidase HDDC2 |
| 蛋白大小 | 204 aa / 23.4 kDa |
| UniProt ID | Q7Z4H3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 204 aa / 23.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=94.8; PDB: 4DMB, 4L1J, 4L7E, 4L7W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003607, IPR006674, IPR039356; Pfam: PF13023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.5/180** | |
| **归一化总分** | | | **79.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf74, NS5ATP2 |

**关键文献**:
1. Research Note: Identification of breeding-related candidate genes in Tianjin-monkey chickens by transcriptome analysis.. *Poultry science*. PMID: 37499610
2. Variability of Gene Expression Identifies Transcriptional Regulators of Early Human Embryonic Development.. *PLoS genetics*. PMID: 26288249
3. Steep, coincident, and concordant clines in mitochondrial and nuclear-encoded genes in a hybrid zone between subspecies of Atlantic killifish, Fundulus heteroclitus.. *Ecology and evolution*. PMID: 27547353

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 91.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 4DMB, 4L1J, 4L7E, 4L7W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4DMB, 4L1J, 4L7E, 4L7W）+ AlphaFold高质量预测（pLDDT=94.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003607, IPR006674, IPR039356; Pfam: PF13023 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTAP | 0.812 | 0.000 | — |
| PNP | 0.810 | 0.000 | — |
| NUDT12 | 0.795 | 0.000 | — |
| METTL5 | 0.792 | 0.000 | — |
| NUDT13 | 0.792 | 0.000 | — |
| ADAT3 | 0.698 | 0.000 | — |
| ADAT2 | 0.691 | 0.000 | — |
| SMUG1 | 0.676 | 0.000 | — |
| PRKAG1 | 0.675 | 0.000 | — |
| MRPS14 | 0.635 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| ENSP00000381220.1 | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| COQ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| LCN2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| IKBKG | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POMC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| MTUS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000398153 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 4DMB, 4L1J, 4L7E, 4L7W | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDDC2 — 5'-deoxynucleotidase HDDC2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小204 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4H3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111906-HDDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4H3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000111906-HDDC2/subcellular

![](https://images.proteinatlas.org/35677/381_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/35677/381_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/35677/389_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/35677/389_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/35677/398_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/35677/398_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4H3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4H3 |
| SMART | SM00471; |
| UniProt Domain [FT] | DOMAIN 46..148; /note="HD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01175" |
| InterPro | IPR003607;IPR006674;IPR039356; |
| Pfam | PF13023; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111906-HDDC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IKBKG | Intact | false |
| LCN2 | Intact | false |
| POMC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
