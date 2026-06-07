---
type: protein-evaluation
gene: "EGLN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EGLN1 — REJECTED (研究热度过高 (PubMed strict=209，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EGLN1 / C1orf12 |
| 蛋白名称 | Egl nine homolog 1 |
| 蛋白大小 | 426 aa / 46.0 kDa |
| UniProt ID | Q9GZT9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 426 aa / 46.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=209 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.9; PDB: 2G19, 2G1M, 2HBT, 2HBU, 2Y33, 2Y34, 3HQR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051559, IPR005123, IPR006620, IPR044862, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- nucleus (GO:0005634)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 209 |
| PubMed broad count | 830 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf12 |

**关键文献**:
1. Proteome-wide Mendelian randomization and functional studies uncover therapeutic targets for polycystic ovarian syndrome.. *American journal of human genetics*. PMID: 39541979
2. Congenital erythrocytosis.. *European journal of haematology*. PMID: 33840141
3. Single-Cell and Spatial Transcriptomics Identified Fatty Acid-Binding Proteins Controlling Endothelial Glycolytic and Arterial Programming in Pulmonary Hypertension.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 40401371
4. Oncogenic TFE3 fusions drive OXPHOS and confer metabolic vulnerabilities in translocation renal cell carcinoma.. *Nature metabolism*. PMID: 39915638
5. Evolutionary history of Tibetans inferred from whole-genome sequencing.. *PLoS genetics*. PMID: 28448578

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 35.2% |
| 有序区域 (pLDDT>70) 占比 | 58.2% |
| 可用 PDB 条目 | 2G19, 2G1M, 2HBT, 2HBU, 2Y33, 2Y34, 3HQR, 3HQU, 3OUH, 3OUI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2G19, 2G1M, 2HBT, 2HBU, 2Y33, 2Y34, 3HQR, 3HQU, 3OUH, 3OUI）+ AlphaFold极高置信度预测（pLDDT=71.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051559, IPR005123, IPR006620, IPR044862, IPR002893; Pfam: PF13640, PF01753 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPAS1 | 0.999 | 0.893 | — |
| HIF1A | 0.999 | 0.968 | — |
| VHL | 0.987 | 0.545 | — |
| OS9 | 0.959 | 0.510 | — |
| EGLN3 | 0.953 | 0.510 | — |
| HIF3A | 0.950 | 0.427 | — |
| FKBP8 | 0.950 | 0.837 | — |
| ARNT | 0.943 | 0.292 | — |
| EGLN2 | 0.942 | 0.000 | — |
| ELOC | 0.920 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15721254|imex:IM-19692 |
| ZNF281 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KRAS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VHL | psi-mi:"MI:0018"(two hybrid) | pubmed:17986458 |
| pyrE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PKM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21620138|imex:IM-16544 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ERP29 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZNG1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 2G19, 2G1M, 2HBT, 2HBU, 2Y33,  | pLDDT=71.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EGLN1 — Egl nine homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小426 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 209 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 209 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZT9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135766-EGLN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EGLN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZT9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000135766-EGLN1/subcellular

![](https://images.proteinatlas.org/22129/284_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22129/284_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22129/285_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22129/285_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22129/286_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22129/286_H3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZT9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9GZT9 |
| SMART | SM00702; |
| UniProt Domain [FT] | DOMAIN 291..392; /note="Fe2OG dioxygenase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00805" |
| InterPro | IPR051559;IPR005123;IPR006620;IPR044862;IPR002893; |
| Pfam | PF13640;PF01753; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135766-EGLN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EPAS1 | Intact, Biogrid | true |
| FKBP8 | Intact, Biogrid | true |
| HIF1A | Intact, Biogrid | true |
| OS9 | Intact, Biogrid | true |
| PTGES3 | Biogrid, Opencell | true |
| CUL3 | Biogrid | false |
| EGLN3 | Biogrid | false |
| FKBP5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
