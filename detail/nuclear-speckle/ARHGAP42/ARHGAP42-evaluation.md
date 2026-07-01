---
type: protein-evaluation
gene: "ARHGAP42"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## ARHGAP42 (Rho GTPase-activating protein 42) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ARHGAP42 |
| 蛋白全称 | Rho GTPase-activating protein 42 |
| UniProt ID | A6NI28 |
| 蛋白大小 | 874 aa / 96.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 7/10 | x1 | 7.0 | 874 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR027267; InterPro:IPR004148; InterPro:IPR047234; InterPro:IPR011993; InterPro:IPR001849; InterPro:IPR047225 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May influence blood pressure by functioning as a GTPase-activating protein for RHOA in vascular smooth muscle

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR004148 |
| InterPro | IPR047234 |
| InterPro | IPR011993 |
| InterPro | IPR001849 |
| InterPro | IPR047225 |
| InterPro | IPR008936 |
| InterPro | IPR000198 |

#### 3.3 核定位

无已知核定位注释

### 深度机制分析

ARHGAP42（Rho GTPase-activating protein 42）的结构域架构以RhoGAP催化模块与信号支架的多域整合为特征：N端RhoGAP催化结构域（IPR047234、IPR047225、IPR008936）通过保守的精氨酸指（arginine finger）加速Rho家族GTP酶（如RHOA、RAC1、CDC42）的GTP水解速率，将活性GTP-Rho转变为非活性GDP-Rho；PH结构域（IPR001849）负责磷酸肌醇依赖的膜靶向；BAR结构域（IPR027267、IPR004148）通过二聚化形成新月形膜弯曲诱导支架。IPR011993（PH-like domain superfamily）和IPR000198（RhoGAP family）进一步分类。

874 aa（96.1 kDa）的大分子量在多域GAP家族中典型。AlphaFold预测结构可用。PPI数据显示与DENND2C（Rab GEF）、CRK（信号衔接蛋白）、DEK（染色质架构蛋白）、BTF3（转录因子）、NACA（转录共激活因子）、PABPN1（核poly(A)结合蛋白）、SLIRP（线粒体RNA结合蛋白）的互作。DEK和NACA的连接尤为值得注意——DEK是已知的染色质结构蛋白和转录调控因子，NACA参与新生多肽的共翻译靶向。

TE调控相关性的机制推论基于核内肌动蛋白的调控角色：ARHGAP42通过抑制RHOA活性影响肌动蛋白骨架动力学，而核内肌动蛋白（nuclear actin）参与染色质重塑、转录延伸和DNA修复等多个核内过程。若ARHGAP42的BAR域使其在核膜凹陷处参与核内肌动蛋白组装调控，则其可能通过Rho信号通路间接影响：（1）SWI/SNF核小体重塑因子（含有actin和ARP作为核心组分）的活性；（2）RNA Pol II转录延伸复合物中的actin/ARP角色；（3）核膜周边异染色质（LADs）的锚定和TE沉默状态。DEK的互作进一步暗示可能参与染色质构象调控。

无GO-CC核定位注释（核定位特异性4/10），PubMed 28篇，新颖性10/10。归一化总分66.7/100。核内肌动蛋白与染色质调控的连接虽有先例但非常间接近，不建议优先靶标。

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DENND2C | BioGRID | 1 |
| CRK | BioGRID | 1 |
| DEK | BioGRID | 1 |
| BTF3 | BioGRID | 1 |
| NACA | BioGRID | 1 |
| PABPN1 | BioGRID | 1 |
| SLIRP | BioGRID | 1 |
| GCH1 | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ARHGAP42

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165895-ARHGAP42

![](https://images.proteinatlas.org/39924/1804_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/39924/1804_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/39924/1808_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/39924/1808_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/39924/451_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/39924/451_B5_5_red_green.jpg)

### PubMed

**Count: 28**

| PMID | Title |
|---|---|
| 41023780 | Investigating the genetic imprint of long body length, high lean meat rate, high fertility and long gestation period in Danish Landrace pigs. |
| 40943595 | Role of RhoGEFs or RhoGAPs in Pyk2-Mediated RhoA Activation in Depolarization-Induced Contraction of Rat Caudal Arterial Smooth Muscle. |
| 39948732 | The gene-panel obtained by anti-PD-1 monotherapy for melanoma reveals prognostic markers and therapeutic targets. |
| 39792147 | Correction to "ARHGAP42 Promotes Cell Migration and Invasion Involving PI3K/Akt Signaling Pathway in Nasopharyngeal Carcinoma". |
| 38660294 | A three-gene expression score for predicting clinical benefit to anti-PD-1 blockade in advanced renal cell carcinoma. |


