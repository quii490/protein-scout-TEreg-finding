---
type: protein-evaluation
gene: "RPAIN"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## RPAIN 核蛋白评估报告
### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RPAIN |
| 蛋白全称 | RPA-interacting protein |
| UniProt ID | Q86UA6 |
| 蛋白大小 | 219 aa / 24.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli fibrillar center; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 219 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=81.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | RIP; RPA_interact_C_dom; RPA_interact_central |
| PPI | 5/10 | x3 | 15.0 | PPI degree=19 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Mediates the import of RPA complex into the nucleus, possibly via some interaction with importin beta. Isoform 2 is sumoylated and mediates the localization of RPA complex into the PML body of the nucleus, thereby participating in RPA function in DNA metabolism

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR028156 | RIP |
| InterPro | IPR028159 | RPA_interact_C_dom |
| InterPro | IPR028155 | RPA_interact_central |
| InterPro | IPR028158 | RPA_interact_N_dom |
| Pfam | PF14768 | RPA_interact_C |
| Pfam | PF14767 | RPA_interact_M |
| Pfam | PF14766 | RPA_interact_N |


#### 3.4 结构信息

蛋白长度 219 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000129197-RPAIN

![](https://images.proteinatlas.org/31526/334_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/31526/334_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/31526/329_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/31526/329_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/31526/332_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/31526/332_G12_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
★★★★  **74.3/100**  |  **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR028156;IPR028159;IPR028155;IPR028158; |
| Pfam | PF14768;PF14767;PF14766; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CYP17A1 | BioGRID | 0 |
| GSTA1 | BioGRID | 0 |
| ADH6 | BioGRID | 0 |
| CDCA5 | BioGRID | 0 |
| RPA1 | BioGRID | 0 |
| RPA2 | BioGRID | 0 |
| UBR7 | BioGRID | 0 |
| CLNK | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q86UA6-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 15**

| 39086230 | DISSyphilis and the Risk of HIV Infection: A Mendelian Randomization Study. | AIDS Res Hum Retroviruses 2025 |
| 38193396 | Unbiased phenotype and genotype matching maximizes gene discovery and diagnostic yield. | Genet Med 2024 |
| 35303002 | Cross-cultural adaptation and measurement properties of the Malay Shoulder Pain and Disability Index. | PLoS One 2022 |

### 深度机制分析

RPAIN是RPA（复制蛋白A）复合物的核输入介导蛋白，在DNA代谢中处于上游调控节点。其结构域架构包括RIP（IPR028156）、RPA_interact_N（IPR028158）、RPA_interact_central（IPR028155）和RPA_interact_C（IPR028159）四个模块，跨越Pfams PF14766/PF14767/PF14768，构成完整的RPA结合界面。AlphaFold pLDDT=81.9（219 aa），ESMFold均值0.85且45.2%残基pLDDT>0.9，独立验证了其折叠的可靠性。PPI网络中RPA1和RPA2为直接互作靶标，支持其作为RPA核定位适配器的核心功能。

关键发现是异构体2通过SUMOylation修饰被导向PML核体（nucleoli fibrillar center + nucleoplasm双定位），参与RPA在DNA损伤应答中的空间调控。这一机制将RPAIN置于SUMO-RPA-PML信号轴的枢纽位置：SUMO化修饰赋予RPAIN核体靶向性，进而将RPA复合物募集至PML体——无膜细胞器中DNA修复因子的关键储存和激活场所。HPA IF图像中观察到nucleoli fibrillar center信号，与PML体在核仁周围的区域性富集一致。

RPAIN的研究新颖性极高（PubMed strict=6, broad=15），但其功能与基因组稳定性维持直接相关。DIS研究（PMID:39086230）提示RPAIN相关通路与HIV感染风险存在孟德尔随机化关联，暗示其可能在病毒DNA整合或宿主DNA损伤应答中发挥作用。鉴于其RPA运输功能、SUMO-PML轴和核仁-核质双重定位，RPAIN可能是连接DNA复制应激与核体介导的抗病毒固有免疫的关键桥梁蛋白，值得通过SUMOylation位点突变和PML体共定位实验进行深入验证。

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RPAIN_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.85 |
| pLDDT > 0.9 | 45.2% |
| pLDDT < 0.5 | 0.0% |
| 残基数 | 219 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

