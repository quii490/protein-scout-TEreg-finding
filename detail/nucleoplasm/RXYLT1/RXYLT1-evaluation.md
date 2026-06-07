---
type: protein-evaluation
gene: "RXYLT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RXYLT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RXYLT1 / TMEM5 |
| 蛋白名称 | Ribitol-5-phosphate xylosyltransferase 1 |
| 蛋白大小 | 443 aa / 51.1 kDa |
| UniProt ID | Q9Y2B1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 443 aa / 51.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR055286, IPR057538, IPR057539; Pfam: PF24785, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM5 |

**关键文献**:
1. Walker-Warburg syndrome: A case report of congenital muscular dystrophy with hydrocephalus.. *Radiology case reports*. PMID: 39253050
2. Chemical and Chemo-Enzymatic Syntheses of Glycans Containing Ribitol Phosphate Scaffolding of Matriglycan.. *ACS chemical biology*. PMID: 35670527
3. A Novel Defined Hypoxia-Related Gene Signature for Prognostic Prediction of Patients With Ewing Sarcoma.. *Frontiers in genetics*. PMID: 35719404
4. RETINAL MANIFESTATIONS OF WALKER-WARBURG SYNDROME IN TWO SIBLINGS WITH RXYLT1 MUTATIONS.. *Retinal cases & brief reports*. PMID: 36007194
5. Targeting the xylosyltransferase TMEM5 in glioblastoma to modulate CLOCK and CRY1 expression and restore temozolomide sensitivity via the circadian signaling axis.. *European journal of pharmaceutical sciences : official journal of the European Federation for Pharmaceutical Sciences*. PMID: 41791532

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 71.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 11.3% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.5，有序区 82.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055286, IPR057538, IPR057539; Pfam: PF24785, PF24786 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FKRP | 0.991 | 0.000 | — |
| B4GAT1 | 0.985 | 0.000 | — |
| FKTN | 0.936 | 0.421 | — |
| POMGNT1 | 0.905 | 0.512 | — |
| POMGNT2 | 0.893 | 0.000 | — |
| B3GALNT2 | 0.878 | 0.000 | — |
| POMK | 0.876 | 0.000 | — |
| POMT2 | 0.862 | 0.000 | — |
| POMT1 | 0.862 | 0.000 | — |
| GMPPB | 0.812 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 无 | pLDDT=85.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RXYLT1 — Ribitol-5-phosphate xylosyltransferase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小443 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2B1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118600-RXYLT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RXYLT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2B1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000118600-RXYLT1/subcellular

![](https://images.proteinatlas.org/64014/1139_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/64014/1139_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/64014/1192_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64014/1192_D2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2B1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2B1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR055286;IPR057538;IPR057539; |
| Pfam | PF24785;PF24786; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118600-RXYLT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| POMGNT1 | Intact, Biogrid | true |
| FKRP | Intact | false |
| FKTN | Intact | false |
| WFS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
