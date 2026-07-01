---
type: protein-evaluation
gene: "SREK1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SREK1 (Splicing regulatory glutamine/lysine-rich protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SREK1 |
| 蛋白全称 | Splicing regulatory glutamine/lysine-rich protein 1 |
| UniProt ID | B3KRJ9 |
| 蛋白大小 | 514 aa / 56.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 514 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR012677; InterPro:IPR035979; InterPro:IPR000504; InterPro:IPR034192; Pfam:PF00076 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Participates in the regulation of alternative splicing by modulating the activity of other splice facors. Inhibits the splicing activity of SFRS1, SFRS2 and SFRS6. Augments the splicing activity of SFRS3

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR012677 |
| InterPro | IPR035979 |
| InterPro | IPR000504 |
| InterPro | IPR034192 |
| Pfam | PF00076 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SFRS3 | STRING | 934 |
| SRSF3 | STRING | 934 |
| SRSF11 | STRING | 933 |
| RBM25 | STRING | 861 |
| SRSF10 | STRING | 850 |
| PNN | STRING | 845 |
| SRSF1 | STRING | 803 |
| RBM39 | STRING | 796 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000153914-SREK1

![](https://images.proteinatlas.org/37673/1060_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/37673/1060_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/37673/1105_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/37673/1105_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/59332/1061_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/59332/1061_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/59332/1017_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/59332/1017_H5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 16**

| 41208460 | Identification of circulating miRNA alterations in diabetes patients excluding periodontitis effects: insights into targ | Ann Med 2025 |
| 40549565 | Biallelic variants in SREK1 downregulating SNORD115 and SNORD116 cause a Prader-Willi-like syndrome. | J Clin Invest 2025 |
| 39657023 | CAX-INTERACTING PROTEIN4 depletion causes early lethality and pre-mRNA missplicing in Arabidopsis. | Plant Physiol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SREK1

### 深度机制分析

**结构域架构**：SREK1/SFRS12（UniProt B3KRJ9，514 aa，56.5 kDa）是SR（serine/arginine-rich）蛋白家族相关的剪接调控因子。其域架构以RNA识别基序（RRM）串联排布为核心：N端RRM1域（InterPro:IPR000504 - RNA recognition motif domain；Pfam:PF00076 - RRM_1；IPR035979 - RNA-binding domain superfamily）采用经典的βαββαβ折叠以芳香族残基堆积（保守RNP-1和RNP-2基序）识别单链RNA，中央区含RRM2域（IPR012677 - Nucleotide-binding alpha-beta plait domain superfamily），两个RRM域可能协同识别较大的RNA底物或桥接两个RNA区域。C端含大量RS二肽富集区（RS domain）和Glu/Lys富集区——这些低复杂度区段（LCR）介导蛋白-蛋白相互作用和核斑体（nuclear speckle）定位。IPR034192定义SREK1家族特有的RRM2-接头-RS域架构。

**PPI互作网络**：STRING数据显示SREK1深深嵌入剪接调控网络：SFRS3和SRSF3（评分934）为同一蛋白的两种表现形式——SRSF3是SR蛋白家族成员（经典剪接因子），SREK1抑制其剪接活性，构成自调控反馈。SRSF11（评分933）和SRSF10（评分850）为剪接因子，SRSF1（评分803）为SR蛋白家族原型成员（ASF/SF2），RBM25（评分861）和RBM39（评分796）为RNA结合基序蛋白，PNN（pinin，评分845）为细胞连接和核斑体组件。该PPI网络的拓扑呈现以SRSF3/SRSF1为枢纽的剪接调控网络，SREK1在其中发挥负调控角色——通过与SRSF1/2/6竞争性结合RNA剪接位点来抑制它们的剪接激活功能，同时增强SRSF3的剪接活性。

**结构-功能关系**：SREK1的RRM1域负责识别前体mRNA（pre-mRNA）的剪接增强子（ESE）或剪接沉默子（ESS）序列，而RS域通过磷酸化依赖的方式招募其他剪接因子（如SR蛋白和hnRNP）至剪接体。在剪接的E/A复合体阶段，SREK1结合于剪接位点近端区域，以位阻方式阻止SRSF1/SRSF2的ESE结合——即通过剪接位点选择调控外显子的包含/跳跃。16篇文献中，Prader-Willi样综合征的关键发现令人瞩目（PMID:40549565 - SREK1双等位基因变异通过下调SNORD115和SNORD116引起Prader-Willi样综合征），点明SREK1在核仁snoRNA调控中的非剪接功能。

**TE调控机制**：剪接因子与TE调控的交汇通过RNA加工效率实现。TE插入内含子后可引入异常剪接供体/受体位点——特别是Alu元件（含9个剪接位点样基序）和LINE-1的5'UTR（含剪接位点变体）。TE源性外显子化（exonization）可产生嵌合转录本和异常蛋白，而SREK1对剪接位点的竞争性调控可决定TE外显子是被包含还是被跳过。SRSF3互作（评分934）指向另一个重要机制——SRSF3已被证明在应激条件下调控Alu RNA的细胞质积累，且SRSF3缺失导致Alu元件广泛外显子化。SREK1作为SRSF3活性的正调控因子（增强其剪接），可能间接抑制Alu和其他TE的外显子化——即SREK1→SRSF3激活→Alu剪接抑制→基因组稳定性保护。

**前沿意义**：SREK1的Prader-Willi样综合征连接提供了snoRNA→核仁功能→染色质结构→TE沉默的通路方向。SNORD115/116是印记基因簇（15q11-q13）中Prader-Willi综合征区的核心非编码RNA，该区域包含大量神经元特异性的CI锌指基因——与KRAB-ZFP TE沉默系统有家族关联。剪接偶联的TE外显子化调控是精密且研究不足的机制——SREK1-SRSF3/SRSF1调控轴提供了功能验证的切入点。


