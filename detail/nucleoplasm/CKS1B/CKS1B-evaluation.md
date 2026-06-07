---
type: protein-evaluation
gene: "CKS1B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CKS1B — REJECTED (研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CKS1B / CKS1 |
| 蛋白名称 | Cyclin-dependent kinases regulatory subunit 1 |
| 蛋白大小 | 79 aa / 9.7 kDa |
| UniProt ID | P61024 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria, Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 9.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.1; PDB: 1BUH, 1DKS, 1DKT, 2ASS, 2AST, 4YC6, 7B5L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000789, IPR036858; Pfam: PF01111 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cyclin-dependent protein kinase holoenzyme complex (GO:0000307)
- nucleoplasm (GO:0005654)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 239 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CKS1 |

**关键文献**:
1. CKS1B as Drug Resistance-Inducing Gene-A Potential Target to Improve Cancer Therapy.. *Frontiers in oncology*. PMID: 33102238
2. Involvement of CKS1B in the anti-inflammatory effects of cannabidiol in experimental stroke models.. *Experimental neurology*. PMID: 38104887
3. Single-cell RNA sequencing reveals the communications between tumor microenvironment components and tumor metastasis in osteosarcoma.. *Frontiers in immunology*. PMID: 39324133
4. CDC28 protein kinase regulatory subunit 1B (CKS1B) expression and genetic status analysis in oral squamous cell carcinoma.. *Histology and histopathology*. PMID: 21117028
5. CKS1B as a potential target for prognostic assessment and intervention in pancreatic cancer and its role in abnormal proliferation and cellular phenotype through mediation of cell cycle signaling pathways.. *Saudi medical journal*. PMID: 38309745

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 1BUH, 1DKS, 1DKT, 2ASS, 2AST, 4YC6, 7B5L, 7B5M, 7B5R, 7NJ0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1BUH, 1DKS, 1DKT, 2ASS, 2AST, 4YC6, 7B5L, 7B5M, 7B5R, 7NJ0）+ AlphaFold极高置信度预测（pLDDT=92.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000789, IPR036858; Pfam: PF01111 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK2 | 0.999 | 0.994 | — |
| CDK1 | 0.999 | 0.994 | — |
| SKP1 | 0.999 | 0.968 | — |
| SKP2 | 0.999 | 0.991 | — |
| CCNA2 | 0.999 | 0.976 | — |
| CCNB1 | 0.998 | 0.978 | — |
| CUL1 | 0.998 | 0.859 | — |
| CDKN1B | 0.997 | 0.984 | — |
| CKS2 | 0.993 | 0.783 | — |
| RBX1 | 0.988 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000311083.5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SKP2 | psi-mi:"MI:0096"(pull down) | pubmed:12813041 |
| SKP1 | psi-mi:"MI:0096"(pull down) | pubmed:12813041 |
| DUSP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14416|pubmed:16286470 |
| CDKN1B | psi-mi:"MI:0415"(enzymatic study) | imex:IM-12127|pubmed:18805092 |
| CDK2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9840943|imex:IM-18880 |
| CDKA-1 | psi-mi:"MI:0096"(pull down) | pubmed:9276444|imex:IM-19106 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 1BUH, 1DKS, 1DKT, 2ASS, 2AST,  | pLDDT=92.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria, Cytosol; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CKS1B — Cyclin-dependent kinases regulatory subunit 1，研究基础较多，新颖性有限。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61024
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173207-CKS1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CKS1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61024
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000173207-CKS1B/subcellular

![](https://images.proteinatlas.org/3424/1445_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1445_A10_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1450_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1450_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1476_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1476_G10_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61024-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61024 |
| SMART | SM01084; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000789;IPR036858; |
| Pfam | PF01111; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173207-CKS1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNA2 | Biogrid, Bioplex | true |
| CCNB1 | Biogrid, Bioplex | true |
| CDK1 | Intact, Biogrid | true |
| CDK2 | Intact, Biogrid, Bioplex | true |
| CDK3 | Intact, Biogrid | true |
| CDKN1A | Biogrid, Bioplex | true |
| CDKN1B | Intact, Biogrid | true |
| SKP1 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
