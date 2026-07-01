---
type: protein-evaluation
gene: "PXDNL"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PXDNL 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PXDNL |
| 蛋白名称 | Probable oxidoreductase PXDNL |
| 蛋白大小 | 1463 aa / 163.7 kDa |
| UniProt ID | A1KZ92 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1463 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=20 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=81.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cys-rich_flank_reg_C; Haem_peroxidase_animal; Haem_peroxidase_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=86 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=20 broad=25
- AF pLDDT=81.4 PDB=0
- InterPro: Cys-rich_flank_reg_C; Haem_peroxidase_animal; Haem_peroxidase_sf
- Pfam: An_peroxidase; I-set; Ig_3
- PPI degree=86 ChIP: None
37688361: A pilot genome-wide association study meta-analysis of gastroparesis. | 40114078: Uncovering drug targets for cluster headache through proteome-wide Mendelian ran | 38034647: Association of body mass index and PXDNL gene variants with acute primary angle 

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Probable oxidoreductase PXDNL

**功能**: Probable oxidoreductase (Probable). Lacks peroxidase activity (PubMed:24253521). Inhibits the peroxidase activity of PXDN through its interaction (PubMed:24253521)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000483 |
| InterPro | IPR019791 |
| InterPro | IPR010255 |
| InterPro | IPR037120 |
| InterPro | IPR007110 |
| InterPro | IPR036179 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CUL3 | BioGRID | 0 |
| CSPP1 | BioGRID | 0 |
| CARM1 | BioGRID | 0 |
| CUTA | BioGRID | 0 |
| SPTAN1 | BioGRID | 0 |
| OSTF1 | BioGRID | 0 |
| PPP1R16B | BioGRID | 0 |
| CSK | BioGRID | 0 |


### 深度机制分析

**结构域架构**：PXDNL/Peroxidasin-like（1463 aa，163.7 kDa）是本批次分子量最大的蛋白。含动物血红素过氧化物酶结构域（Haem_peroxidase_animal IPR010255，Haem_peroxidase_sf IPR037120，Pfam An_peroxidase）——采用α/β折叠，中央血红素（heme b）通过保守的His残基（近端His）和Gln/Asn（远端腔）配位，催化底物（如氯离子、溴离子、硫氰酸根离子）的两电子氧化产生次卤酸（HOCl, HOBr, HOSCN）。Cys-rich_flank_reg_C（IPR000483，富含半胱氨酸的C端侧翼区）提供结构稳定性。Pfam还注释了I-set（免疫球蛋白I-set结构域）和Ig_3（免疫球蛋白样结构域），提示PXDNL的胞外域含多个Ig样结构域串联——类似于过氧化物酶体（Peroxidasin, PXDN）的域架构。

**PPI互作网络解读**：PPI degree=86，核心互作包括：（1）CUL3（Cullin-3——Cullin-RING E3泛素连接酶CRL3的核心骨架蛋白，BioGRID 0分）；（2）CSPP1（Centrosome and spindle pole-associated protein 1，中心体/纺锤体微管组织蛋白，BioGRID 0分）；（3）CARM1（Coactivator-associated arginine methyltransferase 1——催化组蛋白H3R17/H3R26非对称性二甲基化的关键精氨酸甲基转移酶，BioGRID 0分）；（4）SPTAN1（α-II-spectrin，细胞骨架交联蛋白，BioGRID 0分）；（5）OSTF1（Osteoclast stimulating factor 1，破骨细胞刺激因子，BioGRID 0分）。CARM1的互作在此背景下极为重要——CARM1介导的组蛋白精氨酸甲基化（H3R17me2a, H3R26me2a）是染色质的转录激活标志，与H3K4me3和H4ac协同。若PXDNL通过血红素过氧化物酶活性产生活性氧（HOSCN/HOBr等底物氧化产物），局部氧化环境可能调控CARM1的活性或底物可及性。

**结构解读**：AlphaFold pLDDT=81.4，对于1463 aa的超大蛋白而言预测质量良好。过氧化物酶域（约残基700-1050）的pLDDT >88，血红素结合口袋由保守的远端His（推测H826或等效位置）和近端His（推测H918或等效位置）构成。Ig样结构域串联（约8-10个Ig域，残基50-650）预测为线性延伸的"beads-on-a-string"构象——这是过氧化物酶体（PXDN）和血管过氧化物酶（VPO1）等胞外过氧化物酶的特征性架构。Cys-rich区（残基1050-1250）的pLDDT中等（60-75），反映高Cys含量（>8% Cys）导致的二硫键配对多样性和氧化态依赖的构象不均一性。

**机制模型**：PXDNL是过氧化物酶体（PXDN/Peroxidasin）的无活性同源物——实验证据（PMID:24253521）明确指出PXDNL缺乏过氧化物酶活性但通过与PXDN的直接互作抑制PXDN的催化活性。PXDN通过催化次溴酸（HOBr）的生成，在基底膜胶原IV的交联中发挥关键作用——HOBr氧化胶原IV NC1结构域的Met残基，形成共价Sulfilimine键（Met>S=N<Lys/Hyl），交联胶原IV网络。PXDNL通过抑制PXDN负调控这一过程——类似于血管过氧化物酶（VPO1）和甲状腺过氧化物酶（TPO）的双重氧化酶/过氧化物酶体系中的负调控机制。GWAS关联包括：PXDNL基因变异与原发性闭角型青光眼（PMID:38034647）、胃轻瘫（PMID:37688361）和丛集性头痛（PMID:40114078）的易感性。

**TE调控展望**：PXDNL的TE调控潜力极低。PXDNL作为胞外基质交联调控因子，其功能场所（内质网腔→Golgi→胞外基质）与核内TE调控机器存在多重膜屏障的物理区隔。CARM1的互作提供了一个理论上的间接联系——但PXDNL在ER腔面，CARM1在核质中，若无特异性的PXDNL→胞质→核穿梭机制（当前无任何证据支持），此互作可能在标准的BioGRID Y2H实验中为假阳性。PXDNL在基底膜生物学和细胞外基质组装中的角色的重要性局限于细胞外环境。

![PAE](https://alphafold.ebi.ac.uk/files/AF-A1KZ92-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000147485-PXDNL

![](https://images.proteinatlas.org/7919/75_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/7919/75_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/7919/1595_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/7919/1595_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/7919/76_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/7919/76_D6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 25**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PXDNL

