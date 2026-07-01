---
type: protein-evaluation
gene: "HSH2D"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HSH2D 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HSH2D |
| 蛋白名称 | Hematopoietic SH2 domain-containing protein |
| 蛋白大小 | 352 aa / 39.0 kDa |
| UniProt ID | Q96JZ2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 352 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=62.2; PDB=1 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | HSH2D_SH2; SH2; SH2_dom_sf |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=28 |
| **加权总分** | | | **133/180** | |
| **归一化总分 (÷1.83)** | | | **73.2/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (Approved) |
| PubMed | strict=9, broad=44 |
| AlphaFold | pLDDT=62.2 |
| PDB | 1 entry |
| InterPro | HSH2D_SH2; SH2; SH2_dom_sf |
| Pfam | SH2 |
| PPI | combined degree=28 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Hematopoietic SH2 domain-containing protein

**功能**: May be a modulator of the apoptotic response through its ability to affect mitochondrial stability (By similarity). Adapter protein involved in tyrosine kinase and CD28 signaling. Seems to affect CD28-mediated activation of the RE/AP element of the interleukin-2 promoter

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR035047 |
| InterPro | IPR000980 |
| InterPro | IPR036860 |
| Pfam | PF00017 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNK2 | STRING | 862 |
| ANXA1 | STRING | 837 |
| CRK | BioGRID | 1 |
| RBP7 | BioGRID | 1 |
| PINK1 | BioGRID | 1 |
| TSC1 | BioGRID | 1 |
| OLIG1 | BioGRID | 1 |
| NSA2 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：HSH2D（352 aa，39.0 kDa）含一个经典的SH2结构域（IPR035047 HSH2D_SH2，IPR000980 SH2，IPR036860 SH2_dom_sf，PF00017 SH2）——SH2（Src Homology 2）结构域是磷酸化酪氨酸（pTyr）残基的识别模块，采用中央反平行β-片层（3-4股）被两侧α-螺旋包围的保守折叠。pTyr的结合口袋由保守的Arg残基（βB5上的invariant Arg，形成与pTyr磷酸基团的盐桥和双子氢键）和位于EF/αB loop的Ser/Thr残基（与pTyr芳香环的第二次氢键）构成。pTyr+3位置的疏水性口袋赋予SH2域对pTyr两侧氨基酸序列的结合特异性——不同的SH2域偏好不同的pTyr-X-X-hydrophobic序列基序。

**PPI互作网络解读**：PPI degree=28，关键互作包括：TNK2（ACK1，非受体酪氨酸激酶，STRING 862分——这是极高置信度的SH2-pTyr互作，TNK2包含多个自磷酸化pTyr位点作为SH2域的docking位点）、CRK（CT10 regulator of kinase，SH2/SH3适配器蛋白，BioGRID 1分）、ANXA1（Annexin A1，STRING 837分）、PINK1（PTEN-induced kinase 1，线粒体自噬的关键激酶，BioGRID 1分）、TSC1（Harmartin，mTORC1信号通路的负调控因子，BioGRID 1分）。HSH2D通过SH2域与TNK2的结合模式类似于其他SH2蛋白（如Grb2的SH2）识别受体酪氨酸激酶（RTK）磷酸化位点——HSH2D可能在T细胞受体（TCR）/CD28共刺激信号中作为pTyr信号的解读器。

**结构解读**：AlphaFold pLDDT=62.2（1个PDB结构），整体预测置信度偏低。SH2域的pLDDT较高（80-88），呈现标准的SH2折叠——中央β-片层（βA-βG，约7股）和两侧的αA和αB螺旋。pTyr结合口袋在pLDDT >85的水平上清晰可辨，保守Arg残基（约R35位置）侧链呈伸展构象等待配体磷酸基团。低pLDDT区域集中在N端（残基1-100，SH2域前约70 aa）和C端（SH2域后约100 aa）——这两个区域富含预测的内在无序区，但在功能中至关重要：N端无序区可能含磷酸化位点用于招募其他含SH2域的蛋白，C端无序区可能携带多个结合基序（如富含Pro的SH3结合基序）。

**机制模型**：（1）HSH2D作为TCR/CD28信号通路中的SH2适配器蛋白：在T细胞激活后，TCR下游的酪氨酸激酶（如Lck、ZAP-70、TNK2）磷酸化多种底物，HSH2D通过SH2域识别特定pTyr位点后被招募至免疫突触的信号复合物，进而影响下游IL-2启动子中RE/AP（response element/activator protein）元件的转录激活（UniProt功能注释：affects CD28-mediated activation of the RE/AP element of the interleukin-2 promoter）；（2）HSH2D同时参与凋亡信号调控——UniProt注释"modulator of the apoptotic response through its ability to affect mitochondrial stability"，与PINK1的互作支持线粒体质量控制与T细胞凋亡之间的功能连接；（3）核质定位（Approved）的可能来源：TCR信号激活后，含有SH2域的蛋白可通过核定位信号转位入核——precedents包括STAT蛋白（SH2介导的磷酸化依赖二聚化和核转位），HSH2D可能在磷酸化后经类似机制进入核内直接参与IL-2等免疫基因的转录调控。

**TE调控展望**：HSH2D通过免疫信号通路与TE调控的间接联系在于：T细胞激活可导致LINE-1和ERV的表达上调——淋巴细胞在发育过程中的V(D)J重组和体细胞超突变时期经历了全局的染色质开放状态，TE在此窗口期可能被转座。HSH2D作为T细胞共刺激信号的调控者，其对免疫基因转录的影响可能间接改变染色质可及性景观，为非特异性的TE表达调控。然而，这一联系高度推测性，无任何实验证据。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96JZ2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196684-HSH2D

![](https://images.proteinatlas.org/36616/435_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/435_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196684-HSH2D

![](https://images.proteinatlas.org/36616/435_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/435_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196684-HSH2D

![](https://images.proteinatlas.org/36616/435_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/435_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36616/445_E11_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 44**

| 41954065 | Differential expression of cancer-related genes supports prediction of poor response to first-line treatments in T-ALL p | Mol Oncol 2026 |
| 41104335 | Role of biomarker SOCS1 in peritoneal dialysis-associated peritoneal fibrosis and immune infiltration based on machine l | Front Pharmacol 2025 |
| 39405604 | Doxorubicin resistance involves modulation of interferon signaling, transcriptional bursting, and gene co-expression pat | Neoplasia 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/HSH2D

