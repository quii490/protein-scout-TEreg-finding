---
type: protein-evaluation
gene: "TTC27"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC27 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC27 |
| 蛋白名称 | Tetratricopeptide repeat protein 27 |
| 蛋白大小 | 843 aa / 96.6 kDa |
| UniProt ID | Q6P3X3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 843 aa / 96.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011990, IPR019734, IPR044244; Pfam: PF13432 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gene expression in mouse brain following chronic hypoxia: role of sarcospan in glial cell death.. *Physiological genomics*. PMID: 18056785
2. Emw1/TTC27 is a chaperone required for folding of the eukaryotic elongation factor 2.. *Cellular and molecular life sciences : CMLS*. PMID: 41806041
3. A comparative transcriptomic analysis reveals conserved features of stem cell pluripotency in planarians and mammals.. *Stem cells (Dayton, Ohio)*. PMID: 22696458
4. The C. elegans TPR Containing Protein, TRD-1, Regulates Cell Fate Choice in the Developing Germ Line and Epidermis.. *PloS one*. PMID: 25493563
5. Multiple loci influencing hippocampal degeneration identified by genome scan.. *Annals of neurology*. PMID: 22745009

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 66.8% |
| 置信残基 (pLDDT 70-90) 占比 | 30.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.5，有序区 97.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734, IPR044244; Pfam: PF13432 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR3 | 0.888 | 0.000 | — |
| TBL3 | 0.863 | 0.000 | — |
| WDR36 | 0.860 | 0.000 | — |
| NAT10 | 0.851 | 0.000 | — |
| PWP2 | 0.830 | 0.000 | — |
| LOC102724159 | 0.820 | 0.000 | — |
| EFTUD2 | 0.778 | 0.674 | — |
| HEATR1 | 0.774 | 0.000 | — |
| POLR1B | 0.770 | 0.000 | — |
| AAR2 | 0.768 | 0.678 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| Prpf8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 无 | pLDDT=90.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TTC27 — Tetratricopeptide repeat protein 27，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小843 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P3X3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000018699-TTC27/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC27
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P3X3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000018699-TTC27/subcellular

![](https://images.proteinatlas.org/31246/330_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31246/330_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31246/331_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31246/331_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31246/333_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31246/333_D3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P3X3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P3X3 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011990;IPR019734;IPR044244; |
| Pfam | PF13432; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000018699-TTC27/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AAR2 | Biogrid, Bioplex | true |
| EFTUD2 | Biogrid, Opencell, Bioplex | true |
| DHFR2 | Bioplex | false |
| EAPP | Bioplex | false |
| ECD | Biogrid | false |
| GPR182 | Bioplex | false |
| GZMH | Bioplex | false |
| KLK15 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
