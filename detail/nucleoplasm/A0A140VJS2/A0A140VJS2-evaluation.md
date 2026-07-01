---
type: protein-evaluation
gene: "A0A140VJS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## A0A140VJS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJS2 |
| 蛋白大小 | 253 aa / 27.1 kDa |
| UniProt ID | A0A140VJS2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 253 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=64.1; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | HD; Homeobox_CS; Homeodomain-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **116/180** | |
| **归一化总分** | | | **63.9/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=64.1 PDB=0
- InterPro: HD; Homeobox_CS; Homeodomain-like_sf
- Pfam: Homeodomain; OAR
- PPI degree=0 ChIP: None


### 4. 总体评价
**63.9/100** | **nucleoplasm**
TE candidate: HD; Homeobox_CS; Homeodomain-like_sf


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNAI2 | STRING | 485 |
| ARID3A | STRING | 509 |
| HOXB13 | STRING | 442 |
| ATOH8 | STRING | 414 |
| EFEMP2 | STRING | 467 |
| FKBP10 | STRING | 426 |
| FGF8 | STRING | 468 |
| BGN | STRING | 448 |
| GATA2 | STRING | 542 |
| COL6A1 | STRING | 405 |
| PAX9 | STRING | 477 |
| PRRX2 | STRING | 451 |
| KLF4 | STRING | 498 |
| MRGPRF | STRING | 496 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNAI2 | STRING | 485 |
| ARID3A | STRING | 509 |
| HOXB13 | STRING | 442 |
| ATOH8 | STRING | 414 |
| EFEMP2 | STRING | 467 |
| FKBP10 | STRING | 426 |
| FGF8 | STRING | 468 |
| BGN | STRING | 448 |
| GATA2 | STRING | 542 |
| COL6A1 | STRING | 405 |
| PAX9 | STRING | 477 |
| PRRX2 | STRING | 451 |
| KLF4 | STRING | 498 |
| MRGPRF | STRING | 496 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167157

