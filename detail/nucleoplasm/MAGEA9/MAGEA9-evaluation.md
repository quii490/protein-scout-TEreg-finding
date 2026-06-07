---
type: protein-evaluation
gene: "MAGEA9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEA9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEA9 / MAGE9, MAGEA9A |
| 蛋白名称 | Melanoma-associated antigen 9 |
| 蛋白大小 | 315 aa / 35.1 kDa |
| UniProt ID | P43362 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 35.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAGE9, MAGEA9A |

**关键文献**:
1. Long Non-Coding RNA (lncRNA) Metastasis-Associated Lung Adenocarcinoma Transcript 1 (MALAT1) Promotes Cell Proliferation and Migration by Regulating miR-143-3p and MAGE Family Member A9 (MAGEA9) in Oral Squamous Cell Carcinoma.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 32879299
2. Recurrent X chromosome-linked deletions: discovery of new genetic factors in male infertility.. *Journal of medical genetics*. PMID: 24421283
3. Evidence for the involvement of the proximal copy of the MAGEA9 gene in Xq28-linked CNV67 specific to spermatogenic failure.. *Biology of reproduction*. PMID: 28339631
4. Global expression analysis of cancer/testis genes in uterine cancers reveals a high incidence of BORIS expression.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 17363524
5. High expression of MAGE-A9 in tumor and stromal cells of non-small cell lung cancer was correlated with patient poor survival.. *International journal of clinical and experimental pathology*. PMID: 25755744

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 48.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 24.1% |
| 有序区域 (pLDDT>70) 占比 | 67.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 67.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002190; Pfam: PF01454, PF12440 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAGEA4 | 0.651 | 0.626 | — |
| MAGEA10 | 0.647 | 0.617 | — |
| CTAG2 | 0.594 | 0.000 | — |
| APPL1 | 0.585 | 0.585 | — |
| CTAG1B | 0.541 | 0.000 | — |
| MAGEC1 | 0.447 | 0.000 | — |
| HSFX4 | 0.446 | 0.000 | — |
| TMEM86A | 0.432 | 0.000 | — |
| CTAG1A | 0.418 | 0.000 | — |
| GET3 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MAGEA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APPL1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SAP30BP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 7
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 10 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAGEA9 — Melanoma-associated antigen 9，非常新颖，仅有少数基础研究。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43362
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123584-MAGEA9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEA9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43362
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123584-MAGEA9/subcellular

![](https://images.proteinatlas.org/45401/1558_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45401/1558_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51687/1541_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51687/1541_B4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51687/1542_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51687/1542_B4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P43362-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P43362 |
| SMART | SM01373;SM01392; |
| UniProt Domain [FT] | DOMAIN 108..307; /note="MAGE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00127" |
| InterPro | IPR037445;IPR021072;IPR041898;IPR041899;IPR002190; |
| Pfam | PF01454;PF12440; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123584-MAGEA9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPL1 | Intact, Biogrid | true |
| COMMD10 | Bioplex | false |
| CRH | Bioplex | false |
| MAGEA1 | Bioplex | false |
| MAGEA4 | Bioplex | false |
| TRIM28 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
