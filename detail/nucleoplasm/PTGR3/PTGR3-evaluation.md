---
type: protein-evaluation
gene: "PTGR3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTGR3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTGR3 / ZADH2 |
| 蛋白名称 | Prostaglandin reductase 3 |
| 蛋白大小 | 377 aa / 40.1 kDa |
| UniProt ID | Q8N4Q0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm, Golgi apparatus; UniProt: Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 40.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.2; PDB: 2C0C, 2WEK, 2X1H, 2X7H, 7ZEJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013149, IPR013154, IPR020843, IPR011032, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Peroxisome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZADH2 |

**关键文献**:
1. Insights Into the Peroxisomal Protein Inventory of Zebrafish.. *Frontiers in physiology*. PMID: 35295584
2. Identifying Molecular Modulators of the Vascular Invasion in Rectal Carcinoma: Role of ADAMTS8 and Its Co-Dependent Genes.. *International journal of molecular sciences*. PMID: 40650042

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 90.2% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 91.3% |
| 可用 PDB 条目 | 2C0C, 2WEK, 2X1H, 2X7H, 7ZEJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2C0C, 2WEK, 2X1H, 2X7H, 7ZEJ）+ AlphaFold极高置信度预测（pLDDT=93.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013149, IPR013154, IPR020843, IPR011032, IPR036291; Pfam: PF08240, PF00107 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSHZ1 | 0.659 | 0.000 | — |
| HSDL2 | 0.631 | 0.112 | — |
| PEX5 | 0.623 | 0.510 | — |
| SMIM21 | 0.621 | 0.000 | — |
| ZNF407 | 0.593 | 0.046 | — |
| TYSND1 | 0.582 | 0.000 | — |
| FASN | 0.557 | 0.297 | — |
| C6orf223 | 0.543 | 0.000 | — |
| CRYZL1 | 0.531 | 0.000 | — |
| ARMC6 | 0.531 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PEX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22002062|imex:IM-17176 |
| EBI-6095751 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |
| EBI-6096764 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |
| CAT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| FGL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DBT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CKS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRAPPC10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 2C0C, 2WEK, 2X1H, 2X7H, 7ZEJ | pLDDT=93.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Peroxisome / Vesicles; 额外: Nucleoplasm, Golgi apparatus | 一致 |
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
1. PTGR3 — Prostaglandin reductase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4Q0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180011-PTGR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTGR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4Q0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000180011-PTGR3/subcellular

![](https://images.proteinatlas.org/53646/832_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/53646/832_H4_4_red_green.jpg)
![](https://images.proteinatlas.org/53646/838_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/53646/838_E9_4_red_green.jpg)
![](https://images.proteinatlas.org/53646/986_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/53646/986_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N4Q0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N4Q0 |
| SMART | SM00829; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013149;IPR013154;IPR020843;IPR011032;IPR036291;IPR002364;IPR051397; |
| Pfam | PF08240;PF00107; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180011-PTGR3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLPP | Biogrid | false |
| CYP24A1 | Bioplex | false |
| DBT | Bioplex | false |
| MRPL21 | Bioplex | false |
| PEX5 | Biogrid | false |
| TRAPPC10 | Bioplex | false |
| TRAPPC4 | Bioplex | false |
| TRAPPC5 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
