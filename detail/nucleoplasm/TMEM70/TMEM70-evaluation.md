---
type: protein-evaluation
gene: "TMEM70"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM70 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM70 |
| 蛋白名称 | Transmembrane protein 70, mitochondrial |
| 蛋白大小 | 260 aa / 29.0 kDa |
| UniProt ID | Q9BUB7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 260 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=41 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=72.3; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | TMEM70; TMEM70/TMEM186/TMEM223 |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=228 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Supported)
- PubMed strict=41 broad=65
- AF pLDDT=72.3 PDB=0
- InterPro: TMEM70; TMEM70/TMEM186/TMEM223
- Pfam: TMEM70
- PPI degree=228 ChIP: None
20937241: Expression and processing of the TMEM70 protein. | 32275929: TMEM70 functions in the assembly of complexes I and V. | 24576557: Mitochondrial membrane assembly of TMEM70 protein.

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 70, mitochondrial

**功能**: Scaffold protein that participates in the c-ring assembly of mitochondrial ATP synthase (F(1)F(0) ATP synthase or complex V) by facilitating the membrane insertion and oligomer formation of the subunit c/ATP5MC1 through its interaction (PubMed:31652072, PubMed:32275929, PubMed:33359711, PubMed:33753518). Therefore, participates in the early stage of mitochondrial ATP synthase biogenesis and also protects subunit c/ATP5MC1 against intramitochondrial proteolysis (PubMed:18953340, PubMed:20937241, 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009724 |
| InterPro | IPR045325 |
| Pfam | PF06979 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

TMEM70（Transmembrane protein 70, mitochondrial，UniProt: Q9BUB7，260 aa / 29.0 kDa）的结构域架构分析显示：InterPro结构域包括IPR009724, IPR045325；Pfam注释为PF06979。 AlphaFold预测的pLDDT均值为72.3，整体结构置信度中等，部分区域可能为内在无序区，需要注意其构象柔性对功能的影响。

蛋白质互作网络分析揭示TMEM70与以下关键因子存在相互作用：RAF1、C15ORF48、DUSP23、CHDH、RTN1（PPI度为228）。 功能注释显示Scaffold protein that participates in the c-ring assembly of mitochondrial ATP synthase (F(1)F(0) ATP synthase or complex V) by facilitating the membrane insertion and oligomer formation of the subuni。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，TMEM70的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.9/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，TMEM70的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得41篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42289879, 42195294, 41998594等。

综上所述，TMEM70作为一个260 aa / 29.0 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=72.3的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RAF1 | BioGRID | 1 |
| C15ORF48 | BioGRID | 1 |
| DUSP23 | BioGRID | 1 |
| CHDH | BioGRID | 1 |
| RTN1 | BioGRID | 1 |
| NARS2 | BioGRID | 1 |
| CPT2 | BioGRID | 1 |
| DHRS4 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BUB7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000175606-TMEM70

![](https://images.proteinatlas.org/23187/985_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/985_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000175606-TMEM70

![](https://images.proteinatlas.org/23187/985_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/985_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000175606-TMEM70

![](https://images.proteinatlas.org/23187/985_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/985_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/958_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23187/982_G12_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 65**

| 42289879 | Distinct causal associations of mitochondrial function-related proteins with eclampsia versus pre-eclampsia: a two-sampl | J Matern Fetal Neonatal Med 2026 |
| 42195294 | Rare Genetic Diseases with Founder Effect in Roma Children. | Life (Basel) 2026 |
| 41998594 | TMEM70 drives breast cancer progression via mitochondrial oxidative phosphorylation and microenvironment remodeling. | Cancer Cell Int 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM70

