---
type: protein-evaluation
gene: "NEK8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEK8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK8 / JCK, NEK12A |
| 蛋白名称 | Serine/threonine-protein kinase Nek8 |
| 蛋白大小 | 692 aa / 74.8 kDa |
| UniProt ID | Q86SG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Microtubules; 额外: Nuclear speckles, Mitotic spindle, Primary; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cell projection, cilium; |
| 蛋白大小 | 10/10 | ×1 | 10 | 692 aa / 74.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=64 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR017441, IPR058923, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Nuclear speckles, Mitotic spindle, Primary cilium | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cell projection, cilium; Cytoplasm, cytoskeleton, microtubule or... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centrosome (GO:0005813)
- ciliary base (GO:0097546)
- ciliary inversin compartment (GO:0097543)
- cilium (GO:0005929)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 64 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: JCK, NEK12A |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Certain heterozygous variants in the kinase domain of the serine/threonine kinase NEK8 can cause an autosomal dominant form of polycystic kidney disease.. *Kidney international*. PMID: 37598857
3. NEK8, a NIMA-family protein kinase at the core of the ciliary INV complex.. *Cell communication and signaling : CCS*. PMID: 40189576
4. Nek8 regulates the expression and localization of polycystin-1 and polycystin-2.. *Journal of the American Society of Nephrology : JASN*. PMID: 18235101
5. NEK8 promotes the progression of gastric cancer by reprogramming asparagine metabolism.. *Molecular medicine (Cambridge, Mass.)*. PMID: 39762761

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.4% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.9，有序区 85.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR058923, IPR009091; Pfam: PF00069, PF25390 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKS6 | 0.993 | 0.626 | — |
| NPHP3 | 0.991 | 0.000 | — |
| INVS | 0.952 | 0.154 | — |
| ANKS3 | 0.913 | 0.596 | — |
| PIK3C2A | 0.796 | 0.000 | — |
| NPHP4 | 0.782 | 0.000 | — |
| PKD1 | 0.761 | 0.000 | — |
| PKD2 | 0.748 | 0.000 | — |
| SRI | 0.727 | 0.000 | — |
| NPHP1 | 0.706 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 无 | pLDDT=84.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cell projectio / Microtubules; 额外: Nuclear speckles, Mitotic spindl | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NEK8 — Serine/threonine-protein kinase Nek8，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小692 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 64 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86SG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160602-NEK8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86SG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (approved)。来源: https://www.proteinatlas.org/ENSG00000160602-NEK8/subcellular

![](https://images.proteinatlas.org/40679/418_A12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/40679/418_A12_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/40679/424_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40679/424_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40679/429_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40679/429_A12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86SG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86SG6 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 4..258; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR017441;IPR058923;IPR009091;IPR000408;IPR008271;IPR051997;IPR044120; |
| Pfam | PF00069;PF25390; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160602-NEK8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKS3 | Intact, Biogrid | true |
| ANKS6 | Intact, Biogrid | true |
| NEK7 | Intact, Biogrid | true |
| NUDCD2 | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| CACYBP | Biogrid | false |
| HSP90AA1 | Biogrid | false |
| HSP90AB1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
