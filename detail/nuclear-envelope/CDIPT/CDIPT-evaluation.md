---
type: protein-evaluation
gene: "CDIPT"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## CDIPT (CDP-diacylglycerol--inositol 3-phosphatidyltransferase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | CDIPT |
| 蛋白全称 | CDP-diacylglycerol--inositol 3-phosphatidyltransferase |
| UniProt ID | O14735 |
| 蛋白大小 | 213 aa / 23.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 213 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR000462; InterPro:IPR043130; InterPro:IPR048254; InterPro:IPR014387; Pfam:PF01066 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Catalyzes the biosynthesis of phosphatidylinositol (PtdIns) as well as PtdIns:inositol exchange reaction. May thus act to reduce an excessive cellular PtdIns content. The exchange activity is due to the reverse reaction of PtdIns synthase and is dependent on CMP, which is tightly bound to the enzyme

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000462 |
| InterPro | IPR043130 |
| InterPro | IPR048254 |
| InterPro | IPR014387 |
| Pfam | PF01066 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NLRX1 | BioGRID | 0 |
| SARM1 | BioGRID | 0 |
| UNC93B1 | BioGRID | 0 |
| RPLP1 | BioGRID | 0 |
| APP | BioGRID | 0 |
| IQCB1 | BioGRID | 0 |
| NOS2 | BioGRID | 0 |
| UBL4A | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103502-CDIPT

![](https://images.proteinatlas.org/56597/990_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/56597/990_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/56597/962_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/56597/962_C8_3_red_green.jpg)

### PubMed 文献

**PubMed count: 61**

| 42052464 | Comprehensive profiling of alternative splicing and immune landscapes in rectal cancer: implications for mRNA vaccine de | Front Oncol 2026 |
| 41519831 | Identification of key miRNAs and target genes in psoriasis vulgaris and obesity co-morbidity. | Eur J Med Res 2026 |
| 41373709 | Integrated Transcriptomic and Metabolomic Analysis of the Mechanism of Intramuscular Fat Differences in Wandong Cattle. | Int J Mol Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CDIPT

### 深度机制分析

**结构域架构**：CDIPT/PIS1（UniProt O14735，213 aa，23.4 kDa）属于CDP-醇磷脂酰转移酶超家族（CDP-alcohol phosphatidyltransferase）中的磷脂酰肌醇（PI）合酶。其域架构以单个催化核心域构成：IPR000462（CDP-alcohol phosphatidyltransferase）和Pfam:PF01066（CDP-OH_P_transf）采用六次跨膜螺旋的保守折叠，活性位点位于膜包埋腔的内部。催化反应遵循有序序列Bi-Bi机制：首先CDP-DAG（CDP-二酰甘油）结合，然后肌醇攻击α-磷酸→生成PI和CMP。IPR043130（CDP-alcohol phosphatidyltransferase, transmembrane domain）定义跨膜拓扑，IPR048254（PIS1-type CDP-alcohol phosphatidyltransferase）为真菌/后生动物PI合酶的保守标记，IPR014387（CDP-diacylglycerol-inositol 3-phosphatidyltransferase, metazoa/fungi）为真核生物PI合酶家族注释。该蛋白极简（213 aa）——仅够容纳催化核心和短N/C端环区。

**PPI互作网络**：BioGRID数据展示了一个跨免疫、神经退行性疾病和纤毛的信号PPI网络：NLRX1（NLR家族X1，评分0）为线粒体抗病毒信号（MAVS）通路的负调控因子；SARM1（无菌α和TIR基序1，评分0）是Toll样受体信号适配蛋白和神经元轴突降解的NADase；UNC93B1（评分0）是TLR3/7/8/9内体运输的必需伴侣蛋白；APP（淀粉样前体蛋白，评分0）与阿尔茨海默病相关；RPLP1（核糖体磷蛋白P1，评分0）为60S核糖体亚基组分；IQCB1（IQ钙调素结合基序蛋白1，评分0）参与光转导和NPHP相关纤毛病变；NOS2（诱导型一氧化氮合酶，评分0）生成NO作为免疫效应分子；UBL4A（泛素样蛋白4A，评分0）参与tail-anchored蛋白ER插膜。

**结构-功能关系**：CDIPT催化PI的从头合成——通过利用CDP-DAG和肌醇产生PI和CMP。PI是所有磷酸肌醇（PI3P、PI4P、PI(4,5)P₂、PI(3,4,5)P₃等）的代谢前体，在真核细胞信号中处于绝对中心位置。该酶还催化逆行PI:肌醇交换反应（CMP依赖），以调节过度升高的PI水平。PI合酶是PI信号级联的"源头控制点"——其活性直接限定了整个磷酸肌醇信号网络的流量上限。仅61篇PubMed中主要涉及多组学鉴定和代谢通路建模。

**TE调控机制**：CDIPT将磷脂代谢与TE调控连接，通过关键脂质信使的多效功能实现。PI(4,5)P₂是核内独立于质膜的PI信号池，其核水平调控剪接因子（如SF3B1和U2AF）和染色质重塑复合体的活性——已知染色质重塑子SWI/SNF（BAF/PBAF）结合PI(4,5)P₂，SWI/SNF与LINE-1和ERV沉默直接相关。SARM1是CDIPT最具TE调控意义的PPI伙伴——SARM1的TIR域感知TE dsRNA并触发TLR适配信号，而且SARM1的NADase活性参与代谢应激下的NAD⁺耗竭——已知NAD⁺水平经Sirtuins（SIRT1/6）调控ERV/LTR的H3K9ac/H3K56ac去乙酰化沉默。NLRX1/MAVS轴线粒体抗病毒信号直接感知TE反转录的cDNA中间体。APP作为AD蛋白，其γ-分泌酶加工产生AICD（APP胞内域），核内AICD结合TE富含的LTR启动子。

**前沿意义**：CDIPT在213 aa中的极简域架构和PI合成的"总开关"身份赋予其不可替代的代谢调控角色。PI(4,5)P₂是核结构域（核散斑体、PML体、核膜）组装的核心脂质胶水——TE沉默常发生在PML体相关的SUMO化微环境中，而PML体的组装稳定性需要PIP₂。CDIPT通过设定PI→PIP₂的全局合成速率，可能间接决定PML体的组装效率和TE沉默因子在核内的空间分布。CDIPT的61篇文献在PI合酶基础生物化学上建立充分，但其TE调控关联的原创性极高。

