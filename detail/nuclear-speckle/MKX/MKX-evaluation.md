---
type: protein-evaluation
gene: "MKX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MKX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MKX / C10orf48, IRXL1 |
| 蛋白名称 | Homeobox protein Mohawk |
| 蛋白大小 | 352 aa / 39.3 kDa |
| UniProt ID | Q8IYA7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 352 aa / 39.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR008422; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf48, IRXL1 |

**关键文献**:
1. MKX-AS1 Gene Expression Associated with Variation in Drug Response to Oxaliplatin and Clinical Outcomes in Colorectal Cancer Patients.. *Pharmaceuticals (Basel, Switzerland)*. PMID: 37242540
2. Gene dosage-dependent roles of Mkx in postnatal tendon development and maintenance revealed by conditional deletion.. *Developmental biology*. PMID: 40550378
3. Homeodomain proteins: an update.. *Chromosoma*. PMID: 26464018
4. IRX-related homeobox gene MKX is a novel oncogene in acute myeloid leukemia.. *PloS one*. PMID: 39689089
5. The Mohawk homeobox gene represents a marker and osteo-inhibitory factor in calvarial suture osteoprogenitor cells.. *Cell death & disease*. PMID: 38886383

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.0 |
| 高置信度残基 (pLDDT>90) 占比 | 19.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.7% |
| 低置信 (pLDDT<50) 占比 | 41.5% |
| 有序区域 (pLDDT>70) 占比 | 35.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.0），有序残基占 35.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR008422; Pfam: PF05920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNMD | 0.856 | 0.000 | — |
| TCF15 | 0.796 | 0.047 | — |
| SCX | 0.750 | 0.047 | — |
| FMOD | 0.639 | 0.045 | — |
| DCN | 0.632 | 0.045 | — |
| COL1A1 | 0.602 | 0.000 | — |
| ARMC4 | 0.547 | 0.000 | — |
| BGN | 0.542 | 0.045 | — |
| EGR1 | 0.535 | 0.066 | — |
| SMAD3 | 0.522 | 0.064 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| RAB34 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CNP | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| HSH2D | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| TBL1X | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBL1XR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Fas2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| anon-WO0153538.36 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Fer1HCH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG11617 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.0 + PDB: 无 | pLDDT=63.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MKX — Homeobox protein Mohawk，研究基础较多，新颖性有限。
2. 蛋白大小352 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYA7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150051-MKX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYA7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150051-MKX/subcellular

![](https://images.proteinatlas.org/6927/1044_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/6927/1044_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/6927/71_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/6927/71_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/6927/73_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/6927/73_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYA7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IYA7 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR008422; |
| Pfam | PF05920; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000150051-MKX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Biogrid | false |
| SIN3A | Biogrid | false |
| TBL1X | Biogrid | false |
| TBL1XR1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
