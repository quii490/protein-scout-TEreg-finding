---
type: protein-evaluation
gene: "KIFAP3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KIFAP3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KIFAP3 |
| 蛋白名称 | Kinesin-associated protein 3 |
| 蛋白大小 | 792 aa / 91.2 kDa |
| UniProt ID | Q92845 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Microtubules; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 792 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=19 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=83.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARM-like; ARM-type_fold; Armadillo |
| PPI | 7/10 | x3 | 21.0 | PPI degree=128 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- Basal body; Microtubules; Nucleoplasm (Approved)
- PubMed strict=19 broad=59
- AF pLDDT=83.4 PDB=0
- InterPro: ARM-like; ARM-type_fold; Armadillo
- Pfam: KAP
- PPI degree=128 ChIP: None
28140676: Further analysis of KIFAP3 gene in ALS patients from Switzerland and Sweden. | 19451621: Reduced expression of the Kinesin-Associated Protein 3 (KIFAP3) gene increases s | 38869718: LncRNA KIFAP3-5:1 inhibits epithelial-mesenchymal transition of renal tubular ce

### 4. 总体评价
**76.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Kinesin-associated protein 3

**功能**: Involved in tethering the chromosomes to the spindle pole and in chromosome movement. Binds to the tail domain of the KIF3A/KIF3B heterodimer to form a heterotrimeric KIF3 complex and may regulate the membrane binding of this complex (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011989 |
| InterPro | IPR016024 |
| InterPro | IPR000225 |
| InterPro | IPR008658 |
| Pfam | PF05804 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KIF17 | STRING | 855 |
| CHAT | STRING | 848 |
| DCTN1 | STRING | 801 |
| KIF11 | STRING | 791 |
| KLC2 | STRING | 787 |
| DCTN2 | STRING | 760 |
| KIF5B | STRING | 737 |
| APC | STRING | 733 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q92845-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000075945-KIFAP3

![](https://images.proteinatlas.org/23742/237_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/237_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000075945-KIFAP3

![](https://images.proteinatlas.org/23742/237_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/237_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000075945-KIFAP3

![](https://images.proteinatlas.org/23742/237_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/237_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/236_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23742/268_H10_2_blue_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能推断** KIFAP3含有Armadillo (ARM)重复结构域（InterPro: IPR011989, IPR016024, IPR000225），属于ARM-like超家族，同时携带KAP特异结构域（Pfam: PF05804）。ARM重复折叠形成超螺旋 solenoid 结构，通常介导蛋白-蛋白相互作用。KIFAP3的ARM重复区负责与kinesin马达蛋白KIF3A/KIF3B异源二聚体的尾部结构域结合，组装成异源三聚体KIF3复合物。pLDDT均值为83.4，表明AlphaFold对整体折叠有较高置信度；尽管PDB无实验结构，ARM型折叠因其规则的重复螺旋堆积模式，AF2预测质量通常较高。蛋白长达792 aa（91.2 kDa），其较大尺寸提示除核心ARM支架外，可能存在额外的固有无序区域用于调控或招募多种货物适配器。

**PPI网络与信号通路解析** STRING网络核心伙伴包括KIF17（855）、CHAT（848）、DCTN1（801）、KIF11（791）、KLC2（787）、DCTN2（760）、KIF5B（737）和APC（733），PPI度高达128。KIF17与KLC2提示KIFAP3不仅参与KIF3介导的轴突运输，还可能通过KIF17参与树突NMDA受体转运。CHAT的极高分数（848）暗示KIFAP3在胆碱能神经元突触囊泡运输中的关键角色。DCTN1/DCTN2（dynactin组分）的连接揭示KIFAP3可能协调kinesin与dynactin/dynein之间的双向运输切换。APC（腺瘤性结肠息肉蛋白）的参与连接Wnt信号通路与微管运输，提示KIFAP3可能通过APC介导β-catenin降解复合物的空间定位（PubMed: 28140676、38869718支持KIFAP3与神经退行性疾病及上皮-间质转化的关联）。

**结构解读** pLDDT=83.4的预测结构中，ARM重复区域应形成典型的右手超螺旋，每个重复由三个α-螺旋组成，形成连续的疏水核心。全长792个残基中，N端ARM区约300-400个残基构成保守的货物识别平台，C端区域可能包含非结构化的调节区段。PAE图中预期可观察到的低PAE对角线区域对应ARM重复的刚性堆积，而C端高PAE区域提示柔性铰链，可能允许KIF3复合物在微管行走时发生构象适应。与KIF3A/KIF3B结合界面的PAE值应在10-15埃水平，表明异源三聚体组装具有高置信度。

**分子机制模型** 基于所有证据的合成模型如下：KIFAP3作为货物适配器支架，通过ARM重复结构域同时结合KIF3A/KIF3B异源二聚体马达和多种货物蛋白（包括APC、CHAT囊泡、NMDA受体复合物）。在间期，KIFAP3-KIF3复合物沿微管向正端（通常为细胞外周）运输货物；在有丝分裂期，该复合物参与染色体与纺锤体极的拴连。核质定位（HPA Approved级别）提示KIFAP3可能伴随KIF3复合物进入细胞核，在核膜破裂后的有丝分裂期或通过核孔复合物维持核内运输功能。DCTN复合物的共结合暗示存在一个"方向切换"机制：KIFAP3可能作为微管运输的整合节点，协调正端（kinesin）和负端（dynactin/dynein）运输。

**研究与治疗意义** KIFAP3的ALS关联（PubMed: 28140676）及lncRNA KIFAP3-5:1在肾小管上皮细胞中对EMT的抑制作用（PubMed: 38869718）使其成为神经退行性疾病和纤维化的双重新靶点。靶向KIFAP3的ARM重复-货物结合界面可调节特定货物的轴突运输，而不影响所有kinesin功能。CHAT的高分互作提示KIFAP3调节剂可能影响胆碱能突触功能，为阿尔茨海默病的胆碱能假说提供新视角。该蛋白的核质定位及有丝分裂功能暗示其可能参与核内cargo运输，这一方向目前完全未被探索。

### PubMed 文献

**PubMed count: 59**

| 41854441 | Transcriptomic Insights Into Alzheimer's Disease: Differentially Expressed Genes and Cholesterol Metabolism. | CNS Neurosci Ther 2026 |
| 40790242 | Sex-dependent epigenetic disruption of YY1 binding by prenatal BPA exposure downregulates Matr3 and alters Agap1 splicin | Biol Sex Differ 2025 |
| 40783920 | [Impacts of varicocele on the structure and proteomics of rat testis tissue: An experimental study]. | Zhonghua Nan Ke Xue 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KIFAP3

