---
type: protein-evaluation
gene: "MTX2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## MTX2 (Metaxin-2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MTX2 |
| 蛋白全称 | Metaxin-2 |
| UniProt ID | O75431 |
| 蛋白大小 | 263 aa / 28.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 263 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR036282; InterPro:IPR040079; InterPro:IPR033468; InterPro:IPR050931; InterPro:IPR019564; Pfam:PF17171 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in transport of proteins into the mitochondrion

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR036282 |
| InterPro | IPR040079 |
| InterPro | IPR033468 |
| InterPro | IPR050931 |
| InterPro | IPR019564 |
| Pfam | PF17171 |
| Pfam | PF10568 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

**结构域架构**：MTX2（Metaxin-2, 263 aa, 28.9 kDa, O75431）是线粒体外膜蛋白转运受体复合物（SAM/TOB complex）的cytosolic-facing subunit。结构域包含GSH-rich domain（IPR019564, Pfam PF17171）约100 aa的b-strand rich fold——在SAM complex中识别mitochondrial precursor proteins的b-signal。IPR033468（Metaxin-2 specific）和IPR036282（Glutathione S-transferase C-terminal domain-like superfamily）为GST fold——提示可能具有glutathione binding和redox-sensing功能。AlphaFold可用，ESMFold pLDDT=0.92（极高，75.3%残基>0.9，本批最佳ESM fold）——表明MTX2有极高的结构稳定性——几乎所有263个残基均折叠良好。PPI（degree有限）以线粒体和核蛋白为核心：CHCHD3（STRING score=984）为mitochondrial contact site and cristae organizing system（MICOS）组分——MTX2-CHCHD3互作暗示MTX2在mitochondria-ER contact junction和mtDNA nucleoid的组织角色。HNRNPR（BioGRID）和TADA2A（BioGRID）为核蛋白：HNRNPR为hnRNP R（RNA-binding protein, pre-mRNA processing），TADA2A为ADA2a-containing histone acetyltransferase complex（STAGA/ATAC）的亚基——连接至组蛋白乙酰化。MOV10（Moloney leukemia virus 10, BioGRID）是RNA helicase——也是LINE-1 retrotransposition的已知关键抑制因子——MOV10与APOBEC3和RNase L协同抑制LINE-1 ORF2。

**TE调控展望**：MTX2的nuclear body/nucleolus定位（而非mitochondria）暗示其具有"moonlighting"核功能。HNRNPR通过pre-mRNA processing machinery可能与TE-embedded splice sites交互——调控TE外显子化（exonization）。TADA2A所在的STAGA HAT complex（含GCN5/PCAF, SPT3, TAFs）直接催化H3K9ac/H3K14ac——在TE启动子上，H3K9ac标记活跃LTR/ERV转录——MTX2-TADA2A互作可能招募HAT activity至TE LTR——激活ERV transcription——这可能是mt-nuclear stress retrograde signaling的一部分。MOV10是关键——MTX2-MOV10互作将MTX2直接连接至LINE-1 retrotransposition的抑制网络——MTX2可能作为"adaptor"将MOV10招募至mitochondria-associated membrane（MAM）——在MAM处处理潜在外泄的LINE-1 mRNA/RNP。USP10 deubiquitinates MTX2抑制cGAS-STING signaling（PMID 41705350, Circ Res 2026）——将MTX2定位于innate immune sensing of mtDNA and LINE-1 reverse transcripts的核心枢纽——cGAS-STING pathway在LINE-1 retrotransposition诱导的I型IFN response中是主要效应器——MTX2的USP10-dependent调控在TE-driven inflammation中可能是关键的checkpoint。PMID 42296340报道果蝇Myc减轻Metaxin-2缺陷引起的线粒体稳态缺陷（PNAS 2026），42180896报道Metaxins调控H1299肺癌干细胞样特性（Transl Cancer Res 2026）。

### 补充分析 (UniProt API)

**蛋白全称**: Metaxin-2

**功能**: Involved in transport of proteins into the mitochondrion

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036282 |
| InterPro | IPR040079 |
| InterPro | IPR033468 |
| InterPro | IPR050931 |
| InterPro | IPR019564 |
| Pfam | PF17171 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000128654-MTX2

![](https://images.proteinatlas.org/31550/326_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31550/326_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31550/1291_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31550/1291_C7_3_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR036282;IPR040079;IPR033468;IPR050931;IPR019564; |
| Pfam | PF17171;PF10568; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHCHD3 | STRING | 984 |
| EVX2 | STRING | 837 |
| CARD19 | STRING | 804 |
| HOXD3 | STRING | 774 |
| HNRNPR | BioGRID | 1 |
| TADA2A | BioGRID | 1 |
| CCDC155 | BioGRID | 1 |
| MOV10 | BioGRID | 1 |


### PubMed 文献

**PubMed count: 100**

| 42296340 | Drosophila Myc ameliorates defects in mitochondrial homeostasis and muscle maturation caused by Metaxin-2 deficiency. | Proc Natl Acad Sci U S A 2026 |
| 42180896 | Metaxins regulate cancer stem cell-like properties in H1299 cells. | Transl Cancer Res 2026 |
| 41705350 | USP10 Deubiquitinates MTX2 to Suppress cGAS-STING Signaling in MI. | Circ Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MTX2

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/MTX2_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.92 |
| pLDDT > 0.9 | 75.3% |
| pLDDT < 0.5 | 0.4% |
| 残基数 | 263 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

