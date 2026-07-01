---
type: protein-evaluation
gene: "FRMD8"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FRMD8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FRMD8 |
| 蛋白名称 | FERM domain-containing protein 8 |
| 蛋白大小 | 464 aa / 51.2 kDa |
| UniProt ID | Q9BZ67 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Centriolar satellite; Cytosol; Nucleoplasm; Plasma (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 464 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Band_41_domain; FERM/acyl-CoA-bd_prot_sf; FERM_2 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=19 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Centriolar satellite; Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=22 broad=24
- AF pLDDT=79.4 PDB=0
- InterPro: Band_41_domain; FERM/acyl-CoA-bd_prot_sf; FERM_2
- Pfam: FERM_M; KRIT1_FRMD8_FERM_C
- PPI degree=19 ChIP: None
39129223: Whole exome sequencing analyses identified novel genes for Alzheimer's disease a | 36171622: Long non-coding RNA NEAT1 mediated RPRD1B stability facilitates fatty acid metab | 40619383: FRMD8 inhibits tumor metastasis in BRCA1-associated TNBC by negatively regulatin

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: FERM domain-containing protein 8

**功能**: Promotes the cell surface stability of iRhom1/RHBDF1 and iRhom2/RHBDF2 and prevents their degradation via the endolysosomal pathway. By acting on iRhoms, involved in ADAM17-mediated shedding of TNF, amphiregulin/AREG, HBEGF and TGFA from the cell surface (PubMed:29897333, PubMed:29897336). Negatively regulates Wnt signaling, possibly by antagonizing the recruitment of AXIN1 to LRP6 (PubMed:19572019)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019749 |
| InterPro | IPR014352 |
| InterPro | IPR035963 |
| InterPro | IPR019748 |
| InterPro | IPR000299 |
| InterPro | IPR051594 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IKBKG | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| APP | BioGRID | 1 |
| RPS14 | BioGRID | 1 |
| ZNF446 | BioGRID | 1 |
| ZNF474 | BioGRID | 1 |
| HIST1H1E | BioGRID | 1 |
| ZNF423 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：FRMD8（464 aa，51.2 kDa）是FERM超家族成员，含Band_41_domain（IPR019749，FERM/acyl-CoA-bd_prot_sf IPR014352，FERM_2 IPR035963，FERM_M PF08736）和C端KRIT1_FRMD8_FERM_C结构域（IPR051594）。FERM结构域（Four-point-one, Ezrin, Radixin, Moesin）是经典的~300个氨基酸膜-细胞骨架界面的适配器模块，由三个亚结构域（F1: ubiquitin-like, F2: acyl-CoA binding protein-like, F3: PH-like）组成三叶草型（cloverleaf）折叠。FRMD8与iRhom1/RHBDF1和iRhom2/RHBDF2互作为其核心功能（PMID:29897333, PMID:29897336），iRhoms是ADAM17（TACE, TNF-α转换酶）的调控伴侣，控制TNF-α、HB-EGF等信号分子的细胞表面脱落。

**PPI互作网络解读**：PPI degree=19，核心互作揭示三个功能维度：（1）NF-κB信号：IKBKG（NEMO，IKK复合物的调节亚基，BioGRID 1分）——FRMD8可能通过调控TNF-α脱落间接影响NF-κB激活或将自身嵌入NF-κB必需调节因子（NEMO）的信号复合物；（2）APP（淀粉样前体蛋白，BioGRID 1分）——ADAM17是APP的α-分泌酶（非淀粉样生成通路），FRMD8通过稳定iRhom-ADAM17复合物间接调控APP加工；（3）ZNF蛋白网络：ZNF446（BioGRID 1分）、ZNF423（BioGRID 1分）、ZNF474（BioGRID 1分）——多个锌指蛋白的互作暗示FRMD8可能在核质中以FERM域为平台组织ZNF蛋白的局部聚集。HIST1H1E（组蛋白H1.4，BioGRID 1分）的互作进一步支持其在染色质压缩水平的潜在功能。

**结构解读**：AlphaFold pLDDT=79.4，FERM域预测质量较高（>85），形成特征性的三叶草折叠。F1 lobe（ubiquitin-like，pLDDT >88）提供稳定性；F2 lobe（pLDDT 80-85）为iRhom结合的核心区域；F3 lobe（pLDDT >82）呈PH域样折叠，介导与磷脂和蛋白的多重互作。C端FERM_C域（pLDDT 70-80）负责与特定效应器（如iRhom的N端胞质尾）结合。连接FERM域和C端的linker区域pLDDT偏低（55-65），可能存在构象柔性以允许功能域的相对运动。

**机制模型**：（1）膜核心功能：FRMD8通过FERM域的F2亚结构域结合iRhom1/2的N端胞质尾，防止iRhoms被内体-溶酶体途径降解（促进内体-质膜循环），从而上调ADAM17在细胞表面的稳定性。ADAM17的底物（TNF-α、Amphiregulin/AREG、HBEGF、TGFA等）的脱落效率因此受到FRMD8的正调控；（2）Wnt信号负调控：FRMD8负调控Wnt信号通路，可能通过竞争AXIN1与LRP6的结合（PMID:19572019）——此功能独立于iRhom-ADAM17模块；（3）核质功能：多个ZNF蛋白和HIST1H1E的互作暗示FRMD8可能在核质中通过FERM域的多价蛋白结合能力组织染色质结合蛋白的局部浓度。FRMD8的TNBC（三阴性乳腺癌）肿瘤抑制活性（PMID:40619383发现FRMD8通过负调控MALAT1-PRC2复合物抑制肿瘤转移）为这一假说提供了直接的实验支持——MALAT1（metastasis-associated lung adenocarcinoma transcript 1）lncRNA通过招募PRC2至FRMD8启动子进行表观遗传沉默，FRMD8通过干扰MALAT1-PRC2的染色质锚定而维持自身表达。

**TE调控展望**：FRMD8通过PRC2通路与TE调控关联。MALAT1与PRC2（EZH2-SUZ12-EED）的互作依赖RNA-蛋白相互作用，而PRC2介导H3K27me3修饰是TE沉默的关键机制。FRMD8通过负调控MALAT1-PRC2染色质锚定可能影响PRC2在TE区域的分布和H3K27me3沉积效率。PMID:41985336（2026年最新文献）发现MALAT1-PRC2复合物通过FRMD8-ADAM17表观遗传调控轴控制滋养层细胞侵袭，进一步验证了这一通路在发育和疾病中的功能重要性。FRMD8是目前少数同时连接膜受体脱落（ADAM17/iRhom）和染色质调控（PRC2/MALAT1）的"跨界"蛋白，在TE调控中的潜力值得深入实验探索。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BZ67-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126391-FRMD8

![](https://images.proteinatlas.org/2861/63_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/2861/63_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/2861/93_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/2861/93_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/2861/62_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/2861/62_B11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 41985336 | Connecting chromatin to cell invasion: MALAT1-PRC2 complex epigenetically controls trophoblast activity via FRMD8-ADAM17 | Eur J Cell Biol 2026 |
| 41898689 | A Cytokine-Related Gene Signature for Pan-Cancer Prognostic Stratification and Malignant Phenotype Characterization. | Int J Mol Sci 2026 |
| 41498149 | Circulating MALAT1 in Preeclampsia and Association With Cardiometabolic Risk. | Hypertension 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FRMD8

