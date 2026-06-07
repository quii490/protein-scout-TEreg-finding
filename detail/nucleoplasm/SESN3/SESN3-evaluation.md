---
type: protein-evaluation
gene: "SESN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SESN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SESN3 / SEST3 |
| 蛋白名称 | Sestrin-3 |
| 蛋白大小 | 492 aa / 57.3 kDa |
| UniProt ID | P58005 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 492 aa / 57.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029032, IPR006730; Pfam: PF04636 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- TORC2 complex (GO:0031932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 139 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEST3 |

**关键文献**:
1. Aerobic exercise ameliorates insulin resistance in C57BL/6 J mice via activating Sestrin3.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 36220588
2. Super-enhancer-driven core transcription factor FOXP1 delays endothelial cell senescence via phase separation-mediated SESN3 activation.. *Theranostics*. PMID: 41355963
3. A novel regulatory circuit of ATG4B and SESN3 promotes T cell leukemogenesis.. *Journal of experimental & clinical cancer research : CR*. PMID: 41275290
4. The multifaceted role of Sestrin 3 (SESN3) in oxidative stress, inflammation and tumorigenesis.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 40174866
5. Deciphering glial contributions to CSF1R-related disorder via single-nuclear transcriptomic profiling: a case study.. *Acta neuropathologica communications*. PMID: 39217398

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 59.6% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 17.3% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.5，有序区 76.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029032, IPR006730; Pfam: PF04636 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SESN1 | 0.938 | 0.000 | — |
| SESN2 | 0.910 | 0.000 | — |
| CACNA2D2 | 0.844 | 0.000 | — |
| WDR24 | 0.827 | 0.606 | — |
| TP53 | 0.796 | 0.000 | — |
| RICTOR | 0.753 | 0.000 | — |
| PRKAA2 | 0.718 | 0.000 | — |
| PRKAG2 | 0.712 | 0.000 | — |
| WDR59 | 0.711 | 0.421 | — |
| PRDX1 | 0.710 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYCBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26277|pubmed:25263562 |
| NPRL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26277|pubmed:25263562 |
| WDR59 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26277|pubmed:25263562 |
| Xpo7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29748336|pubmed:unassig |
| DSCR9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.5 + PDB: 无 | pLDDT=81.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SESN3 — Sestrin-3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小492 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58005
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149212-SESN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SESN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58005
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149212-SESN3/subcellular

![](https://images.proteinatlas.org/37935/1046_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/37935/1046_E10_4_red_green.jpg)
![](https://images.proteinatlas.org/37935/1396_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/37935/1396_D1_4_red_green.jpg)
![](https://images.proteinatlas.org/37935/451_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/37935/451_H11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58005-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P58005 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029032;IPR006730; |
| Pfam | PF04636; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149212-SESN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| WDR24 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
