---
type: protein-evaluation
gene: "YME1L1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## YME1L1 (ATP-dependent zinc metalloprotease YME1L1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | YME1L1 |
| 蛋白全称 | ATP-dependent zinc metalloprotease YME1L1 |
| UniProt ID | Q96TA2 |
| 蛋白大小 | 773 aa / 85.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 773 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR003593; InterPro:IPR041569; InterPro:IPR003959; InterPro:IPR003960; InterPro:IPR005936; InterPro:IPR027417 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

ATP-dependent metalloprotease that catalyzes the degradation of folded and unfolded proteins with a suitable degron sequence in the mitochondrial intermembrane region (PubMed:24315374, PubMed:26923599, PubMed:27786171, PubMed:31695197, PubMed:33237841, PubMed:36206740). Plays an important role in regulating mitochondrial morphology and function by cleaving OPA1 at position S2, giving rise to a for

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR003593 |
| InterPro | IPR041569 |
| InterPro | IPR003959 |
| InterPro | IPR003960 |
| InterPro | IPR005936 |
| InterPro | IPR027417 |
| InterPro | IPR000642 |
| InterPro | IPR037219 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000136758-YME1L1

![](https://images.proteinatlas.org/66953/1247_F11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/66953/1247_F11_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/66953/1417_E5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66953/1417_E5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66953/1244_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66953/1244_F11_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00382; |
| InterPro | IPR003593;IPR041569;IPR003959;IPR003960;IPR005936;IPR027417;IPR000642;IPR037219; |
| Pfam | PF00004;PF17862;PF01434; |
| UniProt Domain [FT] | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PHB2 | STRING | 841 |
| PHB1 | STRING | 814 |
| PHB | STRING | 814 |
| DAP3 | BioGRID | 1 |
| NDUFB6 | BioGRID | 1 |
| MYOG | BioGRID | 1 |
| BCL11A | BioGRID | 1 |
| DYRK4 | BioGRID | 1 |


### PubMed 文献

**PubMed count: 84**

| 42361792 | A negative regulator of mitochondrial complex I assembly adapts respiration to cellular energy demand. | Mol Cell 2026 |
| 41940976 | Exploratory identification of lycorine as a potential inhibitor of the ACP2/YME1L1 prognostic axis in esophageal squamou | Mol Genet Genomics 2026 |
| 41760253 | Expression of YME1 Like 1 ATPase Increases With the Stage of Adrenocortical Carcinoma Tissue and Is Associated With Poor | Anticancer Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/YME1L1

### 深度机制分析

**结构域架构**：YME1L1（UniProt Q96TA2，773 aa，85.0 kDa）属于AAA+（ATPases Associated with diverse cellular Activities）蛋白酶家族。其域架构为典型的i-AAA蛋白酶组织方式：N端跨膜域锚定于线粒体内膜（将催化域定位于膜间空间），中央AAA+ ATPase域（InterPro:IPR003593 - AAA+ ATPase domain, SMART:SM00382，含Walker A/B基序），以及C端M41家族锌金属蛋白酶催化域（InterPro:IPR041569 - Peptidase M41, Pfam:PF01434）。AAA+域（Pfam:PF00004）形成六聚体环，以ATP水解驱动底物转位进入内部降解腔。IPR003959/系列ATPase核心域和IPR005936/M41 FtsH蛋白酶域共同构成功能双模块。

**PPI互作网络**：STRING数据显示核心互作集中在线粒体质量控制网络：PHB2（prohibitin-2，评分841）、PHB1/PHB（prohibitin-1，评分814）均为线粒体膜支架蛋白，与YME1L1协同调控OPA1剪切和嵴形态。BioGRID记录的DAP3（评分为1）是线粒体核糖体蛋白，NDUFB6（评分为1）属线粒体呼吸链复合体I亚基，MYOG（评分为1）是肌生成转录因子，BCL11A（评分为1）为B细胞转录因子。PPI网络呈线粒体中心性，但MYOG/BCL11A等核转录因子互作可能反映逆行信号调控。

**结构-功能关系**：YME1L1的AAA+域以ATP水解为动力，驱动蛋白底物的解析叠和转位进入M41蛋白酶腔（PMID:24315374, 26923599, 27786171）。其线粒体形态调控功能通过对OPA1（optic atrophy 1）的S2位点剪切实现——非剪切的长型OPA1（L-OPA1）促进线粒体融合，剪切后的短型OPA1（S-OPA1）利于裂变（PMID:31695197）。YME1L1的活性受线粒体膜电位和脂质组成（特别是心磷脂水平）调控，提供能量状态→嵴形态的信号转导通路。

**TE调控机制**：YME1L1本身是线粒体蛋白，其TE调控关联似乎是间接的。然而线粒体功能障碍→活性氧（ROS）升高→DNA损伤→TE去抑制的级联通路为YME1L1提供了TE调控的潜在入口。线粒体应激相关的逆行信号可激活核转录程序，导致染色质重塑复合体重新分配——此过程可能释放TE沉默因子。特别地，PARP1-RAD51通路的线粒体-核信号传递可改变基因组稳定性，而TE启动子常受此类DNA损伤感知通路调控（YARS2相关研究PMID:42235275提示线粒体aaRS参与PARPi抗性）。YME1L1缺陷导致的线粒体碎裂可能经cGAS-STING感知mtDNA泄漏，引发IFN应答—TE激活级联。

**前沿意义**：YME1L1的84篇PubMed文献量表明其已被充分表征（特别是在线粒体生物学领域），但从TE调控视角出发属全新研究角度。将线粒体质量控制与核TE沉默联系起来构成概念创新—需通过YME1L1敲除/敲低后转座子RNA-seq和ATAC-seq验证这一假说。YME1L1现有的药理抑制剂（如Urolithin A通过prohibitin网络间接调控）为快速化学遗传学验证提供了机会。

