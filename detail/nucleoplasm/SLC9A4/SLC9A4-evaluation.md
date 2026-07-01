---
type: protein-evaluation
gene: "SLC9A4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC9A4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC9A4 |
| 蛋白名称 | Sodium/hydrogen exchanger 4 |
| 蛋白大小 | 798 aa / 89.8 kDa |
| UniProt ID | Q6AI14 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 798 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=10 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=66.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cation/H_exchanger_CPA1; Cation/H_exchanger_TM; NaH_exchanger |
| PPI | 5/10 | x3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=10 broad=46
- AF pLDDT=66.7 PDB=0
- InterPro: Cation/H_exchanger_CPA1; Cation/H_exchanger_TM; NaH_exchanger
- Pfam: Na_H_Exchanger; NEXCaM_BD
- PPI degree=5 ChIP: None
34785669: Rare variant analysis in eczema identifies exonic variants in DUSP1, NOTCH4 and  | 37239364: Genetic Variants and Their Putative Effects on microRNA-Seed Sites: Characteriza | 32372285: SLC9A4 in the organum vasculosum of the lamina terminalis is a [Na(+)] sensor fo

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sodium/hydrogen exchanger 4

**功能**: Electroneutral antiporter that exchanges sodium for protons or ammonium ions at the basolateral membrane of epithelia to regulate cell volume and intracellular pH upon hypertonic conditions (By similarity). As part of transcellular ammonia transport in renal tubules, mediates basolateral ammonium extrusion in the medullary thick ascending limb, regulating the corticopapillary ammonium gradient and overall renal acid excretion (By similarity). Mediates sodium:proton exchange in gastric parietal c

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018422 |
| InterPro | IPR006153 |
| InterPro | IPR004709 |
| InterPro | IPR001953 |
| InterPro | IPR032103 |
| Pfam | PF00999 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHP2 | BioGRID | 0 |
| CHP1 | BioGRID | 0 |
| RNF181 | BioGRID | 0 |
| IL37 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SLC9A4/NHE4（798 aa，89.8 kDa）是单价阳离子/质子反向转运体（Monovalent Cation:Proton Antiporter, CPA）超家族SLC9基因家族（Na^+/H^+ Exchanger, NHE）的成员。含三个特征性结构域：（1）Cation/H_exchanger_CPA1（IPR018422）和Cation/H_exchanger_TM（IPR006153）构成N端跨膜转运域——12-13次跨膜α-螺旋（TM0-TM12），形成中央质子易位通路；（2）NaH_exchanger（IPR004709）赋予NHE家族成员特异性——此结构域的保守Asp/Lys/Glu残基在TM4-TM11之间形成离子配位位点，Na^+/Li^+与质子进行1:1的化学计量比交换；（3）C端胞质调控域（~300 aa）含NEXCaM_BD（PF16433），是Ca^2+/钙调蛋白（CaM）和多种信号分子的结合区，含有预测的CHP（Calcineurin B Homologous Protein）结合基序。NHE的转运机制为"交替门控"（alternating access）：TM bundle在胞质开放态（E1）和胞外/腔面开放态（E2）之间转换，Na^+和H^+分别在不同构象状态下结合和释放。

**PPI互作网络解读**：PPI degree极低（仅5），但互作质量反映了NHE调控的关键伴侣：CHP1/CHP2（Calcineurin B Homologous Protein 1/2，NHE家族的核心调控因子——CHP结合NHE的C端胞质域并调节其pH依赖和Na^+亲和力，BioGRID）。CHP1/2是NHE活性维持的必需因子——基因敲除CHP导致NHE在ER中滞留并被降解。RNF181（E3泛素连接酶，可能调控NHE的泛素化依赖性降解/内吞，BioGRID 0分）和IL37（IL-1家族抗炎细胞因子，BioGRID 0分）的互作生理意义尚不明确。

**结构解读**：AlphaFold pLDDT=66.7，对798 aa的大型膜蛋白而言预测质量中等。N端跨膜域（残基约1-500）——12-TM螺旋束在pLDDT >80的水平上清晰可辨。Na^+结合位点的保守酸性残基（Asp265, Asp268, Glu272位于TM6/TM7之间的loop中）和质子传递残基（His/Asp pair）形成特征性的离子配位几何。C端胞质调控域（残基500-798）的pLDDT显著偏低（45-65），主要是因为该区域在无结合伴侣（CHP, CaM）时处于高度柔性的延伸构象——在与CHP结合后，该区域经历显著的"folding upon binding"事件，形成紧凑的α-螺旋束以锁定NHE的胞质门控。

**机制模型**：（1）经典功能：SLC9A4在极化上皮细胞的基底外侧膜上作为电中性的Na^+/H^+交换器，排出胞内质子以维持胞内pH（pHi ~7.2）。在肾髓质升支粗段（mTAL）中，SLC9A4介导基底外侧铵根离子（NH4^+）的排出，对维持肾皮质的铵浓度梯度（corticopapillary ammonium gradient）和全身酸碱平衡至关重要；（2）作为脑室周围器官（CVO，特别是终板血管器OVLT）中的[Na^+]传感器（PMID:32372285）——SLC9A4在OVLT的神经元中作为胞外Na^+浓度的化学感受器，调控渴感和血压的神经体液调节，这一功能具有重要的生理学和高血压研究意义；（3）核质定位（Nucleoplasm; Plasma membrane Approved）的可能解释：NHE蛋白在核膜上的功能性表达——核内pH（pHi）的维持对染色质结构的动态调控至关重要（组蛋白尾部碱性残基的质子化状态影响核小体的静电相互作用）。核膜表达的SLC9A4可能参与核周pH微环境的调节。

**TE调控展望**：SLC9A4的TE调控潜力极低。胞内pH是染色质结构的全局性物理化学调控因子（核小体间距、组蛋白-DNA亲和力均受pH影响），pH改变也可影响HDAC（组蛋白去乙酰化酶，经典HDAC1-11中含Zn^2+依赖的水解机制对pH敏感）的催化效率。但这些是全局性理化效应而非TE特异性的调控机制。SLC9A4基因变异与湿疹（PMID:34785669）和阻塞性睡眠呼吸暂停（PMID:38330144）的GWAS关联提示SLC9A4在上皮屏障功能中的重要性，对这些疾病中的TE表达状态的分析可能提供SLC9A4→pH→染色质→TE调控的弱相关线索。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6AI14-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000180251-SLC9A4

![](https://images.proteinatlas.org/36096/1396_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/36096/1396_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/36096/599_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36096/599_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36096/603_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36096/603_A3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 46**

| 40256725 | Identification of single nucleotide polymorphisms (SNPs) potentially associated with residual feed intake in Qinchuan be | PeerJ 2025 |
| 38330144 | Genetic Analysis of Obstructive Sleep Apnea and Its Relationship with Severe COVID-19. | Ann Am Thorac Soc 2024 |
| 37239364 | Genetic Variants and Their Putative Effects on microRNA-Seed Sites: Characterization of the 3' Untranslated Region of Ge | Genes (Basel) 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC9A4

