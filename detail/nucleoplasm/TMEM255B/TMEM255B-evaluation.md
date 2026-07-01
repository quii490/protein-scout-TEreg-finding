---
type: protein-evaluation
gene: "TMEM255B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM255B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM255B |
| 蛋白名称 | Transmembrane protein 255B |
| 蛋白大小 | 326 aa / 34.6 kDa |
| UniProt ID | Q8WV15 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 326 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM255 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=15 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=3 broad=3
- AF pLDDT=70.8 PDB=0
- InterPro: TMEM255
- Pfam: FAM70
- PPI degree=15 ChIP: None
36856181: MUM1L1 as a Tumor Suppressor and Potential Biomarker in Ovarian Cancer: Evidence | 34466146: lncRNA and mRNA sequencing of the left testis in experimental varicocele rats tr | 34288030: Novel insights into immunohistochemical analysis for diagnosing serous neoplasm 

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 255B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028014 |
| Pfam | PF14967 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 255B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028014 |
| Pfam | PF14967 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WWP1 | BioGRID | 1 |
| PLXDC2 | BioGRID | 1 |
| AMZ2 | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |
| TMEM31 | BioGRID | 1 |
| SFT2D1 | BioGRID | 1 |
| CSNK1G2 | BioGRID | 1 |
| PHYHIP | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM255B（326 aa，34.6 kDa）是功能注释极端稀少的跨膜蛋白，仅含TMEM255结构域（IPR028014，PF14967 FAM70）。该结构域家族在进化上保守（后生动物特异），但其三维折叠和分子功能尚未被实验表征。根据疏水性和跨膜预测，TMEM255B含有4-5次预测的跨膜α-螺旋（TM1-TM5），N端位于胞质侧，C端位于胞外/腔面。DUF829超级家族的其他成员（如TMEM53）具有α/β水解酶折叠，但TMEM255B是否享有相同折叠尚不确定——PF14967与PF05705（DUF829）在序列层面上无明显同源性。TMEM255B是目前少数几个在"功能暗物质"区域中的蛋白之一（在UniProt中连"Function"字段都为空）。

**PPI互作网络解读**：PPI degree=15，互作包括：WWP1（WW domain-containing E3 ubiquitin-protein ligase 1，NEDD4家族HECT型E3泛素连接酶，BioGRID 1分——WWP1泛素化降解PTEN、SMAD2/3、KLF5等多种信号蛋白）、HNRNPL（hnRNP L——本批次多个候选蛋白共享的互作伙伴，再次出现，BioGRID 1分）、CSNK1G2（Casein Kinase 1 gamma 2，Wnt/β-catenin通路中CK1磷酸化β-catenin的组分）、AMZ2（Archease domain-containing protein 2，可能在tRNA剪接中发挥作用）、PLXDC2（Plexin domain-containing protein 2，Semaphorin/plexin信号通路受体）。WWP1的互作提示TMEM255B可能受泛素化调控或通过泛素连接酶复合物参与蛋白降解。

**结构解读**：AlphaFold pLDDT=70.8，预测置信度中等。预测的4-5次跨膜α-螺旋在pLDDT 75-85区间，形成紧凑的TM bundle。TM2和TM3之间的胞质loop较长（~60 aa，pLDDT 55-65），可能构成蛋白-蛋白互作界面（例如WWP1的WW域识别富含Pro的PPxY基序）。N端（残基1-30）和C端（残基280-326）均为胞外/腔面暴露，pLDDT偏低（50-65）。结构预测无法提供TMEM255B是否具有酶活性或仅作为膜锚定支架的信息——需要解析实验结构或生化表征才能确定。

**机制模型**：在如此稀疏的信息条件下，TMEM255B的机制模型仅能基于间接证据构建：（1）WWP1的互作暗示TMEM255B可能是WWP1底物——若WWP1识别TMEM255B中的PPxY或类似基序，则泛素化可能调控TMEM255B的蛋白稳定性、内吞/再循环或构象；（2）HNRNPL的互作是TMPRSS5、TMEM255B、SLC16A9等跨膜蛋白共享的共性——HNRNPL作为RNA结合蛋白可能通过"RNA桥接"机制（即HNRNPL结合特定mRNA或lncRNA，后者进一步结合TMEM255B）建立蛋白-RNA-蛋白间接互作网络，而非直接物理结合；（3）TMEM255B在核质中的HPA Approved信号来源不明——若TMEM255B在核膜上表达（如TMEM53），其核质信号可能来自核膜蛋白在IF中的扩散模式。目前仅3篇PubMed文献（均为转录组/蛋白质组关联研究，无功能验证实验）。

**TE调控展望**：TMEM255B的TE调控潜力为不适用（N/A）。该蛋白的功能注释极度不充分——在功能未知的条件下推测其TE调控功能没有科学意义。若未来WWP1-TMEM255B互作被验证且WWP1被证明通过泛素化调控TE区域的组蛋白修饰相关因子（如PTEN→AKT→BRD4通路以间接影响H4K16ac），则TMEM255B可能获得间接联系——但此推测距离实验验证差距遥远。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8WV15-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000184497-TMEM255B

![](https://images.proteinatlas.org/43334/1717_E5_3_cr57f511c8b8cd9_red_green.jpg)
![](https://images.proteinatlas.org/43334/1717_E5_7_cr57f511d229008_red_green.jpg)
![](https://images.proteinatlas.org/43334/1034_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/43334/1034_D11_4_red_green.jpg)
![](https://images.proteinatlas.org/43334/476_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/43334/476_F7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 36856181 | MUM1L1 as a Tumor Suppressor and Potential Biomarker in Ovarian Cancer: Evidence from Bioinformatics Analysis and Basic  | Comb Chem High Throughput Screen 2023 |
| 34466146 | lncRNA and mRNA sequencing of the left testis in experimental varicocele rats treated with Morinda officinalis polysacch | Exp Ther Med 2021 |
| 34288030 | Novel insights into immunohistochemical analysis for diagnosing serous neoplasm of the pancreas: aquaporin 1, stereocili | Histopathology 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM255B

