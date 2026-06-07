---
type: protein-evaluation
gene: "DCLRE1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCLRE1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCLRE1A / KIAA0086, SNM1, SNM1A |
| 蛋白名称 | DNA cross-link repair 1A protein |
| 蛋白大小 | 1040 aa / 116.4 kDa |
| UniProt ID | Q6PJP8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1040 aa / 116.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.9; PDB: 4B87, 5AHR, 5NZW, 5NZX, 5NZY, 5Q1J, 5Q1K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011084, IPR006642, IPR036866; Pfam: PF07522 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0086, SNM1, SNM1A |

**关键文献**:
1. DCLRE1A Contributes to DNA Damage Repair and Apoptosis in Age-Related Cataracts by Regulating the lncRNA/miRNA/mRNA Axis.. *Current eye research*. PMID: 37503815
2. Gene expression profiles in human lymphocytes irradiated in vitro with low doses of gamma rays.. *Radiation research*. PMID: 18088177
3. The role of double-strand break repair, translesion synthesis, and interstrand crosslinks in colorectal cancer progression-clinicopathological data and survival.. *Journal of surgical oncology*. PMID: 31650563
4. A network-pathway based module identification for predicting the prognosis of ovarian cancer patients.. *Journal of ovarian research*. PMID: 27806724
5. Identification of candidate cancer predisposing variants by performing whole-exome sequencing on index patients from BRCA1 and BRCA2-negative breast cancer families.. *BMC cancer*. PMID: 30947698

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.9 |
| 高置信度残基 (pLDDT>90) 占比 | 33.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 60.1% |
| 有序区域 (pLDDT>70) 占比 | 38.5% |
| 可用 PDB 条目 | 4B87, 5AHR, 5NZW, 5NZX, 5NZY, 5Q1J, 5Q1K, 5Q1L, 5Q1M, 5Q1N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.9），有序残基占 38.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011084, IPR006642, IPR036866; Pfam: PF07522 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPSF3 | 0.941 | 0.000 | — |
| CPSF2 | 0.902 | 0.000 | — |
| FANCD2 | 0.860 | 0.088 | — |
| FANCM | 0.852 | 0.100 | — |
| MUS81 | 0.851 | 0.000 | — |
| FANCI | 0.848 | 0.000 | — |
| SLX4 | 0.846 | 0.000 | — |
| SLX1A | 0.835 | 0.000 | — |
| FAN1 | 0.830 | 0.115 | — |
| ELAC2 | 0.824 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KTN1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| U2SURP | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KPNA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000361384 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.9 + PDB: 4B87, 5AHR, 5NZW, 5NZX, 5NZY,  | pLDDT=57.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCLRE1A — DNA cross-link repair 1A protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1040 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PJP8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198924-DCLRE1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCLRE1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PJP8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198924-DCLRE1A/subcellular

![](https://images.proteinatlas.org/36907/403_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/36907/403_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/36907/406_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/36907/406_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/36907/408_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/36907/408_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PJP8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PJP8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011084;IPR006642;IPR036866; |
| Pfam | PF07522; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198924-DCLRE1A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PCNA | Biogrid, Opencell | true |
| ERCC6 | Biogrid | false |
| PIAS1 | Biogrid | false |
| SLX4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
