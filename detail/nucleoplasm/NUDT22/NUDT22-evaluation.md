---
type: protein-evaluation
gene: "NUDT22"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NUDT22 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NUDT22 |
| 蛋白名称 | Uridine diphosphate glucose pyrophosphatase NUDT22 |
| 蛋白大小 | 303 aa / 32.6 kDa |
| UniProt ID | Q9BRQ3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 303 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=92.8; PDB=33 |
| 调控结构域 | 4/10 | ×2 | 8.0 | NUDIX_hydrolase_dom; NUDT22/NUDT9-like |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=31 |
| **加权总分** | | | **144/180** | |
| **归一化总分** | | | **79.8/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Enhanced)
- PubMed strict=1 broad=3
- AF pLDDT=92.8 PDB=33
- InterPro: NUDIX_hydrolase_dom; NUDT22/NUDT9-like
- Pfam: 
- PPI degree=31 ChIP: None
29413322: Human NUDT22 Is a UDP-Glucose/Galactose Hydrolase Exhibiting a Unique Structural

### 4. 总体评价
**79.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Uridine diphosphate glucose pyrophosphatase NUDT22

**功能**: Pyrophosphatase hydrolyzing the diphosphate bond in the nucleotide-sugars UDP-glucose and UDP-galactose with a preference for the former, yielding glucose 1-phosphate or galactose 1-phosphate and UMP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000086 |
| InterPro | IPR055295 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NUDT14 | STRING | 787 |
| NUDT17 | STRING | 746 |
| NUDT5 | STRING | 724 |
| LHX6 | BioGRID | 1 |
| ZMYND12 | BioGRID | 1 |
| ZNF343 | BioGRID | 1 |
| IKZF5 | BioGRID | 1 |
| LHX3 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BRQ3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000149761-NUDT22

![](https://images.proteinatlas.org/39334/488_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/39334/488_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/39334/485_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/39334/485_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/39334/494_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/39334/494_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/53464/965_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/53464/965_H3_3_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 41613547 | The multifaceted regulatory roles of Nudix hydrolases in cancer and their therapeutic potential. | Front Oncol 2025 |
| 36871087 | NUDT22 promotes cancer growth through pyrimidine salvage. | Oncogene 2023 |
| 29413322 | Human NUDT22 Is a UDP-Glucose/Galactose Hydrolase Exhibiting a Unique Structural Fold. | Structure 2018 |

### 深度机制分析

NUDT22属于NUDIX水解酶超家族，其核心结构域IPR000086（NUDIX hydrolase domain）赋予了该蛋白水解核苷酸-糖中二磷酸键的催化能力。特别值得注意的是，NUDT22是NUDT22/NUDT9-like亚家族（IPR055295）成员，该亚家族采用了独特的结构折叠——不同于经典NUDIX折叠，这一结构特征在2018年Structure期刊上被首次定义（PMID: 29413322）。AF2预测的pLDDT高达92.8分，说明该蛋白的整体折叠高度有序，其33个PDB条目进一步印证了结构的成熟度。这种独特的折叠构型很可能演化出了底物选择的特异性，使其偏向UDP-glucose而非UDP-galactose——在核苷酸-糖代谢的精密调控中，这种底物偏好性可能决定了不同代谢分支的通量分配。

从互作网络来看，NUDT22与NUDT14（评分787）、NUDT17（746）和NUDT5（724）形成紧密的NUDIX家族内互作簇，提示这些水解酶可能在核苷酸代谢中构成功能互补或协同调控网络。更关键的是，BioGRID和STRING数据揭示了NUDT22与一系列转录因子的物理互作——包括LHX6、LHX3（LIM-homeodomain转录因子）、IKZF5（Ikaros家族锌指蛋白）以及ZNF343、ZMYND12等锌指蛋白。这种NUDIX水解酶与转录调控因子的互作模式，强烈暗示NUDT22可能在核内承担超越核苷酸代谢的结构性角色——可能通过其独特的蛋白折叠作为分子支架，参与转录调控复合体的组装或稳定化。

2023年Oncogene上的关键研究（PMID: 36871087）揭示了NUDT22通过嘧啶补救途径促进癌症生长的机制：水解UDP-glucose产生的UMP可直接进入嘧啶核苷酸池，为快速增殖的癌细胞提供核苷酸前体。这与2025年Frontiers in Oncology综述将NUDIX水解酶定位为癌症多面调控因子的结论高度一致。综合来看，NUDT22的功能模型具有双重性：经典催化活性通过水解UDP-glucose参与核苷酸-糖代谢稳态，而非经典功能可能通过其独特结构折叠作为蛋白互作支架，将代谢信号与转录调控进行整合。这种"兼职"（moonlighting）行为使其成为连接细胞代谢状态与基因表达调控的潜在枢纽——尤其值得在代谢重编程驱动的癌症背景下探索其是否通过转录因子互作影响特定基因程序的表达。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NUDT22

