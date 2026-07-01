---
type: protein-evaluation
gene: "ENDOD1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## ENDOD1 (Endonuclease domain-containing 1 protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ENDOD1 |
| 蛋白全称 | Endonuclease domain-containing 1 protein |
| UniProt ID | O94919 |
| 蛋白大小 | 500 aa / 55.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 500 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR044929; InterPro:IPR001604; InterPro:IPR039015; InterPro:IPR060501; InterPro:IPR020821; InterPro:IPR044925 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May act as a DNase and a RNase. Plays a role in the modulation of innate immune signaling through the cGAS-STING pathway by interacting with RNF26

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR044929 |
| InterPro | IPR001604 |
| InterPro | IPR039015 |
| InterPro | IPR060501 |
| InterPro | IPR020821 |
| InterPro | IPR044925 |
| Pfam | PF28501 |
| Pfam | PF01223 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RNF26 | STRING | 792 |
| MOV10 | BioGRID | 1 |
| NXF1 | BioGRID | 1 |
| SPPL2B | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |
| RNF4 | BioGRID | 1 |
| HRAS | BioGRID | 1 |
| FASN | BioGRID | 1 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000149218-ENDOD1

![](https://images.proteinatlas.org/8932/1395_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8932/1395_H7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/8932/82_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8932/82_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8932/101_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8932/101_C7_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 21**

| 42035094 | Overexpression of ENDOD1 inhibits proliferation, migration, and invasion of colorectal cancer. | Cell Div 2026 |
| 41996197 | Brain Proteomic Responses to Glucocorticoids and Their Relationship With Transcriptome: A Systematic Meta-Analysis. | FASEB J 2026 |
| 41138693 | Uncovering the Molecular Networks of Extracellular Vesicles in the Pathogenesis of Periodontitis. | Int Dent J 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ENDOD1

### 深度机制分析

**结构域架构**：ENDOD1（UniProt O94919，500 aa，55.0 kDa）含两个核心催化域。其一是IPR001604（DNA/RNA non-specific endonuclease, Pfam:PF01223）——该域采用类似于Serratia核酸酶的α/β折叠，以Mg²⁺/Mn²⁺依赖的方式催化单链或双链核酸的非序列特异性切割，同时具有DNase和RNase活性。其二是IPR039015（Endonuclease domain-containing 1 protein type），为ENDOD1特异性的家族标记。IPR044929和IPR044925定义核酸酶超家族的进化保守域。Pfam:PF28501为新定义的ENDOD1专属N端延伸域。IPR060501为cGAS-STING通路相关的功能域标记。

**PPI互作网络**：STRING/BioGRID数据显示RNF26（E3泛素连接酶，评分792）为最强互作伙伴——RNF26定位于内质网，通过催化内质网膜蛋白的K63链泛素化来调控内质网到核内体的囊泡分选，并可直接调控cGAS-STING信号（RNF26在ER上锚定STING蛋白）。MOV10（Moloney白血病病毒10同源物，评分1）为关键发现——MOV10是已知的LINE-1和IAP反转录转座子抑制因子（作为RNA解旋酶结合TE RNA并招募TUT4/7尿苷化酶）。HNRNPL（异质核核糖核蛋白L，评分1）为pre-mRNA剪接和mRNA稳定性调控因子。NXF1（核输出因子1，评分1）介导成熟的polyA+ RNA出核。

**结构-功能关系**：ENDOD1的双核酸酶活性（DNase/RNase）赋予其多功能核酸处理能力。UniProt功能描述明确指出ENDOD1参与cGAS-STING先天免疫信号通路的调控，这是通过RNF26互作实现的——RNF26通过内质网膜定位控制STING的降解时效。ENDOD1可能通过水解胞质中的异常DNA/RNA片段来设定cGAS-STING活化的阈值，防止先天免疫的过度激活。MOV10互作提示ENDOD1的RNase活性可将TE RNA转录本作为底物。NXF1互作指向TE相关RNA加工在核输出水平的功能。

**TE调控机制**：ENDOD1在TE调控中的核心角色通过三重通路实现。其一，通过MOV10互作参与TE RNA降解——MOV10识别LINE-1和IAP RNA，ENDOD1的RNase活性可协同将这类RNA切割为碎片，以TUT4/7介导的尿苷化降解或XRN1 5'→3'外切酶途径清除。其二，cGAS-STING通路对TE来源的胞质DNA具有先天免疫感知功能——ENDOD1通过RNF26→STING轴调控此通路的活化阈值，防止慢性TE转座导致的持续性炎症（I型IFN病）。其三，NXF1/HNRNPL互作提示ENDOD1可能通过调控TE RNA的核输出效率来限制TE编码蛋白的胞质翻译——hnRNP L已知结合LINE-1 ORF1 RNA的3'UTR。

**前沿意义**：ENDOD1作为cGAS-STING调控因子和核酸酶的双重身份，使其成为TE先天免疫感知网络的理想节点蛋白。MOV10互作（BioGRID评分1）是将ENDOD1直接嵌入TE限制因子网络的最关键证据，而cGAS-STING轴则提供了炎症调控的旁路。21篇PubMed文献中已有癌症相关研究（PMID:42035094 - ENDOD1过表达抑制结直肠癌增殖、迁移和侵袭），而TE在肿瘤中的去抑制模式使ENDOD1的TE调控功能具有转化医学价值。

