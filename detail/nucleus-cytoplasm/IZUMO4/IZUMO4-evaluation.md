---
type: protein-evaluation
gene: "IZUMO4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## IZUMO4 (Izumo sperm-egg fusion protein 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | IZUMO4 |
| 蛋白全称 | Izumo sperm-egg fusion protein 4 |
| UniProt ID | Q1ZYL8 |
| 蛋白大小 | 232.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 232 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR029389, IPR052868, PF15005|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=4 |
| **加权总分** | | | **76/180** | |
| **归一化总分 (÷1.83)** | | | **41/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Secreted + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: IZUMO4 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Secreted + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

Izumo family, fertilization。

#### 3.3 PPI 网络

PPI degree=4。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

IZUMO4 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR029389 |
| InterPro | IPR052868 |
| Pfam | PF15005 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR029389;IPR052868; |
| Pfam | PF15005; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000099840-IZUMO4

![](https://images.proteinatlas.org/48496/2204_H3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/48496/2204_H3_20_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TEX101 | BioGRID | 0 |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/IZUMO4_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.49 |
| pLDDT > 0.9 | 0.0% |
| pLDDT < 0.5 | 53.4% |
| 残基数 | 232 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 深度机制分析

IZUMO4属于Izumo精子-卵融合蛋白家族，其深度机制分析需置于受精生物学的框架中。该蛋白含有一个Izumo domain（InterPro:IPR029389, Pfam:PF15005），这是一个以免疫球蛋白样β-三明治折叠为核心的蛋白互作模块，在Izumo家族中高度保守。ESMFold预测显示了极差的结构置信度——全局pLDDT仅0.49(在所有24个评估蛋白中倒数第二），53.4%残基pLDDT<0.5，且高置信残基占比为0%。这种广泛的结构无序可能并非技术性预测失败——在受精相关的膜表面蛋白中，免疫球蛋白样结构域通常需要与配体结合后才能稳定其折叠状态。IZUMO4类似其家族成员IZUMO1，可能在与卵表面受体（如JUNO）结合时经历显著的折叠耦合，单独存在时保持部分无序的"开放"构象。

然而，IZUMO4与IZUMO1在功能层级上存在差异。IZUMO1已在遗传学和生物化学层面被确认为哺乳动物精卵融合的核心因子——IZUMO1敲除雄性小鼠完全不育，其与卵表面JUNO受体的识别是物种特异性受精的关键步骤。IZUMO4的功能角色相对不明确，可能作为Izumo家族的辅助成员参与精子膜蛋白复合体的组装或精卵融合的调控，而非核心融合因子。

PPI互作网络的质量极差——BioGRID仅收录1个互作伙伴TEX101（score=0）。TEX101（Testis-expressed protein 101）是一种GPI锚定的精子膜蛋白，定位于精子表面，与IZUMO1存在直接互作（在精子成熟过程中TEX101被切割并释放）。IZUMO4与TEX101的互作可能反映了IZUMO家族蛋白在精子膜上的共定位或复合体组装。PPI degree=4的极低连通性（主要是STRING预测的弱链接）表明IZUMO4在现有的互作组学数据中几乎不可见。

在核定位方面，UniProt的GO-CC将IZUMO4注释为"Secreted + Nucleus"——这是一个需要深入讨论的矛盾定位。作为精子膜蛋白，IZUMO4的核心功能必然发生于细胞表面（精卵识别与融合），而GO中的"Nucleus"注释可能来源于将非特异性核染色信号误判为功能性核定位的自动注释流程。HPA明确返回hpa_nuclear=False，支持核信号的缺失。此外，IZUMO4的Izumo结构域不具备任何DNA结合能力或染色质关联功能。PubMed几乎无直接功能研究（PMID 21630460等），在研究新颖性评分为5/10（unclassified_bare来源）。综合来看，推荐等级2/5（41/100）是合理的。深度机制模型为：精子膜上的IZUMO4→Izumo域维持部分无序构象→与TEX101或Izumo家族成员共定位→可能的精卵融合辅助功能。这一模型与TE调控完全无关，无任何核内功能的分子基础。



- UniProt: https://www.uniprot.org/uniprotkb/Q1ZYL8
- HPA: https://www.proteinatlas.org/
