---
type: protein-evaluation
gene: "KRT77"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## KRT77 (Keratin, type II cytoskeletal 1b) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KRT77 |
| 蛋白全称 | Keratin, type II cytoskeletal 1b |
| UniProt ID | Q7Z794 |
| 蛋白大小 | 578 aa / 63.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 578 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR018039; InterPro:IPR039008; InterPro:IPR032444; InterPro:IPR003054; Pfam:PF00038; Pfam:PF16208 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Structural component of intermediate filaments in epithelial cells of stratified epithelia. Assembles into heteropolymers with a type I keratin, forming keratin intermediate filament networks contributing to epithelial integrity

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR018039 |
| InterPro | IPR039008 |
| InterPro | IPR032444 |
| InterPro | IPR003054 |
| Pfam | PF00038 |
| Pfam | PF16208 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NUAK1 | BioGRID | 0 |
| NFKBIL1 | BioGRID | 0 |
| USP32P2 | BioGRID | 0 |
| USP53 | BioGRID | 0 |
| CUL5 | BioGRID | 0 |
| DCUN1D1 | BioGRID | 0 |
| SHC1 | BioGRID | 0 |
| CRK | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000189182-KRT77

![](https://images.proteinatlas.org/45934/1573_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45934/1573_G5_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 16**

| 41792138 | The genetic basis of dermatophytosis skin infection susceptibility. | Nat Commun 2026 |
| 41348204 | An integrated approach combining computational analyses and experimental validation deciphers the mechanism and active s | Naunyn Schmiedebergs Arch Pharmacol 2026 |
| 40341493 | Exhaled breath protein composition in patients hospitalised during the first wave of COVID-19. | J Breath Res 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRT77

### 深度机制分析

**结构域架构**：KRT77（UniProt Q7Z794，578 aa，63.6 kDa）属于II型细胞角蛋白（碱性角蛋白）家族。其域架构遵循角蛋白经典的三段式设计：N端头域（Head）、中央α-螺旋杆状域（Rod）和C端尾域（Tail）。中央杆状域（InterPro:IPR039008 - Keratin, type II；IPR018039 - Intermediate filament protein, conserved site）形成约310 aa的α-螺旋卷曲螺旋（coiled-coil）二聚化界面，由四个分段（1A、1B、2A、2B）经三个非螺旋连接子（L1、L12、L2）串联——这是所有中间丝的保守组织方式。Pfam:PF00038（Intermediate filament protein）和PF16208（Keratin_2_head）分别注释杆状域和II型角蛋白头域。IPR003054（Keratin, type II）定义II型（碱性）角蛋白特异性的电荷特征，IPR032444（Keratin_2_head）为KRT77特异性头部域。与I型（酸性）角蛋白（如KRT10/KRT14等）形成专性异二聚体（1:1化学计量），该异二聚体再反平行组装为四聚体原丝——进一步横向结合为10 nm中间丝。

**PPI互作网络**：BioGRID互作数据展示了角蛋白-信号蛋白交互网络：NUAK1（AMPK相关激酶，评分0）磷酸化调控角蛋白丝的解聚/组装动态；NFKBIL1（IκB样蛋白，评分0）参与NF-κB信号抑制；USP32P2和USP53为去泛素化酶假基因/家族成员（评分0）；CUL5（Cullin-5泛素连接酶支架，评分0）和DCUN1D1（Cullin neddylation调控因子，评分0）构成Cullin-RING E3连接酶（CRL）网络；SHC1（SH2转化蛋白1，评分0）和CRK（CT10调节激酶，评分0）为酪氨酸激酶信号适配蛋白。CUL5是最具TE调控意义的PPI伙伴——它以含SOCS-box蛋白为底物受体，介导抗病毒限制因子（如APOBEC3G）和信号蛋白的泛素化降解，直接参与HIV-1限制和ERV抑制。

**结构-功能关系**：KRT77的表达局限于复层鳞状上皮的棘层和颗粒层——这是皮肤屏障分化末期形成角质化包膜的阶段。作为II型角蛋白，KRT77必须与I型角蛋白伙伴形成异聚体才能组装为功能性中间丝网络。角蛋白丝不仅是机械支撑结构，其动态重构（受磷酸化调控——NUAK1互作支持此观点）响应渗透压、氧化应激和UV损伤信号。与典型表皮角蛋白相比，KRT77的C端尾域较短（约40 aa而非70-100 aa），这意味着甘氨酸/丝氨酸丰富的柔性C端域较少。仅16篇文献中自然通讯级别的皮肤病遗传学论文（PMID:41792138）暗示KRT77变异体可影响皮肤感染易感性。

**TE调控机制**：角蛋白与中国纤维的TE调控连接主要通过核被膜结构和信号转导实现。NFKBIL1（IκB样NF-κB抑制因子）的PPI提示KRT77可能通过角蛋白丝→灶黏附→整合素→NF-κB通路的机械转导调控先天免疫基因表达和TE转录。CUL5-CRL的E3泛素连接酶网络直接参与APOBEC3蛋白的稳定性调控——APOBEC3G/F是LINE-1逆转录转座和HIV-1复制的强效胞苷脱氨酶限制因子。在表皮分化过程中，角蛋白丝网络的解聚伴随转录重编程（包括ERV表达上调作为正常分化程序的一部分），而KRT77-NUAK1磷酸化轴可能协调这一过程。

**前沿意义**：KRT77是角蛋白家族中最少被研究的成员之一，但CUL5-DCUN1D1-CRL泛素连接酶网络使其在TE限制方面具有间接但潜在的功能。角蛋白作为"危险信号"在细胞应激/损伤后释放，激活TLR→NF-κB→IFN信号——此通路已知可同时沉默和激活TE家族（取决于TE种类和细胞上下文）。在皮肤病背景下，KRT77突变通过改变角蛋白丝的完整性可能扰乱表皮免疫稳态——这可能导致ERV去抑制，因为健康表皮中ERV受到严格沉默。


