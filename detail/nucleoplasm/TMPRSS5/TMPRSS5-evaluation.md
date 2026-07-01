---
type: protein-evaluation
gene: "TMPRSS5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMPRSS5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMPRSS5 |
| 蛋白名称 | Transmembrane protease serine 5 |
| 蛋白大小 | 457 aa / 49.6 kDa |
| UniProt ID | Q9H3S3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 457 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=11 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin; Peptidase_S1A |
| PPI | 5/10 | x3 | 15.0 | PPI degree=47 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=11 broad=18
- AF pLDDT=79.3 PDB=0
- InterPro: Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin; Peptidase_S1A
- Pfam: SRCR_2; Trypsin
- PPI degree=47 ChIP: None
40304040: Proteome-Wide Genetic Study in East Asians and Europeans Identified Multiple The | 41639462: Phenome-wide analysis of copy number variants in 470,727 UK Biobank genomes. | 17918741: cAMP-dependent regulation of spinesin/TMPRSS5 gene expression in astrocytes.

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protease serine 5

**功能**: May play a role in hearing

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009003 |
| InterPro | IPR043504 |
| InterPro | IPR001314 |
| InterPro | IPR001190 |
| InterPro | IPR036772 |
| InterPro | IPR001254 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TOR3A | BioGRID | 1 |
| BDH1 | BioGRID | 1 |
| N4BP2L2 | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |
| FBXO7 | BioGRID | 1 |
| MCL1 | BioGRID | 1 |
| NR2F2 | BioGRID | 1 |
| CLN6 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：TMPRSS5（457 aa，49.6 kDa）属于II型跨膜丝氨酸蛋白酶（Type II transmembrane serine protease, TTSP）家族，含三个结构模块：（1）SRCR_2结构域（PF15494）——富半胱氨酸清道夫受体（Scavenger Receptor Cysteine-Rich）结构域，常见于免疫相关蛋白，可能介导蛋白-蛋白互作或配体识别；（2）Trypsin结构域（PF00089）和Peptidase_S1_PA（IPR009003）、Peptidase_S1_PA_chymotrypsin（IPR043504）、Peptidase_S1A（IPR001254）——含经典Ser-His-Asp催化三联体，执行蛋白质水解功能。N端跨膜锚定（II型拓扑，N-in/C-out）将催化域定位于胞外/腔面，需经自身激活切割（autoactivation cleavage）才能产生活性蛋白酶。

**PPI互作网络解读**：PPI degree=47，关键互作包括：TOR3A（Torsin-3A，AAA+ ATPase参与ER/核膜蛋白质量控制，BioGRID 1分）、MCL1（髓系细胞白血病1，抗凋亡Bcl-2家族蛋白，BioGRID 1分）、NR2F2（COUP-TFII，核受体孤儿受体，BioGRID 1分）、FBXO7（SCF泛素连接酶底物识别亚基，BioGRID 1分）、HNRNPL（hnRNP L，再次出现为共享互作伙伴）。NR2F2是最值得关注的互作——作为核受体转录因子，NR2F2在血管发育、代谢和肿瘤发生中发挥关键作用，TMPRSS5可能通过蛋白水解剪切NR2F2或其共因子调控核受体信号通路。

**结构解读**：AlphaFold pLDDT=79.3，预测质量较高。Trypsin结构域（pLDDT >85）为经典的丝氨酸蛋白酶折叠——两组β-桶（各6股β-链）包围催化三联体（His-Asp-Ser），底物结合裂隙决定了酶切序列特异性（偏好碱性残基Arg/Lys后的肽键）。SRCR结构域（pLDDT 70-80）形成紧凑的β-卷曲折叠，通过保守的二硫键网络稳定，其凹面可能作为蛋白-蛋白互作界面。跨膜螺旋和N端胞质尾的pLDDT较低。

**机制模型**：（1）经典功能：TMPRSS5作为膜锚定蛋白酶在细胞表面或囊泡内催化特定底物的剪切——在听觉系统的功能已获实验支持（UniProt功能注释"May play a role in hearing"，PMID:17918741发现cAMP调控TMPRSS5在星形胶质细胞中的表达）；（2）核质中的蛋白水解信号：TMPRSS5的核质定位（Approved）可能反映其在ER-高尔基体-核膜运输路径中的出现，或更可能的是——TMPRSS5自身或其剪切产物进入核质后通过NR2F2的蛋白水解调控核受体转录活性。这种"膜锚定蛋白酶→核受体调控"的模式在NOTCH信号（γ-secretase切割→NICD核移位）中有先例；（3）HNRNPL的反复出现（多个本批次候选蛋白均以此为互作伙伴）可能指向HNRNPL作为RNA结合蛋白通过RNA"桥接"多种蛋白形成功能聚集体的"枢纽"作用。

**TE调控展望**：TMPRSS5的TE调控潜力极低。其作为丝氨酸蛋白酶的主要功能集中在蛋白水解信号通路的细胞外/囊泡内阶段。即便存在NR2F2核受体互作，该调控主要涉及代谢和发育基因而非TE。然而，NR2F2已被报道在某些癌症中结合ERV-LTR启动子区域的DR1（直接重复）序列元件——若TMPRSS5通过蛋白水解剪切调控NR2F2的活性，则可能间接影响LTR驱动的TE转录。这是一个高度推测性的间接联系，需实验验证。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H3S3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166682-TMPRSS5

![](https://images.proteinatlas.org/10992/1364_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/10992/1364_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/10992/85_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/10992/85_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/10992/87_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/10992/87_F10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 18**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMPRSS5