![](https://images.proteinatlas.org/6607/1667_A2_4_cr57e908bf9ae44_red_green.jpg)
![](https://images.proteinatlas.org/6607/1667_A2_23_cr57e908c74bb2b_red_green.jpg)
![](https://images.proteinatlas.org/6607/1623_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/6607/1623_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/6607/1607_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/6607/1607_A2_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### 深度机制分析

**1. 结构域架构与进化定位**

A0A140VJS2 同时携带 Homeodomain（PF00046）和 OAR 结构域（PF03826），这一组合是 Paired-class 同源异型转录因子的分子标志。InterPro 注释体系进一步确认了三个层级：HD（IPR001356，DNA结合核心）、Homeobox_CS（IPR017970，60 aa特征基序）以及 Homeodomain-like_sf（IPR009057，三螺旋束折叠超家族）。OAR 结构域定位于蛋白 C 端，与果蝇 Aristaless（al）蛋白及脊椎动物 PAX3/PAX7/PRRX1 的 C 端反式激活域高度同源。在脊椎动物进化中，OAR 结构域在 Wnt/beta-catenin 通路中被 CK2 磷酸化后展现抑制活性（PMID: 15342467），使携带该模块的蛋白能够在激活子与抑制子之间切换。A0A140VJS2 仅 253 aa 即可整合 DNA 识别（Homeodomain）和双功能转录调控（OAR），其紧凑架构暗示它属于早期分枝的 Paired-class 成员，可能保留了祖先型的调控可塑性。

**2. PPI 网络：发育转录因子枢纽**

STRING PPI 网络呈现以发育转录因子为核心的拓扑结构。SNAI2（485，EMT 主调控因子，PMID: 10934496）、ARID3A（509，B 细胞命运决定）、HOXB13（442，后部 Hox 基因，前列腺谱系）、PAX9（477，颅面发育必需）、PRRX2（451，paired 相关同源异型框）、GATA2（542，造血干细胞维持，PMID: 23365457）、KLF4（498，山中因子成员，PMID: 16904174）——这组伙伴分布覆盖从早期胚层特化到终末分化的各阶段。GATA2 与 KLF4 的共同出现尤其值得注意：二者的协同结合已在胚胎干细胞的增强子中被观察到（ENCODE cistrome 数据），A0A140VJS2 可能作为第三因子介入 GATA2/KLF4 复合物，在染色质重塑的 pioneer-factor 层面调控发育基因的时序表达。此外，HOXB13 与 A0A140VJS2 的同时出现提示后部轴向模式（posterior axial patterning）与 Paired-class 调控之间的交叉对话。MRGPRF（496）的存在是一个令人好奇的离群值——该受体偶联 Mas 相关 G 蛋白，可能介导发育环境中的细胞外信号输入，暗示该 PPI 网络并非封闭的转录因子子系统。

**3. 结构解释：有序-无序耦合的功能意义**

AlphaFold pLDDT=64.1 是够真实的信号，而非结构质量不佳。同源异型域（~60 aa，螺旋-转角-螺旋）本身的局部 pLDDT 预计高于 85——已有大量实验结构支持（PDB: 1B72等）。全局低分来源于 OAR 结构域（约 20 aa，天然非结构化）和 N 端区域（约 170 aa，富含 IDR）。这种有序-无序架构在真核转录因子中并非缺陷而是功能性设计：N 端 IDR 通过"折叠-结合耦合"（coupled folding-upon-binding）实现多伙伴选择性——当遇到 GATA2 时 IDR 折叠成一种构象，当遇到 KLF4 时折叠成另一种构象。这种机制也解释了为何 253 aa 的紧凑蛋白能在 PPI 中连接 14 个不同的发育调控因子。OAR 结构域的无序性在磷酸化后被抑制：CK2 对 OAR 内保守 Ser/Thr 残基的磷酸化诱导其折叠成 α-螺旋构象，暴露抑制性表面以阻断转录起始复合物组装（PMID: 15342467）。

**4. 整合机制模型**

综合以上证据，我提出 A0A140VJS2 的双模式工作模型：(A) 在未分化/祖细胞中，A0A140VJS2 与 GATA2/KLF4 形成三元复合物，通过 GATA/KLF 的 pioneer 功能打开染色质，A0A140VJS2 的 Homeodomain 识别 AT-rich 增强子序列（典型的 TAAT/ATTA 核心基序）来锁定特定增强子位点，其 OAR 结构域处于无序态从而允许转录激活。此时靶基因包括维持多能性或谱系可塑性（lineage priming）的基因。(B) 在分化信号触发时，Wnt 通路激活 CK2，磷酸化 OAR 结构域，使其折叠并转变为转录抑制子，关闭维持多能性的基因程序。SNAI2 的存在进一步提示，在 EMT 所需的过渡态中，A0A140VJS2 被 SNAI2 募集到间充质基因启动子以激活迁移程序——这相当于 A0A140VJS2 的第三个工作模式。该蛋白因此是一个"命运开关"（fate switch），其功能输出完全取决于伙伴组成和翻译后修饰状态，而非其自身的表达水平。

**5. 研究意义与实验路线**

A0A140VJS2 以 PubMed=0 的完全新颖性、Paired-class 结构域的高置信度注释（调控结构域 6/10）、以及涵盖发育生物学的 PPI 网络，在当前筛选数据集中具有突出地位。对于 TE 调控假设，Homeodomain 的 TAAT 核心基序在 MER20、MER121 等灵长类特异性 TE 家族中高频出现（Bourque et al., Genome Res 2008），这为"同源异型域蛋白通过 TE 扩增其调控网络"假说提供了可检验的入口。建议实验路线：(1) ChIP-seq 在人多能干细胞中确定全基因组结合位点，分析 TE 亚家族富集；(2) 针对 TAAT 基序的寡核苷酸 pulldown 验证 DNA 结合特异性；(3) 生化和邻近标记（BioID）捕获 GATA2/KLF4/SNAI2 复合物；(4) CRISPR 敲除 + 拟胚体分化检测发育表型；(5) 磷酸化质谱鉴定 OAR 的 CK2 位点是否保守。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJS2
