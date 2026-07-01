---
type: protein-evaluation
gene: "HCRTR2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HCRTR2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HCRTR2 |
| 蛋白名称 | Orexin receptor type 2 |
| 蛋白大小 | 444 aa / 50.7 kDa |
| UniProt ID | O43614 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 444 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=90 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=79.0; PDB=11 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Orexin_rcpt |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=42 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=90 broad=244
- AF pLDDT=79.0 PDB=11
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Orexin_rcpt
- Pfam: 7tm_1; Orexin_rec2
- PPI degree=42 ChIP: None
34052813: Hypocretin/Orexin Receptor Pharmacology and Sleep Phases. | 30917683: Genetics of cluster headache. | 30652302: Analysis of HCRTR2 Gene Variants and Cluster Headache in Sweden.

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Orexin receptor type 2

**功能**: G protein-coupled receptor that binds neuropeptides orexin-A and orexin-B, two neuropeptides derived from a common precursor, prepro-orexin (PubMed:26950369, PubMed:33547286, PubMed:35614071, PubMed:9491897). Upon neuropeptide ligand binding, HCRTR2 can couple with both G(q)/11 and G(i)/o heterotrimeric G proteins thereby initiating distinct downstream signaling cascades (PubMed:35614071). Involved in regulating the sleep-wake cycle (By similarity). Contributes to central regulation of glucose h

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR000204 |
| InterPro | IPR004060 |
| Pfam | PF00001 |
| Pfam | PF03827 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：HCRTR2（444 aa, 50.7 kDa, O43614, Orexin receptor type 2/Hypocretin receptor 2）是class A G蛋白偶联受体（GPCR）家族成员——含7次跨膜（7-TM）alpha-helix bundle（GPCR_Rhodpsn, IPR000276）、特征性DRY motif（TM3胞内侧）、NPxxY motif（TM7）和disulfide bridge（Cys in extracellular loop 1-Cys in extracellular loop 2）。Orexin_rec2域（Pfam PF03827）为OX2R特异性胞外N端域以识别orexin-A和orexin-B配体。AlphaFold pLDDT=79.0, PDB=11——结构可信度极高（与GPCR结构基因组学的大量实验structure解析相关）。7-TM bundle pLDDT>85，胞内和胞外loop pLDDT 65-80。GPCR典型结构：N端胞外→TM1→ICL1→TM2→ECL1→TM3（DRY motif, 含ionic lock）→ICL2→TM4→ECL2→TM5→ICL3（G protein coupling domain）→TM6→ECL3→TM7（NPxxY motif）→C端胞内（含phosphorylation sites for GRK/b-arrestin recruitment）。

**PPI互作网络解读**：PPI degree=42。核心伙伴——GNAI1（STRING 920）和GNAS（STRING 914）——揭示HCRTR2的双重G蛋白偶联：GNAI1是Gai（inhibitory G protein alpha subunit）——激活后抑制adenylyl cyclase（AC）→降低cAMP→关闭PKA信号；GNAS是Gas（stimulatory G protein alpha subunit）——激活后刺激AC→升高cAMP→激活PKA→磷酸化CREB。双G蛋白偶联（promiscuous coupling）使OX2R可根据orexin配体浓度、细胞类型和membrane microdomain环境在不同G蛋白间切换——产生信号多样性。CD274（PD-L1, STRING 788）为免疫检查点蛋白——OX2R-CD274互作连接orexin信号至肿瘤免疫微环境。XPO7（exportin-7, BioGRID, score=1）是核转运受体（nuclear transport receptor, karyopherin-beta family）——可能参与OX2R胞内域的核转位（若经proteolytic cleavage释放胞内域进入核质）。

