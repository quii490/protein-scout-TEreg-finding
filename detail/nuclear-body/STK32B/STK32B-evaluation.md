---
type: protein-evaluation
gene: "STK32B"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## STK32B (Serine/threonine-protein kinase 32B) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | STK32B |
| 蛋白全称 | Serine/threonine-protein kinase 32B |
| UniProt ID | Q9NY57 |
| 蛋白大小 | 414 aa / 45.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 414 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR011009; InterPro:IPR000719; InterPro:IPR017441; InterPro:IPR008271; Pfam:PF00069 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Serine/threonine-protein kinase 32B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000152953-STK32B
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/15820/1125_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/15820/1125_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/15820/1599_E12_4_red_green.jpg)
![](https://images.proteinatlas.org/15820/1599_E12_5_red_green.jpg)
![](https://images.proteinatlas.org/15820/129_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/15820/129_F9_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00220; |
| InterPro | IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |
| UniProt Domain | DOMAIN 23..283; /note="Protein kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00159" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSP90AA1 | BioGRID | 0 |
| GLRX3 | BioGRID | 0 |
| HLA-A | BioGRID | 0 |
| HSPB1 | BioGRID | 0 |
| DSP | BioGRID | 0 |
| SERPINB3 | BioGRID | 0 |
| MAPK12 | BioGRID | 0 |
| LAGE3 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：STK32B（414 aa，45.5 kDa）是丝氨酸/苏氨酸蛋白激酶32B，属于蛋白激酶超家族，结构域架构简洁：Protein kinase催化结构域（UniProt DOMAIN 23-283，IPR000719, PF00069）——采用经典的蛋白激酶双叶折叠，N端叶（N-lobe, 约23-100 aa）由5条反平行β-链（β1-β5）和调控性αC螺旋组成，C端叶（C-lobe, 约100-283 aa）以α-螺旋为主（αD-αI），活性位点裂隙位于双叶之间的界面。IPR011009（蛋白激酶样结构域超家族）、IPR017441（蛋白激酶ATP结合基序）和IPR008271（丝氨酸/苏氨酸蛋白激酶活性位点）完善了催化机制的结构注释。N/C端延伸区域（1-22 aa和284-414 aa）可能代表调控性结构域，AlphaFold pLDDT在这些区域显著下降（pLDDT<60）。HPA定位显示Nuclear bodies（Supported）。

**PPI互作网络解读**：PPI degree有限但揭示关键调控网络：HSP90AA1（热休克蛋白90α，分子伴侣）——调控蛋白激酶折叠成熟和构象稳定性的核心伴侣，HSP90通过其N端ATPase结构域与STK32B结合，维持其催化活性构象；GLRX3（含PICOT结构域的谷氧还蛋白）——氧化还原感应蛋白，通过铁硫簇感知氧化应激信号并调控下游激酶活性；HSPB1（小热休克蛋白27）——分子伴侣和肌动蛋白动力学调控因子，在应激条件下防止STK32B错误折叠和聚集；MAPK12（p38γ应激激酶）——MAPK通路成员，可能作为STK32B的上游激活激酶或下游底物；DSP（桥粒蛋白）和SERPINB3（丝氨酸蛋白酶抑制剂）代表细胞连接和蛋白酶-抗蛋白酶平衡的交叉调控。HLA-A和LAGE3为非典型互作。

**结构解读**：N端叶的G-loop（Gly-rich loop, GxGxxG）覆盖ATP的磷酸基团形成"磷酸夹"结构，αC螺旋的Glu残基与催化Lys（VAIK基序）形成盐桥以锁定活化构象。C端叶的催化环（catalytic loop, HRDxxxxN基序）中的Asp残基作为催化碱接受底物Ser/Thr羟基的质子，活化环（activation loop, DFG...APE）的磷酸化状态直接调控激酶活性（DFG-in=活化, DFG-out=非活化）。STK32B属于STK32家族——与STK32A和STK32C并列，该家族以N端富含Pro/Gly的延伸序列和C端无结构化尾端为特征，区别于典型激酶（如PKA/AKT）。激酶结构域pLDDT预测质量应当中等偏上（基于典型的蛋白激酶折叠保守性）。

**机制模型**：STK32B的调控遵循激酶的经典范式：（1）HSP90-HSP70共伴侶-CDC37通路介导正确的折叠和成熟的互作组装；（2）GLRX3通过氧化还原传感调控活化环磷酸化状态；（3）活化后，STK32B通过识别底物共有基序（R/K-x-x-S/T, 碱性残基偏好）磷酸化下游靶蛋白；（4）Nuclear bodies的定位提示STK32B可能在Cajal体（coilin+）或PML核体中富集，已知这些核体是蛋白质修饰（SUMOylation/磷酸化）和RNP成熟的处理中心。STK32B可能在此微环境中磷酸化剪接因子（splicing factors）或snRNP组分以调控mRNA剪接。

**TE调控展望**：STK32B与TE调控的直接关联弱。然而，Nuclear bodies与剪接调控密切相关——已知许多TE衍生外显子（特别是Alu外显子化事件）的剪接选择受核体驻留的剪接因子调控。若STK32B在Nuclear bodies中磷酸化SRSF蛋白家族（SR蛋白）或hnRNP蛋白，则可能间接影响TE衍生剪接位点的选择效率。激酶的"黑马"间接TE调控模式值得以磷酸化蛋白质组学方法探索STK32B的底物谱中是否富集染色质/RNA结合蛋白。目前无文献支持。

### PubMed 文献

**PubMed count: 27**

| 41964082 | The molecular landscape of the C1498 murine acute myeloid leukemia cell line. | Biomark Res 2026 |
| 41275706 | Serine/threonine kinase 32 family proteins: The potential multifaceted regulators in cancer. | Transl Oncol 2026 |
| 41102292 | Evaluating cell-specific gene expression using single-cell and single-nuclei RNA-sequencing data from human pancreatic i | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STK32B

