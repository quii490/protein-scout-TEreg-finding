---
type: protein-evaluation
gene: "BBS9"
date: 2026-06-03
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## BBS9 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BBS9 / PTHB1 |
| 蛋白全名 | Protein PTHB1 |
| 蛋白大小 | 887 aa / 99.3 kDa |
| UniProt ID | Q3SYG4 (BBS9_HUMAN) |
| 功能描述 | The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the pri... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | GO-CC nuclear: nucleoplasm (IDA:HPA) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 887 aa / 99.3 kDa, <300或>800 |
| 研究新颖性 | 6/10 | x5 | 30.0 | PubMed strict=60（中等偏少，41-60→6分） |
| 三维结构 | 9/10 | x3 | 27.0 | PDB X-ray confirmed (1 entries); AF mean pLDDT 85.1 |
| 调控结构域 | 3/10 | x2 | 6.0 | No clear regulatory domain identified |
| PPI 网络 | 2/10 | x3 | 6.0 | IntAct experiment: 15 partners (0 regulatory: none identified) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **91/180**************** | |
| **归一化总分 (÷1.83)** | | | **49.7/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Primary cilium, Primary cilium tip, Primary cilium transition zone, Flagellar centriole, Mid piece, Principal piece |
| HPA 额外定位 | Nucleoplasm, Vesicles, Cytosol, Acrosome, Equatorial segment |
| 抗体可靠性 | Supported |
| IF 图像 | IF images available (2 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 60 |
| symbol_only (Title/Abstract) | 93 |
| broad (all fields) | 99 |

1. PMID 20301537: Adam MP, Bick S, Mirzaa GM (1993). "Bardet-Biedl Syndrome Overview.." **.
2. PMID 30651579: Sewda A, White SR, Erazo M (2019 Mar). "Nonsyndromic craniosynostosis: novel coding variants.." *Pediatric research*.
3. PMID 39327728: Tinh NH, Hop NV, Phuong PT (2024 Nov). "Novel genotyping assay for a 212-kb deletion from the BBS9 gene, and frequency of the allele in pig populations in Vietnam.." *Journal of veterinary diagnostic investigation : official publication of the American Association of Veterinary Laboratory Diagnosticians, Inc*.
4. PMID 16380913: Nishimura DY, Swiderski RE, Searby CC (2005 Dec). "Comparative genomics and gene expression analysis identifies BBS9, a new Bardet-Biedl syndrome gene.." *American journal of human genetics*.
5. PMID 32256100: Perez-Garcia J, Espuela-Ortiz A, Lorenzo-Diaz F (2020). "Pharmacogenetics of Pediatric Asthma: Current Perspectives.." *Pharmacogenomics and personalized medicine*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 85.1 |
| pLDDT >90 | 61.2% |
| pLDDT 70-90 | 26.0% |
| pLDDT 50-70 | 3.9% |
| pLDDT <50 | 8.8% |

**评价**: AlphaFold 预测整体置信度极高（mean pLDDT 85.1，61% 残基 >90），蛋白折叠预测可靠。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 4YD8 | X-ray | 1.80 A | A/B=1-407 |
| 6XT9 | EM | 3.80 A | I=1-887 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR028074 | IPR entry IPR028074 |
| InterPro | IPR028073 | IPR entry IPR028073 |
| InterPro | IPR026511 | IPR entry IPR026511 |
| InterPro | IPR055364 | IPR entry IPR055364 |
| InterPro | IPR055363 | IPR entry IPR055363 |
| InterPro | IPR055362 | IPR entry IPR055362 |
| Pfam | PF14727 | Pfam entry PF14727 |
| Pfam | PF23339 | Pfam entry PF23339 |
| Pfam | PF14728 | Pfam entry PF14728 |
| Pfam | PF23338 | Pfam entry PF23338 |
| Pfam | PF23337 | Pfam entry PF23337 |

**评价**: BBSome 复合物组分，参与纤毛蛋白的运输。BBS9/PTHB1 是 BBSome 的核心亚基之一，主要在纤毛生成和维持中发挥作用。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| BBS1 | 0.999 | 0.989 | 0.900 | 0.999 |
| BBS5 | 0.999 | 0.892 | 0.900 | 0.999 |
| TTC8 | 0.999 | 0.970 | 0.900 | 0.985 |
| BBIP1 | 0.999 | 0.000 | 0.900 | 0.998 |
| BBS4 | 0.999 | 0.962 | 0.900 | 0.999 |
| BBS7 | 0.999 | 0.873 | 0.900 | 0.999 |
| BBS2 | 0.999 | 0.881 | 0.900 | 0.999 |
| LZTFL1 | 0.986 | 0.846 | 0.500 | 0.832 |
| BBS10 | 0.976 | 0.292 | 0.400 | 0.948 |
| BBS12 | 0.967 | 0.292 | 0.400 | 0.927 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| tdk | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 | psi-mi:"MI:0915"(physical association) |
| ARL6 | psi-mi:"MI:0096"(pull down) | imex:IM-14958|pubmed:20603001 | psi-mi:"MI:0914"(association) |
| Sstr3 | psi-mi:"MI:0096"(pull down) | imex:IM-14958|pubmed:20603001 | psi-mi:"MI:0914"(association) |
| BBS4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14959|pubmed:17574030 | psi-mi:"MI:0914"(association) |
| BBS1 | psi-mi:"MI:0029"(cosedimentation through density gradient) | imex:IM-14959|pubmed:17574030 | psi-mi:"MI:0915"(physical association) |
| BBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14959|pubmed:17574030 | psi-mi:"MI:0915"(physical association) |
| BBS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14959|pubmed:17574030 | psi-mi:"MI:0915"(physical association) |
| TTC8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14959|pubmed:17574030 | psi-mi:"MI:0915"(physical association) |
| BBS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 | psi-mi:"MI:0914"(association) |
| Bbs1 | psi-mi:"MI:0029"(cosedimentation through density gradient) | pubmed:22500027|imex:IM-17327 | psi-mi:"MI:0403"(colocalization) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| BBS1 | 16 |
| BBS10 | 2 |
| BBS12 | 2 |
| BBS2 | 16 |
| BBS4 | 7 |
| BBS5 | 9 |
| BBS7 | 10 |
| IQCB1 | 5 |
| LZTFL1 | 11 |
| TTC8 | 3 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 综合评分一般，多维度均未显示突出优势

**风险/不确定性**:
1. 核定位证据偏弱（得分 4/10），需要更多的实验验证
2. 研究热度偏高（60 篇），创新空间有限

**分类**: nucleus-cytoplasm
**综合评分**: 50/100

---

**数据来源**: UniProt Q3SYG4, HPA ENSG00000122507, AlphaFold AF-Q3SYG4-F1, STRING, IntAct

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Primary cilium (supported)。来源: https://www.proteinatlas.org/ENSG00000122507-BBS9/subcellular

![](https://images.proteinatlas.org/21289/2200_E4_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/21289/2200_E4_45_blue_red_green.jpg)
![](https://images.proteinatlas.org/21289/2121_G12_19_red_green.jpg)
![](https://images.proteinatlas.org/21289/2121_G12_8_red_green.jpg)
![](https://images.proteinatlas.org/21289/2128_E11_16_red_green.jpg)
![](https://images.proteinatlas.org/21289/2128_E11_79_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3SYG4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3SYG4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028074;IPR028073;IPR026511;IPR055364;IPR055363;IPR055362; |
| Pfam | PF14727;PF23339;PF14728;PF23338;PF23337; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000122507-BBS9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BBS1 | Intact, Biogrid | true |
| BBS5 | Intact, Biogrid | true |
| BBS7 | Intact, Biogrid | true |
| LZTFL1 | Intact, Biogrid, Bioplex | true |
| BBS2 | Intact | false |
| BBS4 | Intact | false |
| IQCB1 | Intact | false |
| NME3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
