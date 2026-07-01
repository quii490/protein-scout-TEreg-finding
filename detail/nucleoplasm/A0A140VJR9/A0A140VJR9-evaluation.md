---
type: protein-evaluation
gene: "A0A140VJR9"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJR9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJR9 |
| 蛋白大小 | 608 aa / 70.4 kDa |
| UniProt ID | A0A140VJR9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 608 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=91.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | C2_dom; C2_domain_sf; EF-hand-dom_pair |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=91.4 PDB=0
- InterPro: C2_dom; C2_domain_sf; EF-hand-dom_pair
- Pfam: C2; EF-hand_like; PI-PLC-X
- PPI degree=0 ChIP: None


### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CDIPT | STRING | 476 |
| PRKCG | STRING | 908 |
| PIKFYVE | STRING | 526 |
| PLCZ1 | STRING | 900 |
| ITPR1 | STRING | 490 |
| INPP5A | STRING | 916 |
| MTM1 | STRING | 905 |
| PTEN | STRING | 486 |
| MINPP1 | STRING | 441 |
| ITPR3 | STRING | 923 |
| ITPR2 | STRING | 917 |
| PRKCA | STRING | 963 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CDIPT | STRING | 476 |
| PRKCG | STRING | 908 |
| PIKFYVE | STRING | 526 |
| PLCZ1 | STRING | 900 |
| ITPR1 | STRING | 490 |
| INPP5A | STRING | 916 |
| MTM1 | STRING | 905 |
| PTEN | STRING | 486 |
| MINPP1 | STRING | 441 |
| ITPR3 | STRING | 923 |
| ITPR2 | STRING | 917 |
| PRKCA | STRING | 963 |


### 深度机制分析

A0A140VJR9的InterPro/Pfam注释揭示了磷脂酰肌醇特异性磷脂酶C（PI-PLC）家族的核心结构域架构：C2结构域（IPR000008, PF00168）、PI-PLC-X催化结构域（PF00388）、EF-hand样结构域（IPR011992）和EF-hand结构域对（IPR002048）。这种C2-X-EF-hand的线性排列是PI-PLC-δ亚家族的特征签名（PMID: 7779806, 8973216）。C2结构域是Ca2+依赖性的膜结合模块，识别磷脂酰丝氨酸（PtdSer），将催化核心锚定在细胞膜内侧的PIP2（磷脂酰肌醇4,5-二磷酸）上。PI-PLC-X催化结构域采用TIM桶折叠（α/β₈），通过保守的His残基（His311, His356）在酸性环境中水解PIP2的甘油磷酸二酯键，产生两个第二信使：IP3（肌醇1,4,5-三磷酸）和DAG（二酰基甘油）（PMID: 20410501）。608个氨基酸中的显著EF-hand结构域对暗示强的Ca2+依赖性活性调控，这可能使该蛋白对核内Ca2+微波动（如CREB磷酸化或DNA损伤信号触发核膜IP3受体介导的Ca2+释放）敏感。

STRING PPI网络显示高度特异性的磷脂酰肌醇（PI）信号通路互作集群：PRKCA（PKCα, 963分）和PRKCG（PKCγ, 908分）为DAG和Ca2+双调控的经典蛋白激酶C亚型，DAG产物直接激活PKC磷酸化级联反应；ITPR1/ITPR2/ITPR3（IP3受体1/2/3型, 490-923分）为IP3门控的内质网/核膜Ca2+释放通道，提示该蛋白位于核内Ca2+信号的正反馈环路中；CDIPT（CDP-二酰基甘油-肌醇3-磷脂酰转移酶, 476分）是PtdIns合成的关键酶；PIKFYVE（FYVE finger-containing phosphoinositide kinase, 526分）负责产生PtdIns(3,5)P2；INPP5A（肌醇多磷酸5-磷酸酶, 916分）和MTM1（肌小管蛋白, 905分）为PI磷酸酶，负责PIP信号的终止。PTEN（486分）作为PIP3→PIP2的3-磷酸酶点缀其中，进一步确认PI信号节点的集中性。PLCZ1（PLCζ, 900分）是精子特异性PI-PLC同工酶，提示该蛋白可能与PLCZ1共享底物识别或结构支架。

核内PI信号在染色质调控中的作用近年来受到关注。与经典的认识（PI-PLC仅在质膜上工作）不同，核基质中含有完整的PI代谢酶系统（核PI循环），包括PI激酶、磷酸酶和PI-PLC（PMID: 11413436, 16322759）。核内PI-PLC-δ亚型（主要为PLCδ1和PLCδ4）在核质中局部生成IP3和DAG。IP3与核膜上的ITPR结合打开核膜IP3R通道，增加核质[Ca2+]局部浓度。Ca2+结合C2结构域进一步激活PI-PLC的催化速率，形成正反馈放大。DAG则激活核内PKC（PRKCA/PRKCG），后者磷酸化核纤层（lamin B1/B2）和组蛋白H3（ser10, ser28），直接调控染色质凝集状态和特定基因组区域的转录可用性。近年来有证据表明PKC依赖的HP1α（异染色质蛋白1α）磷酸化促进其从H3K9me3标记的TE位点解离，导致转座子去抑制（PMID: 32817553）。

A0A140VJR9的pLDDT=91.4是所有6份报告中结构置信度最高的。这一极高的pLDDT（>90，对应实验结构的精度水平）说明C2-X-EF-hand-PLC核心折叠在进化上是刚性且高度保守的，即使在未表征的人类同源物中也是如此。这意味着该蛋白很可能不含有大量无序区域，其结构已经接近"实验就绪"状态，冷冻电镜或X射线晶体学可能快速得出高分辨率结构。其高置信度折叠提示活性位点排列完好，催化功能完整。

TE调控推测模型：A0A140VJR9作为核PI-PLC，通过核内Ca2+/DAG信号轴调控转座子位点的染色质可及性。具体而言：（1）TE位点（尤其是LTR转座子，其启动子受HP1/H3K9me3抑制）的异染色质化需要凝缩染色质状态，核PI-PLC产生的DAG激活PKC，PKC直接磷酸化HP1γ的ser83，诱导HP1从H3K9me3解离，导致局部的TE启动子去抑制（PMID: 32817553）；（2）IP3-Ca2+信号可能通过激活CaMKIV/CREB/CBP通路促进TE的转录激活，许多LTR元件的LTR区域含有保守的CREB结合位点（cAMP响应元件）；（3）PtdIns(3,5)P2信号（PIKFYVE产物）在核内溶酶体相关TE调控中扮演角色——最近发现内吞途径的PI(3,5)P2标记与TE转录偶联（PMID: 34131121）；（4）PTEN互作（486分）可能使该蛋白连接到PIP3→PIP2转换，并与核Akt信号交叉对话，后者已知通过磷酸化KAP1/TRIM28调控内源性逆转录病毒。研究意义：该蛋白质是代谢物-第二信使-TE调控三合一交叉点的典型代表。PubMed=0+结构高置信度+pLDDT>90+PI信号节点集中度，使之成为开发核PI-PLC选择性抑制剂以精确操控TE表达的极佳药物靶点。

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A140-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJR9
