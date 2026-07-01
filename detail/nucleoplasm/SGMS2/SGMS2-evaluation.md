---
type: protein-evaluation
gene: "SGMS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SGMS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SGMS2 |
| 蛋白名称 | Phosphatidylcholine:ceramide cholinephosphotransferase 2 |
| 蛋白大小 | 365 aa / 42.3 kDa |
| UniProt ID | Q8NHU3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Golgi apparatus; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 365 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=44 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=76.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Sphingomyelin_synth-like; Sphingomyelin_synth-like_dom |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=40 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Supported)
- PubMed strict=44 broad=115
- AF pLDDT=76.8 PDB=0
- InterPro: Sphingomyelin_synth-like; Sphingomyelin_synth-like_dom
- Pfam: PAP2_C
- PPI degree=40 ChIP: None
34236445: Early-Onset Osteoporosis. | 37668887: Bone fragility and osteoporosis in children and young adults. | 40158738: Stromal Stiffness-Regulated IGF2BP2 in Pancreatic Cancer Drives Immune Evasion v

### 深度机制分析

SGMS2编码磷脂酰胆碱：神经酰胺胆碱磷酸转移酶2（Sphingomyelin Synthase 2），其结构域架构以鞘磷脂合酶特征性折叠为特征：SAM羧基端跨膜螺旋（跨膜域）和N端催化结构域（IPR045221、IPR025749、Pfam PAP2_C）采用磷酸酯酶/磷酸转移酶折叠，催化两步可逆的磷酸胆碱转移反应。SGMS2与SGMS1在亚细胞分布上互补——SGMS1主要定位于高尔基体（反式高尔基网路），SGMS2主要定位于质膜（PubMed:12869553），但LOC注释同时显示核质定位（Nucleoplasm, Supported可信度）。

365 aa（42.3 kDa）的小型蛋白中容纳了完整的催化结构域和一个跨膜螺旋。AlphaFold pLDDT为76.8，结构域折叠预测可靠，但无实验PDB验证。PPI网络以鞘磷脂生物合成路径为核心：与CERS6（神经酰胺合酶6，960评分）、ASAH1（神经酰胺酶，955评分）、SGPP1（S1P磷酸酶，942评分）、SGMS1（910评分）构成紧密的功能模块。BioGRID数据进一步揭示了与核膜/核骨架蛋白的关联——TMPO（LAP2）、LMNA（核纤层蛋白Lamin A/C）和CENPO（着丝粒蛋白），暗示SGMS2可能在核膜-质膜脂质交通中发挥角色。

TE调控相关性的机制推论围绕核膜脂质环境与染色质组织的交叉：SGMS2通过控制鞘磷脂（SM）与磷脂酰胆碱（PC）的平衡，影响膜脂微域（lipid raft或caveolae）的形成和分布。核膜的内膜富含核纤层蛋白（Lamin）和层相关多肽（LAP），是异染色质（包括含TE的LADs：lamin-associated domains）的锚定位点。若SGMS2的质膜/高尔基体-核质穿梭影响内核膜的脂质组成，其可能间接改变LADs（异染色质锚定区域）的形成和维持，调控TE区域（如LINE-1富含的LADs）的压缩状态。

然而，PCDHGA4核定位证据为Uncertain，TE调控链条过长。PubMed 44篇（严格匹配）赋分8/10新颖性。归一化总分67.8/100，互证+2。若未来获得SGMS2在核膜的明确定位和核膜脂质环境-TAD/LAD可及性关联的直接证据，其脂质调控TE的假说将具有跨领域的新颖性，但现阶段不作为优先靶标。

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Phosphatidylcholine:ceramide cholinephosphotransferase 2

**功能**: Sphingomyelin synthase that primarily contributes to sphingomyelin synthesis and homeostasis at the plasma membrane. Catalyzes the reversible transfer of phosphocholine moiety in sphingomyelin biosynthesis: in the forward reaction transfers phosphocholine head group of phosphatidylcholine (PC) on to ceramide (CER) to form ceramide phosphocholine (sphingomyelin, SM) and diacylglycerol (DAG) as by-product, and in the reverse reaction transfers phosphocholine from SM to DAG to form PC and CER (PubM

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045221 |
| InterPro | IPR025749 |
| Pfam | PF14360 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CERS6 | STRING | 960 |
| ASAH1 | STRING | 955 |
| SGPP1 | STRING | 942 |
| SGMS1 | STRING | 909 |
| TMPO | BioGRID | 1 |
| KIF2C | BioGRID | 1 |
| CENPO | BioGRID | 1 |
| LMNA | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NHU3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SGMS2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164023-SGMS2

![](https://images.proteinatlas.org/15541/2075_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2075_B7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164023-SGMS2

![](https://images.proteinatlas.org/15541/2075_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2075_B7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164023-SGMS2

![](https://images.proteinatlas.org/15541/2075_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2075_B7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/1913_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15541/2049_G1_2_blue_red_green.jpg)

### PubMed

**Count: 115**

| PMID | Title |
|---|---|
| 41877782 | Identification of plasma biomarkers in a PTZ-induced Sudden Unexpected Death-like model through integrated proteomics and metabolomics methods. |
| 41821748 | Pathogenic SGMS2 variants are not a common cause of early-onset osteoporosis among Finnish patients. |
| 41707846 | Ceramide metabolism in oxidative and glycolytic muscle: Significance for lipid-induced insulin resistance. |
| 41517371 | Spectrum of Osteoporosis Etiologies with Associated Vertebral Compression Fractures in Children: Analysis of 11 Cases. |
| 41463320 | Integrative Single-Cell and Machine Learning Analysis Develops a Glutamine Metabolism-Based Prognostic Model and Identifies MSMO1 as a Therapeutic Tar |


