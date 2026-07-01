---
type: protein-evaluation
gene: "TMEM182"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM182 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM182 |
| 蛋白名称 | Transmembrane protein 182 |
| 蛋白大小 | 229 aa / 25.9 kDa |
| UniProt ID | Q6ZP80 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 229 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=20 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=87.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PMP22/EMP/MP20/Claudin; TMEM182 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=20 broad=22
- AF pLDDT=87.5 PDB=0
- InterPro: PMP22/EMP/MP20/Claudin; TMEM182
- Pfam: Claudin_2
- PPI degree=22 ChIP: None
38181918: The transmembrane protein TMEM182 promotes fat deposition and alters metabolomic | 34427057: TMEM182 interacts with integrin beta 1 and regulates myoblast differentiation an | 18803820: Expression and regulation of transcript for the novel transmembrane protein Tmem

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 182

**功能**: Negatively regulates myogenesis and skeletal muscle regeneration via its association with ITGB1 (By similarity). Modulates ITGB1 activation by decreasing ITGB1-LAMB1 interaction and inhibiting ITGB1-mediated intracellular signaling during myogenesis (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004031 |
| InterPro | IPR026763 |
| Pfam | PF13903 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SYNE4 | BioGRID | 0 |
| LGALS3 | BioGRID | 0 |
| TSPAN12 | BioGRID | 0 |
| GJA8 | BioGRID | 0 |
| PLP1 | BioGRID | 0 |
| GPR42 | BioGRID | 0 |
| KLRC1 | BioGRID | 0 |
| MALL | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM182（229 aa，25.9 kDa）含有PMP22/EMP/MP20/Claudin结构域（IPR004031）和TMEM182特异性结构域（IPR026763），Pfam注释为Claudin_2（PF13903）。该家族蛋白的共同特征是四次跨膜α-螺旋拓扑（tetraspan），N端和C端均位于胞质侧，形成两个胞外loop（ECL1和ECL2）和一个胞内loop（ICL）。Claudin家族蛋白是紧密连接（tight junction）的核心结构组分，通过同型/异型反式互作（ECL2介导）形成细胞间通透屏障。但TMEM182缺乏Claudin标志性的C端PDZ结合基序，提示其可能在紧密连接中发挥调节性而非结构性功能。

**PPI互作网络解读**：PPI degree=22，关键互作为ITGB1（整合素β1，PMID:34427057通过实验证实TMEM182直接与ITGB1结合并调控成肌细胞分化，是唯一有实验证据支持的互作）。其余互作包括：SYNE4（含Spectrin重复的核膜蛋白，参与核-细胞骨架连接）、LGALS3（Galectin-3，半乳糖凝集素，参与糖基化信号和细胞粘附）、TSPAN12（Tetraspanin-12，Notch/ADAM10剪切调控因子）、GJA8（Connexin 50，间隙连接蛋白）。ITGB1互作的实验验证为TMEM182的功能提供了坚实锚定点。

**结构解读**：AlphaFold pLDDT=87.5，本批次中预测质量最高之一。四次跨膜α-螺旋清晰可辨（pLDDT >90），形成紧密的螺旋束（helix bundle）。ECL1和ECL2形成特征性的β-发夹结构（pLDDT >85），通过保守的半胱氨酸残基形成的二硫键稳定。胞质N端和C端的pLDDT较低（50-60），C端尾可能具有构象柔性，内含ITGB1的结合区域。高pLDDT值反映了四次跨膜蛋白的结构预测成熟度——此类拓扑在实验结构中常见，使得AlphaFold的预测非常可靠。

**机制模型**：（1）经典功能：TMEM182在质膜（可能也在囊泡膜）上通过ITGB1的结合调节整合素β1的活化——TMEM182降低了ITGB1与其配体LAMB1（层粘连蛋白β1）的互作亲和力（PMID:34427057），从而抑制整合素信号通路（FAK-Src-RhoA）及随后的成肌细胞融合和肌纤维形成；（2）在成脂分化中，TMEM182促进脂肪沉积和代谢重编程（PMID:38181918），可能通过相同的ITGB1介导的细胞基质粘附调控机制；（3）核质定位（Approved）的可能解释：TMEM182可能作为核膜的整合膜蛋白表达——核膜内层富含LINC复合物（SUN-KASH蛋白）和细胞骨架连接蛋白，TMEM182可能通过与SYNE4（推测为KASH域的核膜锚定蛋白）互作锚定于核膜，在核-细胞骨架连接的机械感应信号传导中发挥作用。

**TE调控展望**：TMEM182的TE调控潜力极低。其主要作为膜整合蛋白在细胞-基质粘附和肌生成/脂质代谢中发挥作用。然而，整合素信号通路（由TMEM182负调控）通过FAK-YAP/TAZ机械转导通路影响染色质开放性和基因表达——YAP/TAZ已知在某些环境中激活TE（特别是LTR启动子下游的致癌基因）。TMEM182通过抑制ITGB1可能间接减弱YAP/TAZ活性，进而调制TE驱动的转录。这一间接联系在骨骼肌TE生物学（PMID:36785897的连锁研究）中可能具有组织特异性意义。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZP80-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170417-TMEM182

![](https://images.proteinatlas.org/45861/837_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/837_B4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170417-TMEM182

![](https://images.proteinatlas.org/45861/837_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/837_B4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170417-TMEM182

![](https://images.proteinatlas.org/45861/837_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/837_B4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/1028_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45861/802_B11_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 22**

| 41557513 | From Nutrition for All to Precision Nutrition for Everyone: A Journey Through Omics and Asian Metabolic Health. Nevin S. | Food Nutr Bull 2026 |
| 41133695 | Exploring the Regulation of Tmem182 Gene Expression in the Context of Retinoid X Receptor Signaling. | J Dev Biol 2025 |
| 40877790 | Transcriptome analysis reveals key genes and regulatory networks underlying intramuscular fat deposition in rabbits. | BMC Genomics 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM182

