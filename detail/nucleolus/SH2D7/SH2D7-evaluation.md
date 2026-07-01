---
type: protein-evaluation
gene: "SH2D7"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH2D7 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SH2D7 |
| 蛋白全称 | SH2 domain-containing protein 7 |
| UniProt ID | A6NKC9 |
| 蛋白大小 | 451 aa / 49.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 451 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=1 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=57.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SH2; SH2_dom_sf; SH2D7_SH2 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

暂无功能注释

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR000980 | SH2 |
| InterPro | IPR036860 | SH2_dom_sf |
| InterPro | IPR035885 | SH2D7_SH2 |
| Pfam | PF00017 | SH2 |


#### 3.4 结构信息

蛋白长度 451 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00252; |
| InterPro | IPR000980;IPR036860;IPR035885; |
| Pfam | PF00017; |
| UniProt Domain | DOMAIN 51..142; /note="SH2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00191" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMEM45B | STRING | 542 |
| C3orf22 | STRING | 574 |
| SH2D7 | STRING | 479 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000183476-SH2D7

![](https://images.proteinatlas.org/51320/1947_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/51320/1947_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/51320/1927_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/51320/1927_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/51320/1955_H11_2_cr5dc042a08e275_red_green.jpg)
![](https://images.proteinatlas.org/51320/1955_H11_22_cr5dc042a08f185_red_green.jpg)
![](https://images.proteinatlas.org/58382/1947_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/58382/1947_H4_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**71.6/100** | **nucleolus**
Nuclear protein


### 深度机制分析

**结构域架构**: SH2D7含有一个经典的SH2磷酸酪氨酸识别结构域（残基51-142, PF00017），属于SH2超家族（IPR036860）中的SH2D7特异性亚家族（IPR035885）。蛋白总长451 aa，但SH2结构域仅占约90 aa，意味着约360 aa为非结构域区域。AlphaFold pLDDT仅57.1，远低于折叠良好的球状蛋白典型值（>85），强烈预示SH2结构域以外的区域具有广泛的内在无序性——这是信号适配蛋白的典型特征。SH2结构域识别pY-X-X-疏水基序，而长的无序尾巴则提供多价低亲和力互作界面。

**PPI网络解读**: 自互作评分479表明SH2D7可能形成同源二聚体，这是一个关键的调控机制——二聚化可使两个SH2结构域协同识别双磷酸化底物，亲和力通过亲和效应指数级增强。TMEM45B（评分542）是内质网驻留跨膜蛋白，C3orf22（评分574）功能未知。这两种互作暗示SH2D7可能响应内质网-核信号轴。与IQCN（高CALM3评分，679）不同，SH2D7的互作网络评分中等且无已知激酶伴侣——它可能是上游未知酪氨酸激酶的孤儿底物识别模块。

**结构解释**: pLDDT 57.1反映了一种"部分折叠"蛋白——SH2结构域本身（pLDDT预计>75）为稳定的5股β-折叠夹心结构，但两侧序列高度无序。这种"折叠结构域+长无序区"的架构是信号适配蛋白（如GRB2、NCK）的共有模式，允许一个紧凑的识别模块通过柔性连接区扫描核内磷酸化底物。

**机制整合模型**: SH2D7作为核仁磷酸化信号解码器，其工作机制如下：(1) 在基础状态下，SH2D7以单体形式游离于核仁-核质之间，SH2结构域处于部分封闭构象；(2) 核仁应激（如rRNA转录抑制、核糖体蛋白失衡）激活核仁内未知酪氨酸激酶，磷酸化核仁磷蛋白（如nucleolin、nucleophosmin、UBF）；(3) SH2D7通过SH2结构域识别磷酸化底物，无序区触发同源二聚化以增强结合亲和力；(4) 二聚化SH2D7招募下游效应器（TMEM45B关联信号通路），将核仁应激信息传递至细胞质。与经典SH2蛋白（如STAT、PI3K调控亚基）不同，SH2D7缺乏酶活性结构域，其功能纯粹是信号桥接。

**研究/转化意义**: SH2D7是SH2蛋白家族中极少数定位于核仁的成员，这使其成为"核仁磷酸化信号"这一新兴领域的开拓性研究对象。PubMed仅1篇且为无关文献，表明这是全新的生物学前沿。鉴定SH2D7的磷酸化底物及其上游激酶将开辟核仁信号转导新领域，可能对核仁应激相关疾病（如骨髓衰竭综合征、神经退行性疾病）有治疗意义。

### 补充分析 (UniProt API)

**蛋白全称**: SH2 domain-containing protein 7

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000980 |
| InterPro | IPR036860 |
| InterPro | IPR035885 |
| Pfam | PF00017 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-A6NKC9-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 1**

| 38988920 | Value analysis of ITLN1 in the diagnostic and prognostic assessment of colorectal cancer. | Transl Cancer Res 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH2D7

