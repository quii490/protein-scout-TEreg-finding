---
type: protein-evaluation
gene: "KCNC1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## KCNC1 (Voltage-gated potassium channel KCNC1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KCNC1 |
| 蛋白全称 | Voltage-gated potassium channel KCNC1 |
| UniProt ID | P48547 |
| 蛋白大小 | 511 aa / 56.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 511 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR000210; InterPro:IPR005821; InterPro:IPR003968; InterPro:IPR003974; InterPro:IPR005403; InterPro:IPR011333 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Voltage-gated potassium channel that opens in response to the voltage difference across the membrane and through which potassium ions pass in accordance with their electrochemical gradient (PubMed:25401298, PubMed:35840580). The mechanism is time-dependent and inactivation is slow (By similarity). Plays an important role in the rapid repolarization of fast-firing brain neurons (By similarity). Can

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000210 |
| InterPro | IPR005821 |
| InterPro | IPR003968 |
| InterPro | IPR003974 |
| InterPro | IPR005403 |
| InterPro | IPR011333 |
| InterPro | IPR003131 |
| InterPro | IPR028325 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KCNC2 | BioGRID | 0 |
| ANK3 | BioGRID | 0 |
| KCNG3 | BioGRID | 0 |
| KCNH1 | BioGRID | 0 |
| KCNV2 | BioGRID | 0 |
| DLG1 | BioGRID | 0 |
| CAMK2A | BioGRID | 0 |
| KCNC4 | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000129159-KCNC1

![](https://images.proteinatlas.org/47634/1417_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/47634/1417_B10_4_red_green.jpg)
![](https://images.proteinatlas.org/47634/1372_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/47634/1372_E11_3_red_green.jpg)
![](https://images.proteinatlas.org/47634/1370_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/47634/1370_E11_3_red_green.jpg)
![](https://images.proteinatlas.org/48249/1417_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/48249/1417_A9_3_red_green.jpg)

### PubMed 文献

**PubMed count: 169**

| 42347804 | An epilepsy-associated KV3.1 potassium channel variant acts via dominant-positive effect. | J Gen Physiol 2026 |
| 42141755 | Discovery of Kv3.1 channel inhibitors reveals VU0521426 as a state-dependent inactivator preferentially active against p | Am J Physiol Cell Physiol 2026 |
| 42003125 | Potassium Channelopathies and Precision Medicine Approaches in Epilepsy: A Systematic Review of Personalized Treatment S | Curr Neuropharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNC1

### 深度机制分析

**结构域架构**：KCNC1/Kv3.1（UniProt P48547，511 aa，56.2 kDa）是电压门控钾通道（Kv）Shaw亚家族的成员。其域架构包含经典的6次跨膜螺旋（S1-S6）Kv通道设计：S1-S4形成电压感受域（VSD），S4携带多个正电荷精氨酸残基构成电压传感器的核心（InterPro:IPR003968 - Potassium channel, voltage-dependent, Kv）；S5-S6形成中央钾离子选择性孔道域（IPR005821 - Ion transport domain），包含保守的钾选择性过滤器序列（TVGYG）。N端T1域（IPR003131 - Potassium channel tetramerisation-type BTB domain）介导亚基的四聚化组装，使4个Kv3.1亚基形成功能性同源/异源四聚体通道。Pfam:PF02257（BTB/POZ）提供T1域注释。

**PPI互作网络**：BioGRID互作数据显示KCNC1与同源通道亚基形成功能伙伴网络：KCNC2（Kv3.2，评分0）、KCNG3（Kv6.3，评分0）、KCNH1（Kv10.1，评分0）、KCNV2（Kv8.2，评分0）和KCNC4（Kv3.4，评分0）。ANK3（Ankyrin-G，评分0）介导通道在轴突起始段的亚细胞定位，DLG1（PSD-95，评分0）为突触后密度支架蛋白，CAMK2A（CaMKIIα，评分0）为钙/钙调蛋白依赖性激酶。该PPI网络呈现典型的神经离子通道互作拓扑。

**结构-功能关系**：KCNC1在膜电位去极化后打开钾选择性通道，介导快firing神经元的快速复极化（PMID:25401298, 35840580）。失活动力学缓慢（By similarity），支持高频放电能力。HPA IF数据在多细胞系中呈细胞质/膜染色模式。169篇PubMed文献主要围绕癫痫和Kv3.1通道病等领域（PMID:42347804 - 癫痫相关Kv3.1变异体通过显性正效应起作用；PMID:42003125 - 钾通道病与癫痫精准医学）。

**TE调控机制**：KCNC1作为质膜电压门控离子通道，其TE调控关联似乎是高度间接的。但ANK3锚定蛋白互作提示了一个令人兴奋的连接——ANK3在核被膜和核内均有分布（特定同工型），参与核骨架-膜连接，该蛋白是看家基因的染色质组织者。膜电位变化通过钙信号（CAMK2A下游）可激活即早基因（IEG）——IEG启动子区域富含ERV/LTR序列，因此Kv3.1→膜电位→Ca²⁺→CAMK→CREB的级联通路可直接影响TE包含的CRE响应元件。此外，神经元活动调控的染色质重塑已知涉及LINE-1的体细胞插入事件——电压门控通道活性改变可能通过调控此过程的基因组可及性间接影响TE移动性。

**前沿意义**：KCNC1代表离子通道超家族中TE调控方向的极端案例——其TE调控意义不在于直接的染色质结合，而在于神经活动→表观遗传重编程→TE激活的间接通路。癫痫相关KCNC1突变体（PMID:42347804）的诱导多能干细胞模型可用于测试膜兴奋性改变是否导致神经元TE表达谱变化，但该方向概念创新性大于直接实验可行性。

