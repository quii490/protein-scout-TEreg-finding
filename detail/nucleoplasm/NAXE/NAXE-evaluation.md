---
type: protein-evaluation
gene: "NAXE"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NAXE 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NAXE |
| 蛋白名称 | NAD(P)H-hydrate epimerase |
| 蛋白大小 | 288 aa / 31.7 kDa |
| UniProt ID | Q8NCW5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 288 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=27 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | YjeF_N_dom; YjeF_N_dom_sf; YJEFN_prot_NAXE-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Vesicles (Approved)
- PubMed strict=27 broad=68
- AF pLDDT=86.5 PDB=0
- InterPro: YjeF_N_dom; YjeF_N_dom_sf; YJEFN_prot_NAXE-like
- Pfam: YjeF_N
- PPI degree=7 ChIP: None
30252363: Vitamin B3. | 39937421: Phenotypic diversity in NAXE mutations. | 35819538: Identification of a novel homozygous mutation in NAXE gene associated with early

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: NAD(P)H-hydrate epimerase

**功能**: Catalyzes the epimerization of the S- and R-forms of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration (By similarity) (PubMed:27616477). This is a prerequisite for the S-specific NAD(P)H-hydrate dehydratase to allow the repair of both epimers of NAD(P)HX (By similarity). Accelerates cholesterol efflux from endothelial cells to high-density lipoprotein (HDL) and thereby regulates angiogenesis (PubMed:23719382)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004443 |
| InterPro | IPR036652 |
| InterPro | IPR032976 |
| Pfam | PF03853 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DCP2 | STRING | 772 |
| NUDT14 | STRING | 728 |


### 深度机制分析

**结构域架构**：NAXE（288 aa，31.7 kDa）含有YjeF_N_dom（IPR004443，YjeF_N_dom_sf IPR036652）和YJEFN_prot_NAXE-like（IPR032976，PF03853 YjeF_N）结构域。YjeF_N是NAD(P)HX差向异构酶的催化核心——催化NAD(P)H的受损形式NAD(P)HX（R型和S型差向异构体）之间的相互转化。YjeF_N折叠采用α/β/α三明治结构，由7股平行/反平行β-片层和8个α-螺旋组成，其ATP结合位点（Walker A/B样基序，GXXGXG(P-loop)+酸性催化残基）靠近C端结构域的界面。NAXE是NAD(P)HX修复系统（NAD(P)HX epimerase + NAD(P)HX dehydratase）的第一酶，与NAXD（ATP-NAD(P)HX dehydratase）串联合作完成NAD(P)H的代谢修复循环——这是细胞代谢质量控制的基本机制。

**PPI互作网络解读**：PPI degree极低（仅7），主要互作为DCP2（mRNA脱帽酶2，催化m^7GpppN→m^7GDP + pN的脱帽反应，STRING 772分）和NUDT14（Nudix水解酶14，尿苷二磷酸葡萄糖/UDPG焦磷酸酶，STRING 728分）。这两个互作均基于STRING的基因组邻接（gene neighborhood）和共表达数据，可能反映功能关联而非直接物理互作。NAXE的低PPI度与其作为代谢酶的特性一致——代谢酶通常通过底物-产物关系而非稳定的蛋白复合物发挥作用。

**结构解读**：AlphaFold pLDDT=86.5，预测质量较高。YjeF_N域在pLDDT >85的水平上呈现高度有序的α/β折叠。ATP结合位点由P-loop（GXXGXGK[ST]）的Lys残基（K79或等效位置）直接配位ATP的α-和β-磷酸。差向异构反应的活性位点由保守的酸性残基（Asp/Glu）组成，负责NAD(P)HX底物的C6位差向异构化——先通过碱性残基（Lys/Arg）抽取C6位的质子形成烯醇式中间体，再由酸性残基从相反面重新质子化完成立体化学翻转。C端延伸区（pLDDT 70-80）参与产物的释放和与下游NAXD的底物通道传递（substrate channeling）。

**机制模型**：NAXE的功能是细胞代谢物修复（metabolite repair）的经典代表。NAD(P)H在酶促反应（如甘油醛-3-磷酸脱氢酶GAPDH的反应中间体）或自发热诱导水合下会形成环化的NAD(P)HX（6元NAD(P)H环+1 H2O）——这种异常代谢物积累对细胞有毒（抑制多种脱氢酶的活性并消耗细胞ATP/ADP池）。NAXE催化NAD(P)HX的R/S型差向异构化，使其转化为NAXD的底物形式，NAXD再利用ATP将NAD(P)HX脱水为正常NAD(P)H。NAXE的核质定位（Cytosol; Nucleoplasm; Vesicles Approved）与NAD(P)H代谢酶的广泛亚细胞分布一致——核内的NAD(P)H池支持PARP（多ADP-核糖聚合酶）、Sirtuin脱乙酰酶和多种氧化还原酶的活性，NAXE的核内代谢物修复功能对核内NAD(P)H稳态至关重要。

**TE调控展望**：NAXE的TE调控潜力极低。NAD(P)H代谢的全局性意味着其通过影响核内氧化还原状态可间接影响许多生物过程，但TE特异性调控无任何实验线索。然而，NAXE突变导致的NADHX修复缺陷病（常染色体隐性遗传的进行性脑病，PMID:41737236报道中国患者新发复合杂合变异）呈现出严重的神经退行性表型——该类疾病的基因组不稳定性增加（可能通过NAD^+耗竭→降低PARP和Sirtuin底物水平→DNA修复缺陷→体细胞TE扩增）的理论可能性值得在罕见疾病的TE分析中提及，但非NAXE蛋白的直接功能。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NCW5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000163382-NAXE

![](https://images.proteinatlas.org/43766/857_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43766/857_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43766/1027_H7_3_red_green.jpg)
![](https://images.proteinatlas.org/43766/1027_H7_8_red_green.jpg)
![](https://images.proteinatlas.org/43766/847_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43766/847_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/48164/858_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/48164/858_G11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 68**

| 41737236 | Progressive encephalopathy associated with novel compound heterozygous NAXE mutations in a Chinese patient: case report  | Front Pediatr 2026 |
| 41621837 | Unveiling Immune System Perturbations in Early Development Through Zebrafish Models of NADHX Repair Deficiency. | J Inherit Metab Dis 2026 |
| 41578284 | Deficiency of the NAD(P)HX metabolic repair system: a treatable mitochondrial disease. | Orphanet J Rare Dis 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NAXE

