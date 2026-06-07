---
type: protein-evaluation
gene: "KLHL23"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL23 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL23 |
| 蛋白名称 | Kelch-like protein 23 |
| 蛋白大小 | 558 aa / 63.9 kDa |
| UniProt ID | Q8NBE8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Actin filaments; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 63.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR030566, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sofosbuvir induces gene expression for promoting cell proliferation and migration of hepatocellular carcinoma cells.. *Aging*. PMID: 35833210
2. Confirming whether KLHL23 deficiency potentiates migration in urothelial carcinoma.. *The Chinese journal of physiology*. PMID: 34169920
3. Molecular gene signature and prognosis of non-small cell lung cancer.. *Oncotarget*. PMID: 27437769
4. Unveiling KLHL23 as a key immune regulator in hepatocellular carcinoma through integrated analysis.. *Aging*. PMID: 39636292
5. Dysfunction of Cullin 3 RING E3 ubiquitin ligase causes vasoconstriction and increased sodium reabsorption in diabetes.. *Archives of biochemistry and biophysics*. PMID: 34343486

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.2 |
| 高置信度残基 (pLDDT>90) 占比 | 68.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 94.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.2，有序区 94.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR030566, IPR015915; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.705 | 0.644 | — |
| PHOSPHO2 | 0.635 | 0.000 | — |
| ZNF551 | 0.609 | 0.059 | — |
| AMDHD1 | 0.592 | 0.591 | — |
| DCDC2C | 0.505 | 0.000 | — |
| PRR5-ARHGAP8 | 0.505 | 0.000 | — |
| ACOT8 | 0.504 | 0.504 | — |
| KNCN | 0.485 | 0.000 | — |
| RPL17-C18orf32 | 0.479 | 0.000 | — |
| DCDC2B | 0.477 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| PLS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AMDHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BSPRY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAXO5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.2 + PDB: 无 | pLDDT=90.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Actin filaments; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

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
1. KLHL23 — Kelch-like protein 23，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBE8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213160-KLHL23/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL23
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBE8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (approved)。来源: https://www.proteinatlas.org/ENSG00000213160-KLHL23/subcellular

![](https://images.proteinatlas.org/47593/699_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/47593/699_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/47593/716_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/47593/716_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/47593/719_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/47593/719_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NBE8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NBE8 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 36..104; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037"; DOMAIN 139..240; /note="BACK" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR030566;IPR015915;IPR006652;IPR047068;IPR011333; |
| Pfam | PF07707;PF00651;PF01344;PF24681; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213160-KLHL23/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AMDHD1 | Intact, Bioplex | false |
| CUL3 | Biogrid | false |
| NUDCD3 | Intact | false |
| ZFP36L1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
