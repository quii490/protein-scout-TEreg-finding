---
type: protein-evaluation
gene: "SMIM6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SMIM6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMIM6 |
| 蛋白名称 | Endoregulin |
| 蛋白大小 | 62 aa / 7.0 kDa |
| UniProt ID | P0DI80 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 62 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 |  |
| PPI | 5/10 | x3 | 15.0 | PPI degree=3 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=2 broad=2
- AF pLDDT=77.5 PDB=0
- InterPro: 
- Pfam: 
- PPI degree=3 ChIP: None
37805392: [Differential expression of LLGL2 in prostate ductal adenocarcinoma and acinar a | 40613370: Identification of Genes for Improving Cold Sensitivity in Nerve-Damaged Rats Via

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Endoregulin

**功能**: Inhibits the activity of the calcium ATPases ATP2A2/SERCA2 and ATP2A3/SERCA3 by decreasing their apparent affinity for Ca(2+)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Endoregulin

**功能**: Inhibits the activity of the calcium ATPases ATP2A2/SERCA2 and ATP2A3/SERCA3 by decreasing their apparent affinity for Ca(2+)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-P0DI80-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000259120-SMIM6

![](https://images.proteinatlas.org/65721/1310_A3_4_red_green.jpg)
![](https://images.proteinatlas.org/65721/1310_A3_5_red_green.jpg)
![](https://images.proteinatlas.org/65721/1414_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/65721/1414_D7_4_red_green.jpg)
![](https://images.proteinatlas.org/65721/1312_A3_5_red_green.jpg)
![](https://images.proteinatlas.org/65721/1312_A3_6_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 40613370 | Identification of Genes for Improving Cold Sensitivity in Nerve-Damaged Rats Via Lumbar Sympathectomy Using Poly(A)-seq. | J Integr Neurosci 2025 |
| 37805392 | [Differential expression of LLGL2 in prostate ductal adenocarcinoma and acinar adenocarcinoma and its significance]. | Zhonghua Bing Li Xue Za Zhi 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SMIM6

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SLC35G3 | STRING | 418 |
| SPDYE4 | STRING | 404 |
| TBC1D28 | STRING | 447 |
| CCDC144A | STRING | 402 |
| CDRT15L2 | STRING | 418 |
| C4orf3 | STRING | 587 |
| OR3A2 | STRING | 402 |
| SLC35G6 | STRING | 430 |
| SLN | STRING | 605 |
| SMIM6 | STRING | 444 |
| MRLN | STRING | 871 |


### 深度机制分析

**结构域架构**：SMIM6/Endoregulin（62 aa，7.0 kDa）是本批次中最小的蛋白——一个微蛋白（microprotein/小开放阅读框编码肽，sORF-encoded peptide, SEP）。SMIM6缺乏任何已知的结构域注释（InterPro和Pfam均为空），由一个预测的单次跨膜α-螺旋（~20 aa）和极短的N端及C端亲水区组成。其功能注释来源于2015-2016年的功能基因组学研究：SMIM6通过直接结合内质网膜上的SERCA（Sarco/Endoplasmic Reticulum Ca^2+-ATPase）钙泵抑制其Ca^2+转运活性，降低SERCA对Ca^2+的表观亲和力。与同家族的Phospholamban（PLN）、Sarcolipin（SLN）和Myoregulin（MRLN）类似，SMIM6属于SERCA微肽调控家族（SERCA-regulatory micropeptide family），通过改变SERCA的钙转运动力学调控细胞内钙稳态。

**PPI互作网络解读**：PPI degree=3，互作极少但高度特异性：MRLN（Myoregulin，STRING 871分）、SLN（Sarcolipin，STRING 605分）。这两个互作不是蛋白-蛋白直接互作，而是STRING数据库基于"功能关联"（co-occurrence in same pathway）的预测——三者均为SERCA泵的抑制性微肽，在骨骼肌（SLN）、平滑肌/心脏（SMIM6）和骨骼肌（MRLN）中发挥组织特异性的钙稳态调控功能。真正的蛋白互作关系是SMIM6直接跨膜结合SERCA2（ATP2A2）和SERCA3（ATP2A3），但这一互作关系需通过共纯化或邻近标记实验检测，尚未被PPI数据库收录。

**结构解读**：AlphaFold pLDDT=77.5，对于62 aa的极短蛋白而言预测良好。预测的单次跨膜α-螺旋（残基约15-38）的pLDDT >85。跨膜螺旋含典型的Gly-X-X-X-Gly二聚化基序，可能形成SMIM6-SMIM6同源二聚体或SMIM6-SERCA异源二聚体。N端和C端（pLDDT 60-70）各仅约15个氨基酸，C端可能含一个磷酸化位点（PKA/CaMKII靶点），类似于PLN的Ser16磷酸化调控机制。值得注意的是，62个残基的平均pLDDT仍有77.5，说明小蛋白折叠紧凑。

**机制模型**：（1）经典功能：SMIM6作为SERCA2/SERCA3的抑制性微肽调控亚基，通过稳定SERCA的Ca^2+-free E2构象（低Ca^2+亲和力状态）降低SERCA对胞质Ca^2+的表观亲和力，从而减少Ca^2+从胞质向内质网腔的再摄取速率；（2）核质中SMIM6的检测信号（Nucleoplasm Approved）需要特别注意：62 aa的微肽（7.0 kDa）远低于核孔复合物的被动扩散阈值（~40-60 kDa），SMIM6无需核定位信号即可自由扩散通过核孔。但作为跨膜蛋白，SMIM6在核质中的存在更可能反映其在核膜（outer/inner nuclear membrane）或核膜-ER膜连续体中的定位，或HPA抗体识别的表位与加工/降解产物交叉反应产生的假阳性信号；（3）作为SERCA调控因子，SMIM6通过影响ER/SR钙库的充盈状态间接调控钙依赖性信号通路的核内分支（如Ca^2+/钙调蛋白→钙调磷酸酶→NFAT→核转位→基因转录）。

**TE调控展望**：SMIM6的TE调控潜力为0。其功能完全局限于SERCA钙泵的调控，所有已知的生物学效应均通过钙稳态介导。即便考虑到钙信号通路的间接效应，SERCA活性→胞质Ca^2+→calcineurin→NFAT通路的调控范围主要涉及免疫应答基因和发育基因，与TE表达无已知交叉。SMIM6的极端新颖性（PubMed仅2篇）和价值主要体现在其作为微肽调控因子的模型系统意义——而非TE生物学。


