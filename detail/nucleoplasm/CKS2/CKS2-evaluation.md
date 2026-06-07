---
type: protein-evaluation
gene: "CKS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CKS2 — REJECTED (研究热度过高 (PubMed strict=160，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CKS2 |
| 蛋白名称 | Cyclin-dependent kinases regulatory subunit 2 |
| 蛋白大小 | 79 aa / 9.9 kDa |
| UniProt ID | P33552 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria, Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 9.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=160 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.5; PDB: 1CKS, 4Y72, 4YC3, 5HQ0, 5LQF, 6GU2, 6GU3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000789, IPR036858; Pfam: PF01111 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cyclin-dependent protein kinase holoenzyme complex (GO:0000307)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 160 |
| PubMed broad count | 218 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of osteoarthritis-associated chondrocyte subpopulations and key gene-regulating drugs based on multi-omics analysis.. *Scientific reports*. PMID: 40216809
2. Biological functions and therapeutic potential of CKS2 in human cancer.. *Frontiers in oncology*. PMID: 39188686
3. High Expression of CKS2 Predicts Adverse Outcomes: A Potential Therapeutic Target for Glioma.. *Frontiers in immunology*. PMID: 35663965
4. Prognostic significance of cyclin-dependent kinase subunit 2 (CKS2) in malignant tumours: a meta-analysis and bioinformatic analysis.. *BMJ open*. PMID: 38296306
5. CKS2 Mediates Hepatocellular Carcinoma Recurrence After Hepatic Ischemia-Reperfusion Injury Related to M2 Macrophages.. *Journal of inflammation research*. PMID: 40908951

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.5 |
| 高置信度残基 (pLDDT>90) 占比 | 87.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 1CKS, 4Y72, 4YC3, 5HQ0, 5LQF, 6GU2, 6GU3, 6GU4, 6GU6, 6GU7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CKS, 4Y72, 4YC3, 5HQ0, 5LQF, 6GU2, 6GU3, 6GU4, 6GU6, 6GU7）+ AlphaFold极高置信度预测（pLDDT=92.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000789, IPR036858; Pfam: PF01111 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCNB1 | 0.999 | 0.978 | — |
| CDK1 | 0.999 | 0.992 | — |
| CDK2 | 0.994 | 0.895 | — |
| CKS1B | 0.993 | 0.783 | — |
| CCNA2 | 0.990 | 0.850 | — |
| SKP2 | 0.982 | 0.114 | — |
| CCNB2 | 0.976 | 0.797 | — |
| CDC20 | 0.971 | 0.453 | — |
| SKP1 | 0.971 | 0.071 | — |
| CDK3 | 0.956 | 0.898 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSC22D4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GRB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VTN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FZR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| FZR3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CDKA-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CDKB1-2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CDKB2-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.5 + PDB: 1CKS, 4Y72, 4YC3, 5HQ0, 5LQF,  | pLDDT=92.5, v6 | 预测+实验 |
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

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CKS2 — Cyclin-dependent kinases regulatory subunit 2，研究基础较多，新颖性有限。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 160 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 160 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P33552
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123975-CKS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CKS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P33552
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000123975-CKS2/subcellular

![](https://images.proteinatlas.org/3424/1445_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1445_A10_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1450_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1450_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1476_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3424/1476_G10_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P33552-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P33552 |
| SMART | SM01084; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000789;IPR036858; |
| Pfam | PF01111; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123975-CKS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNA2 | Biogrid, Bioplex | true |
| CCNB1 | Biogrid, Bioplex | true |
| CCNB2 | Biogrid, Bioplex | true |
| CDK2 | Biogrid, Bioplex | true |
| CDK3 | Intact, Biogrid | true |
| CDKN1A | Biogrid, Bioplex | true |
| PKMYT1 | Biogrid, Opencell | true |
| CDK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
