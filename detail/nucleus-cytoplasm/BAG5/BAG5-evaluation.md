---
type: protein-evaluation
gene: "BAG5"
date: 2026-06-03
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## BAG5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BAG5 / KIAA0873 |
| 蛋白全名 | BAG family molecular chaperone regulator 5 |
| 蛋白大小 | 447 aa / 51.2 kDa |
| UniProt ID | Q9UL15 (BAG5_HUMAN) |
| 功能描述 | Co-chaperone for HSP/HSP70 proteins. It functions as a nucleotide-exchange factor promoting the release of ADP from HSP70, thereby activating HSP70-mediated protein refolding (PubMed:20223214). Has an essential role in maintaining proteostasis at junctional membrane complexes (JMC), where it may function as a scaffold between the HSPA8 chaperone and JMC proteins enabling correct, HSPA8-dependent J... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | GO-CC nuclear: nucleus (IDA:ParkinsonsUK-UCL); perinuclear region of cytoplasm (IDA:BHF-UCL) |
| 蛋白大小 | 10/10 | x1 | 10.0 | 447 aa / 51.2 kDa, 300-800理想区间 |
| 研究新颖性 | 4/10 | x5 | 20.0 | PubMed strict=73（中等偏多，61-80→4分） |
| 三维结构 | 10/10 | x3 | 30.0 | PDB X-ray (1 entries) + AF pLDDT mean 90.5, 71%>90 |
| 调控结构域 | 6/10 | x2 | 12.0 | Ubiquitin pathway enzyme |
| PPI 网络 | 4/10 | x3 | 12.0 | IntAct experiment: 15 partners (2 regulatory: CIRBP, CUL3) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **100/180**************** | |
| **归一化总分 (÷1.83)** | | | **54.6/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Vesicles |
| HPA 额外定位 | Nucleoplasm, Plasma membrane, Primary cilium, Primary cilium tip, Centrosome, Basal body |
| 抗体可靠性 | Approved |
| IF 图像 | IF images available (6 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 73 |
| symbol_only (Title/Abstract) | 97 |
| broad (all fields) | 102 |

1. PMID 38454159: Gan S, Zhou S, Ma J (2024 Apr). "BAG5 regulates HSPA8-mediated protein folding required for sperm head-tail coupling apparatus assembly.." *EMBO reports*.
2. PMID 37903258: Wu S, Edskes HK, Wickner RB (2023 Nov 7). "Human proteins curing yeast prions.." *Proceedings of the National Academy of Sciences of the United States of America*.
3. PMID 39788499: Pan Q, Hu X, Guo K (2024 Jul 28). "Beta-amyloid protein regulates miR-15a and activates Bag5 to influence neuronal apoptosis in Alzheimer's disease.." *Zhong nan da xue xue bao. Yi xue ban = Journal of Central South University. Medical sciences*.
4. PMID 35821856: Gupta MK, Randhawa PK, Masternak MM (2022). "Role of BAG5 in Protein Quality Control: Double-Edged Sword?." *Frontiers in aging*.
5. PMID 33137395: Zou Z, Zheng Q, Cai J (2021 Mar). "Identification of BAG5 from orange-spotted grouper (Epinephelus coioides) involved in viral infection.." *Developmental and comparative immunology*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 90.5 |
| pLDDT >90 | 71.1% |
| pLDDT 70-90 | 23.0% |
| pLDDT 50-70 | 5.1% |
| pLDDT <50 | 0.7% |

**评价**: AlphaFold 预测整体置信度极高（mean pLDDT 90.5，71% 残基 >90），蛋白折叠预测可靠。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 2D9D | NMR | - | A=275-350 |
| 3A8Y | X-ray | 2.30 A | C/D=341-447 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR039773 | IPR entry IPR039773 |
| InterPro | IPR036533 | IPR entry IPR036533 |
| InterPro | IPR003103 | IPR entry IPR003103 |
| Pfam | PF02179 | Pfam entry PF02179 |

**评价**: BAG domain (PF02179) 是 Hsp70/Hsc70 分子伴侣的核苷酸交换因子结合模块。BAG5 调控分子伴侣辅助的蛋白折叠和降解，与帕金森病相关。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| HSPA1B | 0.991 | 0.982 | 0.400 | 0.218 |
| HSPA8 | 0.979 | 0.664 | 0.400 | 0.903 |
| HSPA4 | 0.960 | 0.669 | 0.400 | 0.810 |
| HSPA1A | 0.956 | 0.911 | 0.400 | 0.232 |
| BAG2 | 0.955 | 0.292 | 0.400 | 0.903 |
| GAK | 0.936 | 0.301 | 0.000 | 0.911 |
| STUB1 | 0.919 | 0.538 | 0.000 | 0.829 |
| BAG1 | 0.918 | 0.000 | 0.400 | 0.866 |
| HSPA2 | 0.893 | 0.671 | 0.400 | 0.490 |
| RAB29 | 0.890 | 0.292 | 0.000 | 0.851 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216883 | psi-mi:"MI:0915"(physical association) |
| MAP3K1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216883 | psi-mi:"MI:0915"(physical association) |
| CIRBP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| ATG2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 | psi-mi:"MI:0914"(association) |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 | psi-mi:"MI:0914"(association) |
| Tnf | psi-mi:"MI:0096"(pull down) | imex:IM-12051|pubmed:17623297 | psi-mi:"MI:0914"(association) |
| HSP70-1 | psi-mi:"MI:0047"(far western blotting) | pubmed:16003391|imex:IM-18904 | psi-mi:"MI:0407"(direct interaction) |
| UIMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| OTUD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| BANP | 3 |
| CDCA7L | 3 |
| DES | 3 |
| EFEMP1 | 3 |
| FAM118B | 3 |
| GOLGA6A | 3 |
| HSPA1B | 6 |
| KASH5 | 6 |
| KRTAP5-4 | 3 |
| LCE2C | 3 |
| LRRK1 | 3 |
| LRRK2 | 12 |
| MAD1L1 | 10 |
| THAP1 | 7 |
| TOM1 | 3 |
| TRIM27 | 6 |
|  | 2 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 蛋白大小适中（447 aa），适合重组表达和结构研究

**风险/不确定性**:
1. 核定位证据偏弱（得分 4/10），需要更多的实验验证
2. 研究热度偏高（73 篇），创新空间有限

**分类**: nucleus-cytoplasm
**综合评分**: 55/100

---

**数据来源**: UniProt Q9UL15, HPA ENSG00000166170, AlphaFold AF-Q9UL15-F1, STRING, IntAct

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000166170-BAG5/subcellular

![](https://images.proteinatlas.org/16429/131_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16429/131_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16429/132_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16429/132_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16429/164_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16429/164_D1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UL15-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UL15 |
| SMART | SM00264; |
| UniProt Domain [FT] | DOMAIN 9..86; /note="BAG 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00369"; DOMAIN 95..167; /note="BAG 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00369"; DOMAIN 182..260; /note="BAG 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00369"; DOMAIN 275..350; /note="BAG 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00369"; DOMAIN 365..442; /note="BAG 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00369" |
| InterPro | IPR039773;IPR036533;IPR003103; |
| Pfam | PF02179; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166170-BAG5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DNAJB1 | Biogrid, Opencell | true |
| DNAJC7 | Biogrid, Opencell | true |
| LRRK1 | Intact, Biogrid | true |
| LRRK2 | Intact, Biogrid | true |
| MAD1L1 | Intact, Biogrid | true |
| AMBRA1 | Biogrid | false |
| BANP | Intact | false |
| CDCA7L | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
