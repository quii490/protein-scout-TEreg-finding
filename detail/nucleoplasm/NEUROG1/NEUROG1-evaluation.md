---
type: protein-evaluation
gene: "NEUROG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NEUROG1 — REJECTED (研究热度过高 (PubMed strict=151，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEUROG1 / BHLHA6, NEUROD3, NGN, NGN1 |
| 蛋白名称 | Neurogenin-1 |
| 蛋白大小 | 237 aa / 25.7 kDa |
| UniProt ID | Q92886 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 25.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=151 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050359, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 151 |
| PubMed broad count | 434 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA6, NEUROD3, NGN, NGN1 |

**关键文献**:
1. Astaxanthin activates the Nrf2/Keap1/HO-1 pathway to inhibit oxidative stress and ferroptosis, reducing triphenyl phosphate (TPhP)-induced neurodevelopmental toxicity.. *Ecotoxicology and environmental safety*. PMID: 38219622
2. Essential transcription factors for induced neuron differentiation.. *Nature communications*. PMID: 38102126
3. Neurog1 and Olig2 integrate patterning and neurogenesis signals in development of zebrafish dopaminergic and glutamatergic dual transmitter neurons.. *Developmental biology*. PMID: 37944224
4. Neocortical neurogenesis: a proneural gene perspective.. *The FEBS journal*. PMID: 40545564
5. Examining the NEUROG2 lineage and associated gene expression in human cortical organoids.. *Development (Cambridge, England)*. PMID: 39680368

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 26.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 37.6% |
| 低置信 (pLDDT<50) 占比 | 30.4% |
| 有序区域 (pLDDT>70) 占比 | 32.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 32.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050359, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POU4F1 | 0.911 | 0.000 | — |
| ASCL1 | 0.886 | 0.098 | — |
| CACNA1G | 0.811 | 0.000 | — |
| CRABP1 | 0.740 | 0.000 | — |
| RUNX3 | 0.737 | 0.000 | — |
| SHH | 0.734 | 0.000 | — |
| ISL1 | 0.728 | 0.048 | — |
| LHX2 | 0.719 | 0.048 | — |
| TCF12 | 0.712 | 0.442 | — |
| SOCS1 | 0.703 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCF12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CRYAA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| DYNC1H1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| KLK6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| RUNX1T1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| CBFA2T2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| POTEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCDC85C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NEUROG1 — Neurogenin-1，研究基础较多，新颖性有限。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 151 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 151 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92886
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181965-NEUROG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEUROG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92886
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000181965-NEUROG1/subcellular

![](https://images.proteinatlas.org/72232/1944_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/72232/1944_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/72232/1958_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/72232/1958_D3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92886-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92886 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 92..144; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050359;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181965-NEUROG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TCF4 | Intact, Biogrid | true |
| ASS1 | Bioplex | false |
| CREBBP | Biogrid | false |
| CRYAA | Intact | false |
| DYNC1H1 | Intact | false |
| KLK6 | Intact | false |
| NT5C | Bioplex | false |
| TCF12 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
