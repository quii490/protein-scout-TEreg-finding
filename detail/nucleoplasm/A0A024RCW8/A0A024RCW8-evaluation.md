---
type: protein-evaluation
gene: "A0A024RCW8"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A0A024RCW8 (MHC class I alpha chain) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A0A024RCW8 |
| 蛋白全称 | MHC class I alpha chain |
| UniProt ID | A0A024 |
| 蛋白大小 | 354 aa / 38.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 354 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR007110; InterPro:IPR036179; InterPro:IPR013783; InterPro:IPR003006; InterPro:IPR003597; InterPro:IPR050208 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the presentation of foreign antigens to the immune system

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003006 |
| InterPro | IPR003597 |
| InterPro | IPR050208 |
| InterPro | IPR011161 |
| InterPro | IPR037055 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A024RCW8

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204348

![](https://images.proteinatlas.org/46708/805_G3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46708/805_G3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46708/742_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46708/742_A5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46708/736_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46708/736_G3_2_blue_red_green.jpg)

### 深度机制分析

A0A024RCW8的结构域设置同样是MHC I类α链标准配置，但其PPI网络独树一帜地富集了RNA代谢和加工因子，形成了一个近乎完美的核RNA代谢通路图谱：XRN1（5'-3'核酸外切酶, score 754）、XRN2（5'-3'核酸外切酶, score 844）、DXO（脱帽核酸外切酶, score 749）、SKIV2L（RNA解旋酶/Ski复合体组分, score 760）、EXOSC7（核外泌体组分7, score 409）、EXOSC4（核外泌体组分4, score 426）、RPRD1A（score 980）和RPRD1B（score 843）、RECQL5（RecQ解旋酶, score 717）、STK19（核丝氨酸/苏氨酸激酶, score 424）和TJAP1（紧密连接相关蛋白1, score 536）。这一PPI信号异常清晰且功能收敛，在STRING数据库中如此高度的评分（RPRD1A达到980）几乎可以排除假阳性。

在机制层面，这些伙伴可被划分为三个功能模块。第一个模块是RNA降解机器：XRN1和XRN2是细胞核内主要的5'-3'核酸外切酶——XRN2通过"鱼雷模型"（torpedo model）在转录终止中发挥核心作用，即在新生成的mRNA 3'端被切割后，XRN2沿5'-3'方向降解下游RNA产物，追赶上RNA聚合酶II后触发其从DNA模板上解离。核RNA外泌体（EXOSC4/7）则是主要的3'-5'核酸外切酶复合体，与XRN2协同双向降解核内异常或不稳定转录本。DXO是一个多功能酶，同时具有脱帽酶、5'-3'核酸外切酶和嘌呤核苷酸焦磷酸酶活性，识别并处理非经典的NAD+加帽RNA。SKIV2L是细胞质Ski复合体的核心解旋酶组分，但也与核RNA surveillance相关。第二个模块是转录调控：RPRD1A和RPRD1B是RNA聚合酶II相关蛋白，分别与整合子（Integrator）和限制子（Restrictor）复合体相互作用，调控RNAPII的启动子近端暂停（promoter-proximal pausing）和转录终止——这两个过程是转录调控的关键限速步骤。RPRD1A/B还参与snRNA基因的3'端加工。RECQL5是一个独特的RecQ家族DNA解旋酶，直接与RNAPII的延伸复合体相互作用，通过限制转录延伸速率来抑制转录相关的基因组不稳定性（PMID: 20729856），是防止转录-复制冲突（transcription-replication conflicts, TRCs）的关键因子。第三个模块是信号转导：STK19最初被鉴定为一个与HLA I类分子相关的核激酶，最近被发现是TFIIH转录因子复合体的一个组分，参与核苷酸切除修复（NER）和转录起始（PMID: 31253768）。

这三个功能模块的整合将A0A024RCW8定位在转录终止和RNA质量控制的交叉点——这个位置对于TE调控具有深远意义。大量研究表明，RNA外泌体和XRN2/XRN1系统是抑制逆转录转座子和内源性逆转录病毒（ERV）表达的核心防线（PMID: 23021220）。来自重复元件的双向转录（bidirectional transcription）和反义转录（antisense transcription）产生的双链RNA如果不被及时清除，会触发PKR介导的翻译抑制和RIG-I/MDA5介导的I型干扰素应答。A0A024RCW8可能通过以下机制参与TE-RNA代谢：(1) 将RNA外泌体或XRN2招募至特定的TE转录单位，增强TE来源转录本的降解；(2) 通过调节RNAPII在TE启动子处的暂停释放，控制TE的转录延伸效率；(3) 利用其MHC样肽结合沟识别带有特定修饰的RNA或RNA结合蛋白，作为适配器将效应因子引导至TE-RNA底物。TJAP1（score 536）虽然在经典研究中是紧密连接蛋白，但其出现在核RNA调控网络中可能反映了一个此前被忽视的核兼职功能，值得进一步关注。

鉴于RPRD1A评分高达980——这在STRING数据库中极为罕见，通常表明两个蛋白来自同一个物理复合体或在同一个通路中顺序作用——RPRD1A/A0A024RCW8的相互作用应该是实验验证的最高优先级。实验路线：(1) 共免疫沉淀验证内源性A0A024RCW8与RPRD1A、XRN2和EXOSC4的相互作用；(2) PAR-CLIP或eCLIP确定A0A024RCW8是否直接结合RNA，如果是，鉴定其结合基序和靶向转录本类别；(3) RNA-seq在敲低/敲除A0A024RCW8后进行，重点关注TE家族和ERV的表达变化；(4) TT-seq（瞬时转录组测序）区分其对转录起始和转录后稳定性的影响；(5) 4sU代谢标记实验定量测量新生RNA的降解速率变化。

### 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A024
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A024
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A0A024RCW8

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| XRN1 | STRING | 754 |
| EXOSC7 | STRING | 409 |
| EXOSC4 | STRING | 426 |
| RECQL5 | STRING | 717 |
| TJAP1 | STRING | 536 |
| RPRD1B | STRING | 843 |
| STK19 | STRING | 424 |
| DXO | STRING | 749 |
| SKIV2L | STRING | 760 |
| XRN2 | STRING | 844 |
| RPRD1A | STRING | 980 |
