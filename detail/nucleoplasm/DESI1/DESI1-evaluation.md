---
type: protein-evaluation
gene: "DESI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DESI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DESI1 / FAM152B, PPPDE2 |
| 蛋白名称 | Desumoylating isopeptidase 1 |
| 蛋白大小 | 168 aa / 18.3 kDa |
| UniProt ID | Q6ICB0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Cytokinetic bridge; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 168 aa / 18.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.5; PDB: 3EBQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008580, IPR042266; Pfam: PF05903 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **152.0/180** | |
| **归一化总分** | | | **84.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Cytokinetic bridge | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM152B, PPPDE2 |

**关键文献**:
1. Downregulation of hsa-miR-135b-5p Inhibits Cell Proliferation, Migration, and Invasion in Colon Adenocarcinoma.. *Genetics research*. PMID: 36407085
2. Modelling reoxygenation effects in non-small cell lung cancer cell lines and showing epithelial-mesenchymal transition.. *Journal of cancer research and clinical oncology*. PMID: 35932303
3. DeSUMOylating isopeptidase: a second class of SUMO protease.. *EMBO reports*. PMID: 22370726
4. Chemical composition of kabuli and desi chickpea (Cicer arietinum L.) cultivars grown in Xinjiang, China.. *Food science & nutrition*. PMID: 36655092
5. Non-TZF Protein AtC3H59/ZFWD3 Is Involved in Seed Germination, Seedling Development, and Seed Development, Interacting with PPPDE Family Protein Desi1 in Arabidopsis.. *International journal of molecular sciences*. PMID: 33947021

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 92.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 94.7% |
| 可用 PDB 条目 | 3EBQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.5，有序区 94.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008580, IPR042266; Pfam: PF05903 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBQLN4 | 0.997 | 0.994 | — |
| UBQLN1 | 0.995 | 0.994 | — |
| PSMD11 | 0.994 | 0.994 | — |
| PSMC5 | 0.994 | 0.994 | — |
| PSMC4 | 0.994 | 0.994 | — |
| PSMC3 | 0.994 | 0.994 | — |
| PSMA2 | 0.994 | 0.994 | — |
| TMBIM6 | 0.994 | 0.994 | — |
| PSMA7 | 0.994 | 0.994 | — |
| PSMC2 | 0.994 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FGF7 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| cydC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000263256.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A384LGH0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| bcr | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBQLNL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTAG2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DAZAP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UHRF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 3EBQ | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Cytokinetic bridge | 一致 |
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
1. DESI1 — Desumoylating isopeptidase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小168 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ICB0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100418-DESI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DESI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ICB0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000100418-DESI1/subcellular

![](https://images.proteinatlas.org/53415/831_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53415/831_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53415/868_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53415/868_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53415/882_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53415/882_C4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ICB0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ICB0 |
| SMART | SM01179; |
| UniProt Domain [FT] | DOMAIN 7..149; /note="PPPDE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01205" |
| InterPro | IPR008580;IPR042266; |
| Pfam | PF05903; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100418-DESI1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBC | Intact, Biogrid | true |
| UBQLN1 | Intact, Biogrid | true |
| UBQLN2 | Intact, Biogrid | true |
| ABI3 | Intact | false |
| AGR3 | Intact | false |
| CDIP1 | Intact | false |
| CTAG1A | Intact | false |
| CTAG1B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
