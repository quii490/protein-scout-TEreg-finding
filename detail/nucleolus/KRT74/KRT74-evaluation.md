---
type: protein-evaluation
gene: "KRT74"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## KRT74 (Keratin, type II cytoskeletal 74) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KRT74 |
| 蛋白全称 | Keratin, type II cytoskeletal 74 |
| UniProt ID | Q7RTS7 |
| 蛋白大小 | 529 aa / 58.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 529 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR018039; InterPro:IPR039008; InterPro:IPR032444; InterPro:IPR003054; Pfam:PF00038; Pfam:PF16208 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Has a role in hair formation. Specific component of keratin intermediate filaments in the inner root sheath (IRS) of the hair follicle (Probable)

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR018039 |
| InterPro | IPR039008 |
| InterPro | IPR032444 |
| InterPro | IPR003054 |
| Pfam | PF00038 |
| Pfam | PF16208 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**结构域架构**：KRT74（529 aa, 58.2 kDa, Q7RTS7, Keratin, type II cytoskeletal 74）属于中间丝（Intermediate Filament, IF）蛋白超家族中的II型角蛋白（Type II keratin）。经典角蛋白结构为三域架构：（1）N-terminal head domain（~residues 1-139）——低复杂度区域富含Gly/Ser/Phe/charged residues——含多个phosphorylation sites和interacting motifs；（2）Central alpha-helical rod domain（IPR018039, IPR039008, Pfam PF00038, residues 140-453）——长约315 aa的extended alpha-helix——含coiled-coil formed by heptad repeats（abcdefg pattern, a/d positions为hydrophobic）——由linker L1、L12、L2分割成coil 1A、1B、2A、2B四个subdomains——coil 1A和2B是最保守的区域，包含IF consensus motif（LNDR/LEGE motif）；（3）C-terminal tail domain（~residues 453-529）——较短的non-helical tail。KRT74特异结构域为KRT74-type keratin domain（IPR032444）和Keratin 2 head（Pfam PF16208）。ESMFold/AlphaFold预测pLDDT中等——central rod domain因coiled-coil特征pLDDT 50-75，head/tail domain pLDDT <50。功能注释（PROSITE-ProRule IF rod证据级别ECO:0000255）——在hair follicle inner root sheath (IRS)中作为specific component of keratin intermediate filaments——对毛发形成至关重要。

**PPI互作网络解读**：PPI degree有限。ALK（Anaplastic lymphoma kinase, BioGRID）是receptor tyrosine kinase（RTK）——ALK经fusion proteins（如NPM-ALK, EML4-ALK）在多种肿瘤中驱动oncogenic signaling——KRT74-ALK互作提示KRT74可能作为ALK signaling的scaffold或ALK trafficking的regulator。IQCB1（IQ calmodulin-binding motif containing 1/NPHP5, BioGRID）是primary cilium protein——与CEP290/NPHP6形成complex在ciliary transition zone调控protein entry/exit——KRT74-IQCB1互作暗示keratin在ciliogenesis中的非经典功能。HEXIM1（BioGRID）是P-TEFb（positive transcription elongation factor b）的inhibitor——HEXIM1 binding 7SK snRNA→sequestering CDK9/Cyclin T1（P-TEFb catalytic subunit）→inhibiting RNA Pol II transcription elongation——KRT74-HEXIM1互作将keratin连接至transcription elongation control。LMO4（LIM domain only 4, BioGRID）是transcriptional co-regulator。KRT31/KRT34/KRT37/KRT19（BioGRID）是其他keratin family members——反映keratin超家族内部heterodimerization network——type I（KRT19/31/34/37）和type II（KRT74）keratins以obligate heterodimer形式组装。

