---
type: protein-evaluation
gene: "GGT7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GGT7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GGT7 / GGTL3, GGTL5 |
| 蛋白名称 | Glutathione hydrolase 7 |
| 蛋白大小 | 662 aa / 70.5 kDa |
| UniProt ID | Q9UJ14 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 662 aa / 70.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043138, IPR000101, IPR043137, IPR029055; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GGTL3, GGTL5 |

**关键文献**:
1. Systematic interrogation of functional genes underlying cholesterol and lipid homeostasis.. *Genome biology*. PMID: 40098013
2. The human gamma-glutamyltransferase gene family.. *Human genetics*. PMID: 18357469
3. TXNDC12 inhibits pancreatic tumor cells ferroptosis by regulating GSH/GGT7 and promotes its growth and metastasis.. *Journal of Cancer*. PMID: 38911386
4. Expression Status and Prognostic Significance of Gamma-Glutamyl Transpeptidase Family Genes in Hepatocellular Carcinoma.. *Frontiers in oncology*. PMID: 34513707
5. [The role of polymorphic variants rs11546155 and rs6119534 of the GGT7 gene and risk factors in the development of acute pancreatitis].. *Voprosy pitaniia*. PMID: 35596634

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 82.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.1，有序区 82.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043138, IPR000101, IPR043137, IPR029055; Pfam: PF01019 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSS | 0.959 | 0.000 | — |
| ANPEP | 0.949 | 0.000 | — |
| GGT6 | 0.946 | 0.000 | — |
| GGT5 | 0.940 | 0.000 | — |
| GGCT | 0.939 | 0.000 | — |
| OPLAH | 0.935 | 0.000 | — |
| LAP3 | 0.930 | 0.000 | — |
| GGT1 | 0.930 | 0.000 | — |
| TLCD3A | 0.927 | 0.000 | — |
| GCLC | 0.925 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAX | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| LHFPL5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CLDN19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNPEP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| M2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| CMTM7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.1 + PDB: 无 | pLDDT=85.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Vesicles; 额外: Nucleoplasm | 一致 |
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
1. GGT7 — Glutathione hydrolase 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小662 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJ14
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131067-GGT7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GGT7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJ14
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000131067-GGT7/subcellular

![](https://images.proteinatlas.org/13339/1585_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/13339/1585_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/13339/1595_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/13339/1595_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/13339/1616_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/13339/1616_G4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJ14-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UJ14 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043138;IPR000101;IPR043137;IPR029055; |
| Pfam | PF01019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131067-GGT7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LHFPL5 | Intact, Biogrid | true |
| ADIPOR2 | Biogrid | false |
| CMTM7 | Intact | false |
| CYB561 | Intact | false |
| DCP2 | Biogrid | false |
| GPR25 | Intact | false |
| LRRC59 | Biogrid | false |
| MALL | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
