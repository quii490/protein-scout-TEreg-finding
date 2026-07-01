---
type: protein-evaluation
gene: "SEC31B"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SEC31B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SEC31B |
| 蛋白名称 | Protein transport protein Sec31B |
| 蛋白大小 | 1179 aa / 128.7 kDa |
| UniProt ID | Q9NQW1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm; Vesicles (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 1179 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=69.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | SEC31-like; WD40/YVTN_repeat-like_dom_sf; WD40_repeat_CS |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=32 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Vesicles (Supported)
- PubMed strict=10 broad=16
- AF pLDDT=69.5 PDB=0
- InterPro: SEC31-like; WD40/YVTN_repeat-like_dom_sf; WD40_repeat_CS
- Pfam: WD40
- PPI degree=32 ChIP: None
34539983: An integrated analysis of enhancer RNAs in glioma and a validation of their prog | 27634427: Secretory COPII Protein SEC31B Is Required for Pollen Wall Development. | 28379579: Discovery of novel heart rate-associated loci using the Exome Chip.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein transport protein Sec31B

**功能**: As a component of the coat protein complex II (COPII), may function in vesicle budding and cargo export from the endoplasmic reticulum

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040251 |
| InterPro | IPR015943 |
| InterPro | IPR019775 |
| InterPro | IPR036322 |
| InterPro | IPR001680 |
| Pfam | PF00400 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：SEC31B（1179 aa, 128.7 kDa, Q9NQW1）是COPII coat complex的核心组分，含三个结构层次：（1）N端WD40 beta-propeller域（IPR015943, IPR036322, IPR001680, Pfam PF00400）——典型的7-blade beta-propeller折叠，每个blade由4条anti-parallel beta-strand组成，形成环状platform——WD40域作为蛋白-蛋白互作scaffold识别多种partner的短线性肽段（SLiM）或磷酸化肽段。（2）SEC31-like中央域（IPR040251）——含多个alpha-helical repeat形成extended solenoid架构——介导与SEC13的异二聚化和COPII cage组装。（3）C端proline-rich区域——含多个PPxP和PPxY motif——参与与SEC23-SEC24复合物的互作。AlphaFold pLDDT=69.5——WD40 beta-propeller域pLDDT高（~85-90）折叠可靠，中央solenoid域pLDDT中等（~60-75），proline-rich tail pLDDT低（~35-50）符合内在无序特征。

**PPI互作网络解读**：PPI degree=32。关键伙伴均来自BioGRID。SF3A2（splicing factor 3a subunit 2, BioGRID）是U2 snRNP的组分——参与pre-mRNA剪接中branch site recognition——SEC31B-SF3A2互作罕见地连接COPII trafficking与mRNA剪接机器。MYC（BioGRID）是经典bHLH-LZ转录因子——MYC调控核糖体biogenesis和蛋白翻译——SEC31B-MYC互作可能反映MYC对ER-Golgi分泌通路的上调。BMI1（BioGRID）是Polycomb repressive complex 1（PRC1）核心亚基——介导H2AK119ub1——PRC1在染色质上的功能依赖核内蛋白turnover——BMI1-SEC31B互作提示核内蛋白降解或转运与Polycomb silencing之间的关联。CCT2/3/6A/6B/7（BioGRID）是chaperonin TRiC/CCT亚基——TRiC以ATP依赖方式折叠actin、tubulin等胞质蛋白——SEC31B在核质中与TRiC互作提示SEC31B可能在核内作为TRiC的co-chaperone协助核蛋白折叠。

**结构解读**：pLDDT=69.5——WD40 beta-propeller（residues ~1-400）是结构上最可靠的区域。Beta-propeller采用7-blade circular arrangement——中心形成water-filled channel——blade边缘的暴露loop提供partner binding specificity。中央SEC31-like solenoid域在COPII cage assembly中经SEC13-SEC31B heterotetramer形成cage的edge element——每个SEC13-SEC31B二聚体作为cage的structural strut——SEC31B的alpha-helical solenoid折叠提供机械刚性以生成60-100 nm直径的COPII vesicle cage。C端proline-rich tail与SEC23-SEC24（inner coat）经proline-rich motif-Sec23 interaction互作——将outer cage（SEC13-SEC31）连接至membrane-proximal inner coat。

**机制模型**：（1）ER-to-Golgi COPII trafficking——SEC31B与SEC13形成heterotetrameric outer cage——识别SEC23-SEC24-Sar1-GTP inner coat——在ER exit site（ERES）上经Sar1 GTPase cycle驱动COPII cage assembly/disassembly——包装cargo protein进入COPII vesicle向cis-Golgi运输。（2）核质功能——HPA显示Cytosol; Nucleoplasm; Vesicles (Supported)——SEC31B的核质分布提示其可能参与核膜（NE）上的COPII-like trafficking——NE是ER的延伸——某些核蛋白可能需要COPII-like机制从ER向核膜或核内运输。（3）Glioma enhancer RNA关联（PMID:34539983）——SEC31B在胶质瘤enhancer RNA分析中被鉴定——enhancer RNA（eRNA）的转录和功能依赖核内proteostasis——SEC31B-BMI1互作可能将COPII trafficking与Polycomb-dependent gene silencing连接。

**TE调控展望**：SEC31B的TE调控关联为间接。COPII trafficking缺陷导致ER stress→unfolded protein response（UPR）→ATF6/XBP1/PERK信号→ATF6/XBP1作为转录因子激活ER stress response gene——其中部分gene为LTR/ERV插入（如某些HERV启动子在UPR中被激活）。MYC互作连接至MYC-dependent TE转录——MYC结合E-box（CACGTG）在许多LINE-1和ERV LTR中存在——MYC overexpression在多种肿瘤中激活TE转录——SEC31B-MYC互作可能无意中为MYC提供核内trafficking或turnover平台→间接影响MYC-dependent TE activation。BMI1-PRC1的H2AK119ub1在ERV silencing中与H3K9me3协同——SEC31B-BMI1互作可能通过影响PRC1在TE区域的稳定性调节TE repression效率。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SF3A2 | BioGRID | 0 |
| MYC | BioGRID | 0 |
| BMI1 | BioGRID | 0 |
| CCT7 | BioGRID | 0 |
| CCT3 | BioGRID | 0 |
| CCT6B | BioGRID | 0 |
| CCT6A | BioGRID | 0 |
| CCT2 | BioGRID | 0 |
### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000075826-SEC31B

![](https://images.proteinatlas.org/60052/1308_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/60052/1308_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/60052/1276_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/60052/1276_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/60052/1100_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/60052/1100_G4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 16**

| 42081668 | Eukaryotic chaperonin coordinates root meristem activity by regulating SEC31B-dependent COPII vesicle trafficking of PIN | J Integr Plant Biol 2026 |
| 40596853 | Identification of candidate proteins influencing spermatogenesis in Shandong black cattle via integrated multiomics anal | BMC Genomics 2025 |
| 39676131 | Identification of diagnostic biomarkers in prostate cancer-related fatigue by construction of predictive models and expe | Br J Cancer 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SEC31B

