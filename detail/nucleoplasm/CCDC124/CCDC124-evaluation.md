---
type: protein-evaluation
gene: "CCDC124"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCDC124 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCDC124 |
| 蛋白名称 | Coiled-coil domain-containing protein 124 |
| 蛋白大小 | 223 aa / 25.8 kDa |
| UniProt ID | Q96CT7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 223 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=14 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=79.9; PDB=6 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ccdc124/Oxs1; Ccdc124/Oxs1_C |
| PPI | 7/10 | x3 | 21.0 | PPI degree=187 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=14, broad=15
- AF pLDDT: 79.9 / PDB: 6
- InterPro: Ccdc124/Oxs1; Ccdc124/Oxs1_C
- Pfam: Ccdc124
- PPI degree=187 / ChIP: None
31893575: FOLFOX treatment response prediction in metastatic or recurrent colorectal cance | 36291090: Nuclear Proteomics of Induced Leukemia Cell Differentiation. | 34369007: Dimerization underlies the aggregation propensity of intrinsically disordered co

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CCDC124（Coiled-coil domain-containing protein 124，又名OXS1）是一个223个氨基酸的保守核糖体结合蛋白，其核心折叠由Ccdc124/Oxs1结构域（IPR010422/PF06244）及Ccdc124/Oxs1_C（IPR054414）C端延伸构成。AlphaFold预测pLDDT为79.9，且已有6个PDB条目——该蛋白与80S核糖体形成的冷冻电镜复合体结构（PMID:32687489）是解析度最高的核糖体-辅助因子相互作用之一。CCDC124的coiled-coil基序介导同源二聚化，形成稳定的反平行二聚体，以非旋转构象（nonrotated conformation）锁定翻译不活跃的核糖体——这是核糖体休眠（ribosome hibernation）的结构基础。

核糖体休眠是细胞在营养缺乏和应激条件下的一种生存策略：CCDC124通过结合80S核糖体的P-stalk区域和40S亚基交界面，阻止翻译延伸因子（eEF2）的结合和核糖体旋转，从而使全局蛋白质合成暂停，同时保护核糖体免遭降解。这一机制与细菌中的核糖体休眠因子（HPF/RaiA）在功能上类似但在结构上完全不同——代表了真核生物中独立进化的核糖体稳态调控策略。

HPA的核质定位虽为nan（无数据，核定位特异性5/10），但蛋白质组学研究（PMID:36291090）在核蛋白质组中明确鉴定了CCDC124——白血病细胞分化过程中的核质蛋白质组变化中CCDC124被鉴定，支持其真实存在于核质。PPI网络（degree=187）几乎全部由核糖体蛋白（RPS5: STRING 924, RPS19: 922, RPL5/11/23A: 918-917）占据——这强烈指向其与非翻译核糖体亚基形成稳定复合体的核心功能，而非独立核活动。RACK1（STRING 916）是值得关注的PPI伙伴——作为核糖体相关信号支架蛋白，连接CCDC124与PKC和Src信号通路。

从TE调控角度，CCDC124通过调控全局翻译影响基因组稳定性的间接模型更具可能性。核糖体休眠缺陷导致翻译质量控制（RQC）失效，可能产生截短蛋白（包括来自TE编码的逆行转录酶ORF2蛋白），进而影响逆转录转座效率。此外，核质蛋白质组中的CCDC124鉴定提示可能存在翻译非依赖的核内功能——例如通过其coiled-coil结构域参与蛋白质相互作用网络。在应激颗粒中，CCDC124与G3BP1共定位（PMID:39009911）——G3BP1是应激颗粒的核心支架蛋白，已知其调控LINE-1逆转录转座，这一观察为CCDC124-TE调控假说提供了间接支持。总体而言，CCDC124的TE调控潜力需要以"核糖体休眠→翻译质量控制→TE蛋白表达调控"的多层间接效应模型来构建。

### 补充分析 (UniProt API)

**蛋白全称**: Coiled-coil domain-containing protein 124

**功能**: Ribosome-binding protein involved in ribosome hibernation: associates with translationally inactive ribosomes and stabilizes the nonrotated conformation of the 80S ribosome, thereby promoting ribosome preservation and storage (PubMed:32687489). Also required for proper progression of late cytokinetic stages (PubMed:23894443)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR010422 |
| InterPro | IPR054414 |
| Pfam | PF06244 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAU | STRING | 952 |
| RPS5 | STRING | 924 |
| RPS19 | STRING | 922 |
| RPL5 | STRING | 918 |
| RPS15 | STRING | 918 |
| RPL23A | STRING | 917 |
| RPL11 | STRING | 917 |
| RACK1 | STRING | 916 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96CT7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCDC124

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000007080-CCDC124

![](https://images.proteinatlas.org/41708/557_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/557_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000007080-CCDC124

![](https://images.proteinatlas.org/41708/557_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/557_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000007080-CCDC124

![](https://images.proteinatlas.org/41708/557_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/557_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/502_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41708/493_H1_2_blue_red_green.jpg)

### PubMed

**Count: 15**

| PMID | Title |
|---|---|
| 41516182 | Detection and Characterization of the Eukaryotic Vacant Ribosome. |
| 41335005 | Spatial Mapping and Interactome Profiling of m(6)A-Modified R-Loops via Chemically Inducible Split-APEX2 Proximity Labeling. |
| 40700276 | Proteomic Profiling Reveals Novel Molecular Insights into Dysregulated Proteins in Established Cases of Rheumatoid Arthritis. |
| 40255396 | Development and validation of a disulfidptosis-related genes signature for predicting outcomes and immunotherapy in acute myeloid leukemia. |
| 39009911 | Live Cell Protein Imaging of Tandem Complemented-GFP11-Tagged Coiled-Coil Domain-Containing Protein-124 Identifies this Factor in G3BP1-Induced Stress |


