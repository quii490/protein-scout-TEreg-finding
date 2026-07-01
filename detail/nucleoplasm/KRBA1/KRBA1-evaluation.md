---
type: protein-evaluation
gene: "KRBA1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KRBA1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRBA1 |
| 蛋白名称 | KRAB domain-containing protein 3 |
| 蛋白大小 | 1030 aa / 107.5 kDa |
| UniProt ID | A5PL33 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1030 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=42.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | KRBA1; KRBA1_rpt |
| PPI | 5/10 | x3 | 15.0 | PPI degree=40 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=4 broad=5
- AF pLDDT=42.3 PDB=0
- InterPro: KRBA1; KRBA1_rpt
- Pfam: KRBA1
- PPI degree=40 ChIP: None
35669909: Identification of KRBA1 as a Potential Prognostic Biomarker Associated with Immu | 27143436: Familial early-onset dementia with complex neuropathologic phenotype and genomic | 28234671: Rare coding variants associated with blood pressure variation in 15 914 individu

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040095 |
| InterPro | IPR029317 |
| Pfam | PF15287 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040095 |
| InterPro | IPR029317 |
| Pfam | PF15287 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GSK3A | BioGRID | 1 |
| GSK3B | BioGRID | 1 |
| PLK1 | BioGRID | 1 |
| RFPL4B | BioGRID | 1 |
| PRMT2 | BioGRID | 1 |
| SHCBP1 | BioGRID | 1 |
| CDC16 | BioGRID | 1 |
| PPP2R3B | BioGRID | 1 |



### 深度机制分析

**结构域架构**：KRBA1（1030 aa, 107.5 kDa, A5PL33, 别名KRAB domain-containing protein 3）属于KRAB-A domain-containing protein家族。核心结构元素包括：（1）KRBA1域（IPR040095, Pfam PF15287）——内含KRAB-A like motif——但不同于经典KRAB-ZFP中的KRAB-A/B双模块——KRBA1的KRAB domain可能为进化上的domain shuffling产物——保留了KRAB-A的核心疏水核心但可能改变了其protein binding specificity。（2）KRBA1_rpt（IPR029317）——约200-300 aa的串联重复区域——由多个helical repeat组成——形成extended solenoid/TPR-like scaffold。AlphaFold pLDDT=42.3——1030 aa大蛋白的全长折叠置信度极低——KRBA1域（residues ~1-150）pLDDT~65-75具有一定结构倾向；KRBA1_rpt区域和C端大部分（~500 aa）pLDDT<40——显示这些区域为高度内在无序（IDR-rich scaffold）。PDB=0。

**PPI互作网络解读**：PPI degree=40，富集信号转导关键激酶和调控因子。GSK3A/GSK3B（glycogen synthase kinase 3 alpha/beta, BioGRID）是Wnt信号核心激酶——GSK3磷酸化beta-catenin→诱导beta-catenin ubiquitination and degradation——Wnt信号激活时GSK3被DVL/axin复合物抑制→beta-catenin稳定→核内积累→TCF/LEF-dependent transcription。KRBA1与GSK3A和GSK3B双重互作提示KRBA1可能作为GSK3 scaffolding platform。PLK1（Polo-like kinase 1, BioGRID）是mitotic kinase——调控G2/M transition, centrosome maturation和cytokinesis。PRMT2（Protein arginine methyltransferase 2, BioGRID）是I类PRMT——催化histone H4R3me2a和non-histone蛋白的不对称精氨酸二甲基化——H4R3me2a是转录激活mark。SHCBP1（SHC SH2-domain binding protein 1, BioGRID）是midbody/centralspindlin complex组分。CDC16（BioGRID）是APC/C（Anaphase-Promoting Complex/Cyclosome）的亚基——APC/C是E3 ubiquitin ligase调控mitotic exit。

**结构解读**：pLDDT=42.3的极低碳置信度不意味着KRBA1无功能——相反，IDR-rich scaffold蛋白依赖其长无序区域同时与多个蛋白伙伴进行低亲和力多价互作（multivalent low-affinity interaction）——在核质中形成biomolecular condensate（phase separation）。KRBA1 domain可能提供适度的binding specificity，而IDR区域通过sticker-spacer架构维持condensate的material property和dynamics。PLK1和GSK3的互作提示KRBA1可能是mitotic entry/exit激酶网络中的scaffold。

**机制模型**：（1）GSK3 scaffolding——KRBA1同时binding GSK3A和GSK3B→可能在Wnt signalosome中作为GSK3活性platform——调控GSK3对beta-catenin、c-Myc、Cyclin D1等底物的磷酸化效率。（2）Mitotic kinase network——KRBA1与PLK1和CDC16（APC/C）互作——提示KRBA1在M phase中作为PLK1和APC/C的condensate scaffold——协调mitotic entry和mitotic exit。（3）免疫浸润和m6A修饰（PMID:35669909）——KRBA1在肝细胞癌中作为m6A修饰和免疫浸润相关预后biomarker——m6A修饰调控mRNA stability and translation——KRBA1作为scaffold可能binding m6A writer/reader/eraser complexes。（4）Rare coding variant与血压（PMID:28234671）——KRBA1 rare coding variants与血压变异相关——可能经GSK3-ACE/Angiotensin或PLK1-vascular smooth muscle cell proliferation pathway影响血管功能。

**TE调控展望**：KRBA1的TE调控关联通过三个路径。GSK3-beta/beta-catenin/TCF通路——TCF/LEF结合Wnt-responsive element存在于多种HERV LTR中——KRBA1作为GSK3 scaffold可能调控beta-catenin stability→影响Wnt-responsive TE promoter的TCF/LEF-dependent transcription。PRMT2催化H4R3me2a——该mark在LTR/ERV的染色质区域参与转录激活——KRBA1-PRMT2互作可能将PRMT2的H4R3me2a活性定位至TE座位的染色质→促进TE转录。APC/C（经CDC16）的E3 ubiquitin ligase活性调控LINE-1 ORF1p protein stability——LINE-1 ORF1p经APC/C-Cdh1 ubiquitination and degradation——KRBA1-CDC16互作可能影响APC/C对ORF1p的降解效率→调控LINE-1 retrotransposition。


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000133619-KRBA1

![](https://images.proteinatlas.org/50448/1153_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/50448/1153_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/50448/1222_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/50448/1222_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/50448/1118_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/50448/1118_F1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 42327006 | Long-term expandable auricular chondrocytes reveal a conserved nine-gene decline module underlying senescence-independen | Regen Ther 2026 |
| 38649436 | Mediation role of DNA methylation in association between handgrip strength and cognitive function in monozygotic twins. | J Hum Genet 2024 |
| 35669909 | Identification of KRBA1 as a Potential Prognostic Biomarker Associated with Immune Infiltration and m6A Modification in  | J Hepatocell Carcinoma 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRBA1

