---
type: protein-evaluation
gene: "GRHL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GRHL2 — REJECTED (研究热度过高 (PubMed strict=192，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRHL2 / BOM, TFCP2L3 |
| 蛋白名称 | Grainyhead-like protein 2 homolog |
| 蛋白大小 | 625 aa / 71.1 kDa |
| UniProt ID | Q6ISB3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 625 aa / 71.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=192 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 5MR7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007604, IPR057520, IPR040167; Pfam: PF04516, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell-cell junction (GO:0005911)
- chromatin (GO:0000785)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 192 |
| PubMed broad count | 296 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BOM, TFCP2L3 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Reprogramming the GRHL2-CDK19 axis by gene therapy alleviates prostate aging.. *Nature aging*. PMID: 41266629
3. Generation of a Biliary Tract Cancer Cell Line Atlas Identifies Molecular Subtypes and Therapeutic Targets.. *Cancer discovery*. PMID: 40353839
4. GRHL2-controlled gene expression networks in luminal breast cancer.. *Cell communication and signaling : CCS*. PMID: 36691073
5. The MLL3/GRHL2 complex regulates malignant transformation and anti-tumor immunity in squamous cancer.. *The Journal of experimental medicine*. PMID: 39964485

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 42.4% |
| 有序区域 (pLDDT>70) 占比 | 53.2% |
| 可用 PDB 条目 | 5MR7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 53.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007604, IPR057520, IPR040167; Pfam: PF04516, PF25416 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESRP1 | 0.891 | 0.000 | — |
| OVOL2 | 0.832 | 0.000 | — |
| OVOL1 | 0.674 | 0.000 | — |
| RAB25 | 0.668 | 0.000 | — |
| FOXA1 | 0.665 | 0.292 | — |
| KMT2C | 0.642 | 0.068 | — |
| CDH1 | 0.642 | 0.000 | — |
| GATA3 | 0.616 | 0.000 | — |
| LMO4 | 0.610 | 0.605 | — |
| HOXB13 | 0.596 | 0.061 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| GRHL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMO4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| C4A | psi-mi:"MI:0030"(cross-linking study) | pubmed:26153859|imex:IM-26734 |
| ESR1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:26153859|imex:IM-26734 |
| PAX5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PAX6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PIAS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBI-26476579 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 5MR7 | pLDDT=66.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GRHL2 — Grainyhead-like protein 2 homolog，研究基础较多，新颖性有限。
2. 蛋白大小625 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 192 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 192 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

GRHL2（Grainyhead-like protein 2 homolog）。定位于nucleoplasm及chromatin（GO:0000785）。包含625 aa / 71.1 kDa。UniProt编号Q6ISB3。其InterPro结构域组成为IPR007604、IPR057520、IPR040167。Pfam注释2个保守结构域（PF04516、PF25416）。AlphaFold预测三维结构pLDDT=66.9（中等置信度），高置信残基占比仅37.8%，低置信残基（pLDDT<50）占比42.4%，有序区域占比53.2%。实验结构PDB条目5MR7为其DNA结合域提供了部分结构数据。

从功能机制角度，GRHL2是一个CP2/Grh家族转录因子，含有Grh/CP2 DNA结合结构域（aa 244-482，PROSITE-ProRule:PRU01313），能直接识别CpG岛和特定DNA基序，调控上皮细胞分化、细胞间连接形成等关键生物学过程。文献证据表明GRHL2通过MLL3/GRHL2复合物（PPI网络显示与KMT2C/MLL3 STRING score=0.642）调控鳞状细胞癌恶性转化与抗肿瘤免疫（PMID:39964485），通过GRHL2-CDK19轴调控前列腺衰老进程（PMID:41266629），在胆道癌中作为分子分型标志物（PMID:40353839），并在腔面型乳腺癌中控制广泛的基因表达网络（PMID:36691073）。其chromatin直接定位注释（GO:0000785）进一步确认其作为染色质结合调控因子的功能身份。PPI网络显示其与ESRP1（STRING score=0.891）、OVOL2（0.832）、FOXA1（0.665）、LMO4（0.610，含实验验证score=0.605）、HOXB13（0.596）等存在高置信度互作。IntAct实验验证互作包括Sall4（PMID:20362541）、Tfcp2l1、GRHL1、PAX5、PAX6、PIAS2等发育转录因子，提示GRHL2在转录调控网络中居于枢纽位置。

从结构生物学角度，该蛋白预测结构质量较低（pLDDT=66.9），42.4%残基处于低置信区域（pLDDT<50），提示存在大量内在无序区（IDR）及灵活片段。在真核转录因子中，IDR区域常介导液-液相分离（LLPS），通过形成转录凝聚体富集Pol II和共激活因子。GRHL2的chromatin直接定位与CpG结合能力使其成为TE调控的直接候选因子——其DNA结合域可能直接识别TE序列中的CpG元件，而IDR区域可能驱动TE区域的转录凝聚体形成。

从研究转化角度，PubMed strict检索共192篇文献，已超过100篇筛选阈值（评分0/10），整体评定为REJECTED。但值得注意的是，其与TE调控的直接关联尚未被任何文献报道，在TE特异性功能层面仍属新颖方向。综合评分44.7/100，虽不满足本研究的新颖性筛选标准，但其chromatin定位与TF枢纽功能使其在TE机制研究的背景参考中仍有重要价值。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ISB3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083307-GRHL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRHL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ISB3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000083307-GRHL2/subcellular

![](https://images.proteinatlas.org/62839/1287_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/62839/1287_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/62839/1315_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/62839/1315_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/62839/1424_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/62839/1424_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ISB3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ISB3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 244..482; /note="Grh/CP2 DB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01313" |
| InterPro | IPR007604;IPR057520;IPR040167; |
| Pfam | PF04516;PF25416; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000083307-GRHL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AR | Biogrid | false |
| GRHL1 | Intact | false |
| GRHL3 | Biogrid | false |
| GSN | Biogrid | false |
| LMO4 | Intact | false |
| PAX5 | Intact | false |
| PAX6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