**结构解读**：OX2R的7-TM orthosteric ligand-binding pocket位于TM bundle外侧——orexin-A（33 aa neuropeptide with two intrachain disulfide bonds, N-terminal pyroglutamate, C-terminal amidation, a-helical structure）和orexin-B（28 aa linear peptide）结合在TM3-TM5-TM6-TM7的胞外部分和ECL2形成的深裂缝中。配体结合诱导TM6和TM7的cytoplasmic end外移（~14 angstrom outward movement of TM6）——暴露G protein binding crevice——允许C-terminal a5 helix of Ga subunit插入。OX2R与OX1R在orexin ligand affinity上不同：OX2R对orexin-A和orexin-B亲和力相当（nonselective），OX1R对orexin-A的亲和力远高于orexin-B——差异由TM2胞外侧和ECL1的序列差异决定。

**机制模型**：（1）睡眠-觉醒周期调控（OX2R的核心功能）——orexinergic neurons in lateral hypothalamus释放orexin-A/B→激活postsynaptic OX2R→Gq/Gs coupling→PLC-beta→IP3→Ca2+ release + DAG→PKC + PKA→CREB phosphorylation→诱导"觉醒"基因（如c-Fos, Arc, BDNF）转录→维持觉醒状态并稳定睡眠-觉醒转换。（2）OX1R/OX2R cross-over（PMID:42323509）——选择性OX2R agonist治疗可增强神经可塑性基因表达和应激韧性（resilience）——提示OX2R>OX1R偏向性信号在情绪调控中的特殊角色。（3）多巴胺神经元调控（PMID:42320783）——OX1R和OX2R在VTA（腹侧被盖区）和SNc（黑质致密部）多巴胺神经元的差异性调控——OX2R激活促进dopamine neuron burst firing（通过Ca2+ and TRPC3/6/7 non-selective cation channel），OX1R影响tonic firing——两者协同控制reward和motor function。（4）Cluster headache遗传学（PMID:30917683, 30652302）——HCRTR2 variants与cluster headache（从集性头痛）的遗传关联——提示orexin信号通过调控trigeminal vascular system和circadian rhythm参与pain processing。

**TE调控展望**：OX2R的TE调控为高度间接，通过GPCR信号通路的多级放大效应延迟反应。Orexin→OX2R→Gas→cAMP↑→PKA→CREB phosphorylation→CREB结合CRE（TGACGTCA）——CRE-like motifs在LINE-1 5'UTR和HERV LTR中存在——OX2R信号可能通过CREB间接激活TE启动子。Gq→Ca2+↑→CaMKIV→CREB phosphorylation是另一条通路。Orexinergic neurons和其靶神经元的OX2R信号可能以昼夜节律/觉醒状态依赖的方式调控TE转录——在觉醒期的神经元中TE活性可能更高（由于更高的cAMP/Ca2+ levels和更活跃的CREB-dependent transcription）——这构成state-dependent TE regulation概念。CD274（PD-L1）互作指向免疫检查点与orexin信号的关联——在肿瘤微环境中，orexin可能通过OX2R-CD274 axis调节抗肿瘤免疫——影响肿瘤细胞中TE（尤其是ERV）的免疫原性——ERV转录产生的dsRNA可激活TLR3/MDA5/RIG-I innate immune sensing→I型IFN→抗肿瘤免疫。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GNAI1 | STRING | 920 |
| GNAS | STRING | 914 |
| CD274 | STRING | 788 |
| XPO7 | BioGRID | 1 |
| FASTKD1 | BioGRID | 1 |
| INTS1 | BioGRID | 1 |
| MYADM | BioGRID | 1 |
| PDS5A | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43614-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137252-HCRTR2

![](https://images.proteinatlas.org/70481/2231_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/70481/2231_G2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 244**

| 42323509 | Selective orexin receptor cross-over treatment increases resilience and expression of neuroplastic signaling genes. | Neuropsychopharmacology 2026 |
| 42320783 | Divergent modulation of dopaminergic neurons by hypocretin/orexin receptors-1 and -2 shapes dopaminergic cell activity a | Biol Psychiatry 2026 |
| 42239891 | Dependence of energy balance and hypothalamic neuropeptide gene expression on initial tumor load in mice. | Front Oncol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/HCRTR2

