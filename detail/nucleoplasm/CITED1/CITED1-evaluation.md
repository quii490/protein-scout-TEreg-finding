---
type: protein-evaluation
gene: "CITED1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CITED1 — REJECTED (研究热度过高 (PubMed strict=137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CITED1 / MSG1 |
| 蛋白名称 | Cbp/p300-interacting transactivator 1 |
| 蛋白大小 | 193 aa / 19.9 kDa |
| UniProt ID | Q99966 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 193 aa / 19.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=137 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007576; Pfam: PF04487 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 137 |
| PubMed broad count | 215 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MSG1 |

**关键文献**:
1. Roles and signaling pathways of CITED1 in tumors: overview and novel insights.. *The Journal of international medical research*. PMID: 38190845
2. CITED1 expression in odontogenic cysts.. *BMC oral health*. PMID: 38997708
3. Cited1 deficiency suppresses intestinal tumorigenesis.. *PLoS genetics*. PMID: 23935526
4. Regulation of macrophage IFNγ-stimulated gene expression by the transcriptional coregulator CITED1.. *Journal of cell science*. PMID: 36594555
5. CITED1 protein expression suggests Papillary Thyroid Carcinoma in high throughput tissue microarray-based study.. *Thyroid : official journal of the American Thyroid Association*. PMID: 15072698

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.2 |
| 高置信度残基 (pLDDT>90) 占比 | 10.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 35.2% |
| 低置信 (pLDDT<50) 占比 | 40.4% |
| 有序区域 (pLDDT>70) 占比 | 24.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.2），有序残基占 24.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007576; Pfam: PF04487 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.975 | 0.634 | — |
| CREBBP | 0.809 | 0.589 | — |
| SIX2 | 0.784 | 0.000 | — |
| SMAD4 | 0.747 | 0.230 | — |
| TFAP2A | 0.734 | 0.045 | — |
| ESR1 | 0.702 | 0.292 | — |
| TFAP2B | 0.681 | 0.294 | — |
| TFAP2C | 0.675 | 0.045 | — |
| TMEM26 | 0.663 | 0.000 | — |
| EYA1 | 0.634 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2624922 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13608|pubmed:20227041 |
| ENSP00000499148.1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13608|pubmed:20227041 |
| TP53 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13608|pubmed:20227041 |
| Twist1 | psi-mi:"MI:0096"(pull down) | pubmed:22975381|imex:IM-17775 |
| RAD21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VPS26A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCNA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CDK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.2 + PDB: 无 | pLDDT=59.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. CITED1 — Cbp/p300-interacting transactivator 1，研究基础较多，新颖性有限。
2. 蛋白大小193 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 137 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99966
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125931-CITED1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CITED1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99966
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CITED1/IF_images/CITED1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000125931-CITED1/subcellular

![](https://images.proteinatlas.org/49051/1269_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/49051/1269_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/49051/771_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/49051/771_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/49051/979_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/49051/979_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99966-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99966 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007576; |
| Pfam | PF04487; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125931-CITED1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ESR1 | Intact, Biogrid | true |
| CASP6 | Intact | false |
| CCK | Intact | false |
| CREBBP | Biogrid | false |
| EP300 | Biogrid | false |
| JUN | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
