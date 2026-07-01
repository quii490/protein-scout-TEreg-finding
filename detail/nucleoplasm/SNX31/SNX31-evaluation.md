---
type: protein-evaluation
gene: "SNX31"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SNX31 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SNX31 |
| 蛋白名称 | Sorting nexin-31 |
| 蛋白大小 | 440 aa / 50.8 kDa |
| UniProt ID | Q8N9S9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 440 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=15 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=84.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PH-like_dom_sf; PX_dom; PX_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=15 broad=23
- AF pLDDT=84.7 PDB=0
- InterPro: PH-like_dom_sf; PX_dom; PX_dom_sf
- Pfam: PX; SNX17-27-31_F1_FERM; SNX17-31_F2_FERM
- PPI degree=7 ChIP: None
22817889: A landscape of driver mutations in melanoma. | 41380477: Identification of genes underlying nigrostriatal iron accumulation: transcriptom | 40609204: MIA and CD163 as promising diagnostic biomarkers in vascular dementia: A multi-m

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sorting nexin-31

**功能**: May be involved in protein trafficking

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011993 |
| InterPro | IPR001683 |
| InterPro | IPR036871 |
| InterPro | IPR048763 |
| InterPro | IPR048767 |
| InterPro | IPR040842 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LZTS2 | BioGRID | 0 |
| RAC1 | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| GOPC | BioGRID | 0 |
| NRBP1 | BioGRID | 0 |
| ATP5A1 | BioGRID | 0 |
| TRIM69 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N9S9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000174226-SNX31

![](https://images.proteinatlas.org/24284/1395_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/24284/1395_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/24284/224_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/24284/224_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/24284/226_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/24284/226_F6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 23**

| 41380477 | Identification of genes underlying nigrostriatal iron accumulation: transcriptome-wide association study of iron-sensiti | EBioMedicine 2026 |
| 40609204 | MIA and CD163 as promising diagnostic biomarkers in vascular dementia: A multi-method study combining WGCNA, machine lea | Int Immunopharmacol 2025 |
| 39932472 | Contact Lens Wear Alters Transcriptional Responses to Pseudomonas aeruginosa in Both the Corneal Epithelium and the Bact | Invest Ophthalmol Vis Sci 2025 |

### 深度机制分析

SNX31属于Sorting Nexin家族，其核心结构域架构由PX结构域（IPR001683）和FERM样结构域（SNX17-27-31_F1_FERM、SNX17-31_F2_FERM）组成，此外还含有一个PH样超家族折叠（IPR011993）。PX结构域负责识别磷脂酰肌醇磷酸（PIPs），引导蛋白定位于富含特定PIPs的内体膜，而FERM样结构域则介导与跨膜货物蛋白以及细胞骨架的相互作用。AlphaFold预测的整体pLDDT为84.7，但在无PDB实验结构验证的情况下，其结构域间相对取向存在不确定性，尤其是PX与FERM区域之间的铰链区域PAE预计较高。

PPI网络分析显示SNX31与LZTS2、RAC1、RNF123、GOPC、NRBP1、ATP5A1及TRIM69等蛋白存在相互作用（BioGRID degree=7，均为低置信度评分0）。其中RAC1为小GTPase，参与肌动蛋白骨架重塑与细胞迁移调控；GOPC为高尔基体相关PDZ蛋白，参与囊泡运输；TRIM69具有E3泛素连接酶活性。这些互作模式提示SNX31可能在内体-高尔基体转运网络中发挥货物分选与运输调控功能。

从调控机制角度，SNX31定位于Cytosol、Golgi apparatus及Nucleoplasm（HPA Approved），其核质定位意味着该蛋白可能通过参与转运含转录因子的内体或直接穿梭入核来间接影响基因表达。PubMed文献提示SNX31与黑色素瘤驱动突变（PMID:22817889）、铁积累相关神经退行性疾病（PMID:41380477）及血管性痴呆生物标志物（PMID:40609204）有关联，但尚无直接TE调控证据。其72.1/100的评分中，新颖性（45.0/50）与核定位特异性（36.0/40）贡献最大，而调控结构域（8.0/20）与三维结构验证（18.0/30）仍是关键短板。

未来研究应通过实验确定SNX31在核质中的具体功能——是通过内体转运间接影响信号通路，还是直接参与核内蛋白复合物的组装。鉴于其PX-FERM双结构域构架，SNX31可能作为一个分子接头，同时结合膜脂质环境和蛋白货物，为TE调控因子提供运输平台。ChIP及RNA-Seq实验将是验证其转录/TE调控功能的关键步骤。PMID:41380477提示的铁代谢通路关联值得进一步深入挖掘。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNX31

