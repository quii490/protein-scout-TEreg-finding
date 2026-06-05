---
type: protein-evaluation
gene: "EXOC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXOC4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC4 / KIAA1699, SEC8, SEC8L1 |
| 蛋白名称 | Exocyst complex component 4 |
| 蛋白大小 | 974 aa / 110.5 kDa |
| UniProt ID | Q96A65 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Midbody, Midbody ring; Cell projection; Cytoplasm, cytoskele |
| 蛋白大小 | 8/10 | ×1 | 8 | 974 aa / 110.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=78.7; PDB: 7PC5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039682, IPR007191, IPR048630; Pfam: PF20652, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Midbody, Midbody ring; Cell projection; Cytoplasm, cytoskeleton, microtubule organizing center, cent... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- exocyst (GO:0000145)
- Flemming body (GO:0090543)
- growth cone membrane (GO:0032584)
- membrane (GO:0016020)
- microvillus (GO:0005902)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 97 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1699, SEC8, SEC8L1 |

**关键文献**:
1. Unveiling EXOC4/SEC8: a key player in enhancing antiviral immunity by inhibiting the FBXL19-STING1-SQSTM1 signaling axis.. *Autophagy*. PMID: 40413753
2. Altered methylation pattern in EXOC4 is associated with stroke outcome: an epigenome-wide association study.. *Clinical epigenetics*. PMID: 36180927
3. Schizophrenia-Related Synaptic Dysfunction and Abnormal Sensorimotor Gating in Akap11-Deficient Mice.. *Schizophrenia bulletin*. PMID: 40408419
4. Polymorphisms near EXOC4 and LRGUK on chromosome 7q32 are associated with Type 2 Diabetes and fasting glucose; the NHLBI Family Heart Study.. *BMC medical genetics*. PMID: 18498660
5. The Association of an SNP in the EXOC4 Gene and Reproductive Traits Suggests Its Use as a Breeding Marker in Pigs.. *Animals : an open access journal from MDPI*. PMID: 33671441

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.7 |
| 高置信度残基 (pLDDT>90) 占比 | 44.5% |
| 置信残基 (pLDDT 70-90) 占比 | 29.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 73.6% |
| 可用 PDB 条目 | 7PC5 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=78.7，有序区 73.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039682, IPR007191, IPR048630; Pfam: PF20652, PF04048 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC2 | 0.999 | 0.992 | — |
| EXOC7 | 0.999 | 0.993 | — |
| EXOC6 | 0.999 | 0.978 | — |
| EXOC1 | 0.999 | 0.993 | — |
| EXOC3 | 0.999 | 0.985 | — |
| EXOC5 | 0.999 | 0.993 | — |
| EXOC8 | 0.999 | 0.993 | — |
| EXOC6B | 0.993 | 0.942 | — |
| RALA | 0.988 | 0.125 | — |
| EXOC3L1 | 0.969 | 0.867 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| NFKBIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DTNBP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| EXOC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| nef | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| WASHC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-17363|pubmed:24344185 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.7 + PDB: 7PC5 | pLDDT=78.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Midbody, Midbody ring; Cell projection; Cytoplasm, / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EXOC4 — Exocyst complex component 4，非常新颖，仅有少数基础研究。
2. 蛋白大小974 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A65
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131558-EXOC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A65
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96A65-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
