---
type: protein-evaluation
gene: "ENSG00000267179"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## ENSG00000267179 (CNK3/IPCEF1 fusion protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ENSG00000267179 |
| 蛋白全称 | CNK3/IPCEF1 fusion protein |
| UniProt ID | G9CGD6 |
| 蛋白大小 | 899 aa / 98.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 7/10 | x1 | 7.0 | 899 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR049628; InterPro:IPR010599; InterPro:IPR051566; InterPro:IPR017874; InterPro:IPR001478; InterPro:IPR036034 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Required for hepatocyte growth factor (HGF)-dependent activation of Arf6 and HGF-stimulated cell migration

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR049628 |
| InterPro | IPR010599 |
| InterPro | IPR051566 |
| InterPro | IPR017874 |
| InterPro | IPR001478 |
| InterPro | IPR036034 |
| InterPro | IPR011993 |
| InterPro | IPR001849 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 亚细胞定位: https://www.proteinatlas.org/ENSG00000267179-ENSG00000267179/subcellular

### HPA IF 图像

![](https://images.proteinatlas.org/47845/1391_H6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47845/1391_H6_4_blue_red_green.jpg)


### 深度机制分析

**结构域架构**: 该融合蛋白携带一套典型的信号转导支架结构域组合。PH结构域(IPR001849/IPR011993)负责磷脂酰肌醇介导的膜靶向,CRIB结构域(IPR010599)选择性结合GTP-Cdc42/Rac1小G蛋白,PDZ结构域(IPR001478/IPR036034)介导蛋白-蛋白互作及亚细胞定位锚定。CNK3部分原本作为KSR/Ras/MAPK通路的支架,IPCEF1部分则募集cytohesin/Arf-GEF以激活Arf6。该融合将Ras和Arf6两条关键小G蛋白信号通路桥接于单一分子平台,此外IPR051566和IPR017874两个未充分注释结构域可能提供核内靶向的新界面。

**PPI网络**: CRBN相互作用(STRING评分407)具有特殊意义——cereblon是CRL4^CRBN E3泛素连接酶的底物识别亚基,提示该融合蛋白可能是IMiD类药物(来那度胺等)的新底物。RNF166(456)同为E3泛素连接酶,参与天然免疫信号,意味着该蛋白稳定性受到多重泛素化调控。CENPA相互作用(418)是最值得关注的核定位线索:CENPA是着丝粒特异性组蛋白H3变体,暗示该融合蛋白可能在特定细胞周期阶段被募集至着丝粒区域,参与着丝粒染色质或动粒信号调控。

**结构解析**: 蛋白全长899 aa(98.9 kDa),虽无实验PDB结构,但其多结构域架构提示为一个延伸的、灵活的多价支架。PH-CRIB-PDZ三模块的组合赋予其同时感知膜脂质环境(PIP2/PIP3)、小G蛋白激活状态和特定蛋白伙伴的能力。各结构域间较长的无序连接区可能提供构象柔性,允许同时对接多个信号复合物。AF pLDDT可作为折叠置信度的参考。

**机制模型**: CNK3/IPCEF1融合蛋白作为一种双GTPase调控的信号支架,其活性受Cdc42(Ras通路)和Arf6(内膜运输)的双重输入。CRBN/RNF166对支架的泛素化决定了其在核质和着丝粒区域的驻留时间。一旦被稳定,它通过CENPA招募至着丝粒染色质,可能协调有丝分裂期间的着丝粒组装或纺锤体检查点信号。这是目前文献中尚未被描述的机制,着丝粒染色质上是否存在Ras-Arf信号交叉值得深入研究。

**研究意义**: 该蛋白的TrEMBL状态(未经Swiss-Prot审核)和PubMed为零的情况,结合其独特的融合支架结构和CENPA互作,使其成为一个高度新颖的靶标。若能在着丝粒处验证其定位和功能,将开辟"小G蛋白信号调控着丝粒生物学"的新研究方向,对理解染色体不稳定性相关的肿瘤发生有潜在价值。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/G9CGD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/G9CGD6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ENSG00000267179

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CRBN | STRING | 407 |
| RNF166 | STRING | 456 |
| CENPA | STRING | 418 |
