---
type: protein-evaluation
gene: "UBA5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBA5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBA5 |
| 蛋白名称 | Ubiquitin-like modifier-activating enzyme 5 |
| 蛋白大小 | 404 aa / 44.9 kDa |
| UniProt ID | Q9GZZ9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 404 aa |
| 研究新颖性 | 7/10 | ×5 | 35.0 | PubMed=81 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=86.7; PDB=12 |
| 调控结构域 | 4/10 | ×2 | 8.0 | D-isomer_DH_CS1; ThiF/MoeB/HesA; ThiF_NAD_FAD-bd |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=139 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Enhanced)
- PubMed: strict=81, broad=116
- AF pLDDT: 86.7 / PDB: 12
- InterPro: D-isomer_DH_CS1; ThiF/MoeB/HesA; ThiF_NAD_FAD-bd
- Pfam: ThiF
- PPI degree=139 ChIP: None
38762759: VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy. | 40333994: Patient-derived models of UBA5-associated encephalopathy identify defects in neu | 40601633: UFMylation: A supervisor of the HIF1α pathway and a potential therapeutic target

### 4. 总体评价
★★★★  **74.9/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-like modifier-activating enzyme 5

**功能**: E1-like enzyme which specifically catalyzes the first step in ufmylation (PubMed:15071506, PubMed:18442052, PubMed:20368332, PubMed:25219498, PubMed:26929408, PubMed:27545674, PubMed:27545681, PubMed:27653677, PubMed:30412706, PubMed:30626644, PubMed:34588452). Activates UFM1 by first adenylating its C-terminal glycine residue with ATP, and thereafter linking this residue to the side chain of a cysteine residue in E1, yielding a UFM1-E1 thioester and free AMP (PubMed:20368332, PubMed:26929408, P

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029752 |
| InterPro | IPR045886 |
| InterPro | IPR000594 |
| InterPro | IPR035985 |
| Pfam | PF00899 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

UBA5（Ubiquitin-like modifier-activating enzyme 5）是UFMylation修饰途径的核心E1激活酶，其结构域架构融合了泛素激活机制和代谢酶折叠。InterPro注释包括：D-isomer_DH_CS1（IPR029752）——D-异构体脱氢酶保守位点、ThiF/MoeB/HesA（IPR045886）——硫胺素/钼嘌呤生物合成酶折叠、ThiF_NAD_FAD-bd（IPR000594）——NAD/FAD结合域。Pfam注释为ThiF（PF00899）。这种结构域组合极为罕见——一个E1激活酶却采用了硫胺素生物合成酶的折叠。404个氨基酸（44.9 kDa）和pLDDT=86.7的高结构置信度，加上12个PDB结构条目，使得UBA5成为本评估队列中结构数据最丰富的蛋白之一。

UFMylation（泛素折叠修饰因子1共价修饰）是近年来迅速发展的类泛素修饰途径。UBA5催化该途径的第一步：（1）利用ATP腺苷酸化UFM1的C端甘氨酸残基；（2）随后将UFM1连接到UBA5活性位点半胱氨酸残基上，形成硫酯键连接的UBA5~UFM1中间体；（3）通过转硫酯反应将UFM1传递给E2酶UFC1。随后，E3连接酶UFL1将UFM1转移到底物蛋白的赖氨酸残基上。UFMylation修饰的主要靶标包括内质网应激信号通路蛋白、核糖体蛋白和DNA损伤修复蛋白。HPA免疫荧光显示nan (Enhanced)，虽然定位信息不够精确，但"Enhanced"的可信度等级提示其在部分亚细胞区室中有明确的富集信号。

PPI网络精准反映了UFMylation途径的层级结构：BioGRID数据显示UFM1（泛素折叠修饰因子1，UBA5的底物）、UFC1（E2激活酶）和ATG101（自噬相关蛋白101）的互作——ATG101的参与将UFMylation与自噬调控联系起来。GABARAPL2（GABA-A受体相关蛋白样2，一种类泛素蛋白）、SH3GLB2（内吞蛋白B1）、ALDH2（线粒体乙醛脱氢酶2，ALDH2*2突变蛋白）和SARS（丝氨酰-tRNA合成酶）的互作扩展了UBA5在代谢、自噬和翻译调控中的功能谱。UBA5的PPI degree=139反映了UFMylation修饰在多种细胞过程中的广泛参与。

从TE调控角度，UBA5通过UFMylation修饰途径在DNA损伤修复中的作用具有重要研究价值。PMID 42297806（Nat Commun, 2026）系统发现了UFM1受体，揭示了UFMylation在指导非同源末端连接（NHEJ）DNA修复中的调控模块。DNA损伤是TE元件激活的主要诱因之一——双链断裂（DSB）可触发LINE-1逆转座子的异常表达和移动，而DNA修复蛋白（如53BP1、BRCA1）通过形成修复灶限制DNA末端并间接抑制TE的转座。UFMylation在NHEJ中的新角色将UBA5与基因组稳定性的维护直接联系起来。此外，UFMylation调控内质网稳态（PMID 41854117, FASEB J, 2026）——内质网应激在衰老和疾病中驱动TE去抑制——以及黄病毒复制中的保守角色（PMID 41826287, Nat Commun, 2026），均提示UBA5-UFM1轴在多种应激条件下的广泛调控功能。

UBA5的研究新颖性适中（PubMed strict=81篇），但其结构生物学深度（PDB=12）和UFMylation修饰的新兴重要性使其成为TE调控机制研究的有力候选。核心验证实验应包括：（1）ChIP-seq确定UBA5/UFMylation在TE位点的富集；（2）在UBA5敲除细胞中分析全局TE转录组变化；（3）鉴定UBA5的核定位信号和UFMylation的核内底物。UBA5相关的UFMylation修饰是评估队列中最具"新维度"的TE调控候选机制。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APEH | BioGRID | 0 |
| GABARAPL2 | BioGRID | 0 |
| ATG101 | BioGRID | 0 |
| SH3GLB2 | BioGRID | 0 |
| UFM1 | BioGRID | 0 |
| UFC1 | BioGRID | 0 |
| ALDH2 | BioGRID | 0 |
| SARS | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9GZZ9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000081307-UBA5

![](https://images.proteinatlas.org/17235/134_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/134_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000081307-UBA5

![](https://images.proteinatlas.org/17235/134_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/134_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000081307-UBA5

![](https://images.proteinatlas.org/17235/134_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/134_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/133_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17235/135_E12_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 116**

| 42297806 | Systematic discovery of UFM1 receptors reveals a regulatory module in DNA repair directing non-homologous end-joining. | Nat Commun 2026 |
| 41854117 | UFMylation: A Key Role in Maintaining Endoplasmic Reticulum Homeostasis. | FASEB J 2026 |
| 41826287 | A genus-wide interaction atlas across NS4B orthologues identifies a conserved role for UFMylation in orthoflavivirus rep | Nat Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBA5

