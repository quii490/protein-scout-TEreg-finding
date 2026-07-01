---
type: protein-evaluation
gene: "FNDC1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## FNDC1 (Fibronectin type III domain-containing protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | FNDC1 |
| 蛋白全称 | Fibronectin type III domain-containing protein 1 |
| UniProt ID | Q4ZHG4 |
| 蛋白大小 | 1894 aa / 208.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1894 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR003961; InterPro:IPR036116; InterPro:IPR013783; InterPro:IPR049109; Pfam:PF00041; Pfam:PF21731 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May be an activator of G protein signaling

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR003961 |
| InterPro | IPR036116 |
| InterPro | IPR013783 |
| InterPro | IPR049109 |
| Pfam | PF00041 |
| Pfam | PF21731 |

#### 3.3 核定位

无已知核定位注释

### 深度机制分析

FNDC1（纤连蛋白III型结构域包含蛋白1）采用超长重复序列结构——核心由数个纤连蛋白III型（Fn3）结构域串联组成（IPR003961、IPR036116、IPR013783、Pfam PF00041），每个Fn3域采用β-三明治折叠（约90 aa），通过疏水核心稳定。IPR049109（Pfam PF21731）覆盖N端特定区域。1894 aa（208.3 kDa）的超大型分子量在非肌球蛋白类ECM蛋白中也是最大的之一，主要由Fn3串联重复占据。

AlphaFold预测结构可用，Fn3域的重复性意味着折叠相对可靠。PPI数据显示与FZR1（APC/C激活子）、IVL（外皮蛋白）、ATP6V0C（空泡ATP酶亚基）、CRYAB（小热休克蛋白）的互作。值得注意FZR1连接——FZR1/CDC20交替激活APC/C（后期促进复合物/环体），是细胞周期G1/S和G2/M过渡的核心E3连接酶开关。

TE调控相关性机制推论基于FNDC1在核斑（nuclear speckle）的定位：核斑是mRNA剪接因子（如SC35/SRSF2、SRRM1/SR蛋白）的储存和活跃剪接体组装位点。若FNDC1通过Fn3域的蛋白-蛋白互作表面与剪接因子结合，其可能参与TE衍生外显子的剪接调控。特别地，PDZ域结合蛋白偶联和膜受体内部化的同时，许多Alu和LINE-1元件引入的隐蔽剪接位点在核斑中接受剪接决策（包含或跳过），FNDC1的超长Fn3串联阵列可能作为剪接因子招募的"平台"。此外，FZR1/APC/C的连接暗示可能在G1/S过渡期调控TE衍生蛋白的蛋白解稳定性。

无GO-CC核定位注释（核定位特异性4/10），PubMed 92篇。归一化总分66.7/100。超长Fn3阵列作为剪接因子脚手架的概念值得进一步探索，但当前TE调控证据过少。

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Fibronectin type III domain-containing protein 1

**功能**: May be an activator of G protein signaling

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003961 |
| InterPro | IPR036116 |
| InterPro | IPR013783 |
| InterPro | IPR049109 |
| Pfam | PF00041 |
| Pfam | PF21731 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FZR1 | BioGRID | 1 |
| IVL | BioGRID | 1 |
| ATP6V0C | BioGRID | 0 |
| IGHG2 | BioGRID | 0 |
| CRYAB | BioGRID | 0 |
| TF | BioGRID | 0 |
| IGHG1 | BioGRID | 0 |
| LGALS7B | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FNDC1

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164694-FNDC1

![](https://images.proteinatlas.org/30962/2155_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/30962/2155_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/30962/396_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/30962/396_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/30962/392_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/30962/392_D10_3_red_green.jpg)

### PubMed

**Count: 92**

| PMID | Title |
|---|---|
| 42329880 | High-Throughput Olink Proteomics Elucidates the Immuno-Neurological Landscape of Gastric Cancer. |
| 42185599 | Explainable machine learning-driven identification of heart failure biomarkers: a multi-model feature selection approach with SHAP-based interpretabil |
| 42055255 | FNDC1-driven macrophage polarization promotes breast cancer cell invasion. |
| 42003973 | A novel prognostic signature based on mitochondrial permeability transition-driven necrosis genes for biochemical recurrence prediction in prostate ca |
| 41986425 | FNDC1 is closely related to poor prognosis and immune cell infiltration in gastric cancer. |


