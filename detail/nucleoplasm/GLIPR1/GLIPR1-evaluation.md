---
type: protein-evaluation
gene: "GLIPR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLIPR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLIPR1 / GLIPR, RTVP1 |
| 蛋白名称 | Glioma pathogenesis-related protein 1 |
| 蛋白大小 | 266 aa / 30.4 kDa |
| UniProt ID | P48060 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 266 aa / 30.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.1; PDB: 3Q2R, 3Q2U |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018244, IPR014044, IPR035940, IPR001283, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- azurophil granule membrane (GO:0035577)
- extracellular space (GO:0005615)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 96 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLIPR, RTVP1 |

**关键文献**:
1. Shared diagnostic genes and potential mechanism between PCOS and recurrent implantation failure revealed by integrated transcriptomic analysis and machine learning.. *Frontiers in immunology*. PMID: 37261354
2. Glioma pathogenesis-related protein 1 performs dual functions in tumor cells.. *Cancer gene therapy*. PMID: 33742130
3. GLI pathogenesis-related 1 functions as a tumor-suppressor in lung cancer.. *Molecular cancer*. PMID: 26988096
4. GLIPR1 promotes proliferation, metastasis and 5-fluorouracil resistance in hepatocellular carcinoma by activating the PI3K/PDK1/ROCK1 pathway.. *Cancer gene therapy*. PMID: 35760898
5. Tumor growth and metastasis suppression by Glipr1 gene-modified macrophages in a metastatic prostate cancer model.. *Gene therapy*. PMID: 21512508

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 70.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 8.6% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 3Q2R, 3Q2U |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3Q2R, 3Q2U）+ AlphaFold高质量预测（pLDDT=87.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018244, IPR014044, IPR035940, IPR001283, IPR034121; Pfam: PF00188 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GART | 0.831 | 0.000 | — |
| GLIPR2 | 0.762 | 0.000 | — |
| LAPTM5 | 0.635 | 0.000 | — |
| TP53 | 0.573 | 0.000 | — |
| PPARA | 0.538 | 0.045 | — |
| SRGN | 0.517 | 0.000 | — |
| ARHGDIB | 0.507 | 0.000 | — |
| FABP1 | 0.505 | 0.000 | — |
| HELZ2 | 0.484 | 0.067 | — |
| IQGAP1 | 0.475 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| queE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ALOXE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CMTM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CKLF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LCOR | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 3Q2R, 3Q2U | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLIPR1 — Glioma pathogenesis-related protein 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小266 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48060
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139278-GLIPR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLIPR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48060
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GLIPR1/IF_images/BJ-Human-fibroblast_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GLIPR1/IF_images/U-251MG_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000139278-GLIPR1/subcellular

![](https://images.proteinatlas.org/11084/2095_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11084/2095_E2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/11084/2100_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11084/2100_A5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/11084/2173_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11084/2173_G1_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48060-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P48060 |
| SMART | SM00198; |
| UniProt Domain [FT] | DOMAIN 38..175; /note="SCP" |
| InterPro | IPR018244;IPR014044;IPR035940;IPR001283;IPR034121;IPR002413; |
| Pfam | PF00188; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139278-GLIPR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOXE3 | Intact | false |
| CMTM6 | Bioplex | false |
| HBB | Bioplex | false |
| HNRNPK | Biogrid | false |
| HSPA8 | Biogrid | false |
| HTT | Intact | false |
| WAS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
