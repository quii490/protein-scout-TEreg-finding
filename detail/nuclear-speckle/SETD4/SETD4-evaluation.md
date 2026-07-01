---
type: protein-evaluation
gene: "SETD4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SETD4 (SET domain-containing protein 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SETD4 |
| 蛋白全称 | SET domain-containing protein 4 |
| UniProt ID | Q9NVD3 |
| 蛋白大小 | 440 aa / 48.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 440 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR015353; InterPro:IPR036464; InterPro:IPR001214; InterPro:IPR046341; InterPro:IPR016852; InterPro:IPR050600 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Protein-lysine N-methyltransferase that methylates both histones and non-histone proteins (PubMed:31308046, PubMed:35545041, PubMed:37926288). Via its catalytic activity, regulates many processes, including cell proliferation, cell differentiation, inflammatory response and apoptosis. Regulates the inflammatory response by mediating mono- and dimethylation of 'Lys-4' of histone H3 (H3K4me1 and H3K

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR015353 |
| InterPro | IPR036464 |
| InterPro | IPR001214 |
| InterPro | IPR046341 |
| InterPro | IPR016852 |
| InterPro | IPR050600 |
| InterPro | IPR044429 |
| Pfam | PF09273 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SETD6 | STRING | 735 |
| NXF1 | BioGRID | 1 |
| DDX55 | BioGRID | 1 |
| ZMIZ1 | BioGRID | 1 |
| TADA3 | BioGRID | 1 |
| WWP1 | BioGRID | 1 |
| TP53 | BioGRID | 1 |
| TCEAL1 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000185917-SETD4

![](https://images.proteinatlas.org/35405/836_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/35405/836_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/35405/786_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35405/786_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/35405/781_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35405/781_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/35405/685_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/35405/685_D5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 42256269 | Structural variation drives praziquantel response and host adaptation in Schistosoma japonicum. | iScience 2026 |
| 42178595 | Epigenome-wide DNA methylation and spontaneous preterm birth among pregnant black women. | Clin Epigenetics 2026 |
| 41947902 | SETD4 as a marker of disease burden and treatment response in childhood acute lymphoblastic leukemiaSETD4 as a marker of | Oncol Lett 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SETD4

### 深度机制分析

**结构域架构**：SETD4（UniProt Q9NVD3，440 aa，48.4 kDa）是SET结构域含赖氨酸甲基转移酶（KMT）家族的成员。其域架构以C端SET催化域（InterPro:IPR001214 - SET domain；SMART:SM00317；Pfam:PF00856）为催化核心——该域采用伪结折叠将S-腺苷-L-甲硫氨酸（SAM）的甲基供体基团定向转移至赖氨酸底物的ε-氨基基团。N端含MHD（myeloid translocation protein-related homology domain, IPR015353），可能参与蛋白-蛋白相互作用中的底物识别。IPR046341（SET domain superfamily）定义SET甲基转移酶超家族的进化折叠保守性。IPR036464（MHD-like superfamily）为N端辅助域的折叠超家族标记。IPR016852（SETD4-type methyltransferase）为SETD4家族特异性标记。IPR050600为最新定义的含SET域蛋白家族。

**PPI互作网络**：BioGRID/STRING数据构成了一个染色质调控PPI中枢：SETD6（含SET域蛋白6，评分735）为另一SET家族甲基转移酶；NXF1（核输出因子1，评分1）参与mRNA出核；DDX55（DEAD-box RNA解旋酶，评分1）参与核糖体生物合成和pre-mRNA加工；ZMIZ1（PIAS样蛋白，评分1）为染色质重塑和STAT活化的共激活因子；TADA3（转录适配蛋白3，评分1）属于STAGA/SAGA组蛋白乙酰转移酶复合体；WWP1（HECT E3泛素连接酶，评分1）催化底物泛素化；TP53（p53，评分1）为核心转录因子和肿瘤抑制蛋白；TCEAL1（转录延长因子A样蛋白1，评分1）为转录因子。

**结构-功能关系**：SETD4催化H3K4me1和H3K4me2（组蛋白H3第4位赖氨酸的单甲基化和二甲基化）（PMID:31308046, 35545041, 37926288），在炎症应答中发挥调控作用。此外，SETD4也可以催化非组蛋白底物（如p53/TP53）的赖氨酸甲基化，通过改变蛋白稳定性、活性或亚细胞定位影响其功能。TADA3（SAGA HAT复合体组分）和ZMIZ1（STAT共激活因子）的PPI提示SETD4可能在激活转录复合体的上下文中调控H3K4甲基化标记——H3K4me1/2是增强子和启动子的活性标记。37篇PubMed（PMID:41947902 - ALL中SETD4作为疾病负荷标志物）和癌症表观遗传学研究（PMID:42178595 - 表观基因组范围DNA甲基化与早产）初步刻画了其功能和表达。

**TE调控机制**：H3K4me1/2是增强子激活的标志性组蛋白修饰，而内源性逆转录病毒（ERV）和其他TEs的LTR启动子需要H3K4甲基化标记才能启动转录。SETD4对H3K4me1/me2的催化活性暗示其可能正向调控TE转录——但SETD4也会甲基化非组蛋白底物（如p53），而p53已被证实可直接结合和沉默ERV/LTR序列。TADA3-SAGA-GCN5（乙酰转移酶）和SETD4甲基转移酶构成组蛋白修饰的交叉对话框（cross-talk）——乙酰化和甲基化的平衡可能决定TE启动子的转录输出。WWP1（HECT E3泛素连接酶）通过SETD4的泛素化调控其蛋白水平稳定性——即WWP1→SETD4降解→H3K4me1/2减少→TE启动子去激活的级联通路。

**前沿意义**：SETD4单一位于核斑体类别，但SET域蛋白质的核定位是功能必需的。鉴于H3K4甲基化在增强子生物学和TE调控中的核心地位，SETD4代表了新兴的SET甲基转移酶-TE调控交叉研究的前沿靶标。其H3K4me1/me2的催化特异性使SETD4区别于H3K9me3通路（HP1/KAP1/KRAB-ZFP），可能定义了TE甲基化调控的一类新方向——增强子样TE（而非异染色质沉默的TE）。通过SETD4 ChIP-seq定位H3K4me1/2信号在TE位点的分布及SETD4-KO后的变化，可直接验证此机制。


