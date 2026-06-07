---
type: protein-evaluation
gene: "BABAM2"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## BABAM2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BABAM2 / BRCC45, BRE |
| 蛋白全名 | BRISC and BRCA1-A complex member 2 |
| 蛋白大小 | 383 aa / 43.6 kDa |
| UniProt ID | Q9NXR7 (BABAM2_HUMAN) |
| 功能描述 | Component of the BRCA1-A complex, a complex that specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). The BRCA1-A complex also possesses deubiquitinase activity that specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX (PubMed:17525341... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | UniProt experimental nuclear + (Cytoplasm, Nucleus) |
| 蛋白大小 | 10/10 | x1 | 10.0 | 383 aa / 43.6 kDa, 300-800理想区间 |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed strict=6（极低研究量，≤20→10分） |
| 三维结构 | 8/10 | x3 | 24.0 | PDB cryo-EM (4 entries); AF mean pLDDT 92.5 |
| 调控结构域 | 8/10 | x2 | 16.0 | Chromatin-associated regulatory protein |
| PPI 网络 | 3/10 | x3 | 9.0 | IntAct experiment: 15 partners (1 regulatory: CUL1) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **137/180************ | |
| **归一化总分 (÷1.83)** | | | **74.9/100************ | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Cytosol |
| HPA 额外定位 | 无数据 |
| 抗体可靠性 | Supported |
| IF 图像 | IF images available (8 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 6 |
| symbol_only (Title/Abstract) | 11 |
| broad (all fields) | 55 |

1. PMID 35864959: Jin F, Zhu Y, Liu M (2022). "Babam2 negatively regulates osteoclastogenesis by interacting with Hey1 to inhibit Nfatc1 transcription.." *International journal of biological sciences*.
2. PMID 32927585: Ramos H, Bogdanov P, Sampedro J (2020 Sep 10). "Beneficial Effects of Glucagon-Like Peptide-1 (GLP-1) in Diabetes-Induced Retinal Abnormalities: Involvement of Oxidative Stress.." *Antioxidants (Basel, Switzerland)*.
3. PMID 34975328: Yun M, Yingzi L, Jie G (2022). "PPDPF Promotes the Progression and acts as an Antiapoptotic Protein in Non-Small Cell Lung Cancer.." *International journal of biological sciences*.
4. PMID 41349746: Yao X, Liu Y, Kadira HI (2026 Jan). "Identification and evolution analysis of the fos gene family: highlighting the role of fosab in muscle growth of mandarin fish Siniperca chuatsi.." *International journal of biological macromolecules*.
5. PMID 40775720: Yaman Y, Aymaz R, Keleş M (2025 Aug 8). "Investigation of growth traits in Turkish Merino lambs using multi-locus GWAS approaches: Karacabey Merino.." *BMC veterinary research*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 92.5 |
| pLDDT >90 | 76.5% |
| pLDDT 70-90 | 22.2% |
| pLDDT 50-70 | 1.3% |
| pLDDT <50 | 0.0% |

**评价**: AlphaFold 预测整体置信度极高（mean pLDDT 92.5，76% 残基 >90），蛋白折叠预测可靠。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 6H3C | EM | 3.90 A | C/H=1-383 |
| 6R8F | EM | 3.80 A | E/G=1-133 |
| 8PVY | EM | 3.02 A | E/F/K/L=1-383 |
| 8PY2 | EM | 3.32 A | E/F/K/L=1-383 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR010358 | IPR entry IPR010358 |
| Pfam | PF06113 | Pfam entry PF06113 |

**评价**: BRISC complex 亚基，参与去泛素化 (K63-specific)。该复合体与BRCA1-A complex共享多个亚基，在DNA损伤应答和炎症信号中发挥作用。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| BRCC3 | 0.999 | 0.999 | 0.900 | 0.998 |
| ABRAXAS2 | 0.999 | 0.987 | 0.900 | 0.993 |
| BABAM1 | 0.999 | 0.999 | 0.900 | 0.998 |
| BRCA1 | 0.999 | 0.783 | 0.900 | 0.995 |
| ABRAXAS1 | 0.999 | 0.994 | 0.900 | 0.997 |
| BARD1 | 0.999 | 0.334 | 0.900 | 0.995 |
| UIMC1 | 0.999 | 0.994 | 0.900 | 0.997 |
| SHMT2 | 0.998 | 0.983 | 0.900 | 0.192 |
| RAD51 | 0.975 | 0.573 | 0.720 | 0.814 |
| BRCA2 | 0.960 | 0.566 | 0.720 | 0.704 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| BABAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827|mint:MINT-5218676 | psi-mi:"MI:0915"(physical association) |
| ABRAXAS2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| BRCC3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| PHB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| TMX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| MMS19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| RPN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| FKBP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| ATG2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| ABRAXAS2 | 3 |
| BABAM1 | 17 |
| BRCC3 | 4 |
| SMAD4 | 5 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (5/5)

**核心优势**:
1. 核定位证据较为充分（得分 7/10）
2. 研究新颖性极高：仅 6 篇严格文献，chromatin/epigenetics 方向几乎空白，属于真正的'未被开垦领域'
3. 蛋白大小适中（383 aa），适合重组表达和结构研究

**风险/不确定性**:

**分类**: nucleoplasm
**综合评分**: 75/100

---

**数据来源**: UniProt Q9NXR7, HPA ENSG00000158019, AlphaFold AF-Q9NXR7-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000158019-BABAM2/subcellular

![](https://images.proteinatlas.org/17926/143_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17926/143_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17926/144_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17926/144_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17926/145_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17926/145_C2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXR7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010358; |
| Pfam | PF06113; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158019-BABAM2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABRAXAS2 | Intact, Biogrid, Bioplex | true |
| BABAM1 | Intact, Biogrid | true |
| BRCC3 | Intact, Biogrid | true |
| SHMT2 | Biogrid, Bioplex | true |
| ABRAXAS1 | Biogrid | false |
| BARD1 | Biogrid | false |
| BRAF | Intact | false |
| BRCA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
