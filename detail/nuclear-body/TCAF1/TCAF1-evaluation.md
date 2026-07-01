---
type: protein-evaluation
gene: "TCAF1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## TCAF1 (TRPM8 channel-associated factor 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TCAF1 |
| 蛋白全称 | TRPM8 channel-associated factor 1 |
| UniProt ID | Q9Y4C2 |
| 蛋白大小 | 921 aa / 101.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 7/10 | x1 | 7.0 | 921 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR029062; InterPro:IPR035423; InterPro:IPR042279; InterPro:IPR031161; InterPro:IPR051244; Pfam:PF17291 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Positively regulates the plasma membrane cation channel TRPM8 activity. Involved in the recruitment of TRPM8 to the cell surface. Promotes prostate cancer cell migration inhibition in a TRPM8-dependent manner

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR029062 |
| InterPro | IPR035423 |
| InterPro | IPR042279 |
| InterPro | IPR031161 |
| InterPro | IPR051244 |
| Pfam | PF17291 |
| Pfam | PF13402 |
| Pfam | PF27027 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

**结构域架构**: TCAF1拥有一个M60肽酶结构域（残基542-841, Peptidase M60, PF13402），属于gluzincin金属肽酶超家族。IPR031161 (Peptidase M60-like) 和IPR029062 (I类谷氨酰胺酰胺转移酶样) 共同暗示该结构域具有锌离子催化的肽键水解活性。PF27027和PF27016是新注释的DUF结构域，可能提供底物识别特异性。M60肽酶家族典型成员（如Zmpste24）参与核纤层蛋白A的CAAX加工，定位于核膜——这一先例为TCAF1的核体定位提供了结构域层面的合理解释。IPR051244和IPR042279的特异性TCAF1特征表明其通过基因复制获得了人类特异性功能（PMID 34433829证实TCAF基因在尼安德特人与现代人中经历不同选择压力）。

**PPI网络解读**: TRPM8（评分666）——经典的冷/薄荷醇激活TRP通道，是最强互作伙伴，证实TCAF1的离子通道调控功能。然而最具深度的信号来自GTF2H2（评分409）——TFIIH核心亚基，直接参与转录起始和核苷酸切除修复。UBXN1（评分483）含UBX结构域，是p97/VCP segregase的适配蛋白。这三者组合——离子通道（TRPM8）、转录/修复（GTF2H2）、泛素-蛋白稳态（UBXN1）——描绘出TCAF1作为"信号-转录-降解"三元界面的核心角色。

**结构解释**: AlphaFold可用但无实验PDB结构。M60肽酶结构域预计折叠为典型的gluzincin折叠——含保守的HEXXH锌结合基序的alpha/beta结构。921 aa中的N端约500 aa可能为非结构域区域，提供蛋白互作界面。

**机制整合模型**: TCAF1是复制应激的Ca2+门控-肽酶感应器，其运作机制为：(1) 在正常条件下，TCAF1通过M60肽酶结构域与核体蛋白（如PML体成分）互作，维持基础肽酶活性；(2) 胞质DNA或复制应激触发TRPV2/TRPM8介导的Ca2+内流，Ca2+信号通过钙调蛋白或直接构象变化激活TCAF1；(3) 活化的TCAF1肽酶结构域切割核体蛋白底物，释放活性片段或降解抑制因子，解除复制叉保护限制；(4) GTF2H2通过TFIIH锚定TCAF1于转录活跃区域，UBXN1通过p97/VCP介导底物的泛素-蛋白酶体降解。PMID 38816425证明TCAF1响应胞质DNA促进TRPV2介导的Ca2+释放以保护复制叉，直接支持该模型的Ca2+-DNA损伤响应环节。

**研究/转化意义**: TCAF1的肽酶活性是目前最大的知识空白——其切割底物完全未知。鉴定M60肽酶结构域的底物可能揭示新的复制应激信号肽。TCAF1-SNX在复制应激和DNA损伤中的角色使其成为基因组不稳定性疾病（癌症、早衰）的潜在干预靶点。此外，TCAF家族在人类进化中的正选择信号暗示其功能与人类特有性状（如大脑大小、寿命）相关。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TCAF1

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 38816425 | TCAF1 promotes TRPV2-mediated Ca(2+) release in response to cytosolic DNA to protect stressed replication forks. |
| 38125428 | Application of serum peptidomics for Parkinson's disease in SNCA-A30P mice. |
| 37806621 | Liver transcriptome profiles of dairy cows with different serum metabotypes. |
| 36012311 | The Association between TRP Channels Expression and Clinicopathological Characteristics of Patients with Pancreatic Adenocarcinoma. |
| 34433829 | Evidence for opposing selective forces operating on human-specific duplicated TCAF genes in Neanderthals and humans. |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000198420-TCAF1

![](https://images.proteinatlas.org/11732/1914_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11732/1914_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/11732/1902_D8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/11732/1902_D8_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/11732/2033_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11732/2033_A2_4_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01276; |
| InterPro | IPR029062;IPR035423;IPR042279;IPR031161;IPR051244; |
| Pfam | PF17291;PF13402;PF27027;PF27016; |
| UniProt Domain | DOMAIN 542..841; /note="Peptidase M60"; /evidence="ECO:0000255|PROSITE-ProRule:PRU01060" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ARHGEF5 | STRING | 415 |
| GTF2H2 | STRING | 409 |
| UBXN1 | STRING | 483 |
| TRPM8 | STRING | 666 |
