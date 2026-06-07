---
type: protein-evaluation
gene: "TRIM11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM11 / RNF92 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM11 |
| 蛋白大小 | 468 aa / 52.8 kDa |
| UniProt ID | Q96F44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 468 aa / 52.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=94 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.6; PDB: 7QS1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 94 |
| PubMed broad count | 145 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF92 |

**关键文献**:
1. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
2. Nucleosome assembly protein-like 1 degradation-dependent novel cardioprotection mechanism of Wnt2 against ischemia‒reperfusion injury.. *Signal transduction and targeted therapy*. PMID: 41397965
3. MITF Pathway-Activated Cutaneous Neoplasms.. *Advances in anatomic pathology*. PMID: 40387110
4. TRIM11 Prevents Ferroptosis in model of asthma by UBE2N-TAX1BP1 signaling.. *BMC pulmonary medicine*. PMID: 39472837
5. TRIM11 suppresses ferritinophagy and gemcitabine sensitivity through UBE2N/TAX1BP1 signaling in pancreatic ductal adenocarcinoma.. *Journal of cellular physiology*. PMID: 33629745

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 63.5% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 2.8% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 7QS1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.6，有序区 91.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF00622, PF00643 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AIM2 | 0.885 | 0.294 | — |
| TRAT1 | 0.845 | 0.000 | — |
| UBE2N | 0.837 | 0.491 | — |
| MED15 | 0.778 | 0.625 | — |
| BBOX1 | 0.774 | 0.000 | — |
| PLEKHF1 | 0.769 | 0.000 | — |
| FPR2 | 0.683 | 0.000 | — |
| PYCR1 | 0.669 | 0.000 | — |
| TRIM28 | 0.661 | 0.292 | — |
| TRIM44 | 0.647 | 0.174 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000284551.6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-23213|pubmed:22829933 |
| A0A0F7RFU1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PAX6 | psi-mi:"MI:0018"(two hybrid) | pubmed:16098226|imex:IM-18993 |
| gpsA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RNF126 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM35 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| ZBTB44 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUDT9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUFIP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 7QS1 | pLDDT=88.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRIM11 — E3 ubiquitin-protein ligase TRIM11，研究基础较多，新颖性有限。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 94 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154370-TRIM11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRIM11/IF_images/TRIM11_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000154370-TRIM11/subcellular

![](https://images.proteinatlas.org/28541/254_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/28541/254_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/28541/291_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/28541/291_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/43879/765_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/43879/765_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96F44-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96F44 |
| SMART | SM00336;SM00589;SM00184;SM00449; |
| UniProt Domain [FT] | DOMAIN 268..461; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR006574;IPR003877;IPR050143;IPR000315;IPR001841;IPR013083;IPR017907; |
| Pfam | PF13765;PF00622;PF00643;PF15227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154370-TRIM11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MED15 | Intact, Biogrid | true |
| UBE2N | Intact, Biogrid | true |
| AIM2 | Biogrid | false |
| CCDC88C | Biogrid | false |
| KDM5C | Biogrid | false |
| MAPT | Biogrid | false |
| MCL1 | Biogrid | false |
| PHLPP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
