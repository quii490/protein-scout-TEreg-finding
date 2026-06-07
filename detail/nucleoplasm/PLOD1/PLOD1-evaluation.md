---
type: protein-evaluation
gene: "PLOD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PLOD1 — REJECTED (研究热度过高 (PubMed strict=157，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLOD1 / LLH, PLOD |
| 蛋白名称 | Procollagen-lysine,2-oxoglutarate 5-dioxygenase 1 |
| 蛋白大小 | 727 aa / 83.5 kDa |
| UniProt ID | Q02809 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Rough endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 83.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=157 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050757, IPR057589, IPR044861, IPR029044, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Uncertain |
| UniProt | Rough endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic complex (GO:1902494)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- rough endoplasmic reticulum membrane (GO:0030867)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 157 |
| PubMed broad count | 207 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LLH, PLOD |

**关键文献**:
1. TEAD4 functions as a prognostic biomarker and triggers EMT via PI3K/AKT pathway in bladder cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 35581606
2. Regulation of EBNA1 protein stability and DNA replication activity by PLOD1 lysine hydroxylase.. *PLoS pathogens*. PMID: 37262099
3. P3H4 and PLOD1 expression associates with poor prognosis in bladder cancer.. *Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico*. PMID: 35149972
4. Matricellular protein CCN1 promotes collagen alignment and scar integrity after myocardial infarction.. *Matrix biology : journal of the International Society for Matrix Biology*. PMID: 39098433
5. New mechanistic insights to PLOD1-mediated human vascular disease.. *Translational research : the journal of laboratory and clinical medicine*. PMID: 34400365

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 87.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050757, IPR057589, IPR044861, IPR029044, IPR005123; Pfam: PF03171, PF25342, PF25238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLOD2 | 0.977 | 0.632 | — |
| COLGALT1 | 0.965 | 0.231 | — |
| PLOD3 | 0.965 | 0.422 | — |
| COLGALT2 | 0.929 | 0.000 | — |
| P4HA2 | 0.908 | 0.000 | — |
| CAMKMT | 0.900 | 0.000 | — |
| P4HA1 | 0.881 | 0.000 | — |
| COL5A2 | 0.865 | 0.071 | — |
| COL5A1 | 0.857 | 0.245 | — |
| CHST14 | 0.825 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Col11a1 | psi-mi:"MI:0096"(pull down) | pubmed:22038862|imex:IM-16591 |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| Q947H0 | psi-mi:"MI:0096"(pull down) | imex:IM-14965|pubmed:20217867 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 无 | pLDDT=92.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Rough endoplasmic reticulum membrane / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PLOD1 — Procollagen-lysine,2-oxoglutarate 5-dioxygenase 1，研究基础较多，新颖性有限。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 157 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 157 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02809
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083444-PLOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02809
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000083444-PLOD1/subcellular

![](https://images.proteinatlas.org/49137/682_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/49137/682_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/49137/827_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/49137/827_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/49137/829_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/49137/829_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02809-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q02809 |
| SMART | SM00702; |
| UniProt Domain [FT] | DOMAIN 636..727; /note="Fe2OG dioxygenase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00805" |
| InterPro | IPR050757;IPR057589;IPR044861;IPR029044;IPR005123;IPR006620;IPR001006; |
| Pfam | PF03171;PF25342;PF25238; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000083444-PLOD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HNRNPH1 | Biogrid, Opencell, Bioplex | true |
| HNRNPH2 | Intact, Biogrid, Bioplex | true |
| CANX | Opencell | false |
| COL4A4 | Bioplex | false |
| COL6A1 | Bioplex | false |
| COL9A3 | Bioplex | false |
| CPSF6 | Opencell | false |
| CTSS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
