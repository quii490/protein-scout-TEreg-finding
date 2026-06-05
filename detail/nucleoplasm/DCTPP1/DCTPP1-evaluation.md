---
type: protein-evaluation
gene: "DCTPP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCTPP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTPP1 / XTP3TPA |
| 蛋白名称 | dCTP pyrophosphatase 1 |
| 蛋白大小 | 170 aa / 18.7 kDa |
| UniProt ID | Q9H773 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Mitochondrion; Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 8/10 | ×1 | 8 | 170 aa / 18.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.6; PDB: 7MU5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052555, IPR025984; Pfam: PF12643 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Mitochondrion; Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XTP3TPA |

**关键文献**:
1. Identification of Novel Target DCTPP1 for Colorectal Cancer Therapy with the Natural Small-Molecule Inhibitors Regulating Metabolic Reprogramming.. *Angewandte Chemie (International ed. in English)*. PMID: 39143504
2. DCTPP1: A promising target in cancer therapy and prognosis through nucleotide metabolism.. *Drug discovery today*. PMID: 40180312
3. Chemical Genetics Reveals a Role of dCTP Pyrophosphatase 1 in Wnt Signaling.. *Angewandte Chemie (International ed. in English)*. PMID: 31173446
4. Comparative proteomics analysis of gastric cancer stem cells.. *PloS one*. PMID: 25379943
5. Combined protein and transcriptomics identifies DCTPP1 as a putative biomarkers for predicting immunotherapy responsiveness in gastric cancer patients.. *Anti-cancer drugs*. PMID: 39908235

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 16.5% |
| 有序区域 (pLDDT>70) 占比 | 73.6% |
| 可用 PDB 条目 | 7MU5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.6，有序区 73.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052555, IPR025984; Pfam: PF12643 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCTD | 0.959 | 0.000 | — |
| DCK | 0.934 | 0.000 | — |
| NME1 | 0.930 | 0.095 | — |
| AK9 | 0.929 | 0.099 | — |
| NT5C | 0.925 | 0.000 | — |
| RRM2 | 0.922 | 0.047 | — |
| NT5M | 0.922 | 0.000 | — |
| RRM1 | 0.917 | 0.045 | — |
| RRM2B | 0.916 | 0.047 | — |
| NME2 | 0.914 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000322524.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NTAQ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NOA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 7MU5 | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus; Cytoplasm, cytosol / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCTPP1 — dCTP pyrophosphatase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小170 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H773
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179958-DCTPP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTPP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H773
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000179958-DCTPP1/subcellular

![](https://images.proteinatlas.org/2832/2104_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/2832/2104_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/2832/36_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/2832/36_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/2832/37_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/2832/37_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H773-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
