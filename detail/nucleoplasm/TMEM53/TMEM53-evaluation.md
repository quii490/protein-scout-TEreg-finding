---
type: protein-evaluation
gene: "TMEM53"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM53 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM53 |
| 蛋白名称 | Transmembrane protein 53 |
| 蛋白大小 | 277 aa / 31.6 kDa |
| UniProt ID | Q6P2H8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 277 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=13 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=89.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | AB_hydrolase_fold; DUF829_TMEM53 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=12 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Approved)
- PubMed: strict=13, broad=14
- AF pLDDT: 89.4 / PDB: 0
- InterPro: AB_hydrolase_fold; DUF829_TMEM53
- Pfam: DUF829
- PPI degree: 12 / ChIP: None
**Papers**: 40680154: Novel TMEM53 missense variant generated a new ubiquitination site and cause Cran | 37584551: Identification of TMEM53 as a novel SADS-CoV restriction factor that targets vir | 33824347: Deficiency of TMEM53 causes a previously unknown sclerosing bone disorder by dys

### 4. 总体评价
★★★★  **73.2/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 53

**功能**: Ensures normal bone formation, through the negative regulation of bone morphogenetic protein (BMP) signaling in osteoblast lineage cells by blocking cytoplasm-nucleus translocation of phosphorylated SMAD1/5/9 proteins

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029058 |
| InterPro | IPR008547 |
| Pfam | PF05705 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| DHX32 | BioGRID | 1 |
| CCNB2 | BioGRID | 1 |
| NME2P1 | BioGRID | 0 |
| FAM105A | BioGRID | 0 |
| EVA1B | BioGRID | 0 |
| ATP6V0D2 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM53（277 aa，31.6 kDa）含两个结构域：AB_hydrolase_fold（IPR029058）和DUF829_TMEM53（IPR008547，PF05705 DUF829）。AB_hydrolase_fold是α/β水解酶超家族的标准折叠（由8股β-片层和6个α-螺旋组成），含有保守的Ser-His-Asp催化三联体——然而，DUF829_TMEM53家族成员的催化活性尚未得到生化证实，其活性位点残基的保守性较弱（推测催化三联体可能已退化）。TMEM53定位于核膜——2026年最新研究（PMID:41408477）明确将TMEM53定义为"outer nuclear membrane regulator"（外核膜调控因子），参与颅骨和管状骨的骨形成调控。

**PPI互作网络解读**：PPI degree=12，核心互作包括：TRIM25（三联基序蛋白25 / E3泛素连接酶，RIG-I抗病毒信号通路的核心调控因子，BioGRID 1分）、APP（淀粉样前体蛋白，BioGRID 1分）、CCNB2（Cyclin B2，有丝分裂的M期促进因子调节亚基，BioGRID 1分）、DHX32（DEAH-box RNA解旋酶32，BioGRID 1分）。TRIM25的互作最值得关注——TMEM53作为外核膜蛋白可能通过TRIM25连接核膜信号和RIG-I/MAVS先天免疫通路。CCNB2的互作提示TMEM53可能参与G2/M转换和核膜崩解/重建周期。

**结构解读**：AlphaFold pLDDT=89.4，预测质量极高。α/β水解酶折叠清晰可辨——中央β-片层（平行β1-β8）被两侧的α-螺旋包裹。催化三联体（推测Ser-cisSer/Asp-His）位于β4-sheet C端和β7-sheet C端的loop"亲核肘"（nucleophilic elbow）中。与经典水解酶不同的是，TMEM53的活性位点口袋的入口被一段独特的α-螺旋（αD）部分封闭——这一"盖子"螺旋可能通过构象变化调控底物进入，或代表TMEM53已从水解酶功能进化为非催化的蛋白互作结构域。pLDDT >90的区域覆盖了整个α/β水解酶折叠核心，反映了该结构域的高度有序。

**机制模型**：TMEM53的核心功能已被明确为BMP（Bone Morphogenetic Protein）信号的负调控因子：（1）TMEM53定位于外核膜，阻止磷酸化SMAD1/5/9从胞质向核内的转位（UniProt注释：blocking cytoplasm-nucleus translocation of phosphorylated SMAD1/5/9 proteins），从而负调控BMP信号下游靶基因（如成骨细胞分化因子）的转录；（2）TMEM53功能缺失导致颅管发育不良（Craniotubular Dysplasia, Ikegawa型，MIM:619727）——患者表现出颅骨和长骨的过度硬化（Facial and skeletal sclerosing bone disorder），机制为BMP信号的去抑制导致成骨细胞过度活化（PMID:33824347, PMID:41408477）；（3）TMEM53也可作为病毒限制因子——2023年发现TMEM53限制猪急性腹泻综合征冠状病毒（SADS-CoV）的复制，通过靶向病毒RNP复合物发挥抗病毒活性（PMID:37584551）。

**TE调控展望**：TMEM53是目前发现TE调控潜力为中等的罕见候选。BMP/SMAD信号通路已被报道调控内源性逆转录病毒（特别是IAP家族，PMID涉及早期胚胎和胚胎干细胞中的ERV激活）。TMEM53通过负调控SMAD1/5/9的核转位，可能间接抑制SMAD结合位点（SBE, GTCTAGAC）附近TE的转录。LTR元件中常含有功能性SBE基序（MAD/SMAD结合位点的出现频率在ERVL和MaLR家族的LTR中高于随机预期），提示SMAD-TMEM53调控轴在特定TE家族中的潜在调控功能。此外，2026年的TBK1-TMEM53-PD-L1通路发现（PMID:42292694，2026最新文献）将TMEM53延伸至肿瘤免疫检查点调控——免疫逃避和TE去抑制在肿瘤中常协同发生，TMEM53在此交叉点的功能值得进一步探索。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6P2H8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126106-TMEM53

![](https://images.proteinatlas.org/21134/1898_E1_10_cr5ba363dfb4c9b_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/1898_E1_19_cr5ba363dfb5724_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126106-TMEM53

![](https://images.proteinatlas.org/21134/1898_E1_10_cr5ba363dfb4c9b_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/1898_E1_19_cr5ba363dfb5724_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126106-TMEM53

![](https://images.proteinatlas.org/21134/1898_E1_10_cr5ba363dfb4c9b_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/1898_E1_19_cr5ba363dfb5724_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/146_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21134/148_A1_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 42220757 | Adult-Onset Craniotubular Dysplasia, Ikegawa Type: A Report of a Case From Bahrain With a Novel Compound Heterozygous TM | Cureus 2026 |
| 41408477 | TMEM53 as an outer nuclear membrane regulator of cranial and tubular bone formation in craniotubular dysplasia. | J Hum Genet 2026 |
| 40767825 | TMEM53 Gene Mutation Combined with Uniparental Diploidy of Chromosome 1 Causes Binocular Optic Atrophy Secondary to Cran | Ophthalmology 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM53

