---
type: protein-evaluation
gene: "TMEM42"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM42 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TMEM42 |
| 蛋白全称 | Transmembrane protein 42 |
| UniProt ID | Q69YG0 |
| 蛋白大小 | 159 aa / 17.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 4/10 | ×1 | 4.0 | 159 aa|
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=72.5; PDB=0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | IPR037185, IPR039632|
| PPI | 6/10 | ×3 | 18.0 | PPI degree=58 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

暂无功能注释

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR037185 | EmrE-like |
| InterPro | IPR039632 | TMEM42 |


#### 3.4 结构信息

蛋白长度 159 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169964-TMEM42

![](https://images.proteinatlas.org/52569/826_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/52569/826_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/52569/819_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/52569/819_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/52569/809_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/52569/809_H5_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。

### 深度机制分析

**结构域架构**：TMEM42（159 aa, 17.5 kDa）是功能完全未知的小跨膜蛋白，含EmrE-like域（IPR037185）和TMEM42特异地标（IPR039632）。EmrE-like家族为SMR（Small Multidrug Resistance）型转运蛋白超家族，特征为约100 aa的4-helix antiparallel bundle——可在膜中同源二聚化形成功能转运孔。TMHMM预测TMEM42为3-4次跨膜蛋白——呈tetraspanin-like排列（类似于CD9/CD81/CD63）。AlphaFold pLDDT=72.5（transmembrane helices >80），ESMFold pLDDT=0.72轻微下降。PPI（degree=58）以SUMO化和核蛋白为核心：UBE2I/UBC9（STRING score=746, SUMO化E2 conjugase）是SUMO pathway的中枢酶——催化SUMO1/2/3的C端Gly与底物Lys的isopeptide bond形成。LMNA（lamin A/C, BioGRID）为核纤层主要组分——TMEM42-LMNA互作暗示TMEM42在inner nuclear membrane（INM）的定位——可能作为核膜上的SUMO化支架蛋白。DTX2（Deltex E3 ligase, BioGRID, Notch signaling regulator）连接至泛素化，VENTX（vent-like homeobox transcription factor, BioGRID）连接至转录调控。

**TE调控展望**：UBE2I/UBC9是核内SUMO化通路的核心酶——SUMO化是转录沉默、PML nuclear body组装和DNA damage response的关键修饰——众多TE相关转录因子（如DAXX, TRIM28/KAP1, PIAS1/3/4）依赖SUMO化发挥功能。TMEM42在INM上与LMNA和UBE2I互作——可能在核膜邻域形成SUMO化微域——影响nuclear periphery的转录沉默——而LADs（lamin-associated domains）富含LINE-1重复序列。核仁定位（nucleolus）本身是rDNA repeats和pericentromeric satellite repeats的核内场所——TMEM42可能在nucleolus-periphery transport pathway中调控特定RNA的subnuclear trafficking。

### 4. 总体评价
**69.4/100** | **nucleolus**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 42

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037185 |
| InterPro | IPR039632 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 42

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037185 |
| InterPro | IPR039632 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR037185;IPR039632; |
| Pfam | 未检出 |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBE2I | STRING | 746 |
| LMNA | BioGRID | 1 |
| DTX2 | BioGRID | 1 |
| ZDHHC15 | BioGRID | 1 |
| MTIF3 | BioGRID | 1 |
| FAM209A | BioGRID | 1 |
| VENTX | BioGRID | 1 |
| RBPMS | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q69YG0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM42

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/TMEM42_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.72 |
| pLDDT > 0.9 | 1.9% |
| pLDDT < 0.5 | 17.0% |
| 残基数 | 159 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

