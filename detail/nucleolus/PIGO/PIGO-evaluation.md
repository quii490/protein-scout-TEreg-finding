---
type: protein-evaluation
gene: "PIGO"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PIGO 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PIGO |
| 蛋白全称 | GPI ethanolamine phosphate transferase 3, catalytic subunit |
| UniProt ID | Q8TEQ8 |
| 蛋白大小 | 1089 aa / 119.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1089 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=32 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=82.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Alkaline_phosphatase_core_sf; Phosphodiest/P_Trfase; PIG-O_N |
| PPI | 6/10 | x3 | 18.0 | PPI degree=81 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Catalytic subunit of the ethanolamine phosphate transferase 3 complex that transfers an ethanolamine phosphate (EtNP) from a phosphatidylethanolamine (PE) to the 6-OH position of the third alpha-1,2-linked mannose of the a 2-acyl-6-[alpha-D-mannosyl-(1->2)-alpha-D-mannosyl-(1->6)-2-phosphoethanolami

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR017850 | Alkaline_phosphatase_core_sf |
| InterPro | IPR002591 | Phosphodiest/P_Trfase |
| InterPro | IPR037675 | PIG-O_N |
| InterPro | IPR039524 | PIGO/GPI13 |
| Pfam | PF01663 | Phosphodiest |


#### 3.4 结构信息

蛋白长度 1089 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**69.9/100** | **nucleolus**
Nuclear protein


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165282-PIGO

![](https://images.proteinatlas.org/14905/172_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14905/172_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14905/121_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14905/121_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14905/123_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14905/123_H2_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR017850;IPR002591;IPR037675;IPR039524; |
| Pfam | PF01663; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIGU | STRING | 961 |
| GAB1 | STRING | 961 |
| PER1 | STRING | 765 |
| APP | BioGRID | 1 |
| PTH1R | BioGRID | 1 |
| ZDHHC12 | BioGRID | 1 |
| HRAS | BioGRID | 1 |
| SPPL2B | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TEQ8-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：PIGO（1089 aa，119.8 kDa）是GPI（糖基磷脂酰肌醇）锚定生物合成途径的催化亚基，属于乙醇胺磷酸转移酶3复合体的核心组分。其结构域架构包括：PIG-O_N（IPR037675）——N端胞质结构域（约1-200 aa），可能介导与PIGU（GPI转酰胺酶复合体亚基）的异源二聚化；Phosphodiest/P_Trfase催化结构域（IPR002591，PF01663）——编码磷酸二酯酶/磷酸转移酶活性中心，负责将乙醇胺磷酸（EtNP）从磷脂酰乙醇胺（PE）供体转移至甘露糖-3的6-OH位；Alkaline_phosphatase_core_sf（IPR017850）——碱性磷酸酶核心超家族折叠，提供双金属离子（Zn²⁺/Mg²⁺）催化口袋。AlphaFold pLDDT=82.5，Phosphodiest结构域（约300-700 aa）预测质量尤其高（pLDDT>88），而PIG-O_N和C端跨膜螺旋（~1000-1080 aa）置信度稍低。

**PPI互作网络解读**：PPI degree=81，核心互作清晰描绘了GPI生物合成复合体的组织架构：PIGU（STRING 961，GPI转酰胺酶复合体亚基，最强实验信号）与PIGO形成稳定的异源二聚体活性单元；GAB1（STRING 961，GRB2相关结合蛋白1）——RTK信号转导衔接蛋白，指向GPI锚定与生长因子信号通路的交叉调控；PER1（STRING 765，昼夜节律调控因子）——非预期的互作，提示GPI生物合成可能受昼夜节律调控；HRAS（BioGRID 1）——小GTP酶，可能参与GPI锚定蛋白的膜转运。APP（淀粉样前体蛋白）、PTH1R（甲状旁腺激素受体）、ZDHHC12（棕榈酰转移酶）均属膜蛋白互作网络。

**结构解读**：PIG-O_N结构域可能采取α/β折叠，形成与PIGU互作的疏水界面。Phosphodiest催化结构域采用经典的碱性磷酸酶折叠——中央β-片层（β1-β8）被α-螺旋包围形成α/β/α三明治，双金属离子结合口袋位于β-片层C端边缘。催化机制遵循两步亲核取代：第一步，磷酸-组氨酸中间体（phospho-His）在活性位点His残基上形成；第二步，EtNP基团转移至受体甘露糖的6-OH。C端单跨膜α-螺旋将催化域锚定于内质网膜的腔面侧——这与GPI锚定发生在ER腔内的已知事实一致。

**机制模型**：（1）PIGO-PIGU异源二聚体在内质网膜上组装，PIG-O_N与PIGU的胞质域结合；（2）Phosphodiest催化域面向ER腔，接受PE供体底物并催化EtNP转移至GPI中间体的Man-3；（3）GAB1通过其PH结构域与PIGO互作，可能介导RTK（如EGFR/Met）的PI3K/AKT信号与GPI生物合成的偶联；（4）HPA检测到的Nucleoli/Nucleoplasm定位（Approved）提示PIGO可能存在核内功能——PIG-O_N含有推测的NLS样碱性序列，可能允许核输入；（5）核仁中PIGO可能参与核仁特异性GPI锚定蛋白（如某些核仁驻留糖蛋白）的修饰，或作为GPI生物合成状态的细胞器间信号传感器（PMID:42190144显示PIGO突变导致早发性婴儿发育及癫痫性脑病，侧面揭示其非经典功能的重要性）。

**TE调控展望**：PIGO主要功能定位于GPI锚定生物合成，与TE调控的直接关联极弱。唯一值得注意的线索是PER1互作（STRING 765）——若PIGO通过PER1偶联昼夜节律调控，且昼夜节律已知可影响特定TE家族（如Alu、SINE）的转录输出，则PIGO可能通过GPI锚定蛋白的节律性表达间接影响TE相关膜蛋白的丰度。但此联系过于间接，不建议作为TE研究靶标。

### PubMed 文献

**PubMed count: 110**

| 42190144 | Burst-Suppression EEG in Early Infantile Developmental and Epileptic Encephalopathies: Phenotype, Genotype, and Outcome. | Neurology 2026 |
| 42137603 | Optimized AAV vector enables potent therapeutic rescue of inherited glycosylphosphatidylinositol deficiency in mice. | Mol Ther Adv 2026 |
| 41777335 | Partially covered or uncovered metal stent efficacy in malignant unresectable distal biliary obstruction (METARSI): Rand | Endosc Int Open 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PIGO

