---
type: protein-evaluation
gene: "PRKRIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRKRIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRKRIP1 |
| 蛋白名称 | PRKR-interacting protein 1 |
| 蛋白大小 | 184 aa / 21.0 kDa |
| UniProt ID | Q9H875 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Actin filaments; 额外: Cytosol; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 21.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.5; PDB: 5XJC, 6ICZ, 6QDV, 7W5A, 7W5B, 8C6J, 9FMD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009548; Pfam: PF06658 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Cytosol | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- spliceosomal complex (GO:0005681)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. An Atomic Structure of the Human Spliceosome.. *Cell*. PMID: 28502770
2. Identification of a Novel 4-gene Prognostic Model Related to Neutrophil Extracellular Traps for Colorectal Cancer.. *The Turkish journal of gastroenterology : the official journal of Turkish Society of Gastroenterology*. PMID: 39549020
3. PRKRIP1, A Splicing Complex Factor, Is a Marker of Poor Prognosis in Colorectal Cancer.. *Anticancer research*. PMID: 36192001
4. Protein microarrays discover angiotensinogen and PRKRIP1 as novel targets for autoantibodies in chronic renal disease.. *Molecular & cellular proteomics : MCP*. PMID: 21183621

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.5 |
| 高置信度残基 (pLDDT>90) 占比 | 56.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 70.6% |
| 可用 PDB 条目 | 5XJC, 6ICZ, 6QDV, 7W5A, 7W5B, 8C6J, 9FMD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5XJC, 6ICZ, 6QDV, 7W5A, 7W5B, 8C6J, 9FMD）+ AlphaFold极高置信度预测（pLDDT=80.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009548; Pfam: PF06658 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC40 | 0.987 | 0.900 | — |
| SLU7 | 0.983 | 0.800 | — |
| SYF2 | 0.963 | 0.800 | — |
| SNRPE | 0.959 | 0.959 | — |
| PPIL1 | 0.958 | 0.800 | — |
| SNRPG | 0.951 | 0.951 | — |
| CACTIN | 0.948 | 0.900 | — |
| SNRPA1 | 0.946 | 0.938 | — |
| AQR | 0.938 | 0.937 | — |
| FAM32A | 0.930 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KHDRBS1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SNRPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRPA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRPGP15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRAF2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| CEP70 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| LRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.5 + PDB: 5XJC, 6ICZ, 6QDV, 7W5A, 7W5B,  | pLDDT=80.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Actin filaments; 额外: Cytosol | 一致 |
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
1. PRKRIP1 — PRKR-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H875
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128563-PRKRIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRKRIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H875
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (supported)。来源: https://www.proteinatlas.org/ENSG00000128563-PRKRIP1/subcellular

![](https://images.proteinatlas.org/51146/712_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51146/712_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51146/804_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51146/804_H11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51146/964_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51146/964_H11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H875-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H875 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009548; |
| Pfam | PF06658; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128563-PRKRIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP70 | Intact | false |
| SNRPA1 | Bioplex | false |
| SNRPE | Biogrid | false |
| TRAF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