**结构解读**：Keratin IF组装遵循层次化机制：（1）type I + type II keratin monomer形成parallel coiled-coil heterodimer（~45 nm长）；（2）两个heterodimer以anti-parallel staggered方式形成tetramer（A11模式或A22模式）——tetramer是可溶性assembly unit；（3）tetramer以head-to-tail和lateral association方式组装成8-tetramer-wide unit-length filament（ULF, ~60 nm长, ~16 nm wide）；（4）ULF经end-to-end annealing和radial compaction形成mature IF（~10 nm diameter, several micrometers long）——整个过程不依赖ATP/GTP hydrolysis，完全由蛋白-蛋白interaction energy驱动。KRT74的head domain中conserved phosphorylation sites（Ser/Thr residues）经PKC, PKA, MAPK, CDK1磷酸化→调控keratin filament disassembly during mitosis和cell migration。Tail domain中的conserved Gly-rich motifs可能参与与KRT74-specific binding partner在IRS中的interaction。

**机制模型**：（1）Hair follicle IRS keratin network——KRT74作为IRS-specific type II keratin与对应type I keratin（可能为KRT25/KRT27/KRT28）形成heterodimeric IF network——在IRS细胞中提供mechanical integrity（抵抗hair shaft movement产生的shear stress）——IRS keratin IF与hair shaft cuticle和companion layer形成interlocking structural framework。（2）Hair loss disorder——KRT74 loss-of-function variants导致alopecia totalis（PMID:40766069）——KRT74 deficiency→IRS keratin IF network failure→IRS structural collapse→hair shaft无法获得mechanical support→hair shaft断裂和脱落→baricitinib（JAK1/2 inhibitor）treatment may indirectly补偿keratin defect通过JAK-STAT signaling的免疫调节作用在hair follicle immune privilege中发挥作用。（3）Wool/cashmere quality（PMID:40941372, PMID:40502394）——KRT74表达水平与羊毛纤维直径和羊绒品质相关——在fine-wool sheep（Gansu Alpine fine-wool sheep）和cashmere goat（Jiangnan/Changthangi pashmina）中KRT74作为毛发品质marker。

**TE调控展望**：KRT74的TE调控关联极其遥远。IF蛋白传统上被视为纯结构蛋白（cytoskeletal mechanical support），但近年研究发现keratins在信号转导中发挥non-mechanical signaling roles——keratin intermediate filament作为signal-responsive scaffold调控kinase activation、apoptosis和cell migration。HEXIM1互作是最有意义的TE相关连接——HEXIM1-P-TEFb（CDK9/Cyclin T1）调控RNA Pol II promoter-proximal pausing和transcription elongation——该过程在TE expression中重要性日益被认识——LINE-1和ERV LTR promoter的Pol II elongation效率受P-TEFb活性影响——KRT74-HEXIM1互作如发生在核内→可能影响P-TEFb availability→间接影响TE transcription elongation。但KRT74主要为胞质keratin（IRS特异），其在nucleoplasm/nucleolus中出现的可能性较低（除非在某些细胞类型中keratin网络重新organize至核周或核内）。作为TrEMBL条目（PubMed=0）的结构蛋白，直接TE调控推测缺乏实验基础。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170484-KRT74

![](https://images.proteinatlas.org/40655/1941_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40655/1941_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40655/1985_A1_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/40655/1985_A1_33_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01391; |
| InterPro | IPR018039;IPR039008;IPR032444;IPR003054; |
| Pfam | PF00038;PF16208; |
| UniProt Domain | DOMAIN 140..453; /note="IF rod"; /evidence="ECO:0000255|PROSITE-ProRule:PRU01188" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ALK | BioGRID | 0 |
| IQCB1 | BioGRID | 0 |
| HEXIM1 | BioGRID | 0 |
| KRT31 | BioGRID | 0 |
| KRT37 | BioGRID | 0 |
| KRT34 | BioGRID | 0 |
| LMO4 | BioGRID | 0 |
| KRT19 | BioGRID | 0 |


### PubMed 文献

**PubMed count: 19**

| 40941372 | Screening of Protein Related to Wool Development and Fineness in Gansu Alpine Fine-Wool Sheep. | Animals (Basel) 2025 |
| 40766069 | Case Report: A novel KRT74 variant in an eight-year-old boy with alopecia totalis successfully treated with baricitinib. | Front Med (Lausanne) 2025 |
| 40502394 | Molecular mechanisms underlying cashmere quality differences between Jiangnan cashmere goats and Changthangi pashmina go | Front Vet Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRT74

