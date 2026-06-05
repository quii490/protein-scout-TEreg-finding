---
type: protein-evaluation
gene: "FAH"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAH — REJECTED (研究热度过高 (PubMed strict=464，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAH |
| 蛋白名称 | Fumarylacetoacetase |
| 蛋白大小 | 419 aa / 46.4 kDa |
| UniProt ID | P16930 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 46.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=464 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005959, IPR011234, IPR036663, IPR015377, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **62.0/180** | |
| **归一化总分** | | | **34.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 464 |
| PubMed broad count | 2796 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Oxidative stress gene expression, DNA methylation, and gut microbiota interaction trigger Crohn's disease: a multi-omics Mendelian randomization study.. *BMC medicine*. PMID: 37170220
2. Bioprinting functional hepatocyte organoids derived from human chemically induced pluripotent stem cells to treat liver failure.. *Gut*. PMID: 40032498
3. In vitro expansion of single Lgr5+ liver stem cells induced by Wnt-driven regeneration.. *Nature*. PMID: 23354049
4. Tyrosine catabolism enhances genotoxic chemotherapy by suppressing translesion DNA synthesis in epithelial ovarian cancer.. *Cell metabolism*. PMID: 37890478
5. Efficient expansion and CRISPR-Cas9-mediated gene correction of patient-derived hepatocytes for treatment of inherited liver diseases.. *Cell stem cell*. PMID: 38772378

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005959, IPR011234, IPR036663, IPR015377, IPR036462; Pfam: PF01557, PF09298 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSTZ1 | 0.997 | 0.000 | — |
| HPD | 0.993 | 0.000 | — |
| FAHD1 | 0.974 | 0.000 | — |
| HGD | 0.945 | 0.000 | — |
| TAT | 0.935 | 0.000 | — |
| FH | 0.871 | 0.000 | — |
| SDHA | 0.854 | 0.000 | — |
| SDHB | 0.830 | 0.000 | — |
| SDHC | 0.823 | 0.000 | — |
| SDHD | 0.805 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| KRTAP13-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLEKHF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CHRDL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| KRTAP5-9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| KRTAP10-8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| SERTAD1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| ADAMTSL4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FAH — Fumarylacetoacetase，研究基础较多，新颖性有限。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 464 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 464 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16930
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103876-FAH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16930
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000103876-FAH/subcellular

![](https://images.proteinatlas.org/44093/1925_F11_16_cr5cd55732c1b67_red_green.jpg)
![](https://images.proteinatlas.org/44093/1925_F11_3_cr5cd55732c12fc_red_green.jpg)
![](https://images.proteinatlas.org/44093/1956_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/44093/1956_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/44093/698_F7_5_red_green.jpg)
![](https://images.proteinatlas.org/44093/698_F7_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16930-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
