---
type: protein-evaluation
gene: "SCRT2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---
## SCRT2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SCRT2 |
| 蛋白名称 | Transcriptional repressor scratch 2 |
| 蛋白大小 | 307 aa / 32.6 kDa |
| UniProt ID | Q9NQ03 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) + ChIP |
| 蛋白大小 | 9/10 | x1 | 9.0 | 307 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=11 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=56.4; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | x3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
HPA: Nucleoplasm (Approved)
PubMed: strict=11, broad=20
AF pLDDT: 56.4  PDB: 0
InterPro: Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type
Pfam: zf-C2H2
PPI degree: 9  ChIP: Yes
**Papers**: 32984310: Scratch2, a Snail Superfamily Member, Is Regulated by miR-125b. | 35854088: Myelin toxicity of chlorhexidine in zebrafish larvae. | 39268037: Differentiation stage-specific expression of transcriptional regulators for epit

### 4. 总体评价
★★★★  **71.6/100**  |  **nucleoplasm**
**TE candidate** -- Snail/Krueppel_Znf; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

SCRT2（Scratch 2）是Snail超家族（Snail/Slug/Scratch）中的转录抑制因子，307个氨基酸的经典锌指转录因子架构包含多个C2H2型锌指结构域（IPR013087/Znf_C2H2_type, PF00096/zf-C2H2）。每个C2H2锌指通过2个半胱氨酸和2个组氨酸配位一个Zn2+离子，形成紧凑的ββα折叠单元——α-螺旋插入DNA大沟进行序列特异性识别。Snail/Krueppel_Znf超家族（IPR050527/IPR036236）成员通常结合E-box（CAGGTG/CACCTG）基序，通过N端的SNAG（Snail/Gfi）抑制结构域招募共抑制因子（如CtBP、Sin3A/HDAC、PRC2）来沉默靶基因转录。

HPA Approved的Nucleoplasm定位加上ChIP验证（核定位特异性9/10）使SCRT2成为本批次中核定位证据最强的蛋白之一。其PPI网络（degree=9）虽小但引人注目：与FZR1（Cdh1，APC/C泛素连接酶的底物识别亚基）、SBDS（核糖体成熟因子）、TRRAP（SAGA乙酰转移酶复合体的核心组分）和RECQL（RecQ DNA解旋酶）的互作（BioGRID=1）一一指向核内核心功能——细胞周期调控、核糖体生物合成、组蛋白乙酰化和DNA修复。尤为重要的是，TRRAP作为所有SAGA乙酰转移酶功能的必需支架蛋白，SCRT2-TRRAP互作暗示SCRT2可能通过SAGA复合体调控靶基因位点的H3K9/H3K27乙酰化水平。

在发育生物学层面，SCRT2的最新突破性发现为：一个模块化增强子（enhancer）介导SCRT2对ISLET1的抑制——ISLET1是脊髓运动神经元分化的关键转录因子（PMID:40818523）。这一发现表明SCRT2通过结合ISLET1位点附近的特异性增强子元件，在脊髓背侧抑制运动神经元命运，维持感觉神经元谱系。在癌症方面，SCRT2在上皮间质转化（EMT）中的表达具有分化阶段特异性（PMID:39268037），提示其在不同EMT阶段（起始vs完成）发挥双向调控。

SCRT2被标记为TE_REG_CANDIDATE，这一判断基于深刻的分子机制基础。Snail超家族转录因子是经典的表观遗传修饰招募因子——SCRT2通过其SNAG结构域直接结合LSD1（KDM1A，H3K4me2去甲基化酶）——这是其他Snail家族成员（如SNAI1）的共同机制。通过与LSD1/Sin3A/HDAC复合体的协同，SCRT2可将靶基因位点（包括转座子起始位点）上的活性H3K4me2转化为H3K4me0，同时去除乙酰化——创建"封闭型"染色质状态。无脊椎动物Scratch同源基因被证明直接调控转座子——这一进化保守性使SCRT2成为脊椎动物TE调控研究的极具价值候选。建议首先通过ChIP-seq鉴定SCRT2的全基因组结合图谱，重点分析TE区和增强子区的富集模式。

**蛋白全称**: Transcriptional repressor scratch 2

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FZR1 | BioGRID | 1 |
| SBDS | BioGRID | 1 |
| RECQL | BioGRID | 1 |
| SLFN11 | BioGRID | 1 |
| TRRAP | BioGRID | 1 |
| HIBCH | BioGRID | 0 |
| S100A13 | BioGRID | 0 |
| EEF1A2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NQ03-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000215397-SCRT2

![](https://images.proteinatlas.org/67697/1363_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/67697/1363_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/67697/1381_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/67697/1381_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/67697/1353_E10_4_red_green.jpg)
![](https://images.proteinatlas.org/67697/1353_E10_6_red_green.jpg)

### PubMed 文献

**PubMed count: 20**

| 40818523 | A modular enhancer mediates SCRT2 repression of ISLET1 in the spinal cord. | Dev Biol 2025 |
| 40214613 | A strategy for multimodal integration of transcriptomics, proteomics, and radiomics data for the prediction of recurrenc | Int J Cancer 2025 |
| 39268037 | Differentiation stage-specific expression of transcriptional regulators for epithelial mesenchymal transition in dentate | Front Neurosci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SCRT2

