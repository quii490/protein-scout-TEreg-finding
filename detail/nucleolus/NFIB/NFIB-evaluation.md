---
type: protein-evaluation
gene: "NFIB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFIB — REJECTED (研究热度过高 (PubMed strict=391，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFIB |
| 蛋白名称 | Nuclear factor 1 B-type |
| 蛋白大小 | 420 aa / 47.4 kDa |
| UniProt ID | O00712 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 420 aa / 47.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=391 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000647, IPR020604, IPR019739, IPR019548, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cerebellar mossy fiber (GO:0044300)
- chromatin (GO:0000785)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 391 |
| PubMed broad count | 592 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Histological types of breast cancer: how special are they?. *Molecular oncology*. PMID: 20452298
2. Increased retinoic acid signaling decreases lung metastasis in salivary adenoid cystic carcinoma by inhibiting the noncanonical Notch1 pathway.. *Experimental & molecular medicine*. PMID: 36879115
3. ASCL1 and NEUROD1 Reveal Heterogeneity in Pulmonary Neuroendocrine Tumors and Regulate Distinct Genetic Programs.. *Cell reports*. PMID: 27452466
4. Single-Cell RNA-Seq Analysis of Retinal Development Identifies NFI Factors as Regulating Mitotic Exit and Late-Born Cell Specification.. *Neuron*. PMID: 31128945
5. HMGA2-WIF1 Rearrangements Characterize a Distinctive Subset of Salivary Pleomorphic Adenomas With Prominent Trabecular (Canalicular Adenoma-like) Morphology.. *The American journal of surgical pathology*. PMID: 34324456

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 43.8% |
| 有序区域 (pLDDT>70) 占比 | 45.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 45.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000647, IPR020604, IPR019739, IPR019548, IPR003619; Pfam: PF00859, PF03165, PF10524 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFIX | 0.832 | 0.781 | — |
| NFIC | 0.815 | 0.783 | — |
| NFIA | 0.812 | 0.705 | — |
| SOX2 | 0.757 | 0.607 | — |
| MPDZ | 0.735 | 0.000 | — |
| SLC1A3 | 0.721 | 0.000 | — |
| HMGA2 | 0.707 | 0.087 | — |
| LNX1 | 0.664 | 0.000 | — |
| PAX6 | 0.649 | 0.294 | — |
| SOX9 | 0.615 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sox2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| NFIC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFIX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRCC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Osgep | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Dctn3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cry1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli fibrillar center | 一致 |
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
1. NFIB — Nuclear factor 1 B-type，研究基础较多，新颖性有限。
2. 蛋白大小420 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 391 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 391 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00712
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147862-NFIB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFIB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00712
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000147862-NFIB/subcellular

![](https://images.proteinatlas.org/3956/26_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/3956/26_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/3956/27_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/3956/27_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/3956/28_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/3956/28_H11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00712-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00712 |
| SMART | SM00523; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000647;IPR020604;IPR019739;IPR019548;IPR003619; |
| Pfam | PF00859;PF03165;PF10524; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
