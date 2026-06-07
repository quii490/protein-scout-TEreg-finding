---
type: protein-evaluation
gene: "TSPAN31"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSPAN31 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSPAN31 / SAS |
| 蛋白名称 | Tetraspanin-31 |
| 蛋白大小 | 210 aa / 23.1 kDa |
| UniProt ID | Q12999 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytokinetic bridge, Cytoso; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 210 aa / 23.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018499, IPR000301; Pfam: PF00335 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytokinetic bridge, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SAS |

**关键文献**:
1. The role of tetraspanins pan-cancer.. *iScience*. PMID: 35992081
2. Role of Tetraspanins in Hepatocellular Carcinoma.. *Frontiers in oncology*. PMID: 34540692
3. TSPAN31 Activates Fatty Acid Metabolism and PI3K/AKT Pathway to Promote Tumor Progression in Breast Cancer.. *Molecular carcinogenesis*. PMID: 40135650
4. Overexpression of Tetraspanin31 contributes to malignant potential and poor outcomes in gastric cancer.. *Cancer science*. PMID: 35307915
5. TSPAN31 regulates the proliferation, migration, and apoptosis of gastric cancer cells through the METTL1/CCT2 pathway.. *Translational oncology*. PMID: 35429902

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.3 |
| 高置信度残基 (pLDDT>90) 占比 | 64.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.3，有序区 91.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018499, IPR000301; Pfam: PF00335 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD53 | 0.715 | 0.000 | — |
| CD37 | 0.687 | 0.000 | — |
| TSPAN17 | 0.668 | 0.000 | — |
| CD63 | 0.646 | 0.165 | — |
| TM4SF1 | 0.632 | 0.000 | — |
| CD81 | 0.627 | 0.174 | — |
| METTL1 | 0.609 | 0.000 | — |
| TSPAN5 | 0.566 | 0.000 | — |
| CD9 | 0.562 | 0.000 | — |
| OS9 | 0.555 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| eIF4E5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MED6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| FoxL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15545 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mRpS6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| BMP10 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TSPAN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC30A2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYP4F2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NAT8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.3 + PDB: 无 | pLDDT=89.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus; 额外: Nucleoplasm, Cytokinetic brid | 一致 |
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
1. TSPAN31 — Tetraspanin-31，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小210 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12999
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135452-TSPAN31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPAN31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12999
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000135452-TSPAN31/subcellular

![](https://images.proteinatlas.org/30758/1764_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30758/1764_G4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/30758/1768_F9_18_cr5950c68e51359_blue_red_green.jpg)
![](https://images.proteinatlas.org/30758/1768_F9_4_cr5950c68e51bf5_blue_red_green.jpg)
![](https://images.proteinatlas.org/30758/1822_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30758/1822_H3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12999-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12999 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018499;IPR000301; |
| Pfam | PF00335; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135452-TSPAN31/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BMP10 | Intact | false |
| CYP4F2 | Intact | false |
| NAT8 | Intact | false |
| SLC30A2 | Intact | false |
| TSPAN2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
