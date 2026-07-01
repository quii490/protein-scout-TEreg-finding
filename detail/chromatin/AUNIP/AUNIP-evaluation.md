---
type: protein-evaluation
gene: "AUNIP"
date: 2026-06-03
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## AUNIP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AUNIP / C1orf135 |
| 蛋白全名 | Aurora kinase A- and ninein-interacting protein |
| 蛋白大小 | 357 aa / 40.3 kDa |
| UniProt ID | Q9H7T9 (AUNIP_HUMAN) |
| 功能描述 | DNA-binding protein that accumulates at DNA double-strand breaks (DSBs) following DNA damage and promotes DNA resection and homologous recombination (PubMed:29042561). Serves as a sensor of DNA damage: binds DNA with a strong preference for DNA substrates that mimic structures generated at stalled replication forks, and anchors RBBP8/CtIP to DSB sites to promote DNA end resection and ensuing homol... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | UniProt experimental nuclear + (Nucleus, Chromosome, Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, Cytoplasm, cytoskeleton, spin |
| 蛋白大小 | 10/10 | x1 | 10.0 | 357 aa / 40.3 kDa, 300-800理想区间 |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed strict=10（极低研究量，≤20→10分） |
| 三维结构 | 3/10 | x3 | 9.0 | AF low confidence: mean pLDDT 51.5 |
| 调控结构域 | 7/10 | x2 | 14.0 | Transcription factor (bHLH/ARID/homeobox family) |
| PPI 网络 | 2/10 | x3 | 6.0 | IntAct experiment: 15 partners (1 regulatory: GRB2) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **117/180************ | |
| **归一化总分 (÷1.83)** | | | **63.9/100************ | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Centrosome |
| HPA 额外定位 | 无数据 |
| 抗体可靠性 | Supported |
| IF 图像 | IF images available (6 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 10 |
| symbol_only (Title/Abstract) | 14 |
| broad (all fields) | 25 |

1. PMID 40386627: Guo X, Liu T, Li N (2025 Jun). "AUNIP was a candidate marker for prognosis and immunology in pan-cancer.." *3 Biotech*.
2. PMID 35846349: Zhang S, Li S, Wei Y (2022). "Identification of Potential Antigens for Developing mRNA Vaccine for Immunologically Cold Mesothelioma.." *Frontiers in cell and developmental biology*.
3. PMID 37348876: Makarious MB, Lake J, Pitz V (2023 Nov 2). "Large-scale rare variant burden testing in Parkinson's disease.." *Brain : a journal of neurology*.
4. PMID 29042561: Lou J, Chen H, Han J (2017 Oct 17). "AUNIP/C1orf135 directs DNA double-strand breaks towards the homologous recombination repair pathway.." *Nature communications*.
5. PMID 39148731: Luo D, Wang H, Zeng Z (2024). "Integrated bioinformatics analysis of nucleotide metabolism based molecular subtyping and biomarkers in lung adenocarcinoma.." *Frontiers in immunology*.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AURKA | STRING | 757 |
| DTL | STRING | 739 |
| ELAVL1 | BioGRID | 1 |
| PRMT6 | BioGRID | 1 |
| GRB2 | BioGRID | 1 |
| NIN | BioGRID | 1 |
| PRKAB2 | BioGRID | 1 |
| NXF1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 深度机制分析

AUNIP（Aurora kinase A- and ninein-interacting protein, 357 aa, UniProt Q9H7T9）。定位于Centrosome（HPA Supported），但UniProt和GO注释包含Nucleus/Chromosome——这是DSB修复后DNA末端切除相关的核功能所需。InterPro注释IPR029286（AUNIP domain），Pfam PF15334。AlphaFold pLDDT仅51.5（有序区11.8%），60.8%残基<50，表明该蛋白含大量无序区域。

从DNA损伤修复机制角度，AUNIP是DNA双链断裂（DSB）应答蛋白，在DNA损伤后积累于DSB位点，促进DNA末端切除和同源重组（HR）修复（PMID:29042561）。AUNIP作为DNA损伤传感器——优先结合模拟停滞复制叉结构的DNA底物，并将CtIP（RBBP8）锚定至DSB位点以启动末端切除。STRING互作网络以细胞周期/复制蛋白为主：AURKA（0.757, experimental=0.617，其命名来源）、DTL（0.739）、MCM10（0.674）、UHRF1（0.543）。BioGRID确证AURKA、NIN、ELAVL1、PRMT6等互作。

从TE调控角度，AUNIP与UHRF1（score=0.543）和PRMT6（BioGRID）的潜在关联尤其值得关注。UHRF1是维持DNA甲基化的关键因子——通过识别半甲基化CpG位点招募DNMT1实现复制后DNA甲基化维持。TE区域的DNA甲基化维持高度依赖UHRF1-DNMT1轴。PRMT6催化H3R2me2a修饰抑制H3K4me3，在ERV沉默中发挥作用。若AUNIP通过DSB修复路径与UHRF1/PRMT6交联，其DNA损伤应答可能影响TE区域的表观遗传稳定性——特别是TE重组位点形成的DSB修复过程中。

极度新颖（PubMed=10），但pLDDT极低（51.5）限制了结构导向的功能预测。综合评分63.9/100。建议：γ-H2AX/AUNIP共定位和ChIP检测TE邻近DSB热点处的AUNIP富集。

### 5. AlphaFold 结构预测

| 平均 pLDDT | 51.5 |
| pLDDT >90 | 1.7% |
| pLDDT 70-90 | 10.1% |
| pLDDT 50-70 | 27.5% |
| pLDDT <50 | 60.8% |

**评价**: AlphaFold 预测置信度较低（mean pLDDT 51.5），61% 残基 <50，蛋白可能含有大量无序区域。



### 6. PDB 条目

0 entries found.

### 7. InterPro/Pfam 结构域

| InterPro | IPR029286 | IPR entry IPR029286 |
| Pfam | PF15334 | Pfam entry PF15334 |

**评价**: AUNIP/AURKA 互作蛋白，参与有丝分裂纺锤体组装和DNA损伤应答，与AURKA激酶协同调控细胞周期。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| AURKA | 0.757 | 0.617 | 0.000 | 0.203 |
| DTL | 0.739 | 0.000 | 0.000 | 0.623 |
| MCM10 | 0.674 | 0.000 | 0.000 | 0.136 |
| ERCC6L | 0.653 | 0.000 | 0.000 | 0.476 |
| UHRF1 | 0.543 | 0.000 | 0.000 | 0.441 |
| KIF2C | 0.491 | 0.000 | 0.000 | 0.117 |
| CDCA5 | 0.491 | 0.000 | 0.000 | 0.000 |
| ANLN | 0.489 | 0.000 | 0.000 | 0.395 |
| EXO1 | 0.488 | 0.000 | 0.000 | 0.178 |
| LRRC74B | 0.479 | 0.000 | 0.000 | 0.479 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| TRIM68 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0915"(physical association) |
| NXF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| C14orf119 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| PRKAB2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| AURKA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| GRB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 | psi-mi:"MI:0915"(physical association) |
| PIK3R3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 | psi-mi:"MI:0915"(physical association) |
| PDCD1LG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| GTF3C3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep | psi-mi:"MI:0915"(physical association) |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep | psi-mi:"MI:0915"(physical association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| C14orf119 | 3 |
| DR1 | 3 |
| FGFR3 | 3 |
| GSN | 3 |
| GTF3C3 | 3 |
| HRAS | 3 |
| NXF1 | 3 |
| PRKAB2 | 3 |
| TRIM68 | 2 |
|  | 3 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**核心优势**:
1. 核定位证据较为充分（得分 7/10）
2. 研究新颖性极高：仅 10 篇严格文献，chromatin/epigenetics 方向几乎空白，属于真正的'未被开垦领域'
3. 蛋白大小适中（357 aa），适合重组表达和结构研究

**风险/不确定性**:

**分类**: chromatin
**综合评分**: 64/100

---

**数据来源**: UniProt Q9H7T9, HPA ENSG00000127423, AlphaFold AF-Q9H7T9-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000127423-AUNIP/subcellular

![](https://images.proteinatlas.org/28730/1773_B12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/28730/1773_B12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/28730/273_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28730/273_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28730/274_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28730/274_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H7T9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029286; |
| Pfam | PF15334; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127423-AUNIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AURKA | Biogrid | false |
| C14orf119 | Intact | false |
| DR1 | Intact | false |
| FGFR3 | Intact | false |
| GRB2 | Intact | false |
| GSN | Intact | false |
| GTF3C3 | Intact | false |
| HRAS | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
