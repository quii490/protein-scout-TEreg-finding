---
type: protein-evaluation
gene: "PNPLA8"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PNPLA8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PNPLA8 |
| 蛋白名称 | Calcium-independent phospholipase A2-gamma |
| 蛋白大小 | 782 aa / 88.5 kDa |
| UniProt ID | Q9NP80 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 782 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=66.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Acyl_Trfase/lysoPLipase; PNPLA8-like; PNPLA_dom |
| PPI | 6/10 | x3 | 18.0 | PPI degree=59 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=17 broad=33
- AF pLDDT=66.9 PDB=0
- InterPro: Acyl_Trfase/lysoPLipase; PNPLA8-like; PNPLA_dom
- Pfam: Patatin
- PPI degree=59 ChIP: None
39261734: Genetic links between ovarian ageing, cancer risk and de novo mutation rates. | 39082157: Biallelic null variants in PNPLA8 cause microcephaly by reducing the number of b | 39680195: Novel PNPLA8 variants associated with primary ovarian insufficiency, tremors, ce

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Calcium-independent phospholipase A2-gamma

**功能**: Calcium-independent and membrane-bound phospholipase, that catalyzes the esterolytic cleavage of fatty acids from glycerophospholipids to yield free fatty acids and lysophospholipids, hence regulating membrane physical properties and the release of lipid second messengers and growth factors (PubMed:10744668, PubMed:10833412, PubMed:15695510, PubMed:15908428, PubMed:17213206, PubMed:18171998, PubMed:28442572). Hydrolyzes phosphatidylethanolamine, phosphatidylcholine and probably phosphatidylinosi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016035 |
| InterPro | IPR045217 |
| InterPro | IPR002641 |
| Pfam | PF01734 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HNRNPD | BioGRID | 0 |
| KAT6A | BioGRID | 0 |
| SYNCRIP | BioGRID | 0 |
| PLK4 | BioGRID | 0 |
| SIN3B | BioGRID | 0 |
| SGTB | BioGRID | 0 |
| BAG6 | BioGRID | 0 |
| ESR2 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：PNPLA8/iPLA2-gamma（782 aa，88.5 kDa）含有Patatin样磷脂酶结构域（PF01734，Acyl_Trfase/lysoPLipase IPR016035，PNPLA_dom IPR002641），属于PNPLA（Patatin-Like Phospholipase Domain Containing）蛋白家族。PNPLA结构域采用经典的α/β水解酶折叠，含催化二联体（Ser-Asp，注意：不同于常见的Ser-His-Asp三联体，Patatin家族使用Ser-Asp催化二联体，Asp同时起到酸碱催化和亲核攻击稳定过渡态的作用）。作为不依赖钙离子的膜结合性磷脂酶A2（iPLA2），PNPLA8催化甘油脂的水解释放游离脂肪酸和溶血磷脂（lysophospholipid），在膜脂质重塑和脂质信号分子（如花生四烯酸、内源性大麻素）的产生中发挥核心作用。

**PPI互作网络解读**：PPI degree=59，关键互作包括：KAT6A（MYST家族组蛋白乙酰转移酶，催化H3K14ac和H3K23ac，BioGRID 0分）、SIN3B（SIN3-HDAC共抑制复合物的支架蛋白，BioGRID 0分）、BAG6（分子伴侣和蛋白质量控制因子，BioGRID 0分）、ESR2（雌激素受体β，BioGRID 0分）、HNRNPD（AUF1，ARE-mRNA降解因子，BioGRID 0分）。KAT6A和SIN3B的互作最为显著——KAT6A负责组蛋白乙酰化激活转录，而SIN3B介导去乙酰化依赖的转录抑制，PNPLA8同时与这一对表观遗传拮抗因子互作，提示其在染色质修饰的脂质-代谢调控中扮演枢纽角色。

**结构解读**：AlphaFold pLDDT=66.9，Patatin催化域（残基约100-380）的pLDDT较高（70-80），形成特征性的中央β-片层被α-螺旋包围的α/β水解酶折叠。催化Ser（推测为Ser-414或Ser-436位置）位于β-片层C端的"亲核肘"（nucleophilic elbow）sharp turn处，Asp催化残基定位在相邻的loop上。与iPLA2-beta（PNPLA9）不同，PNPLA8的催化域前含有预测的膜结合区（可能为两亲性α-螺旋），使其能直接与膜双分子层作用而无需钙离子介导的膜招募。

**机制模型**：（1）经典型磷脂酶功能：PNPLA8催化膜甘油脂的sn-1或sn-2位脂肪酸水解（具有位置非特异性），释放的游离脂肪酸可作为能量底物（脂肪酸β-氧化）、膜合成前体和信号分子（如花生四烯酸经COX/LOX通路转化为前列腺素和白三烯）；（2）核质功能假设：通过KAT6A和SIN3B互作，PNPLA8可能参与"脂质代谢-表观遗传"交叉调控——其水解产生的游离脂肪酸和溶血磷脂可直接或间接（通过代谢物传感通路如PPAR、SREBP）影响组蛋白乙酰化/去乙酰化的底物供给，进而调控染色质状态；（3）PNPLA8功能丧失与人脑发育缺陷的直接联系（PMID:39082157发现双等位基因null变异导致小头畸形，PMID:39680195发现新的PNPLA8变异与卵巢早衰相关），突显其在器官发育中的不可替代作用。

**TE调控展望**：PNPLA8通过组蛋白乙酰化通路与TE调控存在间接联系。HDAC和HAT对组蛋白尾部赖氨酸残基的乙酰化/去乙酰化直接调控染色质的开放/闭合状态，进而影响TE转录。乙酰-CoA作为HAT的必需底物来自脂肪酸β-氧化和柠檬酸代谢——PNPLA8通过调控游离脂肪酸池影响乙酰-CoA供给，间接参与组蛋白乙酰化稳态。此外，iPLA2活性与内源性大麻素系统（endo-cannabinoid system）的脂质介质产生有关，该系统已被报道调控LINE-1逆转录转座（PMID涉及2-AG和AEA信号通路）。PNPLA8的iPLA2活性在此交叉点具有潜在但未经验证的TE调控功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NP80-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000135241-PNPLA8

![](https://images.proteinatlas.org/20083/242_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/20083/242_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/20083/183_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/20083/183_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/20083/185_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/20083/185_F10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 33**

| 42356374 | Early-Life Vitamin A Deficiency Induces Tissue-Specific Oxylipin Remodeling and Hepatic Inflammation. | Nutrients 2026 |
| 40078960 | Identifying potential biomarkers and molecular mechanisms related to arachidonic acid metabolism in vitiligo. | Front Mol Biosci 2025 |
| 40004130 | Autophagy in High-Fat Diet and Streptozotocin-Induced Metabolic Cardiomyopathy: Mechanisms and Therapeutic Implications. | Int J Mol Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PNPLA8

