---
type: protein-evaluation
gene: "EZH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EZH1 — REJECTED (研究热度过高 (PubMed strict=203，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EZH1 / KIAA0388 |
| 蛋白名称 | Histone-lysine N-methyltransferase EZH1 |
| 蛋白大小 | 747 aa / 85.3 kDa |
| UniProt ID | Q92800 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 747 aa / 85.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=203 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.6; PDB: 7KSO, 7KSR, 7KTP, 7TD5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026489, IPR045318, IPR048358, IPR021654, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- ESC/E(Z) complex (GO:0035098)
- heterochromatin (GO:0000792)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 203 |
| PubMed broad count | 365 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0388 |

**关键文献**:
1. Mechanisms of action and resistance in histone methylation-targeted therapy.. *Nature*. PMID: 38383791
2. Targeting Excessive EZH1 and EZH2 Activities for Abnormal Histone Methylation and Transcription Network in Malignant Lymphomas.. *Cell reports*. PMID: 31747604
3. Genetic insights into idiopathic pulmonary fibrosis: a multi-omics approach to identify potential therapeutic targets.. *Journal of translational medicine*. PMID: 40091050
4. The role of EZH1 and EZH2 in development and cancer.. *BMB reports*. PMID: 36476271
5. PRC2-EZH1 contributes to circadian gene expression by orchestrating chromatin states and RNA polymerase II complex stability.. *The EMBO journal*. PMID: 39433902

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 67.6% |
| 可用 PDB 条目 | 7KSO, 7KSR, 7KTP, 7TD5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7KSO, 7KSR, 7KTP, 7TD5）+ AlphaFold高质量预测（pLDDT=74.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026489, IPR045318, IPR048358, IPR021654, IPR044438; Pfam: PF21358, PF11616, PF18118 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EZH2 | 0.999 | 0.786 | — |
| SUZ12 | 0.999 | 0.997 | — |
| EED | 0.999 | 0.997 | — |
| RBBP7 | 0.999 | 0.729 | — |
| RBBP4 | 0.999 | 0.930 | — |
| AEBP2 | 0.999 | 0.972 | — |
| JARID2 | 0.998 | 0.959 | — |
| RING1 | 0.978 | 0.091 | — |
| RNF2 | 0.974 | 0.091 | — |
| PHF19 | 0.971 | 0.827 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Eed | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Stk38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Jarid2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Suz12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Aebp2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Rbbp4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Mtf2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| CCNDBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PHF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 7KSO, 7KSR, 7KTP, 7TD5 | pLDDT=74.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. EZH1 — Histone-lysine N-methyltransferase EZH1，研究基础较多，新颖性有限。
2. 蛋白大小747 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 203 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 203 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92800
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108799-EZH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EZH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92800
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000108799-EZH1/subcellular

![](https://images.proteinatlas.org/5478/118_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/5478/118_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/5478/119_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/5478/119_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/5478/120_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/5478/120_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92800-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92800 |
| SMART | SM01114;SM00717;SM00317; |
| UniProt Domain [FT] | DOMAIN 504..606; /note="CXC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00970"; DOMAIN 613..728; /note="SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00190" |
| InterPro | IPR026489;IPR045318;IPR048358;IPR021654;IPR044438;IPR041343;IPR041355;IPR001005;IPR001214;IPR046341;IPR033467; |
| Pfam | PF21358;PF11616;PF18118;PF18264;PF00856; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108799-EZH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EED | Intact, Biogrid | true |
| AEBP2 | Biogrid | false |
| BRAF | Intact | false |
| EPOP | Biogrid | false |
| EZH2 | Biogrid | false |
| JARID2 | Biogrid | false |
| LCOR | Biogrid | false |
| MTF2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
