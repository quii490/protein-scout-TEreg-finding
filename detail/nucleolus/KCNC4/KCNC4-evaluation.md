---
type: protein-evaluation
gene: "KCNC4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## KCNC4 (Voltage-gated potassium channel KCNC4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KCNC4 |
| 蛋白全称 | Voltage-gated potassium channel KCNC4 |
| UniProt ID | Q03721 |
| 蛋白大小 | 635 aa / 69.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 635 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR000210; InterPro:IPR005821; InterPro:IPR003968; InterPro:IPR003974; InterPro:IPR005405; InterPro:IPR021645 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Voltage-gated potassium channel that opens in response to the voltage difference across the membrane, forming a potassium-selective channel through which potassium ions pass in accordance with their electrochemical gradient (PubMed:7993631). The channel displays rapid activation and inactivation kinetics (PubMed:7993631)

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000210 |
| InterPro | IPR005821 |
| InterPro | IPR003968 |
| InterPro | IPR003974 |
| InterPro | IPR005405 |
| InterPro | IPR021645 |
| InterPro | IPR011333 |
| InterPro | IPR003131 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116396-KCNC4

![](https://images.proteinatlas.org/14740/172_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14740/172_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14740/121_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14740/121_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14740/123_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14740/123_C2_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00225; |
| InterPro | IPR000210;IPR005821;IPR003968;IPR003974;IPR005405;IPR021645;IPR011333;IPR003131;IPR028325;IPR027359; |
| Pfam | PF02214;PF00520;PF11601; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMEM67 | BioGRID | 0 |
| KCNC3 | BioGRID | 0 |
| KCNC1 | BioGRID | 0 |
| DNAJB5 | BioGRID | 0 |
| SLC25A51 | BioGRID | 0 |
| PLD6 | BioGRID | 0 |
| SMPD2 | BioGRID | 0 |
| DNAJB4 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNC4

### PubMed

**Count: 82**

| PMID | Title |
|---|---|
| 42158954 | Integrative transcriptomic analysis revealed the roles and prognostic value of ion channels in hypertrophic cardiomyopathy. |
| 41751383 | Identification and Validation of Signature Genes in Invasiveness-Associated Modules of Nonfunctioning Pituitary Adenomas. |
| 41493638 | Investigating the Effects of Sea Anemone (Stichodactyla haddoni) Toxin on Potassium and Sodium Channel Gene Expression and Cell Death Mechanisms in A5 |
| 39519104 | Genome Sequencing Identifies 13 Novel Candidate Risk Genes for Autism Spectrum Disorder in a Qatari Cohort. |
| 39092227 | The role of metabolic memory in diabetic kidney disease: identification of key genes and therapeutic targets. |

### 深度机制分析

KCNC4（Kv3.4，电压门控钾通道亚家族C成员4）的结构域架构体现了电压门控钾通道超家族的经典设计原则，但在其中又具有鲜明个性。N端胞质区域包含SMART SM00225标注的BTB/POZ结构域（Pfam PF02214, IPR000210）——这是一个约120个氨基酸残基的蛋白-蛋白互作模块，在Kv3亚家族中承担四聚体化装配的功能：四个KCNC4亚基通过其N端BTB域的T1四聚化界面（由保守疏水残基形成正交α/β折叠对接面）组装为功能性同源或异源四聚体通道。中心跨膜区由六个跨膜螺旋（S1-S6, IPR005821离子转运域, Pfam PF00520）构成，其中S1-S4形成电压感受域（VSD），S4上的正电荷精氨酸/赖氨酸残基（每三个位置一个）沿电压梯度的向外移动驱动通道构象从关闭态（S4"向下"）转向开放态（S4"向上"），S5-S6构成钾选择性滤器——保守的TVGYG签名序列以主链羰基氧精确复制K⁺水合壳层从而实现K⁺>Na⁺的十万倍选择性。KCNC4最独特的特征是极快的激活和失活动力学（PubMed:7993631）——这源于S6和S4-S5接头的序列差异，使其在超过动作电位阈值后几乎立即开放，为快速重复放电神经元提供高频动作电位复极化电流。635 aa/69.8 kDa的分子量包含C端长的胞质调节域（IPR003968 Kv3.4特异注释, IPR021645），C端含有多个磷酸化位点，PKC和ERK激酶可在此区域磷酸化以调节通道活性（包括失活恢复速率）。

PPI网络虽然偏向低分（BioGRID 8个伙伴均无实验评分），但组合模式体现了K⁺通道与蛋白质稳态系统的功能耦合。TMEM67（meckelin）是纤毛基部和内体系统的跨膜蛋白，其与KCNC4的互作提示通道蛋白在纤毛基部分选-囊泡运输路径中的质量控制；DNAJB4和DNAJB5（均为HSP40/DnaJ共伴侣蛋白家族成员）参与HSP70介导的膜蛋白折叠——这种"离子通道-蛋白稳态"的互作在神经系统中特别重要，因为电压门控钾通道的错误折叠与多种通道病变（channelopathy）相关。同家族KCNC1（Kv3.1）和KCNC3（Kv3.3）可在神经系统中共表达并形成异源通道，改变通道的电压依赖性和失活时间常数，这一互作已有电生理实验支持但被BioGRID列为0评分值（可能因检测方法为电生理而非经典PPI实验）。

无核定位注释和"主要定位于质膜"的功能角色（K⁺通道只在质膜上发挥电信号传导功能）是KCNC4被纳入nucleolus候选蛋白的最根本矛盾点。实际上内质网和核膜上确实存在功能性钾通道活性（在核膜中形成钾选择性通透以维持核质K⁺梯度），但Kv3.4亚家族目前无任何核膜定位证据。归一化得分67.8/100（124/180）中的4/10核定位评分不可低估，任何"膜通道蛋白剪切后NLS-BTB域转位入核"或"核膜K⁺选择性通道"的假说在当前阶段都缺乏实验支持。82篇PubMed宽松文献（严格检索0篇）主要涉及心肌病、神经发育障碍和癌症的转录组/基因组关联研究——其中无任何一篇将KCNC4与核功能讨论在实质层面联系起来。该蛋白在当前状态下的TE调控科学价值极低，其核心价值可能在于——如果未来被证明通过非经典机制定位至核膜——为"离子通道-染色质调控"交叉领域提供一个前所未有的实验切入点。


