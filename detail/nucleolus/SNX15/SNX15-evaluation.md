---
type: protein-evaluation
gene: "SNX15"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SNX15 (Sorting nexin-15) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNX15 |
| 蛋白全称 | Sorting nexin-15 |
| UniProt ID | Q9NRS6 |
| 蛋白大小 | 342 aa / 37.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 342 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR051866; InterPro:IPR007330; InterPro:IPR036181; InterPro:IPR001683; InterPro:IPR036871; Pfam:PF04212 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May be involved in several stages of intracellular trafficking. Overexpression of SNX15 disrupts the normal trafficking of proteins from the plasma membrane to recycling endosomes or the TGN

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR051866 |
| InterPro | IPR007330 |
| InterPro | IPR036181 |
| InterPro | IPR001683 |
| InterPro | IPR036871 |
| Pfam | PF04212 |
| Pfam | PF00787 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

SNX15（342 aa, UniProt Q9NRS6）是Sorting Nexin家族中含MIT-PX双结构域的另一个成员，其结构域架构与SNX30形成对比：N端PX结构域（aa 1-130, IPR001683, Pfam PF00787）和C端MIT结构域（aa 265-342, SMART SM00745）。PX结构域赋予PI3P依赖性内体定位能力，而MIT（Microtubule Interacting and Trafficking）结构域通常识别ESCRT-III组分（如CHMP1-6）的MIM（MIT Interacting Motif）序列，参与多囊泡体（MVB）分选途径。SMART还检出BAR结构域（SM00312），但UniProt未单独注释BAR域，提示可能出现不完全的BAR样折叠。SNX15的过表达破坏蛋白质从质膜到循环内体或TGN的正常运输，且被发现与APP的细胞表面循环和Aβ产生调控相关（PMID:36322338）。

PPI数据揭示了具有强烈TE调控暗示的互作伙伴。METTL14（m6A甲基转移酶14, BioGRID评分1）和KDM1A（LSD1, 组蛋白去甲基化酶, BioGRID评分1）是核心亮点。METTL14与METTL3形成异源二聚体催化mRNA的m6A修饰——m6A已被证实广泛修饰LINE-1和ERV RNA转录本，影响其稳定性和翻译效率。METTL14与SNX15的互作可能在内体膜表面发生，参与m6A修饰的TE mRNA在内体-核质界面的转运质量控制。KDM1A/LSD1是CoREST抑制复合物的催化核心，通过去除H3K4me1/me2活化标记使染色质转录抑制——LSD1在胚胎干细胞中被证明直接结合并沉默ERV-MERVL元件，维持多能性基因网络的TE依赖性转录平衡。SNX15-KDM1A的互作提供了一条从内体运输到染色质修饰的直接分子链路。

HOXC10（同源框转录因子Hox-C10）和TOP3B（拓扑异构酶IIIβ, DNA拓扑异构酶IA型）的互作进一步拓宽了SNX15的核内功能暗示。TOP3B与TDRD3形成复合物结合m6A修饰的mRNA并参与R-loop的解析——R-loop在TE基因座上的异常积累可引发DNA损伤和TE去抑制。值得注意的是，RARA-SNX15融合基因在APL中发现（t(11;17;15)染色体易位, PMID:35854096），将SNX15直接牵入核受体介导的转录调控——PML-RARA融合蛋白通过异常招募HDAC和DNMT改变染色质状态，可能连带SNX15进入RARA靶基因位点（包括TE衍生增强子）。ESMFold预测的平均pLDDT=0.77（33.9%残基>0.9）表明PX和MIT结构域折叠可独立验证。

---

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000110025-SNX15

![](https://images.proteinatlas.org/38955/436_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38955/436_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38955/521_B8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38955/521_B8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/38955/442_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38955/442_B8_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00745;SM00312; |
| InterPro | IPR051866;IPR007330;IPR036181;IPR001683;IPR036871; |
| Pfam | PF04212;PF00787; |
| UniProt Domain | DOMAIN 1..130; /note="PX"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00147"; DOMAIN 265..342; /note="MIT" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAM3A | STRING | 779 |
| METTL14 | BioGRID | 1 |
| KDM1A | BioGRID | 1 |
| HOXC10 | BioGRID | 1 |
| TOP3B | BioGRID | 1 |
| RABAC1 | BioGRID | 0 |
| VPS36 | BioGRID | 0 |
| FN1 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNX15

### PubMed

**Count: 17**

| PMID | Title |
|---|---|
| 37926552 | IST1 regulates select recycling pathways. |
| 37577466 | IST1 regulates select endosomal recycling pathways. |
| 36322338 | Correction to: SNX15 Regulates Cell Surface Recycling of APP and Aβ Generation. |
| 35854096 | A novel RARA-SNX15 fusion in PML-RARA-positive acute promyelocytic leukemia with t(11;17;15)(q13;q21.2;q24.1). |
| 34831096 | Transcriptomic-Based Identification of the Immuno-Oncogenic Signature of Cholangiocarcinoma for HLC-018 Multi-Target Therapy Exploration. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/SNX15_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.77 |
| pLDDT > 0.9 | 33.9% |
| pLDDT < 0.5 | 6.7% |
| 残基数 | 342 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。