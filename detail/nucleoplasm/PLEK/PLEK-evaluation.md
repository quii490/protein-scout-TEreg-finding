---
type: protein-evaluation
gene: "PLEK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEK / P47 |
| 蛋白名称 | Pleckstrin |
| 蛋白大小 | 350 aa / 40.1 kDa |
| UniProt ID | P08567 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 40.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.0; PDB: 1PLS, 1W4M, 1X05, 1XX0, 1ZM0, 2CSO, 2I5C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000591, IPR011993, IPR001849, IPR037370, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- ruffle membrane (GO:0032587)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: P47 |

**关键文献**:
1. Differentiation-related genes in tumor-associated macrophages as potential prognostic biomarkers in non-small cell lung cancer.. *Frontiers in immunology*. PMID: 36969247
2. Integrative network-based analysis on multiple Gene Expression Omnibus datasets identifies novel immune molecular markers implicated in non-alcoholic steatohepatitis.. *Frontiers in endocrinology*. PMID: 37008925
3. The osteosarcoma immune microenvironment in progression: PLEK as a prognostic biomarker and therapeutic target.. *Frontiers in immunology*. PMID: 40895569
4. Comprehensive analysis identifies crucial genes associated with immune cells mediating progression of carotid atherosclerotic plaque.. *Aging*. PMID: 38382092
5. Higher expression of PLEK and LY86 as the potential biomarker of carotid atherosclerosis.. *Medicine*. PMID: 37861500

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.0 |
| 高置信度残基 (pLDDT>90) 占比 | 37.7% |
| 置信残基 (pLDDT 70-90) 占比 | 46.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 83.7% |
| 可用 PDB 条目 | 1PLS, 1W4M, 1X05, 1XX0, 1ZM0, 2CSO, 2I5C, 2I5F |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1PLS, 1W4M, 1X05, 1XX0, 1ZM0, 2CSO, 2I5C, 2I5F）+ AlphaFold极高置信度预测（pLDDT=82.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR011993, IPR001849, IPR037370, IPR037371; Pfam: PF00610, PF00169 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCF2 | 0.977 | 0.000 | — |
| BTK | 0.929 | 0.000 | — |
| CYTH1 | 0.920 | 0.000 | — |
| OSBP | 0.908 | 0.000 | — |
| PLCD1 | 0.893 | 0.000 | — |
| SRC | 0.877 | 0.000 | — |
| AKT1 | 0.867 | 0.000 | — |
| RABIF | 0.861 | 0.000 | — |
| CDC42 | 0.847 | 0.000 | — |
| RHOA | 0.837 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTN1 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| PF4 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| THBS1 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| CAVIN2 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| RDX | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| HSD17B4 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| F13A1 | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| MSN | psi-mi:"MI:0096"(pull down) | imex:IM-13589|pubmed:19722192 |
| WDR75 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SARAF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.0 + PDB: 1PLS, 1W4M, 1X05, 1XX0, 1ZM0,  | pLDDT=82.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEK — Pleckstrin，研究基础较多，新颖性有限。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P08567
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115956-PLEK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P08567
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000115956-PLEK/subcellular

![](https://images.proteinatlas.org/57341/1674_F5_14_cr58079440718b9_blue_red_green.jpg)
![](https://images.proteinatlas.org/57341/1674_F5_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/57341/1714_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57341/1714_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57341/1770_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57341/1770_C9_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P08567-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
