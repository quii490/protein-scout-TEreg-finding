---
type: protein-evaluation
gene: "SLC6A9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC6A9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC6A9 |
| 蛋白名称 | Sodium- and chloride-dependent glycine transporter 1 |
| 蛋白大小 | 706 aa / 78.3 kDa |
| UniProt ID | P48067 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 706 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=47 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=81.1; PDB=9 |
| 调控结构域 | 4/10 | x2 | 8.0 | Na/ntran_symport; Na/ntran_symport_glycine_GLY1; SNS_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=15 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=47 broad=380
- AF pLDDT=81.1 PDB=9
- InterPro: Na/ntran_symport; Na/ntran_symport_glycine_GLY1; SNS_sf
- Pfam: SNF
- PPI degree=15 ChIP: None
36415754: Glycine encephalopathy. | 37777856: GWAS Meta-Analysis of Suicide Attempt: Identification of 12 Genome-Wide Signific | 35817773: Blocking glycine utilization inhibits multiple myeloma progression by disrupting

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sodium- and chloride-dependent glycine transporter 1

**功能**: Sodium- and chloride-dependent glycine transporter (PubMed:37962965, PubMed:8183239). Essential for regulating glycine concentrations at inhibitory glycinergic synapses

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000175 |
| InterPro | IPR003028 |
| InterPro | IPR037272 |
| Pfam | PF00209 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

SLC6A9（Sodium- and chloride-dependent glycine transporter 1），又名GlyT1，是神经递质钠同向转运体（NSS/LeuT折叠）家族的原型成员。结构域架构包括Na/ntran_symport（IPR000175）、Na/ntran_symport_glycine_GLY1（IPR003028）和SNS_sf（IPR037272），Pfam为SNF（PF00209）。706个氨基酸（78.3 kDa）、12次跨膜拓扑结构和LeuT折叠构成了其特征性的转运体结构——一个倒置重复的5+5跨膜螺旋束围绕中央的底物和离子结合位点。pLDDT=81.1的高置信度和9个PDB结构条目为GlyT1的结构-功能关系研究奠定了坚实基础。

GlyT1利用钠离子和氯离子的电化学梯度驱动甘氨酸的跨膜摄取。在CNS中，GlyT1主要表达于星形胶质细胞和谷氨酸能突触的突触前末端，通过快速清除突触间隙中的甘氨酸来终止抑制性甘氨酸能神经传递。甘氨酸同时是NMDA型谷氨酸受体的必须共激动剂，因此GlyT1也间接调控谷氨酸能兴奋性神经传递。这些功能使GlyT1成为精神分裂症、癫痫和慢性疼痛治疗中的重要药理学靶标——GlyT1抑制剂（如Iclepertin/BIT1）已在临床试验中。HPA免疫荧光显示Golgi apparatus; Nucleoplasm (Approved)——高尔基体定位与膜蛋白的生物合成和运输一致，但核质定位再次挑战了经典转运体模型。

PPI网络揭示了SLC6A9与核内蛋白的显著连接。STRING数据显示HMGN3（896分）是最高置信度的互作伙伴——HMGN3是HMGN家族的非组蛋白染色质结合蛋白，通过竞争性地与核小体结合来打开染色质结构，促进转录活化和DNA修复。这一核小体重塑因子与膜转运体的高置信度互作极为引人注目。BioGRID中STX1A（突触融合蛋白1A，SNARE复合体组分）和THOC2（THO复合体亚基2，参与mRNA出核）的互作分别将SLC6A9与突触囊泡释放和RNA核质运输联系起来。HRAS、RHOA和FASN的互作将转运蛋白纳入GTP酶信号和脂肪酸合成的调控网络。

从TE调控角度，SLC6A9的潜力主要通过甘氨酸代谢与一碳代谢/甲基化的交叉通路实现。甘氨酸是重要的甲基供体——通过甘氨酸裂解系统（GCS）转化为5,10-亚甲基四氢叶酸（5,10-MTHF），后者为S-腺苷甲硫氨酸（SAM）合成提供甲基基团。SAM是DNA甲基转移酶（DNMTs）和组蛋白甲基转移酶（HMTs）的通用甲基供体。因此，GlyT1通过调控细胞内甘氨酸可用度间接影响全基因组的DNA和组蛋白甲基化水平——而DNA甲基化是TE元件表观遗传沉默的核心机制。甘氨酸限制条件可能导致SAM耗竭、DNA低甲基化，进而引发逆转座子元件的去抑制和转录激活。

HMGN3-SLC6A9的高置信度互作进一步提示了甘氨酸代谢状态通过染色质结合蛋白直接反馈至染色质结构的机制。HMGN3通过打开染色质促进转录——在甘氨酸缺乏时，SLC6A9表达或活性下调可能通过HMGN3改变染色质开放性。SLC6A9的PubMed覆盖广泛（strict=47, broad=380），PPI degree=15的适中互作度，以及HMGN3和THOC2的核功能关联，均提示该蛋白可能通过代谢-表观遗传轴间接但广泛地影响TE元件的转录活性和基因组稳定性。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HMGN3 | STRING | 896 |
| STX1A | BioGRID | 1 |
| THOC2 | BioGRID | 1 |
| HRAS | BioGRID | 1 |
| FASN | BioGRID | 1 |
| RHOA | BioGRID | 1 |
| DTX2 | BioGRID | 1 |
| TMEM17 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P48067-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196517-SLC6A9

![](https://images.proteinatlas.org/13977/138_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196517-SLC6A9

![](https://images.proteinatlas.org/13977/138_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196517-SLC6A9

![](https://images.proteinatlas.org/13977/138_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/166_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13977/139_A7_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 380**

| 42289532 | Clinicopathological and molecular characterization of HPV-associated cervical poorly cohesive carcinoma: a rare aggressi | J Pathol Clin Res 2026 |
| 42153166 | Dendrobine inhibits the growth and invasion of human breast cancer cells by regulating the NF-κB signaling pathway via t | Cytotechnology 2026 |
| 42053463 | The Effect of Iclepertin on Hematological Parameters: An Overview of Nonclinical Studies and Clinical Trials in Healthy  | J Clin Pharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC6A9

