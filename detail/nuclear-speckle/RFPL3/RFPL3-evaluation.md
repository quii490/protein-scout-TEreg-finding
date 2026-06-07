---
type: protein-evaluation
gene: "RFPL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RFPL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RFPL3 |
| 蛋白名称 | Ret finger protein-like 3 |
| 蛋白大小 | 317 aa / 35.4 kDa |
| UniProt ID | O75679 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Plasma membrane; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 317 aa / 35.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RFPL3 and CBP synergistically upregulate hTERT activity and promote lung cancer growth.. *Oncotarget*. PMID: 26318425
2. Importin 13 promotes NSCLC progression by mediating RFPL3 nuclear translocation and hTERT expression upregulation.. *Cell death & disease*. PMID: 33082305
3. EGF upregulates RFPL3 and hTERT via the MEK signaling pathway in non‑small cell lung cancer cells.. *Oncology reports*. PMID: 29749533
4. Genome-wide Association Study of Dimensional Psychopathology Using Electronic Health Records.. *Biological psychiatry*. PMID: 29496196
5. Identification of RFPL3 protein as a novel E3 ubiquitin ligase modulating the integration activity of human immunodeficiency virus, type 1 preintegration complex using a microtiter plate-based assay.. *The Journal of biological chemistry*. PMID: 25107902

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.1，有序区 84.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF11002, PF00622 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFPL2 | 0.742 | 0.465 | — |
| PAX6 | 0.669 | 0.045 | — |
| RFPL1 | 0.623 | 0.604 | — |
| ASNSD1 | 0.597 | 0.597 | — |
| PRAMEF11 | 0.594 | 0.105 | — |
| PRAMEF13 | 0.584 | 0.105 | — |
| OR1N2 | 0.505 | 0.000 | — |
| PRAMEF12 | 0.498 | 0.105 | — |
| HSPB2 | 0.487 | 0.488 | — |
| DAB2IP | 0.478 | 0.478 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLAIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RGP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C3orf62 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EIF1AX | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RFPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RFPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DAB2IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.1 + PDB: 无 | pLDDT=85.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Plasma membrane | 一致 |
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
1. RFPL3 — Ret finger protein-like 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小317 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75679
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128276-RFPL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RFPL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75679
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000128276-RFPL3/subcellular

![](https://images.proteinatlas.org/48320/1711_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/48320/1711_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/48320/1712_B12_14_cr5804a7b6268fd_red_green.jpg)
![](https://images.proteinatlas.org/48320/1712_B12_24_cr5804a7c7dcdc9_red_green.jpg)
![](https://images.proteinatlas.org/48320/1737_C3_13_cr58063ebd153c9_red_green.jpg)
![](https://images.proteinatlas.org/48320/1737_C3_2_cr58063eb3ccd17_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75679-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75679 |
| SMART | SM00589;SM00449; |
| UniProt Domain [FT] | DOMAIN 107..301; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR006574;IPR022723;IPR037960;IPR003877;IPR050143;IPR001841;IPR013083; |
| Pfam | PF13765;PF11002;PF00622;PF15227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128276-RFPL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C3orf62 | Intact | false |
| DDIT4L | Intact | false |
| EIF1AX | Intact | false |
| HSPB2 | Intact | false |
| LNX1 | Intact | false |
| PFDN4 | Intact | false |
| RGP1 | Intact | false |
| SLAIN1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
