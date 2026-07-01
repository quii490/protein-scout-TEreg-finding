---
type: protein-evaluation
gene: "SMIM2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SMIM2 (Small integral membrane protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SMIM2 |
| 蛋白全称 | Small integral membrane protein 2 |
| UniProt ID | Q9BVW6 |
| 蛋白大小 | 85 aa / 9.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 85 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 3/10 | x2 | 6.0 | 无已知结构域 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **110/180** | |
| **归一化总分 (/1.83)** | | | **60.1/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 2

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 2

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---

### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 2

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000139656-SMIM2
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/77071/1759_H3_33_red_green.jpg)
![](https://images.proteinatlas.org/77071/1759_H3_36_red_green.jpg)
![](https://images.proteinatlas.org/77071/1822_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/77071/1822_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/77071/1791_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/77071/1791_A5_2_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBQLN1 | BioGRID | 0 |
| UBQLN2 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SMIM2

### PubMed

**Count: 2**

| PMID | Title |
|---|---|
| 38482248 | Construction and validation of a prognostic signature for mucinous colonic adenocarcinoma based on N7-methylguanosine-related long non-coding RNAs. |
| 34527442 | Cut-off points to screening for sarcopenia in community-dwelling older people residents in Brazil. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SMIM2_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.47 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 81.2% |
| 建模残基数 | 85 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

SMIM2（Small integral membrane protein 2）是本次评估的24个蛋白中数据质量最差的一个。该蛋白仅85个氨基酸（9.3 kDa），是典型的微蛋白（microprotein），可能因其体积过小而常被常规基因注释流程遗漏。最关键的问题出现在结构域分析层面：InterPro、Pfam、SMART和UniProt Domain注释均未检出任何已知结构域（报告中结构域表格为空白），这意味着其序列在已知蛋白家族数据库中无任何同源性匹配。ESMFold预测进一步强化了这一困境——全局pLDDT仅0.47（在所有评估蛋白中最低），81.2%的残基pLDDT<0.5，且高置信残基（pLDDT>0.9）占比为0%。这种极低的结构置信度可能有三种解释：(1)该蛋白在生理条件下以完全无序状态存在；(2)序列中存在未知的折叠拓扑，超出了现有结构预测模型的训练范围；(3)该基因编码的蛋白质产物可能缺少稳定的三维结构。

PPI互作网络的BioGRID数据同样贫乏：仅有两个互作伙伴（UBQLN1和UBQLN2），且评分均为0的最低置信度。UBQLN1/2属于ubiquilin家族，是泛素-蛋白酶体通路中的穿梭蛋白，负责将多泛素化底物递送至蛋白酶体降解。这两个蛋白出现在SMIM2的互作谱中可能有两种解释——SMIM2作为真正的互作伙伴被UBQLN识别并递送降解，或者SMIM2作为膜蛋白在异源表达系统中与UBQLN蛋白产生非特异性结合（后者在仅85aa的小蛋白中更为可能）。此外，PubMed仅收录2篇文献，且均与SMIM2本身无关——一篇为基于N7-甲基鸟苷相关lncRNA的粘液性结肠腺癌预后模型构建（PMID 38482248），另一篇为巴西社区老年人肌少症筛查切点研究（PMID 34527442），两者均仅在文献的基因列表中提及SMIM2，无任何直接功能研究。

尽管如此，HPA IF图像数据显示SMIM2在nucleoplasm和nuclear bodies中具有可检测的免疫荧光信号，这一观察与本评估项目的筛选标准一致。但这种"核定位"可能存在技术性误导：(1) 85aa的小蛋白可能通过自由扩散进入细胞核（<40kDa蛋白通常可被动穿过核孔复合体），无需主动核定位信号；(2) IF信号可能来自抗体与核内类似序列蛋白的交叉反应——小蛋白的抗体特异性通常更难保证；(3) 缺乏细胞分馏实验的独立验证，IF信号不能作为功能性核定位的充分证据。

综合来看，SMIM2目前不适合作为TE调控候选蛋白进行深入研究。推荐等级2/5（60.1/100）是所有评估蛋白中最低的之一。该蛋白的深度机制模型实际上不存在——缺乏已知结构域意味着无法推断其分子功能，PPI数据不足无法构建互作网络，极低的结构置信度限制了对三级结构的理解，且文献完全缺乏。建议在继续推进前完成：(1)确认该基因是否真正翻译为稳定蛋白产物（mass spectrometry validation）；(2)明确其膜拓扑和可能的细胞器定位；(3)寻找条件特异性表达或互作数据。



- UniProt: https://www.uniprot.org/uniprotkb/Q9BVW6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVW6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMIM2
