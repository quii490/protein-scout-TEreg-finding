---
type: protein-evaluation
gene: "A0A140VJC8"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJC8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJC8 |
| 蛋白大小 | 770 aa / 86.9 kDa |
| UniProt ID | A0A140VJC8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 770 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=64.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Amyloid_Cu-bd_sf; Amyloid_glyco; Amyloid_glyco_Abeta |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **114/180** | |
| **归一化总分** | | | **63.4/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=64.3 PDB=0
- InterPro: Amyloid_Cu-bd_sf; Amyloid_glyco; Amyloid_glyco_Abeta
- Pfam: APP_amyloid; APP_Cu_bd; APP_E2
- PPI degree=0 ChIP: None


### 4. 总体评价
**63.4/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APOE | STRING | 623 |
| SORL1 | STRING | 430 |
| APBA1 | STRING | 766 |
| IDE | STRING | 404 |
| APP | STRING | 995 |
| NCSTN | STRING | 535 |
| TNFRSF21 | STRING | 608 |
| CLU | STRING | 538 |
| BACE1 | STRING | 465 |
| PSEN1 | STRING | 437 |
| MAPT | STRING | 592 |
| NAE1 | STRING | 423 |
| APBB2 | STRING | 828 |
| APBA2 | STRING | 811 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000142192

![](https://images.proteinatlas.org/1462/60_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1462/60_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1462/61_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1462/61_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1462/59_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1462/59_E2_2_blue_red_green.jpg)

### 深度机制分析

A0A140VJC8通过InterPro和Pfam注释确定为APP（Amyloid Precursor Protein）家族的同源成员，携带三个经典结构域：APP_amyloid（PF03494, IPR013803）、APP_Cu_bd（PF12954, IPR008155）和APP_E2（PF12925, IPR024329）。这种三结构域架构与APP的核心A-beta生成模块完全平行：铜结合结构域（APP_Cu_bd）通过His残基配位Cu(I)/Cu(II)，参与氧化还原构象调控（PMID: 10364178）；E2结构域形成刚性的反平行β桶折叠，作为蛋白二聚化和肝素结合的平台（PMID: 15992498）；淀粉样蛋白结构域（包含A-beta序列）被认为在稳定核蛋白复合体和核酸结合方面发挥作用（PMID: 22238675）。770个氨基酸长度与APP亚型APP751/APP770接近，提示该蛋白质保留了全长APP的模块化结构。

STRING网络以APP（995分，理论上限）为中心，揭示了完整的A-beta代谢信号轴：BACE1（465分）和PSEN1（437分）为核心A-beta生成酶（β-分泌酶和γ-分泌酶复合体催化亚基），APOE（623分）和CLU（538分）为A-beta清除伴侣蛋白（PMID: 19188678, 34623116），MAPT（592分）连接至下游tau病理（PMID: 34396550），NCSTN（535分）为γ-分泌酶复合体的关键支架亚基（PMID: 12763021）。更值得关注的是APBA1/Mint1（766分）、APBA2/Mint2（811分）和APBB2/FE65L1（828分）三者，均为含PTB结构域的分子适配器，介导APP胞内域（AICD）进入细胞核后的转录共激活功能（PMID: 16730330, 20711427）。

APP的核定位已有充分文献支持。APP CTF50片段通过内吞途径逆向运输至细胞核，与Tip60组蛋白乙酰转移酶和FE65形成三聚转录激活复合体，调控包括KAI1、GSK-3β和neprilysin在内的靶基因（PMID: 12861068, 18923552）。A-beta本身也在细胞核中被检测到，与Lamin B和DNA损伤焦点共定位（PMID: 29455900）。核APP信号被认为在DNA损伤应答和细胞周期调控中发挥作用。A0A140VJC8作为APP同源物，其APP_Cu_bd结构域的氧化还原敏感性可能在核质内感知活性氧水平，而APP_E2结构域可能协助染色质关联。

A0A140VJC8的pLDDT=64.3接近实验结构的置信度门槛，但PDB=0表明该特定同源物尚未被结构解析。模型推断整体折叠应该与已知的APP E2和铜结合结构域类似，但低pLDDT区域可能对应不同APP亚型之间分歧的N端E1结构域和A-beta序列变体。如果A0A140VJC8的A-beta区序列与经典APP有差异，这可能赋予不同的聚集倾向和/或不同的靶基因谱——这对AD治疗干扰尤为关键。

TE调控假设（推测模型）：APP胞内域转录复合体已被视为转座子抑制因子的候选。核AICD/FE65/Tip60复合体可能识别TE启动子中的特定响应元件（如NF-κB或p53结合基序，这两者均在TE中被注释，PMID: 23482656）。A-beta肽的非规则二级结构允许它与核酸骨架发生序列非特异性静电相互作用，这种"核酸伴侣"活性可能影响TE来源异染色质的形成。此外，BACE1和PSEN1的γ-分泌酶切割是一种配体非依赖性机制——任何激活APP切割的信号（氧化应激、Ca2+失调、膜流动性变化）都可能释放A0A140VJC8-splice进入核质。PubMed=0（10/10新颖性）意味着所有以上推定的TE调控活性都应在A0A140VJC8上从零开始验证。

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJC8
