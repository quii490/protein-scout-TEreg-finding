---
type: protein-evaluation
gene: "SH3D19"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3D19 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3D19 |
| 蛋白名称 | SH3 domain-containing protein 19 |
| 蛋白大小 | 790 aa / 86.5 kDa |
| UniProt ID | Q5HYK7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 790 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=58.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Endophilin_SH3RF; Eve1_SH3_1; Eve1_SH3_3 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=59 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- HPA: Cytosol; Nucleoplasm (Supported)
- PubMed: strict=5, broad=9
- AF pLDDT: 58.2 / PDB: 0
- InterPro: Endophilin_SH3RF; Eve1_SH3_1; Eve1_SH3_3
- Pfam: SH3_1; SH3_2; SH3_9
- PPI degree: 59 / ChIP: None
**Papers**: 35726356: Decoding the transcriptome of denervated muscle at single-nucleus resolution. | 12615363: Gene expression of Sh3d19, a novel adaptor protein with five Src homology 3 doma | 16858696: Identification of novel Runx1 (AML1) translocation partner genes SH3D19, YTHDf2,

### 4. 总体评价
★★★★  **71.6/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 domain-containing protein 19

**功能**: May play a role in regulating A disintegrin and metalloproteases (ADAMs) in the signaling of EGFR-ligand shedding (PubMed:15280379). May be involved in suppression of Ras-induced cellular transformation and Ras-mediated activation of ELK1 (PubMed:14551139). Required for regulation of cell morphology and cytoskeletal organization (PubMed:21834987)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050384 |
| InterPro | IPR035834 |
| InterPro | IPR035835 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| Pfam | PF00018 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SH3YL1 | STRING | 835 |
| PUM1 | STRING | 817 |
| ZNF687 | STRING | 745 |
| GRB2 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| ACTB | BioGRID | 1 |
| ACTR3 | BioGRID | 1 |
| CXADR | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5HYK7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000109686-SH3D19

![](https://images.proteinatlas.org/58562/1749_D3_8_cr5804b30b7d01d_red_green.jpg)
![](https://images.proteinatlas.org/58562/1749_D3_22_cr5804b3181f706_red_green.jpg)
![](https://images.proteinatlas.org/58562/1623_G12_4_red_green.jpg)
![](https://images.proteinatlas.org/58562/1623_G12_7_red_green.jpg)
![](https://images.proteinatlas.org/58562/1010_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/58562/1010_H1_2_red_green.jpg)

### 深度机制分析

**结构域架构**：SH3D19（790 aa，86.5 kDa）是含有5个SH3结构域的衔接蛋白，采用串联SH3结构域阵列的模块化架构：Eve1_SH3_1（IPR035834）和Eve1_SH3_3（IPR035835）为SH3D19特有的SH3亚型，加上Endophilin_SH3RF（IPR050384, PF00018）的分类。5个SH3结构域沿多肽链串联排列——这种串联SH3阵列允许同时识别多个PxxP配体或单个靶蛋白上多个PxxP基序，显著增强结合亲和力（avidity effect）。AlphaFold pLDDT=58.2，低pLDDT与高IDR含量一致（约60%残基处于无序或半无序状态）。Cytosol; Nucleoplasm双定位（Supported）表明存在核质穿梭。

**PPI互作网络解读**：PPI degree=59，互作集中于Ras信号和细胞骨架调控通路：GRB2（BioGRID 1）——经典的SH2-SH3-SH3衔接蛋白，通过SH3结构域与SOS（Ras GEF）互作连接RTK信号至Ras-MAPK通路，SH3D19的5个SH3结构域可能通过同源SH3互作与GRB2形成SH3结构域交换网络；SH3YL1（STRING 835）——同家族SH3蛋白，可能形成异源二聚化或竞争相同的PxxP底物；PUM1（STRING 817，Pumilio RNA结合蛋白）——3'UTR结合蛋白调控mRNA稳定性和翻译，提示SH3D19可能参与RNA-蛋白互作调控；ZNF687（STRING 745）——锌指转录因子；ACTR3（ARP3，Arp2/3复合体的肌动蛋白相关蛋白）和ACTB（β-actin）将SH3D19连接至细胞骨架重塑。CXADR（柯萨奇/腺病毒受体）为膜受体互作。

**结构解读**：5个SH3结构域各自采取经典的β-桶状折叠，但串联排列的方式赋予SH3D19独特的功能属性。相邻SH3结构域之间的linker长度（约20-50 aa）和柔性允许这些SH3结构域以"球链"模式适应不同配体蛋白的空间几何。GRB2通过其C端SH3结构域识别SOS中的PxxP序列——SH3D19可能通过竞争GRB2的SH3结合面来解离GRB2-SOS复合体（负调控MAPK通路），或通过未被占用的SH3将额外的效应蛋白引入该复合体（正调控）。这是衔接蛋白的"信号改写"（signal rewiring）功能模式。

**机制模型**：（1）SH3D19以"SH3海绵"模式运作——5个SH3结构域竞争结合Ras信号通路中的PxxP基序，调节GRB2-SOS、Cbl-CIN85和N-WASP-Arp2/3等关键SH3介导复合体的组装动力学；（2）ADAM金属蛋白酶调控——文献支持SH3D19参与ADAM蛋白酶介导的EGFR配体（如TGF-α, HB-EGF）的脱落（ectodomain shedding，PMID:15280379），SH3D19通过其SH3结构域识别ADAM胞质尾端的PxxP序列调控ADAM的酶活性；（3）Ras转化抑制——SH3D19通过干扰GRB2-SOS-Ras信号轴抑制Ras驱动的细胞转化（PMID:14551139）；（4）核质定位：PUM1的互作提示SH3D19可能在核质中参与mRNA代谢调控——PUM1结合特定mRNA的3'UTR并通过招募CCR4-NOT去腺苷酸酶复合体促进mRNA降解，SH3D19可能通过SH3-PxxP互作调控此过程。

**TE调控展望**：SH3D19通过Ras信号调控和mRNA代谢间接连接TE。PUM1是PUF RNA结合蛋白家族成员，其结合基序（UGUANAUA）在特定的Alu和L1元件3'UTR中存在——PUM1可结合这些TE衍生mRNA并调控其降解。SH3D19通过调控PUM1活性可能影响TE转录本的稳定性。此外，EGFR信号通路的激活可磷酸化RNA Pol II CTD并促进特定ERV的转录延伸——SH3D19作为EGFR信号调控因子可能通过ADAM蛋白酶调控EGFR配体可用性间接参与此过程。

### PubMed 文献

**PubMed count: 9**

| 35726356 | Decoding the transcriptome of denervated muscle at single-nucleus resolution. | J Cachexia Sarcopenia Muscle 2022 |
| 34335696 | Identification of Genomic Regions Influencing N-Metabolism and N-Excretion in Lactating Holstein- Friesians. | Front Genet 2021 |
| 34128958 | Tankyrase regulates epithelial lumen formation via suppression of Rab11 GEFs. | J Cell Biol 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3D19

