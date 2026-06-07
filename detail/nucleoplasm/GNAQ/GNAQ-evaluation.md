---
type: protein-evaluation
gene: "GNAQ"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNAQ — REJECTED (研究热度过高 (PubMed strict=536，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNAQ / GAQ |
| 蛋白名称 | Guanine nucleotide-binding protein G(q) subunit alpha |
| 蛋白大小 | 359 aa / 42.1 kDa |
| UniProt ID | P50148 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Plasma membrane; 额外: Cytosol; UniProt: Cell membrane; Golgi apparatus; Nucleus; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=536 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.0; PDB: 6VU5, 7EZM, 7F6G, 7F6H, 7F6I, 7F8W, 7W3Z |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000654, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Plasma membrane; 额外: Cytosol | Approved |
| UniProt | Cell membrane; Golgi apparatus; Nucleus; Nucleus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- heterotrimeric G-protein complex (GO:0005834)
- lysosomal membrane (GO:0005765)
- nuclear membrane (GO:0031965)
- photoreceptor outer segment (GO:0001750)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 536 |
| PubMed broad count | 994 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GAQ |

**关键文献**:
1. Uveal melanoma: From diagnosis to treatment and the science in between.. *Cancer*. PMID: 26991400
2. Capillary malformations.. *The Journal of clinical investigation*. PMID: 38618955
3. Sturge-Weber syndrome: an overview of history, genetics, clinical manifestations, and management.. *Seminars in pediatric neurology*. PMID: 39389653
4. Melanoma.. *Nature reviews. Disease primers*. PMID: 27188223
5. Malignant blue melanoma.. *Clinics in dermatology*. PMID: 39260463

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 95.6% |
| 可用 PDB 条目 | 6VU5, 7EZM, 7F6G, 7F6H, 7F6I, 7F8W, 7W3Z, 7W40, 7XOW, 8G59 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6VU5, 7EZM, 7F6G, 7F6H, 7F6I, 7F8W, 7W3Z, 7W40, 7XOW, 8G59）+ AlphaFold极高置信度预测（pLDDT=93.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000654, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| S1PR3 | 0.999 | 0.115 | — |
| HRH1 | 0.999 | 0.900 | — |
| GRM5 | 0.999 | 0.000 | — |
| PLCB1 | 0.999 | 0.555 | — |
| PLCB3 | 0.999 | 0.903 | — |
| GRK2 | 0.999 | 0.809 | — |
| S1PR2 | 0.998 | 0.226 | — |
| GRM1 | 0.998 | 0.000 | — |
| ARHGEF25 | 0.997 | 0.900 | — |
| LPAR1 | 0.997 | 0.115 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| LUM | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PPT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ADHFE1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NT5C3A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-1388758 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22118459|imex:IM-16593 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Amelx | psi-mi:"MI:0096"(pull down) | pubmed:31621902|imex:IM-26981 |
| IQSEC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:27265506|imex:IM-25492 |
| MED21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.0 + PDB: 6VU5, 7EZM, 7F6G, 7F6H, 7F6I,  | pLDDT=93.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus; Nucleus; Nucleus m / Nuclear speckles, Plasma membrane; 额外: Cytosol | 一致 |
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
1. GNAQ — Guanine nucleotide-binding protein G(q) subunit alpha，研究基础较多，新颖性有限。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 536 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 536 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50148
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156052-GNAQ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNAQ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50148
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000156052-GNAQ/subcellular

![](https://images.proteinatlas.org/10036/962_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/10036/962_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/10036/970_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/10036/970_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/10036/973_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/10036/973_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50148-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50148 |
| SMART | SM00275; |
| UniProt Domain [FT] | DOMAIN 38..359; /note="G-alpha"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01230" |
| InterPro | IPR000654;IPR001019;IPR011025;IPR027417; |
| Pfam | PF00503; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156052-GNAQ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GNB1 | Biogrid, Opencell | true |
| ARRB1 | Intact | false |
| BTK | Biogrid | false |
| CKS1B | Bioplex | false |
| CYTH1 | Biogrid | false |
| CYTH2 | Biogrid | false |
| GNG10 | Bioplex | false |
| GNG2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
