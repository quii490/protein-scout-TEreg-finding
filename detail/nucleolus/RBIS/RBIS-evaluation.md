---
type: protein-evaluation
gene: "RBIS"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## RBIS 核蛋白评估报告
### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RBIS |
| 蛋白全称 | Ribosomal biogenesis factor |
| UniProt ID | Q8N0T1 |
| 蛋白大小 | 100 aa / 11.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Cytosol; Nucleoli; Nucleoplasm (Enhanced) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 100 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=78.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | RBIS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Trans-acting factor in ribosome biogenesis required for efficient 40S and 60S subunit production

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR031389 | RBIS |
| Pfam | PF15679 | DUF4665 |


#### 3.4 结构信息

蛋白长度 100 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR031389; |
| Pfam | PF15679; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMEM97 | STRING | 438 |
| CCDC117 | STRING | 436 |
| VPS26B | STRING | 400 |
| THYN1 | STRING | 425 |
| TMEM259 | STRING | 401 |
| LRRCC1 | STRING | 482 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000176731-RBIS

![](https://images.proteinatlas.org/44805/1443_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/44805/1443_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/44805/1516_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/44805/1516_E8_4_red_green.jpg)
![](https://images.proteinatlas.org/44805/1479_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/44805/1479_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/71903/1443_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/71903/1443_E6_3_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
★★★★  **71.6/100**  |  **nucleolus**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ribosomal biogenesis factor

**功能**: Trans-acting factor in ribosome biogenesis required for efficient 40S and 60S subunit production

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031389 |
| Pfam | PF15679 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N0T1-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 41**

| 41931495 | Reliability analysis of horseshoe tunnels by radial-based importance sampling method based on complex function displacem | PLoS One 2026 |
| 41763446 | The impact of alcohol consumption on frontal asymmetry and risk-taking. | Biol Psychol 2026 |
| 41053291 | Comparative Effectiveness of Human- and Robot-Based Interventions in Increasing Empathy Among Autistic Children. | J Autism Dev Disord 2025 |

### 深度机制分析

RBIS（100 aa, 11.0 kDa）是一个极小的核仁蛋白，属于核糖体生物合成因子，其结构域仅由单个RBIS结构域（IPR031389, DUF4665/PF15679）组成。100个氨基酸中几乎所有残基都包含在这个DUF4665结构域内，使RBIS成为罕见的"几乎全功能域"蛋白——几乎没有冗余序列。AlphaFold预测pLDDT=78.8，ESMFold独立从头折叠验证的平均pLDDT为0.59，两个预测方法的一致性表明该小蛋白确实具有相对有序的折叠核心，但26.0%残基的pLDDT低于0.5提示部分区域仍高度柔性。

功能上，RBIS是核糖体生物合成的反式作用因子，对40S和60S核糖体亚基的高效产生必需。作为"核糖体组装因子"，RBIS可能在pre-rRNA加工、核糖体蛋白组装或核仁内亚基前体的质量控制中发挥辅助作用。RBIS在胞质、核质和核仁的三重定位（HPA Enhanced级别）与其核糖体生物合成功能完美契合——核仁是rRNA转录和初始加工场所，核质中完成后续组装步骤，胞质中参与翻译调控。

PPI网络鉴定了与TMEM97（STRING 438）、CCDC117（STRING 436）、VPS26B（逆转运复合体，STRING 400）、THYN1（STRING 425）和LRRCC1（STRING 482）的互作。其中VPS26B是retromer复合体亚基维持内体-高尔基体运输，与核糖体生物合成蛋白的关联令人意外；LRRCC1含有亮氨酸富集重复序列，可能作为核仁内蛋白质质量控制的适配器。

在TE调控方面，RBIS主要通过核糖体生物合成和翻译调控间接影响TE表达，而非直接参与染色质/TE沉默。核糖体应激（ribosomal stress）可触发核仁-核质信号通路，包括RPL5/RPL11介导的MDM2扣押和p53激活，这可能改变转座子位点的表观遗传景观。但RBIS本身不含有已知的DNA/RNA结合域或染色质修饰结构域，其TE调控角色可能局限为特定TE编码蛋白翻译效率的全局调控器。由于蛋白极小而功能高度专一，将RBIS作为TE调控的直接靶点开发可能空间有限，但其作为核糖体生物合成标记物在监测TE去抑制相关的翻译重编程中可能具有应用价值。文献稀缺（PubMed=5），提示极具研究新颖性。

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RBIS_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.59 |
| pLDDT > 0.9 | 0.0% |
| pLDDT < 0.5 | 26.0% |
| 残基数 | 100 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

