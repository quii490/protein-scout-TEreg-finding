---
type: protein-evaluation
gene: "PLPP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLPP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLPP4 / DPPL2, PPAPDC1, PPAPDC1A |
| 蛋白名称 | Phospholipid phosphatase 4 |
| 蛋白大小 | 271 aa / 30.4 kDa |
| UniProt ID | Q5VZY2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 271 aa / 30.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPPL2, PPAPDC1, PPAPDC1A |

**关键文献**:
1. Lipid metabolism associated PLPP4 gene drives oncogenic and adipogenic potential in breast cancer cells.. *Biochimica et biophysica acta. Molecular and cell biology of lipids*. PMID: 40187483
2. Gene Expression Network Analysis of Precursor Lesions in Familial Pancreatic Cancer.. *Journal of pancreatic cancer*. PMID: 32783019
3. A genome-wide association study of social trust in 33,882 Danish blood donors.. *Scientific reports*. PMID: 38228779
4. CAPRIN1 Transcriptionally Activated PLPP4 to Inhibit DOX Sensitivity and Promote Breast Cancer Progression.. *Cell biochemistry and biophysics*. PMID: 39556159
5. Integrating metabolomics and transcriptomics to analyze the differences of breast muscle quality and flavor formation between Daweishan mini chicken and broiler.. *Poultry science*. PMID: 38909504

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.1 |
| 高置信度残基 (pLDDT>90) 占比 | 84.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 89.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.1，有序区 89.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DGAT1 | 0.956 | 0.067 | — |
| DGAT2 | 0.951 | 0.000 | — |
| LPIN1 | 0.947 | 0.091 | — |
| PLPP2 | 0.943 | 0.000 | — |
| AGPAT2 | 0.942 | 0.047 | — |
| PNPLA2 | 0.940 | 0.000 | — |
| PNPLA3 | 0.938 | 0.000 | — |
| MOGAT1 | 0.932 | 0.000 | — |
| AGPAT1 | 0.932 | 0.047 | — |
| PLD1 | 0.926 | 0.075 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000381302.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SAR1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BCL2L13 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GJB5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SYT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC35A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CREB3L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SSMEM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MGST3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BMP10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.1 + PDB: 无 | pLDDT=91.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli, Nucleoli rim; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLPP4 — Phospholipid phosphatase 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小271 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VZY2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203805-PLPP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLPP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VZY2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000203805-PLPP4/subcellular

![](https://images.proteinatlas.org/45188/562_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45188/562_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45188/568_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45188/568_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45188/575_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45188/575_E6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VZY2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VZY2 |
| SMART | SM00014; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043216;IPR000326;IPR036938; |
| Pfam | PF01569; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203805-PLPP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARL13B | Intact | false |
| BCL2L13 | Intact | false |
| BIK | Intact | false |
| BMP10 | Intact | false |
| CISD2 | Intact | false |
| CPLX4 | Intact | false |
| CREB3L1 | Intact | false |
| CYB5B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
