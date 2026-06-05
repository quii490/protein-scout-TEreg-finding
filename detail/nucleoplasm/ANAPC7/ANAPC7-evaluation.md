---
type: protein-evaluation
gene: "ANAPC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANAPC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC7 / APC7 |
| 蛋白名称 | Anaphase-promoting complex subunit 7 |
| 蛋白大小 | 565 aa / 63.1 kDa |
| UniProt ID | Q9UJX3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules, Cytokinetic bridge, Mitotic spindle; 额外: Nucle; UniProt: Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytoskeleton, s |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 565 aa / 63.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.0; PDB: 3FFL, 4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011990, IPR019734; Pfam: PF13432, PF13181 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分 (÷1.83)** | | | **78.1/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Cytokinetic bridge, Mitotic spindle; 额外: Nucleoplasm, Vesicles | Supported |
| UniProt | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- anaphase-promoting complex (GO:0005680)
- cytosol (GO:0005829)
- heterochromatin (GO:0000792)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- mitotic spindle (GO:0072686)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APC7 |

**关键文献**:
1. Identification and validation of a PD-L1-related signature from mass spectrometry in gastric cancer.. *Journal of cancer research and clinical oncology*. PMID: 36592213
2. Quantitative Proteomic Analysis of Porcine Intestinal Epithelial Cells Infected with Porcine Deltacoronavirus Using iTRAQ-Coupled LC-MS/MS.. *Journal of proteome research*. PMID: 33045833
3. Using Circ-ANAPC7 as a Novel Type of Biomarker in the Monitoring of Acute Myeloid Leukemia.. *Acta haematologica*. PMID: 34879367
4. Identification of BRIP1, NSMCE2, ANAPC7, RAD18 and TTL from chromosome segregation gene set associated with hepatocellular carcinoma.. *Cancer genetics*. PMID: 36126360
5. miRNA-mRNA analysis of sheep adrenal glands reveals the network regulating reproduction.. *BMC genomic data*. PMID: 35710353

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.0% |
| 置信残基 (pLDDT 70-90) 占比 | 42.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 87.7% |
| 可用 PDB 条目 | 3FFL, 4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3FFL, 4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW）+ AlphaFold预测（pLDDT=83.0），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734; Pfam: PF13432, PF13181 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FZR1 | 0.999 | 0.998 | — |
| ANAPC10 | 0.999 | 0.999 | — |
| ANAPC1 | 0.999 | 0.981 | — |
| CDC27 | 0.999 | 0.999 | — |
| BUB1B | 0.999 | 0.998 | — |
| ANAPC16 | 0.999 | 0.987 | — |
| ANAPC2 | 0.999 | 0.998 | — |
| CDC23 | 0.999 | 0.984 | — |
| ANAPC4 | 0.999 | 0.998 | — |
| CDC20 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pik3ca | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| BAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| anapc7.L | psi-mi:"MI:0030"(cross-linking study) | pubmed:20951947|imex:IM-15161 |
| MGC80529 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20951947|imex:IM-15161 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| PTEN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| CDC27 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.0 + PDB: 3FFL, 4UI9, 5A31, 5G04, 5G05,  | pLDDT=83.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytos / Microtubules, Cytokinetic bridge, Mitotic spindle; | 一致 |
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
1. ANAPC7 — Anaphase-promoting complex subunit 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小565 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJX3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196510-ANAPC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJX3
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:50:47

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (supported)。来源: https://www.proteinatlas.org/ENSG00000196510-ANAPC7/subcellular

![](https://images.proteinatlas.org/70008/1891_A13_27_cr5bbde2d7cb3ae_red_green.jpg)
![](https://images.proteinatlas.org/70008/1891_A13_2_cr5bbde2d7cae22_red_green.jpg)
![](https://images.proteinatlas.org/70008/2108_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/70008/2108_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/70008/2197_D11_5_red_green.jpg)
![](https://images.proteinatlas.org/70008/2197_D11_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJX3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
