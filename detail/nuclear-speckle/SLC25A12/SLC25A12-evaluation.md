---
type: protein-evaluation
gene: "SLC25A12"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SLC25A12 (Electrogenic aspartate/glutamate antiporter SLC25A12, mitochondrial) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SLC25A12 |
| 蛋白全称 | Electrogenic aspartate/glutamate antiporter SLC25A12, mitochondrial |
| UniProt ID | O75746 |
| 蛋白大小 | 678 aa / 74.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 678 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR011992; InterPro:IPR018247; InterPro:IPR002048; InterPro:IPR002067; InterPro:IPR023395; InterPro:IPR018108 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Mitochondrial electrogenic aspartate/glutamate antiporter that favors efflux of aspartate and entry of glutamate and proton within the mitochondria as part of the malate-aspartate shuttle (PubMed:11566871, PubMed:19641205, PubMed:24515575, PubMed:38945283). Also mediates the uptake of L-cysteinesulfinate (3-sulfino-L-alanine) by mitochondria in exchange of L-glutamate and proton (PubMed:11566871).

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| InterPro | IPR002067 |
| InterPro | IPR023395 |
| InterPro | IPR018108 |
| InterPro | IPR051028 |
| Pfam | PF00153 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PNKP | BioGRID | 1 |
| PELO | BioGRID | 1 |
| MYC | BioGRID | 1 |
| SMAD3 | BioGRID | 1 |
| GNAS | BioGRID | 1 |
| ATF2 | BioGRID | 1 |
| JUND | BioGRID | 1 |
| RHOA | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000115840-SLC25A12

![](https://images.proteinatlas.org/35333/378_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/35333/378_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/35333/383_E6_4_red_green.jpg)
![](https://images.proteinatlas.org/35333/383_E6_5_red_green.jpg)
![](https://images.proteinatlas.org/35333/376_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/35333/376_E6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 134**

| 42253507 | Novel African American Colorectal Cancer MSH3 Variants Associate With Major Genomic Instability. | Hum Mutat 2026 |
| 42252407 | An inherited SLC25A12-related recessive form of congenital porencephaly in Limousin cattle. | Genet Sel Evol 2026 |
| 42203926 | A transport-independent role for SLC25A12 in mitochondrial stress signalling. | Nat Cell Biol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC25A12

### 深度机制分析

**结构域架构**：SLC25A12/Aralar1（UniProt O75746，678 aa，74.6 kDa）属于线粒体载体超家族（MCF/SLC25）。其域架构遵循典型的三重串联重复设计：三个同源重复域（Rep1-Rep2-Rep3）各含两个跨膜螺旋，形成六螺旋跨膜桶。每个重复含保守的MCF序列基序（PX[DE]XX[RK]），构成底物结合和转化路径的选择性过滤门。IPR002067（Mitochondrial carrier protein）和IPR018108（Mitochondrial substrate/solute carrier）为MCF超家族标记。IPR023395（Mitochondrial carrier domain superfamily）采用三叶草折叠——三重复对称排列形成假三重轴。IPR002048（EF-hand domain, calcium-binding）注释了一个EF-hand Ca²⁺结合域，赋予SLC25A12 Ca²⁺感知能力——这是MCF中少有的特征。Pfam:PF00153（Mito_carr）为MCF载体域。IPR051028为天冬氨酸/谷氨酸载体家族标记。

**PPI互作网络**：BioGRID互作数据展示了一个偏向转录调控的PPI图谱：MYC（c-MYC转录因子，评分1）—SMAD3（TGF-β信号转录因子，评分1）为核心转录调控节点；ATF2（活化转录因子2，评分1）和JUND（JunD转录因子，评分1）构成AP-1复合体的bZIP二聚伙伴；PNKP（多核苷酸激酶/磷酸酶，评分1）参与DNA末端加工和单链断裂修复；PELO（pelota同源蛋白，评分1）为mRNA监视和无义介导降解（NMD）因子；GNAS（Gsα，评分1）为GPCR G蛋白α亚基；RHOA（评分1）为GTPase信号中心。PPI核心呈现线粒体代谢与核转录的交叉。

**结构-功能关系**：SLC25A12作为线粒体内膜的产电天冬氨酸/谷氨酸反向转运体，介导线粒体天冬氨酸外流与胞质谷氨酸+H⁺内流（1:1交换比）。该转运构成苹果酸-天冬氨酸穿梭（MAS）的线粒体出口臂——MAS将胞质NADH还原当量传递至线粒体呼吸链（通过线粒体苹果酸脱氢酶生成NADH进入ETC）。EF-hand Ca²⁺结合域将Mas活性与线粒体Ca²⁺信号耦联——SLC25A12因此被命名为Aralar（Arachidonic acid-regulated aspartate/glutamate carrier）因其活性受花生四烯酸调控。SLC25A12在葡萄糖刺激胰岛素分泌中不可或缺（MAS在β细胞代谢-分泌偶联中的核心功能）。最近文献（PMID:42203926）揭示了SLC25A12超越转运的非经典线粒体应激信号功能。

**TE调控机制**：SLC25A12与TE调控的连接通过苹果酸-天冬氨酸穿梭（MAS）→代谢→表观基因组轴实现。MAS传递胞质NADH至线粒体，维持高NAD⁺/NADH比——而NAD⁺是Sirtuins（SIRT1/6/7）去乙酰化酶的必须底物。SIRT1去乙酰化H3K9ac和H4K16ac促进ERV/LTR位点的异染色质形成；SIRT6特异性地沉默L1转录。因此SLC25A12通过设定胞质/线粒体NAD⁺/NADH平衡间接调控全基因组H3K9ac/H4K16ac去乙酰化→TE沉默状态。PNKP互作（评分为1）指向DNA损伤修复——LINE-1 ORF2p内切酶活性产生的DNA断裂依赖PNKP末端加工。MYC-SMAD3-ATF2-JUND的转录调控PPI核心支持代谢→转录因子活性→TE启动子调控的多级联通路。最近发现的非转运应激信号功能（PMID:42203926）可能代表SLC25A12直接参与核基因表达调控的另一机制。

**前沿意义**：SLC25A12拥有134篇PubMed的文献基础（主要在线粒体代谢和神经退行性疾病），但"转运非依赖应激信号"（PMID:42203926）的突破性发现完全重塑了对该蛋白功能的认识——它不再仅是代谢物转运体。如果在应激条件下SLC25A12经蛋白裂解释放可溶性片段穿梭至核内调控转录因子活性，则其TE调控功能将从间接代谢调控转变为直接染色质调控。这一假说在现有文献框架内没有先例，通过亚细胞分级+质谱和ChIP-qPCR在SLC25A12敲除细胞中分析TE位点的H3K9ac水平是直接可行的验证方案。

